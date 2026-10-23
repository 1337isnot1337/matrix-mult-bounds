#!/usr/bin/env python3
"""Exact controls for the ordinary diagonal first-support theorem.

Finite controls do not certify the universal projective dimension inputs.
This module uses only the standard library and never imports prior code.
"""

from argparse import ArgumentParser
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import isqrt
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def nonnegative_integer(value):
    if type(value) is not int or value < 0:
        raise ValueError("Expected a nonnegative integer")
    return value


def triangular(d):
    nonnegative_integer(d)
    return d*(d+1)//2


def tau(e):
    nonnegative_integer(e)
    return (isqrt(8*e+1)-1)//2


def paired_deficiency(e):
    nonnegative_integer(e)
    return (isqrt(4*e+1)-1)//2


def budget_allowance(e):
    return max(tau(e)-6, paired_deficiency(e))


def optimized_split(a, b):
    nonnegative_integer(a)
    nonnegative_integer(b)
    h = max(a-6, b-6, (a+b)//2)
    j = max(1, a+6-h)
    if not 1 <= j <= min(12, h+7-b):
        raise ArithmeticError("The integer threshold interval is empty")
    if max(a+6-j, b-7+j) != h:
        raise ArithmeticError("The selected threshold does not attain the minimum")
    return {"F_threshold": j, "G_threshold": 13-j, "allowance": h}


def general_lower_bound(a0):
    nonnegative_integer(a0)
    low, high = 0, a0
    while low < high:
        middle = (low+high)//2
        if middle+budget_allowance(middle) >= a0:
            high = middle
        else:
            low = middle+1
    return low


def repair_bounds(n, c):
    nonnegative_integer(n)
    nonnegative_integer(c)
    if n <= c:
        raise ValueError("The outer target dimension must be positive")
    a0 = max(0, n-5*c-7)
    lower = general_lower_bound(a0)
    return {"n": n, "c": c, "r": n-c, "long_kernel_dimension": 4*(c+3),
            "injective_factor_lower_bound": a0, "general_lower_bound": lower,
            "general_bound_allowance": budget_allowance(lower)}


def rank(rows, prime=None):
    """Sparse exact row elimination over Q or a specified prime field."""
    pivots = {}
    for entries in rows:
        row = {i: (x % prime if prime else Fraction(x)) for i, x in enumerate(entries)
               if (x % prime if prime else x)}
        while row:
            first = min(row)
            if first not in pivots:
                inverse = pow(row[first], -1, prime) if prime else 1/row[first]
                pivots[first] = {i: x*inverse % prime if prime else x*inverse
                                 for i, x in row.items()}
                break
            scale = row[first]
            for i, x in pivots[first].items():
                value = row.get(i, 0)-scale*x
                if prime:
                    value %= prime
                if value:
                    row[i] = value
                else:
                    row.pop(i, None)
    return len(pivots)


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def outer(u, v):
    return [a*b for a in u for b in v]


def shift_transpose_map(r, alternating=False):
    if type(r) is not int or r < 2:
        raise ValueError("The control requires r>=2")
    n = r+1
    rows = []
    for i, j in product(range(r), repeat=2):
        row = [0]*(n*n)
        row[n*i+j] += 1
        row[n*(j+1)+i+1] += 1
        if alternating and (i, j) in ((0, 1), (1, 0)):
            sign = 1 if (i, j) == (0, 1) else -1
            for p in range(n):
                row[n*p+p] += sign
        rows.append(row)
    return rows


def apply_first(rows, weights, n):
    values = [sum(a*row[j] for a, row in zip(weights, rows)) for j in range(n*n)]
    return [values[n*i:n*(i+1)] for i in range(n)]


def check_diagonal_identity(rows, r, prime=None):
    """Compare all u_i*u_j coefficients against (1+xy) f_u(x) f_u(y)."""
    n = r+1
    if len(rows) != r*r or any(len(row) != n*n for row in rows):
        raise ValueError("Wrong first-map format")
    actual, expected = {}, {}
    for i, j in product(range(r), repeat=2):
        parameters = (min(i, j), max(i, j))
        for p, q in product(range(n), repeat=2):
            key = (*parameters, p, q)
            actual[key] = actual.get(key, 0)+rows[r*i+j][n*p+q]
        for shift in (0, 1):
            key = (*parameters, i+shift, j+shift)
            expected[key] = expected.get(key, 0)+1
    def cleaned(values):
        return {key: (value % prime if prime else value)
                for key, value in values.items() if (value % prime if prime else value)}
    if cleaned(actual) != cleaned(expected):
        raise ValueError("The complete diagonal polynomial identity fails")
    return len(cleaned(expected))


def shift_controls():
    result = []
    for r in range(2, 8):
        n = r+1
        rows = shift_transpose_map(r)
        altered = shift_transpose_map(r, alternating=True)
        order = sorted(product(range(r), repeat=2), key=lambda pair: (sum(pair), pair))
        minor = [[rows[r*i+j][n*p+q] for p, q in order] for i, j in order]
        if any(minor[i][i] != 1 for i in range(r*r)):
            raise ArithmeticError("The first-map minor does not have unit diagonal")
        if any(minor[i][j] for i in range(r*r) for j in range(i)):
            raise ArithmeticError("The first-map minor is not triangular")
        fields = []
        for prime in (None, 2, 3):
            count = check_diagonal_identity(rows, r, prime)
            check_diagonal_identity(altered, r, prime)
            u = [1]*r
            ruling = [apply_first(rows, outer(u, [int(j == i) for j in range(r)]), n)
                      for i in range(r)]
            right = rank([row for matrix in ruling for row in matrix], prime)
            left = rank([row for matrix in ruling for row in transpose(matrix)], prime)
            if (right, left) != (n, n) or any(rank(matrix, prime) > 2 for matrix in ruling):
                raise ArithmeticError("The ruling-space control failed")
            off_diagonal = [altered[1][n*i:n*(i+1)] for i in range(n)]
            if rank(off_diagonal, prime) != n:
                raise ArithmeticError("The allowed off-diagonal perturbation lost rank")
            fields.append({"field": "Q" if prime is None else f"F{prime}",
                           "diagonal_monomials": count,
                           "common_right_kernel_dimension": n-right,
                           "common_left_kernel_dimension": n-left,
                           "perturbed_off_diagonal_rank": n})
        result.append({"r": r, "n": n, "first_map_rank": r*r,
                       "unit_minor_determinant": 1,
                       "coordinate_order": [list(pair) for pair in order],
                       "fields": fields})
    return result


def square_span(basis):
    result = [outer(u, u) for u in basis]
    for i in range(len(basis)):
        for j in range(i+1, len(basis)):
            result.append([a+b for a, b in zip(outer(basis[i], basis[j]),
                                               outer(basis[j], basis[i]))])
    return result


def kernel_space_controls():
    # These noncoordinate kernels are disjoint over every field.
    f = [[1, 0, 1, 0, 0], [0, 1, 0, 1, 0]]
    g = [[0, 0, 1, 0, 1]]
    joint = square_span(f)+square_span(g)
    records = []
    for prime in (None, 2, 3):
        if rank(f+g, prime) != 3 or rank(joint, prime) != 4:
            raise ArithmeticError("The joint triangular kernel budget failed")
        cross_cases = []
        for r in range(2, 9):
            u = [int(i in (0, r-1)) for i in range(r)]
            cross = [outer(u, u)]
            for i in range(1, r):
                v = [int(j == i) for j in range(r)]
                cross.append([a+b for a, b in zip(outer(u, v), outer(v, u))])
            if rank(cross, prime) != r:
                raise ArithmeticError("The common-kernel cross space lost a dimension")
            cross_cases.append({"r": r, "cross_space_dimension": r})
        records.append({"field": "Q" if prime is None else f"F{prime}",
                        "kernel_dimensions": [2, 1], "joint_square_dimension": 4,
                        "cross_spaces": cross_cases})
    return {"F_kernel_basis": f, "G_kernel_basis": g, "fields": records}


def native_source_control():
    n, r, short = 5, 4, 4
    u = [1, 0, 1, -1]
    coefficient = apply_first(shift_transpose_map(r), outer(u, u), n)
    long = n+short-1
    size = short*long
    native = [[0]*size for _ in range(size)]
    for p, q, y, v in product(range(n), range(n), range(short), range(short)):
        native[long*y+q+v][short*(p+y)+v] += coefficient[p][q]
    formula = [[coefficient[w-y][z-v] if 0 <= w-y < n and 0 <= z-v < n else 0
                for w, v in product(range(long), range(short))]
               for y, z in product(range(short), range(long))]
    if native != formula:
        raise ArithmeticError("The complete native source slice disagrees with offsets")
    b_space, c_space = [], []
    for sector, shift in product(range(short), range(5)):
        b, c = [0]*size, [0]*size
        for power, value in enumerate(u):
            b[long*sector+power+shift] = value
            c[short*(power+shift)+sector] = value
        b_space.append(b)
        c_space.append(c)
    target = [[u[i]*u[j] if a == b else 0
               for b, j in product(range(4), range(r))]
              for i, a in product(range(r), range(4))]
    fields = []
    for prime in (None, 2, 3):
        ranks = [rank(coefficient, prime), rank(native, prime), rank(target, prime)]
        bd, cd = rank(b_space, prime), rank(c_space, prime)
        if ranks[1] < ranks[0]+15 or ranks[2] != 4:
            raise ArithmeticError("The raw and target slice rank control failed")
        if rank(b_space+transpose(native), prime) != bd or rank(c_space+native, prime) != cd:
            raise ArithmeticError("A native slice leaves its stated divisor containing space")
        fields.append({"field": "Q" if prime is None else f"F{prime}",
                       "coefficient_rank": ranks[0], "native_source_rank": ranks[1],
                       "target_rank": ranks[2], "containing_space_dimensions": [bd, cd]})
    return {"n": n, "r": r, "u": u, "fields": fields,
            "actual_target_long_maps_supplied": False}


def integer_controls(limit=500):
    checked_pairs = 0
    cases = []
    for e in range(limit+1):
        t, q = tau(e), paired_deficiency(e)
        if not triangular(t) <= e < triangular(t+1) or not q*(q+1) <= e < (q+1)*(q+2):
            raise ArithmeticError("An integer square-root boundary failed")
        maximum = -1
        for a, b in product(range(t+1), repeat=2):
            if triangular(a)+triangular(b) > e:
                continue
            direct = min(max(a+6-j, b-7+j) for j in range(1, 13))
            selected = optimized_split(a, b)
            if direct != selected["allowance"]:
                raise ArithmeticError("Threshold enumeration disagrees with the minimax identity")
            maximum = max(maximum, direct)
            checked_pairs += 1
        if maximum != budget_allowance(e):
            raise ArithmeticError("The joint scalar budget maximum failed")
        if e in (0, 1, 2, 3, 6, 12, 20, 21, 41, 42, 175, 176, 188, 199, 500):
            cases.append({"e": e, "tau": t, "q": q, "budget_maximum": maximum,
                          "e_plus_allowance": e+maximum})
    bounds = [repair_bounds(n, c) for n, c in
              ((6, 1), (12, 1), (13, 1), (23, 1), (34, 1), (200, 1), (200, 0), (200, 4))]
    for case in bounds:
        lower = case["general_lower_bound"]
        a0 = case["injective_factor_lower_bound"]
        if lower+budget_allowance(lower) < a0:
            raise ArithmeticError("The rounded bound does not meet the inequality")
        if lower and lower-1+budget_allowance(lower-1) >= a0:
            raise ArithmeticError("The rounded bound is not minimal")
    return {"budget_range": [0, limit], "deficiency_pairs_checked": checked_pairs,
            "thresholds_per_pair": 12, "selected_budgets": cases, "target_bounds": bounds}


def verify_local_sources(manifest=None):
    if manifest is None:
        manifest = json.loads((HERE/"sources.json").read_text())
    records = []
    for item in manifest["local_sources"]:
        path = (ROOT/item["path"]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise ValueError("Missing or invalid pinned source path")
        digest = sha256(path.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            raise ValueError(f"Pinned source hash mismatch: {item['path']}")
        records.append({"path": item["path"], "sha256": digest})
    return records


def certificate():
    sources = verify_local_sources()
    return {"schema": 1,
            "scope": "Finite exact controls for the written ordinary diagonal first-map proof. They do not formalize its projective geometry or construct target long maps.",
            "ordinary_maps_only": True,
            "diagonal_identity_is_polynomial": True,
            "independent_mathematical_review": False,
            "improves_omega": False,
            "local_source_pins": sources,
            "shift_transpose": shift_controls(),
            "kernel_spaces": kernel_space_controls(),
            "native_source": native_source_control(),
            "integer_consequences": integer_controls()}


def validate_certificate(record):
    if record != certificate():
        raise ValueError("Certificate differs from complete exact reconstruction")
    return True


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the finite certificate")
    parser.add_argument("--check", action="store_true", help="Check the saved finite certificate")
    args = parser.parse_args()
    path = HERE/"certificate.json"
    result = certificate()
    if args.write:
        path.write_text(json.dumps(result, indent=2)+"\n")
    if args.check and json.loads(path.read_text()) != result:
        raise ValueError("Certificate differs from complete exact reconstruction")
    print(json.dumps({"sources": len(result["local_source_pins"]),
                      "shift_cases": len(result["shift_transpose"]),
                      "budget_range": result["integer_consequences"]["budget_range"],
                      "n200_c1": repair_bounds(200, 1), "result": "passed"}))


if __name__ == "__main__":
    main()
