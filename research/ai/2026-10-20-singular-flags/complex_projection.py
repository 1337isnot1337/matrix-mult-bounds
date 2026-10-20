"""Complex-coefficient discovery in the flag model with variable projection."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import least_squares
from flag_fit import Model,unpack
from variable_projection import VariableModel


class ComplexModel(VariableModel):
    def complex_x(self,x):
        n=len(self.free);return x[:n]+1j*x[n:]

    def residual_real(self,x):
        r=self.solve(self.complex_x(x))[0];return np.r_[r.real,r.imag]

    def jacobian_real(self,x):
        _,full,blocks=self.solve(self.complex_x(x));model=self.model;m,B=model.m,model.B
        A,Y,Z=unpack(full,m,B);rows=[]
        for ps,ys,ks,D,pinv,c,r in blocks:
            J=np.zeros((len(ps),2*len(self.free)),dtype=complex)
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
                first=delta@c;U=first-D@(pinv@first)
                V=pinv.conj().T@(delta.conj().T@r)
                J[:,column]=U-V
                J[:,column+len(self.free)]=1j*(U+V)
            rows.append(J)
        J=np.vstack(rows);return np.vstack([J.real,J.imag])


def make_model(m,eta,beta=1):
    B=m*(m+1)//2;model=Model(m,B,eta,beta);model.template=model.template.astype(complex)
    return model,ComplexModel(model)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max-nfev',type=int,default=500)
    parser.add_argument('--starts',type=int,default=3);parser.add_argument('--seed',type=int)
    parser.add_argument('--eta',default='0,201,403,607');parser.add_argument('--beta',type=int,default=100)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();seed=args.seed if args.seed is not None else int.from_bytes(os.urandom(8),'big')
    rng=np.random.default_rng(seed);small,sm=make_model(3,[0,7,14])
    full=small.template.copy();full[small.free]=.2*(rng.normal(size=len(small.free))+1j*rng.normal(size=len(small.free)))
    a=full[sm.free];sx=np.r_[a.real,a.imag];direction=rng.normal(size=len(sx));direction/=np.linalg.norm(direction)
    h=1e-6;error=float(np.max(np.abs((sm.residual_real(sx+h*direction)-sm.residual_real(sx-h*direction))/(2*h)-sm.jacobian_real(sx)@direction)))
    print('complex Jacobian error',error,flush=True)
    if error>2e-5:raise ArithmeticError('complex variable-projection Jacobian control failed')
    eta=list(map(int,args.eta.split(',')));model,vm=make_model(4,eta,args.beta);reports=[]
    for index in range(args.starts):
        full=model.template.copy();full[model.free]=.2*(rng.normal(size=len(model.free))+1j*rng.normal(size=len(model.free)))
        A,Y,Z=unpack(full,4,10)
        # Vary the component phases rather than forcing every free pivot positive.
        for p in range(2):A[p,3-p]=np.exp(2j*np.pi*rng.random())
        for y,(a,b) in enumerate(model.points):
            if a:Y[y,model.y_degree[y]]=np.exp(2j*np.pi*rng.random())
        z=full[vm.free];initial=np.r_[z.real,z.imag];calls=[0];best=[float('inf'),None]
        def residual(values):
            r=vm.residual_real(values);relative=float(np.linalg.norm(r)/model.denominator);calls[0]+=1
            if relative<best[0]:best[:]=relative,values.copy()
            if calls[0]%100==1:print('start',index,'call',calls[0],'relative',relative,'best',best[0],flush=True)
            return r
        result=least_squares(residual,initial,jac=vm.jacobian_real,x_scale='jac',max_nfev=args.max_nfev,
                             ftol=1e-12,xtol=1e-12,gtol=1e-12)
        _,full,_=vm.solve(vm.complex_x(best[1]));matrices=unpack(full,4,10)
        report={'index':index,'nfev':result.nfev,'status':result.status,'message':result.message,
                'best_relative_residual':best[0],'max_abs_coefficient':float(max(np.max(np.abs(M)) for M in matrices))}
        for key,M in zip(['A','B','C'],matrices):report[key+'_real']=M.real.tolist();report[key+'_imag']=M.imag.tolist()
        reports.append(report)
        data={'m':4,'B':10,'eta':eta,'beta':args.beta,'seed':seed,'seed_origin':'provided' if args.seed is not None else 'os.urandom(8)',
              'complex_input_parameters':len(vm.free),'real_optimization_parameters':2*len(vm.free),
              'output_complex_parameters_eliminated':len(model.free)-len(vm.free),
              'max_nfev':args.max_nfev,'jacobian_directional_error':error,'rcond':1e-12,
              'numpy_version':np.__version__,'scipy_version':scipy.__version__,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'imported_source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                        for name in ['flag_fit.py','variable_projection.py','numerical_common.py','flag_obstruction.py']},
              'reports':reports,'certified_degeneration':False}
        args.output.write_text(json.dumps(data,indent=2)+'\n');print('completed',index,'best',best[0],flush=True)
