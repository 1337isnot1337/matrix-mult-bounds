"""Disjoint seven-term cores for the integer product-oblique residual.

This is a continuation of the frozen oblique-paired-repair package.  It
does not modify the maps.  All terms have integer coefficients and replay
over Z, hence over every field.  Tensor-rank optimality is not claimed.
"""

from itertools import product
from pathlib import Path
import argparse
import importlib.util
import json
import sys

PARENT = Path(__file__).resolve().parent.parent
PACKAGE = PARENT / "2026-10-23-oblique-paired-repair"
if not PACKAGE.is_dir():
    PACKAGE = PARENT / "oblique-paired-repair"
sys.path.insert(0, str(PACKAGE))
from karatsuba_repair import _add, _record, expand_terms
from exact import Field, contract, matrix_multiplication, subtract
_SPEC = importlib.util.spec_from_file_location('oblique_border_source_verify', PACKAGE/'verify.py')
_SOURCE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_SOURCE)
formula_residual, product_maps = _SOURCE.formula_residual, _SOURCE.product_maps


def core_terms(r, s, i, j):
    """Replace the eight terms on (i,j-s),(i-s,j),(i,j) by seven."""
    k, ell = i-s, j-s
    u, v, w = {r*i+ell: 1}, {r*k+j: 1}, {r*i+j: 1}
    xx, zz = {4*i: 1, 4*k+1: -1}, {4*i+2: 1, 4*k+3: -1}
    aa, eta, yy = {4*k: 1}, {4*k+1: 1}, {4*i+1: 1}
    pp, qq = {ell: 1}, {2*r+ell: 1}
    rr, ss = {j: 1, 2*r+ell: -1}, {r+j: 1, 3*r+ell: -1}
    tt = {2*r+j: 1}
    return [
        _record(_add(u,w), _add(xx,zz), qq),
        _record(u,xx,_add(pp,qq,-1)),
        _record(w,zz,_add(tt,qq,-1)),
        _record(_add(v,w),eta,_add(rr,ss)),
        _record(v,_add(aa,eta,-1),rr),
        _record(w,_add(yy,eta,-1),ss),
        _record(w,xx,rr),
    ]


def slice_terms(r, s, bad, i, j):
    """The direct two- or four-term decomposition, before core replacement."""
    aa = {r*i+j: 1}
    if i in bad and j in bad:
        return [
            _record(aa,{4*i:1},{j:1}),
            _record(aa,{4*i+2:1,4*(i-s)+3:-1},{2*r+j:1}),
            _record(aa,{4*i+1:1},{r+j:1,3*r+j-s:-1}),
            _record(aa,{4*(i-s)+1:-1},{2*r+j-s:1}),
        ]
    if i in bad:
        return [_record(aa,{4*i+2*a:1,4*(i-s)+2*a+1:-1},{2*a*r+j:1})
                for a in range(2)]
    if j in bad:
        return [_record(aa,{4*i+v:1},{v*r+j:1,(v+2)*r+j-s:-1})
                for v in range(2)]
    return []


def grid_terms(n, b):
    if type(n) is not int or type(b) is not int or b < 2 or n < b+1:
        raise ValueError("Require integers b>=2 and n>=b+1")
    r, s, d = n-1, b-1, n-b-1
    bad = set(range(s,r-1))
    boundary = [i for i in sorted(bad) if i-s not in bad]
    if len(boundary) != min(d,s):
        raise ArithmeticError("Boundary size changed")
    covered, terms = set(), []
    for i,j in product(boundary,repeat=2):
        points={(i,j-s),(i-s,j),(i,j)}
        if len(points)!=3 or points & covered:
            raise ArithmeticError("The selected core supports overlap")
        covered.update(points)
        terms.extend(core_terms(r,s,i,j))
    for i,j in product(range(r),repeat=2):
        if (i,j) not in covered:
            terms.extend(slice_terms(r,s,bad,i,j))
    if len(terms)!=4*r*d-min(d,s)**2:
        raise ArithmeticError("The scalar count changed")
    return terms


def certificate(n, b, raw=False, complete=False):
    terms=grid_terms(n,b)
    residual=formula_residual(n,b)
    expanded=expand_terms(terms)
    if expanded!=residual:
        raise ArithmeticError("The integer scalar decomposition is false")
    if raw:
        r=n-1
        native,_=contract(n,b,(r,4,r),product_maps(n,b))
        actual=subtract(matrix_multiplication((r,4,r)),native,Field())
        if actual!=expanded:
            raise ArithmeticError("The native source coefficients differ")
    r,d,s=n-1,n-b-1,b-1
    result={"n":n,"b":b,"target":[r,4,r],"dependencies":d,
            "direct_terms":4*r*d,"disjoint_cores":min(d,s)**2,
            "scalar_rank_upper_bound":len(terms),
            "integer_coefficients_replayed":True,
            "native_source_replayed":raw,
            "tensor_rank_optimality_claimed":False}
    if complete:
        result['rank_one_terms']=terms
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    controls=[certificate(b+1+d,b,raw=(b,d) in {(4,1),(4,2),(4,3),(2,3),(3,5)})
              for b in range(2,10) for d in range(9)]
    result={"formula":"4*r*d-min(d,b-1)^2, r=n-1, d=n-b-1",
            "all_fields":True,"controls":controls,
            "witness_n7_b4":certificate(7,4,raw=True,complete=True),
            "improves_omega":False}
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({"controls":len(controls),"native_controls":sum(c['native_source_replayed'] for c in controls),
          "examples":[c for c in controls if c['b']==4]},indent=2))


if __name__=='__main__':
    main()
