"""Exact controls for the written critical finite-state obstruction."""
from itertools import combinations
from math import factorial,prod
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
x,z=s.symbols('x z')

def rank(M):return int(DomainMatrix.from_Matrix(M).convert_to(s.QQ).rank())

def partitions(n,minimum=1):
 if not n:yield ()
 for k in range(minimum,n+1):
  for p in partitions(n-k,k):yield (k,)+p

def incidence(rho):
 values=[]
 for k in range(3,rho+1):
  values.append(max(l*(8+k-l)+10*(k-l)-1+(rho-k)*17 for l in range(1,k)))
 if rho>=3:assert max(values)==17*rho-22
 return {'support_count':rho,'circuit_bounds':values,
         'eight_state_bad_dimension':136+rho-22 if rho>=3 else None,
         'nine_state_bad_dimension':137+rho-22 if 3<=rho<=7 else None}

def hermite_controls():
 out=[]
 for p in partitions(8):
  rho=len(p);base=8+rho
  count=0
  if rho<=7:
   for i,j in combinations(range(rho),2):
    mult=[e+1+int(h in (i,j)) for h,e in enumerate(p)]
    N=sum(mult);assert N<=17
    V=s.Matrix([[0 if k<t else factorial(k)//factorial(k-t)*(h+1)**(k-t)
                 for h,m in enumerate(mult) for t in range(m)] for k in range(N)])
    expected=prod(factorial(t) for m in mult for t in range(m))*prod((j-i)**(mult[i]*mult[j]) for i in range(rho) for j in range(i+1,rho))
    assert V.det(method='domain-ge')==expected and expected
    count+=1
  out.append({'partition':list(p),'discarded_jet_dimension':base,
              'pair_determinants_checked':count,'eight_simple_exception':rho==8})
 return out

def jordan_control(a,b,e,full=False,general=False):
 n=a+1;A=s.zeros(n)
 for j in range(e-1):A[j,j+1]=1
 for j in range(e+1,n):A[j,j]=j-e
 u=s.zeros(n,1);v=s.zeros(1,n);u[e-1]=x;v[0]=z;u[e]=v[e]=1
 for j in range(e+1,n):u[j]=v[j]=1
 if general:
  u[e-1]=(1+x)**(a-2)*(x+2);u[e]=(1+x)**(a-2)*(3*x+1)
  v[0]=(1+z)**(b-2)*(z+3);v[e]=(1+z)**(b-2)*(2*z+1)
  for j in range(e-1):u[j]=sum((j+k+1)*x**k for k in range(a))
  for j in range(1,e):v[j]=sum((j+k+2)*z**k for k in range(b))
 U=s.Matrix.vstack(*[v*A**p for p in range(a)])
 V=s.Matrix.hstack(*[A**q*u for q in range(b)])
 c=s.zeros(n,1);c[0]=1;c[e]=-z
 d=s.zeros(1,n);d[e-1]=1;d[e]=-x
 if general:
  c[0]=2*z+1;c[e]=-(z+3);d[e-1]=3*x+1;d[e]=-(x+2)
 assert all(s.expand(t)==0 for t in U*c) and all(s.expand(t)==0 for t in d*V)
 g=s.expand((d*c)[0]);expected=(x+2)*(z+3)+int(e==1)*(3*x+1)*(2*z+1) if general else x*z+int(e==1)
 assert s.expand(g-expected)==0
 moments=[s.Poly((v*A**k*u)[0],x,z) for k in range(a+b-1)]
 T=s.Matrix([[moments[p+q].coeff_monomial(x**i*z**ss) for q in range(b) for i in range(a)] for p in range(a) for ss in range(b)])
 assert rank(T)==n
 assert rank((U*V).subs({x:1,z:1}))==a
 out={'a':a,'b':b,'exceptional_block':e,'general_coefficients':general,'crossed_rank':n,'scalar_rank':a,
      'primitive_pairing':str(g),'source_rank_from_pairing_criterion':a*a*b+(a if e==1 else 1)}
 if full:
  m=a+b-1;N=a*b*m;M=s.zeros(N)
  for j in range(b):
   for p in range(a):
    for L in range(m):
     for H in range(m):
      for q in range(b):
       for rr in range(a):
        if 0<=H-j<a and 0<=L-rr<b:
         M[(j*a+p)*m+L,(H*b+q)*a+rr]=moments[p+q].coeff_monomial(x**(H-j)*z**(L-rr))
  out['complete_source_rank']=rank(M)
  assert out['complete_source_rank']==out['source_rank_from_pairing_criterion']
 return out

def report():
 return {'status':'finite controls for written obstruction under audit',
         'incidence':[incidence(rho) for rho in range(1,9)],
         'partitions':hermite_controls(),
         'jordan_controls':[jordan_control(3,4,e,True) for e in range(1,4)]+[jordan_control(8,10,e) for e in range(1,9)]+[jordan_control(3,4,2,True,True),jordan_control(8,10,4,False,True)],
         'fixed_eight_support_image_dimension':640,
         'six_fixed_plus_proportional_pair_dimension':560,
         'required_leg_dimension':1056,'rank_two_parameter_dimension':126,
         'improves_omega':False,'independent_review':False}
if __name__=='__main__':print(json.dumps(report(),indent=2))
