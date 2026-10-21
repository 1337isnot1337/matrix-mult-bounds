"""Search compression kernels through normalized slice-algebra closure.

For Q_(n,b) -> M(n,b,n), a concise target with an invertible first slice
has a normalized slice space isomorphic to M_n, represented b times.
Closure alone is insufficient: exact acceptance also requires the full
n^2-dimensional span, a one-dimensional center, and nondegenerate trace
form. Numerical searches are discovery only.
"""
import argparse
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path
import time


SPEC = importlib.util.spec_from_file_location("narrow_algebra_dependency",
                                             Path(__file__).with_name("narrow_source_search.py"))
NARROW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NARROW)


def rref(matrix):
    rows = [[Fraction(x) for x in row] for row in matrix]
    if not rows:
        return rows, []
    pivots = []
    for column in range(len(rows[0])):
        index = next((i for i in range(len(pivots), len(rows)) if rows[i][column]), None)
        if index is None:
            continue
        pivot = len(pivots)
        rows[pivot], rows[index] = rows[index], rows[pivot]
        divisor = rows[pivot][column]
        rows[pivot] = [x/divisor for x in rows[pivot]]
        for i, row in enumerate(rows):
            if i != pivot and row[column]:
                factor = row[column]
                rows[i] = [x-factor*y for x, y in zip(row, rows[pivot])]
        pivots.append(column)
        if len(pivots) == len(rows):
            break
    return rows, pivots


def inverse(matrix):
    n = len(matrix)
    reduced, pivots = rref([list(row)+[int(i == j) for j in range(n)] for i, row in enumerate(matrix)])
    if pivots[:n] != list(range(n)):
        raise ArithmeticError("The chosen first slice is singular")
    return [row[n:] for row in reduced]


def matmul(left, right):
    columns = list(zip(*right))
    return [[sum((x*y for x, y in zip(row, column)), Fraction(0)) for column in columns] for row in left]


def exact_algebra(slices, anchor_coefficients):
    """Exact rank, closure, center, and trace-form checks over Q.

    Slices are square matrices. After an invertible anchor normalization,
    full span + closure + center dimension one + nondegenerate trace form
    identifies a central simple algebra over C. If its dimension is n^2
    and the module dimension n*b, its tensor is M(n,b,n).
    """
    dimension = len(slices[0])
    count = len(slices)
    anchor = [[sum(Fraction(c)*s[i][j] for c, s in zip(anchor_coefficients, slices))
               for j in range(dimension)] for i in range(dimension)]
    anchor_inverse = inverse(anchor)
    normalized = [matmul(s, anchor_inverse) for s in slices]
    flat = [[x for row in s for x in row] for s in normalized]
    _, pivot_positions = rref(flat)
    if len(pivot_positions) != count:
        return {"span_dimension": len(pivot_positions), "expected_span_dimension": count,
                "closed": False, "accepted": False, "reason": "first-leg span collapsed"}
    extraction_inverse = inverse([[flat[k][position] for k in range(count)] for position in pivot_positions])
    products = [[matmul(left, right) for right in normalized] for left in normalized]
    checked = 0
    for i, j in product(range(count), repeat=2):
        vector = [x for row in products[i][j] for x in row]
        coordinates = matmul(extraction_inverse, [[vector[p]] for p in pivot_positions])
        if any(vector[p] != sum(coordinates[k][0]*flat[k][p] for k in range(count))
               for p in range(dimension*dimension)):
            return {"span_dimension": count, "closed": False, "accepted": False,
                    "first_failed_product": [i, j], "complete_products_checked": checked}
        checked += 1
    commutator_constraints = [[products[i][j][r][c]-products[j][i][r][c] for i in range(count)]
                              for j, r, c in product(range(count), range(dimension), range(dimension))]
    center_dimension = count-len(rref(commutator_constraints)[1])
    trace_form = [[sum(products[i][j][r][r] for r in range(dimension)) for j in range(count)]
                  for i in range(count)]
    trace_rank = len(rref(trace_form)[1])
    return {"span_dimension": count, "closed": True, "complete_products_checked": checked,
            "center_dimension": center_dimension, "trace_form_rank": trace_rank,
            "accepted": center_dimension == 1 and trace_rank == count,
            "coefficient_ring": "Q", "interpretation_field": "C"}


