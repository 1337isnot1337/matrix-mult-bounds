"""Floating discovery of graded coefficient identities; never an acceptance test."""
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location('fatpoint', Path(__file__).with_name('fatpoint_route.py'))
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def discover(a, iterations, seed, width_extra=0):
    dims, terms = target.tensor(a)
    n = dims[1]
    b = n+width_extra
    r = b+a-1
    degrees = np.array([d for d in range(a) for _ in range(d+1)])
    desired = np.zeros((a, n, n))  # shared, output, input
    for x, y, z in terms:
        desired[x, z, y] = 1
    rng = np.random.default_rng(seed)
    p = rng.normal(size=(b, n))/np.sqrt(b)
    q = np.zeros((n, r))
    best = None
    best_error = float('inf')
    for step in range(iterations):
        for z in range(n):
            keep = np.flatnonzero(degrees <= a-1-degrees[z])
            design = np.zeros((a*len(keep), r))
            for i in range(a):
                design[i*len(keep):(i+1)*len(keep), i:i+b] = p[:, keep].T
            rhs = desired[:, z, :][:, keep].reshape(-1)
            q[z] = np.linalg.lstsq(design, rhs, rcond=1e-12)[0]
        for y in range(n):
            keep = np.flatnonzero(degrees <= a-1-degrees[y])
            design = np.vstack([q[keep, i:i+b] for i in range(a)])
            p[:, y] = np.linalg.lstsq(design, desired[:, :, y][:, keep].reshape(-1), rcond=1e-12)[0]
        scale = np.linalg.norm(p)/np.sqrt(n)
        if scale:
            p /= scale
            q *= scale
        actual = np.stack([q[:, i:i+b]@p for i in range(a)])
        mask = degrees[:, None]+degrees[None, :] <= a-1
        error = float(np.linalg.norm((actual-desired)[:, mask]))
        if error < best_error:
            best_error = error
            best = (p.copy(), q.copy(), step)
        if error < 1e-10:
            break
    p, q, step = best
    return {
        'a': a, 'N': n, 'source_B': b, 'seed': seed,
        'iterations_requested': iterations, 'best_iteration': step,
        'residual_l2_descriptive': best_error,
        'P_smallest_singular_value': float(np.linalg.svd(p, compute_uv=False)[-1]),
        'Q_smallest_singular_value': float(np.linalg.svd(q, compute_uv=False)[-1]),
        'largest_coefficient': float(max(np.max(np.abs(p)), np.max(np.abs(q)))),
        'status': 'floating discovery only; no exact certificate',
    }, p, q


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--min-a', type=int, default=2)
    parser.add_argument('--max-a', type=int, default=8)
    parser.add_argument('--iterations', type=int, default=500)
    parser.add_argument('--seed', type=int, default=20261020)
    parser.add_argument('--width-extra', type=int, default=0)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    reports = []
    for a in range(args.min_a, args.max_a+1):
        report, p, q = discover(a, args.iterations, args.seed+a, args.width_extra)
        np.savez(args.output_dir/f'candidate-a{a}.npz', P=p, Q=q)
        reports.append(report)
        (args.output_dir/'discovery.json').write_text(json.dumps(reports, indent=2)+'\n')
        print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
