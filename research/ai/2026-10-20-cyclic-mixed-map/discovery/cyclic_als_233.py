from itertools import product
from pathlib import Path
import json,time
import numpy as np

def source(a):
 m=2*a-1;d=a*a*m;T=np.zeros((d,d,d))
 for i,j,p,q,r,s in product(range(a),repeat=6):T[(i*m+p+q)*a+s,(j*a+p)*m+r+s,((i+j)*a+q)*a+r]=1
 return T

def matrix_tensor(l,h,n):
 M=np.zeros((l*h,h*n,n*l))
 for i,j,k in product(range(l),range(h),range(n)):M[i*h+j,j*n+k,k*l+i]=1
 return M

def full(T,F):return np.einsum('abc,ia,jb,kc->ijk',T,*F,optimize=True)

def control(a):
 m=2*a-1;d=a*a*m;F=[np.zeros((a*a,d)) for _ in range(3)]
 for i,j in product(range(a),repeat=2):
  F[0][i*a+j,i*a+j]=1
  F[1][i*a+j,j*a*m+i]=1
  F[2][i*a+j,(i*a+j)*a]=1
 assert np.array_equal(full(source(a),F),matrix_tensor(a,a,a))
 return F

T=source(2);C=control(2);M=matrix_tensor(2,3,3);norm=np.linalg.norm(M)
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True);best=float('inf');records=[];started=time.monotonic()
for trial in range(16):
 seed=202610220+trial;rng=np.random.default_rng(seed);F=[rng.normal(size=(dimension,12))*.3 for dimension in M.shape]
 if trial>=12:
  indices=[[i*3+j for i,j in product(range(2),repeat=2)],[j*3+k for j,k in product(range(2),repeat=2)],[k*2+i for k,i in product(range(2),repeat=2)]]
  for axis in range(3):F[axis][indices[axis]]+=C[axis]
 for iteration in range(1000):
  for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
   others=[i for i in range(3) if i!=axis]
   V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(12,-1)
   target=np.moveaxis(M,axis,0).reshape(M.shape[axis],-1)
   F[axis]=np.linalg.lstsq(V.T,target.T,rcond=1e-12)[0].T
  norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)))
  F=[f*(common/n) for f,n in zip(F,norms)]
  if iteration%10==0 or iteration==999:
   err=np.linalg.norm(full(T,F)-M)/norm
   if err<best:
    best=err;np.savez(root/'cyclic-als-a2-m233-best.npz',A=F[0],B=F[1],C=F[2],error=err,seed=seed,iteration=iteration)
   if err<1e-10:break
 record={'seed':seed,'iterations':iteration+1,'full_relative_error':float(err),'map_norms':[float(np.linalg.norm(f)) for f in F],'map_smallest_singular_values':[float(np.linalg.svd(f,compute_uv=False)[-1]) for f in F]};records.append(record)
 print(record,'best',best,'seconds',time.monotonic()-started,flush=True)
(root/'cyclic-als-a2-m233.json').write_text(json.dumps({'source':'A_2','target':'M(2,3,3)','starts':16,'maximum_iterations':1000,'positive_control':'A_2 to M(2,2,2), exact coordinate equality','best_full_relative_error':float(best),'records':records,'exact_witness_found':False,'exclusion_proved':False},indent=2)+'\n')
