"""Exact auxiliary corner and conditional scalar-defect repair in A(8,8).

The maintained verifier uses only integer arithmetic and the standard library.
It enumerates the complete original source for tensor and mixed-response checks.
It does not assume that the reduced source has the desired matrix restriction.
"""

import argparse
from collections import Counter, defaultdict
from itertools import combinations, product
import json
from pathlib import Path


DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[2]
RESULTS = ROOT / "results/anisotropic-constructions-2026-10-20"
CERTIFICATE = RESULTS / "spin-scalar-corner-certificate.json"
REPORT = RESULTS / "spin-scalar-corner-report.json"
LABELS = tuple(product((5, 6, 7), (6, 7), (6, 7)))
SELECTED = (0, 1, 3, 4, 5, 6, 7, 8, 11)


def coordinate(i, k, s):
    if not (0 <= i < 8 and 0 <= k < 15 and 0 <= s < 8):
        raise ValueError("Source coordinate outside A(8,8)")
    return (15 * i + k) * 8 + s


def decode(column):
    i, tail = divmod(column, 120)
    k, s = divmod(tail, 8)
    return [i, k, s]


def source():
    for i, p, q, r, j, s in product(range(8), repeat=6):
        yield (coordinate(i, p + q, s), coordinate(p, r + s, j),
               coordinate(r, i + j, q))


def corner_maps(selected=SELECTED):
    labels = [LABELS[index] for index in selected]
    return [
        [{coordinate(7, 12, 7): 1}],
        [{coordinate(p, 7 + r, j): 1} for p, r, j in labels],
        [{coordinate(r, 7 + j, 12 - p): 1} for p, r, j in labels],
    ]


def serialize(maps):
    return [[[list(entry) for entry in sorted(row.items())] for row in leg]
            for leg in maps]


def parse(data):
    if not isinstance(data, list) or len(data) != 3:
        raise ArithmeticError("Three integer maps are required")
    maps = []
    for data_leg, width in zip(data, (1, 9, 9)):
        if not isinstance(data_leg, list) or len(data_leg) != width:
            raise ArithmeticError("Incorrect auxiliary target dimensions")
        leg = []
        for data_row in data_leg:
            if not isinstance(data_row, list):
                raise ArithmeticError("A sparse row must be a list")
            row = {}
            for entry in data_row:
                if (not isinstance(entry, list) or len(entry) != 2
                        or any(type(x) is not int for x in entry)):
                    raise ArithmeticError("Sparse entries must be integer pairs")
                column, value = entry
                if not (0 <= column < 960) or not value or column in row:
                    raise ArithmeticError("Invalid or repeated sparse coordinate")
                row[column] = value
            leg.append(row)
        maps.append(leg)
    return maps


def inverse(matrix):
    result = defaultdict(list)
    for row, coefficients in enumerate(matrix):
        for column, value in coefficients.items():
            result[column].append((row, value))
    return result


def clean(counter):
    return {key: value for key, value in counter.items() if value}


def contraction(maps):
    inverses = [inverse(matrix) for matrix in maps]
    coefficients = Counter()
    source_terms = 0
    for point in source():
        source_terms += 1
        for a, b, c in product(*(inverses[leg].get(point[leg], ())
                                for leg in range(3))):
            coefficients[(a[0], b[0], c[0])] += a[1] * b[1] * c[1]
    return clean(coefficients), source_terms


def check_module(maps):
    coefficients, terms = contraction(maps)
    channels = len(maps[1])
    target = {(0, channel, channel): 1 for channel in range(channels)}
    if len(maps[0]) != 1 or len(maps[2]) != channels or coefficients != target:
        raise ArithmeticError("An auxiliary matrix-tensor coefficient fails")
    return {"source_terms_checked": terms,
            "all_target_coefficients_checked": channels * channels,
            "nonzero_target_coefficients": channels}


def responses(maps):
    inverses = [inverse(matrix) for matrix in maps]
    result = [defaultdict(Counter) for _ in range(3)]
    for point in source():
        for free in range(3):
            fixed = [leg for leg in range(3) if leg != free]
            for first, second in product(*(inverses[leg].get(point[leg], ())
                                           for leg in fixed)):
                result[free][point[free]][(first[0], second[0])] += first[1] * second[1]
    return [{column: clean(row) for column, row in leg.items() if clean(row)}
            for leg in result]


