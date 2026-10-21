"""Monomial Laurent-map discovery in the M4-to-M5 output grading.

Rows have powers A_ik=-[i=4]-[k=4], B_ij=[i=4], C_jk=[k=4].
Every negative-power coefficient must vanish; the whole constant
coefficient must be M(5,4,5). Positive powers are explicitly permitted.
Numerical residuals are never accepted as exact identities.
"""
import argparse
import json
from pathlib import Path
import time
import numpy as np
from narrow_rectangle_balanced import boundary, apply_axis, covariance, positive_power


def block_balance(left, la, right, ra, blocks):
    g=covariance(left,la)
    h=covariance(right,ra).conj()
    transform=np.zeros_like(g)
    start=0
    for width in blocks:
        idx=slice(start,start+width)
        gg,hh=g[idx,idx],h[idx,idx]
        gh=positive_power(gg,0.5)
        gm=positive_power(gg,-0.5)
        scale=gm@positive_power(gh@hh@gh,0.5)@gm
        transform[idx,idx]=positive_power(scale,0.5)
        start+=width
    return apply_axis(transform,left,la),apply_axis(np.linalg.inv(transform).T,right,ra)


def weighted_gauge(maps):
    a=maps[0].reshape(5,5,-1)
    b=maps[1].reshape(5,4,-1)
    c=maps[2].reshape(4,5,-1)
    a,b=block_balance(a,0,b,0,[4,1])
    b,c=block_balance(b,1,c,0,[4])
    a,c=block_balance(a,1,c,1,[4,1])
    return [array.reshape(matrix.shape) for array,matrix in zip([a,b,c],maps)]


def fit(seed, iterations, auxiliary_rank, checkpoint, initial=None):
    base_shape,source_terms,_,_=boundary.base.coordinates(6,4)
    ss=[d+auxiliary_rank for d in base_shape]
    source=np.zeros(ss)
    for point in source_terms:
        source[point]+=1
    for j in range(auxiliary_rank):
        source[tuple(d+j for d in base_shape)]=1
    target,_,_=boundary.target_data(6,4,'rectangle',1)
    weights=[np.array([-int(i==4)-int(k==4) for i in range(5) for k in range(5)]),
             np.array([int(i==4) for i in range(5) for j in range(4)]),
             np.array([int(k==4) for j in range(4) for k in range(5)])]
    degree=weights[0][:,None,None]+weights[1][None,:,None]+weights[2][None,None,:]
    mask=degree<=0
    assert np.count_nonzero(mask)==7568
    assert not np.any(target[degree!=0])
    rng=np.random.default_rng(seed)
    if initial:
        old=json.loads(initial.read_text())
        maps=[np.array(r)+1j*np.array(i) for r,i in zip(old['maps_real'],old['maps_imag'])]
        maps=[np.pad(m,((0,0),(0,auxiliary_rank))) for m in maps]
        maps=[m+0.2*(rng.normal(size=m.shape)+1j*rng.normal(size=m.shape))/2**0.5 for m in maps]
    else:
        maps=[(rng.normal(size=(target.shape[k],ss[k]))+1j*rng.normal(size=(target.shape[k],ss[k])))/(2*ss[k])**0.5 for k in range(3)]
    norm=np.linalg.norm(target)
    history=[]
    best=float('inf')
    start=time.monotonic()
    for step in range(iterations+1):
        if step%100==0 or step==iterations:
            actual=np.einsum('is,jt,ku,stu->ijk',*maps,source,optimize=True)
            diff=actual-target
            error=float(np.linalg.norm(diff[mask])/norm)
            row={'iteration':step,'relative_nonpositive_coefficient_error':error,
                 'maximum_nonpositive_coefficient_error':float(np.max(np.abs(diff[mask]))),
                 'negative_degree_coefficient_norms':{str(p):float(np.linalg.norm(actual[degree==p])) for p in [-2,-1]},
                 'constant_coefficient_error_norm':float(np.linalg.norm(diff[degree==0])),
                 'positive_degree_coefficient_norm':float(np.linalg.norm(actual[degree>0])),
                 'map_norms':[float(np.linalg.norm(m)) for m in maps],
                 'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
                 'elapsed_seconds':time.monotonic()-start}
            history.append(row)
            print(json.dumps({'seed':seed,'auxiliary_rank':auxiliary_rank,**row}),flush=True)
            if error<best:
                best=error
                checkpoint.write_text(json.dumps({'n':6,'b':4,'target_outer':5,'seed':seed,'auxiliary_rank':auxiliary_rank,
                    'source_shape':ss,'map_row_powers':[w.tolist() for w in weights],
                    'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],
                    'relative_nonpositive_coefficient_error':error,'exact_coefficient_certificate':False},indent=2)+'\n')
            if error<1e-12:
                break
        if step==iterations:
            break
        for axis in range(3):
            other=[k for k in range(3) if k!=axis]
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],np.transpose(source,(axis,*other)),optimize=True).reshape(ss[axis],-1)
            wanted=np.transpose(target,(axis,*other)).reshape(target.shape[axis],-1)
            other_degree=(weights[other[0]][:,None]+weights[other[1]][None,:]).ravel()
            for weight in np.unique(weights[axis]):
                rows=np.flatnonzero(weights[axis]==weight)
                columns=other_degree+weight<=0
                restricted=env[:,columns]
                gram=restricted@restricted.conj().T
                gram.flat[::gram.shape[0]+1]+=1e-12
                maps[axis][rows]=np.linalg.lstsq(gram.T,(wanted[rows][:,columns]@restricted.conj().T).T,rcond=1e-14)[0].T
        if step%10==0:
            maps=weighted_gauge(maps)
    return {'source':'Q(6,4) direct sum D_r','target':'M(5,4,5)',
            'auxiliary_rank':auxiliary_rank,'seed':seed,'iterations_completed':step,'maximum_iterations':iterations,
            'map_row_powers':[w.tolist() for w in weights],
            'coefficient_position_counts_by_degree':{str(p):int(np.count_nonzero(degree==p)) for p in range(-2,3)},
            'all_nonpositive_positions_checked':int(np.count_nonzero(mask)),'all_target_positions_accounted':10000,
            'best_relative_nonpositive_coefficient_error':best,'history':history,
            'method':'Complex masked ALS with target row Laurent powers and weight-preserving block gauge',
            'exact_coefficient_certificate':False,'degeneration_proved':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,required=True)
    parser.add_argument('--iterations',type=int,default=3000)
    parser.add_argument('--auxiliary-rank',type=int,default=0)
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=fit(args.seed,args.iterations,args.auxiliary_rank,args.checkpoint,args.initial)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='history'},indent=2))
