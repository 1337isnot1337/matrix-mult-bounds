"""Unrestricted constant-map discovery for cyclic convolutions.

This optional NumPy experiment allows mixing different source torus weights.
Every reported objective is recomputed on the complete target tensor.
Floating residuals are never accepted as algebraic certificates.
"""
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from singular_support import support_points, exact_monomial_control


class DenseProblem:
    def __init__(self,a,b,shape=None,source_mode='full',direct_sum=None,scaling=None):
        self.a,self.b=a,b
        self.shape=tuple(shape) if shape is not None else None
        self.source_mode=source_mode
        self.direct_sum=tuple(direct_sum) if direct_sum is not None else None
        if (self.shape is None)==(self.direct_sum is None):
            raise ValueError('Choose one matrix shape or a direct sum of square sizes')
        if self.shape is not None:
            l,h,n=self.shape
            self.target_dims=(l*h,h*n,n*l)
        else:
            d=sum(n*n for n in self.direct_sum)
            self.target_dims=(d,d,d)
        self.dimension=a*b*(a+b-1)
        points=support_points(a,b,source_mode)
        if len(points)!=len(set(points)):
            raise ArithmeticError("Duplicate source coordinates")
        self.points=points
        self.scaling=scaling
        if scaling is not None:
            if any(np.shape(s)!=(self.dimension,) for s in scaling):
                raise ValueError('Source diagonal scaling has an incorrect dimension')
            if any(not np.all(np.isfinite(s)) or np.any(s==0) for s in scaling):
                raise ValueError('Source diagonal scaling must be finite and invertible')
        self.groups=[]
        self.group_coefficients=[]
        for axis in range(3):
            other=[i for i in range(3) if i!=axis]
            groups=[[] for _ in range(self.dimension)]
            coefficients=[[] for _ in range(self.dimension)]
            for p in points:
                groups[p[axis]].append((p[other[0]],p[other[1]]))
                if scaling is not None:
                    coefficients[p[axis]].append(np.prod([scaling[j][p[j]] for j in range(3)]))
            self.groups.append([np.array(g,dtype=np.int64).reshape(-1,2) for g in groups])
            self.group_coefficients.append([np.array(c) for c in coefficients])
        self.target=np.zeros(self.target_dims)
        if self.shape is not None:
            for i,j,k in product(range(l),range(h),range(n)):
                self.target[i*h+j,j*n+k,k*l+i]=1
            self.norm=np.sqrt(l*h*n)
        else:
            offset=0
            for n in self.direct_sum:
                for i,j,k in product(range(n),repeat=3):
                    self.target[offset+i*n+j,offset+j*n+k,offset+k*n+i]=1
                offset+=n*n
            self.norm=np.sqrt(sum(n**3 for n in self.direct_sum))
        self.target_nonzero=[]
        for axis in range(3):
            flat=np.moveaxis(self.target,axis,0).reshape(self.target_dims[axis],-1)
            self.target_nonzero.append([np.flatnonzero(row) for row in flat])

    def contraction(self,maps,axis):
        other=[i for i in range(3) if i!=axis]
        left,right=maps[other[0]],maps[other[1]]
        result=np.empty((self.dimension,left.shape[0],right.shape[0]),dtype=np.result_type(left,right))
        for x,pairs in enumerate(self.groups[axis]):
            l=left[:,pairs[:,0]]
            if self.scaling is not None:
                l=l*self.group_coefficients[axis][x]
            result[x]=l@right[:,pairs[:,1]].T
        return result.reshape(self.dimension,-1)

    def update(self,maps,axis):
        matrix=self.contraction(maps,axis)
        gram=matrix@matrix.conj().T
        values,vectors=np.linalg.eigh(gram)
        cutoff=max(float(values[-1]),1.)*1e-12
        selected=values>cutoff
        inverse=(vectors[:,selected]/values[selected])@vectors[:,selected].conj().T
        cross=np.stack([matrix[:,indices].conj().sum(axis=1)
                        for indices in self.target_nonzero[axis]])
        maps[axis]=cross@inverse

    def residual(self,maps):
        actual=(maps[0]@self.contraction(maps,0)).reshape(self.target_dims)
        return float(np.linalg.norm(actual-self.target)/self.norm)

    def normalize(self,maps):
        norms=np.array([np.linalg.norm(m) for m in maps])
        if min(norms)<=0:
            raise ArithmeticError("An iterate collapsed an entire map")
        scale=np.exp(np.mean(np.log(norms)))
        for m,norm in zip(maps,norms):
            m*=scale/norm

    def random_maps(self,seed,complex_maps):
        rng=np.random.default_rng(seed)
        maps=[]
        for d in self.target_dims:
            m=rng.normal(size=(d,self.dimension))
            if complex_maps:
                m=(m+1j*rng.normal(size=m.shape))/np.sqrt(2)
            maps.append(m/np.sqrt(self.dimension))
        return maps


