"""Exact grading allocation and optional NumPy discovery; no exponent claim."""

from collections import Counter, defaultdict
from itertools import product
import argparse
import json
from pathlib import Path
import sys
import time


def example(a=10):
    if a == 10:
        return [
            (list(range(4)), [9, 10, 11, 12, 14, 15, 18, 19, 20, 23, 24], list(range(10))),
            (list(range(10)), [10, 13, 14, 16, 17, 18, 20, 21, 22, 23, 24, 27], list(range(4, 10))),
        ]
    if a == 2:
        return [(list(range(2)), [1, 2], list(range(2)))]
    raise ValueError("Only the specified control and target are supplied")


def coordinates(a, blocks):
    h = 2*a-1
    source = [list(product(range(a), repeat=2)),
              list(product(range(a), range(h))), list(product(range(h), range(a)))]
    sw = [[p+q for p, q in source[0]], [y+h-1-j for y, j in source[1]],
          [h-1-z+v for z, v in source[2]]]
    target = [[], [], []]
    tw = [[], [], []]
    terms = []
    offsets = [0, 0, 0]
    for block, (alpha, beta, gamma) in enumerate(blocks):
        ll, bb, rr = len(alpha), len(beta), len(gamma)
        for i, k in product(range(ll), range(rr)):
            target[0].append((block, i, k)); tw[0].append(alpha[i]+gamma[k])
        for i, j in product(range(ll), range(bb)):
            target[1].append((block, i, j)); tw[1].append(beta[j]-alpha[i])
        for j, k in product(range(bb), range(rr)):
            target[2].append((block, j, k)); tw[2].append(4*a-4-beta[j]-gamma[k])
        for i, j, k in product(range(ll), range(bb), range(rr)):
            terms.append((offsets[0]+i*rr+k, offsets[1]+i*bb+j, offsets[2]+j*rr+k))
        offsets = [len(axis) for axis in target]
    si = [{label: i for i, label in enumerate(axis)} for axis in source]
    st = [(si[0][p, q], si[1][y, q+v], si[2][p+y, v])
          for p, q, y, v in product(range(a), repeat=4)]
    return source, sw, st, target, tw, terms


def grade_certificate(a=10):
    blocks = example(a)
    source, sw, st, target, tw, tt = coordinates(a, blocks)
    profiles = []
    for axis in range(3):
        s, t = Counter(sw[axis]), Counter(tw[axis])
        if any(t[w] > s[w] for w in t):
            raise ArithmeticError("Target exceeds a source weight space")
        profiles.append([{"weight": w, "source": s[w], "target": t[w], "slack": s[w]-t[w]}
                         for w in sorted(set(s)|set(t))])
    if Counter(sw[0]) != Counter(tw[0]):
        raise ArithmeticError("The target is intended to use the full first leg")
    for terms, weights in [(st, sw), (tt, tw)]:
        if any(sum(weights[k][term[k]] for k in range(3)) != 4*a-4 for term in terms):
            raise ArithmeticError("A coefficient violates the grading")
    return {"a": a, "blocks": [{"alpha": x, "beta": y, "gamma": z} for x, y, z in blocks],
            "source_dimensions": list(map(len, source)), "target_dimensions": list(map(len, target)),
            "source_terms_checked": len(st), "target_terms_checked": len(tt),
            "weight_profiles": profiles, "graded_map_parameter_count": sum(
                sum(row["source"]*row["target"] for row in axis) for axis in profiles),
            "degeneration_constructed": False, "improves_omega": False}


def numerical_problem(a, graded=True):
    import numpy as np
    source, sw, st, target, tw, tt = coordinates(a, example(a))
    if not graded:
        sw = [[0]*len(axis) for axis in source]
        tw = [[0]*len(axis) for axis in target]
    sg, tg = [], []
    sl, tl = [], []
    for weights, groups, lookup in [(sw, sg, sl), (tw, tg, tl)]:
        for axis in range(3):
            g = defaultdict(list)
            for i, w in enumerate(weights[axis]): g[w].append(i)
            groups.append(dict(g))
            lookup.append({i: (w, j) for w, ids in g.items() for j, i in enumerate(ids)})
    support = set()
    for wa, wb, wc in product(*(sorted(x) for x in tg)):
        if wa+wb+wc == (4*a-4 if graded else 0): support.add((wa, wb, wc))
    sblocks, tblocks = {}, {}
    for w in sorted(support):
        sblocks[w] = np.zeros(tuple(len(sg[k][w[k]]) for k in range(3)))
        tblocks[w] = np.zeros(tuple(len(tg[k][w[k]]) for k in range(3)))
    for terms, lookup, arrays in [(st, sl, sblocks), (tt, tl, tblocks)]:
        for term in terms:
            pairs = [lookup[k][term[k]] for k in range(3)]
            w = tuple(x[0] for x in pairs)
            if w in arrays: arrays[w][tuple(x[1] for x in pairs)] += 1
    return sg, tg, sblocks, tblocks


