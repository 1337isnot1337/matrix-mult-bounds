#!/usr/bin/env python3
"""Exact finite controls for the support-capacity proofs.

These controls do not certify the algebraic-geometric dimension theorems.
No numerical optimizer or third-party dependency is used.
"""

from argparse import ArgumentParser
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def rank(rows, prime=None):
    """Row rank over Q, or the specified prime field."""
    basis = {}
    for source in rows:
        row = {
            j: (value % prime if prime else Fraction(value))
            for j, value in enumerate(source)
            if (value % prime if prime else value)
        }
        while row:
            pivot = min(row)
            if pivot in basis:
                scale = row[pivot]
                for j, value in basis[pivot].items():
                    new = row.get(j, 0) - scale * value
                    if prime:
                        new %= prime
                    if new:
                        row[j] = new
                    else:
                        row.pop(j, None)
            else:
                inverse = pow(row[pivot], -1, prime) if prime else 1 / row[pivot]
                basis[pivot] = {
                    j: (value * inverse % prime if prime else value * inverse)
                    for j, value in row.items()
                }
                break
    return len(basis)


def unit(size, index):
    return [int(j == index) for j in range(size)]


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def tensor_vector(left, right):
    return [a * b for a in left for b in right]


def add_entry(mapping, key, value):
    mapping[key] = mapping.get(key, 0) + value
    if not mapping[key]:
        del mapping[key]


def laurent_outer(a, b, c):
    """Vectors are dictionaries (coordinate, power) -> integer."""
    result = {}
    for (i, p), x in a.items():
        for (j, q), y in b.items():
            for (k, s), z in c.items():
                add_entry(result, (i, j, k, p + q + s), x * y * z)
    return result


def add_tensors(*tensors):
    result = {}
    for tensor in tensors:
        for key, value in tensor.items():
            add_entry(result, key, value)
    return result


def contract_laurent(tensor, leg, functional):
    result = {}
    for (a, b, c, power), value in tensor.items():
        coords = (a, b, c)
        for (index, shift), coefficient in functional.items():
            if coords[leg] == index:
                remaining = tuple(coords[i] for i in range(3) if i != leg)
                add_entry(result, (*remaining, power + shift), value * coefficient)
    return result


def encoded(mapping):
    return [[*key, value] for key, value in sorted(mapping.items())]


def polynomial_minor(columns, coordinates):
    result = {}
    for permutation in permutations(range(len(columns))):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
        term = {0: (-1)**inversions}
        for row, column in enumerate(permutation):
            entry = {power: value for (index, power), value in columns[column].items()
                     if index == coordinates[row]}
            multiplied = {}
            for p, x in term.items():
                for q, y in entry.items():
                    add_entry(multiplied, p + q, x * y)
            term = multiplied
        for power, value in term.items():
            add_entry(result, power, value)
    return result


def pole_cancellation_control(leading_coefficient=1):
    """Replay README (12), including each separately polar summand."""
    t_image = laurent_outer(
        {(1, -1): leading_coefficient},
        {(0, 0): 1, (1, 1): 1},
        {(0, 0): 1, (1, 1): 1},
    )
    a_maps = [
        {(0, 0): 1, (1, -1): -1},
        {(2, 0): 1, (1, 0): -1},
        {(3, 0): 1, (1, 1): -1},
    ]
    e_image = add_tensors(*[
        laurent_outer(a_map, {(b, 0): 1}, {(c, 0): 1})
        for a_map, (b, c) in zip(a_maps, [(0, 0), (1, 0), (1, 1)])
    ])
    target = {(2 * i + j, i, j, 0): 1 for i in range(2) for j in range(2)}
    if add_tensors(t_image, e_image) != target:
        raise ValueError("The Laurent images do not sum to the complete target")
    annihilator = {(0, 1): -1, (1, 0): 1}
    contractions = []
    for leg in (1, 2):
        if contract_laurent(t_image, leg, annihilator):
            raise ValueError("The moving annihilator does not kill the source image")
        correction = contract_laurent(e_image, leg, annihilator)
        if correction != contract_laurent(target, leg, annihilator):
            raise ValueError("The auxiliary contraction is not the target contraction")
        if any(key[-1] < 0 for key in correction):
            raise ValueError("An annihilator contraction still has a pole")
        contractions.append(encoded(correction))
    # Columns t*a_maps[0], a_maps[1], a_maps[2] give a regular basis.
    regular_basis = [
        {(0, 1): 1, (1, 0): -1},
        a_maps[1],
        a_maps[2],
    ]
    limits = [[vector.get((i, 0), 0) for i in range(4)] for vector in regular_basis]
    if rank(limits) != 3 or rank(limits, 2) != 3:
        raise ValueError("The regular first-support basis loses dimension")
    minor = polynomial_minor(regular_basis, (1, 2, 3))
    if minor != {0: -1}:
        raise ValueError("The unit support minor changed")
    return {
        "target_shape": [4, 2, 2],
        "source_first_support": 3,
        "source_image": encoded(t_image),
        "auxiliary_image": encoded(e_image),
        "total_target": encoded(target),
        "annihilator_contractions": contractions,
        "saturated_first_basis_at_zero": limits,
        "regular_basis_unit_minor": minor[0],
        "negative_powers_cancel": True,
        "union_support_dimension": 3,
    }


