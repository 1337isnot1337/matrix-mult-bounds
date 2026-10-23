"""Finite checks of the bundle-dimension arithmetic and Cech indexing.

The splitting theorem and parameter-space proof are mathematical dependencies;
these controls do not independently verify them.
"""
from itertools import combinations_with_replacement
from math import isqrt
import json

def splitting_controls(maximum=5):
 checked=0;occurring_rank_range=0;zero_controls=0
 for p in range(1,maximum+1):
  for q in range(1,maximum+1):
   n=p+q;N=p*q*(n-1)
   zero=[-q]*p+[p]*q
   h1=lambda e:sum(max(x-y-1,0) for x in e for y in e)
   assert h1(zero)==N;zero_controls+=1
   for e in combinations_with_replacement(range(-q,p+1),n):
    if sum(e):continue
    s=sum(max(x,0) for x in e);c=h1(e)
    assert c>=n*s-n*n//4
    h0=sum(max(x-y+1,0) for x in e for y in e)
    assert h0-c==n*n
    assert p*n*(q+1)+q*q-h0==N-c
    r=p*q-s
    if r>=0:
     assert N-c<=r*n+(p-q)**2//4
     occurring_rank_range+=1
    checked+=1
 return {'splitting_types_checked':checked,'types_with_nonnegative_hankel_rank':occurring_rank_range,
         'zero_extension_controls':zero_controls,'maximum_p_q':maximum}

def cech_controls():
 total=0
 for p,q in [(1,1),(2,3),(3,2),(8,9),(9,8),(9,9),(10,8)]:
  # Track an independent symbol for every matrix coefficient.
  for row_block in range(q):
   for out in range(p):
    for col_block in range(p):
     for inp in range(q):
      obtained=[]
      for k in range(p+q-1):
       exponent=-k-1+col_block
       if -q<=exponent<=-1 and exponent==-row_block-1:
        obtained.append((k,out,inp))
      assert obtained==[(row_block+col_block,out,inp)]
      total+=1
 return total

def exclusion(a,b,shapes,D,k=None):
 if not 2<=a<=b:return None
 if k is None:k=isqrt(2*a-1)
 if not 2*(a-1)<k*(k+2):return None
 ab=a*b;N=ab*(a+b-1)
 for j,(m,n,p) in enumerate(shapes):
  for i,(u,v,t) in enumerate(((m,n,p),(n,p,m),(p,m,n))):
   if k>min(u,v) or u*v<=(a-1)*ab:continue
   lift=k*t+2*N-sum(D)+D[i]
   crossed=lift-(ab-1)*a
   if crossed<a:continue # The earlier strict saturation screen handles this case.
   cap=min(N,crossed*(a+b)+(a-b)**2//4);dim=k*(u+v-k)
   if dim>cap:
    return {'block':j,'leg':i,'parameter_rank_cap':k,'lift_upper':lift,
            'crossed_rank_cap':crossed,'determinantal_dimension':dim,
            'bundle_dimension_cap':cap,'lower_symbol_space_cap':(a-1)*ab}
 return None

def one_window_controls():
 checked=0
 for q in range(1,31):
  for r in range(q+1):
   exact=r*(2*q-r)
   cap=min(q*q,r*(q+1)+(q-1)**2//4)
   assert exact<=cap
   checked+=1
 return checked

def report():
 return {'integer_controls':splitting_controls(),'cech_entries_checked':cech_controls(),'generic_matrix_controls':one_window_controls(),
         'status':'finite checks; general bundle-extension proof unreviewed'}

if __name__=='__main__':print(json.dumps(report(),indent=2))
