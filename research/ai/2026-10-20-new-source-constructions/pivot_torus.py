"""Nonmonic balanced-flag discovery via target diagonal equivalence.

The predecessor's monic elimination is reused without changing archived code.
Numerical residuals are discovery data, never degeneration certificates.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import least_squares
import sympy as sp
from target_orbit import incidence_data

PREDECESSOR = Path(__file__).resolve().parents[1] / "2026-10-20-balanced-coefficients"
sys.path.insert(0, str(PREDECESSOR))
from coefficient_system import System
from polynomial_pilot import PolynomialModel


class TorusModel(PolynomialModel):
    def __init__(self):
        super().__init__(System())
        self.nfree = self.n
        targets, matrix, columns, relations = incidence_data(self.system)
        self.target_terms = targets
        self.target_columns = columns
        self.relations = [[int(v) for v in relation] for relation in relations]
        self.n = self.nfree + len(columns)
        for level in self.levels:
            incidence = np.zeros((len(level["constraints"]), len(columns)))
            for row, (p, y, z, wanted) in enumerate(level["constraints"]):
                incidence[row] = [int(column in (p, 4+y, 14+z)) for column in columns]
            level["torus_incidence"] = incidence

    def evaluate(self, parameters):
        free = parameters[:self.nfree]
        logarithms = parameters[self.nfree:]
        system = self.system
        values = np.zeros(len(system.keys), dtype=complex)
        jac = np.zeros((len(values), self.n), dtype=complex)
        for index, value in system.constant_values.items():
            values[index] = complex(value)
        values[system.free] = free
        jac[np.ix_(system.free, range(self.nfree))] = np.eye(self.nfree)
        residuals, derivatives = [], []
        for level in self.levels:
            count = len(level["constraints"])
            if not count:
                continue
            a, b, c = level["term_indices"].T
            lower = np.zeros(count, dtype=complex)
            lower_jac = np.zeros((count, self.n), dtype=complex)
            np.add.at(lower, level["term_rows"], values[a]*values[b]*values[c])
            derivative = (jac[a]*(values[b]*values[c])[:, None]
                          + jac[b]*(values[a]*values[c])[:, None]
                          + jac[c]*(values[a]*values[b])[:, None])
            np.add.at(lower_jac, level["term_rows"], derivative)
            target = level["target"] * np.exp(level["torus_incidence"] @ logarithms)
            target_jac = np.zeros((count, self.n), dtype=complex)
            target_jac[:, self.nfree:] = target[:, None] * level["torus_incidence"]
            matrix = level["M"]
            columns = level["free_columns"]
            indices = level["free_indices"]
            rhs = target - lower - matrix[:, columns] @ values[indices]
            rhs_jac = target_jac - lower_jac - matrix[:, columns] @ jac[indices]
            pivot_indices = [level["variables"][j] for j in level["pivots"]]
            values[pivot_indices] = level["I"] @ rhs[level["rows"]]
            jac[pivot_indices] = level["I"] @ rhs_jac[level["rows"]]
            remaining = level["remaining_rows"]
            residual = (matrix[remaining] @ values[level["variables"]]
                        + lower[remaining] - target[remaining])
            derivative = (matrix[remaining] @ jac[level["variables"]]
                          + lower_jac[remaining] - target_jac[remaining])
            normalization = np.exp(-level["torus_incidence"][remaining] @ logarithms)
            derivative[:, self.nfree:] -= residual[:, None] * level["torus_incidence"][remaining]
            residuals.append(residual * normalization)
            derivatives.append(derivative * normalization[:, None])
        return np.concatenate(residuals), np.vstack(derivatives), values

    def reconstructed_matrices(self, parameters):
        _, _, values = self.evaluate(parameters)
        matrices = [np.zeros((4, 4), complex), np.zeros((10, 10), complex),
                    np.zeros((10, 13), complex)]
        for (leg, row, drop), value in zip(self.system.keys, values):
            degree = self.system.degrees[leg][row]
            column = degree-drop if leg < 2 else 12-degree+drop
            matrices[leg][row, column] = value
        scalars = np.ones(24, complex)
        scalars[self.target_columns] = np.exp(parameters[self.nfree:])
        for matrix, row_scalars in zip(matrices, (scalars[:4], scalars[4:14], scalars[14:])):
            matrix /= row_scalars[:, None]
        return matrices

    def full_coefficient_check(self, parameters):
        a, b, c = self.reconstructed_matrices(parameters)
        products = np.array([[np.convolve(a[p], b[y]) for y in range(10)] for p in range(4)])
        coefficients = np.einsum("pyk,zk->pyz", products, c)
        residuals = []
        for constraints in self.system.constraints.values():
            for p, y, z, wanted in constraints:
                residuals.append(coefficients[p, y, z] - wanted)
        return {"nonpositive_coefficients_checked": len(residuals),
                "nonpositive_residual_norm": float(np.linalg.norm(residuals)),
                "nonpositive_max_abs_residual": float(np.max(np.abs(residuals))),
                "full_coefficient_max_abs": float(np.max(np.abs(coefficients))),
                "minimum_pivot_magnitude": float(min(abs(matrix[row, self.system.degrees[leg][row]
                     if leg<2 else 12-self.system.degrees[leg][row]])
                     for leg, matrix in enumerate((a,b,c)) for row in range(len(matrix))))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261020)
    parser.add_argument("--starts", type=int, default=4)
    parser.add_argument("--max-nfev", type=int, default=1200)
    parser.add_argument("--free-bound", type=float, default=3.0)
    parser.add_argument("--log-bound", type=float, default=1.0)
    parser.add_argument("--real", action="store_true")
    parser.add_argument("--input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    model = TorusModel()
    rng = np.random.default_rng(args.seed)
    x = .05*rng.normal(size=2*model.n)
    direction = rng.normal(size=len(x)); direction /= np.linalg.norm(direction)
    step = 1e-6
    error = float(np.max(np.abs((model.residual_real(x+step*direction)-model.residual_real(x-step*direction))/(2*step)
                             - model.jacobian_real(x) @ direction)))
    if error > 2e-5:
        raise ArithmeticError("analytic Jacobian failed its directional control")
    bound = np.r_[np.full(model.nfree, args.free_bound),
                  np.full(model.n-model.nfree, args.log_bound)]
    records = []
    warm = None
    if args.input:
        previous = json.loads(args.input.read_text())
        best = min(previous["records"], key=lambda record: record["normalized_coefficient_check"]["nonpositive_residual_norm"])
        warm = np.array(best["real_parameters"])+1j*np.array(best["imag_parameters"])
    for start in range(args.starts):
        initial = np.r_[.2*rng.normal(size=model.nfree), np.zeros(model.n-model.nfree)]
        if start == 0 and warm is not None:
            initial = warm.real
        if args.real:
            residual = lambda p: model.evaluate(p)[0].real
            jacobian = lambda p: model.evaluate(p)[1].real
        else:
            imaginary = warm.imag if start == 0 and warm is not None else .1*rng.normal(size=model.n)
            initial = np.r_[initial, imaginary]
            residual, jacobian = model.residual_real, model.jacobian_real
        full_bound = bound if args.real else np.r_[bound, bound]
        result = least_squares(residual, initial, jac=jacobian, x_scale="jac",
                               bounds=(-full_bound, full_bound), max_nfev=args.max_nfev,
                               ftol=1e-12, xtol=1e-12, gtol=1e-12)
        parameters = result.x if args.real else result.x[:model.n]+1j*result.x[model.n:]
        record = {"start": start, "nfev": result.nfev, "status": result.status,
                  "message": result.message, "residual_norm": float(np.linalg.norm(result.fun)),
                  "real_parameters": parameters.real.tolist(),
                  "imag_parameters": parameters.imag.tolist(),
                  "normalized_coefficient_check": model.full_coefficient_check(parameters)}
        records.append(record)
        print({k:v for k,v in record.items() if not k.endswith("parameters")}, flush=True)
        data = {"source": "C(4,10)", "target": "T4", "base_commit": "9a4ee3d05939d88730045877a6945165845f0398",
                "eta": [0,201,403,607], "beta": 100, "monic_free_parameters": model.nfree,
                "target_torus_parameters": model.n-model.nfree, "polynomial_residuals": 53,
                "target_torus_columns": model.target_columns, "target_relations": model.relations,
                "seed": args.seed, "max_nfev": args.max_nfev, "free_bound": args.free_bound,
                "log_bound": args.log_bound, "real_only": args.real,
                "residuals_normalized_to_unit_target": True,
                "jacobian_directional_error": error, "records": records,
                "exact_solution_found": False, "improves_omega": False,
                "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "predecessor_sha256": {name: hashlib.sha256((PREDECESSOR/name).read_bytes()).hexdigest()
                                         for name in ("coefficient_system.py", "polynomial_pilot.py")}}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+"\n")


if __name__ == "__main__":
    main()