def control():
    problem=DenseProblem(2,2,(2,3,4))
    path=Path(__file__).resolve().parents[3]/'results/cyclic-mixed-map-2026-10-20/witness.json'
    witness=json.loads(path.read_text())
    maps=[np.zeros((d,12)) for d in problem.target_dims]
    for m,name in zip(maps,'ABC'):
        for i,j,v in witness['maps'][name]:
            m[i,j]=int(v)
    if problem.residual(maps)!=0:
        raise ArithmeticError("The integer positive control did not replay")
    before=[m.copy() for m in maps]
    for axis in range(3):
        problem.update(maps,axis)
    if problem.residual(maps)>1e-10:
        raise ArithmeticError("An exact-control least-squares sweep increased the error")
    result={'integer_control_full_relative_error':0.,
            'after_one_sweep_error':problem.residual(maps)}
    parity=DenseProblem(2,2,(2,2,2),source_mode='parity110')
    witness=exact_monomial_control(2,2)
    parity_maps=[np.eye(12)[p] for p in witness['source_coordinates_per_target_leg']]
    if parity.residual(parity_maps)!=0:
        raise ArithmeticError('The parity source integer control did not replay')
    direct=DenseProblem(2,2,source_mode='parity110',direct_sum=(2,))
    if direct.residual(parity_maps)!=0:
        raise ArithmeticError('The direct-sum target control did not replay')
    result['parity110_control_full_relative_error']=0.
    result['single_block_direct_sum_control_full_relative_error']=0.
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--starts',type=int,default=2)
    parser.add_argument('--iterations',type=int,default=60)
    parser.add_argument('--seed',type=int,default=2026102400)
    parser.add_argument('--complex',action='store_true')
    parser.add_argument('--a',type=int,default=4)
    parser.add_argument('--b',type=int,default=5)
    parser.add_argument('--source-mode',choices=('full','step','parity000','parity110'),default='full')
    targets=parser.add_mutually_exclusive_group()
    targets.add_argument('--shape',type=int,nargs=3)
    targets.add_argument('--direct-sum',type=int,nargs='+')
    parser.add_argument('--scaling',type=Path,
                        help='NPZ with invertible source diagonal factors A, B, C')
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--noise',type=float,default=0.1)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    controls=control()
    scaling_file=np.load(args.scaling) if args.scaling else None
    scaling=[scaling_file[name] for name in 'ABC'] if scaling_file is not None else None
    shape=None if args.direct_sum else (args.shape or (12,12,13))
    problem=DenseProblem(args.a,args.b,shape,source_mode=args.source_mode,
                         direct_sum=args.direct_sum,scaling=scaling)
    best=float('inf');records=[];start=time.monotonic()
    initial=np.load(args.initial) if args.initial else None
    for trial in range(args.starts):
        seed=args.seed+trial
        maps=problem.random_maps(seed,args.complex)
        if initial is not None:
            maps=[initial[name]+args.noise*m for name,m in zip('ABC',maps)]
        trajectory=[]
        for step in range(args.iterations):
            for axis in range(3):
                problem.update(maps,axis)
            problem.normalize(maps)
            if step%5==0 or step+1==args.iterations:
                error=problem.residual(maps)
                trajectory.append([step+1,error])
                print('trial',trial,'iteration',step+1,'full_relative_error',error,
                      'seconds',time.monotonic()-start,flush=True)
                if error<best:
                    best=error
                    np.savez_compressed(args.output/'best.npz',A=maps[0],B=maps[1],C=maps[2],
                                        error=error,seed=seed,iteration=step+1)
                if error<1e-10:
                    break
        records.append({'seed':seed,'iterations':step+1,'full_relative_error':error,
                        'trajectory':trajectory,'map_norms':[float(np.linalg.norm(m)) for m in maps]})
        report={'source_lengths':[args.a,args.b],'source_mode':args.source_mode,
                'source_nonzero_coefficients':len(problem.points),
                'source_diagonal_scaling':str(args.scaling) if args.scaling else None,
                'source_scaling_sha256':hashlib.sha256(args.scaling.read_bytes()).hexdigest() if args.scaling else None,
                'target_shape':list(shape) if shape else None,
                'target_direct_sum_sizes':args.direct_sum,
                'map_class':'arbitrary dense constant maps; no weight restriction',
                'complex_maps':args.complex,'maximum_iterations':args.iterations,
                'starts_completed':len(records),'records':records,
                'initial_array':str(args.initial) if args.initial else None,
                'initial_sha256':hashlib.sha256(args.initial.read_bytes()).hexdigest() if args.initial else None,
                'initial_noise':args.noise if args.initial else None,
                'control':controls,'best_full_relative_error':best,
                'full_coefficient_count':int(np.prod(problem.target_dims)),
                'exact_witness_found':False,'exclusion_proved':False,
                'new_exponent_established':False}
        (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