def unit_disjoint_rank(response):
    """Disjoint nonzero column supports and unit entries give an identity minor."""
    occupied = set()
    pivots = []
    for column, row in sorted(response.items()):
        if not row or any(value != 1 for value in row.values()):
            raise ArithmeticError("A response column lacks the required unit entries")
        if occupied.intersection(row):
            raise ArithmeticError("The response column supports are not disjoint")
        occupied.update(row)
        pivots.append({"source_coordinate": decode(column),
                       "output_pair": list(min(row))})
    return {"rank": len(response), "nonzero_source_coordinates":
            [decode(column) for column in sorted(response)],
            "identity_minor_pivots": pivots,
            "disjoint_nonzero_column_supports_checked": True}


def core_ambient_spaces():
    return (
        {coordinate(i, k, s) for i, k, s in product(range(8), range(3), range(8))},
        {coordinate(p, ell, j) for p, ell, j in product(range(2), range(15), range(6))},
        {coordinate(r, h, q) for r, h, q in product(range(6), range(15), range(2))},
    )


def mixed_responses(maps):
    """Keep the free original coordinate and every core ambient basis row."""
    ambient = core_ambient_spaces()
    inverses = [inverse(matrix) for matrix in maps]
    cases = [(free, core, 3 - free - core)
             for free in range(3) for core in range(3) if core != free]
    outputs = [Counter() for _ in cases]
    source_terms = 0
    for point in source():
        source_terms += 1
        for case, (free, core, auxiliary) in enumerate(cases):
            if point[core] in ambient[core]:
                for row, value in inverses[auxiliary].get(point[auxiliary], ()):
                    outputs[case][(point[free], point[core], row)] += value
    reports = []
    for (free, core, auxiliary), output in zip(cases, outputs):
        nonzero = clean(output)
        first = next(iter(sorted(nonzero.items())), None)
        reports.append({"free_leg": "XYZ"[free], "core_leg": "XYZ"[core],
                        "auxiliary_leg": "XYZ"[auxiliary],
                        "source_terms_checked": source_terms,
                        "all_response_coefficients_checked":
                        960 * len(ambient[core]) * len(maps[auxiliary]),
                        "nonzero_response_coefficients": len(nonzero),
                        "first_nonzero_coefficient":
                        None if first is None else [list(first[0]), first[1]]})
    return reports


def check_mixed(maps):
    reports = mixed_responses(maps)
    if any(item["nonzero_response_coefficients"] for item in reports):
        raise ArithmeticError("A full mixed response is nonzero")
    return reports


def corner_first_support(selected):
    support = set()
    for a, b in product(selected, repeat=2):
        p, r, j = LABELS[a]
        other_p, other_r, other_j = LABELS[b]
        i, k, s = 7 + other_j - j, 12 + p - other_p, 7 + r - other_r
        if 0 <= i < 8 and 0 <= s < 8:
            support.add(coordinate(i, k, s))
    return support


def exhaustive_nine_selection():
    histogram = Counter()
    best = []
    minimum = 1000
    for selected in combinations(range(12), 9):
        rank = len(corner_first_support(selected))
        histogram[rank] += 1
        if rank < minimum:
            minimum, best = rank, [list(selected)]
        elif rank == minimum:
            best.append(list(selected))
    return {"selection_domain": "Nine common coordinate channels among the stated twelve",
            "subsets_checked": sum(histogram.values()),
            "first_response_rank_histogram": {str(k): histogram[k] for k in sorted(histogram)},
            "minimum_first_response_rank": minimum, "minimizing_selections": best,
            "arbitrary_linear_channel_subspaces_excluded": False}


def reduced_lift_maps():
    """Embed nine copies of the (27,16,16) source, with the first factor shared."""
    x = [{coordinate(3 * i, k, 3 * s): 1}
         for i, k, s in product(range(3), repeat=3)]
    y, z = [], []
    for e, f in product(range(3), repeat=2):
        y.extend({coordinate(p, e + 3 * ell, f + 3 * j): 1}
                 for p, ell, j in product(range(2), range(4), range(2)))
        z.extend({coordinate(e + 3 * r, f + 3 * h, q): 1}
                 for r, h, q in product(range(2), range(4), range(2)))
    return [x, y, z]


