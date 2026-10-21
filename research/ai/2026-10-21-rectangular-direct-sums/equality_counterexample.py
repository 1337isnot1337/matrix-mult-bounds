"""Exact counterexample to extending fixed-scheme equality to full row rank."""
from fractions import Fraction
import json

def rank(A):
 A=[[Fraction(x) for x in row] for row in A];i=0
 for j in range(len(A[0])):
  k=next((k for k in range(i,len(A)) if A[k][j]),None)
  if k is None:continue
  A[i],A[k]=A[k],A[i];p=A[i][j];A[i]=[x/p for x in A[i]]
  for k in range(i+1,len(A)):
   c=A[k][j];A[k]=[x-c*y for x,y in zip(A[k],A[i])]
  i+=1
  if i==len(A):break
 return i

def small_report():
 a,b,m=2,3,4
 coeff={(0,3,0):1,(1,1,0):1}
 rows=[(j,p,L) for j in range(b) for p in range(a) for L in range(m)]
 cols=[(H,q,r) for H in range(m) for q in range(b) for r in range(a)]
 M=[[coeff.get((H-j,p+q,L-r),0) for H,q,r in cols] for j,p,L in rows]
 recurrence=[[0,0,0],[0,0,1],[0,1,0],[1,0,0]]
 assert rank(M)==12==2*a*b
 assert rank(recurrence)==3
 # Symbol [[0,x,0],[x,0,1]] has minor -x^2.
 return {'format':[a,b],'symbol_sequence':['0','x','0','1'],
         'exact_rational_slice_rank':rank(M),'symbol_rank':2,
         'common_quadratic_annihilator_matrix_rank':rank(recurrence),
         'conclusion':'No constant length-two scheme; full-row-rank equality does not imply one.',
         'scope':'Counterexample to a proposed extension, not to the existing a,b>=3 rank-two theorem.'}

def family_report(a=8):
 b=a+1;m=2*a
 h0=[sum(t**k for t in range(1,a+1)) for k in range(m)]
 h1=[(a+1)**k for k in range(m)]
 def entry(i,k):return h0[k] if i==0 else h1[k] if i==1 else 0
 rows=[(j,p) for j in range(b) for p in range(a)]
 cols=[(H,q) for H in range(m) for q in range(b)]
 block=[[entry(H-j,p+q) for H,q in cols] for j,p in rows]
 block_rank=rank(block)
 recurrence=[h[k:k+a+1] for h in (h0,h1) for k in range(a)]
 recurrence_rank=rank(recurrence)
 assert block_rank==a*b
 assert recurrence_rank==a+1
 return {'format':[a,b],'source_leg_dimension':a*b*m,
         'sequence':'f_k=sum(t**k for t=1..a)+x*(a+1)**k; k=0..2a-1',
         'exact_rational_block_rank':block_rank,'identical_blocks':a,
         'exact_rational_slice_rank':a*block_rank,'symbol_rank':a,
         'common_degree_a_annihilator_rank':recurrence_rank,
         'conclusion':'Equality at full symbol rank does not force a constant length-a scheme.'}

def report():
 return {'small_control':small_report(),'frontier_format':family_report()}

if __name__=='__main__':print(json.dumps(report(),indent=2))
