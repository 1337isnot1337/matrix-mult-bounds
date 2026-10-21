"""Exact finite-symmetry model and bounded P3 matrix-map discovery.

P3 is expressed as two symmetric traceless quadratic products.  The
tetrahedral group reduces ordinary P3 -> M3 maps to 29 parameters.
Optional scalar summands are explicit source coordinates.  Numerical
fits are not tensor identities or exponent improvements.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
import time


def multiplication():
    """U tensor U -> W, W=(x²,y²,xy,yz,zx), x²+y²+z²=0."""
    return [(0, 0, 0, 1), (1, 1, 1, 1), (2, 2, 0, -1), (2, 2, 1, -1),
            (0, 1, 2, 1), (1, 0, 2, 1), (1, 2, 3, 1), (2, 1, 3, 1),
            (2, 0, 4, 1), (0, 2, 4, 1)]


def source_terms(scalars=0):
    terms = defaultdict(int)
    for p, y, z, a in multiplication():
        for q, v, j, b in multiplication():
            terms[p*3+q, y*5+j, z*3+v] += a*b
    for k in range(scalars):
        terms[9+k, 15+k, 15+k] = 1
    return {point: value for point, value in terms.items() if value}


def target_terms():
    return {(3*i+j, 3*j+k, 3*k+i): 1 for i, j, k in product(range(3), repeat=3)}


def invariant_orbits():
    """All 61 orbits of allowed target coefficients under A4.

    The Klein four signs force an even number of each Cartesian index.
    The cyclic rotation groups the remaining 183 positions in threes.
    """
    remaining = set()
    for point in product(range(9), repeat=3):
        labels = [v for k in point for v in divmod(k, 3)]
        if all(labels.count(v) % 2 == 0 for v in range(3)):
            remaining.add(point)
    orbits = []
    while remaining:
        first = min(remaining)
        orbit = []
        for shift in range(3):
            orbit.append(tuple(3*((k//3+shift) % 3)+(k % 3+shift) % 3 for k in first))
        if len(set(orbit)) != 3 or not set(orbit) <= remaining:
            raise ArithmeticError("The target invariant orbit decomposition failed")
        remaining.difference_update(orbit)
        orbits.append(sorted(orbit))
    if len(orbits) != 61:
        raise ArithmeticError("Unexpected invariant dimension")
    return orbits


@lru_cache(None)
def intertwiner_data(scalars=0):
    import sympy as sp
    u = [sp.diag(1, -1, -1), sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])]
    w = [sp.diag(1, 1, -1, 1, -1),
         sp.Matrix([[0, -1, 0, 0, 0], [1, -1, 0, 0, 0],
                    [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0]])]
    target_g = [sp.kronecker_product(g, g) for g in u]
    source_g = [[sp.kronecker_product(g, g) for g in u],
                [sp.kronecker_product(g, h) for g, h in zip(u, w)],
                [sp.kronecker_product(h, g) for g, h in zip(u, w)]]
    if scalars:
        source_g = [[sp.diag(g, sp.eye(scalars)) for g in pair] for pair in source_g]
    bases = []
    for pair in source_g:
        size = pair[0].rows
        equations = sp.Matrix.vstack(*[
            sp.kronecker_product(t, sp.eye(size))-sp.kronecker_product(sp.eye(9), s.T)
            for t, s in zip(target_g, pair)])
        basis = []
        for vector in equations.nullspace():
            multiple = sp.ilcm(*(v.q for v in vector))
            matrix = sp.Matrix(9, size, [int(multiple*v) for v in vector])
            if any(t*matrix != matrix*s for t, s in zip(target_g, pair)):
                raise ArithmeticError("An exact intertwiner equation failed")
            basis.append([[int(matrix[i, j]) for j in range(size)] for i in range(9)])
        bases.append(basis)
    expected = [7+scalars, 11+scalars, 11+scalars]
    if list(map(len, bases)) != expected:
        raise ArithmeticError("Unexpected exact intertwiner dimensions")
    return bases, source_g, target_g, u, w


def exact_controls(scalars=0):
    import sympy as sp
    bases, source_g, target_g, u, w = intertwiner_data(scalars)
    # Explicit polynomial changes of basis from ordinary binary forms.
    x, y = sp.symbols("x y")
    cartesian = [x*x-y*y, sp.I*(x*x+y*y), 2*x*y]
    degree_four = [cartesian[0]**2, cartesian[1]**2,
                   cartesian[0]*cartesian[1], cartesian[1]*cartesian[2],
                   cartesian[2]*cartesian[0]]
    k2 = sp.Matrix([[sp.expand(f).coeff(x, 2-j).coeff(y, j) for f in cartesian] for j in range(3)])
    k4 = sp.Matrix([[sp.expand(f).coeff(x, 4-j).coeff(y, j) for f in degree_four] for j in range(5)])
    if not k2.det() or not k4.det():
        raise ArithmeticError("A binary-form coordinate change is singular")
    if sp.expand(sum(f*f for f in cartesian)) != 0:
        raise ArithmeticError("The Cartesian conic identity failed")
    mu = multiplication()
    for i, j in product(range(3), repeat=2):
        reconstructed = sum(c*degree_four[k] for ii, jj, k, c in mu if (ii, jj) == (i, j))
        if sp.expand(cartesian[i]*cartesian[j]-reconstructed) != 0:
            raise ArithmeticError("The binary-form multiplication identity failed")
    matrix_mu = sp.zeros(5, 9)
    for i, j, k, c in mu:
        matrix_mu[k, 3*i+j] += c
    for g, h in zip(u, w):
        if h*matrix_mu != matrix_mu*sp.kronecker_product(g, g):
            raise ArithmeticError("Exact finite-group multiplication covariance failed")
    # A4's two generators preserve the full trace target as a tensor.
    target = target_terms()
    for g in target_g:
        changed = defaultdict(int)
        images = [[(i, int(g[i, j])) for i in range(9) if g[i, j]] for j in range(9)]
        for point, value in target.items():
            for terms in product(*(images[k] for k in point)):
                changed[tuple(v[0] for v in terms)] += value*terms[0][1]*terms[1][1]*terms[2][1]
        if dict(changed) != target:
            raise ArithmeticError("Exact trace-tensor covariance failed")
    orbits = invariant_orbits()
    if any(len({target.get(point, 0) for point in orbit}) != 1 for orbit in orbits):
        raise ArithmeticError("The target does not obey the invariant orbit equations")
    return {
        "source": f"P3 direct_sum {scalars} scalar tensor(s)",
        "coordinate_equivalence_field": "Q(i)", "search_coefficient_ring": "Q",
        "cartesian_quadratic_polynomials": [str(v) for v in cartesian],
        "quartic_basis_polynomials": [str(sp.expand(v)) for v in degree_four],
        "quadratic_change_of_basis_determinant": str(k2.det()),
        "quartic_change_of_basis_determinant": str(k4.det()),
        "binary_multiplication_products_checked": 9,
        "exact_multiplication_covariance_generators": 2,
        "exact_target_covariance_generators": 2,
        "intertwiner_dimensions": list(map(len, bases)),
        "intertwiner_maps_checked": sum(map(len, bases)),
        "target_coefficient_positions": 729, "allowed_positions": 183,
        "invariant_coordinate_orbits": 61, "orbit_size": 3,
        "cartesian_source_nonzero_terms": len(source_terms(scalars)),
        "controls_passed": True, "improves_omega": False,
    }


def coefficient_contraction(terms, maps):
    """Full 729-position contraction, retaining all off-support terms."""
    result = defaultdict(Fraction)
    columns = [[[ (i, Fraction(row[j])) for i, row in enumerate(matrix) if row[j] ]
                for j in range(len(matrix[0]))] for matrix in maps]
    for point, coefficient in terms.items():
        for image in product(*(columns[axis][coordinate] for axis, coordinate in enumerate(point))):
            result[tuple(v[0] for v in image)] += coefficient*image[0][1]*image[1][1]*image[2][1]
    return {point: value for point, value in result.items() if value}


def numerical_core(scalars=0):
    import numpy as np
    bases = [np.asarray(axis, dtype=np.int64) for axis in intertwiner_data(scalars)[0]]
    orbits = invariant_orbits()
    terms = source_terms(scalars)
    core = np.zeros(tuple(len(axis) for axis in bases)+(len(orbits),), dtype=np.int64)
    for t, orbit in enumerate(orbits):
        i, j, k = orbit[0]
        for (a, b, c), value in terms.items():
            core[:, :, :, t] += value*(bases[0][:, i, a, None, None]
                                     *bases[1][None, :, j, b, None]
                                     *bases[2][None, None, :, k, c])
    wanted = np.asarray([target_terms().get(orbit[0], 0) for orbit in orbits], dtype=float)
    # Independent all-position integer contraction checks the orbit objective.
    coefficients = [np.arange(1, len(axis)+1, dtype=np.int64) for axis in bases]
    maps = [np.einsum("a,aij->ij", c, axis) for c, axis in zip(coefficients, bases)]
    full = coefficient_contraction(terms, [matrix.tolist() for matrix in maps])
    reduced = np.einsum("abct,a,b,c->t", core, *coefficients, optimize=True)
    expected = {point: Fraction(int(value)) for value, orbit in zip(reduced, orbits) for point in orbit if value}
    if full != expected:
        raise ArithmeticError("The reduced objective and complete coefficient contraction disagree")
    return [axis.astype(float) for axis in bases], core.astype(float), wanted, orbits


def fit(scalars, seed, iterations, ridge, report_every, checkpoint):
    import numpy as np
    bases, core, target, orbits = numerical_core(scalars)
    rng = np.random.default_rng(seed)
    coefficients = [rng.normal(size=len(axis))/np.linalg.norm(axis.reshape(len(axis), -1), axis=1)
                    for axis in bases]
    shape = list(core.shape[:3])
    cores = []
    for axis in range(3):
        others = [k for k in range(3) if k != axis]
        cores.append(np.transpose(core, (axis, *others, 3)).reshape(shape[axis], -1, 61))
    norm = float(np.linalg.norm(target))
    start = time.monotonic()
    history, best = [], None
    for iteration in range(iterations+1):
        if iteration % report_every == 0 or iteration == iterations:
            result = np.einsum("abct,a,b,c->t", core, *coefficients, optimize=True)
            difference = result-target
            relative = float(np.linalg.norm(difference)/norm)
            maps = [np.einsum("a,aij->ij", c, basis) for c, basis in zip(coefficients, bases)]
            # Replay all 729 tensor positions, including forced zero positions.
            full = np.zeros((9, 9, 9))
            for point, value in source_terms(scalars).items():
                full += value*np.einsum("i,j,k->ijk", *(maps[k][:, point[k]] for k in range(3)))
            wanted = np.zeros((9, 9, 9))
            for point, value in target_terms().items():
                wanted[point] = value
            full_error = float(np.linalg.norm(full-wanted)/np.linalg.norm(wanted))
            if abs(full_error-relative) > 1e-8*(1+relative):
                raise ArithmeticError("The invariant and complete coefficient residuals disagree")
            row = {"iteration": iteration, "relative_coefficient_error": full_error,
                   "maximum_absolute_coefficient_error": float(np.max(np.abs(full-wanted))),
                   "map_frobenius_norms": [float(np.linalg.norm(matrix)) for matrix in maps],
                   "elapsed_seconds": time.monotonic()-start}
            history.append(row)
            print(json.dumps({"scalars": scalars, "seed": seed, **row}), flush=True)
            if best is None or full_error < best:
                best = full_error
                if checkpoint:
                    Path(checkpoint).write_text(json.dumps({
                        "source": f"P3 direct_sum {scalars} scalar tensor(s)", "scalars": scalars,
                        "equivariant_coefficients": [v.tolist() for v in coefficients],
                        "maps_in_cartesian_source_coordinates": [v.tolist() for v in maps],
                        "relative_coefficient_error": full_error,
                    }, indent=2)+"\n")
            if full_error < 1e-13:
                break
        if iteration == iterations:
            break
        for axis in range(3):
            others = [k for k in range(3) if k != axis]
            vector = np.outer(coefficients[others[0]], coefficients[others[1]]).ravel()
            environment = np.einsum("akt,k->ta", cores[axis], vector, optimize=True)
            augmented = np.vstack((environment, np.eye(shape[axis])*ridge**0.5))
            rhs = np.concatenate((target, np.zeros(shape[axis])))
            coefficients[axis] = np.linalg.lstsq(augmented, rhs, rcond=1e-14)[0]
        norms = [float(np.linalg.norm(np.einsum("a,aij->ij", c, basis)))
                 for c, basis in zip(coefficients, bases)]
        if min(norms) < 1e-100 or not np.isfinite(norms).all():
            raise ArithmeticError("The coefficient maps collapsed or diverged")
        common = float(np.prod(norms))**(1/3)
        coefficients = [c*(common/value) for c, value in zip(coefficients, norms)]
    return {"source": f"P3 direct_sum {scalars} scalar tensor(s)", "target": "M3",
            "scalars": scalars, "intertwiner_dimensions": shape,
            "parameters": sum(shape), "source_shape": [9+scalars, 15+scalars, 15+scalars],
            "source_nonzero_terms": len(source_terms(scalars)), "tensor_positions_checked": 729,
            "independent_invariant_equations": 61, "seed": seed,
            "maximum_iterations": iterations, "iterations_completed": iteration, "ridge": ridge,
            "history": history, "best_relative_coefficient_error": best,
            "method": "real A4-equivariant ordinary-map ALS with full coefficient replay",
            "coefficient_coordinate_equivalence_field": "Q(i)", "numpy_version": np.__version__,
            "exact_coefficient_certificate": False, "construction_supplied": False,
            "improves_omega": False,
            "scope": "Finite symmetry-restricted discovery; a numerical residual does not prove a tensor identity."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scalars", type=int, default=0)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--ridge", type=float, default=1e-12)
    parser.add_argument("--report-every", type=int, default=100)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--control", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.scalars < 0:
        parser.error("--scalars must be nonnegative")
    report = (exact_controls(args.scalars) if args.control else
              fit(args.scalars, args.seed, args.iterations, args.ridge, args.report_every, args.checkpoint))
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key: value for key, value in report.items() if key != "history"}, indent=2))
