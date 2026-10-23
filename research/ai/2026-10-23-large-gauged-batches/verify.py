"""Exact ten- and eleven-split border seeds; standard-library acceptance.

The saved witnesses do not depend on the numerical discovery solver.
The complete Laurent tensors are regenerated and contracted over Q.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
PRIOR = PACKAGE.parent / "2026-10-23-flip-escape"
SPEC = importlib.util.spec_from_file_location("large_gauged_exact_helpers", PRIOR / "verify_split.py")
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)
SCHEMA = "large-gauged-split-border-seed-v1"
SCOPE = ("Exact rank-76 border seeds with ten or eleven U-factor replacements; "
         "no rank record, exponent improvement, search optimum, or Q(6,4) map.")
VARIANTS = {
    "ten": {
        "basis_file": "split_certificate.json",
        "basis_sha256": "a8f3dc9f8e3cd2ce1ef4a581dee01985e47a52077227260b48a1832e0fe79c08",
        "determinants": [1, -1, 1],
        "replacements": [[36, 75, -1], [46, 44, 1], [47, 38, 1], [48, 2, -1],
                         [51, 55, -1], [57, 16, 1], [61, 75, -1], [62, 56, 1],
                         [70, 5, 1], [73, 38, 1]],
        "weights": [[0, -20, 19, 2], [0, -12, 0, -13, 1], [0, 0, -5, 0, 0]],
    },
    "eleven": {
        "basis_file": "five_split_certificate.json",
        "basis_sha256": "12cedfc73b6de98bb302b93941c05027b8acc41df03e4606b99363cb323e1c91",
        "determinants": [1, 1, -1],
        "replacements": [[12, 24, -1], [13, 32, -1], [16, 3, -1], [26, 32, 1],
                         [30, 24, -1], [47, 52, -1], [51, 64, -1], [55, 1, -1],
                         [60, 54, -1], [63, 34, -1], [73, 52, -1]],
        "weights": [[0, 1, 3, 11], [0, 2, 4, 4, 1], [0, 14, 13, 13, 15]],
    },
}
HIGH_WEIGHT_U = {17, 20, 26, 29, 30, 34, 35, 38, 39, 40, 41, 44,
                 46, 51, 55, 59, 61, 64, 67, 70, 72, 74, 75}
TEN_BLOCK = [2, 38, 39, 47, 48, 51, 52, 55, 73]
TEN_CONTACTS = [
    {"leg": 0, "left": [[38, 1], [52, 1]], "right": [[19, 1]],
     "right_component": [19], "dimensions": [5, 1, 5]},
    {"leg": 0, "left": [[38, 1], [51, -1], [52, 1]],
     "right": [[40, -1], [41, 1]], "right_component": [40, 41],
     "dimensions": [5, 2, 6]},
    {"leg": 1, "left": [[39, -1], [51, -1]], "right": [[26, 1]],
     "right_component": [26], "dimensions": [9, 1, 9]},
    {"leg": 2, "left": [[38, -1], [51, 1]], "right": [[58, 1]],
     "right_component": [58, 59], "dimensions": [5, 1, 5]},
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def basis_source(variant):
    specification = VARIANTS[variant]
    data = (PRIOR / specification["basis_file"]).read_bytes()
    require(hashlib.sha256(data).hexdigest() == specification["basis_sha256"],
            "The retained physical-basis source changed")
    return json.loads(data)


def flatten(matrix):
    return [entry for row in matrix for entry in row]


def direction(matrix):
    row = flatten(matrix)
    pivot = next(entry for entry in row if entry)
    return tuple(entry / pivot for entry in row)


def sharing_components(terms):
    parent = list(range(len(terms)))
    def root(index):
        while parent[index] != index:
            index = parent[index]
        return index
    for leg in range(3):
        previous = {}
        for index, term in enumerate(terms):
            key = direction(term[leg])
            if key in previous:
                parent[root(index)] = root(previous[key])
            previous[key] = index
    groups = {}
    for index in range(len(terms)):
        groups.setdefault(root(index), []).append(index)
    return sorted(groups.values())


def check_ten_contacts(terms):
    components = sharing_components(terms)
    require(TEN_BLOCK in components, "The ten-split sharing component changed")
    for record in TEN_CONTACTS:
        leg = record["leg"]
        require(record["right_component"] in components,
                "The recorded other sharing component changed")
        def combination(entries):
            return [sum(coefficient * flatten(terms[index][leg])[coordinate]
                        for index, coefficient in entries)
                    for coordinate in range(len(flatten(terms[0][leg])))]
        left, right = combination(record["left"]), combination(record["right"])
        require(left == right and any(left), "A nonzero cross-span relation differs")
        def rank(indices):
            return len(V.rref([flatten(terms[index][leg]) for index in indices])[1])
        dims = [rank(TEN_BLOCK), rank(record["right_component"]),
                rank(TEN_BLOCK + record["right_component"])]
        require(dims == record["dimensions"], "A cross-span dimension differs")
        require(dims[0] + dims[1] - dims[2] == 1,
                "A recorded cross-span intersection is not one-dimensional")
    return len(TEN_CONTACTS)


def collect_coefficients(terms):
    """Independent sparse contraction of every coordinate and Laurent degree."""
    output = {}
    for u, v, w in terms:
        for a, x, e in u:
            for b, y, f in v:
                for c, z, g in w:
                    key = (e + f + g, a, b, c)
                    output[key] = output.get(key, Fraction(0)) + x * y * z
    return {key: value for key, value in output.items() if value}


def coefficient_replay(certificate):
    count = len(certificate["replacements"])
    surviving = V.parse_factors(certificate["surviving_factors"], 76)
    discarded = V.parse_factors(certificate["discarded_factors"], count)
    minimums = [[min(e for _, _, e in factor) for factor in term] for term in discarded]
    require(all(sum(row) > 0 for row in minimums),
            "A discarded rank-one tensor has nonpositive valuation")
    output = collect_coefficients(surviving)
    error = collect_coefficients(discarded)
    require(not any(key[0] < 0 for key in output),
            "The surviving tensor has a negative Laurent coefficient")
    for a in range(20):
        i, j = divmod(a, 5)
        for b in range(25):
            other_j, k = divmod(b, 5)
            for c in range(20):
                other_k, other_i = divmod(c, 4)
                expected = int((i, j, k) == (other_i, other_j, other_k))
                require(output.get((0, a, b, c), Fraction(0)) == expected,
                        "A constant matrix multiplication coefficient differs")
    require({key: value for key, value in output.items() if key[0] > 0}
            == {key: -value for key, value in error.items()},
            "The full positive remainder differs from the discarded tensor")
    degrees = {str(degree): count for degree, count in
               sorted(Counter(key[0] for key in output).items())}
    return minimums, degrees


def verify(certificate):
    require(certificate.get("schema") == SCHEMA, "Unknown large-split schema")
    require(certificate.get("scope") == SCOPE, "Large-split scope differs")
    variant = certificate.get("variant")
    require(variant in VARIANTS, "Unknown large-split variant")
    specification = VARIANTS[variant]
    require(certificate.get("seed_sha256") == V.SEED_SHA256, "External source pin differs")
    require(certificate.get("basis_certificate_sha256") == specification["basis_sha256"],
            "Physical-basis source pin differs")
    require(certificate.get("dimensions") == [4, 5, 5] and certificate.get("rank") == 76,
            "Unexpected tensor dimensions or rank")
    require(certificate.get("replacements") == specification["replacements"],
            "The registered split specification differs")
    original = basis_source(variant)
    require(certificate["basis_matrices"] == original["basis_matrices"],
            "The physical bases differ from their retained source")
    bases = [[[Fraction(x) for x in row] for row in matrix]
             for matrix in certificate["basis_matrices"]]
    require([V.determinant(matrix) for matrix in bases] == specification["determinants"],
            "The physical bases are not the specified unimodular matrices")
    weights = certificate["weights"]
    require(len(weights) == 3 and all(len(row) == dimension
            and all(type(x) is int for x in row)
            for row, dimension in zip(weights, (4, 5, 5))), "Invalid physical weights")
    surviving, discarded = V.split_seed(V.load_seed(), specification["replacements"])
    require(V.transformed_factors(surviving, bases, weights) == certificate["surviving_factors"],
            "Surviving factors differ from the exact split construction")
    require(V.transformed_factors(discarded, bases, weights) == certificate["discarded_factors"],
            "Discarded factors differ from the exact split construction")
    minimums, degrees = coefficient_replay(certificate)
    require(certificate["minimum_factor_valuations"] == minimums,
            "Recorded discarded valuations differ")
    require(certificate["nonzero_coefficients_by_degree"] == degrees,
            "Recorded Laurent coefficient counts differ")
    gauges = certificate["factor_gauge_exponents"]
    require(certificate["ramification"] == 3 and len(gauges) == len(discarded),
            "Unexpected ramification or gauge count")
    for row, gauge in zip(minimums, gauges):
        require(len(gauge) == 3 and all(type(x) is int for x in gauge) and sum(gauge) == 0,
                "A factor gauge does not preserve its tensor term")
        require(all(3 * value + adjustment > 0 for value, adjustment in zip(row, gauge)),
                "A ramified gauged factor has nonpositive valuation")
    directions = len({direction(term[0]) for term in surviving})
    count = len(discarded)
    require(directions == certificate["distinct_U_directions"] == 76 - count,
            "The surviving U direction count differs")
    deleted_weight = sum(3 + int(i in HIGH_WEIGHT_U) for i, _, _ in specification["replacements"])
    require(certificate["deleted_original_U_weight"] == deleted_weight,
            "Recorded deleted original-U weight differs")
    contacts = check_ten_contacts(surviving) if variant == "ten" else 0
    require(certificate["cross_span_contacts"] == (TEN_CONTACTS if variant == "ten" else []),
            "Recorded cross-span contacts differ")
    return {
        "claim_id": "AI-EXTERNAL-LARGE-GAUGED-SPLIT-SEEDS-008",
        "variant": variant, "seed_sha256": V.SEED_SHA256,
        "intermediate_exact_terms": 76 + count, "surviving_border_terms": 76,
        "distinct_U_directions": directions, "discarded_terms": count,
        "discarded_tensor_valuations": [sum(row) for row in minimums],
        "all_constant_positions_checked": 10000,
        "constant_nonzero_coefficients": int(degrees["0"]), "negative_coefficients": 0,
        "positive_nonzero_coefficients": sum(n for degree, n in degrees.items() if degree != "0"),
        "nonzero_coefficients_by_degree": degrees,
        "deleted_original_U_weight": deleted_weight,
        "retained_original_U_weight": 251 - deleted_weight,
        "cross_initial_component_span_contacts_checked": contacts,
        "actual_cross_component_flip_constructed": False,
        "Q64_maps_constructed": False, "search_optimum_claimed": False,
        "rank_record_claimed": False, "proof_status": "written-unreviewed",
        "improves_omega": False,
    }


def build_certificate(variant):
    specification = VARIANTS[variant]
    original = basis_source(variant)
    bases = [[[Fraction(x) for x in row] for row in matrix]
             for matrix in original["basis_matrices"]]
    surviving, discarded = V.split_seed(V.load_seed(), specification["replacements"])
    ss = V.transformed_factors(surviving, bases, specification["weights"])
    ds = V.transformed_factors(discarded, bases, specification["weights"])
    minimums = [[min(e for _, _, e in factor) for factor in term] for term in ds]
    output = collect_coefficients(V.parse_factors(ss, 76))
    certificate = {
        "schema": SCHEMA, "scope": SCOPE, "variant": variant,
        "seed_sha256": V.SEED_SHA256, "basis_certificate_sha256": specification["basis_sha256"],
        "dimensions": [4, 5, 5], "rank": 76, "replacements": specification["replacements"],
        "basis_matrices": original["basis_matrices"], "weights": specification["weights"],
        "surviving_factors": ss, "discarded_factors": ds,
        "minimum_factor_valuations": minimums, "ramification": 3,
        "factor_gauge_exponents": [[1 - 3*a, 1 - 3*b, 3*a + 3*b - 2] for a, b, c in minimums],
        "nonzero_coefficients_by_degree": {str(degree): count for degree, count in
            sorted(Counter(key[0] for key in output).items())},
        "distinct_U_directions": len({direction(term[0]) for term in surviving}),
        "deleted_original_U_weight": sum(3 + int(i in HIGH_WEIGHT_U)
            for i, _, _ in specification["replacements"]),
        "cross_span_contacts": TEN_CONTACTS if variant == "ten" else [],
    }
    verify(certificate)
    return certificate


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--variant", choices=VARIANTS, default="eleven")
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()
    if args.write_certificate:
        witness = build_certificate(args.variant)
        args.write_certificate.write_text(json.dumps(witness, indent=2) + "\n")
    else:
        witness = json.loads((PACKAGE / (args.variant + "_certificate.json")).read_text())
    print(json.dumps(verify(witness), indent=2))
