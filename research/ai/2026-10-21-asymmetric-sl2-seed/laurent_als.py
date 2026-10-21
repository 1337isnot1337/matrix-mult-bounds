"""Discover finite-degree Laurent families; numerical coefficients are not proofs."""
import argparse,json,time
from pathlib import Path
from itertools import product
import numpy as np
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('output',type=Path);p.add_argument('--sweeps',type=int,default=300);p.add_argument('--warm',type=Path);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
if a.warm:
 z=np.load(a.warm);M=[z[n].copy() for n in 'ABC']
else:
 root=Path('results/local/asymmetric-sl2-seed');names=['gauss-newton-preconditioned','sparse-gauss-newton','sparse-gauss-newton-restart'];samples=[];ts=[]
 for name in names:
  z=np.load(root/name/'best.npz');M=[z[n] for n in 'ABC'];norms=[np.linalg.norm(m) for m in M];t=float(np.prod(norms)**(1/3));ts.append(t);samples.append([m*t/n for m,n in zip(M,norms)])
 scale=np.mean(ts);V=np.array([[t/scale,1,scale/t] for t in ts]);M=[np.linalg.solve(V,np.stack([m[leg].ravel() for m in samples])).reshape(3,*samples[0][leg].shape) for leg in range(3)]
W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);H=M[0].shape[0];d=(H-1)//2;assert H==2*d+1;degrees=list(range(d,-d-1,-1));levels=3*d+1;target=np.zeros((25,20,20))
for i,j,k in product(range(5),range(5),range(4)):target[5*i+j,4*j+k,5*k+i]=1
rhses=[np.concatenate([target.transpose(1,2,0).reshape(400,25),np.zeros(((levels-1)*400,25))]),np.concatenate([target.transpose(0,2,1).reshape(500,20),np.zeros(((levels-1)*500,20))]),np.concatenate([target.reshape(500,20),np.zeros(((levels-1)*500,20))])];history=[];best=float('inf');start=time.monotonic()
def physical(M):return [np.einsum('hst,sab->htab',m,W,optimize=True) for m in M]
def outputs(P):
 out=[np.zeros_like(target,dtype=complex) for _ in range(levels)]
 for i,j,k in product(range(H),repeat=3):
  degree=degrees[i]+degrees[j]+degrees[k]
  if degree>=0:out[degree]+=np.einsum('iab,jbc,kca->ijk',P[0][i],P[1][j],P[2][k],optimize=True)
 return out
for step in range(a.sweeps):
 for leg in range(3):
  P=physical(M);pair={}
  for i,j in product(range(H),repeat=2):
   if leg==0:D=np.einsum('sab,jbc,kca->jks',W,P[1][i],P[2][j],optimize=True)
   elif leg==1:D=np.einsum('iab,sbc,kca->iks',P[0][i],W,P[2][j],optimize=True)
   else:D=np.einsum('iab,jbc,sca->ijs',P[0][i],P[1][j],W,optimize=True)
   deg=degrees[i]+degrees[j];pair[deg]=pair.get(deg,0)+D.reshape(-1,45)
  zero=np.zeros_like(next(iter(pair.values())));D=np.concatenate([np.concatenate([pair.get(degree-h,zero) for h in degrees],axis=1) for degree in range(levels)],axis=0)
  M[leg]=np.linalg.lstsq(D,rhses[leg],rcond=1e-12)[0].reshape(H,45,-1)
 norms=[np.linalg.norm(m) for m in M];common=np.prod(norms)**(1/3);M=[m*common/n for m,n in zip(M,norms)]
 if step%10==0 or step+1==a.sweeps:
  out=outputs(physical(M));errors=[float(np.linalg.norm(T-(target if d==0 else 0))/10) for d,T in enumerate(out)];error=float(np.linalg.norm(errors));history.append([step,error,errors,float(common),time.monotonic()-start]);print(history[-1],flush=True)
  if error<best:best=error;np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',M)))
  report={'status':'numerical Laurent-family search only, not an exact degeneration','degrees':degrees,'required_output_coefficients':list(range(levels)),'best_joint_relative_error':best,'history':history,'sweeps':step+1};(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
