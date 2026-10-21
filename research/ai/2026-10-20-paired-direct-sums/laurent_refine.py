"""Bounded discovery for every first-order Laurent coefficient equation.

The additional gauge equations fix each leading norm to one and each
leading/derivative inner product to zero.  They do not replace any tensor
coefficient equations.  Coefficient bounds make this an explicitly limited
real numerical search; solver termination is not a mathematical certificate.
"""
import argparse
import importlib.util
from itertools import product
import json
from pathlib import Path
import time


SPEC = importlib.util.spec_from_file_location("paired_laurent_discovery",
                                             Path(__file__).with_name("laurent_search.py"))
JET = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(JET)


class CoefficientProblem:
    def __init__(self, a):
        import numpy as np
        self.a = a
        self.sg, self.tg, self.source, self.target = JET.problem(a)
        self.keys = [(k, w) for k in range(3) for w in sorted(self.tg[k])]
        self.shape, self.indices = {}, {}
        offset = 0
        for k, w in self.keys:
            shape = (2, len(self.tg[k][w]), len(self.sg[k][w]))
            size = int(np.prod(shape))
            self.shape[k, w] = shape
            self.indices[k, w] = np.arange(offset, offset+size).reshape(shape)
            offset += size
        self.parameters = offset
        self.rows = {}
        offset = 0
        for w, target in self.target.items():
            size = target.size
            self.rows[w] = np.arange(offset, offset+2*size).reshape((2, *target.shape))
            offset += 2*size
        self.coefficient_rows = offset
        self.equations = offset+6
        self.target_norm = sum(float((x*x).sum()) for x in self.target.values())**0.5
        self.last_x = self.last_value = None

    def unpack(self, x):
        maps = [{}, {}, {}]
        for k, w in self.keys:
            maps[k][w] = x[self.indices[k, w]]
        return maps

    def pack(self, maps):
        import numpy as np
        x = np.zeros(self.parameters)
        for k, w in self.keys:
            x[self.indices[k, w]] = maps[k][w]
        return x

    def value_and_jacobian(self, x):
        import numpy as np
        if self.last_x is not None and np.array_equal(x, self.last_x):
            return self.last_value
        maps = self.unpack(x)
        residual = np.zeros(self.equations)
        jacobian = np.zeros((self.equations, self.parameters))
        for w, source in self.source.items():
            local = [maps[k][w[k]] for k in range(3)]
            for degree in (0, 1):
                value = sum(np.einsum("is,jt,ku,stu->ijk", local[0][levels[0]],
                           local[1][levels[1]], local[2][levels[2]], source, optimize=True)
                            for levels in product((0, 1), repeat=3) if sum(levels) == degree)
                if degree == 1:
                    value -= self.target[w]
                residual[self.rows[w][degree]] = value
            for axis in range(3):
                other = [k for k in range(3) if k != axis]
                transposed = np.transpose(source, (axis, *other))
                left, right = (local[k] for k in other)
                u0 = np.einsum("jt,ku,stu->sjk", left[0], right[0], transposed, optimize=True)
                u1 = (np.einsum("jt,ku,stu->sjk", left[1], right[0], transposed, optimize=True)
                      +np.einsum("jt,ku,stu->sjk", left[0], right[1], transposed, optimize=True))
                u0 = u0.reshape(u0.shape[0], -1).T
                u1 = u1.reshape(u1.shape[0], -1).T
                for row in range(len(self.tg[axis][w[axis]])):
                    r0 = np.take(self.rows[w][0], row, axis=axis).ravel()
                    r1 = np.take(self.rows[w][1], row, axis=axis).ravel()
                    leading_columns, derivative_columns = self.indices[axis, w[axis]][:, row]
                    jacobian[np.ix_(r0, leading_columns)] = u0
                    jacobian[np.ix_(r1, leading_columns)] = u1
                    jacobian[np.ix_(r1, derivative_columns)] = u0
        for axis in range(3):
            rnorm, rdot = self.coefficient_rows+2*axis, self.coefficient_rows+2*axis+1
            residual[rnorm] = sum(float((m[0]*m[0]).sum()) for m in maps[axis].values())-1
            residual[rdot] = sum(float((m[0]*m[1]).sum()) for m in maps[axis].values())
            for w, m in maps[axis].items():
                leading_columns, derivative_columns = self.indices[axis, w]
                jacobian[rnorm, leading_columns] = 2*m[0]
                jacobian[rdot, leading_columns] = m[1]
                jacobian[rdot, derivative_columns] = m[0]
        self.last_x = x.copy()
        self.last_value = residual, jacobian
        return self.last_value

    def residual(self, x):
        return self.value_and_jacobian(x)[0]

    def jacobian(self, x):
        return self.value_and_jacobian(x)[1]

    def random_start(self, seed, derivative_bound):
        import numpy as np
        rng = np.random.default_rng(seed)
        maps = [{w: rng.normal(size=self.shape[k, w]) for w in self.tg[k]} for k in range(3)]
        JET.normalize_leading_maps(maps)
        for axis in range(3):
            projection = sum(float((m[0]*m[1]).sum()) for m in maps[axis].values())
            for m in maps[axis].values():
                m[1] -= projection*m[0]
            derivative_size = sum(float((m[1]*m[1]).sum()) for m in maps[axis].values())**0.5
            for m in maps[axis].values():
                m[1] *= min(1, 3/max(1e-100, derivative_size))
        return np.clip(self.pack(maps), -0.99*derivative_bound, 0.99*derivative_bound)

    def diagnostics(self, x):
        import numpy as np
        residual = self.residual(x)
        leading = sum(float((residual[self.rows[w][0]]**2).sum()) for w in self.target)**0.5
        constant = sum(float((residual[self.rows[w][1]]**2).sum()) for w in self.target)**0.5
        maps = self.unpack(x)
        return {"leading_coefficient_norm": leading,
                "constant_relative_error": constant/self.target_norm,
                "combined_coefficient_relative_error": (leading**2+constant**2)**0.5/self.target_norm,
                "maximum_absolute_coefficient_error": float(np.max(np.abs(residual[:self.coefficient_rows]))),
                "maximum_absolute_gauge_error": float(np.max(np.abs(residual[self.coefficient_rows:]))),
                "first_derivative_map_norms": [sum(float((m[1]*m[1]).sum()) for m in axis.values())**0.5
                                               for axis in maps],
                "maximum_absolute_parameter": float(np.max(np.abs(x)))}


