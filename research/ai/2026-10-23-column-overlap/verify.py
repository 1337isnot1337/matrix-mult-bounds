"""Exact native-source controls for the full-channel overlap theorem.

Only the Python standard library is used. Complete tensor coefficients,
including all implicit zeros, are compared. Formal maps are finite Laurent
polynomials over Q; no floating-point decision is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def rank(rows):
    """Rank of sparse rational rows without modifying the input."""
    pivots = {}
    for raw in rows:
        row = {k: F(v) for k, v in raw.items() if v}
        while row:
            p = min(row)
            if p not in pivots:
                scale = row[p]
                pivots[p] = {k: v / scale for k, v in row.items()}
                break
            scale = row[p]
            for k, v in pivots[p].items():
                value = row.get(k, F(0)) - scale * v
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
    return len(pivots)


def dense_rank(matrix):
    return rank([{j: value for j, value in enumerate(row) if value}
                 for row in matrix])


def inverse(matrix):
    n = len(matrix)
    rows = [[F(v) for v in row] + [F(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        p = next(i for i in range(j, n) if rows[i][j])
        rows[p], rows[j] = rows[j], rows[p]
        scale = rows[j][j]
        rows[j] = [value / scale for value in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                scale = rows[i][j]
                rows[i] = [a - scale * b for a, b in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def identity(m):
    return [[F(i == j) for j in range(m)] for i in range(m)]


def poly(value=0, degree=0):
    return {degree: F(value)} if value else {}


def add(left, right, scale=1):
    out = dict(left)
    for degree, value in right.items():
        new = out.get(degree, F(0)) + scale * value
        if new:
            out[degree] = new
        else:
            out.pop(degree, None)
    return out


def mul(left, right):
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            out = add(out, {a + b: x * y})
    return out


def evaluate(value, t):
    return sum((coefficient * F(t) ** degree
                for degree, coefficient in value.items()), F(0))


def constant_blocks(matrices):
    return [[[poly(value) for value in row] for row in matrix]
            for matrix in matrices]


def constant_first(values):
    return {pq: {a: poly(value) for a, value in images.items() if value}
            for pq, images in values.items()}


def target(l, m, r):
    return {(i * r + j, j * m + a, a * l + i): poly(1)
            for i, j, a in itertools.product(range(l), range(r), range(m))}


def native(n, m, sb, sc, beta, gamma, first):
    """Expand the literal n^2*m^2 source terms and all local-map entries."""
    b_index, c_index = {s: j for j, s in enumerate(sb)}, {s: i for i, s in enumerate(sc)}
    l = len(sc)
    out = {}
    expanded = 0
    for p, q, y, v in itertools.product(range(n), range(n), range(m), range(m)):
        j, i = b_index.get(q + v), c_index.get(p + y)
        if j is None or i is None:
            continue
        for a, av in first.get((p, q), {}).items():
            for alpha, bv in enumerate(beta[j][y]):
                if not bv:
                    continue
                for delta, cv in enumerate(gamma[i][v]):
                    if not cv:
                        continue
                    term = mul(mul(av, bv), cv)
                    key = (a, j * m + alpha, delta * l + i)
                    out[key] = add(out.get(key, {}), term)
                    expanded += 1
    return {key: value for key, value in out.items() if value}, expanded


def window_slices(n, m, sb, sc, beta, gamma, at=0):
    """Reconstruct source slices from coefficient windows, independently of native()."""
    l = len(sc)
    bs = [[[evaluate(value, at) for value in row] for row in block] for block in beta]
    cs = [[[evaluate(value, at) for value in row] for row in block] for block in gamma]
    rows = [{} for _ in range(n * n)]
    for i, z in enumerate(sc):
        for j, s in enumerate(sb):
            for y in range(m):
                for v in range(m):
                    p, q = z - y, s - v
                    if not (0 <= p < n and 0 <= q < n):
                        continue
                    row = rows[p * n + q]
                    for alpha in range(m):
                        for delta in range(m):
                            value = bs[j][y][alpha] * cs[i][v][delta]
                            if value:
                                key = (j * m + alpha, delta * l + i)
                                row[key] = row.get(key, F(0)) + value
    return [{key: value for key, value in row.items() if value} for row in rows]


def target_rows(l, m, r):
    return [{(j * m + a, a * l + i): F(1) for a in range(m)}
            for i in range(l) for j in range(r)]


def covered(n, m, positions):
    return sorted({q for s in positions for q in range(max(0, s - m + 1), min(n, s + 1))})


def components(n, m, positions):
    values = sorted(s for s in positions if m - 1 <= s <= n - 1)
    groups = []
    for value in values:
        if not groups or value - groups[-1][-1] >= m:
            groups.append([])
        groups[-1].append(value)
    return groups


def geometry(n, m, sb, sc, beta, gamma):
    good = []
    for positions, blocks in ((sb, beta), (sc, gamma)):
        good.append([s for s, block in zip(positions, blocks)
                     if dense_rank([[evaluate(value, 0) for value in row]
                                    for row in block]) == m])
    ub, uc = covered(n, m, sb), covered(n, m, sc)
    gb, gc = covered(n, m, good[0]), covered(n, m, good[1])
    cb, cc = components(n, m, good[0]), components(n, m, good[1])
    d, nn, gg, c = len(sb) * len(sc), len(ub) * len(uc), len(gb) * len(gc), len(cb) * len(cc)
    return {"all_covered": [ub, uc], "good_covered": [gb, gc],
            "good_source_columns": good, "components": [cb, cc],
            "D": d, "N": nn, "G": gg, "c": c,
            "auxiliary_flattening_lower_bound": max(0, d - nn + gg - c)}


def subtract_tensor(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = add(out.get(key, {}), value, -1)
    return {key: value for key, value in out.items() if value}


def tensor_rows(tensor, count, at):
    rows = [{} for _ in range(count)]
    for (a, b, c), value in tensor.items():
        coefficient = evaluate(value, at)
        if coefficient:
            rows[a][(b, c)] = coefficient
    return rows


def serial_tensor(tensor):
    return [[*key, [[degree, str(value)] for degree, value in sorted(poly_value.items())]]
            for key, poly_value in sorted(tensor.items())]


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def inspect_case(name, n, m, sb, sc, beta, gamma, first, expected_exact=False,
                 expected_residual_rank=None, require_poles=False):
    if n < 1 or m < 2 or len(set(sb)) != len(sb) or len(set(sc)) != len(sc):
        raise ValueError("Positive source sizes and injective routing are required")
    if any(s < 0 or s >= n + m - 1 for s in sb + sc):
        raise ValueError("Source routing column is outside the polynomial range")
    l, r, d = len(sc), len(sb), len(sc) * len(sb)
    source_tensor, expanded = native(n, m, sb, sc, beta, gamma, first)
    wanted = target(l, m, r)
    residual = subtract_tensor(wanted, source_tensor)
    if expected_exact and residual:
        raise AssertionError((name, "constructed target identity failed"))
    # Literal coefficientwise cancellation, including every negative order.
    if residual and subtract_tensor(wanted, subtract_tensor(source_tensor, residual)) == {}:
        raise AssertionError("The deliberately wrong residual sign passed")
    total = subtract_tensor(source_tensor, {key: {e: -v for e, v in value.items()}
                                           for key, value in residual.items()})
    if total != wanted:
        raise AssertionError((name, "complete cancellation identity failed"))
    negative = sum(1 for value in source_tensor.values() for e in value if e < 0)
    if require_poles and not negative:
        raise AssertionError((name, "missing negative source coefficients"))
    data = geometry(n, m, sb, sc, beta, gamma)
    h0 = window_slices(n, m, sb, sc, beta, gamma)
    h2 = window_slices(n, m, sb, sc, beta, gamma, 2)
    r0, r2 = rank(h0), rank(h2)
    intersection = r0 + d - rank(h0 + target_rows(l, m, r))
    if not (r0 >= data["G"] and r2 <= data["N"] and intersection <= data["c"]):
        raise AssertionError((name, "dimension estimate failed", data, r0, r2, intersection))
    native_first = constant_first({(p, q): {p * n + q: 1} for p in range(n) for q in range(n)})
    full, _ = native(n, m, sb, sc, beta, gamma, native_first)
    for at, reconstructed in ((0, h0), (2, h2)):
        if tensor_rows(full, n * n, at) != reconstructed:
            raise AssertionError((name, "native/window reconstruction disagrees", at))
    rr = rank(tensor_rows(residual, d, 2))
    # Evaluation supplies a certified minor over Q(t). If this is D, the
    # rank is exactly D. Constant controls have their exact ordinary rank.
    if rr < data["auxiliary_flattening_lower_bound"]:
        raise AssertionError((name, "observed exact control violates the bound"))
    if expected_residual_rank is not None and rr != expected_residual_rank:
        raise AssertionError((name, rr, expected_residual_rank))
    channel = [[F(0) for _ in range(m)] for _ in range(m)]
    for (a, b, c_index), value in source_tensor.items():
        if a == 0:
            j, alpha = divmod(b, m)
            delta, i = divmod(c_index, l)
            channel[alpha][delta] += evaluate(value, 2) * F(2) ** j * F(3) ** i
    channel_rank = dense_rank(channel)
    return {"name": name, "n": n, "m": m, "target_shape": [l, m, r],
            "routing_B": sb, "routing_C": sc, "geometry": data,
            "leading_source_rank": r0, "source_rank_at_t2": r2,
            "leading_target_intersection_dimension": intersection,
            "residual_rank_at_t2": rr,
            "residual_rank_is_exact_over_Qt": rr == d or not require_poles,
            "source_terms": n * n * m * m,
            "expanded_native_terms": expanded,
            "target_coefficient_positions": m * m * d * d,
            "source_slice_coefficient_positions_per_evaluation": n * n * m * m * d,
            "source_negative_coefficients": negative,
            "source_A0_channel_rank_at_t2_X2_Y3": channel_rank,
            "complete_source_sha256": digest(serial_tensor(source_tensor)),
            "complete_residual_sha256": digest(serial_tensor(residual)),
            "exact_target": not residual}


def separated_case(n, m):
    k = n // m
    positions = [m * (i + 1) - 1 for i in range(k)]
    first = {(m * i + m - 1 - y, m * j + m - 1 - y): {i * k + j: 1}
             for i, j, y in itertools.product(range(k), range(k), range(m))}
    blocks = constant_blocks([identity(m) for _ in positions])
    return inspect_case(f"separated-n{n}-m{m}", n, m, positions, positions,
                        blocks, blocks, constant_first(first), expected_exact=True,
                        expected_residual_rank=0)


def vandermonde_case(n=5, m=3):
    positions = list(range(m - 1, n))
    lam = list(range(1, m + 1))
    vi = inverse([[F(a) ** (-y) for a in lam] for y in range(m)])
    beta, gamma = [], []
    for s in positions:
        beta.append([[vi[a][y] * F(lam[a]) ** (-s) for a in range(m)]
                     for y in range(m)])
        gamma.append([[vi[a][v] * F(lam[a]) ** (-s) for a in range(m)]
                      for v in range(m)])
    first = {(p, q): {0: sum(F(a) ** (p + q) for a in lam)}
             for p in range(n) for q in range(n)}
    result = inspect_case("connected-full-channel-sharp", n, m, positions, positions,
                          constant_blocks(beta), constant_blocks(gamma),
                          constant_first(first), expected_residual_rank=len(positions) ** 2 - 1)
    if result["leading_target_intersection_dimension"] != 1:
        raise AssertionError("Sharp example has the wrong intersection dimension")
    if result["source_A0_channel_rank_at_t2_X2_Y3"] != m:
        raise AssertionError("The full-channel control lost channel rank")
    return result


def moving_separated_case():
    n, m, k = 6, 2, 3
    positions = [1, 3, 5]
    beta = constant_blocks([identity(m) for _ in positions])
    gamma = constant_blocks([identity(m) for _ in positions])
    beta[1] = [[poly(i == j, 1) for j in range(m)] for i in range(m)]
    first = {(m * i + m - 1 - y, m * j + m - 1 - y):
             {i * k + j: poly(1, -int(j == 1))}
             for i, j, y in itertools.product(range(k), range(k), range(m))}
    result = inspect_case("exact-moving-target-requires-saturation-budget", n, m,
                          positions, positions, beta, gamma, first,
                          expected_exact=True, expected_residual_rank=0)
    if result["geometry"]["D"] - result["geometry"]["c"] <= 0:
        raise AssertionError("The omitted-saturation counterexample is ineffective")
    return result


def varying_case():
    n, m = 5, 2
    positions = [1, 2, 3, 4]
    blocks_b = constant_blocks([identity(m) for _ in positions])
    blocks_c = constant_blocks([identity(m) for _ in positions])
    blocks_b[1][1][1] = poly(1, 1)
    first = {(p, q): {0: poly(1 + p + 2 * q, -1)}
             for p in range(n) for q in range(n)}
    return inspect_case("singular-leading-block-with-pole-cancellation", n, m,
                        positions, positions, blocks_b, blocks_c, first,
                        require_poles=True, expected_residual_rank=16)


def boundary_case():
    n, m = 3, 3
    positions_b, positions_c = [0, 1, 3, 4], [0, 2, 4]
    first = {(p, q): {(p + 2 * q) % 12: 1 + p + q} for p in range(n) for q in range(n)}
    return inspect_case("zero-extension-boundary-columns", n, m, positions_b, positions_c,
                        constant_blocks([identity(m) for _ in positions_b]),
                        constant_blocks([identity(m) for _ in positions_c]),
                        constant_first(first), expected_residual_rank=12)


def leading_loss_case():
    n, m = 4, 2
    positions = [1, 2, 3]
    beta = constant_blocks([identity(m) for _ in positions])
    gamma = constant_blocks([identity(m) for _ in positions])
    for j in (0, 1):
        beta[j][0][0] = poly(1, 1)
        beta[j][1][1] = poly(1, 1)
    first = {(p, q): {0: poly(1 + p + q, -1)}
             for p in range(n) for q in range(n)}
    result = inspect_case("actual-leading-slice-rank-loss", n, m, positions, positions,
                          beta, gamma, first, require_poles=True, expected_residual_rank=9)
    if result["source_rank_at_t2"] <= result["leading_source_rank"]:
        raise AssertionError("Rank-loss control did not lose rank")
    return result


def run():
    cases = [separated_case(6, 2), separated_case(8, 4), vandermonde_case(),
             varying_case(), boundary_case(), leading_loss_case(), moving_separated_case()]
    return {"schema": "paired-column-overlap-controls-v1", "arithmetic": "exact rational Laurent polynomials",
            "proof_status": "written-unreviewed", "cases": cases,
            "case_count": len(cases),
            "complete_target_positions": sum(c["target_coefficient_positions"] for c in cases),
            "complete_source_slice_positions": 2 * sum(c["source_slice_coefficient_positions_per_evaluation"] for c in cases),
            "scope": "Finite controls support proof.md; they do not establish the uniform theorem by extrapolation.",
            "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
