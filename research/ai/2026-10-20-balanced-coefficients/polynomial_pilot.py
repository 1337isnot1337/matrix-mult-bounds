"""Optional discovery using polynomial recurrences, without pseudoinverses."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from coefficient_system import System


class PolynomialModel:
    def __init__(self, system):
        self.system = system
        self.n = len(system.free)
        self.levels = []
        for s in system.levels:
            term_rows, terms = [], []
            for row, entries in enumerate(s['terms']):
                term_rows.extend([row]*len(entries)); terms.extend(entries)
            self.levels.append({**s, 'term_rows':np.array(term_rows, dtype=int),
                'term_indices':np.array(terms, dtype=int).reshape(-1, 3),
                'M':np.array(s['matrix']).astype(float),
                'I':np.array(s['inverse']).astype(float).reshape(len(s['pivots']), len(s['rows'])),
                'target':np.array([c[3] for c in s['constraints']])})

    def evaluate(self, free):
        system = self.system
        values = np.zeros(len(system.keys), dtype=complex)
        jac = np.zeros((len(values), self.n), dtype=complex)
        for index,value in system.constant_values.items(): values[index] = complex(value)
        values[system.free] = free
        jac[system.free] = np.eye(self.n)
        residuals, derivatives = [], []
        for s in self.levels:
            count = len(s['constraints'])
            if not count: continue
            a,b,c = s['term_indices'].T
            lower = np.zeros(count, dtype=complex)
            lower_jac = np.zeros((count, self.n), dtype=complex)
            np.add.at(lower, s['term_rows'], values[a]*values[b]*values[c])
            derivative = (jac[a]*(values[b]*values[c])[:,None]
                         +jac[b]*(values[a]*values[c])[:,None]
                         +jac[c]*(values[a]*values[b])[:,None])
            np.add.at(lower_jac, s['term_rows'], derivative)
            M = s['M']; columns = s['free_columns']; indices = s['free_indices']
            rhs = s['target']-lower-M[:,columns]@values[indices]
            rhs_jac = -lower_jac-M[:,columns]@jac[indices]
            pivot_indices = [s['variables'][j] for j in s['pivots']]
            values[pivot_indices] = s['I']@rhs[s['rows']]
            jac[pivot_indices] = s['I']@rhs_jac[s['rows']]
            remaining = s['remaining_rows']
            residuals.append(M[remaining]@values[s['variables']]+lower[remaining]-s['target'][remaining])
            derivatives.append(M[remaining]@jac[s['variables']]+lower_jac[remaining])
        return np.concatenate(residuals), np.vstack(derivatives), values

    def residual_real(self, x):
        n = len(x)//2
        residual = self.evaluate(x[:n]+1j*x[n:])[0]
        return np.r_[residual.real, residual.imag]

    def jacobian_real(self, x):
        n = len(x)//2
        jac = self.evaluate(x[:n]+1j*x[n:])[1]
        return np.block([[jac.real, -jac.imag], [jac.imag, jac.real]])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--starts', type=int, default=3)
    parser.add_argument('--max-nfev', type=int, default=800)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    seed = args.seed if args.seed is not None else int.from_bytes(os.urandom(8), 'big')
    rng = np.random.default_rng(seed)
    system = System(); model = PolynomialModel(system); n = model.n
    x = .1*rng.normal(size=2*n); direction = rng.normal(size=2*n); direction /= np.linalg.norm(direction)
    h = 1e-6
    jac_error = float(np.max(np.abs((model.residual_real(x+h*direction)-model.residual_real(x-h*direction))/(2*h)
                                   -model.jacobian_real(x)@direction)))
    if jac_error > 2e-5: raise ArithmeticError('polynomial recurrence Jacobian control failed')
    print('seed', seed, 'jacobian error', jac_error, flush=True)
    warm = None
    if args.input:
        old = json.loads(args.input.read_text())
        best = min(old['reports'], key=lambda r:r['best_relative_residual'])
        matrices = [np.array(best[k+'_real'])+1j*np.array(best[k+'_imag']) for k in ['A','B','C']]
        warm = []
        for index in system.free:
            leg,row,drop = system.keys[index]; degree = system.degrees[leg][row]
            column = degree-drop if leg < 2 else 12-degree+drop
            warm.append(matrices[leg][row,column])
        warm = np.array(warm)
    reports = []
    for start in range(args.starts):
        initial = (np.r_[warm.real, warm.imag] if start == 0 and warm is not None
                   else .2*rng.normal(size=2*n))
        calls = [0]; best = [float('inf'), None]
        def residual(x):
            value = model.residual_real(x)
            norm = float(np.linalg.norm(value)); calls[0] += 1
            if norm < best[0]: best[:] = norm, x.copy()
            if calls[0]%100 == 1: print('start', start, 'call', calls[0], 'best', best[0], flush=True)
            return value
        result = least_squares(residual, initial, jac=model.jacobian_real, x_scale='jac',
                               max_nfev=args.max_nfev, ftol=1e-12, xtol=1e-12, gtol=1e-12)
        free = best[1][:n]+1j*best[1][n:]
        _,_,values = model.evaluate(free)
        reports.append({'index':start, 'nfev':result.nfev, 'status':result.status,
                        'message':result.message, 'polynomial_residual_norm':best[0],
                        'max_abs_coefficient':float(np.max(np.abs(values))),
                        'free_real':free.real.tolist(), 'free_imag':free.imag.tolist(),
                        'coefficient_real':values.real.tolist(), 'coefficient_imag':values.imag.tolist()})
        data = {**system.summary(), 'seed':seed,
                'seed_origin':'provided' if args.seed is not None else 'os.urandom(8)',
                'max_nfev':args.max_nfev, 'reports':reports, 'jacobian_directional_error':jac_error,
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'system_source_sha256':hashlib.sha256(Path(__file__).with_name('coefficient_system.py').read_bytes()).hexdigest(),
                'warm_input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest() if args.input else None,
                'certified_degeneration':False}
        args.output.write_text(json.dumps(data, indent=2)+'\n')
        print('completed', start, 'best', best[0], flush=True)
