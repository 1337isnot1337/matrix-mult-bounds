"""Floating discovery in a triangular flag normal form; no acceptance by floats."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
from refine_core import transform


def unpack(vector,m,B):
    n=m*(m+1)//2
    return (vector[:m*m].reshape(m,m),vector[m*m:m*m+n*B].reshape(n,B),
            vector[m*m+n*B:].reshape(n,B+m-1))


def full_jacobian(vector,m,B,mask):
    A,Y,Z=unpack(vector,m,B);n=Y.shape[0];width=Z.shape[1]
    p,y,z=np.nonzero(mask);rows=np.arange(len(p));J=np.zeros((len(p),len(vector)))
    for r in range(m):J[rows,p*m+r]=(Y@Z[:,r:r+B].T)[y,z]
    for j in range(B):J[rows,m*m+y*B+j]=(A@Z[:,j:j+m].T)[p,z]
    products=np.array([[np.convolve(A[r],Y[s]) for s in range(n)] for r in range(m)])
    for k in range(width):J[rows,m*m+n*B+z*width+k]=products[p,y,k]
    return J


class Model:
    def __init__(self,m,B,eta):
        self.m,self.B=m,B;self.points=[(a,d-a) for d in range(m) for a in range(d+1)]
        n=len(self.points);width=B+m-1
        self.weights={'x':list(range(m)),'y':[eta[a+b]-a for a,b in self.points],
                      'z':[-eta[m-1-c-d]-c for c,d in self.points]}
        if len(set(self.weights['y']))<n or len(set(self.weights['z']))<n:
            raise ValueError('this pilot requires distinct coordinate weights')
        self.target=np.zeros((m,n,n))
        for y,(a,b) in enumerate(self.points):
            for z,(c,d) in enumerate(self.points):
                if a+b+c+d==m-1:self.target[a+c,y,z]=1
        w=self.weights
        powers=np.array(w['x'])[:,None,None]+np.array(w['y'])[None,:,None]+np.array(w['z'])[None,None,:]
        if np.any(self.target[powers!=0]):raise ArithmeticError('target not weight zero')
        self.mask=powers<=0;self.denominator=np.linalg.norm(self.target)
        rank_y=np.argsort(np.argsort(w['y']));rank_z=np.argsort(np.argsort(w['z']))
        self.y_degree=B-1-rank_y;self.z_minimum=rank_z
        A=np.zeros((m,m));Y=np.zeros((n,B));Z=np.zeros((n,width))
        allowed_A=np.zeros_like(A,dtype=bool);allowed_Y=np.zeros_like(Y,dtype=bool);allowed_Z=np.zeros_like(Z,dtype=bool)
        for p in range(m):allowed_A[p,:m-p]=True
        for y in range(n):allowed_Y[y,:self.y_degree[y]+1]=True
        for z in range(n):allowed_Z[z,self.z_minimum[z]:]=True
        # Exact target diagonal stabilizer anchors, followed by source translation.
        A[-1,0]=1;allowed_A[-1,0]=False
        A[-2,1]=1;allowed_A[-2,1]=False;allowed_A[-2,0]=False
        for y,(a,b) in enumerate(self.points):
            if a==0:Y[y,self.y_degree[y]]=1;allowed_Y[y,self.y_degree[y]]=False
        self.template=np.r_[A.ravel(),Y.ravel(),Z.ravel()]
        self.free=np.flatnonzero(np.r_[allowed_A.ravel(),allowed_Y.ravel(),allowed_Z.ravel()])

    def expand(self,x):
        full=self.template.copy();full[self.free]=x;return full

    def residual(self,x):return (transform(*unpack(self.expand(x),self.m,self.B))-self.target)[self.mask]

    def jacobian(self,x):return full_jacobian(self.expand(x),self.m,self.B,self.mask)[:,self.free]

    def random_start(self,rng):
        full=self.template.copy();full[self.free]=.15*rng.normal(size=len(self.free))
        A,Y,Z=unpack(full,self.m,self.B)
        for p in range(self.m):A[p,self.m-1-p]=1
        for y,j in enumerate(self.y_degree):Y[y,j]=1
        for z,k in enumerate(self.z_minimum):Z[z,k]=1
        return full[self.free]


def calibrate(seed):
    rng=np.random.default_rng(seed);model=Model(2,3,[0,3])
    A=np.array([[0,1],[1,0]]);Y=np.array([[0,0,1],[1,0,0],[0,1,0]])
    Z=np.array([[1,1,0,0],[0,0,1,1],[0,1,1,0]])
    full=np.r_[A.ravel(),Y.ravel(),Z.ravel()];x=full[model.free]
    if not np.array_equal(model.expand(x),full) or np.max(np.abs(model.residual(x)))!=0:
        raise ArithmeticError('exact small flag control failed')
    direction=rng.normal(size=len(x));direction/=np.linalg.norm(direction);h=1e-6
    error=float(np.max(np.abs((model.residual(x+h*direction)-model.residual(x-h*direction))/(2*h)
                              -model.jacobian(x)@direction)))
    if error>1e-7:raise ArithmeticError('flag Jacobian failed finite differences')
    start=x+.02*rng.normal(size=len(x))
    result=least_squares(model.residual,start,jac=model.jacobian,max_nfev=100,
                         ftol=1e-12,xtol=1e-12,gtol=1e-12)
    relative=float(np.linalg.norm(result.fun)/model.denominator)
    if relative>1e-8:raise ArithmeticError('perturbed positive optimization control failed')
    return {'known_exact_control_max_error':0,'free_parameters':len(x),
            'jacobian_directional_error':error,'perturbed_control_relative_residual':relative}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--m',type=int,default=4)
    parser.add_argument('--eta',default='7,14,21,0');parser.add_argument('--starts',type=int,default=2)
    parser.add_argument('--max-nfev',type=int,default=500);parser.add_argument('--seed',type=int)
    parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    seed=args.seed if args.seed is not None else int.from_bytes(os.urandom(8),'big')
    control=calibrate(seed);print('control',control,flush=True)
    eta=list(map(int,args.eta.split(',')));m=args.m;B=m*(m+1)//2;model=Model(m,B,eta)
    reports=[]
    for index in range(args.starts):
        rng=np.random.default_rng(seed+index);x=model.random_start(rng);calls=[0];best=[float('inf'),None]
        def residual(values):
            error=model.residual(values);relative=float(np.linalg.norm(error)/model.denominator);calls[0]+=1
            if relative<best[0]:best[:]=relative,values.copy()
            if calls[0]%100==1:print('start',index,'call',calls[0],'relative',relative,'best',best[0],flush=True)
            return error
        result=least_squares(residual,x,jac=model.jacobian,x_scale='jac',max_nfev=args.max_nfev,
                             ftol=1e-12,xtol=1e-12,gtol=1e-12)
        matrices=unpack(model.expand(best[1]),m,B)
        reports.append({'index':index,'seed':seed+index,'nfev':result.nfev,'status':result.status,
                        'message':result.message,'best_relative_residual':best[0],
                        'max_abs_coefficient':float(max(np.max(np.abs(M)) for M in matrices)),
                        **{key:M.tolist() for key,M in zip(['A','B','C'],matrices)}})
        report={'m':m,'B':B,'eta':eta,'weights':model.weights,'seed':seed,
                'seed_origin':'provided' if args.seed is not None else 'os.urandom(8)',
                'free_parameters':len(model.free),'mask_constraints':int(np.sum(model.mask)),
                'max_nfev':args.max_nfev,'control':control,'reports':reports,
                'numpy_version':np.__version__,'scipy_version':scipy.__version__,
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'certified_degeneration':False}
        args.output.write_text(json.dumps(report,indent=2)+'\n')
        print('completed start',index,'best',best[0],flush=True)
