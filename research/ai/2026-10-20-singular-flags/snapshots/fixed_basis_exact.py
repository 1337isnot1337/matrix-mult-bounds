"""Exact finite discovery with a fixed nondiagonal first-input basis."""
import argparse
from fractions import Fraction
from math import lcm, comb, factorial
import hashlib
import json
import os
from pathlib import Path
import z3


def points(m):
    return [(a, d-a) for d in range(m) for a in range(d+1)]


def verify(w):
    m, B, A = w['m'], w['B'], w['shared_matrix']
    pts = points(m)
    C = [[Fraction(x) for x in row] for row in w['output_matrix']]
    yp = w['source_y_indices']
    if len(set(yp)) != len(pts) or any(j < 0 or j >= B for j in yp):
        raise ArithmeticError('invalid injection')
    count = 0
    for p in range(m):
        for y, (a,b) in enumerate(pts):
            for z,(c,d) in enumerate(pts):
                expected = int(p==a+c and a+b+c+d==m-1)
                if w.get('basis_model') == 'reverse-Newton':
                    import sympy as sp
                    t=sp.Symbol('t'); j=yp[y]
                    polynomial=sp.Poly(sp.prod(t-i for i in range(m-1-p))*sp.prod(t-i for i in range(j)),t)
                    remainder=polynomial
                    coefficients=[0]*(B+m-1)
                    # Independent triangular conversion, without the discovery product formula.
                    for degree in range(polynomial.degree(),-1,-1):
                        coefficient=remainder.nth(degree)
                        coefficients[degree]=int(coefficient)
                        remainder-=sp.Poly(coefficient*sp.prod(t-i for i in range(degree)),t)
                    if not remainder.is_zero:raise ArithmeticError('Newton conversion failed')
                    value=sum(coefficients[k]*C[z][k] for k in range(B+m-1))
                else:
                    value = sum(Fraction(A[p][r])*C[z][yp[y]+r] for r in range(m))
                weight = w['weights']['x'][p]+w['weights']['y'][y]+w['weights']['z'][z]
                if value and weight<0:
                    raise ArithmeticError('negative supported coefficient')
                if weight==0 and value!=expected:
                    raise ArithmeticError('wrong leading coefficient')
                if expected and weight!=0:
                    raise ArithmeticError('wrong desired weight')
                count+=1
    return {'coefficients_checked':count, 'exact_rational_verified':True}


def search(m,B,A,timeout_ms,seed,query_path,basis_model='monomial'):
    pts=points(m);N=len(pts)
    solver=z3.Solver();solver.set(timeout=timeout_ms,random_seed=seed)
    yp=[z3.Int(f'y{i}') for i in range(N)]
    eta=[z3.Real(f'eta{i}') for i in range(m)]
    C=[z3.Array(f'C{z}',z3.IntSort(),z3.RealSort()) for z in range(N)]
    solver.add(z3.Distinct(*yp),*[z3.And(j>=0,j<B) for j in yp],eta[0]==0)
    for z,(c,d) in enumerate(pts):
        sector=m-c-d
        for y,(a,b) in enumerate(pts):
            for p in range(m):
                wanted=(a+b+1==sector and p==a+c)
                weight=p-a-c+eta[a+b]-eta[sector-1]
                if basis_model=='reverse-Newton':
                    degree=m-1-p
                    for j in range(B):
                        coeff=z3.Sum(*[comb(degree,r)*comb(j,r)*factorial(r)*z3.Select(C[z],degree+j-r)
                                       for r in range(min(degree,j)+1)])
                        solver.add(z3.Or(yp[y]!=j,coeff==1) if wanted else
                                   z3.Or(yp[y]!=j,weight>0,coeff==0))
                else:
                    coeff=z3.Sum(*[A[p][r]*z3.Select(C[z],yp[y]+r)
                                   for r in range(m) if A[p][r]])
                    solver.add(coeff==1 if wanted else z3.Or(weight>0,coeff==0))
    query=solver.to_smt2();query_path.write_text(query)
    result=solver.check()
    report={'m':m,'B':B,'shared_matrix':A,'basis_model':basis_model,'solver':z3.get_version_string(),
            'seed':seed,'timeout_ms':timeout_ms,'result':str(result),
            'query_sha256':hashlib.sha256(query.encode()).hexdigest(),
            'scope':'Fixed shared basis followed by singular diagonal weights; coordinate injection on Y; arbitrary constant output matrix.',
            'improves_omega':False}
    if result==z3.sat:
        model=solver.model()
        def fraction(v):
            v=model.eval(v,model_completion=True)
            return Fraction(v.numerator_as_long(),v.denominator_as_long())
        offsets=[fraction(v) for v in eta]
        scale=lcm(*(v.denominator for v in offsets))
        weights={'x':[p*scale for p in range(m)],
                 'y':[-a*scale+int(offsets[a+b]*scale) for a,b in pts],
                 'z':[-c*scale-int(offsets[m-1-c-d]*scale) for c,d in pts]}
        witness={'m':m,'B':B,'shared_matrix':A,'basis_model':basis_model,
                 'source_y_indices':[model.eval(v).as_long() for v in yp],
                 'output_matrix':[[str(fraction(z3.Select(row,k))) for k in range(B+m-1)] for row in C],
                 'weights':weights}
        report['witness']=witness;report['verification']=verify(witness)
    elif result==z3.unknown:
        report['reason_unknown']=solver.reason_unknown()
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--basis',choices=['identity2','hadamard4','newton2','newton4'],required=True)
    p.add_argument('--timeout-ms',type=int,default=45000);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    basis_model='monomial'
    if args.basis=='identity2':m=2;A=[[1,0],[0,1]]
    elif args.basis=='hadamard4':m=4;A=[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]
    else:
        import sympy as sp
        m=int(args.basis[-1]);t=sp.Symbol('t');basis_model='reverse-Newton'
        A=[[int(sp.Poly(sp.prod(t-i for i in range(m-1-p)),t).nth(r)) for r in range(m)] for p in range(m)]
    seed=int.from_bytes(os.urandom(4),'big')&0x7fffffff
    report=search(m,m*(m+1)//2,A,args.timeout_ms,seed,args.output.with_suffix('.smt2'),basis_model)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='witness'},indent=2))