def exact_control():
    """The actual matrix tensor must pass; a closed commutative algebra fails."""
    _, _, target_shape, terms = NARROW.coordinates(3, 2)
    slices = [[[0]*target_shape[1] for _ in range(target_shape[2])] for _ in range(target_shape[0])]
    for a, b, c in terms:
        slices[a][c][b] += 1
    anchor = [int(i == k) for i, k in product(range(3), repeat=2)]
    positive = exact_algebra(slices, anchor)
    if not positive["accepted"] or positive["complete_products_checked"] != 81:
        raise ArithmeticError("The exact matrix-algebra positive control failed")
    diagonal = [[[int(i == j == k) for j in range(4)] for i in range(4)] for k in range(4)]
    negative = exact_algebra(diagonal, [1]*4)
    if not negative["closed"] or negative["accepted"] or negative["center_dimension"] != 4:
        raise ArithmeticError("The commutative-algebra negative control failed")
    triangular = [[[1, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [0, 1]]]
    radical = exact_algebra(triangular, [1, 0, 1])
    if (not radical["closed"] or radical["accepted"] or radical["center_dimension"] != 1
            or radical["trace_form_rank"] != 2):
        raise ArithmeticError("The nonsemisimple-algebra negative control failed")
    return {"matrix_tensor_control": positive, "closed_nonmatrix_control": negative,
            "closed_center_one_nonsemisimple_control": radical,
            "controls_passed": True, "improves_omega": False}


class KernelProblem:
    def __init__(self, n, b=2, stabilized=False, complex_coefficients=False):
        import numpy as np
        self.n, self.b, self.stabilized = n, b, stabilized
        self.complex_coefficients = complex_coefficients
        source_shape, terms, target_shape, _ = NARROW.coordinates(n, b)
        self.ambient, self.dimension = source_shape[1], target_shape[1]
        self.excess = self.ambient-self.dimension
        h = n+b-1
        self.retained_b = [y*h+j for y in range(b) for j in range(n)]
        self.removed_b = [i for i in range(self.ambient) if i not in self.retained_b]
        self.retained_c = [z*b+v for z in range(n) for v in range(b)]
        self.removed_c = [i for i in range(self.ambient) if i not in self.retained_c]
        self.source = np.zeros((n*n, self.ambient, self.ambient))
        for a, bb, c in terms:
            self.source[a, c, bb] += 1
        self.anchor = np.array([int(i == k) for i, k in product(range(n), repeat=2)])
        self.kernel_parameters = 2*self.dimension*self.excess
        self.parameters = self.kernel_parameters*(2 if complex_coefficients else 1)
        self.closure_equations = n**4*self.dimension**2*(2 if complex_coefficients else 1)
        self.equations = self.closure_equations+(b*b+3 if stabilized else 0)

    def compressions(self, x):
        import numpy as np
        d, e = self.dimension, self.excess
        if self.complex_coefficients:
            x = x[:self.kernel_parameters]+1j*x[self.kernel_parameters:]
        left = np.zeros((d, self.ambient), dtype=complex if self.complex_coefficients else float)
        right = np.zeros((self.ambient, d), dtype=complex if self.complex_coefficients else float)
        left[:, self.retained_c] = np.eye(d)
        right[self.retained_b, :] = np.eye(d)
        left[:, self.removed_c] = x[:d*e].reshape(d, e)
        right[self.removed_b, :] = x[d*e:].reshape(e, d)
        return left, right

    def normalized_slices(self, x):
        import numpy as np
        left, right = self.compressions(x)
        slices = np.einsum("is,ast,tj->aij", left, self.source, right, optimize=True)
        anchor = np.einsum("a,aij->ij", self.anchor, slices)
        normalized = slices @ np.linalg.inv(anchor)
        return slices, anchor, normalized

    def residual(self, x):
        import numpy as np
        try:
            _, _, normalized = self.normalized_slices(x)
            basis, triangular = np.linalg.qr(normalized.reshape(self.n*self.n, -1).T)
            if not np.isfinite(basis).all():
                return np.full(self.equations, 1e3)
            matrices = basis.T.reshape(self.n*self.n, self.dimension, self.dimension)
            products = np.einsum("aij,bjk->abik", matrices, matrices, optimize=True).reshape(self.n**4, -1)
            closure = (products-(products @ basis.conj()) @ basis.T).ravel()
            if self.complex_coefficients:
                closure = np.concatenate((closure.real, closure.imag))
            if not self.stabilized:
                return closure
            _, anchor, _ = self.normalized_slices(x)
            span_condition = np.linalg.cond(normalized.reshape(self.n*self.n, -1))
            anchor_condition = np.linalg.cond(anchor)
            d = self.dimension
            commutant_matrix = np.concatenate([np.kron(s, np.eye(d))-np.kron(np.eye(d), s.T)
                                               for s in matrices])
            commutant = np.linalg.svd(commutant_matrix, compute_uv=False)[::-1]
            trace_form = np.einsum("aij,bji->ab", matrices, matrices)
            trace_minimum = np.linalg.svd(trace_form, compute_uv=False)[-1]
            additional = [max(0.0, np.log(anchor_condition/100)),
                          max(0.0, np.log(span_condition/100)),
                          *commutant[1:self.b*self.b],
                          max(0.0, 0.01-commutant[self.b*self.b]),
                          max(0.0, 0.01-trace_minimum)]
            return np.concatenate((closure, additional))
        except np.linalg.LinAlgError:
            return np.full(self.equations, 1e3)

    def diagnostics(self, x):
        import numpy as np
        slices, anchor, normalized = self.normalized_slices(x)
        singular = np.linalg.svd(normalized.reshape(self.n*self.n, -1), compute_uv=False)
        residual = self.residual(x)
        d = self.dimension
        equations = np.concatenate([np.kron(s, np.eye(d))-np.kron(np.eye(d), s.T) for s in normalized])
        commutant_singular = np.linalg.svd(equations, compute_uv=False)
        basis = np.linalg.qr(normalized.reshape(self.n*self.n, -1).T)[0].T.reshape(self.n*self.n,d,d)
        orthonormal_commutant = np.linalg.svd(np.concatenate([
            np.kron(s, np.eye(d))-np.kron(np.eye(d), s.T) for s in basis]), compute_uv=False)
        trace_singular = np.linalg.svd(np.einsum("aij,bji->ab", basis,basis),compute_uv=False)
        return {"closure_residual_norm": float(np.linalg.norm(residual[:self.closure_equations])),
                "maximum_absolute_closure_error": float(np.max(np.abs(residual[:self.closure_equations]))),
                "additional_condition_and_spectrum_residuals": residual[self.closure_equations:].tolist(),
                "anchor_condition_number": float(np.linalg.cond(anchor)),
                "slice_span_singular_values": singular.tolist(),
                "smallest_commutant_singular_values": sorted(commutant_singular)[:self.b*self.b+2],
                "orthonormal_basis_smallest_commutant_singular_values": sorted(orthonormal_commutant)[:self.b*self.b+2],
                "orthonormal_basis_trace_form_singular_values": trace_singular.tolist(),
                "maximum_absolute_kernel_parameter": float(np.max(np.abs(x)))}


def fit(n, seed, evaluations, bound, checkpoint, stabilized=False, complex_coefficients=False):
    import numpy as np
    import scipy
    from scipy.optimize import least_squares
    problem = KernelProblem(n, stabilized=stabilized, complex_coefficients=complex_coefficients)
    rng = np.random.default_rng(seed)
    x = rng.normal(size=problem.parameters)*0.3
    initial = problem.diagnostics(x)
    start = time.monotonic()
    result = least_squares(problem.residual, x, bounds=(-bound, bound), max_nfev=evaluations,
                           ftol=1e-11, xtol=1e-11, gtol=1e-11, method="trf", x_scale="jac")
    elapsed = time.monotonic()-start
    if checkpoint:
        Path(checkpoint).write_text(json.dumps({"n": n, "b": 2, "complex_coefficients": complex_coefficients,
                                               "parameters": result.x.tolist()}, indent=2)+"\n")
    return {"n": n, "b": 2, "seed": seed, "parameter_bound": bound,
            "parameters": problem.parameters, "closure_equations": problem.closure_equations,
            "additional_condition_and_spectrum_equations": problem.equations-problem.closure_equations,
            "stabilized": stabilized,
            "complex_coefficients": complex_coefficients,
            "parameter_bound_applies_to": "each real and imaginary coordinate" if complex_coefficients else "each real coordinate",
            "maximum_function_evaluations": evaluations, "function_evaluations": result.nfev,
            "jacobian_evaluations": result.njev, "elapsed_seconds": elapsed,
            "numpy_version": np.__version__, "scipy_version": scipy.__version__,
            "initial": initial, "final": problem.diagnostics(result.x),
            "solver_status": int(result.status), "solver_message": result.message,
            "exact_coefficient_certificate": False, "construction_supplied": False,
            "improves_omega": False,
            "scope": "One compression-kernel chart, fixed invertible anchor, finite bounded search; closure alone is not a matrix tensor certificate."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--evaluations", type=int, default=400)
    parser.add_argument("--bound", type=float, default=10)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--control", action="store_true")
    parser.add_argument("--stabilized", action="store_true")
    parser.add_argument("--complex", action="store_true", dest="complex_coefficients")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = exact_control() if args.control else fit(args.n, args.seed, args.evaluations, args.bound,
                                                     args.checkpoint, args.stabilized, args.complex_coefficients)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
