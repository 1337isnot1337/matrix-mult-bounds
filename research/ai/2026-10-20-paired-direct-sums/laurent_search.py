"""First-order graded Laurent discovery, with a complete coefficient objective.

The model is epsilon^-1 product_k (L[k] + epsilon H[k]).  It requires
the degree-zero contraction to vanish and the degree-one contraction to
equal the complete target. Numerical residuals do not certify either.
"""
from collections import defaultdict
from fractions import Fraction
import argparse
import importlib.util
from itertools import product
import json
from pathlib import Path
import time


ROOT = Path(__file__).resolve().parents[3]
GRADE_PATH = ROOT / "research/ai/2026-10-20-paired-construction/graded_search.py"
SPEC = importlib.util.spec_from_file_location("paired_graded_dependency", GRADE_PATH)
GRADE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GRADE)


def blocks(a):
    if a == 3:
        return [([0], [2, 4, 5], [0, 1, 2]),
                ([0, 1, 2], [2, 4, 6], [1, 2])]
    if a in (2, 10):
        return GRADE.example(a)
    raise ValueError("only the recorded a=2,3,10 families are available")


def problem(a):
    import numpy as np
    source, sw, st, target, tw, tt = GRADE.coordinates(a, blocks(a))
    sg, tg, sl, tl = [], [], [], []
    for weights, groups, lookup in [(sw, sg, sl), (tw, tg, tl)]:
        for axis in range(3):
            grouped = defaultdict(list)
            for i, w in enumerate(weights[axis]):
                grouped[w].append(i)
            groups.append(dict(grouped))
            lookup.append({i: (w, j) for w, ids in grouped.items() for j, i in enumerate(ids)})
    source_blocks, target_blocks = {}, {}
    for w in product(*(sorted(axis) for axis in tg)):
        if sum(w) != 4*a-4:
            continue
        if any(len(tg[k][w[k]]) > len(sg[k].get(w[k], [])) for k in range(3)):
            raise ArithmeticError("target grading exceeds the source")
        source_blocks[w] = np.zeros(tuple(len(sg[k][w[k]]) for k in range(3)))
        target_blocks[w] = np.zeros(tuple(len(tg[k][w[k]]) for k in range(3)))
    for terms, lookups, arrays in [(st, sl, source_blocks), (tt, tl, target_blocks)]:
        for term in terms:
            locations = [lookups[k][term[k]] for k in range(3)]
            weights = tuple(x[0] for x in locations)
            if weights in arrays:
                arrays[weights][tuple(x[1] for x in locations)] += 1
    return sg, tg, source_blocks, target_blocks


def normalize_leading_maps(maps):
    """Fix all three leading Frobenius norms by reparametrizing epsilon.

The degree-one coefficient is unchanged. The degree-zero coefficient is
divided by the product of norms; its required value remains exactly zero.
This prevents an epsilon rescaling alone from hiding a failed leading term.
"""
    import numpy as np
    norms = [sum(float((x[0]*x[0]).sum()) for x in axis.values())**0.5 for axis in maps]
    if min(norms) < 1e-100:
        raise ArithmeticError("a leading map collapsed")
    common = float(np.prod(norms))
    for axis, norm in zip(maps, norms):
        for x in axis.values():
            x[0] /= norm
            x[1] *= common/norm


def coefficient_arrays(source, maps):
    import numpy as np
    result = {}
    for w, tensor in source.items():
        local = [maps[k][w[k]] for k in range(3)]
        terms = []
        for degree in (0, 1):
            terms.append(sum(np.einsum("is,jt,ku,stu->ijk", local[0][levels[0]],
                              local[1][levels[1]], local[2][levels[2]], tensor,
                              optimize=True)
                             for levels in product((0, 1), repeat=3) if sum(levels) == degree))
        result[w] = terms
    return result


def save_checkpoint(path, maps):
    """Save JSON for repository review, or an optional local NumPy archive."""
    import numpy as np
    data = {f"map_{k}_{w}": x for k, leg in enumerate(maps) for w, x in leg.items()}
    if Path(path).suffix == ".json":
        Path(path).write_text(json.dumps({key: value.tolist() for key, value in data.items()}, indent=2)+"\n")
    else:
        np.savez_compressed(path, **data)


