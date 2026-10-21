"""Fix the exact polarization repair and search 20 remaining parameters.

The source is explicitly P3 direct_sum one scalar.  The diagonal
Klein-four fixed sector is repaired exactly before fitting the other
target coefficients.  No numerical fit is called a construction.
"""
import argparse
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path
import time


SPEC = importlib.util.spec_from_file_location(
    "tetrahedral_reduced_dependency", Path(__file__).with_name("tetrahedral_search.py"))
TETRA = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TETRA)


def bases():
    diagonal = [0, 4, 8]
    source_fixed = [[0, 4, 8], [3, 9, 12], [9, 13, 8]]
    full_bases, source_g, target_g, _, _ = TETRA.intertwiner_data(1)
    augmented = []
    for axis, size in enumerate((10, 16, 16)):
        matrix = [[Fraction(0)]*size for _ in range(9)]
        multiplier = Fraction(1, 2) if axis < 2 else Fraction(-2)
        for i, j in product(range(3), repeat=2):
            matrix[diagonal[i]][source_fixed[axis][j]] = multiplier*(i != j)
        for row in diagonal:
            matrix[row][-1] = Fraction(1)
        off_diagonal = [m for m in full_bases[axis]
                        if not any(value for row in diagonal for value in m[row])]
        augmented.append([matrix]+off_diagonal)
    if [len(axis)-1 for axis in augmented] != [4, 8, 8]:
        raise ArithmeticError("Unexpected remaining parameter dimensions")
    return augmented


def exact_control():
    augmented = bases()
    fixed = [axis[0] for axis in augmented]
    full = TETRA.coefficient_contraction(TETRA.source_terms(1), fixed)
    desired = {(0, 0, 0): Fraction(1), (4, 4, 4): Fraction(1), (8, 8, 8): Fraction(1)}
    if full != desired:
        raise ArithmeticError("The exact full polarization control failed")
    without_scalar = TETRA.coefficient_contraction(TETRA.source_terms(0),
                                                   [[row[:-1] for row in matrix] for matrix in fixed])
    expected = dict(desired)
    for point in product((0, 4, 8), repeat=3):
        expected[point] = expected.get(point, Fraction(0))-1
    expected = {point: value for point, value in expected.items() if value}
    if without_scalar != expected:
        raise ArithmeticError("The rank-one polarization defect changed")
    return {"source": "P3 direct_sum one scalar", "coefficient_ring": "Q in Cartesian coordinates",
            "diagonal_maps_a_b": [["0", "1/2", "1/2"], ["1/2", "0", "1/2"], ["1/2", "1/2", "0"]],
            "diagonal_map_c": [[0, -2, -2], [-2, 0, -2], [-2, -2, 0]],
            "scalar_maps": "all-ones on the three diagonal target coordinates, on each leg",
            "all_target_positions_checked": 729, "fixed_target": "three scalar products D3",
            "original_source_defect": "minus the all-ones rank-one tensor on the diagonal sector",
            "remaining_parameter_dimensions": [4, 8, 8], "controls_passed": True,
            "matrix_multiplication_construction": False, "improves_omega": False}


def numerical_core():
    import numpy as np
    augmented = bases()
    numerators = [np.asarray([[[int(2*Fraction(v)) for v in row] for row in matrix]
                              for matrix in axis], dtype=np.int64) for axis in augmented]
    orbits = TETRA.invariant_orbits()
    core = np.zeros(tuple(len(axis) for axis in augmented)+(61,), dtype=np.int64)
    for t, orbit in enumerate(orbits):
        i, j, k = orbit[0]
        for (a, b, c), value in TETRA.source_terms(1).items():
            core[:, :, :, t] += value*(numerators[0][:, i, a, None, None]
                                     *numerators[1][None, :, j, b, None]
                                     *numerators[2][None, None, :, k, c])
    coefficients = [np.arange(1, len(axis)+1, dtype=np.int64) for axis in augmented]
    maps = [[[sum(Fraction(int(coefficients[k][r]))*Fraction(augmented[k][r][i][j])
                   for r in range(len(augmented[k]))) for j in range(len(augmented[k][0][0]))]
             for i in range(9)] for k in range(3)]
    full = TETRA.coefficient_contraction(TETRA.source_terms(1), maps)
    values = np.einsum("abct,a,b,c->t", core, *coefficients, optimize=True)
    expected = {point: Fraction(int(value), 8) for value, orbit in zip(values, orbits) for point in orbit if value}
    if full != expected:
        raise ArithmeticError("The constrained objective failed its complete exact coefficient control")
    target = np.asarray([TETRA.target_terms().get(orbit[0], 0) for orbit in orbits], dtype=float)
    return [axis.astype(float)/2 for axis in numerators], core.astype(float)/8, target


