import json
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True);data=json.loads((root/'cyclic-a2-m233-exact-algebraic.json').read_text());rows=[];es=[]
# parameters alpha,beta,gamma,cx,cy,u0,u1,v0,v1,v2,w0,w1,w2
for axis,name in enumerate(('A','B','C')):
 for row,col,sign,e in data['maps'][name]:
  v=np.zeros(13,dtype=int)
  if axis==0:
   i,k,s=col//6,(col//2)%3,col%2;v[:5]=[i,-k,s,1,0];ti,tj=divmod(row,3);v[5+ti]+=1;v[7+tj]+=1
  elif axis==1:
   j,p,L=col//6,(col//3)%2,col%3;v[:5]=[j,p,-L,0,1];tj,tk=divmod(row,3);v[7+tj]-=1;v[10+tk]+=1
  else:
   H,q,r=col//4,(col//2)%2,col%2;v[:5]=[-H,q,r,-1,-1];tk,ti=divmod(row,2);v[10+tk]-=1;v[5+ti]-=1
  rows.append(v);es.append(e)
E=np.array(rows);n=len(es);mat=np.hstack([E,-4*np.eye(n)]);objective=np.zeros(13+n);bounds=Bounds(np.r_[np.full(13,-12),np.full(n,-1)],np.r_[np.full(13,12),np.full(n,1)]);result=milp(objective,integrality=np.ones(13+n),bounds=bounds,constraints=LinearConstraint(mat,-np.array(es),-np.array(es)),options={'time_limit':30})
print(result.message)
if result.x is not None:
 x=np.rint(result.x).astype(int);assert np.array_equal(mat@x,-np.array(es));print('gauges',x[:13]);k=0;maps={}
 for name in ('A','B','C'):
  maps[name]=[]
  for row,col,sign,e in data['maps'][name]:
   value=sign*Fraction(2)**int(x[13+k]);k+=1;maps[name].append([row,col,str(value)])
  print(name,maps[name])
 (root/'cyclic-a2-m233-exact-rational.json').write_text(json.dumps({'source':'A_2','target':'M(2,3,3)','field':'Q','entry_format':['row','column','coefficient'],'maps':maps,'algebraic_witness_gauge_parameters':x[:13].tolist()},indent=2)+'\n')
