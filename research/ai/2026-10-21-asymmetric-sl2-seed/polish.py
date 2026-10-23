"""Analytic-Jacobian numerical polishing, never an exact certificate."""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
p=argparse.ArgumentParser();p.add_argument('directory',type=Path);a=p.parse_args();d=a.directory
z=np.load(d/'discovery-problem.npz');m=np.load(d/'best.npz');C=z['compressed'];rhs=z['rhs'];sizes=C.shape[1:];cuts=np.cumsum(sizes)[:-1]
bases=[z[n+'_basis'] for n in 'ABC'];pars=[np.einsum('rst,st->r',b,m[n]) for b,n in zip(bases,'ABC')];initial=np.concatenate(pars);N=len(initial)
def unpack(x):return np.split(x[:N]+1j*x[N:],cuts)
def fun(x):
 r=np.einsum('tijk,i,j,k->t',C,*unpack(x),optimize=True)-rhs
 return np.r_[r.real,r.imag]
def jac(x):
 aa,b,c=unpack(x)
 J=np.concatenate([np.einsum('tijk,j,k->ti',C,b,c),np.einsum('tijk,i,k->tj',C,aa,c),np.einsum('tijk,i,j->tk',C,aa,b)],axis=1)
 return np.block([[J.real,-J.imag],[J.imag,J.real]])
r=least_squares(fun,np.r_[initial.real,initial.imag],jac=jac,max_nfev=3000,ftol=1e-14,xtol=1e-14,gtol=1e-14,x_scale='jac')
pars=unpack(r.x);maps=[np.einsum('r,rst->st',v,b) for v,b in zip(pars,bases)];W=z['W'];phys=[np.einsum('st,sab->tab',v,W) for v in maps];full=np.einsum('iab,jbc,kca->ijk',*phys,optimize=True);w=int(z['vertex_w']);target=np.zeros_like(full)
for i in range(5):
 for j in range(5):
  for k in range(w):target[5*i+j,w*j+k,5*k+i]=1
coeffs=[z[n+'_transform']@v for n,v in zip('ABC',pars)]
np.savez_compressed(d/'polished.npz',**dict(zip('ABC',maps)),**{n+'_coefficients':v for n,v in zip('ABC',coeffs)})
report={'status':'numerical only; exact verification required','nfev':r.nfev,'message':r.message,'full_relative_error':float(np.linalg.norm(full-target)/np.linalg.norm(target)),'maximum_coefficient_error':float(np.max(np.abs(full-target))),'parameter_norms':[float(np.linalg.norm(x)) for x in pars],'coefficients':[[[float(v.real),float(v.imag)] for v in c] for c in coeffs]}
(d/'polish-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
