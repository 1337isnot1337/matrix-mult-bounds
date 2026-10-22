"""Exact unimodular slices and finite reduced determinant certificates.

No numerical arithmetic or optional discovery dependency is used here.
"""

import argparse
from itertools import product
import json
from pathlib import Path
from random import Random

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
RESULTS=ROOT/'results/cyclic-slice-determinants-2026-10-21'


def source_matrix(a,coefficients,prime=None):
    n=a*a*(2*a-1)
    if type(a) is not int or a<1 or len(coefficients)!=n:
        raise ValueError('positive size and full coefficient vector required')
    rows=product(range(a),range(a),range(2*a-1))
    columns=list(product(range(2*a-1),range(a),range(a)))
    matrix=[]
    for j,p,L in rows:
        row=[]
        for H,q,r in columns:
            i,k,s=H-j,p+q,L-r
            value=coefficients[(i*(2*a-1)+k)*a+s] if 0<=i<a and 0<=s<a else 0
            row.append(value%prime if prime else value)
        matrix.append(row)
    return matrix


def integer_slice(a):
    return [int(i+s==a-1 and k==a-1)
            for i,k,s in product(range(a),range(2*a-1),range(a))]


def interval_blocks(a):
    """Finite controls for the all-size interval-block proof in proof.md."""
    if type(a) is not int or a<1:raise ValueError('positive integer size required')
    report=[]
    for t in range(1-a,2*a-1):
        js=[j for j in range(a) if 0<=t+j<2*a-1]
        rs=[r for r in range(a) if 0<=a-1-t+r<2*a-1]
        if len(js)!=len(rs):raise ArithmeticError('interval block is not square')
        B=[[int(0<=t+j-r<a) for r in rs] for j in js]
        n=len(B)
        if t<0:
            expected=[[int(c<=r) for c in range(n)] for r in range(n)]
            if B!=expected:raise ArithmeticError('lower interval block mismatch')
            kind='lower'
        elif t>=a:
            expected=[[int(c>=r) for c in range(n)] for r in range(n)]
            if B!=expected:raise ArithmeticError('upper interval block mismatch')
            kind='upper'
        else:
            difference=[B[0]]+[[x-y for x,y in zip(B[i],B[i-1])] for i in range(1,a)]
            pivots=[t]+list(range(t+1,a))+list(range(t))
            signs=[1]+[1]*(a-1-t)+[-1]*t
            for i in range(1,a):
                if difference[i]!=[signs[i]*int(c==pivots[i]) for c in range(a)]:
                    raise ArithmeticError('central row difference is not a signed unit')
            if difference[0][t]!=1:raise ArithmeticError('missing remaining unit pivot')
            kind='central'
        report.append({'parameter':t,'dimension':n,'kind':kind,'absolute_determinant':1})
    if sum(r['dimension'] for r in report)!=a*(2*a-1):
        raise ArithmeticError('interval dimensions do not cover the source')
    return report


def inverse(matrix,p):
    n=len(matrix)
    work=[[x%p for x in row]+[int(i==j) for j in range(n)]
          for i,row in enumerate(matrix)]
    for column in range(n):
        pivot=next((i for i in range(column,n) if work[i][column]),None)
        if pivot is None:raise ValueError('singular finite-field matrix')
        work[column],work[pivot]=work[pivot],work[column]
        factor=pow(work[column][column],-1,p)
        work[column]=[(x*factor)%p for x in work[column]]
        for i in range(n):
            if i!=column and work[i][column]:
                factor=work[i][column]
                work[i]=[(x-factor*y)%p for x,y in zip(work[i],work[column])]
    return [row[n:] for row in work]


def multiply(A,B,p):
    columns=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,column))%p for column in columns] for row in A]


def apply(matrix,vector,p):
    return [sum(x*y for x,y in zip(row,vector))%p for row in matrix]


def trim(f):
    f=list(f)
    while f and f[-1]==0:f.pop()
    return f


def add(f,g,p):
    return trim([((f[i] if i<len(f) else 0)+(g[i] if i<len(g) else 0))%p
                 for i in range(max(len(f),len(g)))])


