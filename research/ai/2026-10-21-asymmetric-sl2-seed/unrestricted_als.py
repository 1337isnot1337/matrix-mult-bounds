"""Complex alternating least squares on unrestricted original-source maps."""
import argparse,json,time
from pathlib import Path
import numpy as np
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('warm',type=Path);p.add_argument('output',type=Path);p.add_argument('--sweeps',type=int,default=5000);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
z=np.load(a.warm);M=[z[n].copy() for n in 'ABC'];W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);w=M[1].shape[1]//5;target=np.zeros((25,5*w,5*w))
for i in range(5):
 for j in range(5):
  for k in range(w):target[5*i+j,w*j+k,5*k+i]=1
start=time.monotonic();history=[];best=float('inf')
for step in range(a.sweeps):
 for leg in range(3):
  P=[np.einsum('st,sab->tab',m,W,optimize=True) for m in M]
  if leg==0:D=np.einsum('sab,jbc,kca->jks',W,P[1],P[2],optimize=True);rhs=target.transpose(1,2,0).reshape(-1,25)
  elif leg==1:D=np.einsum('iab,sbc,kca->iks',P[0],W,P[2],optimize=True);rhs=target.transpose(0,2,1).reshape(-1,5*w)
  else:D=np.einsum('iab,jbc,sca->ijs',P[0],P[1],W,optimize=True);rhs=target.reshape(-1,5*w)
  M[leg]=np.linalg.lstsq(D.reshape(-1,45),rhs,rcond=1e-12)[0]
 norms=[np.linalg.norm(m) for m in M];common=np.prod(norms)**(1/3);M=[m*common/n for m,n in zip(M,norms)]
 if step%25==0 or step+1==a.sweeps:
  P=[np.einsum('st,sab->tab',m,W,optimize=True) for m in M];T=np.einsum('iab,jbc,kca->ijk',*P,optimize=True);err=float(np.linalg.norm(T-target)/np.linalg.norm(target));history.append([step,err,float(common),time.monotonic()-start]);print(history[-1],flush=True)
  if err<best:
   best=err;np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',M)))
  report={'status':'numerical discovery only','warm':str(a.warm),'sweeps':step+1,'best_relative_error':best,'history':history,'no_exact_restriction_claimed':True}
  (a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
  if err<1e-12:break
