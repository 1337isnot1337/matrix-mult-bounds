"""Exact acceptance for sharp A4 source caps below ranks 100,104,108,112.

Literal-source, coherent-minor and mask arithmetic is copied with credit
from the frozen rank92/rank96 verifier; its bytes are pinned in sources.json.
The written high-threshold cases, staircase witnesses and target application
are new. Acceptance imports neither discovery nor a source constructor.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/high-rank-source-caps-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
OLD_CERTIFICATES = ROOT / "results/torus-rank80-2026-10-23/certificates.json"
SOURCE = tuple(product(range(4), range(7), range(4)))
SHORT = tuple(product(range(4), repeat=2))
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
DISJOINT_PAIRS = ((0, 4), (1, 5), (2, 6))
THRESHOLDS = (100, 104, 108, 112)
DIMENSIONS = (84, 88, 92, 96)
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
    "research/ai/2026-10-23-torus-rank80/proof.md",
    "results/torus-rank80-2026-10-23/certificates.json",
    "research/ai/2026-10-23-source-staircase-spaces/proof.md",
    "research/ai/2026-10-23-rank92-rank96-spaces/proof.md",
    "research/ai/2026-10-23-rank92-rank96-spaces/verify.py",
    "research/ai/2026-10-23-rank92-rank96-spaces/discover.py",
    "research/ai/2026-10-23-leading-rank202/proof.md",
    "research/ai/2026-10-23-all-pair-rank136/proof.md",
)
HEADER = {"schema": "high-rank-source-caps-v1",
          "coefficient_domain": "integers 0 and 1", "verification_modulus": 2}
COHERENT_FAMILIES = ("coherent20_pair", "coherent9_ideals", "coherent13_ideals")
MINOR_FIELDS = {"coefficient_mask", "minor_rows_mask", "minor_columns_mask"}
CLAIM_SCOPE = {
    "field": "C", "strict_source_thresholds": list(THRESHOLDS),
    "sharp_maximum_dimensions": list(DIMENSIONS),
    "arbitrary_complex_linear_spaces": True,
    "order_ideal_reduction_characteristic_zero": True,
    "all_extremizers_classified": False,
    "attained_source_ranks": [96, 100, 104, 108],
    "target_statement_uses_complete_Laurent_presentations": True,
    "individual_scalar_balancing": True,
    "arbitrary_leading_kernels_and_higher_coefficients": True,
    "arbitrary_finite_poles_on_unselected_map": True,
    "retains_full_short_long28_prerequisite": True,
    "short_rank100_long_rank_upper": 20,
    "short_rank100_allowed_positive_long_ranks": list(range(1, 13)) + [20],
    "target_conditions_are_necessary_only": True,
    "screen_maximizer_is_target_construction": False,
    "target_bound_sharp": False, "target_constructed": False,
    "improves_omega": False, "independent_external_review": False,
    "formalized": False,
}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    require(document["base_commit"] == "658e2d54fa7b506f7d8fd51eeec7788f23a00e91"
            and document["field"] == "C", "changed prerequisite version or field")
    entries = document["local_dependencies"]
    require(len(entries) == len(SOURCE_PATHS)
            and {entry["path"] for entry in entries} == set(SOURCE_PATHS),
            "changed source inventory")
    result = {}
    for entry in entries:
        path = ROOT / entry["path"]
        require(path.is_file(), "missing source prerequisite")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == entry["sha256"], "source digest mismatch")
        result[entry["path"]] = digest
    return dict(sorted(result.items()))


def literal_bases():
    """Use the original six short indices, not discovery's entry formula."""
    coherent = {coordinate: set() for coordinate in SHORT}
    source = {coordinate: set() for coordinate in SOURCE}
    positions = set()
    for i, j, p, q, r, s in product(range(4), repeat=6):
        position = ((4*j+p)*7+r+s, (4*(i+j)+q)*4+r)
        require(position not in positions, "overlapping coefficient labels")
        positions.add(position)
        source[i, p+q, s].add(position)
    for i, j, r, s in product(range(4), repeat=4):
        coherent[i, s].add((7*j+r+s, 4*(i+j)+r))
    require(len(positions) == 4096 and sum(map(len, coherent.values())) == 256,
            "literal source term count changed")
    return coherent, source


