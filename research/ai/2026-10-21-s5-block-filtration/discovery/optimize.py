"""Numerical discovery for corner/Loewy support majorants; not acceptance."""
import json
from pathlib import Path
from itertools import product,combinations_with_replacement
import numpy as np
from scipy.optimize import minimize

HERE=Path(__file__).resolve().parent
report=json.loads((HERE/'peirce.json').read_text())
raw={}
for c in report['corners']:
 if c['i'] in [1,2,3,4] or c['j'] in [1,2,3,4]:
  continue
 for k,(a,b) in enumerate(zip(c['power_dimensions'],c['power_dimensions'][1:])):
  if a>b:
   typ=(int(c['i']!=0),int(c['j']!=0),k)
   raw[typ]=raw.get(typ,0)+a-b
keys=list(raw)
A=set()
for x,y,z in product(keys,repeat=3):
 if x[1]==y[0] and y[1]==z[0] and z[1]==x[0] and x[2]+y[2]+z[2]<=6:
  A.add(tuple([x,y,z].count(k) for k in keys))
A=np.array(sorted(A))
coeff=np.array([raw[k] for k in keys])
x=np.array([(k[2]-2)*np.log(.8) for k in keys])
r=minimize(lambda x:np.dot(coeff,np.exp(x)),x,jac=lambda x:coeff*np.exp(x),constraints={'type':'ineq','fun':lambda x:A@x,'jac':lambda x:A},method='SLSQP',options={'ftol':1e-9,'maxiter':1000})
print(r.success,r.fun,'constraints',len(A),'min',min(A@r.x))
for k,c,x in zip(keys,coeff,r.x):
 print(k,c,round(x,9),round(np.exp(x),9))
(HERE/'optimizer.json').write_text(json.dumps({'keys':keys,'coefficients':coeff.tolist(),'weights':r.x.tolist(),'score':float(r.fun),'constraints':A.tolist()},indent=2)+'\n')
