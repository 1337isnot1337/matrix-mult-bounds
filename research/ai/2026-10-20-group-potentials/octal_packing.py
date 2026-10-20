"""Necessary local label-packing discovery for F8^2:C7 target (19,19,19).

Each normal fiber has a fixed three-point direction subset, with two fibers
reduced to two points. Independent translated masks are a relaxation of the
global offset problem. SAT outcomes without traces are experiments only.
"""
from itertools import combinations
import argparse
import json
from pathlib import Path
import random
import time

from pysat.card import CardEnc,EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose4
from octal_group import fm,inverse,scale
from quaternary_directions import sumspace
from mask_packing import exact_pack


def basis(seed):
    rng=random.Random(seed)
    while True:
        columns=rng.sample(range(1,64),6)
        if len(sumspace(*[{0,x} for x in columns]))==64:return columns


def masks_for(base,left,right,q):
    points=[[0,*base[2*f:2*f+2]] for f in range(3)]
    masks=[]
    for a in range(1,8):
        b=fm(a,q)
        A=points[left] if a<6 else points[left][:2]
        B=points[right] if b<6 else points[right][:2]
        W={scale(inverse(a),x^y) for x in A for y in B}
        if len(W)!=len(A)*len(B):raise ArithmeticError('pair direction collision')
        translations=sorted({sum(1<<(v^w) for w in W) for v in range(64)})
        masks.append(translations)
    return masks


def local_pack(masks):
    pool=IDPool();clauses=[];choices=[];used=[]
    for a,options in enumerate(masks):
        vars=[pool.id(('mask',a,m)) for m in range(len(options))];choices.append(vars)
        clauses.extend(CardEnc.equals(vars,1,vpool=pool,encoding=EncType.seqcounter).clauses)
        row=[pool.id(('used',a,h)) for h in range(64)];used.append(row)
        for m,mask in enumerate(options):
            for h in range(64):
                if mask&(1<<h):clauses.append([-vars[m],row[h]])
    clauses.append([choices[0][0]])
    for h in range(64):
        clauses.extend([[-used[a][h],-used[b][h]] for a,b in combinations(range(7),2)])
    solver=Glucose4(bootstrap_with=clauses)
    solved=solver.solve();selected=None
    if solved:
        model={v for v in solver.get_model() if v>0}
        selected=[next(mask for lit,mask in zip(row,options) if lit in model)
                  for row,options in zip(choices,masks)]
        if any(x&y for x,y in combinations(selected,2)):
            raise ArithmeticError('refusing a non-disjoint packing')
    stats=solver.accum_stats();solver.delete()
    return {'solver_satisfiable':solved,'selected_masks':selected,
            'total_labels':sum(x.bit_count() for x in selected) if selected else None,
            'solver_statistics':stats,'unsat_proof_checked':False}


def screen(base):
    results=[]
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in range(1,8):
            result=exact_pack(masks_for(base,f,g,q))
            results.append({'families':[f,g],'quotient':q,**result})
            if not result['satisfiable']:return results
    return results


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=421)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();base=basis(args.seed);started=time.monotonic()
    result={'group':'F8^2:C7','target_shape':[19,19,19],'base_seed':args.seed,
        'base_columns':base,'local_packings':screen(base),'improves_omega':False,
        'scope':'Local relaxation only; no global group subsets or positive potentials.'}
    result['elapsed_seconds']=time.monotonic()-started
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
