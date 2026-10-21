"""Numerical projected ALS for avoiding deficient long-leg map components.

The singular-value floor is a search constraint, not an identity or an
obstruction.  Full tensor coefficients are always the acceptance test.
"""
import argparse
import json
from pathlib import Path
import time
import numpy as np
from narrow_rectangle_balanced import boundary, gauge


def fit(seed, iterations, floor, checkpoint, initial=None):
    n, b, l = 6, 4, 5
    ss, st, _, _ = boundary.base.coordinates(n, b)
    source = np.zeros(ss)
    for pt in st:
        source[pt] += 1
    target, _, _ = boundary.target_data(n,b,'rectangle',1)
    rng = np.random.default_rng(seed)
    if initial:
        point = json.loads(initial.read_text())
        maps = [np.array(r)+1j*np.array(i) for r,i in zip(point['maps_real'],point['maps_imag'])]
        maps = [m+0.05*(rng.normal(size=m.shape)+1j*rng.normal(size=m.shape))/2**0.5 for m in maps]
    else:
        maps = [(rng.normal(size=(target.shape[k],ss[k]))+1j*rng.normal(size=(target.shape[k],ss[k])))/(2*ss[k])**0.5 for k in range(3)]
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
                 'elapsed_seconds':time.monotonic()-start}
            history.append(row)
            print(json.dumps({'seed':seed,'floor':floor,**row}),flush=True)
            if error<best:
                best=error
                checkpoint.write_text(json.dumps({'n':n,'b':b,'defect':1,'seed':seed,'floor':floor,
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
            if axis in (1,2):
                u,s,vh=np.linalg.svd(maps[axis],full_matrices=False)
                maps[axis]=(u*np.maximum(s,floor))@vh
        if step%10==0:
            maps=gauge(maps,l,b,l)
    return {'n':n,'b':b,'target_outer':l,'seed':seed,'iterations_completed':step,
            'long_leg_singular_value_floor':floor,'initial':str(initial) if initial else 'random',
            'best_relative_coefficient_error':best,'history':history,'all_target_positions_checked':10000,
            'method':'Complex ALS with singular-value projection after each long-leg update and MM target-gauge balancing',
            'projection_is_search_heuristic':True,'exact_coefficient_certificate':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,required=True)
    parser.add_argument('--iterations',type=int,default=3000)
    parser.add_argument('--floor',type=float,default=0.1)
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--checkpoint',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=fit(args.seed,args.iterations,args.floor,args.checkpoint,args.initial)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='history'},indent=2))
