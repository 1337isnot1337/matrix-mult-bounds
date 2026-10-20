"""Floating variable projection; all output coefficients are solved linearly."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from flag_fit import Model,unpack


class VariableModel:
    def __init__(self,model):
        self.model=model;self.cut=model.m**2+len(model.points)*model.B
        self.free=model.free[model.free<self.cut]

    def solve(self,x):
        model=self.model;m,B=model.m,model.B;n=len(model.points);width=B+m-1
        full=model.template.copy();full[self.free]=x
        A,Y,Z=unpack(full,m,B)
        products=np.array([[np.convolve(A[p],Y[y]) for y in range(n)] for p in range(m)])
        blocks=[];residuals=[]
        for z in range(n):
            ps,ys=np.nonzero(model.mask[:,:,z]);ks=np.arange(model.z_minimum[z],width)
            D=products[ps,ys][:,ks];target=model.target[ps,ys,z]
            pinv=np.linalg.pinv(D,rcond=1e-12);c=pinv@target;residual=D@c-target
            Z[z,ks]=c
            blocks.append((ps,ys,ks,D,pinv,c,residual));residuals.append(residual)
        return np.concatenate(residuals),full,blocks

    def residual(self,x):return self.solve(x)[0]

    def jacobian(self,x):
        residual,full,blocks=self.solve(x);model=self.model;m,B=model.m,model.B
        A,Y,Z=unpack(full,m,B);rows=[]
        for ps,ys,ks,D,pinv,c,r in blocks:
            J=np.zeros((len(ps),len(self.free)))
            for column,index in enumerate(self.free):
                delta=np.zeros_like(D)
                if index<m*m:
                    p0,degree=divmod(index,m);selected=np.flatnonzero(ps==p0)
                    valid=np.flatnonzero((ks>=degree)&(ks-degree<B))
                    delta[np.ix_(selected,valid)]=Y[ys[selected]][:,ks[valid]-degree]
                else:
                    y0,degree=divmod(index-m*m,B);selected=np.flatnonzero(ys==y0)
                    valid=np.flatnonzero((ks>=degree)&(ks-degree<m))
                    delta[np.ix_(selected,valid)]=A[ps[selected]][:,ks[valid]-degree]
                first=delta@c
                J[:,column]=first-D@(pinv@first)-pinv.T@(delta.T@r)
            rows.append(J)
        return np.vstack(rows)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max-nfev',type=int,default=500)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True);parser.add_argument('--seed',type=int)
    args=parser.parse_args();seed=args.seed if args.seed is not None else int.from_bytes(os.urandom(8),'big')
    rng=np.random.default_rng(seed)
    small=Model(3,6,[0,7,14]);sm=VariableModel(small);sx=small.random_start(rng)
    sf=small.expand(sx);x=sf[sm.free];direction=rng.normal(size=len(x));direction/=np.linalg.norm(direction)
    h=1e-6
    jac_error=float(np.max(np.abs((sm.residual(x+h*direction)-sm.residual(x-h*direction))/(2*h)-sm.jacobian(x)@direction)))
    print('Jacobian error',jac_error,flush=True)
    if jac_error>2e-5:raise ArithmeticError('variable-projection Jacobian control failed')
    source=args.input;old=json.loads(source.read_text())
    model=Model(4,10,old['eta'],old.get('beta',1));vm=VariableModel(model)
    reports=[]
    for index in range(3):
        if index==0:
            best=min(old['reports'],key=lambda r:r['best_relative_residual'])
            initial=np.r_[np.array(best['A']).ravel(),np.array(best['B']).ravel(),np.array(best['C']).ravel()][vm.free]
            origin='best full-flag fit'
        else:
            initial=model.expand(model.random_start(rng))[vm.free];origin='OS-seeded random flag start'
        calls=[0];best=[float('inf'),None]
        def residual(x):
            value=vm.residual(x);relative=float(np.linalg.norm(value)/model.denominator);calls[0]+=1
            if relative<best[0]:best[:]=relative,x.copy()
            if calls[0]%100==1:print('start',index,'call',calls[0],'relative',relative,'best',best[0],flush=True)
            return value
        result=least_squares(residual,initial,jac=vm.jacobian,x_scale='jac',max_nfev=args.max_nfev,
                             ftol=1e-12,xtol=1e-12,gtol=1e-12)
        _,full,_=vm.solve(best[1]);matrices=unpack(full,4,10)
        reports.append({'index':index,'origin':origin,'nfev':result.nfev,'status':result.status,
                        'message':result.message,'best_relative_residual':best[0],
                        'max_abs_coefficient':float(max(np.max(np.abs(M)) for M in matrices)),
                        **{key:M.tolist() for key,M in zip(['A','B','C'],matrices)}})
        report={'m':4,'B':10,'eta':old['eta'],'seed':seed,'free_input_parameters':len(vm.free),
                'output_parameters_eliminated':len(model.free)-len(vm.free),
                'jacobian_directional_error':jac_error,'rcond':1e-12,'max_nfev':args.max_nfev,
                'input_report_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'reports':reports,'certified_degeneration':False}
        args.output.write_text(json.dumps(report,indent=2)+'\n')
        print('completed start',index,'best',best[0],flush=True)
