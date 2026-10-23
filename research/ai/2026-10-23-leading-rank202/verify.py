"""Integer acceptance for the A4 leading-rank total bound 202.

No source constructor, matrix search, or symbolic dependency is imported.
The universal geometric inputs are the byte-pinned written proofs.
"""

from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/leading-rank202-2026-10-23"
RESULT = RESULT_DIR / "controls.json"
CENSUS = RESULT_DIR / "census.json.gz"
SOURCE_PATHS = (
    "research/ai/2026-10-23-all-pair-rank136/proof.md",
    "research/ai/2026-10-23-all-pair-rank144/proof.md",
    "research/ai/2026-10-23-rank92-rank96-spaces/proof.md",
)
CLAIM_SCOPE = {
    "claim_id": "AI-A4-LEADING-RANK-SUM202-001",
    "field": "C",
    "complete_Laurent_presentations": True,
    "individual_scalar_balancing": True,
    "arbitrary_complex_leading_kernels": True,
    "arbitrary_higher_coefficients": True,
    "arbitrary_finite_poles_on_the_unselected_map": True,
    "retains_every_pair136_prerequisite": True,
    "strict_source_thresholds": [92, 96],
    "source_dimension_caps": [68, 72],
    "every_pair_sum_upper": 136,
    "total_leading_rank_upper": 202,
    "short_rank100_long_rank_upper": 28,
    "necessary_conditions_only": True,
    "unique_screen_maximizer": [70, 66, 66],
    "screen_maximizer_is_target_construction": False,
    "target_leading_rank_bounds_sharp": False,
    "matrix_target_constructed": False,
    "smaller_exponent_established": False,
    "independent_external_review": False,
    "formalized": False,
}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def canonical_bytes(document):
    return (json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode()


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    require(document["base_commit"] == "16a13196c3ac501e9e80adfdb7dade0041fc6a36"
            and document["source_cap_commit"] == "a7b550a2b2aa8c36f2eef268a73e083aece39bd2"
            and document["field"] == "C", "changed source version or field")
    entries = document["local_dependencies"]
    require(tuple(entry["path"] for entry in entries) == SOURCE_PATHS, "changed source inventory")
    for entry in entries:
        path = ROOT / entry["path"]
        require(path.is_file(), "missing source prerequisite")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"],
                "source digest mismatch")
    return {entry["path"]: entry["sha256"] for entry in entries}


def source_dimension_cap(rank_ceiling):
    require(type(rank_ceiling) is int and rank_ceiling >= 0, "invalid source rank ceiling")
    if rank_ceiling < 92:
        return 68
    if rank_ceiling < 96:
        return 72
    return 112


