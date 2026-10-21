from pathlib import Path
exec(Path(__file__).with_name('weighted_cyclic_m3_balanced.py').read_text().split('records=[];')[0])
from scipy.optimize import least_squares
shape=(9,9,9);cuts=[0,108,216,324]
def split(x):return [x[cuts[i]:cuts[i+1]].reshape(9,12) for i in range(3)]
def full(x):return (np.einsum('abc,ia,jb,kc->ijk',T,*split(x),optimize=True)-M).ravel()
def fulljac(x):
 F=split(x);parts=[]
 for axis,expr in enumerate(('abc,ib,jc->aij','abc,ia,jc->bij','abc,ia,jb->cij')):
  others=[j for j in range(3) if j!=axis];V=np.einsum(expr,T,F[others[0]],F[others[1]],optimize=True).reshape(12,-1);J=np.kron(np.eye(9),V.T);dims=[9,9,9,108];perm=[([axis]+others).index(j) for j in range(3)]+[3];parts.append(J.reshape(dims).transpose(perm).reshape(M.size,108))
 return np.concatenate(parts,axis=1)
def moment(x):
 E=[np.sum(f*f,axis=1).reshape(3,3) for f in split(x)];return np.r_[E[0].sum(1)-E[2].sum(0),E[0].sum(0)-E[1].sum(1),E[1].sum(0)-E[2].sum(1)][1:]
def momentjac(x):
 J=np.zeros((9,324))
 for axis,F in enumerate(split(x)):
  for row in range(9):
   i,j=divmod(row,3);cols=slice(cuts[axis]+row*12,cuts[axis]+(row+1)*12)
   if axis==0:J[i,cols]=2*F[row];J[3+j,cols]=2*F[row]
   elif axis==1:J[3+i,cols]=-2*F[row];J[6+j,cols]=2*F[row]
   else:J[6+i,cols]=-2*F[row];J[j,cols]=-2*F[row]
 return J[1:]
records=[]
for kind in ('weighted','weighted-balanced'):
 w=np.load(root/f'cyclic-{kind}-m333-best.npz');F=balance([w[k].copy() for k in ('A','B','C')]);x0=np.concatenate([f.ravel() for f in F]);mask=w['mask'].ravel();scale=max(1,float(np.linalg.norm(x0)**2)/10)
 def residual(x):return np.r_[full(x)[mask],moment(x)/scale]
 def jac(x):return np.r_[fulljac(x)[mask],momentjac(x)/scale]
 rng=np.random.default_rng(202610400);v=rng.normal(size=324);h=max(1e-6,1e-7*np.linalg.norm(x0)/np.linalg.norm(v));check=np.max(abs((residual(x0+h*v)-residual(x0-h*v))/(2*h)-jac(x0)@v));print('start',kind,'error',np.linalg.norm(full(x0)[mask])/np.linalg.norm(M),'norm',np.linalg.norm(x0),'jaccheck',check,flush=True)
 assert check/max(1,float(np.max(abs(jac(x0)@v))))<1e-6
 r=least_squares(residual,x0,jac=jac,method='lm',max_nfev=1000,ftol=1e-12,xtol=1e-12,gtol=1e-12)
 F=split(r.x);record={'initialization':kind,'nfev':r.nfev,'weighted_relative_error':float(np.linalg.norm(full(r.x)[mask])/np.linalg.norm(M)),'moment_residual':float(np.linalg.norm(moment(r.x))),'map_norms':[float(np.linalg.norm(f)) for f in F],'max_unweighted_coefficient':float(np.max(abs(full(r.x)+M.ravel()))),'exact_certificate':False};records.append(record);print(record,flush=True)
 np.savez(root/f'cyclic-{kind}-m333-lm.npz',A=F[0],B=F[1],C=F[2],u=w['u'],v=w['v'],w=w['w'],mask=mask)
(root/'cyclic-weighted-m333-lm.json').write_text(json.dumps(records,indent=2)+'\n')
