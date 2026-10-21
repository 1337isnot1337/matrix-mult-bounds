"""Bounded complex discovery in the new polynomial-flag chamber.

All nonpositive coefficients are checked separately. A small residual is
not an exact construction or a distance certificate.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

from chamber_system import ChamberModel
from full_pivot_torus import FullModel
from torus_exact import ExactModel


class Model(FullModel):
    def __init__(self, eta, beta):
        self.exact = exact = ChamberModel(eta,beta)
        self.fixed = set()
        self.active = list(range(len(exact.variables)))
        self.n = len(self.active)+len(exact.columns)
        self.wanted = np.array([wanted for _,wanted in exact.equations])
        self.incidence = np.array([[int(column in (p,4+y,14+z)) for column in exact.columns]
                                  for p,y,z in exact.all_triples])
        term_rows,terms = [],[]
        for row,(monomials,_) in enumerate(exact.equations):
            for term in monomials:
                term_rows.append(row);terms.append(list(term)+[125]*(3-len(term)))
        self.term_rows = np.array(term_rows)
        self.terms = np.array(terms)

    def evaluate(self, parameters):
        values,logs = self.unpack(parameters)
        a,b,c = self.terms.T
        rows = len(self.exact.equations)
        coefficients = np.zeros(rows,complex)
        np.add.at(coefficients,self.term_rows,values[a]*values[b]*values[c])
        derivative = np.zeros((rows,126),complex)
        for coordinate,product in [(a,values[b]*values[c]),(b,values[a]*values[c]),(c,values[a]*values[b])]:
            np.add.at(derivative,(self.term_rows,coordinate),product)
        scale = np.exp(-self.incidence@logs)
        residual = coefficients*scale-self.wanted
        jac = np.hstack((derivative[:,self.active]*scale[:,None],
                         -self.incidence*(coefficients*scale)[:,None]))
        return residual,jac

    def independent_check(self, parameters):
        result = super().independent_check(parameters)
        result['nonpositive_coefficients_checked'] = len(self.exact.equations)
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eta',default='0,301,628,844')
    parser.add_argument('--beta',type=int,default=100)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--seed',type=int,default=20261021)
    parser.add_argument('--max-nfev',type=int,default=2000)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    previous = ExactModel()
    model = Model(list(map(int,args.eta.split(','))),args.beta)
    raw = np.array(source['coefficients_real'])+1j*np.array(source['coefficients_imag'])
    old = np.zeros(len(previous.system.keys),complex)
    for index,value in previous.system.constant_values.items():old[index] = complex(value)
    old[previous.variables] = raw
    lookup = {}
    for (leg,row,drop),value in zip(previous.system.keys,old):
        degree = previous.system.degrees[leg][row]
        column = degree-drop if leg<2 else 12-degree+drop
        lookup[leg,row,column] = value
    free = []
    for index in model.exact.variables:
        leg,row,drop = model.exact.system.keys[index]
        degree = model.exact.system.degrees[leg][row]
        column = degree-drop if leg<2 else 12-degree+drop
        free.append(lookup.get((leg,row,column),0))
    logs = np.array(source['target_logs_real'])+1j*np.array(source['target_logs_imag'])
    parameters = np.r_[free,logs]
    rng = np.random.default_rng(args.seed)
    parameters += 0.01*(rng.normal(size=model.n)+1j*rng.normal(size=model.n))
    initial = np.r_[parameters.real,parameters.imag]
    direction = rng.normal(size=len(initial));direction /= np.linalg.norm(direction)
    step = 1e-6
    derivative_error = float(np.max(abs((model.real_residual(initial+step*direction)-model.real_residual(initial-step*direction))/(2*step)
                                         -model.real_jacobian(initial)@direction)))
    if derivative_error>3e-5:
        raise ArithmeticError('independent Jacobian directional check failed')
    bounds = np.r_[np.full(125,50.),np.full(18,5.),np.full(125,50.),np.full(18,5.)]
    result = least_squares(model.real_residual,initial,jac=model.real_jacobian,
                           bounds=(-bounds,bounds),x_scale='jac',max_nfev=args.max_nfev,
                           ftol=1e-13,xtol=1e-13,gtol=1e-13)
    parameters = result.x[:model.n]+1j*result.x[model.n:]
    coefficients,logs = model.unpack(parameters)
    residual,jac = model.evaluate(parameters)
    report = {'eta':model.exact.system.eta,'beta':model.exact.system.beta,'seed':args.seed,
              'max_nfev':args.max_nfev,'nfev':result.nfev,'status':result.status,'message':result.message,
              'coefficient_component_bound':50,'target_log_component_bound':5,
              'residual_norm':float(np.linalg.norm(residual)),
              'independent_check':model.independent_check(parameters),
              'coefficients_real':coefficients[:125].real.tolist(),'coefficients_imag':coefficients[:125].imag.tolist(),
              'target_logs_real':logs.real.tolist(),'target_logs_imag':logs.imag.tolist(),
              'jacobian_singular_values':np.linalg.svd(jac,compute_uv=False).tolist(),
              'jacobian_directional_error':derivative_error,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
              'exact_solution_found':False,'improves_omega':False}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items()if not isinstance(v,list)},flush=True)


if __name__ == '__main__':
    main()
