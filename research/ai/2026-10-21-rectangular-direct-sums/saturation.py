"""Finite certificates for the rank-three saturation obstruction.

The general projection/torus arguments are written in saturation.md.
This file certifies the two finite Hankel-space bounds, not those proofs.
"""
from itertools import combinations
from pathlib import Path
import argparse
import json
from math import comb

PRIME = 101
SEED = 271828


def next_state(state):
    return (1664525*state+1013904223) % (2**32)


def draw(state, support, length):
    h=[0]*length
    for k in support:
        state=next_state(state)
        h[k]=1+state%(PRIME-1)
    return state,h


def pivot_columns(matrix):
    A=[row[:] for row in matrix]
    i=0;piv=[]
    for j in range(len(A[0])):
        k=next((k for k in range(i,len(A)) if A[k][j]%PRIME),None)
        if k is None: continue
        A[i],A[k]=A[k],A[i]
        inv=pow(A[i][j]%PRIME,-1,PRIME)
        A[i]=[(x*inv)%PRIME for x in A[i]]
        for k in range(i+1,len(A)):
            c=A[k][j]%PRIME
            A[k]=[(x-c*y)%PRIME for x,y in zip(A[k],A[i])]
        piv.append(j);i+=1
        if i==len(A):break
    return piv


def determinant(matrix):
    """Independent integer Bareiss replay, not the modular generator."""
    A=[row[:] for row in matrix]; n=len(A); sign=1; previous=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((i for i in range(k+1,n) if A[i][k]),None)
            if p is None:return 0
            A[k],A[p]=A[p],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator%previous==0
                A[i][j]=numerator//previous
        for i in range(k+1,n):A[i][k]=0
        previous=pivot
    return sign*A[-1][-1]


def generate(a,b):
    assert a<=b
    length=a+b-1;state=SEED;certs=[]
    for support in combinations(range(length),a):
        for attempt in range(1,101):
            state,h=draw(state,support,length)
            matrix=[[h[i+j] for j in range(b)] for i in range(a)]
            cols=pivot_columns(matrix)
            if len(cols)==a:
                certs.append([attempt,sum(1<<j for j in cols)])
                break
        else:raise AssertionError(('No witness found',support))
    return {'a':a,'b':b,'rank_cap':a-1,'seed':SEED,'prime':PRIME,
            'ordered_supports':'lexicographic combinations(range(a+b-1), a)',
            'certificates':certs}


def verify(record):
    a,b=record['a'],record['b'];length=a+b-1
    assert 2 <= a <= b
    assert record['rank_cap']==a-1 and record['seed']==SEED and record['prime']==PRIME
    supports=list(combinations(range(length),a))
    assert len(record['certificates'])==len(supports)==comb(length,a)
    state=SEED
    for support,(attempt,mask) in zip(supports,record['certificates']):
        assert 1<=attempt<=100 and 0<=mask<2**b
        for _ in range(attempt):state,h=draw(state,support,length)
        cols=[j for j in range(b) if mask>>j&1]
        assert len(cols)==a
        minor=[[h[i+j] for j in cols] for i in range(a)]
        det=determinant(minor)
        assert det%PRIME != 0, ('bad witness',support)
    return {'format':[a,b],'coordinate_spaces_certified':len(supports),
            'maximum_vector_dimension_of_bounded_rank_space':a-1,
            'verification':'independent integer determinant per support'}


def exclusion(a,b,shapes,dimensions):
    """Return the concrete saturated-symbol contradiction, if certified."""
    if (a,b) not in [(7,9),(8,8)]:return None
    ab=a*b;size=ab*(a+b-1);rank_cap=a-1
    for block,(m,n,p) in enumerate(shapes):
        dims=(m*n,n*p,p*m); third=(p,m,n)
        for leg in range(3):
            # If a block has a short index below three, rank<=3 already
            # contains every parameter. The same (looser) bound is safe.
            lift=3*third[leg]+2*size-sum(dimensions)+dimensions[leg]
            if dims[leg]>rank_cap*ab and lift<(rank_cap+1)*ab:
                return {'block':block,'leg':leg,'rank_three_lift_upper':lift,
                        'next_symbol_rank_threshold':(rank_cap+1)*ab,
                        'block_parameter_dimension':dims[leg],
                        'full_symbol_injection_cap':rank_cap*ab}
    return None


def refine(frontier):
    records=[]
    for rec in frontier:
        if not rec['surviving_targets']:continue
        excluded=[];remaining=[]
        for target in rec['surviving_targets']:
            witness=exclusion(rec['a'],rec['b'],target['shapes'],target['leg_dimensions'])
            if witness is None:remaining.append(target)
            else:excluded.append({'shapes':target['shapes'],'witness':witness})
        records.append({'a':rec['a'],'b':rec['b'],
                        'previous_survivors':len(rec['surviving_targets']),
                        'excluded':excluded,'remaining':remaining})
    return records

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--directory',type=Path,required=True)
    args=parser.parse_args();args.directory.mkdir(parents=True,exist_ok=True)
    certificates=[generate(7,9),generate(8,8)]
    summaries=[verify(c) for c in certificates]
    (args.directory/'hankel-coordinate-certificates.json').write_text(json.dumps(certificates,separators=(',',':'))+'\n')
    frontier=json.loads((args.directory/'frontier.json').read_text())
    refined=refine(frontier)
    (args.directory/'saturation.json').write_text(json.dumps({'hankel_space_verification':summaries,'target_refinement':refined},indent=2)+'\n')
    print(summaries)
    print([(r['a'],r['b'],len(r['excluded']),len(r['remaining'])) for r in refined])
