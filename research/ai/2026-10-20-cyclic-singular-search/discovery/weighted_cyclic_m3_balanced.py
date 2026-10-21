from itertools import product
from fractions import Fraction
from pathlib import Path
import json,time
import numpy as np
root=Path('results/local/cyclic-singular-search');root.mkdir(parents=True,exist_ok=True);T=np.zeros((12,12,12))
for i,j,p,q,r,s in product(range(2),repeat=6):T[(i*3+p+q)*2+s,(j*2+p)*3+r+s,((i+j)*2+q)*2+r]=1
M=np.zeros((9,9,9))
for i,j,k in product(range(3),repeat=3):M[i*3+j,j*3+k,k*3+i]=1
small=json.loads((Path(__file__).resolve().parents[4]/'results/cyclic-mixed-map-2026-10-20/witness.json').read_text());base=[np.zeros((9,12)) for _ in range(3)]
for axis,name in enumerate(('A','B','C')):
 for row,col,coefficient in small['maps'][name]:
  if axis==0:newrow=row
  elif axis==1:
   j,k=divmod(row,4)
   if k>=3:continue
   newrow=j*3+k
  else:
   k,i=divmod(row,2)
   if k>=3:continue
   newrow=k*3+i
  base[axis][newrow,col]=float(Fraction(coefficient))

def balance(F):
 for _ in range(30):
  previous=sum(np.linalg.norm(f)**2 for f in F)
  E=[np.sum(abs(f)**2,axis=1).reshape(3,3) for f in F]
  u=(E[2].sum(axis=0)/E[0].sum(axis=1))**.25
  F[0]*=np.repeat(u,3)[:,None];F[2]/=np.tile(u,3)[:,None]
  E=[np.sum(abs(f)**2,axis=1).reshape(3,3) for f in F]
  v=(E[1].sum(axis=1)/E[0].sum(axis=0))**.25
  F[0]*=np.tile(v,3)[:,None];F[1]/=np.repeat(v,3)[:,None]
  E=[np.sum(abs(f)**2,axis=1).reshape(3,3) for f in F]
  w=(E[2].sum(axis=1)/E[1].sum(axis=0))**.25
  F[1]*=np.tile(w,3)[:,None];F[2]/=np.repeat(w,3)[:,None]
  current=sum(np.linalg.norm(f)**2 for f in F)
  if previous-current<1e-10*current:break
 return F

records=[];started=time.monotonic();best=float('inf')
for trial in range(16):
 seed=202610380+trial;rng=np.random.default_rng(seed)
 if trial<4:u,v,w=np.array([0,1,3]),np.array([0,2,6]),np.array([0,4,12])
 else:u,v,w=[rng.choice(np.arange(-5,6),size=3,replace=False) for _ in range(3)]
 weights=[(u[:,None]+v[None,:]).ravel(),(-v[:,None]+w[None,:]).ravel(),(-w[:,None]-u[None,:]).ravel()];degrees=weights[0][:,None,None]+weights[1][None,:,None]+weights[2][None,None,:];mask=degrees<=0
 assert np.all(degrees[M!=0]==0)
 F=[f+rng.normal(size=f.shape)*(.03,.1,.3,1.)[trial%4] for f in base]
 for iteration in range(500):
  for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
   others=[j for j in range(3) if j!=axis];V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(12,-1);target=np.moveaxis(M,axis,0).reshape(9,-1);selected=np.moveaxis(mask,axis,0).reshape(9,-1)
   F[axis]=np.array([np.linalg.lstsq(V[:,selected[i]].T,target[i,selected[i]],rcond=1e-12)[0] for i in range(9)])
  norms=[np.linalg.norm(f) for f in F];common=np.exp(np.mean(np.log(norms)));F=balance([f*(common/vv) for f,vv in zip(F,norms)])
  if iteration%10==0 or iteration==499:
   full=np.einsum('abc,ia,jb,kc->ijk',T,*F,optimize=True);err=np.linalg.norm((full-M)[mask])/np.linalg.norm(M)
   if err<best:best=err;np.savez(root/'cyclic-weighted-balanced-m333-best.npz',A=F[0],B=F[1],C=F[2],u=u,v=v,w=w,mask=mask,seed=seed,error=err,iteration=iteration)
   if err<1e-10:break
 record={'seed':seed,'u':u.tolist(),'v':v.tolist(),'w':w.tolist(),'nonpositive_coefficient_count':int(mask.sum()),'iterations':iteration+1,'weighted_relative_error':float(err),'full_unweighted_relative_error':float(np.linalg.norm(full-M)/np.linalg.norm(M)),'max_unweighted_coefficient':float(np.max(abs(full))),'map_norms':[float(np.linalg.norm(f)) for f in F],'smallest_map_singular_values':[float(np.linalg.svd(f,compute_uv=False)[-1]) for f in F]};records.append(record);print(record,'best',best,'seconds',time.monotonic()-started,flush=True)
(root/'cyclic-weighted-balanced-m333.json').write_text(json.dumps({'source':'A_2','target':'M(3,3,3)','starts':16,'maximum_iterations':500,'class':'constant dense maps followed by target-vertex diagonal weights; target stabilizer balanced after each sweep','records':records,'best_weighted_relative_error':float(best),'exact_witness_found':False,'exclusion_proved':False},indent=2)+'\n')
