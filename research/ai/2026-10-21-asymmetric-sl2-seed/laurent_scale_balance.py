"""Balance Laurent-variable scale; this is not progress toward an identity."""
from pathlib import Path
import argparse,hashlib,io,json
import numpy as np

def scale_data(maps):
 H=maps[0].shape[0];d=(H-1)//2;degrees=np.arange(d,-d-1,-1)
 q=sum(np.sum(np.abs(m)**2,axis=(1,2)) for m in maps)
 if not np.any(q[degrees>0]) or not np.any(q[degrees<0]):
  raise ValueError('Need nonzero coefficients on both sides for a finite scale minimum')
 def derivative(t):return float(np.sum(degrees*q*np.exp(2*degrees*t)))
 lo,hi=-20.,20.
 assert derivative(lo)<0<derivative(hi)
 for _ in range(100):
  mid=(lo+hi)/2
  if derivative(mid)>0:hi=mid
  else:lo=mid
 logc=(lo+hi)/2;c=float(np.exp(logc));factors=c**degrees
 den=float(np.sum(degrees**2*q*factors**2))
 gradients=[-(degrees*factors**2)[:,None,None]*m/den for m in maps]
 return c,gradients

def balance(maps):
 c,_=scale_data(maps);d=(maps[0].shape[0]-1)//2;degrees=np.arange(d,-d-1,-1);factors=c**degrees
 out=[m*factors[:,None,None] for m in maps]
 return out,{'scale':c,'initial_coefficient_norm':float(np.sqrt(sum(np.linalg.norm(m)**2 for m in maps))),
             'balanced_coefficient_norm':float(np.sqrt(sum(np.linalg.norm(m)**2 for m in out))),
             'degree_order':degrees.tolist(),'positive_residual_multipliers':(c**np.arange(3*d+1)).tolist(),
             'constant_tensor_coefficient_unchanged_algebraically':True,
             'residual_norms_are_scale_dependent':True,'exact_certificate':False}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
 raw=a.input.read_bytes();z=np.load(io.BytesIO(raw));out,r=balance([z[n] for n in 'ABC']);a.output.mkdir(parents=True,exist_ok=True)
 np.savez_compressed(a.output/'balanced.npz',**dict(zip('ABC',out)));r['input_sha256']=hashlib.sha256(raw).hexdigest()
 (a.output/'report.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