def load_checkpoint(path, target_groups):
    import numpy as np
    if Path(path).suffix == ".json":
        saved = json.loads(Path(path).read_text())
        return [{w: np.array(saved[f"map_{k}_{w}"], dtype=float) for w in target_groups[k]} for k in range(3)]
    with np.load(path) as saved:
        return [{w: saved[f"map_{k}_{w}"].copy() for w in target_groups[k]} for k in range(3)]


def fit(a, seed=0, iterations=300, ridge=1e-8, report_every=25, checkpoint=None):
    import numpy as np
    sg, tg, source, target = problem(a)
    rng = np.random.default_rng(seed)
    maps = [{w: rng.normal(size=(2, len(tg[k][w]), len(sg[k][w])))/len(sg[k][w])**0.5
             for w in tg[k]} for k in range(3)]
    normalize_leading_maps(maps)
    target_norm = sum(float((x*x).sum()) for x in target.values())**0.5
    start = time.monotonic()
    history = []
    best = None
    best_maps = None
    for step in range(iterations+1):
        if step % report_every == 0 or step == iterations:
            output = coefficient_arrays(source, maps)
            leading_error = sum(float((x[0]*x[0]).sum()) for x in output.values())**0.5
            constant_error = sum(float(((output[w][1]-target[w])**2).sum()) for w in target)**0.5
            residual = (leading_error**2+constant_error**2)**0.5/target_norm
            row = {"iteration": step, "leading_coefficient_norm": leading_error,
                   "constant_relative_error": constant_error/target_norm,
                   "combined_relative_residual": residual,
                   "first_derivative_map_norms": [sum(float((x[1]*x[1]).sum()) for x in leg.values())**0.5
                                                  for leg in maps],
                   "elapsed_seconds": time.monotonic()-start}
            history.append(row)
            print(json.dumps(row), flush=True)
            if best is None or residual < best:
                best = residual
                best_maps = [{w: x.copy() for w, x in leg.items()} for leg in maps]
                if checkpoint is not None:
                    save_checkpoint(checkpoint, best_maps)
        if step == iterations:
            break
        for axis in range(3):
            other = [k for k in range(3) if k != axis]
            gram = {w: np.zeros((2*len(sg[axis][w]),)*2) for w in tg[axis]}
            rhs = {w: np.zeros((len(tg[axis][w]), 2*len(sg[axis][w]))) for w in tg[axis]}
            for w, tensor in source.items():
                transposed = np.transpose(tensor, (axis, *other))
                left, right = (maps[k][w[k]] for k in other)
                u0 = np.einsum("jt,ku,stu->sjk", left[0], right[0], transposed, optimize=True)
                u1 = (np.einsum("jt,ku,stu->sjk", left[1], right[0], transposed, optimize=True)
                      +np.einsum("jt,ku,stu->sjk", left[0], right[1], transposed, optimize=True))
                u0 = u0.reshape(u0.shape[0], -1)
                u1 = u1.reshape(u1.shape[0], -1)
                degree_zero = np.concatenate((u0, np.zeros_like(u0)), axis=0)
                degree_one = np.concatenate((u1, u0), axis=0)
                exact_target = np.transpose(target[w], (axis, *other)).reshape(len(tg[axis][w[axis]]), -1)
                gram[w[axis]] += degree_zero @ degree_zero.T + degree_one @ degree_one.T
                rhs[w[axis]] += exact_target @ degree_one.T
            for w in tg[axis]:
                g = gram[w]
                g.flat[::g.shape[0]+1] += ridge
                matrix = np.linalg.lstsq(g, rhs[w].T, rcond=1e-13)[0].T
                maps[axis][w] = np.stack(np.split(matrix, 2, axis=1))
            normalize_leading_maps(maps)
    return {"a": a, "blocks": blocks(a), "seed": seed, "iterations_completed": step,
            "ridge": ridge, "history": history, "best_combined_relative_residual": best,
            "source_grade_blocks": len(source),
            "coefficient_equations_per_degree": sum(t.size for t in target.values()),
            "jet_parameters": sum(x.size for leg in maps for x in leg.values()),
            "method": "graded first-order Laurent ALS, complete degree-zero and degree-one coefficients",
            "exact_coefficient_certificate": False, "construction_supplied": False, "improves_omega": False,
            "scope": "Bounded numerical discovery. Neither existence nor nonexistence follows from a residual."}


