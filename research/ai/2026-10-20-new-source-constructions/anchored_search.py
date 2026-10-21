"""One complex discovery branch kept away from the pure-power shared stratum."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

from full_pivot_torus import FullModel


class AnchoredModel(FullModel):
    def __init__(self,index,value):
        super().__init__()
        self.index,self.value=index,value
        self.fixed={index}
        self.active=[j for j in range(125) if j!=index]
        self.n=len(self.active)+18

    def unpack(self,parameters):
        values,logs=super().unpack(parameters)
        values[self.index]=self.value
        return values,logs


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--index',type=int,choices=range(5),default=3)
    p.add_argument('--value',type=float,default=1.0)
    p.add_argument('--max-nfev',type=int,default=3000)
    args=p.parse_args()
    model=AnchoredModel(args.index,args.value)
    source=json.loads(args.input.read_text())
    coefficients=np.array(source['coefficients_real'])+1j*np.array(source['coefficients_imag'])
    logs=np.array(source['target_logs_real'])+1j*np.array(source['target_logs_imag'])
    parameters=np.r_[coefficients[model.active],logs]
    initial=np.r_[parameters.real,parameters.imag]
    result=least_squares(model.real_residual,initial,jac=model.real_jacobian,x_scale='jac',
                         max_nfev=args.max_nfev,ftol=1e-13,xtol=1e-13,gtol=1e-13)
    parameters=result.x[:model.n]+1j*result.x[model.n:]
    coefficients,logs=model.unpack(parameters)
    f,j=model.evaluate(parameters)
    report={'anchor_index':args.index,'anchor_value':args.value,'max_nfev':args.max_nfev,
            'nfev':result.nfev,'status':result.status,'message':result.message,
            'residual_norm':float(np.linalg.norm(f)),'independent_check':model.independent_check(parameters),
            'coefficients_real':coefficients[:125].real.tolist(),'coefficients_imag':coefficients[:125].imag.tolist(),
            'target_logs_real':logs.real.tolist(),'target_logs_imag':logs.imag.tolist(),
            'jacobian_singular_values':np.linalg.svd(j,compute_uv=False).tolist(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
            'exact_solution_found':False,'improves_omega':False}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items()if not isinstance(v,list)},flush=True)
