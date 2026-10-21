"""Bounded ordinary-map search from Q(6,4) plus explicit scalar summands.

The auxiliary source is D_r, a direct sum of r rank-one tensors.  No
fit is a certificate until every coefficient has been checked exactly.
"""
import argparse
import json
from pathlib import Path
import time
import numpy as np
from narrow_rectangle_balanced import boundary, gauge


def full(maps, source):
    return np.einsum('is,jt,ku,stu->ijk',*maps,source,optimize=True)


def rank_one_seed(tensor, rng):
    best=None
    best_error=float('inf')
    for attempt in range(6):
        vectors=[rng.normal(size=d)+1j*rng.normal(size=d) for d in tensor.shape]
        vectors=[v/np.linalg.norm(v) for v in vectors]
        for step in range(40):
            for axis in range(3):
                other=[k for k in range(3) if k!=axis]
                env=np.einsum('ijk,j,k->i',np.transpose(tensor,(axis,*other)),vectors[other[0]].conj(),vectors[other[1]].conj(),optimize=True)
                norm=np.linalg.norm(env)
                if norm>1e-14:
                    vectors[axis]=env/norm
        tensor_unit=np.einsum('i,j,k->ijk',*vectors)
        weight=np.vdot(tensor_unit,tensor)
        vectors[0]=vectors[0]*weight
        error=np.linalg.norm(tensor-np.einsum('i,j,k->ijk',*vectors))
        if error<best_error:
            best_error=error
            best=[v.copy() for v in vectors]
    norms=[np.linalg.norm(v) for v in best]
    common=np.prod(norms)**(1/3)
    return [v*common/norm for v,norm in zip(best,norms)]


def fit(auxiliary_rank, seed, iterations, checkpoint, initial=None):
    n,b,l=6,4,5
    base_shape,st,_,_=boundary.base.coordinates(n,b)
    ss=[d+auxiliary_rank for d in base_shape]
    source=np.zeros(ss)
    for pt in st:
        source[pt]+=1
    for j in range(auxiliary_rank):
        source[tuple(d+j for d in base_shape)]=1
    target,_,_=boundary.target_data(n,b,'rectangle',1)
    rng=np.random.default_rng(seed)
    if initial:
        point=json.loads(initial.read_text())
        base=[np.array(r)+1j*np.array(i) for r,i in zip(point['maps_real'],point['maps_imag'])]
        maps=[np.pad(m,((0,0),(0,auxiliary_rank))) for m in base]
        remaining=target-full(maps,source)
        for j in range(auxiliary_rank):
            vectors=rank_one_seed(remaining,rng)
            for axis in range(3):
                maps[axis][:,base_shape[axis]+j]=vectors[axis]
            remaining-=np.einsum('i,j,k->ijk',*vectors)
        maps=[m+0.03*(rng.normal(size=m.shape)+1j*rng.normal(size=m.shape))/2**0.5 for m in maps]
    else:
        maps=[(rng.normal(size=(target.shape[k],ss[k]))+1j*rng.normal(size=(target.shape[k],ss[k])))/(2*ss[k])**0.5 for k in range(3)]
    norm=np.linalg.norm(target)
    history=[]
    best=float('inf')
    start=time.monotonic()
    for step in range(iterations+1):
        if step%100==0 or step==iterations:
            diff=full(maps,source)-target
            error=float(np.linalg.norm(diff)/norm)
            row={'iteration':step,'relative_coefficient_error':error,'maximum_absolute_coefficient_error':float(np.max(np.abs(diff))),
                 'map_norms':[float(np.linalg.norm(m)) for m in maps],
                 'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
                 'elapsed_seconds':time.monotonic()-start}
            history.append(row)
            print(json.dumps({'auxiliary_rank':auxiliary_rank,'seed':seed,**row}),flush=True)
            if error<best:
                best=error
                checkpoint.write_text(json.dumps({'n':n,'b':b,'target_outer':l,'seed':seed,
                    'auxiliary_source':'D_r','auxiliary_rank':auxiliary_rank,'source_shape':ss,
                    'maps_real':[m.real.tolist() for m in maps],'maps_imag':[m.imag.tolist() for m in maps],
                    'relative_coefficient_error':error,'exact_coefficient_certificate':False},indent=2)+'\n')
            if error<1e-12:
                break
        if step==iterations:
            break
        for axis in range(3):
            other=[k for k in range(3) if k!=axis]
            env=np.einsum('jt,ku,stu->sjk',maps[other[0]],maps[other[1]],np.transpose(source,(axis,*other)),optimize=True).reshape(ss[axis],-1)
            wanted=np.transpose(target,(axis,*other)).reshape(target.shape[axis],-1)
            gram=env@env.conj().T
            gram.flat[::gram.shape[0]+1]+=1e-12
            maps[axis]=np.linalg.lstsq(gram.T,(wanted@env.conj().T).T,rcond=1e-14)[0].T
        if step%10==0:
            maps=gauge(maps,l,b,l)
            for j in range(auxiliary_rank):
                norms=[np.linalg.norm(m[:,base_shape[k]+j]) for k,m in enumerate(maps)]
                if min(norms)>1e-14:
                    common=np.prod(norms)**(1/3)
                    for k in range(3):
                        maps[k][:,base_shape[k]+j]*=common/norms[k]
    return {'n':n,'b':b,'target_outer':l,'source':'Q(6,4) direct sum D_r',
            'auxiliary_rank':auxiliary_rank,'source_shape':ss,'target_shape':list(target.shape),
            'seed':seed,'iterations_completed':step,'maximum_iterations':iterations,
            'initial':str(initial) if initial else 'random',
            'best_relative_coefficient_error':best,'history':history,'all_target_positions_checked':10000,
            'method':'Complex ordinary-map ALS, with explicit scalar columns and exact MM target-gauge balancing',
            'parameters':sum(m.size for m in maps),'exact_coefficient_certificate':False,
            'fixed_width_all_n_family_proved':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--auxiliary-rank',type=int,required=True)
    parser.add_argument('--seed',type=int,required=True)
    parser.add_argument('--iterations',type=int,default=3000)
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=fit(args.auxiliary_rank,args.seed,args.iterations,args.checkpoint,args.initial)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='history'},indent=2))
