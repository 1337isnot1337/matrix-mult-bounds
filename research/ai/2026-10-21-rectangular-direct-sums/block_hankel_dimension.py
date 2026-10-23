"""Exact finite controls; the general dimension argument is in the companion note."""
from pathlib import Path
import importlib.util
from math import comb, isqrt
import random
import json
spec=importlib.util.spec_from_file_location('hankel_dim_rank',Path(__file__).with_name('equality_counterexample.py'))
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
rank=h.rank

def coherent_cover(L=8,M=9,q=8):
 # Deliberately make the first L charts fail: each has one supported coherent row.
 V=[]
 for lam in range(L):
  v=[0]*q;v[lam%q]=1
  V.append([(-lam)**(M-1-j)*v[i] for j in range(M) for i in range(q)])
 assert rank(V)==L
 chart_ranks=[]
 for lam in range(M):
  W=[[sum(row[j*q+i]*comb(M-1-k,j-k)*lam**(j-k) for j in range(k,M))
       for k in range(M-1) for i in range(q)] for row in V]
  chart_ranks.append(rank(W))
 assert chart_ranks==[L-1]*L+[L]
 return chart_ranks

def exceptional_control(L=8,M=9,p=9,q=8):
 rng=random.Random(271828)
 seq=[[rng.randrange(-5,6) for _ in range(q)] for _ in range(L+M-1)]
 V=[[seq[i+j][t] for j in range(M) for t in range(q)] for i in range(L)]
 assert rank(V)==L and rank([v[:(M-1)*q] for v in V])==L
 c=list(range(1,p+1))
 U=[[c[s] if j==i else 0 for j in range(L)] for i in range(L) for s in range(p)]
 increments=[rank(U[:i*p]) for i in range(1,L+1)]
 assert increments==list(range(1,L+1))
 # Complete coefficient verification for the factorization.
 for i in range(L):
  for j in range(M):
   for s in range(p):
    for t in range(q):
     assert sum(U[i*p+s][k]*V[k][j*q+t] for k in range(L))==c[s]*seq[i+j][t]
 return {'row_prefix_ranks':increments,'right_truncated_rank':L,
         'component_dimension':q*(L+M-1)+p-1}

def exclusion(a,b,shapes,D,k=None):
 if not a<=b:return None
 if k is None:k=isqrt(2*a-1)
 if not 2*(a-1)<k*(k+2):return None
 cap=max(a*(a+b),a*(a+b-1)+b-1,(b*(a+b-1)+a-1) if a==b else 0);ab=a*b;N=ab*(a+b-1)
 for j,(m,n,p) in enumerate(shapes):
  for i,(u,v,t) in enumerate(((m,n,p),(n,p,m),(p,m,n))):
   if k>min(u,v):continue
   upper=k*t+2*N-sum(D)+D[i]
   dim=k*(u+v-k)
   # The caller must supply the finite rank-(a-1) Hankel linear-space certificate.
   if u*v>(a-1)*ab and upper<=a*ab and dim>cap:
    return {'block':j,'leg':i,'parameter_rank_cap':k,'lift_upper':upper,
            'full_symbol_equality_threshold':a*ab,'determinantal_dimension':dim,
            'crossed_hankel_dimension_cap':cap,'lower_symbol_space_cap':(a-1)*ab}
 return None

def square_input_control(M=9,q=9):
 V=[[int(j==k and i==0) for j in range(M) for i in range(q)] for k in range(M)]
 ranks=[]
 for lam in range(M+1):
  W=[[sum(row[j*q+i]*comb(M-1-k,j-k)*lam**(j-k) for j in range(k,M))
       for k in range(M-1) for i in range(q)] for row in V]
  ranks.append(rank(W))
 assert ranks==[M-1]*(M+1)
 return {'chart_ranks':ranks,'common_input_component_dimension':M*(2*M-1)+q-1}

def report():
 w=exclusion(8,9,[(30,30,30),(3,3,3)],[909]*3)
 assert w and w['determinantal_dimension']==171 and w['crossed_hankel_dimension_cap']==136
 assert exclusion(8,10,[(32,33,33),(8,3,3)],[1080,1098,1080]) is None
 assert exclusion(9,9,[(32,33,33),(4,2,2)],[1064,1093,1064]) is not None
 return {'coherent_chart_ranks':coherent_cover(),'exceptional_component':exceptional_control(),'square_input_exception':square_input_control(),
         'M30_plus_M3_exclusion':w,'status':'finite controls; written general proof unreviewed'}

if __name__=='__main__':print(json.dumps(report(),indent=2))
