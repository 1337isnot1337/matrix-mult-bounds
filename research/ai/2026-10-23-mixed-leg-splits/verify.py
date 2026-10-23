"""Exact mixed U/W split seed and its static third-factor cover obstruction.

The Laurent identity uses only the Python standard library.  --enumerate
also compiles the retained C99 enumerator and repeats all 367,290 four-sets.
Numerical discovery output is never an acceptance dependency.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
PRIOR = PACKAGE.parent / "2026-10-23-flip-escape"
GRID = PACKAGE.parent / "2026-10-23-grid-escape"
CLAIM = "AI-EXTERNAL-MIXED-LEG-SPLIT-SEED-011"
SCHEMA = "exact-mixed-leg-split-border-seed-v1"
SCOPE = ("A 76-term border seed from eleven U and two W replacements; "
         "the earlier two weighted screens pass, but the current W directions "
         "cannot be covered by nine rank-at-most-four groups. No all-flips "
         "obstruction, search optimum, rank record, or exponent improvement.")
W_SCHEMA = "mixed-leg-static-W-obstruction-v1"
W_SCOPE = ("Only the displayed surviving W directions, their common invertible "
           "linear images, and nonzero scalar rescalings. No obstruction to "
           "arbitrary subsequent flips, singular limits, or general source maps.")
PINS = {
    "research/ai/2026-10-21-external-grid-seed/factors.json":
        "bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3",
    "research/ai/2026-10-23-flip-escape/five_split_certificate.json":
        "12cedfc73b6de98bb302b93941c05027b8acc41df03e4606b99363cb323e1c91",
    "research/ai/2026-10-23-grid-escape/verify.py":
        "06ffba18bbc832831682ed85e390a67a2996c9b59b44220ac9312e3d03d24617",
    "research/ai/2026-10-23-grid-escape/weighted_flats.c":
        "7174304c15b71139d4a9087795baba9e40b2bc802d89fe954f93c8e3c66b4dee",
    "research/ai/2026-10-23-grid-escape/enumeration.json":
        "5c646e067324eb630215e3e4fc5fecf0f2347dd0af27dd4461c8fef3ad7d6e07",
    "research/ai/2026-10-23-grid-escape/w_enumeration.json":
        "cacd4fb5caf900fc1c3913363701514371c63b3a8420db9286820eac76ff3d2e",
}
REPLACEMENTS = [
    [0, 16, 3, -1], [0, 24, 12, -1], [0, 26, 13, -1],
    [0, 30, 12, 1], [0, 32, 13, -1], [0, 51, 64, -1],
    [0, 52, 47, -1], [0, 55, 1, -1], [0, 60, 54, -1],
    [0, 63, 34, -1], [0, 73, 47, 1], [2, 12, 8, -1], [2, 13, 8, -1],
]
WEIGHTS = [[0, 3, 22, 60], [0, 6, 22, 22, 3], [0, 0, -13, -13, 6]]
NEW_W_WEIGHTS = [
    4, 2, 2, 4, 4, 3, 2, 4, 4, 3, 0, 3, 4, 4, 4, 4, 0, 4, 4,
    4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 0, 0, 4, 4, 0, 4,
    0, 3, 1, 4, 1, 2, 3, 2, 2, 3, 2, 2, 4, 1, 2, 1, 4, 4,
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


V = load_module("mixed_leg_exact_helpers", PRIOR / "verify_split.py")
G = load_module("mixed_leg_weighted_helpers", GRID / "verify.py")


def check_source_pins():
    for path, expected in PINS.items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == expected,
                "A pinned external seed, physical basis, or weighted source changed")


def flatten(matrix):
    return [x for row in matrix for x in row]


def direction(matrix):
    values = flatten(matrix)
    pivot = next((x for x in values if x), None)
    require(pivot is not None, "A projective factor is zero")
    return tuple(Fraction(x) / pivot for x in values)


def mixed_seed(original, replacements=REPLACEMENTS):
    """Each change reads the original factors, even at another changed index.

    A source term may change on only one leg. Destinations may change on a
    different leg: the U destinations 12 and 13 remain valid after W changes.
    """
    surviving = [[[[x for x in row] for row in factor] for factor in term]
                 for term in original]
    discarded, changed = [], set()
    for record in replacements:
        require(isinstance(record, (list, tuple)) and len(record) == 4,
                "A replacement needs leg, source, destination, and scalar")
        leg, i, j, scalar = record
        require(all(type(x) is int for x in record) and leg in (0, 2)
                and 0 <= i < 76 and 0 <= j < 76 and i != j and scalar in (-1, 1),
                "Invalid mixed replacement")
        require(i not in changed, "Repeated changed source term")
        changed.add(i)
        replacement = [[scalar * x for x in row] for row in original[j][leg]]
        difference = [[x - y for x, y in zip(row, other)]
                      for row, other in zip(original[i][leg], replacement)]
        require(any(flatten(difference)), "A discarded difference is zero")
        error = [factor for factor in original[i]]
        error[leg] = difference
        discarded.append(error)
        surviving[i][leg] = replacement
    return surviving, discarded


def collect_coefficients(terms):
    """Independent contraction of every coordinate and Laurent degree."""
    output = {}
    for u, v, w in terms:
        for a, x, e in u:
            for b, y, f in v:
                for c, z, g in w:
                    key = e + f + g, a, b, c
                    output[key] = output.get(key, Fraction(0)) + x * y * z
    return {key: value for key, value in output.items() if value}


def coefficient_replay(certificate):
    surviving = V.parse_factors(certificate["surviving_factors"], 76)
    discarded = V.parse_factors(certificate["discarded_factors"], 13)
    minima = [[min(e for _, _, e in factor) for factor in term] for term in discarded]
    require(all(sum(row) > 0 for row in minima),
            "A discarded rank-one tensor has nonpositive valuation")
    output = collect_coefficients(surviving)
    error = collect_coefficients(discarded)
    require(not any(key[0] < 0 for key in output),
            "The surviving tensor has a negative Laurent degree")
    for a in range(20):
        i, j = divmod(a, 5)
        for b in range(25):
            other_j, k = divmod(b, 5)
            for c in range(20):
                other_k, other_i = divmod(c, 4)
                expected = int((i, j, k) == (other_i, other_j, other_k))
                require(output.get((0, a, b, c), Fraction(0)) == expected,
                        "A constant matrix multiplication coefficient differs")
    require(all(key[0] > 0 for key in error), "The full discarded tensor does not vanish")
    require({key: value for key, value in output.items() if key[0] > 0}
            == {key: -value for key, value in error.items()},
            "The full positive remainder differs from the discarded tensor")
    degrees = {str(degree): count for degree, count in
               sorted(Counter(key[0] for key in output).items())}
    return minima, degrees


def old_screen_values(original, surviving):
    original_u = [direction(term[0]) for term in original]
    original_w, _ = G.load_w_vectors()
    sets = [set(direction(term[leg]) for term in surviving) for leg in range(3)]
    require(len(set(original_u)) == 76 and sets[0] <= set(original_u)
            and sets[2] <= set(original_w), "Surviving directions left the original configuration")
    retained_u = sum(weight for row, weight in zip(original_u, G.WEIGHTS) if row in sets[0])
    retained_w = sum(weight for row, weight in zip(original_w, G.W_WEIGHTS) if row in sets[2])
    return {
        "direction_counts_U_V_W": [len(rows) for rows in sets],
        "deleted_original_weights": {"U": sum(G.WEIGHTS) - retained_u,
                                      "W": sum(G.W_WEIGHTS) - retained_w},
        "retained_original_weights": {"U": retained_u, "W": retained_w},
        "previous_nine_group_capacities": {"U": 216, "W": 144},
        "both_previous_weight_inequalities_pass": retained_u <= 216 and retained_w <= 144,
    }


def build_certificate():
    check_source_pins()
    basis_source = json.loads((PRIOR / "five_split_certificate.json").read_text())
    bases = [[[Fraction(x) for x in row] for row in matrix]
             for matrix in basis_source["basis_matrices"]]
    require([V.determinant(matrix) for matrix in bases] == [1, 1, -1],
            "The retained physical bases are not the specified unimodular matrices")
    original = V.load_seed()
    surviving, discarded = mixed_seed(original)
    certificate = {
        "schema": SCHEMA, "claim_id": CLAIM, "scope": SCOPE, "source_pins": PINS,
        "dimensions": [4, 5, 5], "surviving_terms": 76,
        "replacement_format": ["leg", "source", "destination", "scalar"],
        "replacements": REPLACEMENTS,
        "basis_matrices": basis_source["basis_matrices"], "weights": WEIGHTS,
        "surviving_factors": V.transformed_factors(surviving, bases, WEIGHTS),
        "discarded_factors": V.transformed_factors(discarded, bases, WEIGHTS),
    }
    minima, degrees = coefficient_replay(certificate)
    certificate.update({
        "minimum_factor_valuations": minima,
        "discarded_tensor_valuations": [sum(row) for row in minima],
        "ramification": 3,
        "factor_gauge_exponents": [[1 - 3*a, 1 - 3*b, 3*a + 3*b - 2]
                                   for a, b, c in minima],
        "nonzero_coefficients_by_degree": degrees,
        "old_weight_screens": old_screen_values(original, surviving),
    })
    return certificate


def verify_split(certificate):
    require(isinstance(certificate, dict), "The mixed-split certificate must be an object")
    for key, expected in (("schema", SCHEMA), ("claim_id", CLAIM), ("scope", SCOPE),
                          ("source_pins", PINS), ("replacements", REPLACEMENTS),
                          ("dimensions", [4, 5, 5]), ("surviving_terms", 76)):
        require(certificate.get(key) == expected, "Mixed-split schema, scope, source, or construction differs")
    weights = certificate.get("weights")
    require(isinstance(weights, list) and len(weights) == 3
            and all(isinstance(row, list) and len(row) == size
                    and all(type(x) is int for x in row)
                    for row, size in zip(weights, (4, 5, 5))), "Invalid physical weights")
    require(weights == WEIGHTS, "The registered physical weights differ")
    minima, degrees = coefficient_replay(certificate)
    gauges = certificate.get("factor_gauge_exponents")
    require(certificate.get("ramification") == 3 and isinstance(gauges, list)
            and len(gauges) == 13, "Invalid ramification or factor-gauge count")
    for row, gauge in zip(minima, gauges):
        require(isinstance(gauge, list) and len(gauge) == 3
                and all(type(x) is int for x in gauge) and sum(gauge) == 0,
                "A factor gauge does not preserve its tensor term")
        require(all(3*x + y > 0 for x, y in zip(row, gauge)),
                "A ramified gauged factor has nonpositive valuation")
    regenerated = build_certificate()
    require(json.dumps(certificate, sort_keys=True) == json.dumps(regenerated, sort_keys=True),
            "The saved mixed split differs from the exact reconstructed witness")
    return {
        "expanded_exact_terms": 89, "surviving_border_terms": 76,
        "U_replacements": 11, "W_replacements": 2, "discarded_terms": 13,
        "discarded_tensor_valuations": [sum(row) for row in minima],
        "all_constant_positions_checked": 10000, "constant_nonzero_coefficients": degrees["0"],
        "nonzero_coefficients_at_negative_degrees": 0,
        "nonzero_coefficients_at_positive_degrees": sum(n for degree, n in degrees.items() if degree != "0"),
        "old_weight_screens": regenerated["old_weight_screens"],
    }


def w_configuration(surviving):
    classes = {}
    for i, term in enumerate(surviving):
        row = direction(term[2])
        require(all(x.denominator == 1 for x in row), "A canonical W direction is not integral")
        row = tuple(int(x) for x in row)
        require(all(x in (-1, 0, 1) for x in row), "Unexpected canonical W coefficient")
        classes.setdefault(row, []).append(i)
    vectors = [list(row) for row in classes]
    require(len(vectors) == 56 and G.rank(vectors, 101) == 20,
            "The current W configuration has the wrong size or finite-field span")
    require(all(G.rank([u, v], 101) == 2 for u, v in combinations(vectors, 2)),
            "Distinct W directions collide modulo 101")
    return vectors, list(classes.values())


def check_w_report(report, vectors, weights):
    require((report.get("prime"), report.get("vectors"), report.get("dimension")) == (101, 56, 20),
            "Unexpected W enumeration parameters")
    require(report.get("four_subsets") == comb(56, 4)
            and report.get("independent_four_subsets") == 366288,
            "The W enumeration does not have the registered complete coverage")
    size_hist = {int(k): v for k, v in report["basis_weighted_histogram"].items()}
    weight_hist = {int(k): v for k, v in report["flat_weight_histogram"].items()}
    require(all(type(n) is int and n > 0 for n in [*size_hist.values(), *weight_hist.values()])
            and min(size_hist) >= 4 and max(size_hist) == 7
            and min(weight_hist) >= 0 and max(weight_hist) == 16
            and sum(size_hist.values()) == sum(weight_hist.values()) == 366288,
            "The W enumeration histograms disagree")
    pairs = report["size_exceptional_histogram"]
    marginal, seen = Counter(), set()
    for size, exceptional, count in pairs:
        require(all(type(x) is int for x in (size, exceptional, count))
                and 4 <= size <= 7 and 0 <= exceptional <= size and count > 0
                and (size, exceptional) not in seen, "Invalid W size/weight-four histogram")
        seen.add((size, exceptional))
        marginal[size] += count
    require(dict(marginal) == size_hist, "The W histogram marginals differ")
    require(report["maximum_flat_weight"] == 16 and report["maximum_flat_cardinality"] == 7,
            "The registered W flat cap differs")
    for prefix, weighted in (("", False), ("weighted_", True)):
        indices = report[prefix + "witness_basis"]
        require(len(indices) == 4 and len(set(indices)) == 4
                and all(type(i) is int and 0 <= i < 56 for i in indices), "Invalid W witness basis")
        basis = [vectors[i] for i in indices]
        require(G.rank(basis, 101) == G.rank(basis) == 4, "A W witness basis has the wrong rank")
        members = [i for i, row in enumerate(vectors) if G.rank(basis + [row], 101) == 4]
        require(members == report[prefix + "witness_members"]
                and G.rank([vectors[i] for i in members]) == 4, "A W witness flat differs")
        require(sum(weights[i] for i in members) == 16 if weighted else len(members) == 7,
                "A W extremal witness does not attain its recorded cap")


def verify_w_obstruction(obstruction, full=False):
    require(isinstance(obstruction, dict), "The W obstruction must be an object")
    for key, expected in (("schema", W_SCHEMA), ("claim_id", CLAIM), ("scope", W_SCOPE),
                          ("source_pins", PINS), ("W_replacements", [[12, 8, -1], [13, 8, -1]]),
                          ("class_order", "first occurrence in surviving term order; first nonzero coordinate one"),
                          ("total_weight", 152), ("maximum_rank4_flat_weight", 16),
                          ("rank4_cover_group_lower_bound", 10), ("direction_rank_mod101", 20)):
        require(obstruction.get(key) == expected, "W obstruction schema, scope, source, or bound differs")
    check_source_pins()
    surviving, _ = mixed_seed(V.load_seed())
    vectors, classes = w_configuration(surviving)
    require(obstruction.get("vectors") == vectors and obstruction.get("classes") == classes,
            "The W obstruction does not describe the displayed mixed seed")
    weights = obstruction.get("weights")
    require(isinstance(weights, list) and len(weights) == 56
            and all(type(x) is int and 0 <= x <= 4 for x in weights)
            and weights == NEW_W_WEIGHTS and sum(weights) == 152, "The W weights differ")
    check_w_report(obstruction["enumeration"], vectors, weights)
    if full:
        actual = G.enumerate_flats(vectors, weights)
        check_w_report(actual, vectors, weights)
        require(actual == obstruction["enumeration"], "The complete W enumeration differs from its stored result")
    return {
        "distinct_W_directions": 56, "total_weight": sum(weights),
        "rank_at_most_four_weight_cap": 16, "nine_group_capacity": 144,
        "minimum_rank_at_most_four_groups_by_weight": 10,
        "static_nine_group_cover_excluded": True,
        "stored_four_subsets": comb(56, 4), "stored_independent_four_subsets": 366288,
        "exhaustive_enumeration_rerun_by_this_command": full,
        "arbitrary_subsequent_flips_excluded": False,
        "singular_limits_excluded": False, "general_Q64_maps_excluded": False,
    }


def verify(certificate, obstruction, full=False):
    split = verify_split(certificate)
    flat = verify_w_obstruction(obstruction, full)
    return {
        "claim_id": CLAIM, "mixed_border_seed": split, "static_W_obstruction": flat,
        "proof_status": "written-unreviewed", "rank_record_claimed": False,
        "search_optimum_claimed": False, "Q64_maps_constructed": False, "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--enumerate", action="store_true", help="Repeat every W four-subset using a C99 compiler.")
    args = parser.parse_args()
    witness = json.loads((PACKAGE / "certificate.json").read_text())
    obstruction = json.loads((PACKAGE / "w_obstruction.json").read_text())
    print(json.dumps(verify(witness, obstruction, args.enumerate), indent=2))
