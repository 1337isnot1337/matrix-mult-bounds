from itertools import product
from pathlib import Path
import json,time
import numpy as np
from scipy.optimize import least_squares
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True)
T=np.zeros((12,12,12))
for i,j,p,q,r,s in product(range(2),repeat=6):T[(i*3+p+q)*2+s,(j*2+p)*3+r+s,((i+j)*2+q)*2+r]=1
shape=(6,9,6);M=np.zeros(shape)
for i,j,k in product(range(2),range(3),range(3)):M[i*3+j,j*3+k,k*2+i]=1
cuts=np.cumsum([0]+[d*12 for d in shape]);start=np.load(root/'cyclic-als-a2-m233-best.npz');x0=np.concatenate([start[k].ravel() for k in ('A','B','C')])
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
rng=np.random.default_rng(202610236);direction=rng.normal(size=x0.size);h=1e-6
error=np.max(np.abs((residual(x0+h*direction)-residual(x0-h*direction))/(2*h)-jacobian(x0)@direction));assert error<1e-6
started=time.monotonic();result=least_squares(residual,x0,jac=jacobian,method='lm',max_nfev=1000,ftol=1e-13,xtol=1e-13,gtol=1e-13)
F=split(result.x);report={'nfev':result.nfev,'njev':result.njev,'status':result.status,'message':result.message,'full_relative_error':float(np.linalg.norm(result.fun)/np.linalg.norm(M)),'maximum_coefficient_error':float(np.max(np.abs(result.fun))),'map_norms':[float(np.linalg.norm(f)) for f in F],'smallest_map_singular_values':[float(np.linalg.svd(f,compute_uv=False)[-1]) for f in F],'jacobian_direction_check_maximum_error':float(error),'elapsed_seconds':time.monotonic()-started,'exact_certificate':False}
np.savez(root/'cyclic-als-a2-m233-refined.npz',A=F[0],B=F[1],C=F[2]);(root/'cyclic-als-a2-m233-refined.json').write_text(json.dumps(report,indent=2)+'\n');print(report,flush=True)