def source_controls(coherent, source):
    for coordinate in SHORT:
        positions = coherent[coordinate]
        require(len(positions) == len({row for row, column in positions})
                == len({column for row, column in positions}) == 16,
                "coherent monomial rank changed")
    for i, k, s in SOURCE:
        expected = set()
        for p, q in product(range(4), repeat=2):
            if p+q == k:
                for row, column in coherent[i, s]:
                    j, ell = divmod(row, 7)
                    h, r = divmod(column, 4)
                    expected.add(((4*j+p)*7+ell, (4*h+q)*4+r))
        require(source[i, k, s] == expected, "source tensor factorization mismatch")
        require(len(expected) == len({row for row, column in expected})
                == len({column for row, column in expected}) == 16*MULTIPLICITIES[k],
                "source monomial rank changed")
    layers = {k: set().union(*(source[i, k, s] for i, s in SHORT)) for k in range(7)}
    for a, b in DISJOINT_PAIRS:
        require({row for row, column in layers[a]}.isdisjoint({row for row, column in layers[b]})
                and {column for row, column in layers[a]}.isdisjoint(
                    {column for row, column in layers[b]}), "middle blocks are not disjoint")
    return {"literal_source_terms": 4096, "literal_coherent_terms": 256,
            "coherent_monomial_ranks_checked": 16, "source_factorizations_checked": 112,
            "middle_multiplicities": list(MULTIPLICITIES),
            "disjoint_middle_pairs": [list(pair) for pair in DISJOINT_PAIRS]}


def short_ideals(volume):
    return {shape for shape in product(range(5), repeat=4)
            if sum(shape) == volume and all(shape[i] >= shape[i+1] for i in range(3))}


def parse_mask(value, width):
    require(type(value) is str, "mask must be a hexadecimal string")
    try:
        mask = int(value, 16)
    except ValueError as error:
        raise ArithmeticError("invalid hexadecimal mask") from error
    require(0 <= mask < (1 << width) and value == hex(mask), "noncanonical or out-of-range mask")
    return mask


def indices(mask, width):
    return [index for index in range(width) if (mask >> index) & 1]


def invertible_mod2(matrix, size):
    require(len(matrix) == size and all(type(row) is int and 0 <= row < (1 << size)
                                       for row in matrix), "invalid binary square matrix")
    rows = list(matrix)
    for column in range(size):
        pivot = next((row for row in range(column, size) if (rows[row] >> column) & 1), None)
        if pivot is None:
            return False
        rows[column], rows[pivot] = rows[pivot], rows[column]
        for row in range(column+1, size):
            if (rows[row] >> column) & 1:
                rows[row] ^= rows[column]
    return True


def replay_minor(record, basis, coordinates, matrix_size, rank, allowed):
    require(set(record) in (MINOR_FIELDS, MINOR_FIELDS | {"shape"}), "changed minor fields")
    selected = [coordinates[n] for n in indices(
        parse_mask(record["coefficient_mask"], len(coordinates)), len(coordinates))]
    require(selected and set(selected) <= allowed, "coefficient support leaves its source space")
    rows = indices(parse_mask(record["minor_rows_mask"], matrix_size), matrix_size)
    columns = indices(parse_mask(record["minor_columns_mask"], matrix_size), matrix_size)
    require(len(rows) == len(columns) == rank, "minor has the wrong dimensions")
    full_rows = [0]*matrix_size
    for coordinate in selected:
        for row, column in basis[coordinate]:
            full_rows[row] ^= 1 << column
    minor = [sum(((full_rows[row] >> column) & 1) << index
                 for index, column in enumerate(columns)) for row in rows]
    require(invertible_mod2(minor, rank), "saved integer minor is singular modulo two")