def capacity_control(l, h, r, k_b, k_c, label):
    """Compute forced support directly by contracting native M(l,h,r)."""
    if any(len(f) != l * h for f in k_b) or any(len(g) != h * r for g in k_c):
        raise ValueError("Wrong annihilator coefficient dimensions")
    w_b_vectors = [[f[i * h + alpha] for i in range(l)]
                   for f in k_b for alpha in range(h)]
    w_c_vectors = [[g[alpha * r + j] for j in range(r)]
                   for g in k_c for alpha in range(h)]
    w_b, w_c = rank(w_b_vectors), rank(w_c_vectors)
    contracted_first_vectors = []
    for f in k_b:
        for alpha in range(h):
            for j in range(r):
                vector = [0] * (l * r)
                for i in range(l):
                    vector[i * r + j] += f[i * h + alpha]
                contracted_first_vectors.append(vector)
    for g in k_c:
        for i in range(l):
            for alpha in range(h):
                vector = [0] * (l * r)
                for j in range(r):
                    vector[i * r + j] += g[alpha * r + j]
                contracted_first_vectors.append(vector)
    actual = rank(contracted_first_vectors)
    expected = r * w_b + l * w_c - w_b * w_c
    if actual != expected:
        raise ValueError("The native contraction support does not equal the union formula")
    a_b, a_c = l * h - rank(k_b), h * r - rank(k_c)
    rounded = l * r - (a_b // h) * (a_c // h)
    if actual < rounded:
        raise ValueError("The rounded long-rank consequence failed")
    return {
        "label": label, "target": [l, h, r],
        "annihilator_dimensions": [rank(k_b), rank(k_c)],
        "long_image_ranks": [a_b, a_c],
        "coefficient_span_dimensions": [w_b, w_c],
        "native_contraction_support_rank": actual,
        "union_formula": expected,
        "rank_only_lower_bound": rounded,
    }


def support_controls():
    cases = []
    l, h, r = 3, 2, 4
    w_b = [[1, 1, 0], [0, 1, 1]]
    w_c = [[1, 0, 1, 0], [0, 1, 0, 1]]
    k_b = [tensor_vector(vector, unit(h, alpha)) for vector in w_b for alpha in range(h)]
    k_c = [tensor_vector(unit(h, alpha), vector) for alpha in range(h) for vector in w_c]
    cases.append(capacity_control(l, h, r, k_b, k_c, "noncoordinate_union"))
    for n, b in [(5, 4), (6, 4), (9, 4), (7, 5)]:
        r = n - 1
        bad = range(b - 1, n - 2)
        k_b = [unit(4 * r, 4 * i + alpha) for i in bad for alpha in (0, 2)]
        k_c = [unit(4 * r, alpha * r + j) for j in bad for alpha in (0, 1)]
        result = capacity_control(r, 4, r, k_b, k_c, f"oblique_n{n}_b{b}")
        if result["union_formula"] != r * r - b * b:
            raise ValueError("The oblique annihilator pattern disagrees with its first support")
        cases.append(result)
    return cases


def q_slice_formula(x, width=4):
    n = len(x)
    long = n + width - 1
    rows = []
    for y in range(width):
        for z in range(long):
            rows.append([
                x[w - y][z - v] if 0 <= w - y < n and 0 <= z - v < n else 0
                for w in range(long) for v in range(width)
            ])
    return rows


def q_slice_native(x, width=4):
    """Build from every coefficient of Q, independently of the offset formula."""
    n = len(x)
    long = n + width - 1
    result = [[0] * (width * long) for _ in range(width * long)]
    for p, q, y, v in product(range(n), range(n), range(width), range(width)):
        result[y * long + q + v][(p + y) * width + v] += x[p][q]
    return result


def biform_product(h, f, g):
    """Affine coefficient lists represent fixed-degree homogeneous binary forms."""
    dx, dy = len(h) - 1, len(h[0]) - 1
    result = [[0] * (len(g) + dy) for _ in range(len(f) + dx)]
    for a, row in enumerate(h):
        for b, value in enumerate(row):
            for i, fi in enumerate(f):
                for j, gj in enumerate(g):
                    result[a + i][b + j] += value * fi * gj
    return result


def divisible_space(form, multiplier_degree, width, side):
    degree = len(form) - 1 + multiplier_degree
    long = degree + 1
    result = []
    for short in range(width):
        for shift in range(multiplier_degree + 1):
            vector = [0] * (width * long)
            for i, value in enumerate(form):
                index = short * long + i + shift if side == "B" else (i + shift) * width + short
                vector[index] += value
            result.append(vector)
    return result


def multiplier_control(h, f, g, label):
    x = biform_product(h, f, g)
    if len(x) != len(x[0]):
        raise ValueError("The paired source needs equal outer degrees")
    source = q_slice_native(x)
    if source != q_slice_formula(x):
        raise ValueError("Native Q coefficients and the slice formula disagree")
    dx, dy = len(h) - 1, len(h[0]) - 1
    b_space = divisible_space(g, dy + 3, 4, "B")
    c_space = divisible_space(f, dx + 3, 4, "C")
    b_dim, c_dim = rank(b_space), rank(c_space)
    if rank(b_space + transpose(source)) != b_dim:
        raise ValueError("A B image lies outside its claimed divisor space")
    if rank(c_space + source) != c_dim:
        raise ValueError("A C image lies outside its claimed divisor space")
    cases = []
    for prime in (None, 2, 3):
        coefficient_rank, raw_rank = rank(x, prime), rank(source, prime)
        if coefficient_rank == 0 or raw_rank < coefficient_rank + 15:
            raise ValueError("The nonzero native source-slice lower bound failed")
        cases.append({"field": "Q" if prime is None else f"F{prime}",
                      "coefficient_rank": coefficient_rank, "raw_slice_rank": raw_rank})
    return {"label": label, "n": len(x), "multiplier": h, "f": f, "g": g,
            "containing_space_dimensions": [b_dim, c_dim], "rank_controls": cases}


def source_and_multiplier_controls():
    cases = [
        multiplier_control([[1]], [1, -1, 0, 1], [1, 0, 1, 1], "pure_product"),
        multiplier_control([[1, 0], [0, 1]], [1, -1, 0, 1], [1, 0, 1, 1], "one_plus_xy"),
        multiplier_control([[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                           [1, 1, 1], [1, 0, 1], "one_plus_xy_plus_x2y2"),
    ]
    raw_cases = []
    for n in (2, 3, 5, 8):
        x = [unit(n, i) for i in range(n)]
        source = q_slice_native(x)
        if source != q_slice_formula(x):
            raise ValueError("The two native source constructions disagree")
        for prime in (None, 2, 3):
            cr, sr = rank(x, prime), rank(source, prime)
            if sr < cr + 15:
                raise ValueError("The source lower bound failed on a diagonal control")
            raw_cases.append({"n": n, "field": "Q" if prime is None else f"F{prime}",
                              "coefficient_rank": cr, "raw_slice_rank": sr})
    first_map_cases = []
    h = [[1, 0], [0, 1]]
    for f_rows, g_rows, label in [
        ([unit(3, i) for i in range(3)], [unit(3, i) for i in range(3)], "injective"),
        ([unit(3, 0), unit(3, 1), [1, 1, 0]],
         [unit(3, i) for i in range(3)], "one_factor_deficient"),
    ]:
        image = [[value for row in biform_product(h, f, g) for value in row]
                 for f in f_rows for g in g_rows]
        for prime in (None, 2, 3):
            f_rank, g_rank, l_rank = rank(f_rows, prime), rank(g_rows, prime), rank(image, prime)
            if l_rank != f_rank * g_rank:
                raise ValueError("Nonzero polynomial multiplication lost first-map rank")
            first_map_cases.append({"label": label, "field": "Q" if prime is None else f"F{prime}",
                                    "factor_ranks": [f_rank, g_rank], "first_map_rank": l_rank})
    return {"multiplier_controls": cases, "native_diagonal_controls": raw_cases,
            "first_map_rank_controls": first_map_cases}


def rank_loss_controls():
    n, width = 6, 4
    long = n + width - 1
    x = [[int(p == 2 and q == 2) for q in range(n)] for p in range(n)]
    source = q_slice_native(x)
    paired_rows = [y * long + 2 + v for y in range(width) for v in range(width)]
    paired_columns = [(2 + y) * width + v for y in range(width) for v in range(width)]
    cases = []
    for c_losses in (6, 7):
        removed_b = set(paired_rows[:5])
        removed_c = set(paired_columns[5:5 + c_losses])
        removed_b.update([i for i in range(width * long) if i not in paired_rows][:11])
        removed_c.update([i for i in range(width * long) if i not in paired_columns][:16 - c_losses])
        projected = [[value for j, value in enumerate(row) if j not in removed_c]
                     for i, row in enumerate(source) if i not in removed_b]
        actual = rank(projected)
        expected = 16 - 5 - c_losses
        if len(removed_b) != 16 or len(removed_c) != 16 or actual != expected:
            raise ValueError("The exact two-sided rank-loss control failed")
        cases.append({"n": n, "raw_slice_rank": rank(source),
                      "long_map_ranks": [len(projected), len(projected[0])],
                      "slice_kernel_intersections": [5, c_losses],
                      "compressed_slice_rank": actual,
                      "removed_B_coordinates": sorted(removed_b),
                      "removed_C_coordinates": sorted(removed_c)})
    return cases


def polynomial_first_map_bounds(n, c):
    if not isinstance(n, int) or not isinstance(c, int) or c < 0 or n <= c:
        raise ValueError("Require integers n>c>=0")
    r = n - c
    capped = min(r, max(0, 2 * n - 10 * c - 14))
    uncapped = max(0, 2 * n - 10 * c - 19)
    return {"n": n, "c": c, "r": r, "capped": capped,
            "uncapped": uncapped, "combined": max(capped, uncapped)}


def arithmetic_controls():
    widths = []
    for b in range(1, 5):
        dimension = b * (200 + b - 1)
        widths.append({"n": 200, "c": 1, "b": b, "source_long_dimension": dimension,
                       "first_support_lower_bound": 199**2 - min(199, dimension // 4)**2})
    bounds = [polynomial_first_map_bounds(n, 1) for n in (6, 12, 13, 16, 22, 23, 28, 29, 200)]
    threshold_controls = []
    for c in range(9):
        n = 9 * c + 14
        before = polynomial_first_map_bounds(n - 1, c)
        at = polynomial_first_map_bounds(n, c)
        if before["capped"] >= before["r"] or at["capped"] != at["r"]:
            raise ValueError("The exact capped threshold changed")
        threshold_controls.append({"c": c, "first_n_with_capped_bound_r": n})
    # Exhaust the rank-deficiency possibilities in Section 8, rather than
    # merely evaluating the final expression. This is a finite proof control.
    selected = 0
    boundary_records = []
    for c in range(9):
        kappa = 4 * (c + 3)
        for r in range(kappa - 2, kappa + 25):
            for df, dg in ((0, 0), (1, 0), (0, 1)):
                f, g = r - df, r - dg
                for db, dc in [(0, 0)] + [(d, 0) for d in range(1, 5)] + [(0, d) for d in range(1, 5)]:
                    kb, kc = kappa + db, kappa + dc
                    j = max(1, kc - f + 2)
                    du, dv = f - kc + j - 1, g - kb + 12 - j
                    if not (1 <= j <= 12 and 1 <= du <= f and 1 <= dv <= g):
                        raise ValueError("The higher-stratum thresholds have invalid dimensions")
                    if du + dv - 1 < 2 * r - 2 * kappa + 5:
                        raise ValueError("The Segre lower bound is too small")
                    selected += 1
                    if c == 1 and r == kappa - 2 and df + dg + db + dc == 5:
                        boundary_records.append({"factor_ranks": [f, g], "kernel_dimensions": [kb, kc],
                                                 "j": j, "good_dimensions": [du, dv]})
    return {"width_bounds": widths, "polynomial_first_map_bounds": bounds,
            "exact_capped_thresholds": threshold_controls,
            "positive_dimension_choices_checked": selected,
            "boundary_dimension_choices": boundary_records}


def verify_local_sources():
    root = HERE.parents[2]
    record = json.loads((HERE / "sources.json").read_text())
    checked = []
    for source in record["local_sources"]:
        path = root / source["path"]
        if sha256(path.read_bytes()).hexdigest() != source["sha256"]:
            raise ValueError(f"Changed pinned source: {source['path']}")
        checked.append(source["path"])
    return checked


def certificate():
    return {
        "schema": "first-support-capacity-v1",
        "scope": "Exact finite controls; written geometric proofs remain unreviewed",
        "pole_cancellation": pole_cancellation_control(),
        "support_unions": support_controls(),
        "source_slices": source_and_multiplier_controls(),
        "rank_loss": rank_loss_controls(),
        "integer_consequences": arithmetic_controls(),
    }


def validate_certificate(candidate):
    if candidate != certificate():
        raise ValueError("Saved certificate differs from complete exact reconstruction")
    return True


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    sources = verify_local_sources()
    result = certificate()
    if args.check:
        saved = json.loads((HERE / "certificate.json").read_text())
        if result != saved:
            raise ValueError("Saved certificate differs from complete exact reconstruction")
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"verified_local_sources": sources,
                      "native_source_convention": "A_pq B_y,q+v C_p+y,v",
                      "support_controls": len(result["support_unions"]),
                      "dimension_choices": result["integer_consequences"]["positive_dimension_choices_checked"],
                      "saved_certificate_checked": args.check}, indent=2))


if __name__ == "__main__":
    main()
