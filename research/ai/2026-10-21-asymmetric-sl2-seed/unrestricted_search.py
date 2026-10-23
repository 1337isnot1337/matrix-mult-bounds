"""Unrestricted complex-map discovery from the exact rectangular seed.

All original source coefficients are contracted. Numerical residuals are
not certificates, regardless of their size.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from scipy.optimize import minimize
from rectangular_exact import maps
from intertwiners import source_data

def run(output,steps,seed,warm=None):
 output.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(seed);W=np.array([np.array(x).astype(float) for x in source_data(3)[0]])
 A,B,C=[np.array(m,dtype=float) for m in maps()];BB=np.zeros((45,5,4));CC=np.zeros((45,4,5));BB[:,:,:3]=B.reshape(45,5,3);CC[:,:3,:]=C.reshape(45,3,5);M=[A,BB.reshape(45,20),CC.reshape(45,20)]
 norms=[np.linalg.norm(m) for m in M];common=np.prod(norms)**(1/3);M=[m*common/n for m,n in zip(M,norms)]
 M=[m+rng.normal(size=m.shape)*0.05 for m in M]
 if warm:
  z=np.load(warm);AA=z['A'].T;BB=np.empty((45,25),dtype=complex);CC=np.empty((45,25),dtype=complex)
  for i in range(3):
   for k in range(5):
    for t in range(3):
     BB[(i*5+k)*3+t]=z['B'][:,(t*3+i)*5+k]
     CC[(i*5+k)*3+t]=z['C'][:,(k*3+t)*3+i]
  PP=[np.einsum('st,sab->tab',m,W) for m in [AA,BB,CC]];TT=np.einsum('iab,jbc,kca->ijk',*PP,optimize=True);wanted=np.zeros((25,25,25))
  for i in range(5):
   for j in range(5):
    for k in range(5):wanted[5*i+j,5*j+k,5*k+i]=1
  residual=float(np.linalg.norm(TT-wanted)/np.linalg.norm(wanted));assert abs(residual-float(z['error']))<1e-9,(residual,z['error'])
  M=[AA,BB.reshape(45,5,5)[:,:,:4].reshape(45,20),CC.reshape(45,5,5)[:,:4,:].reshape(45,20)]
  print('verified full warm seed residual',residual,flush=True)
 sizes=[1125,900,900];cuts=np.cumsum(sizes)[:-1];target=np.zeros((25,20,20))
 for i in range(5):
  for j in range(5):
   for k in range(4):target[5*i+j,4*j+k,5*k+i]=1
 shapes=[(45,25),(45,20),(45,20)];calls=0;best=float('inf');history=[];start=time.monotonic()
 def objective(x):
  nonlocal calls,best
  xc=x[:2925]+1j*x[2925:];matrices=[v.reshape(s) for v,s in zip(np.split(xc,cuts),shapes)];P=[np.einsum('st,sab->tab',m,W,optimize=True) for m in matrices]
  T=np.einsum('iab,jbc,kca->ijk',*P,optimize=True);R=T-target;loss=float(np.sum(np.abs(R)**2)/100)
  gradients=[np.einsum('ijk,jbc,kca->iab',R,P[1].conj(),P[2].conj(),optimize=True),np.einsum('ijk,kca,iab->jbc',R,P[2].conj(),P[0].conj(),optimize=True),np.einsum('ijk,iab,jbc->kca',R,P[0].conj(),P[1].conj(),optimize=True)]
  grad=np.concatenate([np.einsum('tab,sab->st',g,W,optimize=True).ravel() for g in gradients])*0.02
  if loss<best:
   best=loss
   if calls%50==0:np.savez_compressed(output/'best.npz',**dict(zip('ABC',matrices)))
  if calls%100==0:
   history.append([calls,loss**0.5,float(np.linalg.norm(x)),time.monotonic()-start]);print(history[-1],flush=True)
  calls+=1;return loss,np.r_[grad.real,grad.imag]
 xc=np.concatenate([m.ravel() for m in M]);x=np.r_[xc.real,xc.imag];f,g=objective(x)
 # Directional finite-difference check of the complete analytic gradient.
 v=rng.normal(size=x.size);v/=np.linalg.norm(v);eps=1e-5
 numeric=(objective(x+eps*v)[0]-objective(x-eps*v)[0])/(2*eps);analytic=float(g@v)
 assert abs(numeric-analytic)<1e-6*max(1,abs(analytic)),(numeric,analytic)
 fit=minimize(objective,x,jac=True,method='L-BFGS-B',options={'maxiter':steps,'maxls':30,'ftol':1e-15,'gtol':1e-10,'maxcor':30})
 final=[v.reshape(s) for v,s in zip(np.split(fit.x[:2925]+1j*fit.x[2925:],cuts),shapes)];np.savez_compressed(output/'final.npz',**dict(zip('ABC',final)))
 report={'status':'numerical discovery only','seed':seed,'iterations':fit.nit,'evaluations':calls,'message':str(fit.message),'final_relative_error':float(fit.fun**0.5),'best_relative_error':best**0.5,'history':history,'no_exact_restriction_claimed':True,'elapsed_seconds':time.monotonic()-start}
 (output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=Path('results/local/asymmetric-sl2-seed/unrestricted'));p.add_argument('--steps',type=int,default=3000);p.add_argument('--seed',type=int,default=271828);p.add_argument('--warm',type=Path);a=p.parse_args();run(a.output,a.steps,a.seed,a.warm)
