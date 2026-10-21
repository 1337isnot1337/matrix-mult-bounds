"""Factored-Jacobian refinement of actual Laurent coefficient equations."""
import argparse,json,time,hashlib,io
from pathlib import Path
from itertools import product
import numpy as np
from scipy.optimize import least_squares
from scipy.sparse.linalg import LinearOperator
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('warm',type=Path);p.add_argument('output',type=Path);p.add_argument('--evaluations',type=int,default=60);p.add_argument('--linear-iterations',type=int,default=300);p.add_argument('--degree',type=int);p.add_argument('--padding-noise',type=float,default=1e-4);p.add_argument('--unregularized',action='store_true');p.add_argument('--preconditioner-floor',type=float,default=1e-10);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);raw=a.warm.read_bytes();input_sha256=hashlib.sha256(raw).hexdigest();(a.output/'input-checkpoint.npz').write_bytes(raw);z=np.load(io.BytesIO(raw));M=[z[n].copy() for n in 'ABC']
if a.degree is not None and 2*a.degree+1>M[0].shape[0]:
 old=M[0].shape[0];new=2*a.degree+1;shift=(new-old)//2;rng=np.random.default_rng(314159);padded=[]
 for m in M:
  v=(rng.normal(size=(new,*m.shape[1:]))+1j*rng.normal(size=(new,*m.shape[1:])))*a.padding_noise;v[shift:shift+old]=m;padded.append(v)
 M=padded
shapes=[m.shape for m in M];sizes=[m.size for m in M];cuts=np.cumsum(sizes)[:-1];N=sum(sizes);W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);H=M[0].shape[0];d=(H-1)//2;assert H==2*d+1;degrees=list(range(d,-d-1,-1));levels=3*d+1;L=45*H;target=np.zeros((levels,25,20,20),dtype=complex);K=target.size
for i,j,k in product(range(5),range(5),range(4)):target[0,5*i+j,4*j+k,5*k+i]=1
start=time.monotonic();history=[];best=float('inf');calls=0

def physical(M):return [np.einsum('hst,sab->htab',m,W,optimize=True) for m in M]
def output(M):
 P=physical(M);out=np.zeros_like(target)
 for i,j,k in product(range(H),repeat=3):
  degree=degrees[i]+degrees[j]+degrees[k]
  if degree>=0:out[degree]+=np.einsum('iab,jbc,kca->ijk',P[0][i],P[1][j],P[2][k],optimize=True)
 return out

def operators(M):
 P=physical(M);Ds=[]
 for leg in range(3):
  pair={}
  for i,j in product(range(H),repeat=2):
   if leg==0:D=np.einsum('sab,jbc,kca->jks',W,P[1][i],P[2][j],optimize=True)
   elif leg==1:D=np.einsum('iab,sbc,kca->iks',P[0][i],W,P[2][j],optimize=True)
   else:D=np.einsum('iab,jbc,sca->ijs',P[0][i],P[1][j],W,optimize=True)
   degree=degrees[i]+degrees[j];pair[degree]=pair.get(degree,0)+D.reshape(-1,45)
  zero=np.zeros_like(next(iter(pair.values())));Ds.append(np.concatenate([np.concatenate([pair.get(degree-h,zero) for h in degrees],axis=1) for degree in range(levels)],axis=0))
 return Ds
S=[]
for D in operators(M):
 values,vectors=np.linalg.eigh(D.conj().T@D);values=np.maximum(values,values[-1]*a.preconditioner_floor);S.append((vectors/np.sqrt(values))@vectors.conj().T)
def unpack(x):return [(Q@v.reshape(L,-1)).reshape(s) for Q,v,s in zip(S,np.split(x[:N]+1j*x[N:],cuts),shapes)]
def real(x):return np.r_[x.real.ravel(),x.imag.ravel()]
def fun(x):
 global calls,best
 m=unpack(x);R=output(m)-target;error=float(np.linalg.norm(R)/10);calls+=1
 if error<best:best=error;np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',m)))
 if calls%5==1:
  history.append([calls,error,[float(np.linalg.norm(r)/10) for r in R],float(np.sqrt(sum(np.linalg.norm(v)**2 for v in m))),time.monotonic()-start]);print(history[-1],flush=True)
  (a.output/'progress.json').write_text(json.dumps({'status':'numerical Laurent coefficients only','history':history,'best_joint_relative_error':best},indent=2)+'\n')
 return real(R)
def jac(x):
 D=[d@q for d,q in zip(operators(unpack(x)),S)]
 def mv(v):
  v=np.asarray(v).ravel();V=[q.reshape(L,-1) for q in np.split(v[:N]+1j*v[N:],cuts)];X=(D[0]@V[0]).reshape(levels,20,20,25).transpose(0,3,1,2);Y=(D[1]@V[1]).reshape(levels,25,20,20).transpose(0,1,3,2);Z=(D[2]@V[2]).reshape(levels,25,20,20);return real(X+Y+Z)
 def rmv(y):
  y=np.asarray(y).ravel();R=(y[:K]+1j*y[K:]).reshape(target.shape);R=[R.transpose(0,2,3,1).reshape(-1,25),R.transpose(0,1,3,2).reshape(-1,20),R.reshape(-1,20)];return real(np.concatenate([(d.conj().T@r).ravel() for d,r in zip(D,R)]))
 return LinearOperator((2*K,2*N),matvec=mv,rmatvec=rmv,dtype=float)
xc=np.concatenate([np.linalg.solve(q,m.reshape(L,-1)).ravel() for q,m in zip(S,M)]);x=real(xc);rng=np.random.default_rng(271828);v=rng.normal(size=2*N);v/=np.linalg.norm(v);y=rng.normal(size=2*K);J=jac(x);left=y@(J@v);right=J.rmatvec(y)@v;assert abs(left-right)<1e-8*max(1,abs(left),abs(right))
errors=[]
for h in (1e-2,1e-3):
 d1=(fun(x+h*v)-fun(x-h*v))/(2*h);d2=(fun(x+h*v/2)-fun(x-h*v/2))/h;errors.append(float(np.linalg.norm((4*d2-d1)/3-J@v)/np.linalg.norm(J@v)))
print('directional errors',errors,flush=True);assert min(errors)<1e-7
fit=least_squares(fun,x,jac=jac,tr_solver='lsmr',tr_options={'maxiter':a.linear_iterations,'atol':1e-9,'btol':1e-9,'regularize':not a.unregularized},max_nfev=a.evaluations,ftol=1e-13,xtol=1e-13,gtol=1e-11);report={'status':'numerical only; no degeneration certificate','degree':d,'padding_noise':a.padding_noise,'input_sha256':input_sha256,'regularized':not a.unregularized,'preconditioner_floor':a.preconditioner_floor,'linear_iterations':a.linear_iterations,'nfev':fit.nfev,'message':fit.message,'best_joint_relative_error':best,'history':history,'seconds':time.monotonic()-start};(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