def check_reduced_lift():
    maps = reduced_lift_maps()
    coefficients, terms = contraction(maps)
    expected = Counter()
    for residue in range(9):
        for i, s in product(range(3), repeat=2):
            for p, q, r, j in product(range(2), repeat=4):
                x = (3 * i + p + q) * 3 + s
                y = 16 * residue + (4 * p + r + s) * 2 + j
                z = 16 * residue + (4 * r + i + j) * 2 + q
                expected[(x, y, z)] += 1
    if coefficients != dict(expected) or any(value != 1 for value in expected.values()):
        raise ArithmeticError("The nine-copy reduced-source identity fails")
    if any(set(inverse(matrix)) - space
           for matrix, space in zip(maps, core_ambient_spaces())):
        raise ArithmeticError("The reduced-source lift escapes the core ambient spaces")
    return {"source_terms_checked": terms, "reduced_format": [27, 16, 16],
            "shared_first_factor": True, "copies": 9, "lifted_format": [27, 144, 144],
            "all_target_coefficients_checked": 27 * 144 * 144,
            "nonzero_target_coefficients": len(coefficients),
            "ambient_containment_checked": True}


def computed_evidence(maps):
    module = check_module(maps)
    mixed = check_mixed(maps)
    ranks = [unit_disjoint_rank(response) for response in responses(maps)]
    if [item["rank"] for item in ranks] != [15, 9, 9]:
        raise ArithmeticError("Unexpected selected auxiliary response ranks")
    if corner_first_support(SELECTED) != {
            coordinate(*triple) for triple in ranks[0]["nonzero_source_coordinates"]}:
        raise ArithmeticError("Pair-formula and full-source response supports differ")
    full_maps = corner_maps(tuple(range(12)))
    full_module = check_module(full_maps)
    full_ranks = [unit_disjoint_rank(response)["rank"] for response in responses(full_maps)]
    if full_ranks != [20, 12, 12]:
        raise ArithmeticError("Unexpected twelve-channel response ranks")
    scan = exhaustive_nine_selection()
    if (scan["subsets_checked"] != 220 or scan["minimum_first_response_rank"] != 15
            or list(SELECTED) != scan["minimizing_selections"][0]):
        raise ArithmeticError("The complete common-channel selection scan fails")
    return {"selected_module": module, "response_ranks": ranks,
            "core_ambient_dimensions": [len(space) for space in core_ambient_spaces()],
            "six_mixed_responses": mixed,
            "twelve_channel_control": {"module": full_module, "response_ranks": full_ranks},
            "complete_coordinate_selection_scan": scan,
            "nine_copy_reduced_lift": check_reduced_lift(),
            "conditional_correction": {
                "missing_premise": "R(27,16,16) maps to M(4,4,3) plus one decomposable error",
                "completed_target_if_premise_holds": [4, 4, 27],
                "response_rank_increase_upper_bounds": [15, 9, 9],
                "first_response_rank_upper_bound": 207,
                "all_three_final_rectangle_budgets_proved": False,
                "missing_maps_constructed": False},
            "new_exponent_established": False, "external_independent_review": False}


def make_certificate():
    maps = corner_maps()
    return {"claim_id": "AI-SPIN-SCALAR-CORNER-125", "field": "Q, hence C",
            "source": [8, 8], "source_leg_dimension": 960,
            "selected_label_indices": list(SELECTED),
            "selected_labels": [list(LABELS[i]) for i in SELECTED],
            "maps": serialize(maps), "evidence": computed_evidence(maps)}


def verify(certificate=None):
    certificate = json.loads(CERTIFICATE.read_text()) if certificate is None else certificate
    if (certificate.get("claim_id") != "AI-SPIN-SCALAR-CORNER-125"
            or certificate.get("field") != "Q, hence C"
            or certificate.get("source") != [8, 8]
            or certificate.get("source_leg_dimension") != 960
            or certificate.get("selected_label_indices") != list(SELECTED)
            or certificate.get("selected_labels") != [list(LABELS[i]) for i in SELECTED]):
        raise ArithmeticError("The scalar-corner certificate has incorrect scope")
    maps = parse(certificate.get("maps"))
    evidence = computed_evidence(maps)
    if certificate.get("evidence") != evidence:
        raise ArithmeticError("The recorded scalar-corner evidence does not match the exact replay")
    if maps != corner_maps():
        raise ArithmeticError("The certificate does not export the stated corner maps")
    return evidence


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true",
                        help="Write the exact proposed certificate before acceptance replay")
    parser.add_argument("--output", type=Path, default=REPORT)
    args = parser.parse_args()
    if args.generate:
        CERTIFICATE.write_text(json.dumps(make_certificate(), indent=2) + "\n")
    report = verify()
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"response_ranks": [item["rank"] for item in report["response_ranks"]],
                      "six_mixed_responses_zero": True,
                      "new_exponent_established": False}))


if __name__ == "__main__":
    main()
