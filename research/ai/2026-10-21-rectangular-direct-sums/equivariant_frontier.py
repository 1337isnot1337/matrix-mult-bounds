"""Exact representation-capacity screen of the maintained ordinary frontier."""
import importlib.util,json,time
from pathlib import Path
from collections import Counter
from functools import lru_cache
root=Path(__file__).resolve().parents[3]
p=root/'research/ai/2026-10-21-rectangular-direct-sums/equivariant_large_targets.py';spec=importlib.util.spec_from_file_location('eq',p);v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
@lru_cache(None)
def parts(n,parity,minimum=0):
 if not n:return ((),)
 first=minimum or(1 if parity==0 else 2)
 return tuple((k,)+p for k in range(first,n+1,2) for p in parts(n-k,parity,k))
@lru_cache(None)
def reps(n,parity):return tuple(Counter(d-1 for d in p) for p in parts(n,parity))
def compatible(U,V,S):
 if max(U)+max(V)>2*max(S):return False
 if sum(U[k]*V[k] for k in U)>S[0]:return False
 counts=Counter()
 for a,ma in U.items():
  for b,mb in V.items():
   for c in range(abs(a-b)//2,(a+b)//2+1):
    counts[c]+=ma*mb
    if counts[c]>S[c]:return False
 return True
@lru_cache(None)
def edges(a,b,d1,d2,parity):
 S=v.source_multiplicities(a,b);R1=reps(d1,parity);R2=reps(d2,parity)
 return tuple(frozenset(j for j,V in enumerate(R2) if compatible(U,V,S)) for U in R1)
def screen(a,b,shape,parity):
 if parity and any(d%2 for d in shape):return {'parity':parity,'impossible_odd_dimension':True}
 p,q,r=shape;A=edges(a,b,p,q,parity);B=edges(a,b,q,r,parity);C=edges(a,b,p,r,parity)
 out={'parity':parity,'representation_counts':[len(reps(d,parity)) for d in shape],'pair_counts':[sum(map(len,E)) for E in (A,B,C)],'witness':None}
 for i,ns in enumerate(A):
  for j in sorted(ns):
   K=B[j]&C[i]
   if K:
    k=min(K);out['witness']=[list(parts(p,parity)[i]),list(parts(q,parity)[j]),list(parts(r,parity)[k])];return out
 return out

def report():
 path=root/'results/rectangular-direct-sums-20261021/single-frontier-2000-summary.json'
 raw=path.read_bytes();rows=json.loads(raw)['remaining']
 out=[{**row,'sectors':[screen(row['a'],row['b'],tuple(row['shape']),parity) for parity in (0,1)]} for row in rows]
 import hashlib
 return {'status':'finite fixed-diagonal SL2 capacity screen only',
         'input_sha256':hashlib.sha256(raw).hexdigest(),'candidate_count':len(out),
         'compatible_candidate_count':sum(any(s.get('witness') for s in r['sectors']) for r in out),
         'records':out,'independent_review':False,'improves_omega':False}
if __name__=='__main__':print(json.dumps(report(),indent=2))