def coherent_controls(document, coherent):
    old = json.loads(OLD_CERTIFICATES.read_text())
    require(all(document[family] == old[family] for family in COHERENT_FAMILIES),
            "credited coherent certificates were changed")
    require(document["coherent20_pair"]["coefficient_mask"] == "0x12", "rank20 pair changed")
    replay_minor(document["coherent20_pair"], coherent, SHORT, 28, 20, {(0, 1), (1, 0)})
    for volume, rank, count in ((9, 24, 7), (13, 28, 3)):
        expected = short_ideals(volume)
        require(len(expected) == count, "short ideal census changed")
        seen = set()
        for record in document[f"coherent{volume}_ideals"]:
            shape = tuple(record["shape"])
            require(shape in expected and shape not in seen, "invalid or repeated coherent ideal")
            seen.add(shape)
            allowed = {(i, s) for i, s in SHORT if s < shape[i]}
            replay_minor(record, coherent, SHORT, 28, rank, allowed)
        require(seen == expected, "incomplete coherent ideal inventory")
    five = short_ideals(5)
    require(five and all(shape[0] >= 2 and shape[1] >= 1 for shape in five),
            "a size5 ideal misses the rank20 pair")
    return {"credited_integer_minors_replayed": 11,
            "size9_ideals": 7, "size13_ideals": 3,
            "all_size5_ideals_contain_the_rank20_pair": True,
            "rank_lower_by_nonzero_layer_size": {"1..4": 16, "5..8": 20,
                                                 "9..12": 24, "13..16": 28}}


