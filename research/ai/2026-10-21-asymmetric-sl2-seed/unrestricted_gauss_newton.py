"""Matrix-free complex Gauss-Newton discovery; no exact identity claim."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('warm',type=Path);p.add_argument('output',type=Path);p.add_argument('--evaluations',type=int,default=100);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
z=np.load(a.warm);M=[z[n].copy() for n in 'ABC'];W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);shapes=[m.shape for m in M];sizes=[m.size for m in M];cuts=np.cumsum(sizes)[:-1];N=sum(sizes);w=shapes[1][1]//5;target=np.zeros((25,5*w,5*w))
for i in range(5):
 for j in range(5):
  for k in range(w):target[5*i+j,w*j+k,5*k+i]=1
K=target.size;start=time.monotonic();history=[];calls=0;best=float('inf')
def unpack(x):return [v.reshape(s) for v,s in zip(np.split(x[:N]+1j*x[N:],cuts),shapes)]
def phys(m):return [np.einsum('st,sab->tab',v,W,optimize=True) for v in m]
def image(P):return np.einsum('iab,jbc,kca->ijk',*P,optimize=True)
def real(v):return np.r_[v.real.ravel(),v.imag.ravel()]
def fun(x):
 global calls,best
 m=unpack(x);r=image(phys(m))-target;err=float(np.linalg.norm(r)/np.linalg.norm(target));calls+=1
 if err<best:best=err;np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',m)))
 if calls%5==1:
  history.append([calls,err,float(np.linalg.norm(x)),time.monotonic()-start]);print(history[-1],flush=True)
  (a.output/'progress.json').write_text(json.dumps({'status':'numerical only','history':history,'best_relative_error':best},indent=2)+'\n')
 return real(r)
def jac(x):
 P=phys(unpack(x))
 def mv(v):
  Q=phys(unpack(np.asarray(v).ravel()));return real(image([Q[0],P[1],P[2]])+image([P[0],Q[1],P[2]])+image([P[0],P[1],Q[2]]))
 def rmv(y):
  y=np.asarray(y).ravel();R=(y[:K]+1j*y[K:]).reshape(target.shape)
  G=[np.einsum('ijk,jbc,kca->iab',R,P[1].conj(),P[2].conj(),optimize=True),np.einsum('ijk,kca,iab->jbc',R,P[2].conj(),P[0].conj(),optimize=True),np.einsum('ijk,iab,jbc->kca',R,P[0].conj(),P[1].conj(),optimize=True)]
  g=np.concatenate([np.einsum('tab,sab->st',v,W,optimize=True).ravel() for v in G]);return real(g)
 return LinearOperator((2*K,2*N),matvec=mv,rmatvec=rmv,dtype=float)
xc=np.concatenate([m.ravel() for m in M]);x=real(xc);rng=np.random.default_rng(314159);v=rng.normal(size=2*N);v/=np.linalg.norm(v);y=rng.normal(size=2*K);J=jac(x)
assert abs(float(y@(J@v))-float((J.rmatvec(y))@v))<1e-8
fd=(fun(x+1e-6*v)-fun(x-1e-6*v))/(2e-6);assert np.linalg.norm(fd-J@v)/np.linalg.norm(J@v)<1e-7
fit=least_squares(fun,x,jac=jac,tr_solver='lsmr',tr_options={'maxiter':150,'atol':1e-9,'btol':1e-9},max_nfev=a.evaluations,ftol=1e-13,xtol=1e-13,gtol=1e-11)
report={'status':'numerical only; no exact restriction claimed','nfev':fit.nfev,'message':fit.message,'best_relative_error':best,'final_relative_error':float(np.linalg.norm(fit.fun)/np.linalg.norm(target)),'history':history,'seconds':time.monotonic()-start}
(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
