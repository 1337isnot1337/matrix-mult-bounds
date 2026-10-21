from itertools import product
from pathlib import Path
from fractions import Fraction
import json,time
import numpy as np
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True);data=json.loads((root/'cyclic-a2-m233-exact-rational.json').read_text());F0=[]
for name,d in zip(('A','B','C'),(6,9,6)):
 F=np.zeros((d,12))
 for i,j,v in data['maps'][name]:F[i,j]=float(Fraction(v))
 F0.append(F)
T=np.zeros((12,12,12))
for i,j,p,q,r,s in product(range(2),repeat=6):T[(i*3+p+q)*2+s,(j*2+p)*3+r+s,((i+j)*2+q)*2+r]=1
for dims in ((3,3,3),(2,3,4)):
 l,h,n=dims;M=np.zeros((l*h,h*n,n*l))
 for i,j,k in product(range(l),range(h),range(n)):M[i*h+j,j*n+k,k*l+i]=1
 indices=[[i*h+j for i,j in product(range(2),range(3))],[j*n+k for j,k in product(range(3),range(3))],[k*l+i for k,i in product(range(3),range(2))]]
 records=[];best=float('inf');start=time.monotonic();tag=''.join(map(str,dims))
 for trial in range(32):
  seed=202610250+trial;scale=(.01,.1,.3,1.)[trial//8];rng=np.random.default_rng(seed);F=[rng.normal(size=(d,12))*scale for d in M.shape]
  for axis in range(3):F[axis][indices[axis]]+=F0[axis]
  for iteration in range(1000):
   for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
    others=[j for j in range(3) if j!=axis];V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(12,-1);target=np.moveaxis(M,axis,0).reshape(M.shape[axis],-1);F[axis]=np.linalg.lstsq(V.T,target.T,rcond=1e-12)[0].T
   norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)));F=[f*(common/v) for f,v in zip(F,norms)]
   if iteration%10==0 or iteration==999:
    err=np.linalg.norm(np.einsum('abc,ia,jb,kc->ijk',T,*F,optimize=True)-M)/np.linalg.norm(M)
    if err<best:best=err;np.savez(root/f'cyclic-extend-{tag}-best.npz',A=F[0],B=F[1],C=F[2],seed=seed,error=err,iteration=iteration)
    if err<1e-11:break
  record={'seed':seed,'noise_scale':scale,'iterations':iteration+1,'full_relative_error':float(err),'map_norms':[float(np.linalg.norm(f)) for f in F]};records.append(record);print(tag,record,'best',best,'seconds',time.monotonic()-start,flush=True)
 (root/f'cyclic-extend-{tag}.json').write_text(json.dumps({'source':'A_2','target':f'M{dims}','starts':32,'maximum_iterations':1000,'initialization':'exact M(2,3,3) witness plus seeded Gaussian noise','records':records,'best_full_relative_error':float(best),'exact_witness_found':False,'exclusion_proved':False},indent=2)+'\n')
