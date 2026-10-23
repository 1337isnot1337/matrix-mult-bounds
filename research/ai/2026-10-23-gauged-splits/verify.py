"""Exact six-split border seed using positive tensor valuations.

The discarded rank-one tensors vanish although two displayed factors
have poles and the combined unscaled arrow representation is not nilpotent.
Only the Python standard library is required.
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
SPEC = importlib.util.spec_from_file_location("gauged_split_exact_helpers", PRIOR / "verify_split.py")
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)
BASE_CERTIFICATE_SHA256 = "a8f3dc9f8e3cd2ce1ef4a581dee01985e47a52077227260b48a1832e0fe79c08"
REPLACEMENTS = [[0, 18, -1], [17, 8, 1], [48, 2, -1],
                [56, 22, -1], [43, 59, -1], [47, 73, 1]]
SCHEMA = "gauged-split-border-seed-v1"
SCOPE = ("Exact rank-76 border seed with six split deletions by positive tensor "
         "valuations; no rank record, exponent improvement, or Q(6,4) map.")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def base_certificate():
    data = (PRIOR / "split_certificate.json").read_bytes()
    require(hashlib.sha256(data).hexdigest() == BASE_CERTIFICATE_SHA256,
            "The retained four-split physical-basis certificate changed")
    return json.loads(data)


def collect_coefficients(terms):
    """Collect all degrees and coordinates directly from sparse factor arrays."""
    output = {}
    for u, v, w in terms:
        for a, x, e in u:
            for b, y, f in v:
                for c, z, g in w:
                    key = (e + f + g, a, b, c)
                    output[key] = output.get(key, Fraction(0)) + x * y * z
    return {key: value for key, value in output.items() if value}


def coefficient_replay(certificate):
    surviving = V.parse_factors(certificate["surviving_factors"], 76)
    discarded = V.parse_factors(certificate["discarded_factors"], 6)
    minimums = [[min(exponent for _, _, exponent in factor) for factor in term]
                for term in discarded]
    require(all(sum(row) > 0 for row in minimums),
            "A discarded rank-one tensor has nonpositive valuation")
    output = collect_coefficients(surviving)
    require(not any(key[0] < 0 for key in output),
            "The surviving tensor has a negative Laurent coefficient")
    # Check every one of the 20*25*20 positions, including all 9900 zeros.
    constants = 0
    for a in range(20):
        i, j = divmod(a, 5)
        for b in range(25):
            other_j, k = divmod(b, 5)
            for c in range(20):
                other_k, other_i = divmod(c, 4)
                expected = int(j == other_j and k == other_k and i == other_i)
                actual = output.get((0, a, b, c), Fraction(0))
                require(actual == expected, "A constant matrix multiplication coefficient differs")
                constants += expected
    error = collect_coefficients(discarded)
    require({key: value for key, value in output.items() if key[0] > 0}
            == {key: -value for key, value in error.items()},
            "The full positive remainder differs from the negative discarded tensor")
    degrees = {str(degree): count for degree, count in
               sorted(Counter(key[0] for key in output).items())}
    return minimums, degrees, constants


def verify(certificate=None):
    if certificate is None:
        certificate = json.loads((PACKAGE / "certificate.json").read_text())
    require(certificate.get("schema") == SCHEMA, "Unknown gauged-split schema")
    require(certificate.get("scope") == SCOPE, "Gauged-split scope differs")
    require(certificate.get("seed_sha256") == V.SEED_SHA256, "External source pin differs")
    require(certificate.get("base_certificate_sha256") == BASE_CERTIFICATE_SHA256,
            "Physical-basis certificate pin differs")
    require(certificate.get("dimensions") == [4, 5, 5]
            and certificate.get("rank") == 76, "Unexpected tensor dimensions or rank")
    require(certificate.get("replacements") == REPLACEMENTS,
            "Unexpected six-split specification")
    original = base_certificate()
    require(certificate["basis_matrices"] == original["basis_matrices"]
            and certificate["weights"] == original["weights"],
            "Physical bases or weights differ from the retained exact witness")
    bases = [[[Fraction(x) for x in row] for row in matrix]
             for matrix in certificate["basis_matrices"]]
    require([V.determinant(matrix) for matrix in bases] == [1, -1, 1],
            "The three physical bases are not unimodular")
    surviving, discarded = V.split_seed(V.load_seed(), REPLACEMENTS)
    weights = certificate["weights"]
    require(V.transformed_factors(surviving, bases, weights) == certificate["surviving_factors"],
            "Surviving factors differ from the exact split construction")
    require(V.transformed_factors(discarded, bases, weights) == certificate["discarded_factors"],
            "Discarded factors differ from the exact split construction")
    minimums, degrees, constants = coefficient_replay(certificate)
    require(certificate["discarded_minimum_factor_valuations"] == minimums,
            "Recorded discarded factor valuations differ")
    require(certificate["nonzero_coefficients_by_degree"] == degrees,
            "Recorded Laurent coefficient counts differ")
    require(certificate["negative_coefficients"] == 0
            and certificate["constant_coefficients"] == constants == 100,
            "Recorded coefficient totals differ")
    require(certificate["ramification"] == 3, "Unexpected parameter ramification")
    gauges = certificate["factor_gauge_exponents"]
    require(len(gauges) == 6, "Expected one factor gauge per discarded term")
    for row, gauge in zip(minimums, gauges):
        require(len(gauge) == 3 and all(type(x) is int for x in gauge)
                and sum(gauge) == 0, "A factor gauge does not preserve its tensor term")
        require(all(3 * value + adjustment >= 1 for value, adjustment in zip(row, gauge)),
                "A gauged factor has nonpositive valuation after ramification")
    # This nonzero mixed cycle proves that common positive unscaled arrow
    # valuations are impossible, independently of the old image-flag algorithm.
    mixed = V.product(V.product(discarded[0][0], discarded[5][1]), discarded[0][2])
    mixed_trace = sum(mixed[i][i] for i in range(4))
    require(mixed_trace == 1, "The nonzero mixed-cycle witness changed")
    require(certificate["unscaled_mixed_cycle"] == {"discarded_labels": [0, 5, 0], "trace": 1},
            "Recorded unscaled mixed-cycle witness differs")
    directions = set()
    for term in surviving:
        flat = [x for row in term[0] for x in row]
        first = next(x for x in flat if x)
        directions.add(tuple(x / first for x in flat))
    require(len(directions) == 70, "Unexpected surviving U direction count")
    return {
        "claim_id": "AI-EXTERNAL-GAUGED-SPLIT-SEED-006",
        "seed_sha256": V.SEED_SHA256,
        "intermediate_exact_terms": 82,
        "surviving_border_terms": 76,
        "distinct_U_directions": len(directions),
        "discarded_minimum_factor_valuations": minimums,
        "discarded_tensor_valuations": [sum(row) for row in minimums],
        "all_ungauged_discarded_factors_positive": all(min(row) > 0 for row in minimums),
        "all_ramified_gauged_discarded_factors_positive": True,
        "unscaled_mixed_cycle_trace": int(mixed_trace),
        "constant_positions_checked": 10000,
        "constant_nonzero_coefficients": constants,
        "negative_coefficients": 0,
        "positive_nonzero_coefficients": sum(count for degree, count in degrees.items() if degree != "0"),
        "nonzero_coefficients_by_degree": degrees,
        "Q64_maps_constructed": False,
        "rank_record_claimed": False,
        "proof_status": "written-unreviewed",
        "improves_omega": False,
    }


def build_certificate():
    base = base_certificate()
    bases = [[[Fraction(x) for x in row] for row in matrix]
             for matrix in base["basis_matrices"]]
    surviving, discarded = V.split_seed(V.load_seed(), REPLACEMENTS)
    ss = V.transformed_factors(surviving, bases, base["weights"])
    ds = V.transformed_factors(discarded, bases, base["weights"])
    minimums = [[min(exponent for _, _, exponent in factor) for factor in term] for term in ds]
    gauges = []
    for a, b, c in minimums:
        gauges.append([0, 0, 0] if min(a, b, c) > 0
                      else [1 - 3*a, 1 - 3*b, 3*a + 3*b - 2])
    output = collect_coefficients(V.parse_factors(ss, 76))
    certificate = {
        "schema": SCHEMA, "scope": SCOPE,
        "seed_sha256": V.SEED_SHA256,
        "base_certificate_sha256": BASE_CERTIFICATE_SHA256,
        "dimensions": [4, 5, 5], "rank": 76,
        "replacements": REPLACEMENTS,
        "basis_matrices": base["basis_matrices"], "weights": base["weights"],
        "surviving_factors": ss, "discarded_factors": ds,
        "discarded_minimum_factor_valuations": minimums,
        "ramification": 3, "factor_gauge_exponents": gauges,
        "unscaled_mixed_cycle": {"discarded_labels": [0, 5, 0], "trace": 1},
        "nonzero_coefficients_by_degree": {str(degree): count for degree, count in
                                           sorted(Counter(key[0] for key in output).items())},
        "negative_coefficients": sum(key[0] < 0 for key in output),
        "constant_coefficients": sum(key[0] == 0 for key in output),
    }
    verify(certificate)
    return certificate


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()
    if args.write_certificate:
        witness = build_certificate()
        args.write_certificate.write_text(json.dumps(witness, indent=2) + "\n")
    else:
        witness = None
    print(json.dumps(verify(witness), indent=2))
