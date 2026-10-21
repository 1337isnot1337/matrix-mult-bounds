"""Replay finite arithmetic and explicitly scoped anisotropic source screens."""
from itertools import permutations, product
import json
from math import isqrt
from pathlib import Path
import random

from representation_packing import equivariant_packing, ordinary_rank_screen, target_shapes


def coefficient(f,a,b,i,k,s):
    if not (0<=i<a and 0<=k<a+b-1 and 0<=s<b):
        return 0
    return f[(i*(a+b-1)+k)*b+s]


def slice_entry(f,a,b,row,column):
    j,p,long_row=row
    long_column,q,r=column
    return coefficient(f,a,b,long_column-j,p+q,long_row-r)


def triangular_minor(f,a,b):
    if not any(f):
        raise ValueError("The zero slice has no nonzero triangular minor")
    k=next(k for k in range(a+b-1)
           if any(coefficient(f,a,b,i,k,s) for i in range(a) for s in range(b)))
    i0=max(i for i in range(a) if any(coefficient(f,a,b,i,k,s) for s in range(b)))
    s0=max(s for s in range(b) if coefficient(f,a,b,i0,k,s))
    p0=min(k,a-1);q0=k-p0
    if not (0<=p0<a and 0<=q0<b):
        raise ArithmeticError("Invalid convolution decomposition")
    rows=[(j,p0,r+s0) for j in range(b) for r in range(a)]
    columns=[(j+i0,q0,r) for j in range(b) for r in range(a)]
    matrix=[[slice_entry(f,a,b,row,col) for col in columns] for row in rows]
    pivot=coefficient(f,a,b,i0,k,s0)
    for row,(j,r) in enumerate(product(range(b),range(a))):
        for column,(jp,rp) in enumerate(product(range(b),range(a))):
            if (jp>j or (jp==j and r>rp)) and matrix[row][column]:
                raise ArithmeticError("Minor violates the triangular zero pattern")
        if matrix[row][row]!=pivot:
            raise ArithmeticError("Minor diagonal differs from the selected pivot")
    return matrix,pivot


def source_frontier(maximum_leg_dimension=300):
    sources=[]
    for a in range(1,isqrt(maximum_leg_dimension)+1):
        for b in range(a,isqrt(maximum_leg_dimension)+1):
            n=a*b*(a+b-1)
            if n>maximum_leg_dimension:
                continue
            shapes=[]
            for shape in target_shapes(a,b):
                l,h,r=shape
                slacks=[2*n-a*b-z*(x+y-1)
                        for x,y,z in ((l,h,r),(h,r,l),(r,l,h))]
                shapes.append({"shape":list(shape),"volume":l*h*r,
                    "minimum_rank_slacks":slacks,
                    "passes_minimum_rank_screen":ordinary_rank_screen(a,b,shape)})
            sources.append({"a":a,"b":b,"source_leg_dimension":n,
                            "improving_shapes":shapes})
    return sources


def finite_controls():
    rng=random.Random(202610207)
    coefficient_tests=0
    checked_slices=0
    for a,b in ((1,1),(1,3),(2,3),(3,2),(3,5),(4,5),(5,4),(4,6),(5,5)):
        n=a*b*(a+b-1)
        for _ in range(12):
            f=[rng.randrange(-2,3) for _ in range(n)]
            if not any(f):
                f[0]=1
            matrix,pivot=triangular_minor(f,a,b)
            if not pivot or len(matrix)!=a*b:
                raise ArithmeticError("Missing claimed triangular minor")
            coefficient_tests+=(a*b)**2
            checked_slices+=1
        # A source corner slice has ab unit entries in distinct rows/columns.
        f=[0]*n;f[0]=1
        rows=list(product(range(b),range(a),range(a+b-1)))
        cols=list(product(range(a+b-1),range(b),range(a)))
        nonzero=[(i,j,slice_entry(f,a,b,row,col))
                 for i,row in enumerate(rows) for j,col in enumerate(cols)
                 if slice_entry(f,a,b,row,col)]
        if len(nonzero)!=a*b or len({i for i,_,_ in nonzero})!=a*b or len({j for _,j,_ in nonzero})!=a*b:
            raise ArithmeticError("Corner slice does not attain minimum rank")
    return {"seed":202610207,"integer_slices":checked_slices,
            "minor_entries_checked":coefficient_tests,"corner_slices":9}


def report():
    cert=404352**561>25**2250
    if not cert:
        raise ArithmeticError("Conditional rational comparison failed")
    selected=(12,12,13)
    return {
        "baseline_commit":"9a4ee3d05939d88730045877a6945165845f0398",
        "new_exponent_established":False,
        "target_constructed":False,
        "independent_review":False,
        "conditional_target":{"source_lengths":[4,5],"source_leg_dimensions":[160]*3,
            "target_shape":list(selected),"target_leg_dimensions":[144,156,156],
            "conditional_exponent":"561/250",
            "integer_comparison":"404352**561 > 25**2250",
            "integer_comparison_passes":cert},
        "source_frontier_maximum_leg_dimension":300,
        "source_frontier":source_frontier(),
        "finite_minor_controls":finite_controls(),
        "selected_full_action":equivariant_packing(4,5,selected),
        "selected_two_factor_actions":[equivariant_packing(4,5,s,True)
                                       for s in sorted(set(permutations(selected)))],
        "positive_representation_controls":[equivariant_packing(2,2,s,True)
                      for s in sorted(set(permutations((2,3,4))))],
    }


if __name__=="__main__":
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    data=report()
    payload=json.dumps(data,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload,end="")
