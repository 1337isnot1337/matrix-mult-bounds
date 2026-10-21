"""Finite bounded higher-order graded Laurent coefficient discovery.

Maps have degrees 0..order, with a common epsilon^-order factor.
Every coefficient below order is constrained to zero and coefficient
order to the complete target. Residuals never certify a degeneration.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path
import time


SPEC = importlib.util.spec_from_file_location("paired_higher_jet_dependency",
                                             Path(__file__).with_name("laurent_search.py"))
JET = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(JET)


class HigherJetProblem:
    def __init__(self, a=3, order=2):
        import numpy as np
        self.a, self.order = a, order
        self.sg, self.tg, self.source, self.target = JET.problem(a)
        self.keys = [(k, w) for k in range(3) for w in sorted(self.tg[k])]
        self.indices, self.shapes = {}, {}
        offset = 0
        for k, w in self.keys:
            shape = (order+1, len(self.tg[k][w]), len(self.sg[k][w]))
            size = int(np.prod(shape))
            self.indices[k, w] = np.arange(offset, offset+size).reshape(shape)
            self.shapes[k, w] = shape
            offset += size
        self.parameters = offset
        offset = 0
        self.rows = {}
        for w, tensor in self.target.items():
            size = (order+1)*tensor.size
            self.rows[w] = np.arange(offset, offset+size).reshape((order+1, *tensor.shape))
            offset += size
        self.coefficient_rows = offset
        self.gauge_rows = 3*(order+1)
        self.equations = offset+self.gauge_rows
        self.target_norm = sum(float((t*t).sum()) for t in self.target.values())**0.5
        self.levels = {d: [x for x in product(range(order+1), repeat=3) if sum(x) == d]
                       for d in range(order+1)}
        self.last_x = self.last_value = None

    def pack(self, maps):
        import numpy as np
        x = np.zeros(self.parameters)
        for k, w in self.keys:
            x[self.indices[k, w]] = maps[k][w]
        return x

    def unpack(self, x):
        maps = [{}, {}, {}]
        for k, w in self.keys:
            maps[k][w] = x[self.indices[k, w]]
        return maps

    def value_and_jacobian(self, x):
        import numpy as np
        if self.last_x is not None and np.array_equal(x, self.last_x):
            return self.last_value
        maps = self.unpack(x)
        residual = np.zeros(self.equations)
        jacobian = np.zeros((self.equations, self.parameters))
        for w, source in self.source.items():
            local = [maps[k][w[k]] for k in range(3)]
            for degree in range(self.order+1):
                value = sum(np.einsum("is,jt,ku,stu->ijk", local[0][levels[0]],
                           local[1][levels[1]], local[2][levels[2]], source, optimize=True)
                            for levels in self.levels[degree])
                if degree == self.order:
                    value -= self.target[w]
                residual[self.rows[w][degree]] = value
            for axis in range(3):
                other = [k for k in range(3) if k != axis]
                transposed = np.transpose(source, (axis, *other))
                left, right = (local[k] for k in other)
                environments = []
                for degree in range(self.order+1):
                    u = sum(np.einsum("jt,ku,stu->sjk", left[d], right[degree-d],
                                      transposed, optimize=True) for d in range(degree+1))
                    environments.append(u.reshape(u.shape[0], -1).T)
                for row in range(len(self.tg[axis][w[axis]])):
                    for degree in range(self.order+1):
                        rows = np.take(self.rows[w][degree], row, axis=axis).ravel()
                        for level in range(degree+1):
                            columns = self.indices[axis, w[axis]][level, row]
                            jacobian[np.ix_(rows, columns)] = environments[degree-level]
        for axis in range(3):
            start = self.coefficient_rows+axis*(self.order+1)
            residual[start] = sum(float((m[0]*m[0]).sum()) for m in maps[axis].values())-1
            for w, m in maps[axis].items():
                jacobian[start, self.indices[axis, w][0]] = 2*m[0]
            for degree in range(1, self.order+1):
                row = start+degree
                residual[row] = sum(float((m[0]*m[degree]).sum()) for m in maps[axis].values())
                for w, m in maps[axis].items():
                    jacobian[row, self.indices[axis, w][0]] = m[degree]
                    jacobian[row, self.indices[axis, w][degree]] = m[0]
        self.last_x = x.copy()
        self.last_value = residual, jacobian
        return self.last_value

    def residual(self, x):
        return self.value_and_jacobian(x)[0]

    def jacobian(self, x):
        return self.value_and_jacobian(x)[1]

    def initial(self, seed, bound, start=None):
        import numpy as np
        rng = np.random.default_rng(seed)
        if start is None:
            maps = [{w: rng.normal(size=self.shapes[k, w]) for w in self.tg[k]} for k in range(3)]
            for axis in maps:
                for degree in range(self.order+1):
                    norm = sum(float((m[degree]*m[degree]).sum()) for m in axis.values())**0.5
                    for m in axis.values():
                        m[degree] *= (1 if degree == 0 else 3)/norm
        else:
            first_order = JET.load_checkpoint(start, self.tg)
            maps = [{w: np.zeros(self.shapes[k, w]) for w in self.tg[k]} for k in range(3)]
            for k, w in self.keys:
                maps[k][w][0] = first_order[k][w][0]
                maps[k][w][self.order] = first_order[k][w][1]
                for degree in range(1, self.order):
                    maps[k][w][degree] = rng.normal(size=maps[k][w][degree].shape)*0.05
            norms = [sum(float((m[0]*m[0]).sum()) for m in axis.values())**0.5 for axis in maps]
            epsilon_scale = float(np.prod(norms))**(1/self.order)
            for axis, norm in zip(maps, norms):
                for m in axis.values():
                    for degree in range(self.order+1):
                        m[degree] *= epsilon_scale**degree/norm
        # These projections choose an initial point, not an equivalence
        # transformation for the tensor at an approximate solution.
        for axis in maps:
            for degree in range(1, self.order+1):
                projection = sum(float((m[0]*m[degree]).sum()) for m in axis.values())
                for m in axis.values():
                    m[degree] -= projection*m[0]
        return np.clip(self.pack(maps), -0.99*bound, 0.99*bound)

    def diagnostics(self, x):
        import numpy as np
        residual = self.residual(x)
        norms = [sum(float((residual[self.rows[w][degree]]**2).sum()) for w in self.target)**0.5
                 for degree in range(self.order+1)]
        maps = self.unpack(x)
        return {"pole_coefficient_norms": norms[:-1], "target_relative_error": norms[-1]/self.target_norm,
                "combined_coefficient_relative_error": sum(v*v for v in norms)**0.5/self.target_norm,
                "maximum_absolute_coefficient_error": float(np.max(np.abs(residual[:self.coefficient_rows]))),
                "maximum_absolute_gauge_error": float(np.max(np.abs(residual[self.coefficient_rows:]))),
                "map_norms_by_axis_and_level": [[sum(float((m[d]*m[d]).sum()) for m in axis.values())**0.5
                                                for d in range(self.order+1)] for axis in maps],
                "maximum_absolute_parameter": float(np.max(np.abs(x)))}


def rational_coefficients(source_terms, maps):
    """Check every coefficient, including all positive powers of epsilon."""
    shape = [len(axis[0]) for axis in maps]
    levels = [len(axis) for axis in maps]
    result = [defaultdict(Fraction) for _ in range(sum(levels)-2)]
    for source in source_terms:
        for coefficient_levels in product(*(range(n) for n in levels)):
            degree = sum(coefficient_levels)
            for target in product(*(range(n) for n in shape)):
                value = Fraction(1)
                for axis in range(3):
                    value *= Fraction(maps[axis][coefficient_levels[axis]][target[axis]][source[axis]])
                if value:
                    result[degree][target] += value
    return [{key: value for key, value in degree.items() if value} for degree in result]


def exact_controls():
    # 1/(2 e^2) [ (e0+e e1)^3 + (e0-e e1)^3 - 2 e0^3 ].
    a = [[[Fraction(1, 2), Fraction(1, 2), -1], [0, 0, 0]],
         [[0, 0, 0], [Fraction(1, 2), Fraction(-1, 2), 0]], [[0, 0, 0], [0, 0, 0]]]
    b = [[[1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, -1, 0]], [[0, 0, 0], [0, 0, 0]]]
    maps = [a, b, b]
    source = [(i, i, i) for i in range(3)]
    actual = rational_coefficients(source, maps)
    target = {(1, 1, 0): 1, (1, 0, 1): 1, (0, 1, 1): 1}
    if actual != [{}, {}, target, {}, {}, {}, {}]:
        raise ArithmeticError("The exact second-order Laurent control failed")
    corrupt = [[[[value for value in row] for row in level] for level in axis] for axis in maps]
    corrupt[0][0][0][2] = -2
    corrupt_result = rational_coefficients(source, corrupt)
    if not corrupt_result[0] or corrupt_result[2] != target:
        raise ArithmeticError("The second-order pole negative control failed")
    return {"exact_second_order_control_passed": True,
            "nonzero_coefficients_by_degree": [len(x) for x in actual],
            "pole_detected_despite_correct_target_coefficient": True}


def controls():
    import numpy as np
    exact = exact_controls()
    problem = HigherJetProblem(3, 2)
    x = problem.initial(82013, 10)
    direction = np.random.default_rng(82014).normal(size=problem.parameters)
    direction /= np.linalg.norm(direction)
    analytic = problem.jacobian(x) @ direction
    step = 1e-5
    numerical = (problem.residual(x+step*direction)-problem.residual(x-step*direction))/(2*step)
    error = float(np.max(np.abs(analytic-numerical)))
    if error >= 1e-7:
        raise ArithmeticError("The higher-jet analytic Jacobian failed its directional check")
    return {**exact,
            "parameters": problem.parameters, "coefficient_equations": problem.coefficient_rows,
            "gauge_equations": problem.gauge_rows,
            "directional_jacobian_check_seed": 82013, "directional_step": step,
            "maximum_directional_derivative_error": error,
            "scope": "Exact coefficient verifier and numerical derivative controls; no target construction."}


def search(a, order, seed, bound, evaluations, start=None, checkpoint=None):
    import numpy as np
    import scipy
    from scipy.optimize import least_squares
    problem = HigherJetProblem(a, order)
    x = problem.initial(seed, bound, start)
    initial = problem.diagnostics(x)
    start_time = time.monotonic()
    result = least_squares(problem.residual, x, jac=problem.jacobian, bounds=(-bound, bound),
                           max_nfev=evaluations, ftol=1e-11, xtol=1e-11, gtol=1e-11,
                           method="trf", x_scale="jac")
    elapsed = time.monotonic()-start_time
    if checkpoint is not None:
        JET.save_checkpoint(checkpoint, problem.unpack(result.x))
    return {"a": a, "order": order, "seed": seed, "coefficient_bound": bound,
            "maximum_function_evaluations": evaluations, "function_evaluations": result.nfev,
            "jacobian_evaluations": result.njev, "elapsed_seconds": elapsed,
            "start": str(start) if start is not None else "independent random start",
            "numpy_version": np.__version__, "scipy_version": scipy.__version__,
            "parameters": problem.parameters, "coefficient_equations": problem.coefficient_rows,
            "gauge_equations": problem.gauge_rows, "initial": initial,
            "final": problem.diagnostics(result.x), "solver_status": int(result.status),
            "solver_message": result.message, "solver_optimality": float(result.optimality),
            "exact_coefficient_certificate": False, "construction_supplied": False, "improves_omega": False,
            "scope": "Finite bounded real grading-preserving jet search; no existence or nonexistence conclusion."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, default=3)
    parser.add_argument("--order", type=int, default=2)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--evaluations", type=int, default=250)
    parser.add_argument("--bound", type=float, default=10)
    parser.add_argument("--start", type=Path)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = (controls() if args.controls else search(args.a, args.order, args.seed, args.bound,
                                                    args.evaluations, args.start, args.checkpoint))
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
