"""Unrestricted constant-map discovery for a narrow paired convolution.

Q_(n,b)=sum A[p,q] B[y,q+v] C[p+y,v], p,q<n and y,v<b.
Target M(n,b,n) uses A[i,k] B[i,j] C[j,k].  Every coefficient,
including zeros outside the target support, enters the objective.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[3]


def coordinates(n, b):
    if not isinstance(n, int) or not isinstance(b, int) or min(n, b) < 1:
        raise ValueError("positive integer dimensions are required")
    h = n+b-1
    source_shape = (n*n, b*h, h*b)
    target_shape = (n*n, n*b, b*n)
    source = [(p*n+q, y*h+q+v, (p+y)*b+v)
              for p, q, y, v in product(range(n), range(n), range(b), range(b))]
    target = [(i*n+k, i*b+j, j*n+k) for i, j, k in product(range(n), range(b), range(n))]
    return source_shape, source, target_shape, target


def coefficient_contraction(source_terms, maps):
    """Contract every source term onto every target coordinate over Q."""
    result = defaultdict(Fraction)
    for source in source_terms:
        for target in product(*(range(len(axis)) for axis in maps)):
            value = Fraction(1)
            for k in range(3):
                value *= Fraction(maps[k][target[k]][source[k]])
            if value:
                result[target] += value
    return {key: value for key, value in result.items() if value}


def exact_control():
    """Independently expand the known Q_(2,2)=P2 positive construction."""
    source_shape, source, target_shape, target = coordinates(2, 2)
    path = ROOT / "research/ai/2026-10-20-paired-construction/exact_p2.py"
    spec = importlib.util.spec_from_file_location("narrow_p2_control", path)
    p2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p2)
    maps = []
    source_coordinates = [list(product(range(2), range(2))),
                          list(product(range(2), range(3))), list(product(range(3), range(2)))]
    for k, substitution in enumerate(p2.maps()):
        matrix = [[0]*source_shape[k] for _ in range(target_shape[k])]
        for column, label in enumerate(source_coordinates[k]):
            coefficient, image = substitution[label]
            matrix[2*image[0]+image[1]][column] = coefficient
        maps.append(matrix)
    actual = coefficient_contraction(source, maps)
    if actual != {term: 1 for term in target}:
        raise ArithmeticError("The full narrow-source rational control failed")
    corrupt = [[[value for value in row] for row in axis] for axis in maps]
    corrupt[2][1][0] *= -1
    if coefficient_contraction(source, corrupt) == actual:
        raise ArithmeticError("The sign-error negative control failed")
    return {"source": "Q_(2,2)=P2", "source_terms": len(source),
            "full_target_positions_checked": target_shape[0]*target_shape[1]*target_shape[2],
            "target_terms": len(actual), "coefficient_ring": "Q", "exact_control_passed": True,
            "sign_error_detected": True, "improves_omega": False}


def save(path, maps):
    Path(path).write_text(json.dumps({f"map_{k}": matrix.tolist() for k, matrix in enumerate(maps)}, indent=2)+"\n")


def fit(n, b, seed, iterations=1000, ridge=1e-12, report_every=100, checkpoint=None):
    import numpy as np
    source_shape, source_terms, target_shape, target_terms = coordinates(n, b)
    source, target = np.zeros(source_shape), np.zeros(target_shape)
    for term in source_terms:
        source[term] += 1
    for term in target_terms:
        target[term] += 1
    norm = float(np.linalg.norm(target))
    rng = np.random.default_rng(seed)
    maps = [rng.normal(size=(target_shape[k], source_shape[k]))/source_shape[k]**0.5 for k in range(3)]
    best, history = None, []
    start = time.monotonic()
    for step in range(iterations+1):
        if step % report_every == 0 or step == iterations:
            difference = np.einsum("is,jt,ku,stu->ijk", *maps, source, optimize=True)-target
            relative = float(np.linalg.norm(difference))/norm
            row = {"iteration": step, "relative_coefficient_error": relative,
                   "maximum_absolute_coefficient_error": float(np.max(np.abs(difference))),
                   "map_frobenius_norms": [float(np.linalg.norm(m)) for m in maps],
                   "elapsed_seconds": time.monotonic()-start}
            history.append(row)
            print(json.dumps({"n": n, "b": b, "seed": seed, **row}), flush=True)
            if best is None or relative < best:
                best = relative
                if checkpoint:
                    save(checkpoint, maps)
            if relative < 1e-13:
                break
        if step == iterations:
            break
        for axis in range(3):
            other = [k for k in range(3) if k != axis]
            transposed = np.transpose(source, (axis, *other))
            environment = np.einsum("jt,ku,stu->sjk", maps[other[0]], maps[other[1]],
                                    transposed, optimize=True)
            environment = environment.reshape(environment.shape[0], -1)
            wanted = np.transpose(target, (axis, *other)).reshape(target_shape[axis], -1)
            gram = environment @ environment.T
            gram.flat[::gram.shape[0]+1] += ridge
            maps[axis] = np.linalg.lstsq(gram, (wanted @ environment.T).T, rcond=1e-14)[0].T
        norms = [float(np.linalg.norm(m)) for m in maps]
        if min(norms) < 1e-100 or not np.isfinite(norms).all():
            raise ArithmeticError("The numerical maps collapsed or diverged")
        common = float(np.prod(norms))**(1/3)
        for k in range(3):
            maps[k] *= common/norms[k]
    return {"n": n, "b": b, "source": f"Q_({n},{b})", "target": f"M({n},{b},{n})",
            "source_shape": source_shape, "target_shape": target_shape,
            "source_terms": len(source_terms), "target_terms": len(target_terms),
            "tensor_equations": int(np.prod(target_shape)),
            "parameters": sum(int(m.size) for m in maps), "seed": seed,
            "maximum_iterations": iterations, "iterations_completed": step, "ridge": ridge,
            "numpy_version": np.__version__, "history": history,
            "best_relative_coefficient_error": best,
            "method": "unrestricted real constant-map ALS, full coefficient objective",
            "exact_coefficient_certificate": False, "construction_supplied": False,
            "improves_omega": False,
            "scope": "Finite numerical discovery; full coefficient identity and implication remain separate proof gates."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--b", type=int, default=2)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--ridge", type=float, default=1e-12)
    parser.add_argument("--report-every", type=int, default=100)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--control", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = (exact_control() if args.control else fit(args.n, args.b, args.seed, args.iterations,
                                                       args.ridge, args.report_every, args.checkpoint))
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({k: v for k, v in report.items() if k != "history"}, indent=2))
