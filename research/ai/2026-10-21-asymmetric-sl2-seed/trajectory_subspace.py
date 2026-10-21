"""Try the span of prior numerical trajectories; no exactness claim."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from intertwiners import source_data
p=argparse.ArgumentParser();p.add_argument('output',type=Path);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
root=Path('results/local/asymmetric-sl2-seed');names=['unrestricted-warm','unrestricted-als','balanced-als','gauss-newton-preconditioned','sparse-gauss-newton','sparse-gauss-newton-restart'];inputs=[np.load(root/n/'best.npz') for n in names];bases=[];initial=[]
for leg in 'ABC':
 raw=np.stack([z[leg].ravel() for z in inputs],axis=1);Q,R=np.linalg.qr(raw);basis=Q.T.reshape(len(inputs),*inputs[0][leg].shape);bases.append(basis);initial.append(Q.conj().T@inputs[-1][leg].ravel())
W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);P=[np.einsum('ast,sxy->atxy',b,W,optimize=True) for b in bases];fullcore=np.einsum('aixy,bjyz,ckzx->ijkabc',*P,optimize=True);flat=fullcore.reshape(10000,-1);target=np.zeros((25,20,20))
for i in range(5):
 for j in range(5):
  for k in range(4):target[5*i+j,4*j+k,5*k+i]=1
Q,R=np.linalg.qr(flat);rhs=Q.conj().T@target.ravel();discard=target.ravel()-Q@rhs;floor=float(np.linalg.norm(discard)/10);C=R.reshape(-1,6,6,6);print('linear span residual floor',floor,flush=True);N=18

def unpack(x):return np.split(x[:N]+1j*x[N:],3)
def fun(x):
 r=np.einsum('tijk,i,j,k->t',C,*unpack(x),optimize=True)-rhs;return np.r_[r.real,r.imag]
def jac(x):
 aa,b,c=unpack(x);J=np.concatenate([np.einsum('tijk,j,k->ti',C,b,c),np.einsum('tijk,i,k->tj',C,aa,c),np.einsum('tijk,i,j->tk',C,aa,b)],axis=1);return np.block([[J.real,-J.imag],[J.imag,J.real]])
x=np.concatenate(initial);fit=least_squares(fun,np.r_[x.real,x.imag],jac=jac,max_nfev=1000,ftol=1e-13,xtol=1e-13,gtol=1e-12);pars=unpack(fit.x);M=[np.einsum('a,ast->st',v,b) for v,b in zip(pars,bases)];physical=[np.einsum('st,sxy->txy',m,W) for m in M];T=np.einsum('ixy,jyz,kzx->ijk',*physical,optimize=True);err=float(np.linalg.norm(T-target)/10);np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',M)));report={'status':'numerical only','input_trajectories':names,'basis_dimensions':[6,6,6],'linear_span_residual_floor':floor,'optimized_full_relative_error':err,'nfev':fit.nfev,'message':fit.message};(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
