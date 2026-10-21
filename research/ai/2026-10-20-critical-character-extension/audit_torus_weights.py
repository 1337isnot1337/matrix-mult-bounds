#!/usr/bin/env python3
"""Independent integer-coefficient audit of the anisotropic torus search.

Unlike the discovery enumerator, this uses no polynomial factorization and
no SymPy. It reconstructs nonnegative factors coefficient by coefficient.
"""

from collections import Counter, defaultdict
from itertools import combinations_with_replacement, product
import json
from pathlib import Path
import time


SOURCE = tuple(sum(1 for i, j, k in product(range(4), range(5), range(8))
                   if i + j + k == degree) for degree in range(15))


def nonnegative_factors(polynomial, first_sum=12, second_sum=13):
    """Yield all F,H>=0 with F H=P, F(1)=first_sum, H(1)=second_sum.

    F is normalized to have a positive constant coefficient. Powers of x
    dividing P therefore all belong to H. Degrees and constant terms are
    exhaustively enumerated; the next coefficient of H is forced once the
    next coefficient of F has been chosen.
    """
    valuation = next(i for i, c in enumerate(polynomial) if c)
    last = max(i for i, c in enumerate(polynomial) if c)
    q = polynomial[valuation:last + 1]
    degree = len(q) - 1

    for df in range(degree + 1):
        dh = degree - df
        for f0 in range(1, min(first_sum, q[0]) + 1):
            if q[0] % f0:
                continue
            h0 = q[0] // f0
            if h0 > second_sum:
                continue
            f, h = [f0] + [0] * df, [h0] + [0] * dh
            if df == 0 and f0 != first_sum:
                continue
            if dh == 0 and h0 != second_sum:
                continue

            def extend(k, sf, sh):
                if k > max(df, dh):
                    if sf != first_sum or sh != second_sum:
                        return
                    for t in range(k, degree + 1):
                        if sum(f[i] * h[t-i] for i in range(max(0, t-dh), min(df, t)+1)) != q[t]:
                            return
                    yield tuple(f), (0,) * valuation + tuple(h)
                    return

                known = sum(f[i] * h[k-i]
                            for i in range(max(1, k-dh), min(df, k-1)+1))
                rhs = q[k] - known
                if rhs < 0:
                    return
                if k > df:
                    candidates = (0,)
                elif k > dh:
                    if rhs % h0:
                        return
                    candidates = (rhs // h0,)
                else:
                    candidates = range(min(first_sum-sf, rhs//h0)+1)
                for fk in candidates:
                    if fk < 0 or (k == df and fk == 0):
                        continue
                    rem = rhs - h0 * fk
                    if rem < 0 or rem % f0:
                        continue
                    hk = rem // f0
                    if k > dh and hk:
                        continue
                    if k == dh and hk == 0:
                        continue
                    nf, nh = sf + fk, sh + hk
                    if nf > first_sum or nh > second_sum:
                        continue
                    if nf == first_sum and k < df:
                        continue
                    if nh == second_sum and k < dh:
                        continue
                    if k >= df and nf != first_sum:
                        continue
                    if k >= dh and nh != second_sum:
                        continue
                    if k <= df:
                        f[k] = fk
                    if k <= dh:
                        h[k] = hk
                    yield from extend(k+1, nf, nh)

            if max(df, dh) == 0:
                if f0 == first_sum and h0 == second_sum:
                    yield tuple(f), (0,) * valuation + tuple(h)
            else:
                yield from extend(1, f0, h0)


def normalized_vertices(f, h):
    radius = 7
    min_second = radius - (len(h)-1)
    first = tuple((i-min_second, c) for i, c in enumerate(f) if c)
    second = tuple(sorted((radius-i-min_second, c) for i, c in enumerate(h) if c))
    return first, second


def compatible(first, second):
    differences = Counter()
    for i, a in first:
        for j, b in second:
            differences[i-j] += a*b
    return all(-7 <= d <= 7 and value <= SOURCE[d+7]
               for d, value in differences.items())


def audit():
    by_second = defaultdict(set)
    valid = 0
    start = time.monotonic()
    for positions in combinations_with_replacement(range(15), 4):
        deficit = Counter(positions)
        p = tuple(c-deficit.get(i, 0) for i, c in enumerate(SOURCE))
        if min(p) < 0:
            continue
        valid += 1
        for f, h in nonnegative_factors(p):
            # Direct multiplication is a separate acceptance check.
            reconstructed = [0] * (len(f)+len(h)-1)
            for i, a in enumerate(f):
                for j, b in enumerate(h):
                    reconstructed[i+j] += a*b
            assert reconstructed + [0] * (len(p)-len(reconstructed)) == list(p)
            first, second = normalized_vertices(f, h)
            assert compatible(first, second)
            by_second[second].add(first)
        if valid % 250 == 0:
            print(f"audited {valid} deficit polynomials in {time.monotonic()-start:.2f}s", flush=True)

    triples = []
    for third, neighbors in sorted(by_second.items()):
        neighbors = sorted(neighbors)
        for i, first in enumerate(neighbors):
            for second in neighbors[i:]:
                if compatible(first, second):
                    triples.append((first, second, third))
    return {
        "method": "exhaustive nonnegative convolution factors; Python integers; no factorization library",
        "source": SOURCE,
        "valid_deficit_polynomials": valid,
        "compatible_pairs": sum(map(len, by_second.values())),
        "distinct_second_profiles": len(by_second),
        "triples": triples,
    }


if __name__ == "__main__":
    result = audit()
    out = Path(__file__).with_name("torus_weight_audit.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "triples"}, indent=2))
    print(f"complete triples: {len(result['triples'])}")
