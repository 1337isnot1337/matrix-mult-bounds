#!/usr/bin/env python3
"""Integer certificate for the fixed oblique residual's border-rank lower bound.

The written proof supplies the closed equalizer condition and its all-size
kernel calculation. This verifier checks literal coefficients, unit minors,
the exported native source maps, every saved control and every source hash.
Only the Python standard library is required.
"""

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
REPOSITORY = PACKAGE.parents[2]
PAIRED = Path("research/ai/2026-10-23-oblique-paired-repair")
BORDER = Path("research/ai/2026-10-23-oblique-border-repair")


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def digest(value):
    encoded = json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def records(tensor):
    return [[*key, value] for key, value in sorted(tensor.items())]


def canonical_residual(b):
    if type(b) is not int or b < 2:
        raise ValueError("Require an integer b>=2; n=b+2 and r=b+1.")
    wings = b - 1
    tensor = {
        (0, 0, 0): 1, (0, 1, 1): 1,
        (1, 2, 2): 1, (1, 3, 3): 1,
        (2, 0, 1): 1, (2, 1, 4): 1,
        (2, 3, 2): 1, (2, 4, 3): 1, (2, 0, 2): 1,
    }
    for j in range(wings):
        tensor[3 + j, 0, 5 + 2 * j] = 1
        tensor[3 + j, 1, 6 + 2 * j] = 1
        tensor[3 + wings + j, 5 + 2 * j, 2] = 1
        tensor[3 + wings + j, 6 + 2 * j, 3] = 1
    return [2 * b + 1, 2 * b + 3, 2 * b + 3], tensor


def embedding_bases(b):
    r, s = b + 1, b - 1
    wings = [i for i in range(r) if i not in (0, s)]
    first = [{r * s: 1}, {s: 1}, {r * s + s: 1}]
    first += [{r * s + j: 1} for j in wings]
    first += [{r * i + s: 1} for i in wings]
    second = [{4 * s: 1, 1: -1}, {4 * s + 2: 1, 3: -1},
              {0: 1}, {1: 1}, {4 * s + 1: 1}]
    second += [{4 * i + h: 1} for i in wings for h in (0, 1)]
    third = [{0: 1}, {2 * r: 1}, {s: 1, 2 * r: -1},
             {r + s: 1, 3 * r: -1}, {2 * r + s: 1}]
    third += [{h * r + j: 1} for j in wings for h in (0, 2)]
    return [first, second, third]


def expand(tensor, bases):
    result = {}
    for (a, b, c), coefficient in tensor.items():
        for (i, x), (j, y), (k, z) in product(bases[0][a].items(),
                                             bases[1][b].items(),
                                             bases[2][c].items()):
            key = (i, j, k)
            result[key] = result.get(key, 0) + coefficient * x * y * z
    return {key: value for key, value in result.items() if value}


def equalizer_rows(shape, tensor):
    """Rows of (L,M) -> (1 tensor L tensor 1)T-(1 tensor 1 tensor M)T.

    L_ij and M_ij mean output i, input j. All m*m L columns precede
    all m*m M columns. Zero output rows are omitted, with labels retained.
    """
    require(shape[1] == shape[2], "The two long dimensions must agree")
    m = shape[1]
    rows = {}
    for (a, b, c), coefficient in tensor.items():
        for i in range(m):
            row = rows.setdefault((a, i, c), {})
            column = m * i + b
            row[column] = row.get(column, 0) + coefficient
            row = rows.setdefault((a, b, i), {})
            column = m * m + m * i + c
            row[column] = row.get(column, 0) - coefficient
    return {label: {column: value for column, value in row.items() if value}
            for label, row in rows.items() if any(row.values())}


def unit_reduce(rows):
    """Sparse integer elimination. No division by a nonunit is accepted."""
    basis, selected, pivots, values = {}, [], [], []
    for label in sorted(rows):
        row = dict(rows[label])
        while row:
            pivot = min(row)
            if pivot not in basis:
                value = row[pivot]
                require(value in (-1, 1), "A displayed elimination pivot is not a unit")
                basis[pivot] = {column: value * x for column, x in row.items()}
                selected.append(list(label))
                pivots.append(pivot)
                values.append(value)
                break
            factor = row[pivot]
            for column, value in basis[pivot].items():
                updated = row.get(column, 0) - factor * value
                if updated:
                    row[column] = updated
                else:
                    row.pop(column, None)
    determinant = 1
    for value in values:
        determinant *= value
    return {"order": len(pivots), "row_labels": selected, "columns": pivots,
            "unit_pivots": values, "determinant": determinant}


