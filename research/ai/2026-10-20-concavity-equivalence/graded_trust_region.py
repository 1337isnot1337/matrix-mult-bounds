"""Trust-region discovery with an analytic Jacobian; no proof acceptance."""
import argparse
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

spec = importlib.util.spec_from_file_location('fatpoint', Path(__file__).with_name('fatpoint_route.py'))
target = importlib.util.module_from_spec(spec)
spec.loader.exec_module(target)


def run(a, budget, seed, width_extra=0):
    dims, terms = target.tensor(a)
    n, b = dims[1], dims[1]+width_extra
    r = b+a-1
    degrees = np.array([d for d in range(a) for _ in range(d+1)])
    desired = np.zeros((a, n, n))
    for i, y, z in terms:
        desired[i, z, y] = 1
    ii, zz, yy = np.nonzero(np.broadcast_to(
        degrees[:, None]+degrees[None, :] <= a-1, (a, n, n)))
    h = np.arange(b)
    pp = h[None, :]*n+yy[:, None]
    qq = b*n+zz[:, None]*r+ii[:, None]+h[None, :]
    rows = np.arange(len(ii))[:, None]

    def unpack(x):
        return x[:b*n].reshape(b, n), x[b*n:].reshape(n, r)

    def fun(x):
        p, q = unpack(x)
        return np.sum(q[zz[:, None], ii[:, None]+h] * p[h[None, :], yy[:, None]], axis=1)-desired[ii, zz, yy]

    def jac(x):
        p, q = unpack(x)
        result = np.zeros((len(ii), b*n+n*r))
        result[rows, pp] = q[zz[:, None], ii[:, None]+h]
        result[rows, qq] = p[h[None, :], yy[:, None]]
        return result

    rng = np.random.default_rng(seed)
    initial = rng.normal(size=b*n+n*r)/np.sqrt(n)
    solution = least_squares(fun, initial, jac=jac, max_nfev=budget,
                             ftol=1e-13, xtol=1e-13, gtol=1e-13)
    p, q = unpack(solution.x)
    return {
        'a': a, 'N': n, 'source_B': b, 'seed': seed,
        'max_nfev': budget, 'nfev': solution.nfev,
        'residual_l2_descriptive': float(np.linalg.norm(fun(solution.x))),
        'P_smallest_singular_value': float(np.linalg.svd(p, compute_uv=False)[-1]),
        'Q_smallest_singular_value': float(np.linalg.svd(q, compute_uv=False)[-1]),
        'largest_coefficient': float(max(np.max(np.abs(p)), np.max(np.abs(q)))),
        'status': 'floating discovery only; no exact coefficient certificate',
    }, p, q


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--min-a', type=int, default=3)
    parser.add_argument('--max-a', type=int, default=6)
    parser.add_argument('--budget', type=int, default=300)
    parser.add_argument('--width-extra', type=int, default=0)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    reports = []
    for a in range(args.min_a, args.max_a+1):
        report, p, q = run(a, args.budget, 20261120+a, args.width_extra)
        np.savez(args.output_dir/f'candidate-a{a}.npz', P=p, Q=q)
        reports.append(report)
        (args.output_dir/'discovery.json').write_text(json.dumps(reports, indent=2)+'\n')
        print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
