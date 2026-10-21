"""Numerical target-vertex gauge balancing; residual norms are gauge-dependent."""
import argparse,hashlib,io,json
from pathlib import Path
import numpy as np


def power(A,p):
    A=(A+A.conj().T)/2
    values,vectors=np.linalg.eigh(A)
    values=np.maximum(values,max(float(values[-1])*1e-13,1e-30))
    return (vectors*values**p)@vectors.conj().T


def transform(M,G,axis):
    return np.moveaxis(np.tensordot(M,G,axes=([axis],[0])),-1,axis)


def gram(M,axis):
    Q=np.moveaxis(M,axis,-1).reshape(-1,M.shape[axis])
    return Q.conj().T@Q


def balance(maps,dimensions=(5,5,4),sweeps=20):
    p,q,r=dimensions
    shapes=[(p,q),(q,r),(r,p)]
    M=[a.reshape(*a.shape[:2],*shape).copy() for a,shape in zip(maps,shapes)]
    gauges=[np.eye(a.shape[-1],dtype=complex) for a in maps]
    history=[]
    for sweep in range(sweeps):
        for leg in range(3):
            other=(leg-1)%3
            Q=gram(M[leg],2);R=gram(M[other],3).T
            Qhalf=power(Q,.5);Qinv=power(Q,-.5)
            X=Qinv@power(Qhalf@R@Qhalf,.5)@Qinv
            G=power(X,.5);H=np.linalg.inv(G).T
            before=sum(np.linalg.norm(a)**2 for a in M)
            M[leg]=transform(M[leg],G,2)
            M[other]=transform(M[other],H,3)
            gauges[leg]=gauges[leg]@np.kron(G,np.eye(shapes[leg][1]))
            gauges[other]=gauges[other]@np.kron(np.eye(shapes[other][0]),H)
            after=sum(np.linalg.norm(a)**2 for a in M)
            assert after<=before*(1+1e-9)
        history.append(float(np.sqrt(after)))
    target=np.zeros((p*q,q*r,r*p),complex)
    for i in range(p):
        for j in range(q):
            for k in range(r):target[q*i+j,r*j+k,p*k+i]=1
    changed=np.einsum('abc,ai,bj,ck->ijk',target,*gauges,optimize=True)
    error=float(np.linalg.norm(changed-target)/np.linalg.norm(target))
    assert error<1e-9
    flat=[a.reshape(m.shape) for a,m in zip(M,maps)]
    assert all(np.allclose(m@g,a,atol=1e-8,rtol=1e-8) for m,g,a in zip(maps,gauges,flat))
    return flat,{'initial_coefficient_norm':float(np.sqrt(sum(np.linalg.norm(m)**2 for m in maps))),
                 'coefficient_norm_history':history,'target_invariance_relative_error':error,
                 'leg_gauge_condition_numbers':[float(np.linalg.cond(g)) for g in gauges],
                 'residual_norms_are_gauge_dependent':True,'exact_certificate':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path);p.add_argument('--sweeps',type=int,default=20);a=p.parse_args()
    raw=a.input.read_bytes();z=np.load(io.BytesIO(raw));maps=[z[n] for n in 'ABC']
    out,report=balance(maps,sweeps=a.sweeps);a.output.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(a.output/'balanced.npz',**dict(zip('ABC',out)))
    report['input_sha256']=hashlib.sha256(raw).hexdigest()
    (a.output/'report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
