"""Full A(5,5) dense-map search from the exact integral M9 core.

The M14-only target is a construction seed, not an exponent-improving
target by itself. Noise is added before the optional source scaling.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from dense_als import DenseProblem


def seeded_maps(problem,core,seed,noise,complex_maps):
    n=problem.shape[0]
    if problem.shape!=(n,n,n) or n<9:
        raise ValueError('The integral M9 seed needs a square target of size at least9')
    maps=problem.random_maps(seed,complex_maps)
    for matrix,name in zip(maps,'ABC'):
        matrix*=noise
        for i in range(9):
            for j in range(9):
                matrix[n*i+j]+=core[name][9*i+j]
    if problem.scaling is not None:
        for matrix,scaling in zip(maps,problem.scaling):
            matrix/=scaling[None,:]
    return maps


def apply_singular_floor(problem,maps,axis,floor):
    """Exploratory rank regularization in original source coordinates."""
    if floor<=0:
        return
    scale=problem.scaling[axis] if problem.scaling is not None else np.ones(problem.dimension)
    original=maps[axis]*scale[None,:]
    u,s,vh=np.linalg.svd(original,full_matrices=False)
    original=(u*np.maximum(s,floor))@vh
    maps[axis]=original/scale[None,:]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n',type=int,default=14)
    parser.add_argument('--noise',type=float,default=.3)
    parser.add_argument('--complex',action='store_true')
    parser.add_argument('--starts',type=int,default=2)
    parser.add_argument('--iterations',type=int,default=60)
    parser.add_argument('--seed',type=int,default=202610214000)
    parser.add_argument('--scaling',type=Path)
    parser.add_argument('--singular-floor',type=float,default=0.)
    parser.add_argument('--floor-final',type=float,default=.015)
    parser.add_argument('--floor-iterations',type=int,default=40)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[3]
    core_path=Path(__file__).with_name('parity_structure_m9_maps.npz')
    core=np.load(core_path)
    scale_file=np.load(args.scaling) if args.scaling else None
    scaling=[scale_file[name] for name in 'ABC'] if scale_file is not None else None
    problem=DenseProblem(5,5,(args.n,)*3,source_mode='full',scaling=scaling)
    args.output.mkdir(parents=True,exist_ok=True)
    zero_noise=seeded_maps(problem,core,0,0.,False)
    core_error=problem.residual(zero_noise)
    expected=(1-(9/args.n)**3)**.5
    if abs(core_error-expected)>1e-12:
        raise ArithmeticError('The embedded integral core failed its complete target residual check')
    del zero_noise
    best=float('inf')
    records=[]
    started=time.monotonic()
    for trial in range(args.starts):
        seed=args.seed+trial
        maps=seeded_maps(problem,core,seed,args.noise,args.complex)
        initial_error=problem.residual(maps)
        trajectory=[]
        for step in range(args.iterations):
            floor=0.
            if args.singular_floor>0 and step<args.floor_iterations:
                floor=args.singular_floor*(args.floor_final/args.singular_floor)**(
                    step/max(1,args.floor_iterations-1))
            for axis in range(3):
                problem.update(maps,axis)
                apply_singular_floor(problem,maps,axis,floor)
            problem.normalize(maps)
            if step==0 or (step+1)%5==0 or step+1==args.iterations:
                error=problem.residual(maps)
                trajectory.append([step+1,error,floor])
                print('trial',trial,'iteration',step+1,'full_relative_error',error,
                      'seconds',time.monotonic()-started,flush=True)
                if error<best:
                    best=error
                    np.savez_compressed(args.output/'best.npz',A=maps[0],B=maps[1],C=maps[2],
                                        error=error,seed=seed,iteration=step+1)
                if error<1e-10:
                    break
        records.append({'seed':seed,'initial_error':initial_error,'iterations':step+1,
                        'trajectory':trajectory,'final_error':problem.residual(maps),
                        'map_norms':[float(np.linalg.norm(m)) for m in maps]})
        result={'source_lengths':[5,5],'source_mode':'full','target_shape':[args.n]*3,
                'source_nonzero_coefficients':len(problem.points),'complex_maps':args.complex,
                'map_class':'arbitrary dense constant maps','core_array':str(core_path.relative_to(root)),
                'core_sha256':hashlib.sha256(core_path.read_bytes()).hexdigest(),
                'core_nonzero_target_coefficients':9**3,'embedded_core_full_relative_error':core_error,
                'initial_noise':args.noise,'noise_convention':'Gaussian perturbation in the original source coordinates, then division by any source diagonal scaling',
                'scaling':str(args.scaling) if args.scaling else None,
                'scaling_sha256':hashlib.sha256(args.scaling.read_bytes()).hexdigest() if args.scaling else None,
                'starts_completed':len(records),'maximum_iterations':args.iterations,'records':records,
                'singular_value_floor':{'initial':args.singular_floor,'final':args.floor_final,
                                        'active_iterations':args.floor_iterations if args.singular_floor else 0,
                                        'metric':'original source coordinates','remaining_iterations':'unregularized ALS'},
                'best_full_relative_error':best,'full_target_coefficient_count':int(np.prod(problem.target_dims)),
                'exact_witness_found':False,'exclusion_proved':False,
                'target_alone_improves_exponent':False,'new_exponent_established':False}
        (args.output/'report.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
