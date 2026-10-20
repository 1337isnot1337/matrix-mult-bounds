"""Bounded exact-scored degenerations after a Chebyshev basis change."""
from fractions import Fraction
import argparse
import importlib.util
from itertools import product
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    'archived_recognition', ROOT/'research/ai/2026-10-20/search_degenerations.py')
archive = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archive)


def support(a, b):
    return [(0, j, j) for j in range(1, b)] + [
        (i, j, k) for i in range(1, a) for j in range(1, b)
        for k in (i+j, abs(i-j))]


def groups_and_weights(wx, wy):
    a, b = len(wx), len(wy)+1
    terms = support(a, b)
    minima = {}
    for i, j, k in terms:
        minima[k] = min(minima.get(k, wx[i]+wy[j-1]), wx[i]+wy[j-1])
    zero = [(i, j, k) for i, j, k in terms if wx[i]+wy[j-1] == minima[k]]
    parent = {}

    def root(v):
        parent.setdefault(v, v)
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for _, j, k in zero:
        parent[root((1, j))] = root((2, k))
    groups = {}
    for term in zero:
        groups.setdefault(root((1, term[1])), []).append(term)
    return list(groups.values()), {k: -v for k, v in minima.items()}


def slice_bound(terms):
    """Rank over F2 is a certified lower bound for these integer matrices."""
    best = 0
    for axis in range(3):
        others = [leg for leg in range(3) if leg != axis]
        slices = {}
        for term in terms:
            rows = slices.setdefault(term[axis], {})
            row, col = term[others[0]], term[others[1]]
            rows[row] = rows.get(row, 0) | (1 << col)
        for rows in slices.values():
            pivots = {}
            for value in rows.values():
                while value:
                    p = value.bit_length()-1
                    if p in pivots:
                        value ^= pivots[p]
                    else:
                        pivots[p] = value
                        break
            best = max(best, len(pivots))
    return best


def inspect(wx, wy, h):
    groups, wz = groups_and_weights(wx, wy)
    blocks, total = [], Fraction(0)
    for group in groups:
        block = archive.recognize(group)
        if block['kind'] == 'convolution':
            score = archive.profile(block['a'], block['b'], h)
        else:
            block = {'kind': 'slice_rank_mod2', 'rank': slice_bound(group)}
            score = Fraction(block['rank'])
        block['terms'] = group
        block['value_exact'] = str(score)
        blocks.append(block)
        total += score
    source = archive.profile(len(wx), len(wy)+1, h)
    return total/source, {
        'source': [len(wx), len(wy)+1], 'x_weights': wx, 'y_weights': wy,
        'y_coordinate_labels': list(range(1, len(wy)+1)),
        'z_weights': wz, 'blocks': blocks,
        'source_exact': str(source), 'target_exact': str(total),
        'ratio_exact': str(total/source), 'profile_violation': total > source,
    }


def cases(max_sum, samples, seed):
    for a in range(2, min(7, max_sum-1)):
        for b in range(2, max_sum-a+1):
            for wx in product(range(2), repeat=a):
                if min(wx):
                    continue
                for wy in product(range(2), repeat=b-1):
                    if min(wy) == 0:
                        yield 'binary', wx, wy
    rng = random.Random(seed)
    for n in range(samples):
        a, b = rng.randint(2, 12), rng.randint(3, 64)
        if n % 2:
            wx = tuple(rng.randint(-8, 8) for _ in range(a))
            wy = tuple(rng.randint(-8, 8) for _ in range(b-1))
            mode = 'random'
        else:
            wx = tuple(-i for i in range(a))
            cuts = [rng.randint(1, b-1) for _ in range(rng.randint(1, 5))]
            wy = tuple(min(abs(2*j-2*c-1) for c in cuts)
                       for j in range(1, b))
            wx = tuple(2*w for w in wx)
            mode = 'distance_to_cuts'
        yield mode, wx, wy


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-sum', type=int, default=11)
    parser.add_argument('--samples', type=int, default=10000)
    parser.add_argument('--seed', type=int, default=20261020)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    h = archive.slopes(100)
    counts, best, best_ratio, witness = {}, None, Fraction(0), None
    for mode, wx, wy in cases(args.max_sum, args.samples, args.seed):
        counts[mode] = counts.get(mode, 0)+1
        ratio, record = inspect(wx, wy, h)
        if ratio > best_ratio:
            best_ratio, best = ratio, record
        if record['profile_violation']:
            witness = record
            break
    report = {
        'new_exponent_established': False, 'seed': args.seed,
        'max_sum': args.max_sum, 'requested_samples': args.samples,
        'completed_counts': counts, 'best': best, 'witness': witness,
        'scope': 'Exact rational scoring after an explicit Chebyshev basis change. '
                 'Unrecognized blocks use a valid F2 slice-rank lower bound. '
                 'Finite profile exclusion would require a separate all-scale implication.',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ('best', 'witness')}, indent=2))
    print('best ratio:', best_ratio, 'profile violation:', witness is not None)


if __name__ == '__main__':
    main()
