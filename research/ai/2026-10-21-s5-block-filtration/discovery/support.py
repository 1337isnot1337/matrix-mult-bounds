"""Discovery for the exact trace tensor on the principal S5 block."""
import json
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import minimize
from peirce import xor,indices
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'2026-10-21-s5-split'))
import radical

G=radical.group()
C=json.loads((HERE/'peirce.json').read_text())
vectors=[]
labels=[]
types=[]
for c in C['corners']:
 i,j=c['i'],c['j']
 if i in range(1,5) or j in range(1,5):
  continue
 span={}
 for degree in range(6,-1,-1):
  count=0
  for word in c['bases'][degree]:
   value=int(word,16)
   if radical.insert(value,span):
    label=(int(i!=0),int(j!=0),degree,count)
    if label not in types:
     types.append(label)
    vectors.append(value)
    labels.append(types.index(label))
    count+=1
assert len(vectors)==88
inv_vectors=[xor(1<<G['inv'][g] for g in indices(v)) for v in vectors]
translates=[[xor(1<<G['mul'][g][h] for h in indices(v)) for v in vectors] for g in range(120)]
constraints=set()
nonzero=0
for a in range(88):
 for b in range(88):
  p=xor(translates[g][b] for g in indices(vectors[a]))
  for c,w in enumerate(inv_vectors):
   if (p&w).bit_count()%2:
    constraints.add(tuple(sorted([labels[a],labels[b],labels[c]])))
    nonzero+=1
print('nonzero',nonzero,'types',len(types),'constraints',len(constraints),flush=True)
A=np.array([[ijk.count(i) for i in range(len(types))] for ijk in sorted(constraints)])
coeff=np.bincount(labels)
x=np.array([(k[2]-2)*np.log(.8) for k in types])
r=minimize(lambda x:np.dot(coeff,np.exp(x)),x,jac=lambda x:coeff*np.exp(x),constraints={'type':'ineq','fun':lambda x:A@x,'jac':lambda x:A},method='SLSQP',options={'ftol':1e-10,'maxiter':2000})
print(r.success,r.fun,min(A@r.x),flush=True)
for k,c,w in zip(types,coeff,r.x):
 print(k,int(c),w,flush=True)
report={'vectors':[hex(v) for v in vectors],'labels':labels,'types':types,'nonzero':nonzero,'constraints':sorted(constraints),'weights':r.x.tolist(),'score':float(r.fun)}
(HERE/'support.json').write_text(json.dumps(report,indent=2)+'\n')
