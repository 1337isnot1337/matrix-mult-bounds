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


def model(path, assignment, partial=False, release_long=False, release_first=False,
          weight_modulus=0, inner_weights=(-1, -3, -5, -7)):
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
    source_weights = [[2*record["weight"]-offset for record in rows
                       for _ in record["generic_rows"]]
                      for rows, offset in zip(data["local_records"], [10, 11, 11])]
    target = np.zeros((25, 20, 20), dtype=complex)
    for i in range(5):
        for j in range(5):
            for k in range(4):
                target[5*i+j, 4*j+k, 5*k+i] = 1
    target_weights = [[2*i-2*j for i in range(5) for j in range(5)],
                      [2*j+inner_weights[k] for j in range(5) for k in range(4)],
                      [-inner_weights[k]-2*i for k in range(4) for i in range(5)]]
    if release_first:
        assert release_long, "The first-leg release is implemented with both long legs released."
        original_maps[0] = np.eye(36, dtype=complex)
        source_weights[0] = [2*(p+q)-10 for p in range(6) for q in range(6)]
        data["maps"][0] = [[["1"] if i == j else [] for j in range(36)] for i in range(36)]
    if release_long:
        original_maps[1] = np.eye(36, dtype=complex)
        original_maps[2] = np.eye(36, dtype=complex)
        base = np.einsum("ia,abc->ibc", original_maps[0], original, optimize=True)
        source_weights[1] = [2*(y+j)-11 for y in range(4) for j in range(9)]
        source_weights[2] = [2*(z+v)-11 for z in range(9) for v in range(4)]
        for axis in (1, 2):
            data["maps"][axis] = [[["1"] if i == j else [] for j in range(36)] for i in range(36)]
    auxiliary = [] if partial else ASSIGNMENTS[assignment]
    if partial:
        source_keep = (list(range(len(source_weights[0]))) if release_first or weight_modulus
                       else [i for i, w in enumerate(source_weights[0]) if w in (-4, -2, 2, 4)])
        target_keep = [i for i, w in enumerate(target_weights[0]) if w in (-4, -2, 2, 4)]
        base = base[source_keep]
        target = target[target_keep]
        source_weights[0] = [source_weights[0][i] for i in source_keep]
        target_weights[0] = [target_weights[0][i] for i in target_keep]
        original_maps[0] = original_maps[0][source_keep]
        data["maps"][0] = [data["maps"][0][i] for i in source_keep]
        data["bulk_target_A_coordinates"] = target_keep
        data["bulk_source_A_coordinates"] = source_keep
        data["omitted_target_A_coordinates"] = [i for i in range(25) if i not in target_keep]
    ranks = len(auxiliary)
    source = np.zeros(tuple(d+ranks for d in base.shape), dtype=complex)
    source[tuple(slice(0, d) for d in base.shape)] = base
    for k in range(ranks):
        source[tuple(d+k for d in base.shape)] = 1
    for axis in range(3):
        source_weights[axis].extend(row[axis] for row in auxiliary)
    for point in zip(*np.nonzero(source)):
        assert sum(source_weights[k][point[k]] for k in range(3)) == 0
    for point in zip(*np.nonzero(target)):
        assert sum(target_weights[k][point[k]] for k in range(3)) == 0
    return source, target, source_weights, target_weights, original_maps, data


