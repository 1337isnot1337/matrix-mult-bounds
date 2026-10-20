"""Discover graded identities with an unrestricted constant shared basis.

Floating output is never proof acceptance. Checkpoints are saved in the worktree.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

spec = importlib.util.spec_from_file_location('fatpoint', Path(__file__).with_name('fatpoint_route.py'))
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def problem(a, extra):
    dims, terms = target.tensor(a)
    n, b = dims[1], dims[1]+extra
    r = b+a-1
    degrees = np.array([d for d in range(a) for _ in range(d+1)])
    desired = np.zeros((a, n, n))
    for i, y, z in terms:
        desired[i, z, y] = 1
    ii, zz, yy = np.nonzero(np.broadcast_to(
        degrees[:, None]+degrees[None, :] <= a-1, (a, n, n)))
    bp, bq = b*n, n*r
    rows = np.arange(len(ii))[:, None]
    j, h = np.arange(b), np.arange(a)

    def unpack(x):
        return (x[:bp].reshape(b, n), x[bp:bp+bq].reshape(n, r),
                x[bp+bq:].reshape(a, a))

    def fun(x):
        p, q, g = unpack(x)
        basis = np.stack([q[:, k:k+b]@p for k in range(a)])
        actual = np.einsum('ih,hzy->izy', g, basis)
        return actual[ii, zz, yy]-desired[ii, zz, yy]

    def jac(x):
        p, q, g = unpack(x)
        result = np.zeros((len(ii), bp+bq+a*a))
        qvalues = q[zz[:, None, None], h[None, :, None]+j[None, None, :]]
        dp = np.einsum('mh,mhb->mb', g[ii], qvalues)
        result[rows, j[None, :]*n+yy[:, None]] = dp
        dq = np.zeros((len(ii), r))
        for k in range(a):
            dq[:, k:k+b] += g[ii, k, None]*p[:, yy].T
        result[rows, bp+zz[:, None]*r+np.arange(r)[None, :]] = dq
        dg = np.stack([(q[:, k:k+b]@p)[zz, yy] for k in range(a)], axis=1)
        result[rows, bp+bq+ii[:, None]*a+h[None, :]] = dg
        return result

    return n, b, unpack, fun, jac


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a', type=int, required=True)
    parser.add_argument('--extra', type=int, default=0)
    parser.add_argument('--budget', type=int, default=500)
    parser.add_argument('--seed', type=int, default=20261220)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    n, b, unpack, fun, jac = problem(args.a, args.extra)
    rng = np.random.default_rng(args.seed)
    size = b*n+n*(b+args.a-1)+args.a**2
    initial = rng.normal(size=size)/np.sqrt(n)
    initial[-args.a**2:] = (np.eye(args.a)+0.1*rng.normal(size=(args.a, args.a))).ravel()
    analytic = jac(initial)
    error = 0.
    for column in rng.choice(size, min(12, size), replace=False):
        shift = np.zeros(size)
        shift[column] = 1e-6
        numeric = (fun(initial+shift)-fun(initial-shift))/(2e-6)
        error = max(error, float(np.max(np.abs(numeric-analytic[:, column]))))
    if error > 1e-6:
        raise ValueError(('analytic Jacobian check failed', error))
    iterations = 0

    def save(x, status):
        p, q, g = unpack(x)
        np.savez(args.output_dir/'candidate.npz', P=p, Q=q, G=g)
        report = {
            'a': args.a, 'N': n, 'B': b, 'seed': args.seed,
            'max_nfev': args.budget, 'callback_iterations': iterations,
            'residual_l2_descriptive': float(np.linalg.norm(fun(x))),
            'P_smallest_singular_value': float(np.linalg.svd(p, compute_uv=False)[-1]),
            'Q_smallest_singular_value': float(np.linalg.svd(q, compute_uv=False)[-1]),
            'G_smallest_singular_value': float(np.linalg.svd(g, compute_uv=False)[-1]),
            'largest_coefficient': float(np.max(np.abs(x))),
            'jacobian_finite_difference_error': error,
            'status': status, 'exact_certificate': False,
        }
        (args.output_dir/'discovery.json').write_text(json.dumps(report, indent=2)+'\n')
        return report

    def checkpoint(x):
        nonlocal iterations
        iterations += 1
        if iterations % 20 == 0:
            report = save(x, 'running floating discovery; not an exact certificate')
            print(json.dumps(report), flush=True)

    solution = least_squares(fun, initial, jac=jac, callback=checkpoint,
        max_nfev=args.budget, ftol=1e-13, xtol=1e-13, gtol=1e-13)
    report = save(solution.x, 'finished floating discovery; not an exact certificate')
    report['nfev'] = solution.nfev
    (args.output_dir/'discovery.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