def exact_jet_coefficients(source_terms, maps):
    """Complete rational contraction of all eight coefficient products.

    maps[axis][degree][target_row][source_column] uses degree 0 or 1.
    Returned degrees 0,1,2,3 precede the common epsilon^-1 factor.
    """
    target_shape = [len(leg[0]) for leg in maps]
    result = [defaultdict(Fraction) for _ in range(4)]
    for source_index in source_terms:
        for levels in product((0, 1), repeat=3):
            degree = sum(levels)
            for target_index in product(*(range(n) for n in target_shape)):
                coefficient = Fraction(1)
                for axis in range(3):
                    coefficient *= Fraction(maps[axis][levels[axis]][target_index[axis]][source_index[axis]])
                if coefficient:
                    result[degree][target_index] += coefficient
    return [{index: value for index, value in degree.items() if value} for degree in result]


def exact_controls():
    """Replay a genuine pole cancellation and an integer paired restriction.

    The W example has a nonzero coefficient of each degree one, two, and
    three before division by epsilon.  The P2 example is the construction
    in the separately maintained exact_p2.py, embedded as a regular jet.
    Neither example provides a degeneration to the larger target.
    """
    diagonal = [(0, 0, 0), (1, 1, 1)]
    leading = [[[1, -1], [0, 0]], [[1, 1], [0, 0]], [[1, 1], [0, 0]]]
    derivative = [[0, 0], [1, 0]]
    w_maps = [[leading[k], derivative] for k in range(3)]
    actual = exact_jet_coefficients(diagonal, w_maps)
    wanted = [{}, {(1, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1},
              {(1, 1, 0): 1, (1, 0, 1): 1, (0, 1, 1): 1}, {(1, 1, 1): 1}]
    if actual != wanted:
        raise ArithmeticError("The full W Laurent control failed")
    # A fit to constant coefficients alone must not accept this example:
    # it has the same constant W coefficient and a nonzero pole.
    corrupt = [[[[x for x in row] for row in level] for level in axis] for axis in w_maps]
    corrupt[0][0][0][1] = -2
    corrupt_coefficients = exact_jet_coefficients(diagonal, corrupt)
    if corrupt_coefficients[1] != wanted[1] or not corrupt_coefficients[0]:
        raise ArithmeticError("The deliberate-pole negative control failed")

    p2_path = ROOT / "research/ai/2026-10-20-paired-construction/exact_p2.py"
    spec = importlib.util.spec_from_file_location("paired_p2_control", p2_path)
    p2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p2)
    source, _, source_terms, target, _, target_terms = GRADE.coordinates(2, GRADE.example(2))
    integer_maps = []
    for axis, substitution in enumerate(p2.maps()):
        target_index = {tuple(label[1:]): i for i, label in enumerate(target[axis])}
        matrix = [[0]*len(source[axis]) for _ in target[axis]]
        for source_index, label in enumerate(source[axis]):
            coefficient, image = substitution[label]
            matrix[target_index[image]][source_index] = coefficient
        integer_maps.append(matrix)
    zero = [[[0]*len(source[k]) for _ in target[k]] for k in range(3)]
    p2_maps = [[zero[0], integer_maps[0]], [integer_maps[1], zero[1]],
               [integer_maps[2], zero[2]]]
    p2_coefficients = exact_jet_coefficients(source_terms, p2_maps)
    if p2_coefficients != [{}, {term: 1 for term in target_terms}, {}, {}]:
        raise ArithmeticError("The full P2 Laurent embedding failed")
    return {"coefficient_ring": "Q", "exact_controls_passed": True,
            "w_source_terms": len(diagonal), "w_target_coordinates_per_degree": 8,
            "w_nonzero_coefficients_by_degree": [len(x) for x in actual],
            "deliberate_pole_detected_despite_correct_constant_term": True,
            "p2_source_terms": len(source_terms), "p2_target_coordinates_per_degree": 64,
            "p2_nonzero_coefficients_by_degree": [len(x) for x in p2_coefficients],
            "scope": "Full coefficient controls for the verifier; neither supplies the a3 or a10 target."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, default=3)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=300)
    parser.add_argument("--ridge", type=float, default=1e-8)
    parser.add_argument("--report-every", type=int, default=25)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = fit(args.a, args.seed, args.iterations, args.ridge, args.report_every, args.checkpoint)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
