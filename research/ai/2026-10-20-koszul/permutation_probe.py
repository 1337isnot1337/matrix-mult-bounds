"""Bounded discovery at a previously untested grading; no float acceptance."""
import importlib.util,itertools,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
BASE=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('graded',BASE/'research/ai/2026-10-20-concavity-equivalence/graded_shared_discovery.py')
graded=importlib.util.module_from_spec(spec);spec.loader.exec_module(graded)
OUT=BASE/'results/local/intermediate-permutations';OUT.mkdir(parents=True,exist_ok=True)
m=4;alpha=5;beta=2;budget=600
n,b,unpack,fun,jac=graded.problem(m,0,alpha,beta)
size=b*n+n*(b+m-1)
perms=[p for p in itertools.permutations(range(m)) if p[0]<m-1-p[0] and p!=tuple(range(m))]
for index,perm in enumerate(perms):
    name=''.join(map(str,perm));seed=202610200+index
    g=np.eye(m)[list(perm),:];rng=np.random.default_rng(seed)
    x0=rng.normal(size=size)/np.sqrt(n)
    full=lambda x:np.r_[x,g.ravel()]
    f=lambda x:fun(full(x))
    j=lambda x:jac(full(x))[:,:size]
    start=time.monotonic()
    result=least_squares(f,x0,jac=j,max_nfev=budget,ftol=1e-12,xtol=1e-12,gtol=1e-12)
    p,q,_=unpack(full(result.x))
    np.savez(OUT/(name+'.npz'),P=p,Q=q,G=g)
    record={'m':m,'B':b,'alpha':alpha,'beta':beta,'permutation':list(perm),'seed':seed,'budget':budget,'nfev':result.nfev,'equations':len(f(x0)),'residual':float(np.linalg.norm(result.fun)),'max_coefficient':float(np.max(np.abs(result.x))),'minimum_singular_values':[float(np.linalg.svd(v,compute_uv=False)[-1]) for v in(p,q)],'seconds':time.monotonic()-start,'status':'floating discovery only; no exact certificate'}
    (OUT/(name+'.json')).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record),flush=True)
