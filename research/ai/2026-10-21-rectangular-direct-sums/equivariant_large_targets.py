"""Exact SL2 representation-capacity screen for two odd-vertex targets."""
from collections import Counter
import json

def odd_partitions(n,minimum=1):
 if not n:yield ()
 for k in range(minimum,n+1,2):
  for p in odd_partitions(n-k,k):yield(k,)+p

def source_multiplicities(a,b):
 out=Counter();degree=a+b-2
 for d in range(abs(a-b),degree+1,2):
  for k in range(abs(degree-d)//2,(degree+d)//2+1):out[k]+=1
 assert sum(v*(2*k+1) for k,v in out.items())==a*b*(a+b-1)
 return out

def compatible(U,V,S):
 if max(U)+max(V)>max(S):return False
 if sum(U[k]*V[k] for k in U)>S[0]:return False
 out=Counter()
 for a,ma in U.items():
  for b,mb in V.items():
   for c in range(abs(a-b),a+b+1):
    out[c]+=ma*mb
    if out[c]>S[c]:return False
 return True

def screen(a,b,target):
 assert any(d%2 for d in target), 'Both parity sectors needed for all-even targets'
 S=source_multiplicities(a,b)
 P=[list(odd_partitions(d)) for d in target]
 reps=[[Counter((d-1)//2 for d in p) for p in ps] for ps in P]
 pairs=[]
 for leg in range(3):
  left,right=leg,(leg+1)%3
  pairs.append({(i,j) for i,U in enumerate(reps[left]) for j,V in enumerate(reps[right]) if compatible(U,V,S)})
 triples=[]
 for i,j in sorted(pairs[0]):
  for jj,k in sorted(pairs[1]):
   if jj==j and (k,i) in pairs[2]:triples.append([list(P[0][i]),list(P[1][j]),list(P[2][k])])
 return {'source':[a,b],'target':list(target),'source_half_degree_multiplicities':{str(k):v for k,v in sorted(S.items())},
         'vertex_representation_counts':[len(p) for p in P],
         'compatible_ordered_pair_counts':[len(p) for p in pairs],
         'compatible_pairs':[[[list(P[i][u]),list(P[(i+1)%3][v])] for u,v in sorted(ps)] for i,ps in enumerate(pairs)],
         'compatible_triples':triples,'scope':'diagonal SL2 matrix-vertex intertwining ansatz only'}

def report():return {'status':'exact representation-capacity exclusion, not a general target obstruction',
                     'controls':[screen(7,12,(35,35,35)),screen(7,13,(37,38,38))],
                     'improves_omega':False,'independent_review':False}
if __name__=='__main__':print(json.dumps(report(),indent=2))
