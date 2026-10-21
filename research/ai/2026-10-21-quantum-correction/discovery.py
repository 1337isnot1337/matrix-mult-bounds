"""Bounded graded correction discovery for a prescribed exact Q64 point.

Every residual includes all 10,000 target coefficients.  Numerical maps
are not certificates.  The JSON also preserves their composition with
the complete exact cyclotomic source maps in the supplied family file.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import time


ASSIGNMENTS = [
    [(-8, 3, 5), (-8, 5, 3), (8, -3, -5), (8, -5, -3), (-6, 3, 3), (6, -3, -3)],
    [(-8, 3, 5), (-8, 5, 3), (8, -3, -5), (8, -5, -3), (-6, 1, 5), (6, -1, -5)],
    [(-8, 3, 5), (-8, 5, 3), (8, -3, -5), (8, -5, -3), (-6, 5, 1), (6, -5, -1)],
]


def model(path, assignment):
    import numpy as np
    data = json.loads(path.read_text())
    assert (data["N"], data["m"], data["order"]) == (5, 4, 14)
    zeta = np.exp(2j*np.pi/14)

    def evaluate(coefficients):
        value = 0j
        for coefficient in coefficients:
            from fractions import Fraction
            value = value*zeta+float(Fraction(coefficient))
        return value

    original_maps = [np.asarray([[evaluate(x) for x in row] for row in axis], dtype=complex)
                     for axis in data["maps"]]
    base = np.zeros((25, 20, 20), dtype=complex)
    for row in data["tensor"]:
        base[tuple(row["positions"])] = evaluate(row["coefficient"])
    original = np.zeros((36, 36, 36), dtype=complex)
    for p in range(6):
        for q in range(6):
            for y in range(4):
                for v in range(4):
                    original[6*p+q, 9*y+8-q-v, 4*(8-p-y)+v] = 1
    replay = np.einsum("ia,jb,kc,abc->ijk", *original_maps, original, optimize=True)
    assert np.max(np.abs(replay-base)) < 2e-11
    auxiliary = ASSIGNMENTS[assignment]
    ranks = len(auxiliary)
    source = np.zeros(tuple(d+ranks for d in base.shape), dtype=complex)
    source[:25, :20, :20] = base
    for k in range(ranks):
        source[25+k, 20+k, 20+k] = 1
    source_weights = [[2*record["weight"]-offset for record in rows
                       for _ in record["generic_rows"]]
                      for rows, offset in zip(data["local_records"], [10, 11, 11])]
    for axis in range(3):
        source_weights[axis].extend(row[axis] for row in auxiliary)
    target = np.zeros((25, 20, 20), dtype=complex)
    for i in range(5):
        for j in range(5):
            for k in range(4):
                target[5*i+j, 4*j+k, 5*k+i] = 1
    target_weights = [[2*i-2*j for i in range(5) for j in range(5)],
                      [2*j-2*k-1 for j in range(5) for k in range(4)],
                      [2*k-2*i+1 for k in range(4) for i in range(5)]]
    for point in zip(*np.nonzero(source)):
        assert sum(source_weights[k][point[k]] for k in range(3)) == 0
    for point in zip(*np.nonzero(target)):
        assert sum(target_weights[k][point[k]] for k in range(3)) == 0
    return source, target, source_weights, target_weights, original_maps, data


def fit(args):
    import numpy as np
    source, target, sw, tw, original_maps, data = model(args.family, args.assignment)
    rng = np.random.default_rng(args.seed)
    masks = [np.asarray(t)[:, None] == np.asarray(s)[None, :] for s, t in zip(sw, tw)]
    maps = [(rng.normal(size=mask.shape)+1j*rng.normal(size=mask.shape))*mask/3 for mask in masks]
    norm = float(np.linalg.norm(target))
    histories, best = [], float("inf")
    started = time.monotonic()
    base_dimensions = [25, 20, 20]
    for iteration in range(args.iterations+1):
        if iteration % args.report_every == 0 or iteration == args.iterations:
            actual = np.einsum("ia,jb,kc,abc->ijk", *maps, source, optimize=True)
            difference = actual-target
            error = float(np.linalg.norm(difference)/norm)
            norms = [float(np.linalg.norm(matrix)) for matrix in maps]
            singular_values = [np.linalg.svd(matrix[:, :d], compute_uv=False).tolist()
                               for matrix, d in zip(maps, base_dimensions)]
            row = dict(iteration=iteration, relative_coefficient_error=error,
                       maximum_coefficient_error=float(np.max(np.abs(difference))),
                       map_frobenius_norms=norms,
                       base_map_minimum_singular_values=[float(s[-1]) for s in singular_values],
                       elapsed_seconds=time.monotonic()-started)
            histories.append(row)
            print(json.dumps(dict(assignment=args.assignment, seed=args.seed, **row)), flush=True)
            if error < best:
                best = error
                composed = [matrix[:, :d]@original_map
                            for matrix, d, original_map in zip(maps, base_dimensions, original_maps)]
                record = dict(source="prescribed root14 point of Q(6,4), direct_sum D6",
                              target="M(5,4,5)", exact_witness=False, improves_omega=False,
                              family_file=str(args.family),
                              family_sha256=hashlib.sha256(args.family.read_bytes()).hexdigest(),
                              auxiliary_weights=ASSIGNMENTS[args.assignment],
                              auxiliary_border_rank_upper_bound=6,
                              source_weights=sw, target_weights=tw,
                              free_complex_parameters=sum(int(mask.sum()) for mask in masks),
                              all_coefficient_positions_checked=target.size,
                              seed=args.seed, assignment=args.assignment,
                              maximum_updates=args.iterations, map_norm_budget=args.norm_budget,
                              numerical_rank_cutoff=args.rcond,
                              relative_coefficient_error=error, history=histories,
                              maps_real=[m.real.tolist() for m in maps],
                              maps_imag=[m.imag.tolist() for m in maps],
                              composed_Q64_maps_real=[m.real.tolist() for m in composed],
                              composed_Q64_maps_imag=[m.imag.tolist() for m in composed],
                              exact_base_maps_cyclotomic=data["maps"],
                              original_source_coordinate_convention="A_(p,q), B_(y,8−q−v), C_(8−p−y,v)")
                args.output.write_text(json.dumps(record, indent=2)+"\n")
            if error < 1e-12 or max(norms) > args.norm_budget:
                break
        if iteration == args.iterations:
            break
        for axis in range(3):
            others = [j for j in range(3) if j != axis]
            tensor = np.transpose(source, (axis, *others))
            environment = np.einsum("abc,jb,kc->ajk", tensor, maps[others[0]], maps[others[1]], optimize=True)
            rhs = np.transpose(target, (axis, *others)).reshape(target.shape[axis], -1)
            environment = environment.reshape(source.shape[axis], -1)
            updated = np.zeros_like(maps[axis])
            for weight in sorted(set(tw[axis])):
                rows = np.flatnonzero(np.asarray(tw[axis]) == weight)
                columns = np.flatnonzero(np.asarray(sw[axis]) == weight)
                design = environment[columns].T
                if args.ridge:
                    design = np.vstack([design, np.sqrt(args.ridge)*np.eye(len(columns))])
                    block_rhs = np.vstack([rhs[rows].T, np.zeros((len(columns), len(rows)))])
                else:
                    block_rhs = rhs[rows].T
                solution = np.linalg.lstsq(design, block_rhs, rcond=args.rcond)[0]
                updated[np.ix_(rows, columns)] = solution.T
            maps[axis] = updated
        norms = [float(np.linalg.norm(matrix)) for matrix in maps]
        if min(norms) < 1e-100 or not all(np.isfinite(norms)):
            break
        common = float(np.prod(norms))**(1/3)
        maps = [matrix*(common/size) for matrix, size in zip(maps, norms)]
    record["history"] = histories
    record["updates_completed"] = iteration
    record["best_relative_coefficient_error"] = best
    record["stopped_by_norm_budget"] = max(norms) > args.norm_budget
    args.output.write_text(json.dumps(record, indent=2)+"\n")
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", type=Path, required=True)
    parser.add_argument("--assignment", type=int, choices=range(len(ASSIGNMENTS)), default=0)
    parser.add_argument("--seed", type=int, default=202610431)
    parser.add_argument("--iterations", type=int, default=1200)
    parser.add_argument("--report-every", type=int, default=100)
    parser.add_argument("--norm-budget", type=float, default=100)
    parser.add_argument("--rcond", type=float, default=1e-12)
    parser.add_argument("--ridge", type=float, default=1e-10)
    parser.add_argument("--output", type=Path, required=True)
    fit(parser.parse_args())