def check_minor(rows, minor):
    order = minor["order"]
    labels = [tuple(label) for label in minor["row_labels"]]
    columns = minor["columns"]
    require(len(labels) == len(set(labels)) == len(columns) == len(set(columns)) == order,
            "A displayed minor repeats or omits a row or column")
    require(all(label in rows for label in labels), "A minor row is not present")
    chosen = set(columns)
    projected = {label: {column: value for column, value in rows[label].items()
                         if column in chosen} for label in labels}
    require(unit_reduce(projected) == minor,
            "The displayed unit minor does not replay")
    return True


def kernel_generators(m):
    identity = {m * i + i: 1 for i in range(m)}
    identity.update({m * m + m * i + i: 1 for i in range(m)})
    # On B, y (index 4) -> Z (index 1); on C, T (4) -> S (3).
    nilpotent = {m + 4: 1, m * m + 3 * m + 4: 1}
    return [identity, nilpotent]


def check_equalizer(b, include_minor=False):
    shape, tensor = canonical_residual(b)
    m = shape[1]
    rows = equalizer_rows(shape, tensor)
    minor = unit_reduce(rows)
    require(minor["order"] == 2 * m * m - 2, "The equalizer rank changed")
    check_minor(rows, minor)
    generators = kernel_generators(m)
    for generator in generators:
        require(all(sum(value * generator.get(column, 0) for column, value in row.items()) == 0
                    for row in rows.values()), "A displayed generator is not in the kernel")
    require(generators[0].get(0) == 1 and generators[1].get(0, 0) == 0
            and generators[1][m + 4] == 1 and generators[0].get(m + 4, 0) == 0,
            "The two kernel generators are not independently certified")
    result = {
        "b": b, "n": b + 2, "r": b + 1,
        "concise_format": shape,
        "concise_tensor_sha256": digest(records(tensor)),
        "concise_nonzero_coefficients": len(tensor),
        "matrix_format_with_zero_rows": [shape[0] * m * m, 2 * m * m],
        "matrix_nonzero_rows": len(rows),
        "matrix_sha256": digest([[*label, [[column, value] for column, value in sorted(row.items())]]
                                 for label, row in sorted(rows.items())]),
        "unit_minor_order": minor["order"],
        "unit_minor_determinant": minor["determinant"],
        "equalizer_kernel_dimension": 2,
        "kernel_generators": [[[column, value] for column, value in sorted(generator.items())]
                              for generator in generators],
        "rank_ceiling_for_border_rank_at_most_m": 2 * m * m - m,
        "border_rank_lower_bound": m + 1,
        "inherited_border_rank_upper_bound": 4 * (b + 1) - 2,
        "unit_minor_and_kernel_replayed": True,
    }
    if include_minor:
        result["unit_minor"] = minor
        result["literal_concise_tensor"] = records(tensor)
    return result


def integer(value):
    require(not isinstance(value, (float, bool)), "Integer inputs cannot be floats or booleans")
    fraction = Fraction(value)
    require(fraction.denominator == 1, "A source-map coefficient is not integral")
    return int(fraction)


def replay_native(repository, saved_case=None):
    if saved_case is None:
        saved = json.loads((Path(repository) / PAIRED / "witness.json").read_text())
        saved_case = next(case for case in saved["cases"] if case["variant"] == "product-oblique")
    require(saved_case["source"] == [6, 4] and saved_case["target"] == [5, 4, 5],
            "The exported native case has different dimensions")
    maps = [[[integer(value) for value in row] for row in matrix] for matrix in saved_case["maps"]]
    require([len(matrix) for matrix in maps] == [25, 20, 20]
            and all(len(row) == 36 for matrix in maps for row in matrix),
            "The native maps have unexpected shapes")
    columns = [[{i: row[j] for i, row in enumerate(matrix) if row[j]}
                for j in range(36)] for matrix in maps]
    image = {}
    for p, q, y, v in product(range(6), range(6), range(4), range(4)):
        source = (6 * p + q, 9 * y + q + v, 4 * (p + y) + v)
        for (a, x), (b, yy), (c, z) in product(*(columns[leg][source[leg]].items()
                                              for leg in range(3))):
            image[a, b, c] = image.get((a, b, c), 0) + x * yy * z
    target = {(5 * i + j, 4 * i + h, 5 * h + j): 1
              for i, h, j in product(range(5), range(4), range(5))}
    native = {key: target.get(key, 0) - image.get(key, 0) for key in set(target) | set(image)}
    native = {key: value for key, value in native.items() if value}
    shape, canonical = canonical_residual(4)
    embedded = expand(canonical, embedding_bases(4))
    saved_residual = {(a, b, c): integer(value)
                      for a, b, c, value in saved_case["verification"]["residual_coefficients"]}
    for key in product(range(25), range(20), range(20)):
        require(native.get(key, 0) == embedded.get(key, 0) == saved_residual.get(key, 0),
                "The literal equalizer tensor does not match an actual native coefficient")
    require(native == embedded == saved_residual, "A tensor coefficient lies outside the target")
    return {"source_coefficients_contracted": 576, "target_coordinates_compared": 10000,
            "native_residual_nonzero_coefficients": len(native),
            "native_residual_sha256": digest(records(native)),
            "concise_tensor_sha256": digest(records(canonical)),
            "literal_tensor_and_native_source_equal": True}


