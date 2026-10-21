from itertools import product
from pathlib import Path
import json,time
import numpy as np
from scipy.optimize import least_squares
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True)
T=np.zeros((12,12,12))
for i,j,p,q,r,s in product(range(2),repeat=6):T[(i*3+p+q)*2+s,(j*2+p)*3+r+s,((i+j)*2+q)*2+r]=1
shape=(6,12,8);M=np.zeros(shape)
for i,j,k in product(range(2),range(3),range(4)):M[i*3+j,j*4+k,k*2+i]=1
cuts=np.cumsum([0]+[d*12 for d in shape]);start=np.load(root/'cyclic-extend-234-best.npz');x0=np.concatenate([start[k].ravel() for k in ('A','B','C')])
def split(x):return [x[cuts[i]:cuts[i+1]].reshape(d,12) for i,d in enumerate(shape)]
def residual(x):return (np.einsum('abc,ia,jb,kc->ijk',T,*split(x),optimize=True)-M).ravel()
def jacobian(x):
 F=split(x);parts=[]
 for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
  others=[j for j in range(3) if j!=axis];V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(12,-1)
  J=np.kron(np.eye(shape[axis]),V.T)
  dims=[shape[axis]]+[shape[j] for j in others]+[shape[axis]*12]
  perm=[([axis]+others).index(j) for j in range(3)]+[3]
  parts.append(J.reshape(dims).transpose(perm).reshape(M.size,shape[axis]*12))
 return np.concatenate(parts,axis=1)

w=np.load(root/'cyclic-als-a2-m234-refined.npz');current=np.concatenate([w[k].ravel() for k in ('A','B','C')]);fixed={};tried=set();records=[];started=time.monotonic()
while len(tried)<len(current):
 index=min((j for j in range(len(current)) if j not in tried),key=lambda j:abs(current[j]));tried.add(index);before=float(current[index]);trial_fixed=dict(fixed);trial_fixed[index]=0.;free=np.asarray([j for j in range(len(current)) if j not in trial_fixed]);base=current.copy()
 for j,v in trial_fixed.items():base[j]=v
 def unpack(y):
  x=base.copy();x[free]=y;return x
 r=least_squares(lambda y:residual(unpack(y)),current[free],jac=lambda y:jacobian(unpack(y))[:,free],method='lm',max_nfev=80,ftol=1e-12,xtol=1e-12,gtol=1e-12)
 candidate=unpack(r.x);err=float(np.linalg.norm(r.fun)/np.linalg.norm(M));accepted=err<1e-11 and np.linalg.norm(candidate)<100
 if accepted:
  current=candidate;fixed=trial_fixed
  F=split(current);np.savez(root/'cyclic-als-a2-m234-sparse.npz',A=F[0],B=F[1],C=F[2],fixed=np.asarray(sorted(fixed)))
 record={'index':int(index),'previous_value':before,'accepted':bool(accepted),'nfev':r.nfev,'relative_error':err,'fixed_count':len(fixed)};records.append(record)
 if accepted or len(tried)%20==0:print(record,'attempts',len(tried),'seconds',time.monotonic()-started,flush=True)
(root/'cyclic-als-a2-m234-sparse.json').write_text(json.dumps({'fixed_zeroes':len(fixed),'records':records,'full_relative_error':float(np.linalg.norm(residual(current))/np.linalg.norm(M)),'exact_certificate':False,'elapsed_seconds':time.monotonic()-started},indent=2)+'\n')
