"""Bounded diagonal-output-flag search for the partial M(5,4,5) tensor.

This is numerical discovery only.  Every Laurent coefficient of exponent
at most zero is included, with negative coefficients required to vanish.
The exact old seed is the two off-diagonal entries of the monomial M2
injection U=span(1,t^2), W=span(1,t).
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time


def build(old_vertices):
    import numpy as np
    source = np.zeros((36, 36, 36), dtype=complex)
    for p in range(6):
        for q in range(6):
            for y in range(4):
                for v in range(4):
                    source[6*p+q, 9*y+8-q-v, 4*(8-p-y)+v] = 1
    coordinates = [5*i+j for i in range(5) for j in range(5) if abs(i-j) in (1, 2)]
    target = np.zeros((14, 20, 20), dtype=complex)
    for row, coordinate in enumerate(coordinates):
        i, j = divmod(coordinate, 5)
        for k in range(4):
            target[row, 4*j+k, 5*k+i] = 1
    old = set(old_vertices)
    flags = [[-int(c//5 not in old)-int(c%5 not in old) for c in coordinates],
             [int(j not in old) for j in range(5) for k in range(4)],
             [int(i not in old) for k in range(4) for i in range(5)]]
    weights = np.asarray(flags[0])[:, None, None]+np.asarray(flags[1])[None, :, None]+np.asarray(flags[2])[None, None, :]
    assert np.all(weights[np.nonzero(target)] == 0)
    maps = [np.zeros((d, 36), dtype=complex) for d in target.shape]
    for ii, i in enumerate(old_vertices):
        for jj, j in enumerate(old_vertices):
            coordinate = 5*i+j
            if coordinate in coordinates:
                maps[0][coordinates.index(coordinate), 6*(2*ii)+2*jj] = 1
        for y in range(2):
            for v in range(2):
                k = 2*y+v
                maps[1][4*i+k, 9*y+8-2*ii-v] = 1
                maps[2][5*k+i, 4*(8-2*ii-y)+v] = 1
    fixed = [[i for i, w in enumerate(axis) if w == 0] for axis in flags]
    seeded = np.einsum("ia,jb,kc,abc->ijk", *maps, source, optimize=True)
    expected = target.copy()
    expected[[i for i, w in enumerate(flags[0]) if w != 0]] = 0
    assert np.array_equal(seeded, expected)
    # All surviving source A entries lie in p,q<4.  Their y=v=0
    # coefficients give an explicit 16-by-16 identity flattening minor.
    pre_a = np.einsum("jb,kc,abc->ajk", maps[1], maps[2], source, optimize=True)
    assert np.linalg.matrix_rank(pre_a.reshape(36, -1)) == 16
    assert sum(len(row) for row in fixed) == 18
    return source, target, coordinates, flags, weights, maps, fixed


def fit(args):
    import numpy as np
    old = tuple(int(v) for v in args.old_vertices.split(","))
    assert len(old) == 2 and abs(old[0]-old[1]) in (1, 2)
    source, target, coordinates, flags, weights, maps, fixed = build(old)
    seed_sparse = [[[int(i), int(j), int(matrix[i, j].real)] for i, j in zip(*np.nonzero(matrix))]
                   for matrix in maps]
    rng = np.random.default_rng(args.seed)
    for axis in (1, 2):
        free = [i for i in range(target.shape[axis]) if i not in fixed[axis]]
        maps[axis][free] = (rng.normal(size=(len(free), 36))+1j*rng.normal(size=(len(free), 36)))/6
    if args.release_seed:
        fixed = [[], [], []]
    if args.resume:
        previous = json.loads(args.resume.read_text())
        maps = [np.asarray(real)+1j*np.asarray(imag)
                for real, imag in zip(previous["maps_real"], previous["maps_imag"])]
    spec = importlib.util.spec_from_file_location("bulk_target_balancer", Path(__file__).with_name("q64_quantum_correction.py"))
    balancer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(balancer)
    mask, negative, zero = weights <= 0, weights < 0, weights == 0
    norm = float(np.linalg.norm(target))
    history, best = [], float("inf")
    started = time.monotonic()
    grouped = []
    for axis in range(3):
        others = [j for j in range(3) if j != axis]
        axis_mask = np.transpose(mask, (axis, *others)).reshape(target.shape[axis], -1)
        rhs = np.transpose(target, (axis, *others)).reshape(target.shape[axis], -1)
        axis_groups = []
        for weight in sorted(set(flags[axis])):
            rows = [i for i, w in enumerate(flags[axis]) if w == weight and i not in fixed[axis]]
            if rows:
                axis_groups.append((rows, axis_mask[rows[0]], rhs[rows]))
        grouped.append(axis_groups)
    for iteration in range(args.iterations+1):
        if iteration % args.report_every == 0 or iteration == args.iterations:
            actual = np.einsum("ia,jb,kc,abc->ijk", *maps, source, optimize=True)
            difference = actual-target
            error = float(np.linalg.norm(difference[mask])/norm)
            norms = [float(np.linalg.norm(m)) for m in maps]
            row = dict(iteration=iteration, relative_constrained_coefficient_error=error,
                       maximum_negative_coefficient=float(np.max(np.abs(actual[negative]))),
                       relative_zero_weight_target_error=float(np.linalg.norm(difference[zero])/norm),
                       maximum_zero_weight_error=float(np.max(np.abs(difference[zero]))),
                       positive_coefficients_ignored_maximum=float(np.max(np.abs(actual[~mask]))),
                       map_frobenius_norms=norms,
                       minimum_map_singular_values=[float(np.linalg.svd(m, compute_uv=False)[-1]) for m in maps],
                       elapsed_seconds=time.monotonic()-started)
            history.append(row)
            print(json.dumps(dict(seed=args.seed, old_vertices=old, **row)), flush=True)
            if error < best:
                best = error
                record = dict(source="Q(6,4)", source_format=[36, 36, 36],
                              original_source_coordinate_convention="A_(p,q), B_(y,8-q-v), C_(8-p-y,v)",
                              target="M(5,4,5) with A offsets ±1,±2 retained", target_format=[14, 20, 20],
                              target_A_coordinates=coordinates, output_Laurent_weights=flags,
                              exact_seed_maps_sparse=seed_sparse, seed_pre_A_rank=16,
                              old_vertices=old, fixed_output_rows=fixed,
                              fixed_seed_scope="old row spaces up to the target stabilizer" if not args.release_seed else "initialization only",
                              all_negative_and_zero_coefficients_checked=int(mask.sum()),
                              negative_coefficients_checked=int(negative.sum()),
                              zero_coefficients_checked=int(zero.sum()),
                              positive_coefficients_omitted=int((~mask).sum()),
                              target_rank_one_terms=56, omitted_target_repair_rank_upper_bound=44,
                              exact_witness=False, improves_omega=False,
                              seed=args.seed, ridge=args.ridge, numerical_rank_cutoff=args.rcond,
                              maximum_updates=args.iterations, sampled_norm_budget=args.norm_budget,
                              sampled_norm_interval=args.report_every, target_stabilizer_balancing=args.balance_target,
                              relative_constrained_coefficient_error=error,
                              maps_real=[m.real.tolist() for m in maps], maps_imag=[m.imag.tolist() for m in maps],
                              history=history)
                args.output.write_text(json.dumps(record, indent=2)+"\n")
            if error < 1e-12 or max(norms) > args.norm_budget:
                break
        if iteration == args.iterations:
            break
        for axis in range(3):
            others = [j for j in range(3) if j != axis]
            reordered = np.transpose(source, (axis, *others))
            environment = np.einsum("abc,jb,kc->ajk", reordered, maps[others[0]], maps[others[1]], optimize=True)
            environment = environment.reshape(36, -1)
            for rows, active, rhs in grouped[axis]:
                design = environment[:, active].T
                values = rhs[:, active].T
                if args.ridge:
                    design = np.vstack([design, np.sqrt(args.ridge)*np.eye(36)])
                    values = np.vstack([values, np.zeros((36, len(rows)))])
                maps[axis][rows] = np.linalg.lstsq(design, values, rcond=args.rcond)[0].T
        if args.balance_target and iteration % 10 == 0:
            maps = balancer.balance_target(maps, coordinates, [-1, -3, -5, -7], 1)
        norms = [float(np.linalg.norm(m)) for m in maps]
        if min(norms) < 1e-100 or not all(np.isfinite(norms)):
            break
        geometric_mean = float(np.prod(norms))**(1/3)
        maps = [m*(geometric_mean/n) for m, n in zip(maps, norms)]
    record["history"] = history
    record["updates_completed"] = iteration
    record["best_relative_constrained_coefficient_error"] = best
    record["stopped_by_sampled_norm_budget"] = max(norms) > args.norm_budget
    args.output.write_text(json.dumps(record, indent=2)+"\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--old-vertices", default="0,1")
    parser.add_argument("--seed", type=int, default=202610451)
    parser.add_argument("--iterations", type=int, default=1200)
    parser.add_argument("--report-every", type=int, default=200)
    parser.add_argument("--ridge", type=float, default=1e-10)
    parser.add_argument("--rcond", type=float, default=1e-12)
    parser.add_argument("--norm-budget", type=float, default=100)
    parser.add_argument("--balance-target", action="store_true")
    parser.add_argument("--release-seed", action="store_true")
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    fit(parser.parse_args())
