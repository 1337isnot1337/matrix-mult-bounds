"""Floating discovery refinement with an analytic trilinear Jacobian."""
import hashlib
import json
import os
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
from refine_core import target_and_weights, transform


def unpack(vector, m, B):
    n=m*(m+1)//2
    return (vector[:m*m].reshape(m,m),
            vector[m*m:m*m+n*B].reshape(n,B),
            vector[m*m+n*B:].reshape(n,B+m-1))


def jacobian(vector,m,B,mask):
    A,Y,Z=unpack(vector,m,B);n=Y.shape[0];width=Z.shape[1]
    p,y,z=np.nonzero(mask);count=len(p);rows=np.arange(count)
    J=np.zeros((count,len(vector)))
    for r in range(m):
        values=Y@Z[:,r:r+B].T
        J[rows,p*m+r]=values[y,z]
    for j in range(B):
        values=A@Z[:,j:j+m].T
        J[rows,m*m+y*B+j]=values[p,z]
    products=np.array([[np.convolve(A[r],Y[s]) for s in range(n)] for r in range(m)])
    for k in range(width):
        J[rows,m*m+n*B+z*width+k]=products[p,y,k]
    return J


def gauge_values(vector,m,B):
    A,Y,Z=unpack(vector,m,B);pts=[(a,d-a) for d in range(m) for a in range(d+1)]
    return np.r_[np.sum(A*A)-m,np.sum(A[0]*A[0])-np.sum(A[-1]*A[-1]),
                 [sum(np.dot(Y[i],Y[i]) for i,(a,b) in enumerate(pts) if a+b==u-1)-u
                  for u in range(1,m+1)]]


def gauge_jacobian(vector,m,B):
    A,Y,Z=unpack(vector,m,B);pts=[(a,d-a) for d in range(m) for a in range(d+1)]
    J=np.zeros((m+2,len(vector)));J[0,:m*m]=2*A.ravel()
    J[1,:m]=2*A[0];J[1,(m-1)*m:m*m]=-2*A[-1]
    for u in range(1,m+1):
        for i,(a,b) in enumerate(pts):
            if a+b==u-1:J[u+1,m*m+i*B:m*m+(i+1)*B]=2*Y[i]
    return J


source=Path('/tmp/matrix-mult-source-20261020/joint-m4.json')
data=json.loads(source.read_text());start=data['best'];m,B=data['m'],data['B']
target,mask,weights=target_and_weights(m,data['order'])
initial=np.r_[np.array(start['A']).ravel(),np.array(start['B']).ravel(),np.array(start['C']).ravel()]
denominator=np.linalg.norm(target[mask])
A,Y,Z=(M.copy() for M in unpack(initial,m,B));before=transform(A,Y,Z)
torus_scale=(np.linalg.norm(A[0])/np.linalg.norm(A[-1]))**(1/(m-1))
pts=[(a,d-a) for d in range(m) for a in range(d+1)]
A*=torus_scale**np.arange(m)[:,None]
Y*=np.array([torus_scale**(-a) for a,b in pts])[:,None]
Z*=np.array([torus_scale**(-c) for c,d in pts])[:,None]
scalar=np.sqrt(m)/np.linalg.norm(A);A*=scalar;Z/=scalar
for u in range(1,m+1):
    yy=[i for i,(a,b) in enumerate(pts) if a+b==u-1]
    zz=[i for i,(c,d) in enumerate(pts) if c+d==m-u]
    scalar=np.sqrt(u)/np.linalg.norm(Y[yy]);Y[yy]*=scalar;Z[zz]/=scalar
initial=np.r_[A.ravel(),Y.ravel(),Z.ravel()]
desired_invariance_error=float(np.max(np.abs((transform(A,Y,Z)-before)[target!=0])))
initial_balanced_relative=float(np.linalg.norm((transform(A,Y,Z)-target)[mask])/denominator)
print('before balance',data['best']['relative_residual'],'after',initial_balanced_relative,
      'torus',torus_scale,'desired invariance error',desired_invariance_error,flush=True)
seed=int.from_bytes(os.urandom(8),'big');rng=np.random.default_rng(seed)
small_m,small_B=2,3
small_target,small_mask,_=target_and_weights(small_m,(1,0))
small_x=rng.normal(size=4+3*3+3*4);direction=rng.normal(size=len(small_x));direction/=np.linalg.norm(direction)
def small_fun(x):return np.r_[(transform(*unpack(x,small_m,small_B))-small_target)[small_mask],gauge_values(x,small_m,small_B)]
h=1e-6
error=float(np.max(np.abs((small_fun(small_x+h*direction)-small_fun(small_x-h*direction))/(2*h)
                          -np.vstack([jacobian(small_x,small_m,small_B,small_mask),gauge_jacobian(small_x,small_m,small_B)])@direction)))
if error>1e-7:raise ArithmeticError('analytic Jacobian failed finite-difference control')
best={'merit':float('inf')};calls=0
def residual(x):
    global calls,best
    value=(transform(*unpack(x,m,B))-target)[mask];relative=float(np.linalg.norm(value)/denominator);calls+=1
    gauges=gauge_values(x,m,B);combined=np.r_[value,gauges];merit=float(np.linalg.norm(combined)/denominator)
    if merit<best['merit']:
        matrices=unpack(x,m,B)
        best={'relative_residual':relative,'merit':merit,'gauge_residual':float(np.linalg.norm(gauges)),'call':calls,
              **{key:matrix.tolist() for key,matrix in zip(['A','B','C'],matrices)},
              'max_abs_coefficient':float(max(np.max(np.abs(M)) for M in matrices))}
    if calls%25==1:print('call',calls,'relative',relative,'best',best['relative_residual'],flush=True)
    return combined

result=least_squares(residual,initial,jac=lambda x:np.vstack([jacobian(x,m,B,mask),gauge_jacobian(x,m,B)]),method='trf',
                     x_scale='jac',max_nfev=300,ftol=1e-12,xtol=1e-12,gtol=1e-12)
report={'m':m,'B':B,'order':data['order'],'weights':weights,
        'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'control_seed':seed,'jacobian_control_error':error,
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'method':'trf','x_scale':'jac','max_nfev':300,'nfev':result.nfev,
        'status':result.status,'message':result.message,'optimality':result.optimality,
        'initial_relative_residual':data['best']['relative_residual'],
        'initial_balanced_relative_residual':initial_balanced_relative,
        'torus_scale':torus_scale,'desired_invariance_error':desired_invariance_error,
        'best':best,'certified_degeneration':False}
Path('/tmp/matrix-mult-source-20261020/balanced-m4.json').write_text(json.dumps(report,indent=2)+'\n')
print('final best',best['relative_residual'],result.message,flush=True)