def fit(args):
    import numpy as np
    inner_weights = tuple(int(x) for x in args.inner_weights.split(","))
    assert len(inner_weights) == 4
    source, target, sw, tw, original_maps, data = model(
        args.family, args.assignment, args.partial_bulk, args.release_long,
        args.release_first, args.weight_modulus, inner_weights)
    rng = np.random.default_rng(args.seed)
    source_labels = [[w % args.weight_modulus if args.weight_modulus else w for w in row] for row in sw]
    target_labels = [[w % args.weight_modulus if args.weight_modulus else w for w in row] for row in tw]
    masks = [np.asarray(t)[:, None] == np.asarray(s)[None, :] for s, t in zip(source_labels, target_labels)]
    maps = [(rng.normal(size=mask.shape)+1j*rng.normal(size=mask.shape))*mask/3 for mask in masks]
    if args.resume:
        previous = json.loads(args.resume.read_text())
        maps = [np.asarray(real)+1j*np.asarray(imag)
                for real, imag in zip(previous["maps_real"], previous["maps_imag"])]
        assert all(matrix.shape == mask.shape for matrix, mask in zip(maps, masks))
        maps = [(matrix+args.resume_noise*(rng.normal(size=mask.shape)+1j*rng.normal(size=mask.shape)))*mask
                for matrix, mask in zip(maps, masks)]
    norm = float(np.linalg.norm(target))
    histories, best = [], float("inf")
    started = time.monotonic()
    base_dimensions = [matrix.shape[0] for matrix in original_maps]
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
                source_name = ("full Q(6,4) source" if args.release_first
                               else "prescribed root14 A image of Q(6,4)" if args.release_long
                               else "prescribed root14 point of Q(6,4)")
                record = dict(source=source_name+("" if args.partial_bulk else ", direct_sum D6"),
                              target="M(5,4,5) restricted to outer diagonals of offsets ±1,±2" if args.partial_bulk else "M(5,4,5)",
                              exact_witness=False, improves_omega=False,
                              family_file=str(args.family),
                              family_sha256=hashlib.sha256(args.family.read_bytes()).hexdigest(),
                              auxiliary_weights=[] if args.partial_bulk else ASSIGNMENTS[args.assignment],
                              auxiliary_border_rank_upper_bound=0 if args.partial_bulk else 6,
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
                if args.partial_bulk:
                    for key in ["bulk_target_A_coordinates", "bulk_source_A_coordinates", "omitted_target_A_coordinates"]:
                        record[key] = data[key]
                    record["naive_rank_cost_to_restore_omitted_target_entries"] = 4*len(data["omitted_target_A_coordinates"])
                record["released_long_source_spaces"] = args.release_long
                record["released_first_source_space"] = args.release_first
                record["weight_modulus"] = args.weight_modulus
                record["inner_weights"] = inner_weights
                record["target_gauge_balancing"] = args.balance_target
                record["resume_file"] = str(args.resume) if args.resume else None
                record["resume_noise"] = args.resume_noise
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
            for weight in sorted(set(target_labels[axis])):
                rows = np.flatnonzero(np.asarray(target_labels[axis]) == weight)
                columns = np.flatnonzero(np.asarray(source_labels[axis]) == weight)
                design = environment[columns].T
                if args.ridge:
                    design = np.vstack([design, np.sqrt(args.ridge)*np.eye(len(columns))])
                    block_rhs = np.vstack([rhs[rows].T, np.zeros((len(columns), len(rows)))])
                else:
                    block_rhs = rhs[rows].T
                solution = np.linalg.lstsq(design, block_rhs, rcond=args.rcond)[0]
                updated[np.ix_(rows, columns)] = solution.T
            maps[axis] = updated
        if args.balance_target and iteration % 10 == 0:
            target_coordinates = data.get("bulk_target_A_coordinates", list(range(25)))
            maps = balance_target(maps, target_coordinates, inner_weights, args.weight_modulus)
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


def balance_target(maps, coordinates, inner_weights, modulus):
    """Apply the diagonal-outer and allowed GL4-middle stabilizer of the target."""
    import numpy as np
    A, B, C = [matrix.copy() for matrix in maps]
    B = B.reshape(5, 4, -1)
    C = C.reshape(4, 5, -1)
    labels = np.asarray(inner_weights)
    if modulus:
        labels = labels % modulus
    for left in range(5):
        rows = [r for r, coordinate in enumerate(coordinates) if coordinate//5 == left]
        ea, ec = np.linalg.norm(A[rows])**2, np.linalg.norm(C[:, left])**2
        if min(ea, ec) > 1e-24:
            factor = (ec/ea)**0.25
            A[rows] *= factor
            C[:, left] /= factor
    for right in range(5):
        rows = [r for r, coordinate in enumerate(coordinates) if coordinate%5 == right]
        ea, eb = np.linalg.norm(A[rows])**2, np.linalg.norm(B[right])**2
        if min(ea, eb) > 1e-24:
            factor = (eb/ea)**0.25
            A[rows] *= factor
            B[right] /= factor

    def positive_power(matrix, exponent):
        values, vectors = np.linalg.eigh((matrix+matrix.conj().T)/2)
        floor = max(1e-20, float(np.max(values))*1e-14)
        return (vectors*np.maximum(values, floor)**exponent)@vectors.conj().T

    for label in sorted(set(labels)):
        block = np.flatnonzero(labels == label)
        b, c = B[:, block], C[block]
        hb = np.einsum("jka,jla->kl", b, b.conj())
        hc = np.einsum("kia,lia->kl", c, c.conj()).T
        root = positive_power(hb, .5)
        inverse_root = positive_power(hb, -.5)
        x = inverse_root@positive_power(root@hc@root, .5)@inverse_root
        g = positive_power(x, .5)
        B[:, block] = np.einsum("kl,jla->jka", g, b)
        C[block] = np.einsum("kl,lia->kia", np.linalg.inv(g).T, c)
    return [A, B.reshape(20, -1), C.reshape(20, -1)]


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
    parser.add_argument("--partial-bulk", action="store_true")
    parser.add_argument("--release-long", action="store_true")
    parser.add_argument("--release-first", action="store_true")
    parser.add_argument("--weight-modulus", type=int, default=0)
    parser.add_argument("--inner-weights", default="-1,-3,-5,-7")
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--resume-noise", type=float, default=0)
    parser.add_argument("--balance-target", action="store_true")
    fit(parser.parse_args())
