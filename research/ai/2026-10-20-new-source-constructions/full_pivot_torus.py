"""Direct cubic numerical discovery, including a pure-shared-power stratum.

The checked target is still C(4,10) -> T4 in the recorded balanced flags.
Numerical convergence is not a certificate.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

from torus_exact import ExactModel
from pivot_torus import TorusModel


class FullModel:
    def __init__(self, pure_shared=False):
        self.exact = exact = ExactModel()
        self.fixed = set(range(5)) if pure_shared else set()
        self.active = [j for j in range(125) if j not in self.fixed]
        self.n = len(self.active) + 18
        self.wanted = np.array([wanted for terms, wanted in exact.equations])
        self.incidence = np.array([[int(column in (p,4+y,14+z)) for column in exact.columns]
                                   for p,y,z in exact.all_triples])
        self.term_rows = []
        self.terms = []
        for row,(terms,wanted) in enumerate(exact.equations):
            for term in terms:
                self.term_rows.append(row)
                self.terms.append(list(term)+[125]*(3-len(term)))
        self.term_rows = np.array(self.term_rows)
        self.terms = np.array(self.terms)

    def unpack(self, parameters):
        values = np.zeros(126,dtype=complex)
        values[self.active] = parameters[:len(self.active)]
        values[125] = 1
        return values,parameters[len(self.active):]

    def evaluate(self, parameters):
        values,logs = self.unpack(parameters)
        incidence = self.incidence
        a,b,c = self.terms.T
        coefficients = np.zeros(121,complex)
        np.add.at(coefficients,self.term_rows,values[a]*values[b]*values[c])
        derivative = np.zeros((121,126),complex)
        for coordinate,product in [(a,values[b]*values[c]),(b,values[a]*values[c]),(c,values[a]*values[b])]:
            np.add.at(derivative,(self.term_rows,coordinate),product)
        norm = np.exp(-incidence@logs)
        residual = coefficients*norm-self.wanted
        jac = np.hstack((derivative[:,self.active]*norm[:,None],
                         -incidence*(coefficients*norm)[:,None]))
        return residual,jac

    def real_residual(self, parameters):
        f,_ = self.evaluate(parameters[:self.n]+1j*parameters[self.n:])
        return np.r_[f.real,f.imag]

    def real_jacobian(self, parameters):
        _,j = self.evaluate(parameters[:self.n]+1j*parameters[self.n:])
        return np.block([[j.real,-j.imag],[j.imag,j.real]])

    def independent_check(self, parameters):
        v,logs = self.unpack(parameters)
        exact = self.exact
        values = np.zeros(len(exact.system.keys),complex)
        for index,value in exact.system.constant_values.items(): values[index] = complex(value)
        values[exact.variables] = v[:125]
        matrices = [np.zeros((4,4),complex),np.zeros((10,10),complex),np.zeros((10,13),complex)]
        for (leg,row,drop),value in zip(exact.system.keys,values):
            degree = exact.system.degrees[leg][row]
            column = degree-drop if leg<2 else 12-degree+drop
            matrices[leg][row,column] = value
        scalars = np.ones(24,complex);scalars[exact.columns] = np.exp(logs)
        for matrix,scale in zip(matrices,[scalars[:4],scalars[4:14],scalars[14:]]): matrix /= scale[:,None]
        a,b,c = matrices
        products = np.array([[np.convolve(a[p],b[y])for y in range(10)]for p in range(4)])
        tensor = np.einsum('pyk,zk->pyz',products,c)
        residual = [tensor[p,y,z]-wanted for (p,y,z),wanted in zip(exact.all_triples,self.wanted)]
        return {'nonpositive_coefficients_checked':121,'residual_norm':float(np.linalg.norm(residual)),
                'max_abs_residual':float(np.max(np.abs(residual))),
                'minimum_row_scale_magnitude':float(np.min(abs(scalars))),
                'full_tensor_max_abs':float(np.max(abs(tensor)))}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--pure-shared',action='store_true')
    p.add_argument('--complex',action='store_true')
    p.add_argument('--seed',type=int,default=20261021)
    p.add_argument('--max-nfev',type=int,default=2000)
    args=p.parse_args()
    source = json.loads(args.input.read_text())
    best=min(source['records'],key=lambda r:r['normalized_coefficient_check']['nonpositive_residual_norm'])
    v=np.array(best['real_parameters'])+1j*np.array(best['imag_parameters'])
    torus=TorusModel();_,_,values=torus.evaluate(v)
    model=FullModel(args.pure_shared)
    parameters=np.r_[values[model.exact.variables][model.active],v[57:]]
    if args.complex:
        rng=np.random.default_rng(args.seed)
        parameters += 0.01j*rng.normal(size=model.n)
        initial=np.r_[parameters.real,parameters.imag]
        residual,jacobian=model.real_residual,model.real_jacobian
    else:
        initial=parameters.real
        residual=lambda x:model.evaluate(x)[0].real
        jacobian=lambda x:model.evaluate(x)[1].real
    rng=np.random.default_rng(args.seed)
    direction=rng.normal(size=len(initial));direction/=np.linalg.norm(direction)
    step=1e-6
    derivative_error=float(np.max(abs((residual(initial+step*direction)-residual(initial-step*direction))/(2*step)-jacobian(initial)@direction)))
    if derivative_error>2e-5:raise ArithmeticError('Jacobian directional control failed')
    result=least_squares(residual,initial,jac=jacobian,x_scale='jac',max_nfev=args.max_nfev,
                         ftol=1e-13,xtol=1e-13,gtol=1e-13)
    parameters=result.x[:model.n]+1j*result.x[model.n:] if args.complex else result.x.astype(complex)
    coefficients,logs=model.unpack(parameters)
    f,j=model.evaluate(parameters)
    report={'pure_shared':args.pure_shared,'complex':args.complex,'seed':args.seed,
            'max_nfev':args.max_nfev,'nfev':result.nfev,'status':result.status,'message':result.message,
            'residual_norm':float(np.linalg.norm(f)),'independent_check':model.independent_check(parameters),
            'coefficients_real':coefficients[:125].real.tolist(),'coefficients_imag':coefficients[:125].imag.tolist(),
            'target_logs_real':logs.real.tolist(),'target_logs_imag':logs.imag.tolist(),
            'jacobian_singular_values':np.linalg.svd(j,compute_uv=False).tolist(),
            'jacobian_directional_error':derivative_error,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
            'exact_solution_found':False,'improves_omega':False}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items()if not isinstance(v,list)},flush=True)


if __name__=='__main__':main()
