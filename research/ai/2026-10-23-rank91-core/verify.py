"""Exact acceptance for the source rank91 core and target total198 continuation."""
from __future__ import annotations

import argparse
from collections import Counter
from functools import lru_cache
import gzip
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/rank91-core-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
CENSUS = RESULT_DIR / "census.json.gz"
SOURCE = tuple(product(range(4), range(7), range(4)))
SHORT = tuple(product(range(4), repeat=2))
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
PAIRS = ((0, 4), (1, 5), (2, 6))
PROFILES = ((16, 16, 16, 8, 8, 4, 0), (16, 16, 12, 8, 8, 4, 4),
            (16, 12, 12, 8, 8, 8, 4), (16, 12, 8, 8, 8, 8, 8))
CORE = ((4, 4, 4, 4), (4, 4, 4, 0), (4, 4, 0, 0), (4, 4, 0, 0),
        (4, 4, 0, 0), (4, 0, 0, 0), (0, 0, 0, 0))
MINOR_FIELDS = {"coefficient_mask", "minor_rows_mask", "minor_columns_mask"}
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
    "research/ai/2026-10-23-rank92-rank96-spaces/proof.md",
    "results/rank92-rank96-spaces-2026-10-23/certificates.json",
    "research/ai/2026-10-23-leading-rank202/proof.md",
)
SCOPE = {"field": "C", "source_rank_threshold_strict": 91,
         "source_dimension_upper": 67, "source_dimension_cap_claimed_sharp": False,
         "complete_Laurent_presentations": True, "individual_scalar_balancing": True,
         "arbitrary_complex_leading_kernels": True, "arbitrary_higher_coefficients": True,
         "arbitrary_finite_poles_on_the_unselected_map": True,
         "retains_all_frozen202_screens": True,
         "mixed_pair_sum_upper": 133, "long_pair_sum_upper": 136,
         "total_leading_rank_upper": 198, "short_rank100_long_rank_upper": 28,
         "screen_maximizers": [[62, 66, 70], [62, 70, 66]],
         "necessary_conditions_only": True, "target_bound_claimed_sharp": False,
         "target_constructed": False, "improves_omega": False,
         "independent_external_review": False, "formalized": False}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def canonical_bytes(document):
    return (json.dumps(document, sort_keys=True, separators=(",", ":"))+"\n").encode()


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    require(document["base_commit"] == "658e2d54fa7b506f7d8fd51eeec7788f23a00e91"
            and document["field"] == "C", "changed source version or field")
    entries = document["local_dependencies"]
    require(tuple(entry["path"] for entry in entries) == SOURCE_PATHS, "changed source inventory")
    result = {}
    for entry in entries:
        path = ROOT / entry["path"]
        require(path.is_file(), "missing source prerequisite")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == entry["sha256"], "source digest mismatch")
        result[entry["path"]] = digest
    return result


def literal_bases():
    coherent = {coordinate: set() for coordinate in SHORT}
    source = {coordinate: set() for coordinate in SOURCE}
    for i, j, r, s in product(range(4), repeat=4):
        coherent[i, s].add((7*j+r+s, 4*(i+j)+r))
    for i, j, p, q, r, s in product(range(4), repeat=6):
        source[i, p+q, s].add(((4*j+p)*7+r+s, (4*(i+j)+q)*4+r))
    require(sum(map(len, coherent.values())) == 256 and sum(map(len, source.values())) == 4096,
            "literal term inventory changed")
    return coherent, source


def parse_mask(value, width):
    require(type(value) is str, "mask must be a hexadecimal string")
    try:
        mask = int(value, 16)
    except ValueError as error:
        raise ArithmeticError("invalid hexadecimal mask") from error
    require(0 <= mask < (1 << width) and value == hex(mask), "noncanonical or out-of-range mask")
    return [index for index in range(width) if (mask >> index) & 1]


def nonsingular_mod2(rows, size):
    require(len(rows) == size and all(type(row) is int and 0 <= row < (1 << size) for row in rows),
            "invalid binary square matrix")
    rows = list(rows)
    for column in range(size):
        pivot = next((r for r in range(column, size) if (rows[r] >> column) & 1), None)
        if pivot is None:
            return False
        rows[column], rows[pivot] = rows[pivot], rows[column]
        for r in range(column+1, size):
            if (rows[r] >> column) & 1:
                rows[r] ^= rows[column]
    return True


