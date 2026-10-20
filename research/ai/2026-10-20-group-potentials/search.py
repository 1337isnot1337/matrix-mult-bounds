"""Bounded SAT search with exact Farkas cuts; discovery, not an exclusion.

Optional discovery dependencies: numpy, scipy, python-sat, sympy.
Independent acceptance is in group_exact.py and uses only integers.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from itertools import combinations,permutations,product
import json
from math import gcd,lcm
from pathlib import Path
import random
import threading
import time

import numpy as np
from scipy.optimize import linprog
from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose4,Cadical195

from group_exact import group,affine_group,borel_anchor_certificate,extra_relations,verify_witness,verify_farkas
from abelian_tables import normal_tables
from symmetry_cnf import lex_geq


def integerize(values):
    values = [v if isinstance(v,Fraction) else Fraction(float(v)).limit_denominator(10**8)
              for v in values]
    denominator = lcm(*(v.denominator for v in values))
    numbers = [int(v*denominator) for v in values]
    common = reduce(gcd,numbers)
    return [n//common for n in numbers] if common else numbers


def potential_or_circuit(relations, width):
    if not relations: return {'potentials':[0]*width}
    lookup = {tuple(r['row']):i for i,r in enumerate(relations)}
    for i,r in enumerate(relations):
        j=lookup.get(tuple(-v for v in r['row']))
        if j is not None: return {'indices':[i,j],'weights':[1,1]}
    R=np.array([r['row'] for r in relations],dtype=float)
    feasible=linprog(np.zeros(width),A_ub=-R,b_ub=-np.ones(len(R)),
                     bounds=[(None,None)]*width,method='highs')
    if feasible.success:
        weights=integerize(feasible.x)
        if not all(sum(a*b for a,b in zip(r['row'],weights))>0 for r in relations):
            raise ArithmeticError('floating LP did not yield an exact potential')
        return {'potentials':weights}
    if feasible.status != 2:
        raise RuntimeError(f'LP unresolved: {feasible.message}')
    alternative=linprog(np.zeros(len(R)),A_eq=np.vstack([R.T,np.ones(len(R))]),
                        b_eq=np.r_[np.zeros(width),1],bounds=(0,None),method='highs')
    if not alternative.success: raise RuntimeError('Farkas discovery LP unresolved')
    indices=[i for i,x in enumerate(alternative.x) if x>1e-8]
    weights=integerize(alternative.x[indices])
    if not verify_farkas(relations,indices,weights):
        import sympy as sp
        matrix=sp.Matrix([[relations[i]['row'][j] for i in indices] for j in range(width)])
        basis=matrix.nullspace()
        if len(basis)!=1: raise ArithmeticError('nonunique exact circuit needs recovery')
        vals=list(basis[0])
        if all(v<0 for v in vals): vals=[-v for v in vals]
        weights=integerize([Fraction(int(v.p),int(v.q)) for v in vals])
        if not verify_farkas(relations,indices,weights):
            raise ArithmeticError('no exact positive Farkas circuit recovered')
    return {'indices':indices,'weights':weights}


def build_solver(G,shape,seed,engine='glucose4',sl2_anchor=None,right_lex=False):
    pool=IDPool()
    N=len(G['matrices'])
    members=[[pool.id(('member',f,g)) for g in range(N)] for f in range(3)]
    reps=sorted({min(g,G['inv'][g]) for g in range(1,N)})
    owners=[{g:pool.id(('owner',f,g)) for g in reps} for f in range(3)]
    clauses=[]
    for f in range(3):
        clauses.append([members[f][0]])
        clauses.extend(CardEnc.equals(members[f],shape[f],vpool=pool,
                                     encoding=EncType.seqcounter).clauses)
        for g,h in combinations(range(N),2):
            q=G['mul'][g][G['inv'][h]]
            q=min(q,G['inv'][q])
            clauses.append([-members[f][g],-members[f][h],owners[f][q]])
    coset_normalization=None;borel_normalization=None
    if 'index' in G:
        r=G['index'];p=G['p']
        lower=[(size+r-1)//r for size in shape]
        if lower[0]*lower[1]*lower[2]>p:
            clauses.append([])
            coset_normalization={'excluded_by_ceiling_product':lower,'subgroup_order':p}
        else:
            fibers={a:[g for g,x in enumerate(G['matrices']) if x[0]==a]
                    for a in {x[0] for x in G['matrices']}}
            upper=[p//(lower[(f+1)%3]*lower[(f+2)%3]) for f in range(3)]
            for f in range(3):
                clauses.extend(CardEnc.atleast([members[f][g] for g in fibers[1]],
                    lower[f],vpool=pool,encoding=EncType.seqcounter).clauses)
                for fiber in fibers.values():
                    if upper[f]<len(fiber):
                        clauses.extend(CardEnc.atmost([members[f][g] for g in fiber],
                            upper[f],vpool=pool,encoding=EncType.seqcounter).clauses)
            # Normalize the largest coset into the identity fiber, record its
            # exact size, and apply the product bound to those actual maxima.
            ranges=[list(range(lower[f],min(upper[f],shape[f])+1)) for f in range(3)]
            selectors=[{k:pool.id(('fiber-maximum',f,k)) for k in ranges[f]} for f in range(3)]
            for f in range(3):
                clauses.extend(CardEnc.equals(list(selectors[f].values()),1,
                              vpool=pool,encoding=EncType.seqcounter).clauses)
                for k,selector in selectors[f].items():
                    exact=CardEnc.equals([members[f][g] for g in fibers[1]],k,
                                         vpool=pool,encoding=EncType.seqcounter)
                    clauses.extend([[-selector,*clause] for clause in exact.clauses])
                    for a,fiber in fibers.items():
                        if a==1:continue
                        maximum=CardEnc.atmost([members[f][g] for g in fiber],k,
                                              vpool=pool,encoding=EncType.seqcounter)
                        clauses.extend([[-selector,*clause] for clause in maximum.clauses])
                # A closest pair on a cyclic fiber can be translated to 0,t
                # with 1<=t<=floor(p/lower). Keep this translation normalization.
                if lower[f]>=2:
                    clauses.append([members[f][G['matrices'].index((1,t,0,1))]
                                    for t in range(1,p//lower[f]+1)])
            table_entries=0;table_cases=0
            for sizes in product(*ranges):
                forbidden=(any(shape[f]==shape[h] and sizes[f]>sizes[h]
                               for f,h in combinations(range(3),2)))
                if (sizes[0]*sizes[1]*sizes[2]>p or
                    forbidden or
                    (shape[0]==shape[1]==shape[2] and
                     sizes!=min(sizes,sizes[1:]+sizes[:1],sizes[2:]+sizes[:2]))):
                    clauses.append([-selectors[f][sizes[f]] for f in range(3)])
                    continue
                if p<=53 and sizes[0]<=3 and max(sizes)<=5:
                    rows=normal_tables(p,*sizes)
                    table_cases+=1;table_entries+=len(rows)
                    row_selectors=[]
                    for rowid,row in enumerate(rows):
                        selected=pool.id(('normal-table',sizes,rowid))
                        row_selectors.append(selected)
                        for f in range(3):
                            clauses.append([-selected,selectors[f][sizes[f]]])
                            for t in row[f]:
                                clauses.append([-selected,members[f][G['matrices'].index((1,t,0,1))]])
                    clauses.append([-selectors[f][sizes[f]] for f in range(3)]+row_selectors)
            anchor=None
            if shape[0]>r:
                anchor=G['matrices'].index((1,1,0,1))
                clauses.append([members[0][anchor]])
            # Translation conjugation fixes every pure translation. If S has
            # any element of nonidentity scale, normalize one such element's
            # translation coordinate to zero using the remaining automorphism.
            pure_multipliers=[members[0][G['matrices'].index((a,0,0,1))]
                              for a in fibers if a!=1]
            for g,x in enumerate(G['matrices']):
                if x[0]!=1:clauses.append([-members[0][g],*pure_multipliers])
            coset_normalization={'subgroup_order':p,'index':r,
                 'identity_fiber_lower':lower,'all_fibers_upper':upper,
                 'first_set_translation_one_anchor':anchor,
                 'identity_fiber_is_maximum':True,
                 'cyclic_maximum_tuple_normalization':shape[0]==shape[1]==shape[2],
                 'equal_shape_maxima_sorted':True,
                 'complete_normal_table_cases':table_cases,
                 'complete_normal_table_rows':table_entries,
                 'justification':'independent right translations, normal-translation '
                   'coset ceiling bound, and simultaneous translation-coordinate scaling'}
    elif G['name']=='SL(2,5)':
        cert=borel_anchor_certificate(G)
        lower=[(size+cert['index']-1)//cert['index'] for size in shape]
        for f in range(3):
            clauses.extend(CardEnc.atleast([members[f][g] for g in cert['members']],
                lower[f],vpool=pool,encoding=EncType.seqcounter).clauses)
        if shape[0]>cert['index']:
            clauses.append([members[0][g] for g in cert['anchors']])
        chosen_anchor=None
        if sl2_anchor is not None:
            names=['central','unipotent','negative-unipotent','order4']
            chosen_anchor=cert['anchors'][names.index(sl2_anchor)]
            clauses.append([members[0][chosen_anchor]])
        lex_start=len(clauses)
        if right_lex:
            cosets={}
            for h in range(N):
                cosets[h]={G['mul'][g][h] for g in cert['members']}
            for f in range(3):
                if f==0 and chosen_anchor is None:continue
                if lower[f]>2:continue
                for h in range(1,N):
                    if f==0:
                        other=G['mul'][chosen_anchor][h]
                        guard=pool.id(('right-eligible',f,h))
                        clauses.extend([[-guard,members[f][h]],[-guard,members[f][other]],
                                        [-members[f][h],-members[f][other],guard]])
                    elif lower[f]==1:
                        guard=members[f][h]
                    else:
                        guard=pool.id(('right-eligible',f,h))
                        others=[members[f][g] for g in cosets[h] if g!=h]
                        clauses.extend([[-guard,members[f][h]],[-guard,*others]])
                        clauses.extend([[-members[f][h],-x,guard] for x in others])
                    translated=[members[f][G['mul'][g][h]] for g in range(N)]
                    clauses.extend(lex_geq(members[f],translated,guard,
                                          lambda:pool.id()))
        borel_normalization={'order':cert['order'],'index':cert['index'],
             'identity_coset_lower':lower,
             'first_set_anchor_disjunction':cert['anchors'] if shape[0]>cert['index'] else [],
             'quotient_orbits_verified':len(cert['quotient_orbit_witnesses']),
             'anchor_branch':sl2_anchor,
             'right_translation_lex_leaders':right_lex,
             'lex_leader_clauses':len(clauses)-lex_start}
    for q in reps:
        for f,h in combinations(range(3),2):
            clauses.append([-owners[f][q],-owners[h][q]])
    # If qS=qT*qU and qT,qU commute, the forward and reversed extra
    # products have opposite potential rows. Such a trade is impossible.
    # Expressing this in quotient owners closes its entire translation orbit.
    commuting_cuts=set()
    for x in range(1,N):
        for y in range(1,N):
            z=G['mul'][x][y]
            if z==0 or z!=G['mul'][y][x]: continue
            qx,qy,qz=(min(v,G['inv'][v]) for v in (x,y,z))
            for fs,ft,fu in permutations(range(3)):
                commuting_cuts.add(tuple(sorted((-owners[fs][qz],
                                                  -owners[ft][qx],
                                                  -owners[fu][qy]))))
    clauses.extend(sorted(commuting_cuts))
    rng=random.Random(seed)
    rng.shuffle(clauses)
    solver_type=Cadical195 if engine=='cadical195' else Glucose4
    solver=solver_type(bootstrap_with=clauses,use_timer=True)
    solver.set_phases([v if rng.randrange(2) else -v for row in members for v in row])
    return solver,members,{'variables':pool.top,'clauses':len(clauses),
                           'inverse_classes':len(reps),'commuting_trade_cuts':len(commuting_cuts),
                           'coset_normalization':coset_normalization,
                           'borel_normalization':borel_normalization,
                           'independent_right_translations':'identity fixed in all sets'}


def run(shape,seconds,seed,output,max_models,affine=None,engine='glucose4',sl2_anchor=None,right_lex=False):
    G=affine_group(*affine) if affine else group(5)
    solver,members,encoding=build_solver(G,shape,seed,engine,sl2_anchor,right_lex)
    started=time.monotonic()
    result={'group':G['name'],'affine_parameters':affine,'shape':shape,'seed':seed,
            'solver':engine,'encoding':encoding,
            'seconds_limit':seconds,'models_limit':max_models,
            'pair_injective_models':0,'exact_farkas_cuts':0,'cuts':[],
            'status':'running','witness':None,'scope':'Bounded search. SAT '
            'timeouts and absent witnesses are not nonexistence proofs.'}
    output.parent.mkdir(parents=True,exist_ok=True)
    def checkpoint():
        result['elapsed_seconds']=time.monotonic()-started
        result['sat_statistics']=solver.accum_stats()
        tmp=output.with_suffix('.tmp')
        tmp.write_text(json.dumps(result,indent=2)+'\n')
        tmp.replace(output)
    checkpoint()
    while result['pair_injective_models']<max_models:
        remaining=seconds-(time.monotonic()-started)
        if remaining<=0:
            result['status']='time-limit';break
        if engine=='cadical195':
            # A conflict budget is cooperative, not a hard wall-clock limit.
            # Smaller batches avoid long unreported overruns on dense cases.
            solver.conf_budget(500)
            solved=solver.solve_limited()
            if solved is None:
                checkpoint()
                continue
        else:
            timer=threading.Timer(remaining,solver.interrupt)
            timer.start()
            try: solved=solver.solve_limited(expect_interrupt=True)
            finally: timer.cancel()
        if solved is None:
            result['status']='time-limit';break
        if solved is False:
            result['status']='solver-reported-unsatisfiable; no proof trace exported';break
        model={v for v in solver.get_model() if v>0}
        sets=[[g for g,v in enumerate(row) if v in model] for row in members]
        relations,intended=extra_relations(G,sets)
        result['pair_injective_models']+=1
        decision=potential_or_circuit(relations,sum(shape))
        if 'potentials' in decision:
            verified=verify_witness(G,sets,decision['potentials'])
            result['witness']={'sets':sets,'matrices':[[G['matrices'][g] for g in row] for row in sets],
                               'potentials':decision['potentials'],'verification':verified}
            result['status']='exact-degeneration-witness';checkpoint();break
        if not verify_farkas(relations,decision['indices'],decision['weights']):
            raise ArithmeticError('refusing an unverified SAT cut')
        selected=set()
        n,m,p=shape
        for i in decision['indices']:
            s,t,tt,u,uu,ss=relations[i]['vertices']
            selected.update([(0,sets[0][s]),(0,sets[0][ss]),
                             (1,sets[1][t]),(1,sets[1][tt]),
                             (2,sets[2][u]),(2,sets[2][uu])])
        cut=sorted(selected)
        solver.add_clause([-members[f][g] for f,g in cut])
        result['exact_farkas_cuts']+=1
        result['cuts'].append({'members':cut,'relation_vertices':[
            relations[i]['vertices'] for i in decision['indices']],
            'relations':[relations[i]['row'] for i in decision['indices']],
            'weights':decision['weights'],'source_sets':sets,
            'extra_relations':len(relations),'intended_terms':intended})
        if result['pair_injective_models']%100==0:
            checkpoint()
            print(json.dumps({k:result[k] for k in ['pair_injective_models','exact_farkas_cuts','elapsed_seconds']}),flush=True)
    else: result['status']='model-limit'
    checkpoint()
    solver.delete()
    print(json.dumps({k:v for k,v in result.items() if k not in ['cuts','witness']},indent=2),flush=True)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shape',type=int,nargs=3,default=[9,9,12])
    parser.add_argument('--seconds',type=float,default=120)
    parser.add_argument('--seed',type=int,default=20261020)
    parser.add_argument('--max-models',type=int,default=1000)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--affine',type=int,nargs=2,metavar=('PRIME','INDEX'))
    parser.add_argument('--solver',choices=['glucose4','cadical195'],default='glucose4')
    parser.add_argument('--sl2-anchor',choices=['central','unipotent','negative-unipotent','order4'])
    parser.add_argument('--right-lex',action='store_true')
    args=parser.parse_args()
    if min(args.shape)<1 or max(args.shape)>120 or args.seconds<=0 or args.max_models<1:
        parser.error('invalid positive shape or limits')
    if args.affine and (args.sl2_anchor or args.right_lex):parser.error('SL2 symmetry options require SL2 source')
    run(args.shape,args.seconds,args.seed,args.output,args.max_models,args.affine,args.solver,args.sl2_anchor,args.right_lex)