def source_pins(repository, source_record=None):
    if source_record is None:
        source_record = json.loads((PACKAGE / "sources.json").read_text())
    for entry in source_record["local_sources"]:
        path = Path(repository) / entry["path"]
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"],
                "Source hash mismatch: " + entry["path"])
    return {"count": len(source_record["local_sources"]), "all_match": True}


def check_predecessor(repository, controls):
    previous = json.loads((Path(repository) / BORDER / "full-residual-rank-certificate.json").read_text())
    require([case["b"] for case in previous["controls"]] == [case["b"] for case in controls],
            "The imported family controls differ")
    for earlier, current in zip(previous["controls"], controls):
        b = current["b"]
        shape, tensor = canonical_residual(b)
        require(earlier["concise_format"] == shape
                and earlier["concise_tensor_coefficients"] == records(tensor),
                "The literal tensor differs from the imported adapted residual")
        bases = [[[[index, value] for index, value in sorted(vector.items())]
                  for vector in leg] for leg in embedding_bases(b)]
        require(earlier["integer_embedding_bases"] == bases,
                "The native embedding differs from the imported unit basis")
        require(all(minor["determinant"] == 1 for minor in earlier["embedding_unit_minors"]),
                "The imported adapted bases lack unit embedding minors")
    return {"complete_adapted_controls_compared": len(controls), "all_match": True}


def build_certificate(repository=REPOSITORY):
    pins = source_pins(repository)
    controls = [check_equalizer(b, include_minor=(b == 4)) for b in [2, 3, 4, 5, 6, 7, 8, 12]]
    return {
        "claim": "AI-OBLIQUE-BORDER-EQUALIZER-001",
        "statement": "For b>=2,n=b+2,r=b+1, the fixed product-oblique residual has border rank at least 2*r+2.",
        "field_scope": "Geometric border rank over algebraic closures, and formal degeneration lower bounds, in every characteristic; usual tensor border rank over C.",
        "proof_status": "written-unreviewed",
        "source_pin_verification": pins,
        "predecessor_control_comparison": check_predecessor(repository, controls),
        "controls": controls,
        "native_n6_control": replay_native(repository),
        "n6_border_rank_interval": [12, 18],
        "inherited_n6_ordinary_rank": 19,
        "all_size_equality_from_written_proof": "dim ker Phi_E = 2",
        "whole_residual_border_rank_optimality_claimed": False,
        "arbitrary_source_map_optimality_claimed": False,
        "historical_novelty_claimed": False,
        "independent_mathematical_review": False,
        "formalized": False,
        "improves_omega": False,
    }


def verify_saved(path, repository=REPOSITORY):
    actual = build_certificate(repository)
    require(json.loads(Path(path).read_text()) == actual,
            "The complete saved equalizer certificate does not match")
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=REPOSITORY)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    if args.write:
        result = build_certificate(args.repository)
        args.write.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    else:
        result = verify_saved(PACKAGE / "certificate.json", args.repository)
    print(json.dumps({"claim": result["claim"], "controls": len(result["controls"]),
                      "source_pins": result["source_pin_verification"]["count"],
                      "n6_border_rank_interval": result["n6_border_rank_interval"],
                      "native_n6_control": result["native_n6_control"]}, indent=2))


if __name__ == "__main__":
    main()