def replay_minor(record, basis, coordinates, width, rank, allowed):
    require(set(record) == MINOR_FIELDS, "changed minor fields")
    selected = [coordinates[n] for n in parse_mask(record["coefficient_mask"], len(coordinates))]
    require(selected and set(selected) <= allowed, "coefficient support leaves its space")
    rows, columns = (parse_mask(record[key], width) for key in ("minor_rows_mask", "minor_columns_mask"))
    require(len(rows) == len(columns) == rank, "minor dimensions changed")
    full_rows = [0]*width
    for coordinate in selected:
        for row, column in basis[coordinate]:
            full_rows[row] ^= 1 << column
    minor = [sum(((full_rows[row] >> column) & 1) << n for n, column in enumerate(columns)) for row in rows]
    require(nonsingular_mod2(minor, rank), "saved minor is singular modulo two")


def short_shapes(volume):
    return {shape for shape in product(range(5), repeat=4)
            if sum(shape) == volume and all(shape[i] >= shape[i+1] for i in range(3))}


def coordinates(layers):
    require(len(layers) == 7 and all(len(shape) == 4 and all(type(x) is int and 0 <= x <= 4 for x in shape)
                                    for shape in layers), "invalid layer shapes")
    return {(i, k, s) for i, k, s in SOURCE if s < layers[k][i]}