def fit(a, seed, iterations, ridge, report_every, checkpoint, graded=True):
    """Finite alternating least squares. Floats never certify a construction."""
    import numpy as np
    sg, tg, source, target = numerical_problem(a, graded=graded)
    rng = np.random.default_rng(seed)
    maps = [{w: rng.normal(size=(len(tg[k][w]), len(sg[k][w])))/len(sg[k][w])**0.5
             for w in tg[k]} for k in range(3)]
    norm2 = sum(float((t*t).sum()) for t in target.values())
    history = []
    start = time.monotonic()
    for step in range(iterations+1):
        if step % report_every == 0 or step == iterations:
            loss = sum(float(((np.einsum("is,jt,ku,stu->ijk", maps[0][w[0]], maps[1][w[1]],
                      maps[2][w[2]], s, optimize=True)-target[w])**2).sum()) for w, s in source.items())
            sizes = [sum(float((m*m).sum()) for m in leg.values())**0.5 for leg in maps]
            row = {"iteration": step, "relative_residual": (loss/norm2)**0.5,
                   "map_frobenius_norms": sizes, "elapsed_seconds": time.monotonic()-start}
            history.append(row)
            print(json.dumps(row), flush=True)
            if checkpoint is not None:
                np.savez_compressed(checkpoint, **{f"map_{k}_{w}": v for k, leg in enumerate(maps) for w, v in leg.items()})
        if step == iterations: break
        for axis in range(3):
            gram = {w: np.zeros((len(sg[axis][w]),)*2) for w in tg[axis]}
            rhs = {w: np.zeros((len(tg[axis][w]), len(sg[axis][w]))) for w in tg[axis]}
            other = [k for k in range(3) if k != axis]
            for w, s in source.items():
                transposed = np.transpose(s, (axis, *other))
                u = np.einsum("jt,ku,stu->sjk", maps[other[0]][w[other[0]]],
                              maps[other[1]][w[other[1]]], transposed, optimize=True)
                u = u.reshape(u.shape[0], -1)
                t = np.transpose(target[w], (axis, *other)).reshape(len(tg[axis][w[axis]]), -1)
                gram[w[axis]] += u @ u.T
                rhs[w[axis]] += t @ u.T
            for w in tg[axis]:
                g = gram[w]
                g.flat[::g.shape[0]+1] += ridge
                maps[axis][w] = np.linalg.lstsq(g, rhs[w].T, rcond=1e-13)[0].T
        # Only global gauge rescaling, whose product is exactly one.
        sizes = [sum(float((m*m).sum()) for m in leg.values())**0.5 for leg in maps]
        common = float(np.prod(sizes))**(1/3)
        if min(sizes) == 0: break
        for k in range(3):
            for w in maps[k]: maps[k][w] *= common/sizes[k]
    return {"a": a, "seed": seed, "iterations_completed": step, "ridge": ridge,
            "python_version": sys.version.split()[0], "numpy_version": np.__version__,
            "history": history, "method": "alternating least squares over float64", "preserves_grading": graded,
            "degeneration_constructed": False, "improves_omega": False,
            "scope": "Numerical search only. Residuals are not existence or nonexistence certificates."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, default=10)
    parser.add_argument("--fit", action="store_true")
    parser.add_argument("--ungraded", action="store_true", help="Use unrestricted maps for a small calibration")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--ridge", type=float, default=1e-7)
    parser.add_argument("--report-every", type=int, default=10)
    parser.add_argument("--checkpoint", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = (fit(args.a, args.seed, args.iterations, args.ridge, args.report_every, args.checkpoint, not args.ungraded)
              if args.fit else grade_certificate(args.a))
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    if not args.fit: print(json.dumps({k: v for k, v in report.items() if k != "weight_profiles"}))