def fit(seed, iterations, ridge, report_every, checkpoint):
    import numpy as np
    augmented, core, target = numerical_core()
    rng = np.random.default_rng(seed)
    coefficients = [np.concatenate(([1.0], rng.normal(size=len(axis)-1))) for axis in augmented]
    axis_cores = []
    for axis in range(3):
        other = [k for k in range(3) if k != axis]
        axis_cores.append(np.transpose(core, (axis, *other, 3)).reshape(len(augmented[axis]), -1, 61))
    norm = float(np.linalg.norm(target))
    start = time.monotonic()
    history, best = [], None
    for iteration in range(iterations+1):
        if iteration % report_every == 0 or iteration == iterations:
            actual = np.einsum("abct,a,b,c->t", core, *coefficients, optimize=True)
            error = float(np.linalg.norm(actual-target)/norm)
            maps = [np.einsum("a,aij->ij", c, basis) for c, basis in zip(coefficients, augmented)]
            full = np.zeros((9, 9, 9))
            for point, value in TETRA.source_terms(1).items():
                full += value*np.einsum("i,j,k->ijk", *(maps[k][:, point[k]] for k in range(3)))
            desired = np.zeros_like(full)
            for point, value in TETRA.target_terms().items():
                desired[point] = value
            full_error = float(np.linalg.norm(full-desired)/np.linalg.norm(desired))
            if abs(error-full_error) > 1e-8*(1+error):
                raise ArithmeticError("The constrained full coefficient residual disagrees")
            row = {"iteration": iteration, "relative_coefficient_error": full_error,
                   "maximum_absolute_coefficient_error": float(np.max(np.abs(full-desired))),
                   "map_frobenius_norms": [float(np.linalg.norm(matrix)) for matrix in maps],
                   "diagonal_sector_maximum_error": float(np.max(np.abs((full-desired)[np.ix_([0,4,8],[0,4,8],[0,4,8])]))),
                   "elapsed_seconds": time.monotonic()-start}
            history.append(row)
            print(json.dumps({"seed": seed, **row}), flush=True)
            if best is None or full_error < best:
                best = full_error
                if checkpoint:
                    Path(checkpoint).write_text(json.dumps({"source": "P3 direct_sum one scalar",
                        "equivariant_coefficients": [v.tolist() for v in coefficients],
                        "maps_in_cartesian_source_coordinates": [v.tolist() for v in maps],
                        "relative_coefficient_error": full_error,
                        "diagonal_sector_fixed_exactly": True}, indent=2)+"\n")
            if full_error < 1e-13:
                break
        if iteration == iterations:
            break
        for axis in range(3):
            other = [k for k in range(3) if k != axis]
            vector = np.outer(coefficients[other[0]], coefficients[other[1]]).ravel()
            environment = np.einsum("akt,k->ta", axis_cores[axis], vector, optimize=True)
            design = np.vstack((environment[:, 1:], np.eye(len(augmented[axis])-1)*ridge**0.5))
            rhs = np.concatenate((target-environment[:, 0], np.zeros(len(augmented[axis])-1)))
            coefficients[axis][1:] = np.linalg.lstsq(design, rhs, rcond=1e-14)[0]
    return {"source": "P3 direct_sum one scalar", "target": "M3",
            "parameters": 20, "parameter_dimensions": [4, 8, 8],
            "full_target_positions_checked": 729, "invariant_coordinate_orbits": 61,
            "fixed_diagonal_sector_positions": 27, "seed": seed,
            "maximum_iterations": iterations, "iterations_completed": iteration,
            "ridge": ridge, "history": history, "best_relative_coefficient_error": best,
            "method": "real A4-equivariant ALS with exact polarization sector fixed",
            "construction_supplied": False, "exact_coefficient_certificate": False,
            "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=1200)
    parser.add_argument("--ridge", type=float, default=1e-12)
    parser.add_argument("--report-every", type=int, default=200)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--control", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = exact_control() if args.control else fit(args.seed, args.iterations, args.ridge, args.report_every, args.checkpoint)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key: value for key, value in report.items() if key != "history"}, indent=2))
