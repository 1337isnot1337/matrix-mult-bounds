"""Bounded Q64 search with first-map rowspace divisible by u-v.

This tests a stated ansatz, not arbitrary first-leg maps.  Scalar
columns, when requested, remain explicit and unrestricted on that leg.
"""
import argparse
import json
from pathlib import Path
import time
import numpy as np
from narrow_rectangle_balanced import boundary, gauge


def fit(auxiliary_rank, seed, iterations, checkpoint):
    n,b,l=6,4,5
    base_shape,st,_,_=boundary.base.coordinates(n,b)
    ss=[d+auxiliary_rank for d in base_shape]
    source=np.zeros(ss)
    for pt in st:
        source[pt]+=1
    for j in range(auxiliary_rank):
        source[tuple(d+j for d in base_shape)]=1
    target,_,_=boundary.target_data(n,b,'rectangle',1)
    projection=np.zeros((25+auxiliary_rank,36+auxiliary_rank))
    for i in range(5):
        for k in range(5):
            projection[5*i+k,6*(i+1)+k]=1
            projection[5*i+k,6*i+k+1]=-1
    for j in range(auxiliary_rank):
        projection[25+j,36+j]=1
    u,s,vh=np.linalg.svd(projection,full_matrices=False)
    assert min(s)>1e-8
    projection=vh
    rng=np.random.default_rng(seed)
    aa=(rng.normal(size=(25,25+auxiliary_rank))+1j*rng.normal(size=(25,25+auxiliary_rank)))/(2*(25+auxiliary_rank))**0.5
    maps=[aa@projection]+[(rng.normal(size=(target.shape[k],ss[k]))+1j*rng.normal(size=(target.shape[k],ss[k])))/(2*ss[k])**0.5 for k in [1,2]]
    norm=np.linalg.norm(target)
    history=[]
    best=float('inf')
    start=time.monotonic()
    for step in range(iterations+1):
        if step%100==0 or step==iterations:
            diff=np.einsum('is,jt,ku,stu->ijk',*maps,source,optimize=True)-target
            error=float(np.linalg.norm(diff)/norm)
            row={'iteration':step,'relative_coefficient_error':error,'maximum_absolute_coefficient_error':float(np.max(np.abs(diff))),
                 'map_norms':[float(np.linalg.norm(m)) for m in maps],
                 'map_smallest_singular_values':[float(np.linalg.svd(m,compute_uv=False)[-1]) for m in maps],
                 'first_rowspace_residual':float(np.linalg.norm(maps[0]-maps[0]@projection.conj().T@projection)),
                 'elapsed_seconds':time.monotonic()-start}
            history.append(row)
            print(json.dumps({'auxiliary_rank':auxiliary_rank,'seed':seed,**row}),flush=True)
            if error<best:
                best=error
                checkpoint.write_text(json.dumps({'n':n,'b':b,'target_outer':l,'seed':seed,'first_space':'(u-v) P4(u) tensor P4(v)',
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
            if axis==0:
                env=projection@env
            gram=env@env.conj().T
            gram.flat[::gram.shape[0]+1]+=1e-12
            coefficient=np.linalg.lstsq(gram.T,(wanted@env.conj().T).T,rcond=1e-14)[0].T
            maps[axis]=coefficient@projection if axis==0 else coefficient
        if step%10==0:
            maps=gauge(maps,l,b,l)
    return {'n':n,'b':b,'target_outer':l,'source':'Q(6,4) direct sum D_r',
            'auxiliary_rank':auxiliary_rank,'source_shape':ss,'target_shape':list(target.shape),
            'first_map_source_rowspace':'{(u-v)Y(u,v): degree_u Y, degree_v Y <=4} plus scalar coordinates',
            'seed':seed,'iterations_completed':step,'maximum_iterations':iterations,
            'best_relative_coefficient_error':best,'history':history,'all_target_positions_checked':10000,
            'method':'Complex ordinary-map ALS constrained to the stated first-leg source subspace',
            'ansatz_restriction':True,'exact_coefficient_certificate':False,
            'fixed_width_all_n_family_proved':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--auxiliary-rank',type=int,default=0)
    parser.add_argument('--seed',type=int,required=True)
    parser.add_argument('--iterations',type=int,default=3000)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=fit(args.auxiliary_rank,args.seed,args.iterations,args.checkpoint)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='history'},indent=2))
