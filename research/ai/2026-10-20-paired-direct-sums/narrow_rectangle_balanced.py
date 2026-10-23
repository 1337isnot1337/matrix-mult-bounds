"""Bounded MM-rectangle fitting with the exact target gauge group.

Gauge balancing changes all three maps together and preserves the complete
MM tensor. Complex coefficient fits remain numerical until exact replay.
"""
import argparse,importlib.util,json,time
from pathlib import Path
import numpy as np
from itertools import product
import rectangle_search_common as boundary

def apply_axis(matrix,array,axis):
    moved=np.moveaxis(array,axis,0);shape=moved.shape
    return np.moveaxis((matrix@moved.reshape(shape[0],-1)).reshape(shape),0,axis)

def covariance(array,axis):
    x=np.moveaxis(array,axis,0).reshape(array.shape[axis],-1)
    return x@x.conj().T

def positive_power(matrix,power,floor=1e-12):
    vals,vecs=np.linalg.eigh((matrix+matrix.conj().T)/2)
    vals=np.maximum(vals,floor*max(1.0,float(np.max(vals))))
    return (vecs*vals**power)@vecs.conj().T

def balance_pair(left,la,right,ra):
    g=covariance(left,la);h=covariance(right,ra).conj()
    gh=positive_power(g,0.5);gm=positive_power(g,-0.5)
    scale=gm@positive_power(gh@h@gh,0.5)@gm
    transform=positive_power(scale,0.5)
    # The transpose, without complex conjugation, enforces bilinear duality.
    left=apply_axis(transform,left,la)
    right=apply_axis(np.linalg.inv(transform).T,right,ra)
    return left,right

def gauge(maps,l,b,r):
    shapes=[(l,r,maps[0].shape[1]),(l,b,maps[1].shape[1]),(b,r,maps[2].shape[1])]
    a,bb,c=[m.reshape(s) for m,s in zip(maps,shapes)]
    a,bb=balance_pair(a,0,bb,0)
    bb,c=balance_pair(bb,1,c,0)
    a,c=balance_pair(a,1,c,1)
    return [x.reshape(m.shape) for x,m in zip([a,bb,c],maps)]

def fit(n,b,defect,seed,iterations,iscomplex,checkpoint,initial=None):
    ss,st,_,_=boundary.base.coordinates(n,b);l=n-defect
    source=np.zeros(ss)
    for pt in st:source[pt]+=1
    target,projection,repair=boundary.target_data(n,b,'rectangle',defect)
    rng=np.random.default_rng(seed)
    if initial:
        old=json.loads(initial.read_text())
        if 'maps' in old:
            maps=[np.array(m,dtype=complex if iscomplex else float) for m in old['maps']]
        else:
            maps=[np.array(r)+1j*np.array(i) for r,i in zip(old['maps_real'],old['maps_imag'])]
            if not iscomplex:maps=[m.real for m in maps]
    else:
        maps=[rng.normal(size=(target.shape[k],ss[k]))/ss[k]**0.5 for k in range(3)]
        if iscomplex:maps=[(m+1j*rng.normal(size=m.shape)/ss[k]**0.5)/2**0.5 for k,m in enumerate(maps)]
    norm=np.linalg.norm(target);hist=[];best=float('inf');start=time.monotonic()
    def full(ms):return np.einsum('is,jt,ku,stu->ijk',*ms,source,optimize=True)
    gauge_max=0.0
    for step in range(iterations+1):
        if step%100==0 or step==iterations:
            error_tensor=full(maps)-target;error=float(np.linalg.norm(error_tensor)/norm)
            row={'iteration':step,'relative_coefficient_error':error,'maximum_absolute_coefficient_error':float(np.max(np.abs(error_tensor))),
                 'map_norms':[float(np.linalg.norm(m)) for m in maps],'elapsed_seconds':time.monotonic()-start}
            hist.append(row);print(json.dumps({'n':n,'b':b,'seed':seed,'complex':iscomplex,**row}),flush=True)
            if error<best:
                best=error
                checkpoint.write_text(json.dumps({'n':n,'b':b,'defect':defect,'seed':seed,'complex':iscomplex,
                    'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],
                    'relative_coefficient_error':error,'exact_coefficient_certificate':False},indent=2)+'\n')
            if error<1e-13:break
        if step==iterations:break
        for axis in range(3):
            other=[k for k in range(3) if k!=axis]
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],np.transpose(source,(axis,*other)),optimize=True).reshape(ss[axis],-1)
            wanted=np.transpose(target,(axis,*other)).reshape(target.shape[axis],-1)
            gram=env@env.conj().T;gram.flat[::gram.shape[0]+1]+=1e-12
            maps[axis]=np.linalg.lstsq(gram.T,(wanted@env.conj().T).T,rcond=1e-14)[0].T
        if step%10==0:
            # Gauge does not preserve the residual norm away from an exact fit.
            # Verify the exact target is fixed independently, then balance.
            maps=gauge(maps,l,b,l)
    return {'n':n,'b':b,'defect':defect,'seed':seed,'complex':iscomplex,'source_shape':ss,'target_shape':target.shape,
            'auxiliary_repair_rank_upper':repair,'all_target_positions_checked':int(target.size),'parameters':sum(m.size for m in maps),
            'iterations_completed':step,'maximum_iterations':iterations,'history':hist,'best_relative_coefficient_error':best,
            'method':'MM target-gauge balanced ordinary ALS','construction_supplied':False,'exact_coefficient_certificate':False,'improves_omega':False}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=5);p.add_argument('--b',type=int,default=4);p.add_argument('--defect',type=int,default=1)
 p.add_argument('--seed',type=int,default=0);p.add_argument('--iterations',type=int,default=3000);p.add_argument('--complex',action='store_true')
 p.add_argument('--initial',type=Path);p.add_argument('--checkpoint',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
 a=p.parse_args();res=fit(a.n,a.b,a.defect,a.seed,a.iterations,a.complex,a.checkpoint,a.initial)
 a.output.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='history'},indent=2))