def rho(size):
    return 0 if size == 0 else 16+4*((size-1)//4)


def equality_profiles():
    """Exhaust size68 nonincreasing profiles, with only necessary rank constraints."""
    result, chosen = [], []

    def visit(remaining):
        k = len(chosen)
        if k == 7:
            if remaining == 0:
                ranks = list(map(rho, chosen))
                if all(MULTIPLICITIES[a]*ranks[a]+MULTIPLICITIES[b]*ranks[b] < 91 for a, b in PAIRS):
                    result.append(tuple(chosen))
            return
        upper = chosen[-1] if chosen else 16
        for value in range(min(upper, remaining)+1):
            if value*(7-k) < remaining or MULTIPLICITIES[k]*rho(value) >= 91:
                continue
            chosen.append(value)
            visit(remaining-value)
            chosen.pop()

    visit(68)
    require(set(result) == set(PROFILES) and len(result) == 4, "equality profile inventory changed")
    return result


def layer_rank_limits(profile):
    limits = [90//m for m in MULTIPLICITIES]
    for a, b in PAIRS:
        limits[a] = min(limits[a], (90-MULTIPLICITIES[b]*rho(profile[b]))//MULTIPLICITIES[a])
        limits[b] = min(limits[b], (90-MULTIPLICITIES[a]*rho(profile[a]))//MULTIPLICITIES[b])
    # Equal-size nested ideals coincide, so every occurrence inherits the strongest limit.
    return {size: min(limits[k] for k in range(7) if profile[k] == size) for size in set(profile)}


def source_controls(document):
    require(set(document) == {"schema", "verification_modulus", "coefficient_domain", "coherent_pairs", "core"}
            and document["schema"] == "rank91-core-minors-v1" and document["verification_modulus"] == 2
            and document["coefficient_domain"] == "integers 0 and 1", "changed certificate schema")
    coherent, source = literal_bases()
    require(len(document["coherent_pairs"]) == 3, "incomplete coherent pair inventory")
    old = json.loads((ROOT / SOURCE_PATHS[3]).read_text())
    class_counts = {}
    for record, d, rank in zip(document["coherent_pairs"], (1, 2, 3), (20, 24, 26)):
        require(set(record) == {"d", "rank_lower"} | MINOR_FIELDS
                and type(record["d"]) is int and record["d"] == d
                and type(record["rank_lower"]) is int and record["rank_lower"] == rank,
                "coherent binomial parameters changed")
        minor = {key: record[key] for key in MINOR_FIELDS}
        expected_support = {(d, 0), (0, d)}
        require({SHORT[n] for n in parse_mask(minor["coefficient_mask"], 16)} == expected_support,
                "coherent binomial support changed")
        replay_minor(minor, coherent, SHORT, 28, rank, expected_support)
        if d == 1:
            require(minor == old["coherent20_pair"], "credited20-minor changed")
        if d == 2:
            require(any(minor == {key: item[key] for key in MINOR_FIELDS} for item in old["coherent9_ideals"]),
                    "credited24-minor changed")
        strips = {(4,)*d+(0,)*(4-d), (d,)*4}
        shapes = short_shapes(4*d)
        require(strips <= shapes, "strip inventory changed")
        for shape in shapes-strips:
            require(shape[d] >= 1 and shape[0] >= d+1, "a non-strip ideal misses its binomial")
        class_counts[str(4*d)] = {"all_short_ideals": len(shapes), "strips": 2,
                                 "non_strips_excluded_by_binomial": len(shapes)-2, "binomial_rank_lower": rank}
    core_record = document["core"]
    require(set(core_record) == {"layers", "dimension", "rank_lower"} | MINOR_FIELDS
            and core_record["layers"] == [list(shape) for shape in CORE]
            and type(core_record["dimension"]) is int and core_record["dimension"] == 56
            and type(core_record["rank_lower"]) is int and core_record["rank_lower"] == 91,
            "common core or its rank budget changed")
    core = coordinates(CORE)
    require(len(core) == 56, "core dimension changed")
    replay_minor({key: core_record[key] for key in MINOR_FIELDS}, source, SOURCE, 112, 91, core)
    transposed_core = {(s, k, i) for i, k, s in core}
    for i, k, s in SOURCE:
        expected = set()
        for row, column in source[i, k, s]:
            jp, ell = divmod(row, 7)
            j, p = divmod(jp, 4)
            hq, r = divmod(column, 4)
            h, q = divmod(hq, 4)
            expected.add(((4*r+q)*7+h, (4*ell+p)*4+j))
        require(expected == source[s, k, i], "literal transpose identity failed")
    ideal_records = []
    for profile in sorted(equality_profiles(), reverse=True):
        limits = layer_rank_limits(profile)
        choices = []
        for size in profile:
            if size in (0, 16):
                choices.append([((size//4),)*4])
            else:
                d = size//4
                require(limits[size] < {4: 20, 8: 24, 12: 26}[size], "layer does not force a strip")
                choices.append([(4,)*d+(0,)*(4-d), (d,)*4])
        accepted = []
        for layers in product(*choices):
            if not all(layers[k][i] >= layers[k+1][i] for k in range(6) for i in range(4)):
                continue
            allowed = coordinates(layers)
            require(len(allowed) == 68 and (core <= allowed or transposed_core <= allowed),
                    "an equality ideal misses both common-core orientations")
            accepted.append([list(shape) for shape in layers])
        require(len(accepted) == 2, "nested strip orientation inventory changed")
        ideal_records.append({"profile": list(profile), "coherent_upper_by_size": {str(k): v for k, v in sorted(limits.items())},
                              "ideals": accepted})
    boundary = old["sharp_spaces"][0]
    require(boundary["dimension"] == 68 and boundary["rank_upper"] == 91, "strict-threshold boundary changed")
    return {"literal_source_terms": 4096, "literal_coherent_terms": 256,
            "integer_minors_replayed": 4, "new_minors": 2, "credited_minors": 2,
            "short_ideal_classes": class_counts, "equality_profiles": ideal_records,
            "equality_ideals": 8, "core_dimension": 56, "core_rank_lower": 91,
            "transpose_basis_identities": 112, "transpose_literal_terms": 4096,
            "weak_rank91_cap67_disproved_by_pinned_dimension68_example": True}


def source_cap(ceiling, endpoint=True):
    require(type(ceiling) is int and ceiling >= 0 and type(endpoint) is bool, "invalid source ceiling")
    if endpoint and ceiling < 91:
        return 67
    if ceiling < 92:
        return 68
    if ceiling < 96:
        return 72
    return 112


def pair_screen(p, q, kind, endpoint=True, use_prior=True):
    require(kind in ("mixed", "long"), "invalid pair kind")
    maximum = 100 if kind == "mixed" else 101
    require(type(p) is int and type(q) is int and 0 <= p <= maximum and 0 <= q <= 101,
            "rank outside established individual ranges")
    require(type(use_prior) is bool, "invalid prior switch")
    divisor, dimension = (10, 110) if kind == "mixed" else (11, 100)
    ceiling = 224-p-q
    lower, upper = dimension-(p//divisor)*(q//divisor), source_cap(ceiling, endpoint)
    prior = use_prior and p+q > 136
    return {"ceiling": ceiling, "kernel_lower": lower, "kernel_upper": upper,
            "excluded_by_prior136": prior, "kernel_contradiction": lower > upper,
            "excluded": prior or lower > upper}


def mark(mask, index):
    mask[index//8] |= 1 << (index % 8)


@lru_cache(maxsize=1)
def target_controls():
    counts, masks, kept = {}, {}, {}
    for kind, maximum in (("mixed", 100), ("long", 101)):
        old, new = set(), set()
        total = (maximum+1)*102
        old_bits, new_bits = bytearray((total+7)//8), bytearray((total+7)//8)
        cuts = Counter()
        for p, q in product(range(maximum+1), range(102)):
            if not pair_screen(p, q, kind, endpoint=False)["excluded"]:
                old.add((p, q))
                mark(old_bits, 102*p+q)
            if not pair_screen(p, q, kind)["excluded"]:
                new.add((p, q))
                mark(new_bits, 102*p+q)
            elif (p, q) in old:
                cuts[p+q] += 1
        require(new <= old, "a frozen202 pair exclusion was lost")
        kept[kind] = old, new
        counts[kind] = {"checked": total, "prior202_retained": len(old), "retained": len(new),
                        "newly_excluded": len(old-new), "new_exclusions_by_sum": {str(s): cuts[s] for s in sorted(cuts)},
                        "maximum_pair_sum": max(p+q for p, q in new)}
        masks[kind] = {"shape": [maximum+1, 102], "index": "102*p+q",
                       "prior202_survivors_hex": old_bits.hex(), "survivors_hex": new_bits.hex()}
    require(counts["mixed"]["prior202_retained"] == 7669 and counts["long"]["prior202_retained"] == 7864,
            "frozen202 pair inventory changed")
    require(counts["mixed"]["maximum_pair_sum"] == 133 and counts["long"]["maximum_pair_sum"] == 136,
            "new pair bounds failed")
    total = 101*102*102
    old_bits, new_bits = bytearray((total+7)//8), bytearray((total+7)//8)
    old_count = new_count = 0
    top, maxima, maximum = Counter(), [], -1
    for a, b, c in product(range(101), range(102), range(102)):
        index = (102*a+b)*102+c
        old_ok = (a, b) in kept["mixed"][0] and (a, c) in kept["mixed"][0] and (b, c) in kept["long"][0]
        new_ok = (a, b) in kept["mixed"][1] and (a, c) in kept["mixed"][1] and (b, c) in kept["long"][1]
        if old_ok:
            old_count += 1
            mark(old_bits, index)
        if not new_ok:
            continue
        require(old_ok, "a frozen202 triple exclusion was lost")
        new_count += 1
        mark(new_bits, index)
        volume = a+b+c
        if volume >= 190:
            top[volume] += 1
        if volume > maximum:
            maximum, maxima = volume, []
        if volume == maximum:
            maxima.append([a, b, c])
    require(old_count == 541407 and maximum == 198 and maxima == [[62, 66, 70], [62, 70, 66]],
            "triple bound or arithmetic endpoints changed")
    masks["triples"] = {"shape": [101, 102, 102], "index": "(102*a+b)*102+c",
                         "prior202_survivors_hex": old_bits.hex(), "survivors_hex": new_bits.hex()}
    prior_control = {"with_prior": pair_screen(100, 100, "mixed"),
                     "new_cap_alone": pair_screen(100, 100, "mixed", use_prior=False)}
    require(prior_control["with_prior"]["excluded"] and not prior_control["new_cap_alone"]["excluded"],
            "prior136 prerequisite control failed")
    return {"pair_counts": counts, "triple_counts": {"checked": total, "prior202_retained": old_count,
            "retained": new_count, "newly_excluded": old_count-new_count, "maximum_total": maximum,
            "maximizers": maxima, "retained_by_total_at_least190": {str(s): top[s] for s in sorted(top)}},
            "prior136_control": prior_control,
            "former202_endpoint": {"prior_passes": not pair_screen(70, 66, "mixed", endpoint=False)["excluded"],
                                    "new_mixed_pair": pair_screen(70, 66, "mixed")}}, masks


def controls(document=None):
    pins = check_sources()
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    source = source_controls(document)
    target, masks = target_controls()
    census = {"schema": "rank91-core-census-v1", "bit_order": "least significant bit first in each byte", **masks}
    report = {"schema": "rank91-core-controls-v1", "source_pins": pins,
              "certificate_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
              "source_controls": source, "target_controls": target,
              "strict_threshold_controls": {str(x): source_cap(x) for x in (90, 91, 92, 95, 96)},
              "census_sha256": hashlib.sha256(canonical_bytes(census)).hexdigest(), "claim_scope": SCOPE}
    return report, census


def replay_saved(report, census):
    expected, expected_census = controls()
    require(report == expected and census == expected_census, "saved evidence, census or scope differs from replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report, census = controls()
    if args.write_report:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report, indent=2)+"\n")
        CENSUS.write_bytes(gzip.compress(canonical_bytes(census), mtime=0))
    else:
        replay_saved(json.loads(RESULT.read_text()), json.loads(gzip.decompress(CENSUS.read_bytes())))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
