"""Translate the added corner to obtain an exact response-164 core.

This is a separate export; the original response-186 witness stays frozen.
Only the standard library and its exact common verifier are used.
"""

from collections import Counter
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity_structure_cross_module_corner as base

MAPS = base.RESULTS / "parity_structure_cross_module_corner_shifted_maps.json"
REPORT = base.RESULTS / "parity_structure_cross_module_corner_shifted_certificate.json"


def construct(reduced, offsets=(4, 4)):
    if len(offsets) != 2 or any(type(v) is not int or not 0 <= v <= 4 for v in offsets):
        raise ValueError("Both corner offsets must be integers between zero and four")
    hi, hs = offsets
    data = base.construct(reduced)
    data["corner_offsets"] = list(offsets)
    for entry in data["maps"][0]["entries"]:
        i, k, s = base.decode(entry[1])
        if k == 14:
            entry[1] = base.coordinate(i+hi, k, s+hs)
    for entry in data["maps"][1]["entries"]:
        i, k, s = base.decode(entry[1])
        if entry[0] % 12 == 11:
            entry[1] = base.coordinate(i, k+hs, s)
    for entry in data["maps"][2]["entries"]:
        i, k, s = base.decode(entry[1])
        if entry[0] // 4 == 11:
            entry[1] = base.coordinate(i, k+hi, s)
    for item in data["maps"]:
        item["entries"].sort()
    return data


def allowed_support(hi, hs):
    answer = {base.coordinate(i, k, s) for i in range(8) for k in range(4) for s in range(0, 8, 2)}
    answer.update(base.coordinate(i, k, 1) for i in range(hi, 8) for k in (7, 9))
    answer.update(base.coordinate(i, k, s) for i in range(2) for k in (7, 8) for s in range(hs+1, 8))
    answer.update(base.coordinate(i, 14, s) for i in range(hi, hi+4) for s in range(hs, hs+4))
    return answer


def verify(data):
    offsets = data.get("corner_offsets")
    if not isinstance(offsets, list) or len(offsets) != 2 or any(type(v) is not int or not 0 <= v <= 4 for v in offsets):
        raise ArithmeticError("Invalid corner offsets")
    hi, hs = offsets
    maps, denominators = base.parse_maps(data)
    values, source_count, contributions = base.response(maps[1], maps[2])
    actual = Counter()
    for rx, column, vx in maps[0]:
        for yz, value in values.get(column, {}).items():
            ry, rz = divmod(yz, 48)
            actual[rx, ry, rz] += vx*value
    actual = {key: value for key, value in actual.items() if value}
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(4*i+j, 12*j+a, 4*a+i): scale for i, j, a in product(range(4), range(4), range(12))}
    if actual != expected:
        raise ArithmeticError("The translated maps fail the full matrix multiplication identity")
    support = allowed_support(hi, hs)
    if not set(values) <= support:
        raise ArithmeticError("The translated response exceeds its proved support")
    rank, _ = base.modular_rank(values[c] for c in sorted(values))
    if rank != len(values):
        raise ArithmeticError("The modular lower rank does not meet the coordinate-support upper rank")
    return {"source": "A(8,8)", "target": "M(4,4,12)", "corner_offsets": offsets,
            "arithmetic": "integer full replay and exact finite-field rank lower bound",
            "source_terms_checked": source_count, "all_target_coefficients_checked": 36864,
            "nonzero_target_coefficients": len(actual), "all_other_coefficients_zero": True,
            "response_integer_contributions": contributions,
            "full_response_rank_exact": rank, "full_response_kernel_dimension_exact": 960-rank,
            "response_lower_rank_prime": base.PRIME, "proved_response_support_size": len(support),
            "response_support_counts_by_middle_coordinate": dict(sorted(Counter(str(base.decode(c)[1]) for c in values).items(), key=lambda item: int(item[0]))),
            "changed_first_core_flattening": base.first_core_flattening(maps[0]),
            "maximum_equal_leg_dimension_from_this_response_test": 960-rank+16,
            "full_M27_plus_M7_constructed": False, "new_exponent_established": False,
            "external_independent_review": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()
    if args.generate:
        data = construct(json.loads(base.REDUCED.read_text()))
        MAPS.write_text(json.dumps(data, separators=(",", ":"))+"\n")
    else:
        data = json.loads(MAPS.read_text())
    report = verify(data)
    report["maps_sha256"] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