def coherent_rank_lower(size):
    require(type(size) is int and 0 <= size <= 16, "invalid short-layer size")
    return 0 if size == 0 else 16+4*((size-1)//4)


def layer_profiles():
    """Directly enumerate every nonincreasing seven-tuple; no discovery input."""
    chosen = []

    def visit(upper):
        if len(chosen) == 7:
            yield tuple(chosen)
            return
        for value in range(upper+1):
            chosen.append(value)
            yield from visit(value)
            chosen.pop()

    yield from visit(16)


def necessary_rank_lower(profile):
    require(len(profile) == 7 and all(type(n) is int and 0 <= n <= 16 for n in profile)
            and all(profile[i] >= profile[i+1] for i in range(6)), "invalid layer profile")
    ranks = tuple(map(coherent_rank_lower, profile))
    return max([MULTIPLICITIES[k]*ranks[k] for k in range(7)] +
               [ranks[0]+3*ranks[4], 2*ranks[1]+2*ranks[5], 3*ranks[2]+ranks[6]])


def dominating_profile(profile, threshold):
    require(threshold in THRESHOLDS, "unsupported theorem threshold")
    if threshold == 100:
        if profile[0] <= 12:
            return "n0<=12", (12, 12, 12, 12, 12, 12, 12)
        if profile[2] >= 13:
            return "n0>=13,n2>=13", (16, 16, 16, 12, 8, 8, 0)
        return "n0>=13,n2<=12", (16, 16, 12, 12, 8, 8, 8)
    if threshold == 104:
        if profile[1] <= 12:
            return "n1<=12", (16, 12, 12, 12, 12, 12, 12)
        if profile[2] >= 13:
            return "n1>=13,n2>=13", (16, 16, 16, 12, 12, 8, 4)
        return "n1>=13,n2<=12", (16, 16, 12, 12, 12, 8, 8)
    if threshold == 108:
        if profile[2] <= 12:
            return "n2<=12", (16, 16, 12, 12, 12, 12, 12)
        return "n2>=13", (16, 16, 16, 12, 12, 12, 8)
    return "n3<=12", (16, 16, 16, 12, 12, 12, 12)


@lru_cache(maxsize=1)
def profile_controls():
    histograms = {threshold: Counter() for threshold in THRESHOLDS}
    cases = {threshold: Counter() for threshold in THRESHOLDS}
    maximizing = {threshold: [] for threshold in THRESHOLDS}
    count = 0
    for profile in layer_profiles():
        count += 1
        peak = necessary_rank_lower(profile)
        for threshold, cap in zip(THRESHOLDS, DIMENSIONS):
            if peak >= threshold:
                continue
            case, bound = dominating_profile(profile, threshold)
            require(all(n <= b for n, b in zip(profile, bound)) and sum(bound) <= cap,
                    "written case split failed on an admissible profile")
            volume = sum(profile)
            histograms[threshold][volume] += 1
            cases[threshold][case] += 1
            if volume == cap:
                maximizing[threshold].append(list(profile))
    require(count == 245157, "complete layer profile inventory changed")
    result = {}
    for threshold, cap, population, extrema in zip(
            THRESHOLDS, DIMENSIONS, (172062, 210614, 222224, 222924), (1, 1, 2, 1)):
        histogram = histograms[threshold]
        require((sum(histogram.values()), max(histogram), histogram[cap]) == (population, cap, extrema),
                "profile maximum or population changed")
        result[str(threshold)] = {
            "admissible_profiles": population, "maximum_volume": cap,
            "profiles_at_maximum": extrema, "maximizing_profiles": sorted(maximizing[threshold]),
            "written_case_counts": dict(sorted(cases[threshold].items())),
            "volume_histogram": {str(v): histogram[v] for v in sorted(histogram)},
        }
    return {"all_nonincreasing_layer_size_profiles": count,
            "constraints": "strict pure-layer and three disjoint-middle-pair rank lower bounds",
            "thresholds": result, "enumeration_uses_discovery": False,
            "upper_proof_is_written_case_split": True}


def family_coordinates(m):
    require(type(m) is int and m in range(4), "sharp family is scoped to m=0,1,2,3")
    return {(i, k, s) for i, k, s in SOURCE if i < 3 or (i == 3 and k < m)}


def check_column_support(allowed, columns, source):
    actual = {column for coordinate in allowed for row, column in source[coordinate]}
    require(actual == columns, "column support does not equal the literal joint support")
    return sum(len(source[coordinate]) for coordinate in allowed)


def sharpness_controls(records, source):
    require(isinstance(records, list) and len(records) == 4
            and [record.get("m") for record in records] == list(range(4)),
            "incomplete or reordered sharp space inventory")
    output = []
    for m, record in enumerate(records):
        require(set(record) == {"d", "m", "dimension", "rank_upper", "column_support_mask"}
                | MINOR_FIELDS, "changed sharp space fields")
        require(type(record["d"]) is int and record["d"] == 3, "changed staircase strip")
        allowed = family_coordinates(m)
        dimension, rank = 84+4*m, 96+4*m
        require(type(record["dimension"]) is int and record["dimension"] == dimension == len(allowed)
                and type(record["rank_upper"]) is int and record["rank_upper"] == rank,
                "changed sharp dimension or rank budget")
        columns = set(indices(parse_mask(record["column_support_mask"], 112), 112))
        expected = {(4*h+q)*4+r for h, q, r in product(range(7), range(4), range(4))
                    if h <= 5 or (h == 6 and q < m)}
        require(columns == expected and len(columns) == rank, "changed staircase column formula")
        terms = check_column_support(allowed, columns, source)
        replay_minor({key: record[key] for key in MINOR_FIELDS}, source, SOURCE, 112, rank, allowed)
        output.append({"d": 3, "m": m, "dimension": dimension,
                       "literal_terms_covered": terms, "supported_columns": rank,
                       "uniform_rank_upper": rank, "attained_rank": rank,
                       "strict_threshold": rank+4})
    return {"sharp_spaces": output, "integer_sharpness_minors_replayed": 4,
            "field_transfer": "Column support bounds hold over every field; odd integer minors are nonzero over C.",
            "weak_threshold_counterexamples": [
                {"rank_ceiling": 100, "dimension": 88, "exceeded_cap": 84, "space": "V1"},
                {"rank_ceiling": 104, "dimension": 92, "exceeded_cap": 88, "space": "V2"},
                {"rank_ceiling": 108, "dimension": 96, "exceeded_cap": 92, "space": "V3"},
                {"rank_ceiling": 112, "dimension": 112, "exceeded_cap": 96, "space": "full source"},
            ],
            "boundary_m4": {"dimension": 100, "supported_columns": 112,
                            "strict_rank112_hypothesis_proved_by_support": False,
                            "attained_rank_asserted": False}}


def source_dimension_cap(rank_ceiling):
    require(type(rank_ceiling) is int and 0 <= rank_ceiling <= 224, "invalid source rank ceiling")
    for threshold, cap in zip(THRESHOLDS, DIMENSIONS):
        if rank_ceiling < threshold:
            return cap
    return 112


def full_short_screen(long_rank, use_prior=True):
    require(type(long_rank) is int and 0 <= long_rank <= 101,
            "long rank lies outside the established individual bound")
    require(type(use_prior) is bool, "invalid prerequisite switch")
    ceiling = 124-long_rank
    lower = 110-10*(long_rank//10)
    upper = source_dimension_cap(ceiling)
    prior = use_prior and long_rank > 28
    return {"long_rank": long_rank, "source_rank_ceiling": ceiling,
            "kernel_lower": lower, "new_kernel_upper": upper,
            "excluded_by_prior28": prior, "new_kernel_contradiction": lower > upper,
            "excluded": prior or lower > upper}


def target_controls():
    records = [full_short_screen(r) for r in range(102)]
    retained = [record["long_rank"] for record in records if not record["excluded"]]
    require(retained == list(range(13)) + [20], "full-short survivor set changed")
    new = [record["long_rank"] for record in records
           if record["excluded"] and not record["excluded_by_prior28"]]
    require(new == list(range(13, 20)) + list(range(21, 29)), "selective full-short exclusions changed")
    require(not full_short_screen(101, use_prior=False)["excluded"]
            and full_short_screen(101)["excluded"], "retained full-short prerequisite was lost")
    maxima, maximum = [], -1
    prior_count = retained_count = 0
    for b in range(102):
        for c in range(102):
            if b > 28 or c > 28:
                continue
            prior_count += 1
            if b not in retained or c not in retained:
                continue
            # The long-pair sum is at most40. Its source ceiling is at least184,
            # so none of the new strict source thresholds constrains this pair.
            require(b+c <= 40 and 224-b-c >= 112, "full-short long-pair boundary changed")
            retained_count += 1
            total = 100+b+c
            if total > maximum:
                maximum, maxima = total, [[100, b, c]]
            elif total == maximum:
                maxima.append([100, b, c])
    require((prior_count, retained_count, maximum, maxima) == (841, 196, 140, [[100, 20, 20]]),
            "full-short pair census or arithmetic maximum changed")
    return {"one_leg_cases_checked": len(records), "one_leg_records": records,
            "retained_long_ranks": retained, "newly_excluded_long_ranks": new,
            "two_long_cases_checked": 102*102, "prior_surviving_triples": prior_count,
            "retained_triples": retained_count, "newly_excluded_triples": prior_count-retained_count,
            "screen_maximum_total": maximum, "screen_maximizers": maxima,
            "zero_rank_is_only_a_census_enlargement": True,
            "screen_maximizer_is_target_construction": False}


def controls(document=None):
    pins = check_sources()
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | set(COHERENT_FAMILIES) | {"sharp_spaces"},
            "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    coherent, source = literal_bases()
    return {
        "schema": "high-rank-source-controls-v1", "source_pins": pins,
        "certificate_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
        "source_controls": source_controls(coherent, source),
        "coherent_controls": coherent_controls(document, coherent),
        "profile_controls": profile_controls(),
        "sharpness_controls": sharpness_controls(document["sharp_spaces"], source),
        "strict_threshold_controls": {str(r): source_dimension_cap(r)
                                      for r in (99, 100, 103, 104, 107, 108, 111, 112)},
        "target_controls": target_controls(), "claim_scope": CLAIM_SCOPE.copy(),
    }


def replay_saved(document):
    require(document.get("claim_scope") == CLAIM_SCOPE, "saved scope differs from the theorem")
    require(document == controls(), "saved evidence differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = controls()
    if args.write_report:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report, indent=2) + "\n")
    else:
        require(json.loads(RESULT.read_text()) == report, "saved evidence or scope differs from exact replay")
    print(json.dumps({"source_caps": dict(zip(THRESHOLDS, DIMENSIONS)),
                      "admissible_profiles": {r: data["admissible_profiles"] for r, data in
                                               report["profile_controls"]["thresholds"].items()},
                      "sharpness": report["sharpness_controls"],
                      "retained_full_short_long_ranks": report["target_controls"]["retained_long_ranks"]}, indent=2))


if __name__ == "__main__":
    main()
