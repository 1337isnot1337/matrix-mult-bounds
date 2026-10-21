"""Small dense-map discovery with damped Gauss--Newton and target gauges.

This is a numerical construction experiment. Its residuals do not certify
tensor identities. Full Jacobians are intended only for small sources.
"""

import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.linalg import cho_factor, cho_solve

from dense_als import DenseProblem
from singular_support import exact_monomial_control


def actual(problem,maps):
    return (maps[0]@problem.contraction(maps,0)).reshape(problem.target_dims)


def jacobian(problem,maps):
    """Complex holomorphic derivative in row-major coordinate-map order."""
    blocks = []
    for axis in range(3):
        contracted = problem.contraction(maps,axis)
        d = problem.target_dims[axis]
        other = [problem.target_dims[i] for i in range(3) if i != axis]
        block = np.kron(np.eye(d),contracted.T)
        block = np.moveaxis(block.reshape(d,*other,d*problem.dimension),0,axis)
        blocks.append(block.reshape(-1,d*problem.dimension))
    return np.concatenate(blocks,axis=1)


def split_vector(problem,vector):
    maps=[]
    offset=0
    for d in problem.target_dims:
        size=d*problem.dimension
        maps.append(vector[offset:offset+size].reshape(d,problem.dimension))
        offset+=size
    return maps


def hermitian_power(matrix,power,relative_floor=1e-12):
    matrix=(matrix+matrix.conj().T)/2
    values,vectors=np.linalg.eigh(matrix)
    floor=max(float(values[-1]),1.)*relative_floor
    values=np.maximum(values,floor)
    return (vectors*values**power)@vectors.conj().T


def balanced_vertex_factor(outgoing,incoming,step=1.):
    """Positive P approximately minimizes ||P A||²+||C P^-1||²."""
    g=np.einsum('ijx,kjx->ik',outgoing,outgoing.conj())
    h=np.einsum('kix,kjx->ij',incoming.conj(),incoming)
    g_half=hermitian_power(g,.5)
    g_inverse_half=hermitian_power(g,-.5)
    x=g_inverse_half@hermitian_power(g_half@h@g_half,.5)@g_inverse_half
    values,vectors=np.linalg.eigh((x+x.conj().T)/2)
    # Bounded gauge steps preserve invertibility and avoid an unstable
    # change of residual metric near rank-deficient numerical iterates.
    values=np.clip(values,.25,4.)**(step/2)
    return (vectors*values)@vectors.conj().T


def gauge_balance(problem,maps,step=1.):
    candidate=[m.copy() for m in maps]
    blocks=[problem.shape] if problem.shape else [(n,n,n) for n in problem.direct_sum]
    offsets=[0,0,0]
    for vertices in blocks:
        edges=[]
        for axis in range(3):
            rows=vertices[axis]*vertices[(axis+1)%3]
            edges.append(candidate[axis][offsets[axis]:offsets[axis]+rows].reshape(
                vertices[axis],vertices[(axis+1)%3],problem.dimension))
            offsets[axis]+=rows
        for vertex in range(3):
            outgoing=edges[vertex]
            incoming=edges[(vertex-1)%3]
            p=balanced_vertex_factor(outgoing,incoming,step)
            p_inverse=np.linalg.inv(p)
            outgoing[...] = np.einsum('ij,jkx->ikx',p,outgoing)
            incoming[...] = np.einsum('ijx,jk->ikx',incoming,p_inverse)
    return candidate


def controls():
    problem=DenseProblem(2,2,source_mode='parity110',direct_sum=(2,))
    control=exact_monomial_control(2,2)
    maps=[np.eye(12,dtype=complex)[p] for p in control['source_coordinates_per_target_leg']]
    if problem.residual(maps)!=0:
        raise ArithmeticError('The exact control did not replay')
    rng=np.random.default_rng(918)
    directions=[rng.normal(size=m.shape)+1j*rng.normal(size=m.shape) for m in maps]
    step=1e-6
    finite=(actual(problem,[m+step*d for m,d in zip(maps,directions)])-
            actual(problem,[m-step*d for m,d in zip(maps,directions)]))/(2*step)
    exact=jacobian(problem,maps)@np.concatenate([d.ravel() for d in directions])
    derivative_error=float(np.linalg.norm(finite.ravel()-exact)/np.linalg.norm(exact))
    if derivative_error>1e-8:
        raise ArithmeticError('Jacobian directional control failed')
    # A deliberately unbalanced exact target remains exact under the
    # target-vertex gauge and can then be balanced without changing it.
    scaled=[m.copy() for m in maps]
    scaled[0].reshape(2,2,12)[0]*=1.7
    scaled[2].reshape(2,2,12)[:,0]/=1.7
    balanced=gauge_balance(problem,scaled)
    gauge_error=problem.residual(balanced)
    if gauge_error>1e-12:
        raise ArithmeticError('The target stabilizer gauge changed an exact target')
    return {'exact_monomial_control_error':0.,
            'complex_directional_jacobian_relative_error':derivative_error,
            'gauge_transformed_control_relative_error':gauge_error}


