"""Exact unequal paired source equivalence and prescribed quantum limits.

Exploratory only. No matrix multiplication target is asserted here.
"""
from collections import Counter
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('paired_quantum_screen',ROOT/'research/ai/2026-10-21-paired-quantum/screens.py')
screen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)
core=screen.core
q,K=core.q,core.K


def diagonal_factor(n,m,leg,i,j):
    D,E=n-1,m-1
    h=D+E
    if leg==0:
        return q**(-i*(i-1)//2-j*(j-1)//2)
    z,v=(j,i) if leg==1 else (i,j)
    s=h-z
    return ((-1)**s*q**(-D*v-v*(v-1)//2+s*(s-1)//2+s*(h-s-1))
            /core.qchoose(h,s))


def source_control(n,m):
    h=n+m-2
    checks=0
    for p in range(n):
        for r in range(n):
            for y in range(m):
                for v in range(m):
                    actual=(diagonal_factor(n,m,0,p,r)*diagonal_factor(n,m,1,y,h-r-v)
                            *diagonal_factor(n,m,2,h-p-y,v))
                    expected=(core.invariant_coefficient(n-1,m-1,p,y)
                              *core.invariant_coefficient(n-1,m-1,r,v))
                    if actual!=expected:
                        raise ArithmeticError(('source equivalence',n,m,p,r,y,v))
                    checks+=1
    return checks


@lru_cache(None)
def local_map(n,m,leg,recouple_A=True):
    D,E=n-1,m-1
    h=D+E
    u,v=[(D,D),(E,h),(h,E)][leg]
    if leg==0 and not recouple_A:
        labels=[(i,j) for i in range(u+1) for j in range(v+1)]
        return (u,v),labels,{(i*(v+1)+j,i*(v+1)+j):diagonal_factor(n,m,0,i,j)
                             for i in range(u+1) for j in range(v+1)}
    inverse=core.inverse_cg(u,v)
    labels=[(k,l) for k in range(min(u,v)+1) for l in range(u+v-2*k+1)]
    rows={label:i for i,label in enumerate(labels)}
    entries={}
    for i in range(u+1):
        for j in range(v+1):
            factor=diagonal_factor(n,m,leg,i,j)
            for label,value in inverse[i,j]:
                entries[rows[label],i*(v+1)+j]=factor*value
    return (u,v),labels,entries


@lru_cache(None)
def transformed_tensor(n,m,recouple_A=True):
    h=n+m-2
    data=[local_map(n,m,k,recouple_A) for k in range(3)]
    maps=[]
    for (u,v),labels,entries in data:
        columns={j:[] for j in range((u+1)*(v+1))}
        for (i,j),value in entries.items():columns[j].append((i,value))
        maps.append(columns)
    tensor={}
    for p in range(n):
        for r in range(n):
            for y in range(m):
                for v in range(m):
                    inputs=(p*n+r,y*(h+1)+h-r-v,(h-p-y)*m+v)
                    for i,x in maps[0][inputs[0]]:
                        for j,z in maps[1][inputs[1]]:
                            for k,w in maps[2][inputs[2]]:
                                key=(i,j,k)
                                tensor[key]=tensor.get(key,K.zero)+x*z*w
    return data,{key:value for key,value in tensor.items() if value}


def initial_tensor(n,m,order,recouple_A=True):
    data,tensor=transformed_tensor(n,m,recouple_A)
    initials=[screen.regular_initial_entries(d,order) for d in data]
    field,poly=screen.residue_field(order)
    row_minima=[row[1] for row in initials]
    records=[]
    exact={}
    for positions,value in tensor.items():
        val,parts=core.initial_residue(value,poly)
        base=val-sum(row_minima[k][positions[k]] for k in range(3))
        numerator,denominator=[sum((field.convert(c)*field.unit**e[0] for e,c in part.items()),field.zero)
                               for part in parts]
        residue=numerator/denominator
        if base<0:raise ArithmeticError(('regular local tensor pole',positions,base))
        records.append({'positions':positions,'generic_coefficient':str(value),
                        'valuation':val,'baseline_valuation':base,
                        'leading_residue_coefficients':screen.encode_field(residue)})
        if base==0:exact[positions]=residue
    shape=[len(d[1]) for d in data]
    ranks=[]
    for axis in range(3):
        other=[k for k in range(3) if k!=axis]
        cols=sorted({tuple(key[k] for k in other) for key in exact})
        matrix=[[exact.get(tuple(row if k==axis else col[other.index(k)] for k in range(3)),field.zero)
                 for col in cols] for row in range(shape[axis])]
        ranks.append(core.rank_over_field(matrix,field.zero))
    return {'n':n,'m':m,'order':order,'recouple_A':recouple_A,'source_format':shape,
            'source_identity_checks':source_control(n,m),
            'local_map_records':[screen.regular_initial(d,order) for d in data],
            'labels':[d[1] for d in data],'row_minima':row_minima,
            'generic_nonzero_coefficients':len(tensor),
            'baseline_valuation_histogram':dict(sorted(Counter(row['baseline_valuation'] for row in records).items())),
            'regular_tensor_flattening_ranks':ranks,
            'regular_tensor_nonzero_coefficients':len(exact),
            'coefficients':records,'improves_omega':False},data,field,exact


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n',type=int,default=3)
    parser.add_argument('--m',type=int,default=2)
    parser.add_argument('--order',type=int,default=8)
    parser.add_argument('--keep-A',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report,*_=initial_tensor(args.n,args.m,args.order,not args.keep_A)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['n','m','order','recouple_A','source_identity_checks',
          'generic_nonzero_coefficients','baseline_valuation_histogram','regular_tensor_flattening_ranks',
          'regular_tensor_nonzero_coefficients']}))
