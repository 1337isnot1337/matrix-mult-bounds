"""Target-stabilizer norm balancing for numerical discovery maps."""
from pathlib import Path
import argparse,json
import numpy as np
from intertwiners import source_data
from rectangular_exact import maps

def power(H,p):
 vals,vec=np.linalg.eigh((H+H.conj().T)/2)
 if min(vals)<=max(vals)*1e-12:raise ValueError('Singular covariance; no unverified inverse used')
 return (vec*vals**p)@vec.conj().T

def balance(M,sweeps):
 w=M[1].shape[1]//5;A,B,C=[m.reshape(45,*s) for m,s in zip(M,[(5,5),(5,w),(w,5)])];blocks=[A.copy(),B.copy(),C.copy()];history=[]
 for step in range(sweeps):
  for vertex in range(3):
   outgoing=blocks[vertex];incoming=blocks[(vertex-1)%3]
   X=np.einsum('sij,skj->ik',outgoing,outgoing.conj());Y=np.einsum('sij,sik->jk',incoming.conj(),incoming)
   Xhalf=power(X,.5);Xinv=power(X,-.5);Z=Xinv@power(Xhalf@Y@Xhalf,.5)@Xinv;P=power(Z,.5);Pinv=np.linalg.inv(P)
   before=sum(np.linalg.norm(b)**2 for b in blocks);blocks[vertex]=np.einsum('ij,sjk->sik',P,outgoing);blocks[(vertex-1)%3]=np.einsum('sij,jk->sik',incoming,Pinv);after=sum(np.linalg.norm(b)**2 for b in blocks)
   assert after<=before*(1+1e-10),(before,after)
  history.append(float(np.sqrt(after)))
 return [b.reshape(45,-1) for b in blocks],history

def error(M):
 W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);P=[np.einsum('st,sab->tab',m,W,optimize=True) for m in M];T=np.einsum('iab,jbc,kca->ijk',*P,optimize=True);w=M[1].shape[1]//5;target=np.zeros_like(T)
 for i in range(5):
  for j in range(5):
   for k in range(w):target[5*i+j,w*j+k,5*k+i]=1
 return float(np.linalg.norm(T-target)/np.linalg.norm(target))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);p.add_argument('--sweeps',type=int,default=20);a=p.parse_args()
 # An exact rectangular positive control verifies the action and index order.
 control=[np.array(m,dtype=complex) for m in maps()];control,h=balance(control,3);assert error(control)<1e-12
 z=np.load(a.input);M=[z[n] for n in 'ABC'];before=error(M);norm=float(np.sqrt(sum(np.linalg.norm(m)**2 for m in M)));balanced,h=balance(M,a.sweeps);after=error(balanced)
 a.output.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',balanced)));report={'status':'numerical gauge change, not a restriction certificate','before_error':before,'after_error':after,'before_norm':norm,'norm_history':h,'exact_control_passed':True};(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
