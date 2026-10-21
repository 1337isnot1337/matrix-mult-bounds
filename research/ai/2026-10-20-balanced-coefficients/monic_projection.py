"""Restricted monic complex discovery; numerical outcomes are not certificates."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import numpy as np
import scipy
from scipy.optimize import least_squares

PACKAGE = Path(__file__).resolve().parents[1]/'2026-10-20-singular-flags'
sys.path.insert(0, str(PACKAGE))
from flag_fit import Model, unpack
from complex_projection import ComplexModel


class MonicModel(ComplexModel):
    def solve(self, x):
        model = self.model
        m, B = model.m, model.B
        n, width = len(model.points), B+m-1
        full = model.template.copy()
        full[self.free] = x
        A, Y, Z = unpack(full, m, B)
        products = np.array([[np.convolve(A[p], Y[y]) for y in range(n)] for p in range(m)])
        blocks, residuals = [], []
        for z in range(n):
            ps, ys = np.nonzero(model.mask[:, :, z])
            ks = np.arange(model.z_minimum[z], width)
            D = products[ps, ys][:, ks]
            target = model.target[ps, ys, z]-D[:, 0]
            inverse = np.linalg.pinv(D[:, 1:], rcond=1e-12)
            c = np.r_[1, inverse@target]
            pinv = np.vstack([np.zeros((1, len(ps)), dtype=complex), inverse])
            residual = D@c-model.target[ps, ys, z]
            Z[z, ks] = c
            blocks.append((ps, ys, ks, D, pinv, c, residual))
            residuals.append(residual)
        return np.concatenate(residuals), full, blocks


def make_model(m, eta, beta=1):
    B = m*(m+1)//2
    model = Model(m, B, eta, beta)
    model.template = model.template.astype(complex)
    A, Y, Z = unpack(model.template, m, B)
    pivots = []
    for p in range(m):
        A[p, m-1-p] = 1
        pivots.append(p*m+m-1-p)
    for y, degree in enumerate(model.y_degree):
        Y[y, degree] = 1
        pivots.append(m*m+y*B+degree)
    for z, degree in enumerate(model.z_minimum):
        Z[z, degree] = 1
        pivots.append(m*m+len(model.points)*B+z*(B+m-1)+degree)
    model.free = np.array([i for i in model.free if i not in pivots], dtype=int)
    return model, MonicModel(model)


def calibrate(rng):
    model, vm = make_model(2, [0, 3])
    full = np.r_[np.array([[0, 1], [1, 0]]).ravel(),
                 np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]).ravel(),
                 np.array([[1, 1, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]]).ravel()]
    control = np.linalg.norm(vm.solve(full[vm.free])[0])
    if control > 1e-12:
        raise ArithmeticError('known exact monic control failed')
    model, vm = make_model(3, [0, 7, 14])
    x = .2*rng.normal(size=2*len(vm.free))
    direction = rng.normal(size=len(x)); direction /= np.linalg.norm(direction)
    h = 1e-6
    difference = (vm.residual_real(x+h*direction)-vm.residual_real(x-h*direction))/(2*h)
    error = float(np.max(np.abs(difference-vm.jacobian_real(x)@direction)))
    if error > 2e-5:
        raise ArithmeticError('monic variable-projection Jacobian failed')
    return {'known_control_residual':float(control), 'jacobian_directional_error':error}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--starts', type=int, default=4)
    parser.add_argument('--max-nfev', type=int, default=600)
    parser.add_argument('--bound', type=float, default=20)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    seed = args.seed if args.seed is not None else int.from_bytes(os.urandom(8), 'big')
    rng = np.random.default_rng(seed)
    controls = calibrate(rng)
    print('seed', seed, 'controls', controls, flush=True)
    model, vm = make_model(4, [0, 201, 403, 607], 100)
    reports = []
    for start in range(args.starts):
        initial = .2*rng.normal(size=2*len(vm.free))
        calls = [0]; best = [float('inf'), None]
        def residual(x):
            value = vm.residual_real(x)
            relative = float(np.linalg.norm(value)/model.denominator)
            calls[0] += 1
            if relative < best[0]: best[:] = relative, x.copy()
            if calls[0]%100 == 1:
                print('start', start, 'call', calls[0], 'best', best[0], flush=True)
            return value
        result = least_squares(residual, initial, jac=vm.jacobian_real, x_scale='jac',
                               bounds=(-args.bound, args.bound), max_nfev=args.max_nfev,
                               ftol=1e-12, xtol=1e-12, gtol=1e-12)
        _, full, _ = vm.solve(vm.complex_x(best[1]))
        matrices = unpack(full, 4, 10)
        report = {'index':start, 'nfev':result.nfev, 'status':result.status,
                  'message':result.message, 'best_relative_residual':best[0],
                  'max_abs_coefficient':float(max(np.max(np.abs(M)) for M in matrices))}
        for key, matrix in zip(['A', 'B', 'C'], matrices):
            report[key+'_real'] = matrix.real.tolist()
            report[key+'_imag'] = matrix.imag.tolist()
        reports.append(report)
        data = {'m':4, 'B':10, 'eta':[0, 201, 403, 607], 'beta':100,
                'all_pivots_fixed_to_one':True, 'ansatz_is_lossless':False,
                'seed':seed, 'seed_origin':'provided' if args.seed is not None else 'os.urandom(8)',
                'max_nfev':args.max_nfev, 'input_component_bound':args.bound,
                'complex_input_parameters':len(vm.free), 'complex_output_parameters':75,
                'controls':controls, 'reports':reports, 'certified_degeneration':False,
                'numpy_version':np.__version__, 'scipy_version':scipy.__version__,
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'imported_source_sha256':{name:hashlib.sha256((PACKAGE/name).read_bytes()).hexdigest()
                    for name in ['complex_projection.py', 'variable_projection.py', 'flag_fit.py',
                                 'flag_obstruction.py', 'numerical_common.py']}}
        args.output.write_text(json.dumps(data, indent=2)+'\n')
        print('completed', start, 'best', best[0], flush=True)
