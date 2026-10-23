"""Exact finite controls for the moving double-plus-simple support family."""
from pathlib import Path
from math import prod
import argparse,importlib.util,json,random
import sympy as s
from sympy.polys.matrices import DomainMatrix
spec=importlib.util.spec_from_file_location('multiple_support_rank',Path(__file__).with_name('distinct_atoms.py'));r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
x,z=s.symbols('x z')
def control(a,b,full_source=False):
 rng=random.Random(314159)
 def poly(t,n):return 1+sum(rng.randint(-2,2)*t**j for j in range(1,n))
 A=poly(z,b-1);C=poly(x,a-1);B=poly(z,b);D=poly(x,a)
 G0=s.expand(A*C+x*C*B+z*A*D);G1=s.expand(x*z*A*C)
 H=[s.expand(poly(x,a)*poly(z,b)) for _ in range(a-2)];nodes=list(range(1,a));m=a+b-1
 f=[s.expand(nodes[0]**k*G0+(k*nodes[0]**(k-1)*G1 if k else 0)+sum(t**k*h for t,h in zip(nodes[1:],H))) for k in range(m)]
 def vand(length):return s.Matrix([[nodes[0]**p,p*nodes[0]**(p-1) if p else 0]+[t**p for t in nodes[1:]] for p in range(length)])
 V=vand(a);W=vand(b);assert V.det()!=0;J=s.zeros(a);J[0,0]=G0;J[0,1]=J[1,0]=G1
 for j,h in enumerate(H,2):J[j,j]=h
 product_matrix=V*J*W.T
 assert all(s.expand(product_matrix[p,q]-f[p+q])==0 for p in range(a) for q in range(b))
 t=s.Symbol('t');rec=s.Poly((t-nodes[0])**2*s.prod(t-h for h in nodes[1:]),t);rec_coeff=[rec.nth(j) for j in range(a+1)]
 assert all(s.expand(sum(rec_coeff[j]*f[k+j] for j in range(a+1)))==0 for k in range(m-a))
 coeff=[s.Poly(t,x,z) for t in f]
 T=[[int(coeff[p+q].coeff_monomial(x**i*z**ss)) for q in range(b) for i in range(a)] for p in range(a) for ss in range(b)]
 assert r.rank_mod(T)==a+1
 point=1
 while r.rank_mod([[int(f[p+q].subs({x:point,z:point})) for q in range(b)] for p in range(a)])!=a:point+=1
 out={'a':a,'b':b,'support_points':nodes,'multiplicities':[2]+[1]*(a-2),'confluent_vandermonde_determinant':int(V.det()),'full_symbol_entries_checked':a*b,'crossed_rank_mod_65519':a+1,'scalar_symbol_rank_mod_65519':a,'evaluation_point':point,'recurrence_coefficients':[int(v) for v in rec_coeff],'recurrence_shifts_checked':m-a,'source_rank_from_block_proof':a*a*b+1,'fixed_support_family_dimension':a*(a+b-1)-2,'moving_support_family_dimension':a*(a+b)-3}
 if full_source:
  N=a*b*m;M=s.zeros(N)
  for j in range(b):
   for p in range(a):
    for L in range(m):
     for HH in range(m):
      for q in range(b):
       for rr in range(a):
        if 0<=HH-j<a and 0<=L-rr<b:M[(j*a+p)*m+L,(HH*b+q)*a+rr]=coeff[p+q].coeff_monomial(x**(HH-j)*z**(L-rr))
  rank=int(DomainMatrix.from_Matrix(M).convert_to(s.QQ).rank());assert rank==a*a*b+1;out['complete_source_rank_over_Q']=rank
 return out

def span_control(a=8,b=10):
 m=a+b-1;nodes=list(range(100,100+m));det=prod(nodes[j]-nodes[i] for i in range(m) for j in range(i+1,m));V=[[t**k for t in nodes] for k in range(m)];assert r.rank_mod(V)==m and det!=0
 return {'a':a,'b':b,'long_points':nodes,'vandermonde_determinant':str(det),'long_rank_mod_65519':m,'separable_biform_monomials':a*b,'certified_linear_span_dimension':a*b*m,'uses_boundary_specializations':True}
def report():return {'status':'explicit moving-support source family; no target maps or smaller exponent','controls':[control(3,4,True),control(8,10)],'full_span_certificate':span_control()}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();v=report();a.output.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps(v,indent=2))
