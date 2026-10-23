from pathlib import Path
import json,random,time,math
from itertools import product
D=6
rows22=[([0],[1,2,3,5],[4]),([1],[2,4],[0,3,5]),([3],[0,2,4,5],[1]),([4],[0],[1,2,3,5]),([1,2],[3,4,5],[0]),([2,3],[1,4],[0,5]),([1,3],[4,5],[0,2]),([1,4],[0,2,3],[5]),([0,2,4,5],[1],[3]),([3,5],[0,1],[2,4]),([0,1,4],[2],[3,5]),([0,3],[4],[1,2,5]),([2],[0,4],[1,3,5]),([3,4],[0,2],[1,5]),([0,4],[3,5],[1,2]),([1,3,4],[0,5],[2]),([0,1],[3],[2,4,5]),([5],[0,1,4],[2,3]),([0,2,4],[5],[1,3]),([4,5],[1,2],[0,3]),([0,2],[1,5],[3,4]),([2,5],[1,3],[0,4])]
Q22=[[i] for i in range(6)]+[[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
mask=lambda xs:sum(1<<i for i in xs)
class Counter:
 def __init__(self,rows,q,d):
  self.d=d;self.full=(1<<d)-1;self.rows=[[mask(x) for x in row] for row in rows];self.ps=[0]+[mask(x) for x in q]
  self.eligible=[[[t for t,row in enumerate(self.rows) if p&row[l]==p] for l in range(3)] for p in self.ps]
  self.subsets=[]
  for a in range(1<<d):
   value=0;h=a
   while True:
    value |= 1<<h
    if not h: break
    h=(h-1)&a
   self.subsets.append(value)
  self.cache={}
 def count(self,profiles,n):
  costs=[]
  for p,eligible in zip(self.ps,self.eligible):
   common=None
   for leg,ts in enumerate(eligible):
    bits=0
    for t in ts: bits |= self.subsets[(profiles[t]|self.rows[t][leg]) & (self.full^p)]
    common=bits if common is None else common&bits
   key=(p,common,n)
   if key not in self.cache:
    value=0;bits=common
    while bits:
     bit=bits&-bits;h=bit.bit_length()-1;size=h.bit_count();bits-=bit
     value+=2**(self.d-p.bit_count()-size)*(n-1)**size
    self.cache[key]=value
   costs.append(self.cache[key])
  return sum(costs),costs
 def score(self,profiles,n):
  b,c=self.count(profiles,n);mass=sum(n**(.75*h.bit_count()) for h in profiles)
  return b/mass,b,mass

def load29():
 x=json.loads(Path('research/ai/2026-10-23-aggregation-families/witness_29.json').read_text())
 return Counter([[row[k] for k in 'UVW'] for row in x['products']],x['correction_subsets'],x['coordinate_count'])

def run(c,n,steps,seed):
 rng=random.Random(seed);full=c.full
 # Exactly one smaller coordinate per row, always active on X initially.
 current=[full^(1<<rng.choice([r for r in range(c.d) if not row[0]>>r&1])) for row in c.rows]
 score=c.score(current,n);best=(score,current[:]);history=[{'step':0,'ratio':score[0],'budget':score[1]}]
 t0=time.monotonic()
 for i in range(1,steps+1):
  t=rng.randrange(len(current));old=current[t];current[t]^=1<<rng.randrange(c.d)
  # Keep no full retained target, so the fixed-grid rigidity hypothesis is escaped.
  if current[t]==full:
   current[t]=old;continue
  newscore=c.score(current,n)
  temp=.25*(1-i/steps)**2+.001
  if newscore[0] < score[0] or rng.random()<math.exp(min(0,(score[0]-newscore[0])/temp)):
   score=newscore
  else:current[t]=old
  if score[0]<best[0][0]-1e-10:
   best=(score,current[:]);history.append({'step':i,'ratio':score[0],'budget':score[1]})
 return {'n':n,'steps':steps,'seed':seed,'best_ratio_float_discovery_only':best[0][0],'budget':best[0][1],'mass_float_discovery_only':best[0][2],'profiles':best[1],'costs':c.count(best[1],n)[1],'history':history,'seconds':time.monotonic()-t0}
if __name__=='__main__':
 c=Counter(rows22,Q22,6)
 report={'hypothesis_escaped':'Smaller product-dependent centered supports; count only nonzero rank-one positions','embedding':'zero extension of the dimension n_t centered dual pair, using common support {0,last} at dimension1','source':'normalized transcription of general22 from arxiv2610.26563v2; exact source and grade acceptance separate','runs':[]}
 for n in (2,3,4,7,11):
  row=run(c,n,10000,20261023+n);report['runs'].append(row)
  print(n,row['best_ratio_float_discovery_only'],row['budget'],row['seconds'],flush=True)
  Path('results/local/pruned-grid/discovery.json').write_text(json.dumps(report,indent=2)+'\n')
