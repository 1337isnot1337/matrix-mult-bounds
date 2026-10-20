"""Exact source degrees and conditional exponent gate for SL(2,5).

The group-algebra calculation is over Q(sqrt(5)); no character table, CAS,
floating optimizer, or external execution is needed to replay it.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import json
from math import isqrt,prod
from pathlib import Path

from group_exact import group

ZERO=(Q(0),Q(0))
ONE=(Q(1),Q(0))


def add(x,y): return x[0]+y[0],x[1]+y[1]
def mul(x,y): return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]


def conjugacy_algebra(G):
    N=len(G['matrices']); remaining=set(range(N)); classes=[]
    while remaining:
        x=min(remaining)
        cls=sorted({G['mul'][G['mul'][g][x]][G['inv'][g]] for g in range(N)})
        classes.append(cls);remaining.difference_update(cls)
    r=len(classes)
    structure=[]
    for i in range(r):
        row=[]
        for j in range(r):
            counts=[0]*N
            for x in classes[i]:
                for y in classes[j]: counts[G['mul'][x][y]]+=1
            if any(any(counts[g]!=counts[c[0]] for g in c) for c in classes):
                raise ArithmeticError('class product is not central')
            row.append([counts[c[0]] for c in classes])
        structure.append(row)
    return classes,structure


def central_product(x,y,structure):
    result=[ZERO]*len(x)
    for i,xi in enumerate(x):
        for j,yj in enumerate(y):
            coefficient=mul(xi,yj)
            for k,n in enumerate(structure[i][j]):
                if n: result[k]=add(result[k],(coefficient[0]*n,coefficient[1]*n))
    return result


def idempotents():
    # Found by diagonalizing one generic central element, then verified below.
    data=[
      (30,[4,0,1,-1,-1,1,-1,-1,4],[0]*9),
      (20,[6,0,0,1,-1,0,1,-1,-6],[0]*9),
      (24,[5,1,-1,0,0,-1,0,0,5],[0]*9),
      (30,[4,0,-1,-1,1,1,-1,1,-4],[0]*9),
      (120,[1]*9,[0]*9),
      (120,[4,0,2,-1,1,-2,-1,1,-4],[0,0,0,-1,1,0,1,-1,0]),
      (120,[4,0,2,-1,1,-2,-1,1,-4],[0,0,0,1,-1,0,-1,1,0]),
      (80,[6,-2,0,1,1,0,1,1,6],[0,0,0,1,1,0,-1,-1,0]),
      (80,[6,-2,0,1,1,0,1,1,6],[0,0,0,-1,-1,0,1,1,0])]
    return [[(Q(a,den),Q(b,den)) for a,b in zip(real,rad)] for den,real,rad in data]


def source_certificate():
    G=group(5);N=len(G['matrices'])
    classes,structure=conjugacy_algebra(G)
    es=idempotents();r=len(classes)
    if r!=9: raise ArithmeticError('unexpected center dimension')
    for i,e in enumerate(es):
        if not any(x!=ZERO for x in e): raise ArithmeticError('zero idempotent')
        for j,f in enumerate(es):
            if central_product(e,f,structure)!=(e if i==j else [ZERO]*r):
                raise ArithmeticError('idempotents are not orthogonal')
    total=[ZERO]*r
    for e in es: total=[add(x,y) for x,y in zip(total,e)]
    if total != [ONE]+[ZERO]*(r-1): raise ArithmeticError('idempotents do not sum to one')
    degrees=[]
    for e in es:
        rank=N*e[0][0]
        if e[0][1] or rank.denominator!=1 or rank<=0:
            raise ArithmeticError('regular idempotent trace is not positive integer')
        d=isqrt(rank.numerator)
        if d*d!=rank: raise ArithmeticError('block dimension is not a square')
        degrees.append(d)
    if sum(d*d for d in degrees)!=N: raise ArithmeticError('dimension sum mismatch')
    return {'group':'SL(2,5)','order':N,'conjugacy_classes':classes,
            'class_sizes':list(map(len,classes)),
            'center_dimension':r,'ordered_block_degrees':degrees,
            'irreducible_degrees':sorted(degrees),
            'primitive_central_idempotents':[
                [[str(a),str(b)] for a,b in e] for e in es],
            'pairwise_idempotent_products_verified':r*r,
            'regular_trace_rule':'rank(e acting on C[G]) = |G| times identity coefficient',
            'external_algebraic_bridge':'Maschke and Artin-Wedderburn over C; '
                 'nine nonzero orthogonal central idempotents in a center of '
                 'dimension nine are primitive. Their regular ranks are d_i^2.',
            'status':'exact finite source certificate; no target embedding asserted'}


def integer_nthroot(n,k):
    if n<0 or k<1: raise ValueError('invalid root')
    if n<2 or k==1: return n
    lo=0;hi=1<<((n.bit_length()+k-1)//k)
    while hi-lo>1:
        mid=(hi+lo)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    return lo


def power_interval(a,p,q,scale):
    radicand=a**p*scale**q
    root=integer_nthroot(radicand,q)
    lo=Q(root,scale)
    hi=lo if root**q==radicand else Q(root+1,scale)
    if lo**q>a**p or hi**q<a**p:
        raise ArithmeticError('invalid power interval')
    return lo,hi


def conditional_gate(degrees,shape,bound=Q(2249,1000),scale=10**8):
    V=prod(shape);p,q=bound.numerator,bound.denominator
    intervals=[power_interval(d,p,q,scale) for d in degrees]
    lhs=sum((hi for lo,hi in intervals),Q(0))
    rhs=power_interval(V,p,3*q,scale)[0]
    if lhs>=rhs: raise ArithmeticError('conditional exponent gate failed')
    return {'shape':list(shape),'bound':str(bound),
            'sum_irrep_powers_upper':str(lhs),'volume_power_lower':str(rhs),
            'strict_margin_lower':str(rhs-lhs),
            'scale':scale,'strict_comparison_verified':True,
            'prerequisite':'An independently verified degeneration from C[SL(2,5)] '
                           'to the indicated matrix tensor. NOT CONSTRUCTED HERE.',
            'conclusion_if_prerequisite_holds':'omega <= '+str(bound),
            'actual_improvement_established':False}


def report():
    source=source_certificate()
    return {'source':source,'conditional_gates':[
        conditional_gate(source['irreducible_degrees'],s)
        for s in [(9,9,12),(9,10,11),(10,10,10)]],
        'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'degrees':result['source']['irreducible_degrees'],
                      'conditional_gates':result['conditional_gates']},indent=2))
