"""Bounded optional Q64 discovery using a complete target operator flag.

No floating-point residual is an exact degeneration certificate.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import sys
import time
import numpy as np

from q64_weighted_laurent import block_balance


def setup(grading):
    alpha=np.arange(5)*20
    beta=np.arange(4)*5
    gamma=np.arange(5)
    if grading=='refined':
        alpha[-1]+=1000
        gamma[-1]+=1000
    elif grading!='lexicographic':
        raise ValueError('Unknown grading')
    weights=[(-alpha[:,None]-gamma[None,:]).ravel(),
             (alpha[:,None]-beta[None,:]).ravel(),
             (beta[:,None]+gamma[None,:]).ravel()]
    target=np.zeros((25,20,20))
    for i,j,k in product(range(5),range(4),range(5)):
        target[5*i+k,4*i+j,5*j+k]=1
    degrees=weights[0][:,None,None]+weights[1][None,:,None]+weights[2][None,None,:]
    assert np.count_nonzero(degrees<=0)==5050
    assert np.count_nonzero(degrees==0)==100
    assert not np.any(target[degrees!=0])
    return weights,target,degrees


def gauge(maps):
    a=maps[0].reshape(5,5,-1)
    b=maps[1].reshape(5,4,-1)
    c=maps[2].reshape(4,5,-1)
    for _ in range(2):
        a,b=block_balance(a,0,b,0,[1]*5)
        b,c=block_balance(b,1,c,0,[1]*4)
        a,c=block_balance(a,1,c,1,[1]*5)
    return [x.reshape(old.shape) for x,old in zip([a,b,c],maps)]


def mode_balance(maps):
    norms=np.array([np.linalg.norm(m) for m in maps])
    common=float(np.exp(np.mean(np.log(norms))))
    return [m*(common/norm) for m,norm in zip(maps,norms)]


def bounded_step(grams,cross,budget):
    vals,vecs=np.linalg.eigh((grams+grams.conj().transpose(0,2,1))/2)
    vals=np.maximum(vals,0)
    coefficients=np.einsum('ri,rij->rj',cross,vecs)
    coefficients=np.where(vals>1e-14*np.maximum(vals[:,-1:],1e-30),coefficients,0)
    def normsq(ridge):
        return float(np.sum(np.abs(coefficients/(vals+ridge))**2))
    lo=1e-12
    if normsq(lo)>budget**2:
        hi=max(lo,float(np.linalg.norm(coefficients)/budget))
        for _ in range(50):
            mid=(lo+hi)/2
            if normsq(mid)>budget**2:
                lo=mid
            else:
                hi=mid
        ridge=hi
    else:
        ridge=lo
    solved=np.einsum('rj,rij->ri',coefficients/(vals+ridge),vecs.conj())
    return solved,float(ridge)


def fit(grading,seed,iterations,initial,checkpoint,norm_budget=None,gauge_kind='diagonal'):
    weights,target,degree=setup(grading)
    source=np.zeros((36,36,36))
    for p,q,y,v in product(range(6),range(6),range(4),range(4)):
        source[6*p+q,9*y+q+v,4*(p+y)+v]=1
    rng=np.random.default_rng(seed)
    if initial:
        point=json.loads(initial.read_text())
        if point.get('auxiliary_rank',0):
            raise ValueError('This search keeps auxiliary rank zero.')
        maps=[np.array(r)+1j*np.array(i) for r,i in zip(point['maps_real'],point['maps_imag'])]
    else:
        maps=[(rng.normal(size=(r,36))+1j*rng.normal(size=(r,36)))/np.sqrt(72) for r in [25,20,20]]
    if norm_budget:
        maps=mode_balance(maps)
        maps=[m*min(1,norm_budget/np.linalg.norm(m)) for m in maps]
    if gauge_kind=='parabolic':
        from q64_parabolic_gauge import gauge as target_gauge
    elif gauge_kind=='diagonal':
        target_gauge=gauge
    else:
        raise ValueError('Unknown gauge kind')
    layouts=[]
    for axis in range(3):
        other=[k for k in range(3) if k!=axis]
        other_degree=(weights[other[0]][:,None]+weights[other[1]][None,:]).ravel()
        order=np.argsort(other_degree,kind='stable')
        count=np.searchsorted(other_degree[order],-weights[axis],side='right')
        wanted=np.transpose(target,(axis,*other)).reshape(target.shape[axis],-1)[:,order]
        layouts.append((other,order,count,wanted,np.transpose(source,(axis,*other))))
    mask=degree<=0
    history=[]; best=float('inf'); started=time.monotonic(); ridges=[None]*3
    for step in range(iterations+1):
        if step%50==0 or step==iterations:
            actual=np.einsum('is,jt,ku,stu->ijk',*maps,source,optimize=True)
            err=actual-target
            residual=float(np.linalg.norm(err[mask])/10)
            record={'iteration':step,'relative_nonpositive_coefficient_error':residual,
                    'maximum_nonpositive_error':float(np.max(np.abs(err[mask]))),
                    'negative_coefficient_norm':float(np.linalg.norm(actual[degree<0])),
                    'constant_coefficient_error_norm':float(np.linalg.norm(err[degree==0])),
                    'positive_coefficient_norm':float(np.linalg.norm(actual[degree>0])),
                    'map_norms':[float(np.linalg.norm(m)) for m in maps],
                    'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
                    'norm_budget':norm_budget,'ridge_parameters':ridges,
                    'elapsed_seconds':time.monotonic()-started}
            history.append(record)
            print(json.dumps(record),flush=True)
            if residual<best:
                best=residual
                checkpoint.write_text(json.dumps({'n':6,'b':4,'target_outer':5,'auxiliary_rank':0,
                    'grading':grading,'seed':seed,'iteration':step,'norm_budget':norm_budget,'target_gauge':gauge_kind,
                    'map_row_powers':[w.tolist() for w in weights],
                    'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],
                    'relative_nonpositive_coefficient_error':residual,'exact_coefficient_certificate':False},separators=(',',':'))+'\n')
            if residual<1e-12 or not np.isfinite(residual) or max(record['map_norms'])>1000:
                break
        if step==iterations:
            break
        for axis,(other,order,count,wanted,st) in enumerate(layouts):
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],st,optimize=True).reshape(36,-1)[:,order]
            grams=np.cumsum(np.einsum('ik,jk->kij',env,env.conj()),axis=0)
            if norm_budget:
                cross=wanted @ env.conj().T
                maps[axis],ridges[axis]=bounded_step(grams[count-1],cross,norm_budget)
            else:
                for row,columns in enumerate(count):
                    gram=grams[columns-1].copy()
                    gram.flat[::37]+=1e-12
                    cross=wanted[row,:columns] @ env[:,:columns].conj().T
                    maps[axis][row]=np.linalg.lstsq(gram.T,cross,rcond=1e-14)[0]
        if step%10==0:
            maps=target_gauge(maps)
        if norm_budget:
            maps=mode_balance(maps)
    return {'source':'Q(6,4)','target':'M(5,4,5)','auxiliary_rank':0,'grading':grading,
            'seed':seed,'norm_budget':norm_budget,'target_gauge':gauge_kind,'maximum_iterations':iterations,'iterations_completed':step,
            'history':history,'best_relative_nonpositive_coefficient_error':best,
            'coefficient_counts':{'negative':4950,'constant':100,'positive':4950},
            'exact_coefficient_certificate':False,'degeneration_proved':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--grading',choices=['refined','lexicographic'],required=True)
    parser.add_argument('--seed',type=int,required=True)
    parser.add_argument('--iterations',type=int,default=1500)
    parser.add_argument('--norm-budget',type=float)
    parser.add_argument('--gauge',choices=['diagonal','parabolic'],default='diagonal')
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=fit(args.grading,args.seed,args.iterations,args.initial,args.checkpoint,args.norm_budget,args.gauge)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key!='history'},indent=2))
