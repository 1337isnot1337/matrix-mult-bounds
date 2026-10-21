"""Exact two-factor equivariant coefficient comparison for discovery.

The Clebsch--Gordan basis is imported from the earlier maintained package.
Neither a passing support screen nor a small numerical residual is a witness.
"""
from collections import defaultdict
from fractions import Fraction
from functools import cache
from itertools import product
from math import comb
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"2026-10-20-clebsch-gordan"))
from cg_blocks import equivariant_basis


@cache
def inverse_pair(p,q):
    original=list(product(range(p+1),range(q+1)))
    basis=equivariant_basis(p,q)
    matrix=sp.Matrix([[pol.get(v,0) for _,_,pol in basis] for v in original])
    inverse=matrix.inv()
    assert inverse*matrix==sp.eye(len(original))
    by_column=[[(i,Fraction(inverse[i,j])) for i in range(len(basis)) if inverse[i,j]]
               for j in range(len(original))]
    return original,basis,by_column


def transform(tensor,degrees):
    bases=[inverse_pair(*pair) for pair in degrees]
    for axis,(_,_,columns) in enumerate(bases):
        transformed=defaultdict(Fraction)
        for point,value in tensor.items():
            for new,factor in columns[point[axis]]:
                transformed[point[:axis]+(new,)+point[axis+1:]]+=factor*value
        tensor={point:value for point,value in transformed.items() if value}
    blocks=defaultdict(dict)
    for point,value in tensor.items():
        labels=[bases[axis][1][v][:2] for axis,v in enumerate(point)]
        blocks[tuple(v[0] for v in labels)][tuple(v[1] for v in labels)]=value
    return dict(blocks)


def paired_tensors(a):
    d=a-1;m=2*a-1
    source={}
    for i,j,r,s in product(range(a),repeat=4):
        point=(i*a+s,j*m+2*d-r-s,(2*d-i-j)*a+r)
        source[point]=Fraction((-1)**(i+j+r+s)*comb(d,i)*comb(d,j)*comb(d,r)*comb(d,s))
    target={}
    for u,v,w in product(range(a),range(a),range(m)):
        point=(u*a+v,(d-v)*m+w,(2*d-w)*a+d-u)
        target[point]=Fraction((-1)**(u+v+w)*comb(d,u)*comb(d,v)*comb(2*d,w))
    degrees=((d,d),(d,2*d),(2*d,d))
    return transform(source,degrees),transform(target,degrees)


def ratio_blocks(a):
    source,target=paired_tensors(a)
    records=[]
    for label in sorted(source.keys()|target.keys()):
        s,t=source.get(label,{}),target.get(label,{})
        if not s or not t:
            ratio=None
        else:
            point=next(iter(s))
            ratio=t.get(point,0)/s[point]
            assert all(t.get(point,0)==ratio*s.get(point,0) for point in s.keys()|t.keys())
        records.append({"labels":list(label),"source_nonzero":bool(s),"target_nonzero":bool(t),
                        "target_source_ratio":str(ratio) if ratio is not None else None})
    return records


if __name__=="__main__":
    import argparse,json
    parser=argparse.ArgumentParser();parser.add_argument("a",type=int)
    args=parser.parse_args()
    print(json.dumps(ratio_blocks(args.a),indent=2))
