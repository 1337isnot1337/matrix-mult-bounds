"""Exact ordinary spin-fiber obstruction; all-power proof in the companion note."""
from collections import Counter
from itertools import product
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
RESULTS=ROOT/'results/anisotropic-constructions-2026-10-20'
INPUT=RESULTS/'parity_balancing_spin1/scalar_witness.json'
OUTPUT=RESULTS/'spin-fiber-compression-ordinary-certificate.json'
LOCAL=(
 (0,0,0,2,0,0,0,0,0,0,0,2),
 (0,0,1,0,0,-1,0,0,0,0,1,0),
 (0,0,0,0,2,0,0,0,0,0,0,0),
 (0,4,0,0,0,0,0,0,0,0,0,0),
 (2,0,0,0,0,0,0,0,0,0,0,2),
 (0,0,0,0,0,0,0,0,0,0,-4,0),
 (0,0,0,0,0,0,0,2,0,0,0,0),
 (0,-1,0,0,0,0,1,0,0,-1,0,0),
 (2,0,0,0,0,0,0,0,2,0,0,0))
POINTS=((0,5,45),(0,7,63),(1,5,63),(1,9,0),(1,9,30))
BASE=({():-64,(20,173,328):64},{():-64,(20,165,364):64},
      {(19,173,364):32},{():-64,(19,152,308):64,(95,228,384):64},
      {(95,228,384):64})
DIVISORS=(64,64,32,64,64)
HIGH_COLUMNS=((0,1,1),(0,2,0),(1,0,1))
HIGH_UNITS=((0,0),(0,2),(2,0))


def variable_id(power,leg,first,trits,last):
    return leg*12**power+(first*3**power+trits)*2**power+last+1


def row_image(power,leg,row):
    """Keep an independent weight on each raw column, including singleton fibers."""
    n=3**power
    I,J=divmod(row,n)
    factors=[]
    for bit in range(power):
        local_row=3*(I//3**bit%3)+J//3**bit%3
        factors.append([(c,v) for c,v in enumerate(LOCAL[local_row]) if v])
    result={}
    for choice in product(*factors):
        first=middle=last=trits=0
        value=1
        for bit,(column,coefficient) in enumerate(choice):
            i,rem=divmod(column,6)
            m,s=divmod(rem,2)
            first+=i*2**bit;middle+=m*2**bit;last+=s*2**bit
            trits=3*trits+m
            value*=coefficient
        variable=variable_id(power,leg,first,trits,last)
        result.setdefault((first,middle,last),[]).append((variable,value))
    return result


def matrix_coefficient(power,point):
    n=3**power;x,y,z=point
    return int(x%n==y//n and y%n==z//n and z%n==x//n)


def selected_equation(power,point):
    """Contract every source term capable of contributing to the selected output."""
    images=[row_image(power,leg,row) for leg,row in enumerate(point)]
    side=2**power;answer=Counter()
    for (i,m,s),xs in images[0].items():
        for (p,L,j),ys in images[1].items():
            q,r=m-p,L-s
            if not (0<=q<side and 0<=r<side):continue
            zs=images[2].get((r,i+j,q),())
            for (vx,x),(vy,y),(vz,z) in product(xs,ys,zs):
                answer[vx,vy,vz]+=x*y*z
    answer[()]-=2**(3*power)*matrix_coefficient(power,point)
    return {m:c for m,c in answer.items() if c}


def lift_point(power,point):
    n=3**power
    return tuple(3*n*(row//n+n*i)+row%n+n*j
                 for row,(i,j) in zip(point,HIGH_UNITS))


def lift_variable(power,variable):
    leg,raw=divmod(variable-1,12**power)
    raw,last=divmod(raw,2**power)
    first,trits=divmod(raw,3**power)
    i,m,s=HIGH_COLUMNS[leg]
    return variable_id(power+1,leg,first+i*2**power,3*trits+m,last+s*2**power)


def lift_polynomial(power,polynomial):
    return {tuple(lift_variable(power,v) for v in m):8*c for m,c in polynomial.items()}


def export_polynomial(polynomial):
    return [{'variables':list(m),'coefficient':c} for m,c in sorted(polynomial.items())]


def bezout_identity():
    normalized=[{m:c//d for m,c in p.items()} for p,d in zip(BASE,DIVISORS)]
    multipliers=((0,-1,(19,152,308)),(1,-1,(19,20,152,173,308,328)),
                 (2,1,(20,20,152,165,308,328)),(3,-1,()),(4,1,()))
    total=Counter()
    for equation,coefficient,monomial in multipliers:
        for other,value in normalized[equation].items():
            total[tuple(sorted(monomial+other))]+=coefficient*value
    if {m:c for m,c in total.items() if c}!={():1}:
        raise ArithmeticError('The integer polynomial identity for one failed')
    return [{'equation':eq+1,'coefficient':c,'variables':list(m)}
            for eq,c,m in multipliers]


def report():
    if tuple(map(tuple,json.loads(INPUT.read_text())['base_common_map_numerator']))!=LOCAL:
        raise ArithmeticError('The fixed local spin map has changed')
    points=POINTS;expected=BASE;controls=[]
    for power in (2,3,4):
        equations=[selected_equation(power,point) for point in points]
        if tuple(equations)!=tuple(expected):
            raise ArithmeticError('The selected original-source coefficients differ')
        for row in {p[0] for p in points}:
            if min(m for _,m,_ in row_image(power,0,row))<2**power-1:
                raise ArithmeticError('The middle-coordinate induction condition failed')
        controls.append({'power':power,'all_raw_column_variables':3*12**power,
                         'equations':[{'target_rows':list(p),'residual':export_polynomial(q)}
                                      for p,q in zip(points,equations)]})
        points=tuple(lift_point(power,p) for p in points)
        expected=tuple(lift_polynomial(power,p) for p in equations)
    return {'field':'Every characteristic-zero field','claim':'AI-SPIN-FIBER-COMPRESSION-118',
            'family':'Independent scalar on every raw column of each fixed spin tensor-power map, followed by its prescribed binary-radix convolution fiber projection',
            'target':'M_(3^k) from A(2^k,2^k), for every integer k>=2',
            'finite_induction_controls':controls,'base_equation_divisors':list(DIVISORS),
            'normalized_bezout_identity_for_one':bezout_identity(),
            'all_power_argument':'Written induction in spin_fiber_compression.md; finite controls are not a substitute for the induction',
            'ordinary_family_excluded':True,'arbitrary_source_maps_excluded':False,
            'laurent_limits_addressed_by_this_certificate':False,
            'laurent_followup':'spin_fiber_closure.md','new_exponent_established':False}


def verify(saved=None):
    if saved is None:saved=json.loads(OUTPUT.read_text())
    actual=report()
    if actual!=saved:raise ArithmeticError('The saved ordinary certificate does not replay')
    return actual


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args=parser.parse_args()
    if args.write:OUTPUT.write_text(json.dumps(report(),indent=2)+'\n')
    else:verify()
    print('Five exact equations and the saved all-power controls pass.')
