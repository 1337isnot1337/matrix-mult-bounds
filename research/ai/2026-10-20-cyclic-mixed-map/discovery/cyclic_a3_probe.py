from itertools import product
from pathlib import Path
from fractions import Fraction
import json,time
import numpy as np
root=Path('results/local/cyclic-mixed-map');root.mkdir(parents=True,exist_ok=True);a=3;m=5;d=a*a*m;T=np.zeros((d,d,d))
for i,j,p,q,r,s in product(range(a),repeat=6):T[(i*m+p+q)*a+s,(j*a+p)*m+r+s,((i+j)*a+q)*a+r]=1
# Embed the exact small source restriction into the first two indices of each convolution.
cols=[[],[],[]]
for col in range(12):
 i,k,s=col//6,(col//2)%3,col%2;cols[0].append((i*m+k)*a+s)
 j,p,L=col//6,(col//3)%2,col%3;cols[1].append((j*a+p)*m+L)
 H,q,r=col//4,(col//2)%2,col%2;cols[2].append((H*a+q)*a+r)
# Extra i,j,p,q,r,s values can create unwanted terms on these columns: verify the embedded restriction.
small=json.loads((Path(__file__).resolve().parents[4]/'results/cyclic-mixed-map-2026-10-20/witness.json').read_text());base=[np.zeros((n,d)) for n in (6,12,8)]
for axis,name in enumerate(('A','B','C')):
 for row,col,v in small['maps'][name]:base[axis][row,cols[axis][col]]=float(Fraction(v))
control=np.zeros((6,12,8))
for i,j,k in product(range(2),range(3),range(4)):control[3*i+j,4*j+k,2*k+i]=1
assert np.array_equal(np.einsum('abc,ia,jb,kc->ijk',T,*base,optimize=True),control)
l,h,n=3,5,9;M=np.zeros((l*h,h*n,n*l))
for i,j,k in product(range(l),range(h),range(n)):M[i*h+j,j*n+k,k*l+i]=1
indices=[[i*h+j for i,j in product(range(2),range(3))],[j*n+k for j,k in product(range(3),range(4))],[k*l+i for k,i in product(range(4),range(2))]]
records=[];best=float('inf');start=time.monotonic()
for trial in range(8):
 seed=202610340+trial;scale=(.01,.1,.3,1.)[trial//2];rng=np.random.default_rng(seed);F=[rng.normal(size=(k,d))*scale for k in M.shape]
 for axis in range(3):F[axis][indices[axis]]+=base[axis]
 for iteration in range(500):
  for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
   others=[j for j in range(3) if j!=axis];V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(d,-1);target=np.moveaxis(M,axis,0).reshape(M.shape[axis],-1);F[axis]=np.linalg.lstsq(V.T,target.T,rcond=1e-12)[0].T
  norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)));F=[f*(common/v) for f,v in zip(F,norms)]
  if iteration%10==0 or iteration==499:
   err=np.linalg.norm(np.einsum('abc,ia,jb,kc->ijk',T,*F,optimize=True)-M)/np.linalg.norm(M)
   if err<best:best=err;np.savez(root/'cyclic-a3-m359-best.npz',A=F[0],B=F[1],C=F[2],seed=seed,error=err,iteration=iteration)
   if err<1e-11:break
 record={'seed':seed,'noise_scale':scale,'iterations':iteration+1,'full_relative_error':float(err),'map_norms':[float(np.linalg.norm(f)) for f in F]};records.append(record);print(record,'best',best,'seconds',time.monotonic()-start,flush=True)
(root/'cyclic-a3-m359.json').write_text(json.dumps({'source':'A_3','target':'M(3,5,9)','starts':8,'maximum_iterations':500,'positive_control':'A_3 restricted to the embedded exact A_2 to M(2,3,4) maps','records':records,'best_full_relative_error':float(best),'exact_witness_found':False,'exclusion_proved':False},indent=2)+'\n')
