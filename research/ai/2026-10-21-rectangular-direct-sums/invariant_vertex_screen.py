"""Bounded physical-subset ordinary screen using invariant-slice ranks."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import gzip,hashlib,importlib.util,json
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('invariant_vertex_capacity',Path(__file__).with_name('equivariant_frontier.py'))
eq=importlib.util.module_from_spec(spec);spec.loader.exec_module(eq)

def multiplicities(U,V):
 out=Counter()
 for a in U:
  for b in V:
   for l in range(abs(a-b)//2,(a+b-2)//2+1):out[l]+=1
 return out

def rejection(vertices,certificate):
 T=[multiplicities(vertices[i],vertices[(i+1)%3]) for i in range(3)]
 for leg in range(3):
  common=set(vertices[leg])&set(vertices[(leg+1)%3])
  if not common:continue
  assert len(common)==1
  alpha=next(iter(common));third=vertices[(leg+2)%3]
  for c in certificate['channels']:
   l=c['half_weight'];lower=T[(leg+1)%3][l]+T[(leg+2)%3][l]+c['rank_mod_p']-2*c['multiplicity']
   target=sum(abs(alpha-gamma)//2<=l<=(alpha+gamma-2)//2 for gamma in third)
   if lower>target:return {'leg':leg,'shared_irrep_dimension':alpha,'half_weight':l,'restricted_rank_lower':lower,'target_rank':target}
 return None

def report():
 a=24;n=124
 raw=gzip.decompress((ROOT/'results/rectangular-direct-sums-20261021/invariant-slice-a24.json.gz').read_bytes());cert=json.loads(raw)
 P=[p for k in range(1,6) if k%2==n%2 for p in combinations(range(1,2*a,2),k) if sum(p)==n]
 R=[Counter(d-1 for d in p) for p in P];S=eq.v.source_multiplicities(a,a);adj=[set() for p in P]
 for i in range(len(P)):
  for j in range(i,len(P)):
   if eq.compatible(R[i],R[j],S):adj[i].add(j);adj[j].add(i)
 counts=Counter();rejections=[];shared=[];survivors=[]
 for i,ns in enumerate(adj):
  for j in sorted(k for k in ns if k>=i):
   for k in sorted(x for x in ns&adj[j] if x>=j):
    counts['capacity_triangles']+=1;V=[list(P[i]),list(P[j]),list(P[k])]
    if all(2*a-1 in p for p in V):counts['shared_top_irrep']+=1;shared.append(V);continue
    w=rejection(V,cert)
    if w:counts['invariant_slice']+=1;rejections.append({'vertices':V,'witness':w})
    else:survivors.append(V)
 return {'status':'bounded physical-subset ordinary ansatz only','a':a,'source_leg':a*a*(2*a-1),'target':n,
         'maximum_summands':5,'restricted_vertex_count':len(P),'counts':dict(counts),
         'shared_top_triples':shared,'rejections':rejections,'survivors':survivors,
         'source_certificate_sha256':hashlib.sha256(raw).hexdigest(),
         'does_not_exclude_general_singular_degenerations':True,'improves_omega':False,'independent_review':False}
if __name__=='__main__':print(json.dumps(report(),indent=2))
