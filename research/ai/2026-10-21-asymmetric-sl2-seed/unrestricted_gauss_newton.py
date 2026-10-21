"""Matrix-free complex Gauss-Newton discovery; no exact identity claim."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('warm',type=Path);p.add_argument('output',type=Path);p.add_argument('--evaluations',type=int,default=100);p.add_argument('--precondition',action='store_true');a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
z=np.load(a.warm);M=[z[n].copy() for n in 'ABC'];W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);shapes=[m.shape for m in M];sizes=[m.size for m in M];cuts=np.cumsum(sizes)[:-1];N=sum(sizes);w=shapes[1][1]//5;target=np.zeros((25,5*w,5*w))
for i in range(5):
 for j in range(5):
  for k in range(w):target[5*i+j,w*j+k,5*k+i]=1
K=target.size;start=time.monotonic();history=[];calls=0;best=float('inf')
S=[np.eye(45,dtype=complex) for _ in M]
if a.precondition:
 P0=[np.einsum('st,sab->tab',m,W,optimize=True) for m in M]
 Ds=[np.einsum('sab,jbc,kca->jks',W,P0[1],P0[2],optimize=True),np.einsum('iab,sbc,kca->iks',P0[0],W,P0[2],optimize=True),np.einsum('iab,jbc,sca->ijs',P0[0],P0[1],W,optimize=True)]
 S=[]
 for D in Ds:
  D=D.reshape(-1,45);values,vectors=np.linalg.eigh(D.conj().T@D);values=np.maximum(values,values[-1]*1e-10);S.append((vectors/np.sqrt(values))@vectors.conj().T)
 print('initial block-normal preconditioning enabled',flush=True)
def unpack(x):return [Q@v.reshape(s) for Q,v,s in zip(S,np.split(x[:N]+1j*x[N:],cuts),shapes)]
def phys(m):return [np.einsum('st,sab->tab',v,W,optimize=True) for v in m]
def image(P):return np.einsum('iab,jbc,kca->ijk',*P,optimize=True)
def real(v):return np.r_[v.real.ravel(),v.imag.ravel()]
def fun(x):
 global calls,best
 m=unpack(x);r=image(phys(m))-target;err=float(np.linalg.norm(r)/np.linalg.norm(target));calls+=1
 if err<best:best=err;np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',m)))
 if calls%5==1:
  history.append([calls,err,float(np.sqrt(sum(np.linalg.norm(v)**2 for v in m))),time.monotonic()-start]);print(history[-1],flush=True)
  (a.output/'progress.json').write_text(json.dumps({'status':'numerical only','history':history,'best_relative_error':best},indent=2)+'\n')
 return real(r)
def jac(x):
 P=phys(unpack(x))
 def mv(v):
  Q=phys(unpack(np.asarray(v).ravel()));return real(image([Q[0],P[1],P[2]])+image([P[0],Q[1],P[2]])+image([P[0],P[1],Q[2]]))
 def rmv(y):
  y=np.asarray(y).ravel();R=(y[:K]+1j*y[K:]).reshape(target.shape)
  G=[np.einsum('ijk,jbc,kca->iab',R,P[1].conj(),P[2].conj(),optimize=True),np.einsum('ijk,kca,iab->jbc',R,P[2].conj(),P[0].conj(),optimize=True),np.einsum('ijk,iab,jbc->kca',R,P[0].conj(),P[1].conj(),optimize=True)]
  g=np.concatenate([(Q.conj().T@np.einsum('tab,sab->st',v,W,optimize=True)).ravel() for Q,v in zip(S,G)]);return real(g)
 return LinearOperator((2*K,2*N),matvec=mv,rmatvec=rmv,dtype=float)
xc=np.concatenate([np.linalg.solve(Q,m).ravel() for Q,m in zip(S,M)]);x=real(xc);rng=np.random.default_rng(314159);v=rng.normal(size=2*N);v/=np.linalg.norm(v);y=rng.normal(size=2*K);J=jac(x)
assert abs(float(y@(J@v))-float((J.rmatvec(y))@v))<1e-8
# The map is cubic. Richardson cancellation removes its central-difference
# cubic error, permitting a larger step that avoids subtractive cancellation.
errors=[]
for h in (1e-2,1e-3,1e-4):
 d1=(fun(x+h*v)-fun(x-h*v))/(2*h);d2=(fun(x+h*v/2)-fun(x-h*v/2))/h
 fd=(4*d2-d1)/3;errors.append(float(np.linalg.norm(fd-J@v)/np.linalg.norm(J@v)))
print('Jacobian directional relative errors',errors,flush=True)
assert min(errors)<1e-7,errors
fit=least_squares(fun,x,jac=jac,tr_solver='lsmr',tr_options={'maxiter':150,'atol':1e-9,'btol':1e-9},max_nfev=a.evaluations,ftol=1e-13,xtol=1e-13,gtol=1e-11)
report={'status':'numerical only; no exact restriction claimed','nfev':fit.nfev,'message':fit.message,'best_relative_error':best,'final_relative_error':float(np.linalg.norm(fit.fun)/np.linalg.norm(target)),'history':history,'seconds':time.monotonic()-start}
(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
