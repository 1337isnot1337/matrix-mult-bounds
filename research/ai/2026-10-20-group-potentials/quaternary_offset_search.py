"""Constructive 96-choice search for M12 inside C[F4^3:C3].

Each of the three index sets has one four-point affine plane in each scalar
coset. Pair-label injectivity becomes a four-color constraint, then every
extra group term is checked with the same exact integer-potential verifier.
This is a restricted discovery ansatz, not an exhaustive group search.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time
from itertools import combinations

from pysat.card import CardEnc,EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical195

from quaternary_group import group,plane_family,scale,fm,coset_representatives
from group_exact import extra_relations,verify_witness,verify_farkas
from search import potential_or_circuit


def run(seconds,max_models,output,pattern='covariant'):
    G=group();H=plane_family(pattern)
    reps=[{a:coset_representatives(P) for a,P in row.items()} for row in H]
    pool=IDPool();clauses=[]
    choices=[{a:[pool.id(('offset',f,a,o)) for o in range(16)] for a in [1,2,3]}
             for f in range(3)]
    for f in range(3):
        for a in [1,2,3]:
            clauses.extend(CardEnc.equals(choices[f][a],1,vpool=pool,
                                         encoding=EncType.seqcounter).clauses)
        clauses.append([choices[f][1][0]])
    for f,g in [(0,1),(1,2),(2,0)]:
        quotient_colors={}
        for q in [1,2,3]:
            quotient_colors[q]=[]
            for a in [1,2,3]:
                b=fm(q,a)
                W={x^scale(q,y) for x in H[f][a] for y in H[g][b]}
                if len(W)!=16:raise ArithmeticError('normal planes are not pair-disjoint')
                cosets=sorted({min(v^w for w in W) for v in range(64)})
                if len(cosets)!=4:raise ArithmeticError('wrong quotient size')
                cmap={v:cosets.index(min(v^w for w in W)) for v in range(64)}
                masks=[sum(1<<(v^w) for w in W) for v in cosets]
                edge=[pool.id(('pair-color',f,g,a,b,c)) for c in range(4)]
                quotient_colors[q].append((edge,masks))
                clauses.extend(CardEnc.equals(edge,1,vpool=pool,encoding=EncType.seqcounter).clauses)
                for o,v in enumerate(reps[f][a]):
                    for z,w in enumerate(reps[g][b]):
                        color=cmap[v^scale(q,w)]
                        clauses.append([-choices[f][a][o],-choices[g][b][z],edge[color]])
            for (left,lm),(right,rm) in combinations(quotient_colors[q],2):
                clauses.extend([[-left[c],-right[d]] for c in range(4) for d in range(4)
                                if lm[c]&rm[d]])
    solver=Cadical195(bootstrap_with=clauses,use_timer=True)
    result={'group':G['name'],'source_family':'quaternary-affine','shape':[12,12,12],
       'plane_pattern':pattern,'normal_planes':[{a:list(P) for a,P in row.items()} for row in H],
       'normal_offset_representatives':reps,
       'encoding':{'variables':pool.top,'clauses':len(clauses),
                   'ansatz':'S_f(a) = (a,a*(P_f+offset_f(a))), four points per scalar coset'},
       'seconds_limit':seconds,'model_limit':max_models,'pair_injective_models':0,
       'exact_farkas_cuts':0,'cuts':[],'witness':None,'status':'running',
       'scope':'Fixed normal-plane ansatz only. Solver UNSAT without a proof '
               'trace is not a nonexistence theorem. No exponent improvement yet.'}
    output.parent.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    index={x:i for i,x in enumerate(G['matrices'])}
    def save():
        result['elapsed_seconds']=time.monotonic()-started
        result['sat_statistics']=solver.accum_stats()
        tmp=output.with_suffix('.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(output)
    save()
    while result['pair_injective_models']<max_models and time.monotonic()-started<seconds:
        solver.conf_budget(10000);solved=solver.solve_limited()
        if solved is None:save();continue
        if not solved:
            result['status']='fixed-plane ansatz solver-reported UNSAT; no proof trace';break
        model={v for v in solver.get_model() if v>0}
        selected=[{a:next(o for o,v in enumerate(choices[f][a]) if v in model)
                   for a in [1,2,3]} for f in range(3)]
        sets=[]
        for f in range(3):
            points=[]
            for a in [1,2,3]:
                offset=reps[f][a][selected[f][a]]
                points.extend(index[(a,scale(a,v^offset))] for v in H[f][a])
            sets.append(sorted(points))
        relations,intended=extra_relations(G,sets)
        result['pair_injective_models']+=1
        decision=potential_or_circuit(relations,36)
        if 'potentials' in decision:
            verified=verify_witness(G,sets,decision['potentials'])
            result['witness']={'sets':sets,'matrices':[[list(G['matrices'][g]) for g in row] for row in sets],
                'potentials':decision['potentials'],'verification':verified,'offsets':selected}
            result['status']='exact-degeneration-witness';save();break
        if not verify_farkas(relations,decision['indices'],decision['weights']):
            raise ArithmeticError('refusing unverified Farkas cut')
        members=set();cells=set()
        for i in decision['indices']:
            s,t,tt,u,uu,ss=relations[i]['vertices']
            for f,j in [(0,s),(0,ss),(1,t),(1,tt),(2,u),(2,uu)]:
                g=sets[f][j];members.add((f,g));cells.add((f,G['matrices'][g][0]))
        offset_cells=[(f,a,selected[f][a]) for f,a in sorted(cells)]
        solver.add_clause([-choices[f][a][o] for f,a,o in offset_cells])
        result['exact_farkas_cuts']+=1
        result['cuts'].append({'members':sorted(members),'source_sets':sets,
           'relation_vertices':[relations[i]['vertices'] for i in decision['indices']],
           'relations':[relations[i]['row'] for i in decision['indices']],
           'weights':decision['weights'],'offset_choice_cut':offset_cells,
           'extra_relations':len(relations),'intended_terms':intended})
        if result['pair_injective_models']%25==0:save()
    else:
        result['status']='time-limit' if time.monotonic()-started>=seconds else 'model-limit'
    save();solver.delete()
    print(json.dumps({k:v for k,v in result.items() if k not in ['cuts','witness']},indent=2))
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds',type=float,default=120)
    parser.add_argument('--max-models',type=int,default=2000)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--plane-pattern',choices=['covariant','one-shear'],default='covariant')
    args=parser.parse_args();run(args.seconds,args.max_models,args.output,args.plane_pattern)
