"""Finite exact controls for the distinct-atom slice-rank formula."""
from math import prod
from pathlib import Path
import json
import sympy as s

def rank_mod(rows,p=65519):
 A=[[int(x)%p for x in row] for row in rows];rank=0
 for j in range(len(A[0])):
  k=next((k for k in range(rank,len(A)) if A[k][j]),None)
  if k is None:continue
  A[rank],A[k]=A[k],A[rank];v=pow(A[rank][j],-1,p);A[rank]=[(x*v)%p for x in A[rank]]
  for k in range(rank+1,len(A)):
   if A[k][j]:
    v=A[k][j];A[k]=[(x-v*y)%p for x,y in zip(A[k],A[rank])]
  rank+=1
  if rank==len(A):break
 return rank

def control(a,b,kind):
 n=a+1;m=a+b-1;N=a*b*m;x=s.Symbol('x');nodes=list(range(1,n+1))
 u=[s.Poly(1+(h+1)*x**(a-1),x) for h in range(n)]
 if kind=='common':v=[s.Poly((h+1)*(1+x**(b-1)),x) for h in range(n)]
 elif kind=='one_extra':v=[s.Poly((x+1)**(b-2)*(x+2+int(h==n-1)),x) for h in range(n)]
 else:v=[s.Poly(1+(h+1)*x**(b-1),x) for h in range(n)]
 uc=[[int(f.nth(i)) for i in range(a)] for f in u];vc=[[int(f.nth(i)) for i in range(b)] for f in v]
 P=s.zeros(N,n*a*b);Q=s.zeros(n*a*b,N)
 for h,t in enumerate(nodes):
  for j in range(b):
   for r in range(a):
    z=(h*b+j)*a+r
    for p in range(a):
     for ss in range(b):P[(j*a+p)*m+ss+r,z]=t**p*vc[h][ss]
    for q in range(b):
     for i in range(a):Q[z,((i+j)*b+q)*a+r]=t**q*uc[h][i]
 M=P*Q;F={(i,k,ss):sum(uc[h][i]*nodes[h]**k*vc[h][ss] for h in range(n)) for i in range(a) for k in range(m) for ss in range(b)}
 for j in range(b):
  for p in range(a):
   for L in range(m):
    for H in range(m):
     for q in range(b):
      for r in range(a):assert M[(j*a+p)*m+L,(H*b+q)*a+r]==F.get((H-j,p+q,L-r),0)
 l=s.lcm([f.as_expr() for f in v]);degree=s.degree(l,x);delta=max(0,a+min(f.degree() for f in v)-degree);predicted=int(b*(a*n-delta));lower=rank_mod(M.tolist());assert lower==predicted
 small=P[:a*m,:];exact_small=int(small.rank());assert b*exact_small==predicted
 return {'a':a,'b':b,'case':kind,'source_dimension':N,'lcm_degree':int(degree),'kernel_per_copy':int(delta),'predicted_slice_rank':predicted,'modular_rank':lower,'exact_small_rank':exact_small,'original_entries_checked':N*N,'factorization_checked':True}

def sharp_large_control():
 a,b=8,10;n=a+1;m=a+b-1;x=s.Symbol('x')
 v=[s.Poly((x+1)**8*(x+2+int(h==8)),x) for h in range(n)]
 P=[[0]*(n*a) for _ in range(a*m)]
 C=[[0]*n for _ in range(a*b)]
 for h in range(n):
  for p in range(a):
   for ss in range(b):
    value=(h+1)**p*int(v[h].nth(ss));C[p*b+ss][h]=value
    for r in range(a):P[p*m+ss+r][h*a+r]=value
 p_rank=rank_mod(P);cross_rank=rank_mod(C)
 assert p_rank==65 and cross_rank==9
 return {'a':a,'b':b,'nodes':list(range(1,10)),'u_polynomials':'all1','v_polynomials':'first eight (z+1)^8*(z+2); last (z+1)^8*(z+3)','small_factor_modular_rank':p_rank,'crossed_left_factor_modular_rank':cross_rank,'source_rank_from_proved_factorization':b*p_rank,'sharp_gap_attained':True}

def report():
 return {'status':'finite controls for written unreviewed distinct-atom lemma; no exponent gain','controls':[control(a,a+1,k) for a in (2,3) for k in ('common','one_extra','generic')],'sharp_large_control':sharp_large_control(),'a8_b10_crossed_rank9_minimum':650,'ordinary_candidate_ceiling':641,'general_counterexample_rank641_retained':True}
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args();r=report();args.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