def optimize(problem,maps,iterations=100,gauge_every=0,callback=None):
    damping=1e-3
    history=[]
    residual=(actual(problem,maps)-problem.target).ravel()
    value=float(np.vdot(residual,residual).real)
    for iteration in range(iterations):
        j=jacobian(problem,maps)
        gram=j.conj().T@j
        gradient=j.conj().T@residual
        diagonal=np.maximum(np.real(np.diag(gram)),max(float(np.max(np.real(np.diag(gram)))),1.)*1e-10)
        accepted=False
        ratio=None
        for attempt in range(12):
            system=gram.copy()
            system[np.diag_indices_from(system)]+=damping*diagonal
            delta=cho_solve(cho_factor(system,lower=True,check_finite=False),-gradient,check_finite=False)
            steps=split_vector(problem,delta)
            candidate=[m+d for m,d in zip(maps,steps)]
            next_residual=(actual(problem,candidate)-problem.target).ravel()
            next_value=float(np.vdot(next_residual,next_residual).real)
            predicted=-2*float(np.vdot(gradient,delta).real)-float(np.vdot(j@delta,j@delta).real)
            if next_value<value:
                ratio=(value-next_value)/predicted if predicted>0 else 0.
                maps=candidate
                residual=next_residual
                value=next_value
                damping=max(damping/3,1e-12) if ratio>.75 else (damping*2 if ratio<.25 else damping)
                accepted=True
                break
            damping*=10
        gauge_accepted=False
        if gauge_every and (iteration+1)%gauge_every==0:
            for gauge_step in (1.,.5,.25):
                candidate=gauge_balance(problem,maps,gauge_step)
                next_residual=(actual(problem,candidate)-problem.target).ravel()
                next_value=float(np.vdot(next_residual,next_residual).real)
                if next_value<value:
                    maps=candidate
                    residual=next_residual
                    value=next_value
                    gauge_accepted=True
                    break
        error=value**.5/problem.norm
        record={'iteration':iteration+1,'full_relative_error':error,'damping':damping,
                'step_accepted':accepted,'gauge_step_accepted':gauge_accepted,
                'actual_to_predicted_reduction':ratio}
        history.append(record)
        if callback:
            callback(maps,record)
        if error<1e-10 or (not accepted and not gauge_accepted):
            break
    return maps,history


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a',type=int,default=2)
    parser.add_argument('--b',type=int,default=2)
    target=parser.add_mutually_exclusive_group()
    target.add_argument('--shape',type=int,nargs=3)
    target.add_argument('--direct-sum',type=int,nargs='+')
    parser.add_argument('--source-mode',default='parity110')
    parser.add_argument('--initial',type=Path)
    parser.add_argument('--noise',type=float,default=0.)
    parser.add_argument('--starts',type=int,default=1)
    parser.add_argument('--iterations',type=int,default=100)
    parser.add_argument('--gauge-every',type=int,default=0)
    parser.add_argument('--seed',type=int,default=202610213000)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    control=controls()
    shape=None if args.direct_sum else (args.shape or (3,3,3))
    problem=DenseProblem(args.a,args.b,shape,source_mode=args.source_mode,direct_sum=args.direct_sum)
    entries=int(np.prod(problem.target_dims))*sum(problem.target_dims)*problem.dimension
    if entries>10_000_000:
        raise ValueError('This discovery routine uses a full Jacobian and is restricted to small targets')
    initial=np.load(args.initial) if args.initial else None
    best=float('inf')
    records=[]
    started=time.monotonic()
    for trial in range(args.starts):
        maps=problem.random_maps(args.seed+trial,True)
        if initial is not None:
            maps=[initial[name]+args.noise*m for name,m in zip('ABC',maps)]
        initial_error=problem.residual(maps)
        def callback(current,record):
            nonlocal best
            error=record['full_relative_error']
            if error<best:
                best=error
                np.savez_compressed(args.output/'best.npz',A=current[0],B=current[1],C=current[2],
                                    error=error,seed=args.seed+trial,iteration=record['iteration'])
            if record['iteration']==1 or record['iteration']%10==0 or error<1e-10:
                print('trial',trial,'iteration',record['iteration'],'error',error,
                      'damping',record['damping'],'seconds',time.monotonic()-started,flush=True)
        maps,history=optimize(problem,maps,args.iterations,args.gauge_every,callback)
        records.append({'seed':args.seed+trial,'initial_error':initial_error,'trajectory':history,
                        'final_error':problem.residual(maps),'map_norms':[float(np.linalg.norm(m)) for m in maps]})
        report={'source_lengths':[args.a,args.b],'source_mode':args.source_mode,'complex_maps':True,
                'target_shape':shape,'target_direct_sum_sizes':args.direct_sum,
                'algorithm':'full complex damped Gauss-Newton; optional residual-decreasing target stabilizer gauge',
                'gauge_every':args.gauge_every,'starts_completed':len(records),'maximum_iterations':args.iterations,
                'initial_array':str(args.initial) if args.initial else None,
                'initial_sha256':hashlib.sha256(args.initial.read_bytes()).hexdigest() if args.initial else None,
                'initial_noise':args.noise,'controls':control,'records':records,
                'best_full_relative_error':best,'full_target_coefficient_count':int(np.prod(problem.target_dims)),
                'exact_witness_found':False,'exclusion_proved':False,'new_exponent_established':False}
        (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