def pair_screen(a, b, kind, use_prior=True):
    require(kind in ("mixed", "long"), "unknown target pair")
    maximum_a = 100 if kind == "mixed" else 101
    require(type(a) is int and type(b) is int
            and 0 <= a <= maximum_a and 0 <= b <= 101,
            "rank lies outside the established individual bounds")
    require(type(use_prior) is bool, "invalid prerequisite switch")
    shared, dimension = (10, 110) if kind == "mixed" else (11, 100)
    ceiling = 224 - a - b
    lower = dimension - (a // shared) * (b // shared)
    upper = source_dimension_cap(ceiling)
    prior = use_prior and a + b > 136
    return {"ranks": [a, b], "kind": kind, "source_rank_ceiling": ceiling,
            "kernel_lower": lower, "new_kernel_upper": upper,
            "excluded_by_prior136": prior, "new_kernel_contradiction": lower > upper,
            "excluded": prior or lower > upper}


def set_bit(mask, index):
    mask[index // 8] |= 1 << (index % 8)


def mask_record(shape, prior, retained):
    return {"shape": shape, "prior_survivors_hex": prior.hex(),
            "new_survivors_hex": retained.hex()}


def pair_controls():
    counts, by_sum, extrema, quotients, bitmaps, kept_sets = {}, {}, {}, {}, {}, {}
    for kind, maximum_a in (("mixed", 100), ("long", 101)):
        length = (maximum_a + 1) * 102
        prior_bits, new_bits = bytearray((length + 7) // 8), bytearray((length + 7) // 8)
        prior_count = 0
        kept, cut = set(), set()
        for a in range(maximum_a + 1):
            for b in range(102):
                index = a * 102 + b
                record = pair_screen(a, b, kind)
                if record["excluded_by_prior136"]:
                    continue
                prior_count += 1
                set_bit(prior_bits, index)
                if record["excluded"]:
                    cut.add((a, b))
                else:
                    kept.add((a, b))
                    set_bit(new_bits, index)
        kept_sets[kind] = kept
        counts[kind] = {
            "pairs_checked": length, "prior_excluded": length - prior_count,
            "prior_surviving": prior_count, "newly_excluded": len(cut),
            "total_excluded": length - len(kept), "retained": len(kept),
            "newly_excluded_sum129_through132": sum(a + b <= 132 for a, b in cut),
            "newly_excluded_sum133_through136": sum(a + b >= 133 for a, b in cut),
        }
        rejected_by_sum = Counter(a + b for a, b in cut)
        retained_by_sum = Counter(a + b for a, b in kept)
        by_sum[kind] = [{"sum": s, "newly_excluded": rejected_by_sum[s],
                         "retained": retained_by_sum[s]} for s in range(129, 137)]
        require(set(rejected_by_sum) == set(range(129, 137)), "unexpected selective exclusion range")
        maximum_sum = max(a + b for a, b in kept)
        extrema[kind] = {"maximum_pair_sum": maximum_sum,
                         "pairs_at_maximum": [list(pair) for pair in sorted(kept)
                                              if sum(pair) == maximum_sum]}
        divisor = 10 if kind == "mixed" else 11
        quotients[kind] = {str(s): [list(pair) for pair in sorted({(a // divisor, b // divisor)
                            for a, b in kept if a + b == s})] for s in range(129, 137)}
        bitmaps[kind] = mask_record([maximum_a + 1, 102], prior_bits, new_bits)
    require(counts == {
        "mixed": {"pairs_checked": 10302, "prior_excluded": 2145, "prior_surviving": 8157,
                  "newly_excluded": 488, "total_excluded": 2633, "retained": 7669,
                  "newly_excluded_sum129_through132": 262,
                  "newly_excluded_sum133_through136": 226},
        "long": {"pairs_checked": 10404, "prior_excluded": 2211, "prior_surviving": 8193,
                 "newly_excluded": 329, "total_excluded": 2540, "retained": 7864,
                 "newly_excluded_sum129_through132": 125,
                 "newly_excluded_sum133_through136": 204},
    }, "complete pair census changed")
    for s in range(133, 137):
        require(quotients["mixed"][str(s)] == [[6, 7], [7, 6]], "mixed high-sum quotients changed")
    for s in range(130, 133):
        require(quotients["mixed"][str(s)] == [[5, 8], [6, 7], [7, 6], [8, 5]],
                "mixed intermediate-sum quotients changed")
    require(not quotients["mixed"]["129"], "mixed sum129 gap was lost")
    prior_control = {"with_prior": pair_screen(100, 100, "mixed"),
                     "new_caps_alone": pair_screen(100, 100, "mixed", use_prior=False)}
    require(prior_control["with_prior"]["excluded"]
            and not prior_control["new_caps_alone"]["excluded"], "prior136 necessity control failed")
    return ({"counts": counts, "by_sum": by_sum, "extrema": extrema,
             "floor_quotients": quotients, "retained_prerequisite_control": prior_control},
            bitmaps, kept_sets)


def triple_controls(kept_sets):
    length = 101 * 102 * 102
    prior_bits, new_bits = bytearray((length + 7) // 8), bytearray((length + 7) // 8)
    prior_count = new_count = 0
    prior_top, new_top = Counter(), Counter()
    full_short = []
    maximum, maximizers = -1, []
    for a in range(101):
        for b in range(102):
            for c in range(102):
                index = (a * 102 + b) * 102 + c
                if a + b > 136 or a + c > 136 or b + c > 136:
                    continue
                prior_count += 1
                set_bit(prior_bits, index)
                total = a + b + c
                prior_top[total] += 1
                if ((a, b) not in kept_sets["mixed"] or (a, c) not in kept_sets["mixed"]
                        or (b, c) not in kept_sets["long"]):
                    continue
                new_count += 1
                set_bit(new_bits, index)
                new_top[total] += 1
                if total > maximum:
                    maximum, maximizers = total, [[a, b, c]]
                elif total == maximum:
                    maximizers.append([a, b, c])
                if a == 100:
                    full_short.append([a, b, c])
    require((length, prior_count, new_count) == (1050804, 603885, 541407),
            "complete triple census changed")
    require(maximum == 202 and maximizers == [[70, 66, 66]], "total bound or unique screen maximum changed")
    require(full_short == [[100, b, c] for b in range(29) for c in range(29)],
            "full-short surviving rectangle changed")
    summary = {
        "triples_checked": length, "prior_surviving": prior_count,
        "new_surviving": new_count, "newly_excluded": prior_count - new_count,
        "maximum_total": maximum, "maximizers": maximizers,
        "top_total_counts": [{"total": s, "prior": prior_top[s], "retained": new_top[s]}
                             for s in range(200, 205)],
        "full_short": {"surviving_triples": len(full_short), "long_rank_interval": [0, 28],
                       "maximum_total": 156, "maximizers": [[100, 28, 28]]},
    }
    return summary, mask_record([101, 102, 102], prior_bits, new_bits)


def controls():
    pins = check_sources()
    pairs, pair_masks, kept_sets = pair_controls()
    triples, triple_masks = triple_controls(kept_sets)
    census = {
        "schema": "leading-rank202-census-v1",
        "encoding": "hexadecimal bytes, bit k of byte j is case 8*j+k; unused bits are zero",
        "order": "lexicographic with last coordinate varying fastest; ranks start at zero",
        "prior_screen": "all relevant rank-pair sums at most 136",
        "new_screen": "prior screen plus both strict source-dimension inequalities",
        "mixed": pair_masks["mixed"], "long": pair_masks["long"], "triples": triple_masks,
    }
    report = {
        "schema": "leading-rank202-controls-v1", "source_pins": pins,
        "census_content_sha256": hashlib.sha256(canonical_bytes(census)).hexdigest(),
        "pair_controls": pairs, "triple_controls": triples,
        "strict_threshold_controls": {str(rank): source_dimension_cap(rank) for rank in (91, 92, 95, 96)},
        "claim_scope": CLAIM_SCOPE.copy(),
        "acceptance_arithmetic": "integers only; imported universal theorems checked by proof hashes",
    }
    return report, census


def replay_saved(document, census):
    require(document.get("schema") == "leading-rank202-controls-v1"
            and document.get("claim_scope") == CLAIM_SCOPE, "saved scope differs from the theorem")
    expected, expected_census = controls()
    require(census == expected_census, "saved complete census differs from exact replay")
    require(document == expected, "saved evidence differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        report, census = controls()
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        CENSUS.write_bytes(gzip.compress(canonical_bytes(census), mtime=0))
        RESULT.write_text(json.dumps(report, indent=2) + "\n")
    else:
        report = json.loads(RESULT.read_text())
        census = json.loads(gzip.decompress(CENSUS.read_bytes()))
        replay_saved(report, census)
    print(json.dumps({"pair_counts": report["pair_controls"]["counts"],
                      "triple_controls": report["triple_controls"],
                      "claim_scope": report["claim_scope"]}, indent=2))


if __name__ == "__main__":
    main()
