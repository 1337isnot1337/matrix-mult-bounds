"""Bounded SciPy MILP discovery. Floating solver status is never a proof."""
from pathlib import Path
import itertools,json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix,csc_matrix

HERE=Path(__file__).resolve().parent
seed_rows=[tuple(map(int,line.split())) for line in (HERE/'best-conflict.masks').read_text().splitlines()]
d,m=seed_rows.pop(0);F=(1<<d)-1;n=d//3
masks=[x for x in range(1<<d) if x.bit_count()==n]
triples=[(a,b,F^a^b) for a in masks for b in masks if not(a&b)]
lookup={t:i for i,t in enumerate(triples)}
seed=[lookup[t] for t in seed_rows];L=len(triples)
classes=[{} for _ in range(3)]
for i,t in enumerate(triples):
 for k in range(3):classes[k].setdefault(t[k],[]).append(i)
A=lil_matrix((L,L),dtype=float)
for i,t in enumerate(triples):
 neighbors=set()
 for k in range(3):neighbors.update(classes[k][t[k]])
 for j in neighbors:A[i,j]=1
 A[i,i]=2
A=csc_matrix(A)
rng=np.random.default_rng(20261028)
pool=[seed];max_size=len(seed);attempts=0;status_counts={};start=time.monotonic();solutions=[]

def exact_accept(S):
 rows=[triples[i] for i in S]
 for a,b,c in itertools.product(range(len(S)),repeat=3):
  if a==b==c:continue
  u,v,w=rows[a][0],rows[b][1],rows[c][2]
  if not(u&v or u&w or v&w):return False
 return True

while attempts<300 and time.monotonic()-start<120:
 base=pool[int(rng.integers(len(pool)))];keep=int(rng.choice([16,18,20,22,24]));core=sorted(map(int,rng.choice(base,size=keep,replace=False)))
 forbidden=[set() for _ in range(3)]
 for i,j in itertools.product(core,repeat=2):
  a,b=triples[i],triples[j]
  for k in range(3):
   u,v=a[(k+1)%3],b[(k+2)%3]
   if not(u&v):forbidden[k].add(F^u^v)
 free=[i for i,t in enumerate(triples) if all(t[k] not in forbidden[k] for k in range(3))]
 attempts+=1
 if len(core)+len(free)<max_size+1:continue
 b=2-np.asarray(A[:,core].sum(axis=1)).ravel()
 result=milp(c=-np.ones(len(free)),integrality=np.ones(len(free)),bounds=Bounds(0,1),constraints=LinearConstraint(A[:,free],-np.inf,b),options={'time_limit':min(3,max(.01,120-(time.monotonic()-start))),'mip_rel_gap':0})
 status_counts[str(result.status)]=status_counts.get(str(result.status),0)+1
 if result.x is not None:
  found=core+[i for i,x in zip(free,result.x) if x>0.5]
  if not exact_accept(found):raise RuntimeError('MILP proposed an invalid exact family')
  if len(found)>=max_size:
   if len(pool)<128:pool.append(found)
   else:pool[int(rng.integers(len(pool)))]=found
   solutions.append({'attempt':attempts,'keep':keep,'free_variables':len(free),'size':len(found),'solver_status':int(result.status)})
  if len(found)>max_size:
   max_size=len(found)
   (HERE/'best-milp.masks').write_text(f'{d} {max_size}\n'+'\n'.join(' '.join(map(str,triples[i])) for i in found)+'\n')
   print('new best',max_size,'attempt',attempts,'seconds',time.monotonic()-start,flush=True)
 if attempts%10==0:print('attempt',attempts,'free',len(free),'best',max_size,'seconds',time.monotonic()-start,flush=True)
report={'kind':'bounded floating MILP discovery with exact family acceptance','attempts':attempts,'time_budget_seconds':120,'maximum_attempts':300,'rng_seed':20261028,'max_products':max_size,'status_counts':status_counts,'elapsed_seconds':time.monotonic()-start,'retained_solutions':solutions,'optimality_claim':False,'negative_result_claim':False}
(HERE/'milp-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='retained_solutions'}),flush=True)
