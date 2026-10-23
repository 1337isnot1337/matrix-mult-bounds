"""Exact vectorized capacity and ordinary slice screen for bounded vertices."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import importlib.util,json
import numpy as np

def load(name):
 spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name(name+'.py'))
 v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v);return v
inv=load('invariant_slice_pairing');target=load('invariant_vertex_screen')

def capacity_graph(a,vertices):
 L=2*a-1;maximum=max(map(len,vertices),default=0)
 assert maximum**2<np.iinfo(np.int16).max
 cg=np.zeros((a,a,L),dtype=np.int16)
 for i in range(a):
  for j in range(a):cg[i,j,abs(i-j):i+j+1]=1
 indices=np.full((len(vertices),maximum),a,dtype=np.int64)
 for row,V in enumerate(vertices):indices[row,:len(V)]=[(d-1)//2 for d in V]
 source=np.array([min(l+1,2*a-1-l) for l in range(L)],dtype=np.int16)
 graph=[]
 for V in vertices:
  g=np.zeros((a+1,L),dtype=np.int16)
  for d in V:g[:a]+=cg[(d-1)//2]
  counts=np.zeros((len(vertices),L),dtype=np.int16)
  for j in range(maximum):counts+=g[indices[:,j]]
  assert counts.max(initial=0)<=maximum**2
  graph.append(set(map(int,np.flatnonzero(np.all(counts<=source,axis=1)))))
 assert all(i in graph[j] for i,ns in enumerate(graph) for j in ns)
 return graph

def screen(a):
 n=1
 while 216*n**3<=(6*a-2)**4:n+=1
 P=[p for k in range(1,6) if k%2==n%2 for p in combinations(range(1,2*a,2),k) if sum(p)==n]
 graph=capacity_graph(a,P);certificate=None;counts=Counter();rejections=[];survivors=[]
 for i,ns in enumerate(graph):
  for j in sorted(k for k in ns if k>=i):
   for k in sorted(x for x in ns&graph[j] if x>=j):
    counts['capacity_triangles']+=1;V=[list(P[i]),list(P[j]),list(P[k])]
    if all(2*a-1 in p for p in V):counts['shared_top_irrep']+=1;continue
    if certificate is None:certificate=inv.certificate(a)
    w=target.rejection(V,certificate)
    if w:counts['invariant_slice']+=1;rejections.append({'vertices':V,'witness':w})
    else:survivors.append(V)
 return {'a':a,'source_leg':a*a*(2*a-1),'target':n,'restricted_vertex_count':len(P),
         'counts':dict(counts),'rejections':rejections,'survivors':survivors,
         'source_channel_ranks':None if certificate is None else [[c['half_weight'],c['multiplicity'],c['rank_mod_p']] for c in certificate['channels']]}

def report():
 rows=[screen(a) for a in range(24,37)]
 return {'status':'bounded physical-subset ordinary ansatz only','maximum_summands':5,
         'sources':rows,'remaining_count':sum(len(r['survivors']) for r in rows),
         'capacity_triangle_count':sum(r['counts'].get('capacity_triangles',0) for r in rows),
         'integer_dtype':'int16; all capacity accumulations <=25',
         'does_not_exclude_general_singular_degenerations':True,'improves_omega':False,'independent_review':False}
if __name__=='__main__':print(json.dumps(report(),indent=2))