def times(f,g,p):
    if not f or not g:return []
    out=[0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        for j,y in enumerate(g):out[i+j]=(out[i+j]+x*y)%p
    return trim(out)


def divide(f,g,p):
    f=trim(f);g=trim(g)
    if not g:raise ValueError('zero polynomial divisor')
    q=[0]*max(0,len(f)-len(g)+1);unit=pow(g[-1],-1,p)
    while len(f)>=len(g):
        k=len(f)-len(g);factor=f[-1]*unit%p;q[k]=factor
        for i,v in enumerate(g):f[i+k]=(f[i+k]-factor*v)%p
        f=trim(f)
    return trim(q),f


def bezout(f,g,p):
    old,r=list(f),list(g);u,v=[1],[];s,t=[],[1]
    while r:
        q,next_r=divide(old,r,p)
        old,r=r,next_r
        u,s=s,add(u,[-x%p for x in times(q,s,p)],p)
        v,t=t,add(v,[-x%p for x in times(q,t,p)],p)
    if len(old)!=1:raise ValueError('pencil characteristic polynomial is not squarefree')
    unit=pow(old[0],-1,p)
    return [x*unit%p for x in u],[x*unit%p for x in v]


def generate(a,prime=1009):
    n=a*a*(2*a-1);f0=integer_slice(a)
    rng=Random(20261021+a);f1=[rng.randrange(prime) for unused in range(n)]
    fixed_inverse=inverse(source_matrix(a,f0,prime),prime)
    A=multiply(fixed_inverse,source_matrix(a,f1,prime),prime)
    vector=[1]+[0]*(n-1);columns=[];current=vector
    for unused in range(n):
        columns.append(current);current=apply(A,current,prime)
    K=[list(row) for row in zip(*columns)]
    coefficients=[-x%prime for x in apply(inverse(K,prime),current,prime)]+[1]
    derivative=[i*coefficients[i]%prime for i in range(1,n+1)]
    u,v=bezout(coefficients,derivative,prime)
    f2=[rng.randrange(prime) for unused in range(n)]
    B=multiply(fixed_inverse,source_matrix(a,f2,prime),prime)
    AB,BA=multiply(A,B,prime),multiply(B,A,prime)
    inverse([[(x-y)%prime for x,y in zip(row,other)] for row,other in zip(AB,BA)],prime)
    return {'size':a,'dimension':n,'prime':prime,'first_slice':f0,'second_slice':f1,
            'commutator_slice':f2,
            'cyclic_vector':vector,'characteristic_coefficients_low_first':coefficients,
            'bezout_polynomial':u,'bezout_derivative':v,
            'scope':'Full source determinant reduced; no tensor-degeneration or exponent exclusion.'}


def verify(witness):
    a=witness['size'];n=a*a*(2*a-1);p=witness['prime']
    if a not in (2,3,4) or p!=1009 or witness['dimension']!=n:
        raise ValueError('unsupported finite source certificate')
    if witness['first_slice']!=integer_slice(a):raise ValueError('incorrect integer source slice')
    for values in [witness['second_slice'],witness['commutator_slice'],witness['cyclic_vector'],
                   witness['characteristic_coefficients_low_first'],
                   witness['bezout_polynomial'],witness['bezout_derivative']]:
        if any(type(x) is not int or not 0<=x<p for x in values):
            raise ValueError('invalid finite-field coefficient')
    if len(witness['cyclic_vector'])!=n:raise ValueError('incorrect cyclic vector format')
    fixed_inverse=inverse(source_matrix(a,witness['first_slice'],p),p)
    A=multiply(fixed_inverse,
               source_matrix(a,witness['second_slice'],p),p)
    columns=[];current=witness['cyclic_vector']
    for unused in range(n):
        columns.append(current);current=apply(A,current,p)
    K=[list(row) for row in zip(*columns)]
    inverse(K,p) # Full Krylov rank makes the relation the characteristic polynomial.
    f=witness['characteristic_coefficients_low_first']
    if len(f)!=n+1 or f[-1]!=1 or f[0]==0:raise ValueError('incorrect full-degree characteristic polynomial')
    if any((current[i]+sum(f[j]*columns[j][i] for j in range(n)))%p for i in range(n)):
        raise ValueError('Krylov characteristic relation failed')
    derivative=[i*f[i]%p for i in range(1,n+1)]
    identity=add(times(witness['bezout_polynomial'],f,p),
                 times(witness['bezout_derivative'],derivative,p),p)
    if identity!=[1]:raise ValueError('squarefree Bezout identity failed')
    B=multiply(fixed_inverse,source_matrix(a,witness['commutator_slice'],p),p)
    AB,BA=multiply(A,B,p),multiply(B,A,p)
    inverse([[(x-y)%p for x,y in zip(row,other)] for row,other in zip(AB,BA)],p)
    if witness['scope']!='Full source determinant reduced; no tensor-degeneration or exponent exclusion.':
        raise ValueError('incorrect mathematical scope')
    return {'size':a,'matrix_dimension':n,'krylov_rank':n,'determinant_pencil_degree':n,
            'normalized_commutator_rank':n,
            'pencil_squarefree':True,'global_source_determinant_reduced':True,
            'improves_omega':False}


def verify_report(report):
    if (report.get('proof_status')!='written; unreviewed'
            or report.get('improves_omega') is not False
            or [w.get('size') for w in report.get('witnesses',[])]!=[2,3,4]):
        raise ValueError('incorrect finite coverage or mathematical status')
    return [verify(w) for w in report['witnesses']]


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    if args.verify:
        report=json.loads(args.verify.read_text())
        print(json.dumps(verify_report(report),indent=2))
    else:
        report={'witnesses':[generate(a) for a in (2,3,4)],'proof_status':'written; unreviewed',
                'improves_omega':False}
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(verify_report(report),indent=2))
