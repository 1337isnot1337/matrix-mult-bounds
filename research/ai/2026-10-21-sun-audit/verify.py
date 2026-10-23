"""Exact, bounded audit of selected identities in Sun 2610.13971v1.

This verifies finite identities and excludes one packetwise interpretation.
It does NOT verify or refute the proposed complete global degeneration.
Only Python's standard library is used. All coefficient work is exact.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path


SOURCE_URL = "https://arxiv.org/html/2610.13971v1"
SOURCE_VERSION = "2610.13971v1"
B0 = (9, 4, 8, 6)
B1 = (8, 6, 4, 9)
K = (2, 5, 8, 16)
A0 = ((0, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 0))
A1 = ((0, 1, 1, 0), (1, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0))
XI = frozenset((6, 7, 10, 11))
CW2_PACKETS = frozenset((1, 2, 4, 8, 15, 16, 23, 27, 29, 30))
THETA = {
    "A1": 3, "A2": 0, "A3": 0,
    "B1": 5, "B2": 9, "B3": 0,
    "C1": 6, "C2": 9, "C3": 0,
    "P": 10, "Q": 12, "R": 15,
}
SIDE_COLOURS = ((0, 5, 9, 0, 15), (0, 3, 0, 0, 12), (0, 0, 0, 0, 10))


def linear(columns, x):
    value = 0
    for i, column in enumerate(columns):
        if (x >> i) & 1:
            value ^= column
    return value


def matrix_binary(rows, x):
    return sum(((sum(v * ((x >> j) & 1) for j, v in enumerate(row)) & 1) << i)
               for i, row in enumerate(rows))


def character(a, b):
    return -1 if (a & b).bit_count() & 1 else 1


def support(q):
    """Literal Definition 2.4 supports, with infinity indexed q+1."""
    result = {}
    for i in range(1, q + 1):
        result[f"A{i}"] = (0, i, i)
        result[f"B{i}"] = (i, 0, i)
        result[f"C{i}"] = (i, i, 0)
    result.update(P=(0, 0, q + 1), Q=(0, q + 1, 0), R=(q + 1, 0, 0))
    return result


def retained(layer, chi):
    if layer == 0:
        return frozenset(("C1",)) if chi in XI else frozenset()
    if chi in (6, 10):
        return frozenset(("A1", "B1", "B2", "C1", "P", "Q", "R"))
    if chi in (7, 11):
        return frozenset(("A1", "A2", "B1", "C1", "P", "Q", "R"))
    return frozenset(("A1", "A3", "B1", "B2", "C1", "P", "Q", "R"))


def packets():
    rows = []
    for state, layer in product(range(16), range(2)):
        p = linear(K, state) ^ (3 if layer else 0)
        chi = matrix_binary(A1 if layer else A0, state)
        rows.append({"packet": p, "layer": layer, "state": state,
                     "chi": chi, "q": 2 if p in CW2_PACKETS else 3,
                     "retained": retained(layer, chi)})
    return sorted(rows, key=lambda row: row["packet"])


def scalar_maps(q, mask, repair=False):
    """Section 5 table literally, with an explicit optional local repair."""
    vectors = [[Q(0)] * (q + 2) for _ in range(3)]
    vectors[0][0], vectors[1][0], vectors[2][0] = Q(1, 128), Q(1), Q(1)
    assignments = {
        frozenset(): (0, 0, 0),
        frozenset(("A",)): (0, 1, 1),
        frozenset(("B",)): (1, 0, 1),
        frozenset(("C",)): (1, 1, 0),
        frozenset(("A", "B", "C")): (1, 1, 1),
    }
    for i in range(1, q + 1):
        kinds = frozenset(k for k in "ABC" if f"{k}{i}" in mask)
        for side, value in enumerate(assignments[kinds]):
            vectors[side][i] = Q(value, 128) if repair and side == 0 else Q(value)
    vectors[0][-1] = Q(int("R" in mask), 128)
    vectors[1][-1] = Q(int("Q" in mask))
    vectors[2][-1] = Q(int("P" in mask))
    return vectors


def scalar_audit():
    occurrences = kept = 0
    failures = []
    repair_failures = []
    for row in packets():
        maps = scalar_maps(row["q"], row["retained"])
        repaired = scalar_maps(row["q"], row["retained"], repair=True)
        for name, indices in support(row["q"]).items():
            occurrences += 1
            kept += name in row["retained"]
            expected = Q(int(name in row["retained"]), 128)
            actual = maps[0][indices[0]] * maps[1][indices[1]] * maps[2][indices[2]]
            corrected = repaired[0][indices[0]] * repaired[1][indices[1]] * repaired[2][indices[2]]
            if actual != expected:
                failures.append({"packet": row["packet"], "support": name,
                                 "actual": str(actual), "expected": str(expected)})
            if corrected != expected:
                repair_failures.append((row["packet"], name))
    assert occurrences == 354 and kept == 128
    assert len(failures) == 50 and not repair_failures
    return {"source_support_occurrences": occurrences, "retained_supports": kept,
            "literal_mismatches": failures, "repair_mismatch_count": len(repair_failures),
            "repair": "Divide every X satellite scalar by 128; retain the stated X centre and infinity scalars."}


def walsh_numerator(rho, beta, row=None):
    """The integer numerator of (5.1), optionally for one source packet."""
    rows = packets() if row is None else (row,)
    total = 0
    for packet in rows:
        b = B1 if packet["layer"] else B0
        sign = character(packet["chi"], rho ^ linear(b, beta))
        total += sign * sum(character(THETA[name], beta) for name in packet["retained"])
    return total


def walsh_audit():
    failures = []
    nonzero = []
    for rho, beta in product(range(16), repeat=2):
        expected = 128 * int(linear(B0, beta) == linear(B1, beta)
                             and rho == linear(B0, beta))
        actual = walsh_numerator(rho, beta)
        if actual != expected:
            failures.append([rho, beta, actual, expected])
        if actual:
            nonzero.append([rho, beta, actual])
    assert not failures and nonzero == [[0, 0, 128], [3, 15, 128]]
    colour_failures = []
    for name, (i, j, k) in support(3).items():
        colour = SIDE_COLOURS[0][i] ^ SIDE_COLOURS[1][j] ^ SIDE_COLOURS[2][k]
        if colour != THETA[name]:
            colour_failures.append(name)
    assert not colour_failures
    return {"pointwise_equations": 256, "failures": failures,
            "nonzero_integer_numerators": nonzero, "side_colour_checks": 12,
            "side_colour_failures": colour_failures}


def defect(u, v, w):
    q, epsilon, a = u
    r, delta, b = v
    s, phi, c = w
    return q ^ r ^ s, b ^ a ^ epsilon, phi ^ epsilon ^ delta, c ^ a ^ epsilon ^ delta


def chart_section(d):
    d_h, d1, d2, d3 = d
    beta = d1 | (d2 << 1) | (d3 << 2)
    rho = d_h ^ linear(B0, beta)
    return rho, beta


def chart_audit():
    checked = 0
    failures = []
    for d_h, d1, d2, d3 in product(range(16), range(2), range(2), range(2)):
        d = (d_h, d1, d2, d3)
        rho, beta = chart_section(d)
        image = linear((1, 2, 12), d1 | (d2 << 1) | (d3 << 2))
        actual = [(r, b) for r, b in product(range(16), repeat=2)
                  if (r ^ linear(B0, b)) == d_h
                  and (linear(B0, b) ^ linear(B1, b)) == image]
        expected = sorted(((rho, beta), (rho ^ 3, beta ^ 15)))
        if actual != expected:
            failures.append({"defect": d, "actual": actual, "expected": expected})
        checked += 1
    assert checked == 128 and not failures
    return {"defects_checked": checked, "representatives_per_defect": 2,
            "chosen_section": "beta=d1+2*d2+4*d3; rho=dH XOR B0(beta)",
            "failures": failures}


def central_mm2():
    """All 64 coefficients; central edge (epsilon,a) means E[a,a+epsilon]."""
    values = {}
    for epsilon, a, delta, b, phi, c in product(range(2), repeat=6):
        x, y, z = 2 * a + (a ^ epsilon), 2 * b + (b ^ delta), 2 * c + (c ^ phi)
        values[x, y, z] = int((a ^ epsilon) == b and (b ^ delta) == c and (c ^ phi) == a)
    assert len(values) == 64 and sum(values.values()) == 8
    return values


def rank_with_rows(matrix):
    """Rational elimination, also retaining a maximal independent row minor."""
    work = [[Q(x) for x in row] for row in matrix]
    row_labels = list(range(len(work)))
    pivot = 0
    for col in range(len(work[0])):
        found = next((i for i in range(pivot, len(work)) if work[i][col]), None)
        if found is None:
            continue
        work[pivot], work[found] = work[found], work[pivot]
        row_labels[pivot], row_labels[found] = row_labels[found], row_labels[pivot]
        diagonal = work[pivot][col]
        work[pivot] = [value / diagonal for value in work[pivot]]
        for i in range(pivot + 1, len(work)):
            multiplier = work[i][col]
            if multiplier:
                work[i] = [a - multiplier * b for a, b in zip(work[i], work[pivot])]
        pivot += 1
        if pivot == len(work):
            break
    return pivot, row_labels[:pivot]


def determinant(matrix):
    work = [[Q(x) for x in row] for row in matrix]
    result = Q(1)
    for col in range(len(work)):
        row = next((i for i in range(col, len(work)) if work[i][col]), None)
        if row is None:
            return Q(0)
        if row != col:
            work[row], work[col] = work[col], work[row]
            result = -result
        value = work[col][col]
        result *= value
        for i in range(col + 1, len(work)):
            coefficient = work[i][col] / value
            for j in range(col + 1, len(work)):
                work[i][j] -= coefficient * work[col][j]
    return result


def mm2_koszul():
    tensor = central_mm2()
    wedges = list(combinations(range(4), 2))
    rows = [(pair, z) for pair in wedges for z in range(4)]
    row_index = {value: i for i, value in enumerate(rows)}
    columns = list(product(range(4), repeat=2))  # first wedge vector, B-dual coordinate
    matrix = [[0] * len(columns) for _ in rows]
    for col, (wedge, y) in enumerate(columns):
        for x, z in product(range(4), repeat=2):
            coefficient = tensor[x, y, z]
            if not coefficient or x == wedge:
                continue
            pair = tuple(sorted((wedge, x)))
            sign = 1 if wedge < x else -1
            matrix[row_index[pair, z]][col] += sign * coefficient
    rank, minor_rows = rank_with_rows(matrix)
    minor = [matrix[i] for i in minor_rows]
    minor_det = determinant(minor)
    assert rank == 16 and minor_det
    return {"rows": len(rows), "columns": len(columns), "rank": rank,
            "row_order": [[list(pair), z] for pair, z in rows],
            "column_order": [list(pair) for pair in columns],
            "matrix": matrix, "nonsingular_minor_rows": minor_rows,
            "minor_determinant": str(minor_det),
            "rank_one_koszul_bound": 3, "border_rank_lower_bound": (rank + 2) // 3}


def packet_pullback_audit():
    """Exclude a particular packetwise lift, not the unspecified global lift."""
    generic = [p for p in packets() if p["layer"] == 1 and p["chi"] not in XI]
    assert len(generic) == 12
    expected_tensor = central_mm2()
    failures = []
    checked = 0
    target_coefficients = []
    for packet in generic:
        assert sorted(THETA[name] & 7 for name in packet["retained"]) == list(range(8))
        for epsilon, a, delta, b, phi, c in product(range(2), repeat=6):
            # These three H4 labels are all nonzero and sum to zero. Thus the
            # restriction never touches a deleted zero coordinate of the dense tensor.
            u, v, w = (1, epsilon, a), (2, delta, b), (3, phi, c)
            rho, beta = chart_section(defect(u, v, w))
            actual = walsh_numerator(rho, beta, packet)
            x, y, z = 2 * a + (a ^ epsilon), 2 * b + (b ^ delta), 2 * c + (c ^ phi)
            expected = 8 * expected_tensor[x, y, z]
            if actual != expected:
                failures.append([packet["packet"], x, y, z, actual, expected])
            if packet == generic[0]:
                target_coefficients.append({"x": x, "y": y, "z": z,
                                            "coefficient": str(Q(actual, 128))})
            checked += 1
    assert not failures and checked == 12 * 64
    # The two supports share x0, yet require different X-dependent characters
    # under the naive supportwise pullback through beta_X=(a+epsilon,epsilon,a+epsilon,0).
    beta_x = 5  # a=1, epsilon=0
    incidence_sign = character(THETA["A1"] ^ THETA["A3"], beta_x)
    assert incidence_sign == -1
    return {"interpretation": "Apply the scalar formula packetwise after substituting the fixed chart section (5.2).",
            "scope": "This interpretation is impossible. No conclusion about all possible outer-row global maps is asserted.",
            "generic_packets": [p["packet"] for p in generic],
            "all_central_coefficient_checks": checked, "failures": failures,
            "nonzero_H4_labels": [1, 2, 3], "result": "M2/16",
            "all_64_coefficients": sorted(target_coefficients, key=lambda v: (v["x"], v["y"], v["z"])),
            "shared_x0_twist_conflict": {"supports": ["A1", "A3"],
                                         "beta_x": beta_x, "relative_sign": incidence_sign},
            "koszul": mm2_koszul()}


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, column)) for column in zip(*b)] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def empty_module_audit():
    b = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [2, 0, 0, 0, 0, -1, 1, 0, 0, 0],
         [2, 0, 0, 0, 0, -1, 0, 1, 0, 0],
         [2, 0, 0, 0, 0, -1, 0, 0, 1, 0],
         [2, 0, 0, 0, 0, -1, 0, 0, 0, 1]]
    d = [[0, 0, 0, 0, 0, 0, 1, 0, 0, -1],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, -1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, -1],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [Q(-1, 2), -1, -1, -1, 0, Q(1, 4), 0, 0, 0, Q(-1, 4)]]
    c = [[1, 0, 0, 0, 0, Q(1, 2), 0, 0, 0, Q(-1, 2)]]
    j = [[Q((i + 5) % 10 == k) for k in range(10)] for i in range(10)]
    assert multiply(multiply(c, j), transpose(c)) == [[1]]
    assert multiply(multiply(b, j), transpose(d)) == identity(7)
    assert multiply(multiply(b, j), transpose(c)) == [[0] for _ in range(7)]
    assert multiply(multiply(d, j), transpose(c)) == [[0] for _ in range(7)]
    assert all(sum(row[5:]) == 0 for row in b + d + c)
    xi = [0, 3, 4, 9, 12] * 2
    actions = []
    for delta in range(16):
        bsigma = [[value * character(xi[k], delta) for k, value in enumerate(row)] for row in b]
        actions.append(multiply(multiply(bsigma, j), transpose(d)))
    failures = []
    for delta, epsilon in product(range(16), repeat=2):
        if multiply(actions[delta], actions[epsilon]) != actions[delta ^ epsilon]:
            failures.append([delta, epsilon])
    assert not failures
    return {"base_pairings_checked": ["cJcT=1", "BJDT=I7", "BJcT=0", "DJcT=0"],
            "last_five_zero_sums": 15, "character_action_products": 256,
            "character_action_failures": failures}


def run():
    return {"source": SOURCE_URL, "version": SOURCE_VERSION,
            "status": "finite audit; packetwise interpretation excluded; global certificate unresolved",
            "claimed_source": {"outer_diagonal_size": 16, "one_row_types": {"CW3": 14, "CW2": 6, "W": 7, "D4": 5},
                               "one_row_dimension": 128, "one_row_border_rank_budget": 128,
                               "source_dimensions": [2048, 2048, 2048],
                               "target": "M32", "target_dimensions": [1024, 1024, 1024]},
            "literal_scalar_normalization": scalar_audit(),
            "walsh_compiler": walsh_audit(),
            "chart_representatives": chart_audit(),
            "packetwise_chart_pullback": packet_pullback_audit(),
            "five_empty_module": empty_module_audit()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
        print(json.dumps({"output": str(args.output), "status": report["status"],
                          "scalar_mismatches": len(report["literal_scalar_normalization"]["literal_mismatches"]),
                          "walsh_checks": 256, "packet_coefficient_checks": 768,
                          "M2_K1_rank": report["packetwise_chart_pullback"]["koszul"]["rank"]}, sort_keys=True))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
