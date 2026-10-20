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


source=Path('/tmp/matrix-mult-source-20261020/refined-m4.json')
data=json.loads(source.read_text());start=data['best'];m,B=data['m'],data['B']
target,mask,weights=target_and_weights(m,data['order'])
initial=np.r_[np.array(start['A']).ravel(),np.array(start['B']).ravel(),np.array(start['C']).ravel()]
denominator=np.linalg.norm(target[mask])
seed=int.from_bytes(os.urandom(8),'big');rng=np.random.default_rng(seed)
small_m,small_B=2,3
small_target,small_mask,_=target_and_weights(small_m,(1,0))
small_x=rng.normal(size=4+3*3+3*4);direction=rng.normal(size=len(small_x));direction/=np.linalg.norm(direction)
def small_fun(x):return (transform(*unpack(x,small_m,small_B))-small_target)[small_mask]
h=1e-6
error=float(np.max(np.abs((small_fun(small_x+h*direction)-small_fun(small_x-h*direction))/(2*h)
                          -jacobian(small_x,small_m,small_B,small_mask)@direction)))
if error>1e-7:raise ArithmeticError('analytic Jacobian failed finite-difference control')
best={'relative_residual':float('inf')};calls=0
def residual(x):
    global calls,best
    value=(transform(*unpack(x,m,B))-target)[mask];relative=float(np.linalg.norm(value)/denominator);calls+=1
    if relative<best['relative_residual']:
        matrices=unpack(x,m,B)
        best={'relative_residual':relative,'call':calls,
              **{key:matrix.tolist() for key,matrix in zip(['A','B','C'],matrices)},
              'max_abs_coefficient':float(max(np.max(np.abs(M)) for M in matrices))}
    if calls%25==1:print('call',calls,'relative',relative,'best',best['relative_residual'],flush=True)
    return value

result=least_squares(residual,initial,jac=lambda x:jacobian(x,m,B,mask),method='trf',
                     x_scale='jac',max_nfev=300,ftol=1e-12,xtol=1e-12,gtol=1e-12)
report={'m':m,'B':B,'order':data['order'],'weights':weights,
        'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'control_seed':seed,'jacobian_control_error':error,
        'numpy_version':np.__version__,'scipy_version':scipy.__version__,
        'method':'trf','x_scale':'jac','max_nfev':300,'nfev':result.nfev,
        'status':result.status,'message':result.message,'optimality':result.optimality,
        'initial_relative_residual':data['best']['relative_residual'],
        'best':best,'certified_degeneration':False}
Path('/tmp/matrix-mult-source-20261020/joint-m4.json').write_text(json.dumps(report,indent=2)+'\n')
print('final best',best['relative_residual'],result.message,flush=True)
