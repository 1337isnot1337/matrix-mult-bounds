from itertools import product
from pathlib import Path
import numpy as np
import json,time
root=Path('results/local/cyclic-equivariant');root.mkdir(parents=True,exist_ok=True);T=np.zeros((12,12,12));M=np.zeros((9,9,9));control=np.zeros_like(M)
for i,j,p,q,r,s in product(range(2),repeat=6):T[(i*3+p+q)*2+s,(j*2+p)*3+r+s,((i+j)*2+q)*2+r]=1
for i,j,k in product(range(3),repeat=3):M[i*3+j,j*3+k,k*3+i]=1
for i,j,k in product(range(2),repeat=3):control[i*3+j,j*3+k,k*3+i]=1
sx=[k-i-s for i,k,s in product(range(2),range(3),range(2))];sy=[l-j-p for j,p,l in product(range(2),range(2),range(3))];sz=[h-q-r for h,q,r in product(range(3),range(2),range(2))];target=[j-i for i,j in product(range(3),repeat=2)];allowed=[np.array([[x==y for y in weights] for x in target]) for weights in (sx,sy,sz)];base=[np.zeros((9,12)) for _ in range(3)]
for i,j in product(range(2),repeat=2):base[0][i*3+j,((1-j)*3+1)*2+i]=1;base[1][i*3+j,(i*2+1-j)*3+1]=1;base[2][i*3+j,(2+i)*2+1-j]=1
assert all(np.array_equal(f*ok,f) for f,ok in zip(base,allowed));assert np.array_equal(np.einsum('abc,ia,jb,kc->ijk',T,*base,optimize=True),control)
records=[];started=time.monotonic();best=float('inf')
for trial in range(32):
 seed=202610420+trial;rng=np.random.default_rng(seed);complex_run=trial>=16;noise=(.03,.1,.3,1.)[trial%4]
 F=[f.astype(complex if complex_run else float)+(rng.normal(size=f.shape)+(1j*rng.normal(size=f.shape) if complex_run else 0))*noise*ok for f,ok in zip(base,allowed)]
 for iteration in range(1000):
  for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
   others=[j for j in range(3) if j!=axis];V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(12,-1);tm=np.moveaxis(M,axis,0).reshape(9,-1)
   for row in range(9):F[axis][row,allowed[axis][row]]=np.linalg.lstsq(V[allowed[axis][row]].T,tm[row],rcond=1e-12)[0]
  norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)));F=[f*common/n for f,n in zip(F,norms)]
  if iteration%10==0 or iteration==999:
   err=np.linalg.norm(np.einsum('abc,ia,jb,kc->ijk',T,*F,optimize=True)-M)/np.linalg.norm(M)
   if err<best:best=err;np.savez(root/'cyclic-cartan-m333-best.npz',A=F[0],B=F[1],C=F[2],seed=seed,error=err,iteration=iteration)
   if err<1e-11:break
 record={'seed':seed,'complex':complex_run,'noise':noise,'iterations':iteration+1,'full_relative_error':float(err),'map_norms':[float(np.linalg.norm(f)) for f in F]};records.append(record);print(record,'best',best,'seconds',time.monotonic()-started,flush=True)
(root/'cyclic-cartan-m333.json').write_text(json.dumps({'source':'A2','target':'M3','class':'Maps intertwining the diagonal Cartan subgroup, all coefficients compared','allowed_map_entries_per_leg':[int(ok.sum()) for ok in allowed],'positive_control':'Exact source to embedded M2 identity','starts':32,'maximum_iterations':1000,'records':records,'best_full_relative_error':float(best),'exact_certificate':False,'general_exclusion':False},indent=2)+'\n')
