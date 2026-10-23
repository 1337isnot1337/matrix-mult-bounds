"""Exact controls for the explicit one-unit convolution source family."""
from pathlib import Path
import argparse,importlib.util,json,random
import sympy as s
spec=importlib.util.spec_from_file_location('atom_rank_control_family',Path(__file__).with_name('distinct_atoms.py'));rr=importlib.util.module_from_spec(spec);spec.loader.exec_module(rr)
x,z=s.symbols('x z')
def build(a,b,seed):
 rng=random.Random(seed)
 def poly(v,n):return sum(rng.randint(-2,2)*v**i for i in range(n))
 A=1+z*poly(z,b-2) if b>2 else s.Integer(1);C=1+x*poly(x,a-2) if a>2 else s.Integer(1)
 B=[poly(z,b) for _ in range(a-1)]+[z*A];D=[poly(x,a) for _ in range(a-1)]+[x*C]
 return A,C,B,D

def sequence(A,C,B,D,a,b):
 return [s.expand(sum(B[r]*D[a-1+k-r] for r in range(k,a))+(A*C if k==0 else 0)) if k<a else s.Integer(0) for k in range(a+b-1)]
def factor(B,D,A,C,a,b):
 U=s.zeros(a,a+1);V=s.zeros(a+1,b);U[0,0]=A;V[0,0]=C
 for p in range(a):
  for h in range(1,a+1):
   if 0<=p+a-h<a:U[p,h]=B[p+a-h]
 for h in range(1,a+1):
  for q in range(b):
   if h-1+q<a:V[h,q]=D[h-1+q]
 return U,V

def control(a,b,seed=17,full_source=True):
 A,C,B,D=build(a,b,seed);f=sequence(A,C,B,D,a,b);U,V=factor(B,D,A,C,a,b);UV=U*V
 for p in range(a):
  for q in range(b):assert s.expand(UV[p,q]-f[p+q])==0
 c=s.zeros(a+1,1);c[1]=1;c[0]=-z;d=s.zeros(a+1,1);d[a]=1;d[0]=-x
 assert all(s.expand(t)==0 for t in U*c) and all(s.expand(t)==0 for t in d.T*V);assert (d.T*c)[0]==x*z
 UF=[[int(s.Poly(U[p,h],z).nth(ss)) for h in range(a+1)] for p in range(a) for ss in range(b)]
 VF=[[int(s.Poly(V[h,q],x).nth(i)) for q in range(b) for i in range(a)] for h in range(a+1)]
 assert rr.rank_mod(UF)==rr.rank_mod(VF)==a+1
 symbol=[[int(f[p+q].subs({x:1,z:1})) for q in range(b)] for p in range(a)]
 # Use another exact point if A(1) or C(1) happened to vanish.
 point=1
 while rr.rank_mod(symbol)!=a:
  point+=1;symbol=[[int(f[p+q].subs({x:point,z:point})) for q in range(b)] for p in range(a)]
 # A nontrivial truncated-unit gauge; verify every output coefficient.
 g=[s.Integer(2)]+[s.Integer((-1)**j) for j in range(1,a)];inv=[1/g[0]]
 for k in range(1,a):inv.append(-sum(g[j]*inv[k-j] for j in range(1,k+1))/g[0])
 br=B[::-1];dr=D[::-1]
 bg=[s.expand(sum(g[j]*br[k-j] for j in range(k+1))) for k in range(a)][::-1]
 dg=[s.expand(sum(inv[j]*dr[k-j] for j in range(k+1))) for k in range(a)][::-1]
 assert sequence(g[0]*A,C/g[0],bg,dg,a,b)==f
 result={'a':a,'b':b,'seed':seed,'full_hankel_entries_checked':a*b,'kernel_pairing':'xz','coefficient_factor_ranks_mod_65519':[a+1,a+1],'symbol_rank_mod_65519':a,'symbol_evaluation_point':point,'gauge_identity_checked':True,'family_dimension':a*b+a*a-a-2,'generic_source_rank_from_proved_criterion':a*a*b+1}
 if full_source:
  m=a+b-1;N=a*b*m;coeff=[s.Poly(t,x,z) for t in f];M=s.zeros(N)
  for j in range(b):
   for p in range(a):
    for L in range(m):
     for H in range(m):
      for q in range(b):
       for r in range(a):
        if 0<=H-j<a and 0<=L-r<b:M[(j*a+p)*m+L,(H*b+q)*a+r]=coeff[p+q].coeff_monomial(x**(H-j)*z**(L-r))
  from sympy.polys.matrices import DomainMatrix
  rank=int(DomainMatrix.from_Matrix(M).convert_to(s.QQ).rank());assert rank==rr.rank_mod(M.tolist())==a*a*b+1;result['full_source_rank_over_Q']=rank
 return result

def report():return {'status':'explicit source-slice family; written dimension proof unreviewed; no matrix target or exponent gain','controls':[control(2,3),control(3,4),control(8,10,full_source=False)]}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=report();a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