def derivative_control(a=3, seed=731):
    """An independent directional difference controls row/column ordering."""
    import numpy as np
    problem = CoefficientProblem(a)
    x = problem.random_start(seed, 10)
    direction = np.random.default_rng(seed+1).normal(size=problem.parameters)
    direction /= np.linalg.norm(direction)
    analytic = problem.jacobian(x) @ direction
    step = 1e-5
    numerical = (problem.residual(x+step*direction)-problem.residual(x-step*direction))/(2*step)
    error = float(np.max(np.abs(analytic-numerical)))
    if error >= 1e-7:
        raise ArithmeticError(f"Directional derivative discrepancy {error}")
    return {"a": a, "parameters": problem.parameters, "equations": problem.equations,
            "seed": seed, "step": step, "maximum_directional_derivative_error": error,
            "control_passed": True}


def refine(a, seed, evaluations, bound, checkpoint=None, start=None):
    import numpy as np
    import scipy
    from scipy.optimize import least_squares
    problem = CoefficientProblem(a)
    x = problem.random_start(seed, bound)
    if start is not None:
        maps = JET.load_checkpoint(start, problem.tg)
        JET.normalize_leading_maps(maps)
        for axis in maps:
            projection = sum(float((m[0]*m[1]).sum()) for m in axis.values())
            for m in axis.values():
                m[1] -= projection*m[0]
        x = np.clip(problem.pack(maps), -0.99*bound, 0.99*bound)
    initial = problem.diagnostics(x)
    start_time = time.monotonic()
    fit = least_squares(problem.residual, x, jac=problem.jacobian, bounds=(-bound, bound),
                        max_nfev=evaluations, ftol=1e-11, xtol=1e-11, gtol=1e-11,
                        method="trf", x_scale="jac")
    elapsed = time.monotonic()-start_time
    if checkpoint is not None:
        JET.save_checkpoint(checkpoint, problem.unpack(fit.x))
    return {"a": a, "seed": seed, "coefficient_bound": bound,
            "maximum_function_evaluations": evaluations, "function_evaluations": fit.nfev,
            "jacobian_evaluations": fit.njev, "elapsed_seconds": elapsed,
            "source_start": str(start) if start is not None else "independent random start",
            "parameters": problem.parameters, "coefficient_equations": problem.coefficient_rows,
            "gauge_equations": 6, "numpy_version": np.__version__, "scipy_version": scipy.__version__,
            "initial": initial, "final": problem.diagnostics(fit.x), "solver_status": int(fit.status),
            "solver_message": fit.message, "solver_optimality": float(fit.optimality),
            "method": "bounded real least squares, analytic Jacobian, full tensor and gauge equations",
            "exact_coefficient_certificate": False, "construction_supplied": False,
            "improves_omega": False,
            "scope": "Finite bounded real first-order graded jet discovery; no existence or nonexistence conclusion."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, default=3)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--evaluations", type=int, default=300)
    parser.add_argument("--bound", type=float, default=10)
    parser.add_argument("--start", type=Path)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = ({"exact_coefficients": JET.exact_controls(), "analytic_jacobian": derivative_control(args.a)}
              if args.controls else refine(args.a, args.seed, args.evaluations, args.bound,
                                            args.checkpoint, args.start))
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
