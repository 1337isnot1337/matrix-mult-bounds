"""Historical floating experiment in an analytically excluded weight region.

See arbitrary_shared_basis.md Section 6. This is not a certificate verifier.
The completed cases used NumPy 2.5.4; no inference relies on residual size.
"""
import argparse,json,sys,time
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
import all_dimension_targets as family

def run(m,seed,cycles,basis='random',free_g=False):
    nodes,_,terms=family.target(m); n=len(nodes); b=n; r=b+m-1
    desired=np.zeros((m,n,n))
    for x,y,z in terms:desired[x,z,y]=1
    degrees=np.array([a+b for a,b in nodes]); powers=np.array([a for a,b in nodes])
    weight=np.arange(m)[:,None,None]-powers[None,:,None]-powers[None,None,:]+(m+1)*(degrees[None,:,None]+degrees[None,None,:]-(m-1))
    ii,zz,yy=np.nonzero(weight<=0); rhs=desired[ii,zz,yy]
    assert np.all(desired[weight!=0]==0)
    rng=np.random.default_rng(seed)
    p=rng.normal(size=(b,n))/np.sqrt(n); q=rng.normal(size=(n,r))/np.sqrt(n)
    if basis=='identity':g=np.eye(m)
    elif basis=='vandermonde':g=np.vander(np.arange(1,m+1),increasing=True).astype(float);g/=np.linalg.norm(g,axis=1)[:,None]
    else:g=np.linalg.qr(rng.normal(size=(m,m)))[0]
    rows=np.arange(len(ii))[:,None]; jj=np.arange(b); kk=np.arange(r)
    start=time.monotonic();best=float('inf');stale=0
    for cycle in range(cycles):
        ap=np.zeros((len(ii),b*n));dp=np.zeros((len(ii),b))
        for h in range(m):dp+=g[ii,h,None]*q[zz[:,None],h+jj]
        ap[rows,jj[None,:]*n+yy[:,None]]=dp
        p=np.linalg.lstsq(ap,rhs,rcond=1e-12)[0].reshape(b,n)
        aq=np.zeros((len(ii),n*r));dq=np.zeros((len(ii),r))
        for h in range(m):dq[:,h:h+b]+=g[ii,h,None]*p[:,yy].T
        aq[rows,zz[:,None]*r+kk[None,:]]=dq
        q=np.linalg.lstsq(aq,rhs,rcond=1e-12)[0].reshape(n,r)
        raw=np.stack([q[:,h:h+b]@p for h in range(m)])
        if free_g:
            for i in range(m):
                selected=ii==i
                g[i]=np.linalg.lstsq(raw[:,zz[selected],yy[selected]].T,rhs[selected],rcond=1e-12)[0]
        error=np.linalg.norm(np.einsum('ih,hzy->izy',g,raw)[ii,zz,yy]-rhs)
        if error<best*(1-1e-8):best=error;stale=0
        else:stale+=1
        if error<1e-10 or stale>=100:break
        scale=np.sqrt(np.linalg.norm(q)/np.linalg.norm(p));p*=scale;q/=scale
    output={'m':m,'B':b,'seed':seed,'basis':basis,'free_g':free_g,'cycles':cycle+1,'equations':len(ii),'residual':float(error),'smallest_singular_values':[float(np.linalg.svd(v,compute_uv=False)[-1]) for v in (p,q,g)],'norms':[float(np.linalg.norm(v)) for v in(p,q,g)],'seconds':time.monotonic()-start,'status':'floating exploration only; no exact certificate'}
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--m',type=int,default=4);parser.add_argument('--cycles',type=int,default=1000);parser.add_argument('--seed',type=int,default=0);parser.add_argument('--basis',default='random');parser.add_argument('--free-g',action='store_true');args=parser.parse_args()
    print(json.dumps(run(args.m,args.seed,args.cycles,args.basis,args.free_g)),flush=True)
