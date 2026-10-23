"""SL2^3 source-gauge norm optimization; checks the full tensor is unchanged."""
from pathlib import Path
import argparse,json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize
from intertwiners import irrep,source_data
SHORT=[np.array(x).astype(float) for x in irrep(2)];LONG=[np.array(-x.T).astype(float) for x in irrep(4)];POSITIONS=[[0,1,2],[2,0,1],[1,2,0]]
def transform(M,x):
 parameters=(x[:9]+1j*x[9:]).reshape(3,3);short=[expm(sum(v*G for v,G in zip(p,SHORT))) for p in parameters];long=[expm(sum(v*G for v,G in zip(p,LONG))) for p in parameters];out=[]
 for leg,m in enumerate(M):
  T=m.reshape(3,5,3,-1)
  for factor in range(3):
   axis=POSITIONS[leg][factor];Q=long[factor] if axis==1 else short[factor];V=np.moveaxis(T,axis,0);V=(Q@V.reshape(V.shape[0],-1)).reshape(V.shape);T=np.moveaxis(V,0,axis)
  out.append(T.reshape(m.shape))
 return out

def image(M,W):
 P=[np.einsum('st,sab->tab',m,W,optimize=True) for m in M];return np.einsum('iab,jbc,kca->ijk',*P,optimize=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);z=np.load(a.input);M=[z[n].copy() for n in 'ABC'];W=np.array([np.array(x).astype(float) for x in source_data(3)[0]]);before=image(M,W);history=[];initial=float(np.sqrt(sum(np.linalg.norm(m)**2 for m in M)))
 # Check a generic finite source action before optimizing any parameters.
 rng=np.random.default_rng(271828);test=transform(M,rng.normal(size=18)*0.03);assert np.linalg.norm(image(test,W)-before)/np.linalg.norm(before)<1e-9
 for phase in range(3):
  def objective(x):return float(sum(np.linalg.norm(m)**2 for m in transform(M,x)))
  fit=minimize(objective,np.zeros(18),method='L-BFGS-B',bounds=[(-1,1)]*18,options={'maxiter':150,'ftol':1e-13,'gtol':1e-7})
  candidate=transform(M,fit.x);drift=float(np.linalg.norm(image(candidate,W)-before)/np.linalg.norm(before));assert drift<1e-9,drift;M=candidate;history.append({'phase':phase,'norm':float(np.sqrt(fit.fun)),'iterations':fit.nit,'tensor_relative_drift':drift});print(history[-1],flush=True)
 np.savez_compressed(a.output/'best.npz',**dict(zip('ABC',M)));report={'status':'numerical source gauge; no new restriction claimed','initial_norm':initial,'phases':history,'generic_action_control_passed':True};(a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
