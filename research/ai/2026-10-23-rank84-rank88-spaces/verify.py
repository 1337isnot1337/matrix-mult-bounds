"""Independent exact acceptance for sharp A4 dimension caps below ranks84/88."""
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
RESULT_DIR = ROOT / "results/rank84-rank88-spaces-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
OLD_CERTIFICATES = ROOT / "results/torus-rank80-2026-10-23/certificates.json"
SOURCE = tuple(product(range(4), range(7), range(4)))
SHORT = tuple(product(range(4), repeat=2))
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
DISJOINT_PAIRS = ((0, 4), (1, 5), (2, 6))
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
    "research/ai/2026-10-23-torus-rank80/proof.md",
    "results/torus-rank80-2026-10-23/certificates.json",
    "research/ai/2026-10-23-source-staircase-spaces/proof.md",
)
HEADER = {"schema": "rank84-rank88-source-caps-v1",
          "coefficient_domain": "integers 0 and 1", "verification_modulus": 2}
COHERENT_FAMILIES = ("coherent20_pair", "coherent9_ideals", "coherent13_ideals")
MINOR_FIELDS = {"coefficient_mask", "minor_rows_mask", "minor_columns_mask"}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    entries = document["local_dependencies"]
    require(len(entries) == len(SOURCE_PATHS)
            and {item["path"] for item in entries} == set(SOURCE_PATHS),
            "changed source inventory")
    result = {}
    for item in entries:
        path = ROOT / item["path"]
        require(path.is_file(), "missing source prerequisite")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(digest == item["sha256"], "source digest mismatch")
        result[item["path"]] = digest
    return dict(sorted(result.items()))


def literal_bases():
    """Rebuild basis supports from the original six short indices."""
    coherent = {coordinate: set() for coordinate in SHORT}
    source = {coordinate: set() for coordinate in SOURCE}
    positions = set()
    for i, j, p, q, r, s in product(range(4), repeat=6):
        position = ((4*j+p)*7+r+s, (4*(i+j)+q)*4+r)
        require(position not in positions, "overlapping source coefficient labels")
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
        require(len(positions) == len({r for r, c in positions})
                == len({c for r, c in positions}) == 16,
                "coherent monomial rank changed")
    for i, k, s in SOURCE:
        expected = set()
        for p, q in product(range(4), repeat=2):
            if p+q != k:
                continue
            for row, column in coherent[i, s]:
                j, ell = divmod(row, 7)
                h, r = divmod(column, 4)
                expected.add(((4*j+p)*7+ell, (4*h+q)*4+r))
        require(source[i, k, s] == expected, "source tensor factorization mismatch")
        rank = 16*MULTIPLICITIES[k]
        require(len(expected) == len({r for r, c in expected})
                == len({c for r, c in expected}) == rank,
                "source monomial rank changed")
    layers = {k: set().union(*(source[i, k, s] for i, s in SHORT)) for k in range(7)}
    for a, b in DISJOINT_PAIRS:
        require({r for r, c in layers[a]}.isdisjoint({r for r, c in layers[b]})
                and {c for r, c in layers[a]}.isdisjoint({c for r, c in layers[b]}),
                "paired middle blocks are not row-and-column disjoint")
    return {"literal_source_terms": 4096, "literal_coherent_terms": 256,
            "coherent_monomial_ranks_checked": 16, "source_factorizations_checked": 112,
            "middle_multiplicities": list(MULTIPLICITIES),
            "disjoint_middle_pairs": [list(pair) for pair in DISJOINT_PAIRS]}


def short_ideals(volume):
    """Exhaust all four heights directly; no discovery enumerator is imported."""
    return {shape for shape in product(range(5), repeat=4)
            if sum(shape) == volume and all(shape[i] >= shape[i+1] for i in range(3))}


def parse_mask(value, width):
    require(type(value) is str, "mask must be a hexadecimal string")
    try:
        mask = int(value, 16)
    except ValueError as error:
        raise ArithmeticError("invalid hexadecimal mask") from error
    require(0 <= mask < (1 << width) and value == hex(mask),
            "mask is out of range or noncanonical")
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
    selected = [coordinates[index] for index in
                indices(parse_mask(record["coefficient_mask"], len(coordinates)), len(coordinates))]
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
    require(document["coherent20_pair"]["coefficient_mask"] == "0x12",
            "coherent rank20 pair changed")
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
            "coherent_rank_lower_by_nonzero_layer_size":
                {"1..4": 16, "5..8": 20, "9..12": 24, "13..16": 28}}


def coherent_rank_lower(size):
    require(type(size) is int and 0 <= size <= 16, "invalid short-layer size")
    return 0 if size == 0 else 16+4*((size-1)//4)


def layer_profiles():
    """Recursively enumerate every nonincreasing seven-tuple in [0,16]."""
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


@lru_cache(maxsize=1)
def profile_controls():
    counts = {84: Counter(), 88: Counter()}
    maximal = {84: [], 88: []}
    total = 0
    for profile in layer_profiles():
        total += 1
        ranks = tuple(map(coherent_rank_lower, profile))
        pure = [MULTIPLICITIES[k]*ranks[k] for k in range(7)]
        paired = [ranks[0]+3*ranks[4], 2*ranks[1]+2*ranks[5], 3*ranks[2]+ranks[6]]
        peak, volume = max(pure+paired), sum(profile)
        for threshold in (84, 88):
            if peak < threshold:
                counts[threshold][volume] += 1
                target = 56 if threshold == 84 else 60
                if volume == target:
                    maximal[threshold].append(list(profile))
    require(total == 245157, "complete layer profile inventory changed")
    expected = {84: (51553, 56, 4), 88: (59809, 60, 2)}
    result = {}
    for threshold, (number, maximum, maximizers) in expected.items():
        census = counts[threshold]
        require((sum(census.values()), max(census), census[maximum])
                == (number, maximum, maximizers), "profile bound or census changed")
        result[str(threshold)] = {
            "admissible_profiles": number, "maximum_volume": maximum,
            "profiles_at_maximum": maximizers, "maximizing_profiles": sorted(maximal[threshold]),
            "volume_histogram": {str(size): census[size] for size in sorted(census)},
        }
    return {"all_nonincreasing_layer_size_profiles": total,
            "constraints": "strict pure-layer and three disjoint-middle-pair rank lower bounds",
            "thresholds": result, "enumeration_uses_discovery": False}


def staircase_support(source, d, m):
    require(type(d) is int and d == 2 and type(m) is int and m in (0, 1, 2),
            "unsupported staircase parameters")
    allowed = {coordinate for coordinate in SOURCE
               if coordinate[0] < d or (coordinate[0] == d and coordinate[1] < m)}
    support = set().union(*(source[coordinate] for coordinate in allowed))
    columns = {column for row, column in support}
    expected = {(4*h+q)*4+r for h, q, r in product(range(7), range(4), range(4))
                if h <= 4 or (h == 5 and q < m)}
    require(columns == expected and len(allowed) == 56+4*m and len(columns) == 80+4*m,
            "literal staircase support or dimension changed")
    return allowed, columns


def sharpness_controls(records, boundary, source):
    require(isinstance(records, list) and len(records) == 2, "incomplete sharp space inventory")
    require([record.get("m") for record in records] == [0, 1], "sharp spaces are missing or reordered")
    summaries = []
    for record, (dimension, rank) in zip(records, ((56, 80), (60, 84))):
        require(set(record) == {"d", "m", "dimension", "rank_upper"} | MINOR_FIELDS,
                "changed sharp space fields")
        require(type(record["dimension"]) is int and record["dimension"] == dimension
                and type(record["rank_upper"]) is int and record["rank_upper"] == rank,
                "sharp dimension or rank budget changed")
        allowed, columns = staircase_support(source, record["d"], record["m"])
        minor = {key: record[key] for key in MINOR_FIELDS}
        replay_minor(minor, source, SOURCE, 112, rank, allowed)
        summaries.append({"d": record["d"], "m": record["m"], "dimension": dimension,
                          "supported_columns": len(columns), "uniform_rank_upper": rank,
                          "attained_rank": rank, "strict_threshold": rank+4})
    require(boundary == {"d": 2, "m": 2, "dimension": 64, "rank_upper": 88}
            and all(type(value) is int for value in boundary.values()), "changed boundary space")
    allowed, columns = staircase_support(source, 2, 2)
    return {"sharp_spaces": summaries,
            "boundary_space": {"dimension": len(allowed), "supported_columns": len(columns),
                               "uniform_rank_upper": 88, "strict_rank88_not_established": True},
            "integer_sharpness_minors_replayed": 2,
            "field_transfer": "Odd integer minors are nonzero over C; support bounds hold over every field."}


def long_pair_controls():
    """Finite corollary screen; the prior long sum144 theorem is a pinned input."""
    new = Counter()
    total = 0
    for b, c in product(range(111), repeat=2):
        total += 1
        if not 136 < b+c <= 144:
            continue
        delta = 224-b-c
        threshold, cap = (84, 56) if delta < 84 else (88, 60)
        require(delta < threshold, "long-pair strict rank threshold failed")
        needed = 100-(b//11)*(c//11)
        require(needed > cap, "long-pair support inequality did not contradict source cap")
        new[threshold] += 1
    require(total == 12321 and sum(new.values()) == 644, "long-pair census changed")
    return {"integer_long_rank_pairs": total, "credited_prior_long_sum_upper": 144,
            "new_long_sum_upper": 136, "newly_excluded_pairs": 644,
            "excluded_by_threshold": {str(k): new[k] for k in sorted(new)},
            "rank_sum136_boundary_not_excluded": True,
            "conditional_on_credited_prior_long_sum_and_saturation": True,
            "target_rank_pair_theorem_claimed": False,
            "all_target_leg_pairs_claimed": False}


def controls(document=None):
    pins = check_sources()
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | set(COHERENT_FAMILIES) | {"sharp_spaces", "boundary_space"},
            "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    coherent, source = literal_bases()
    return {
        "schema": "rank84-rank88-controls-v1", "source_pins": pins,
        "certificate_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
        "source_controls": source_controls(coherent, source),
        "coherent_controls": coherent_controls(document, coherent),
        "profile_controls": profile_controls(),
        "sharpness_controls": sharpness_controls(document["sharp_spaces"], document["boundary_space"], source),
        "long_pair_controls": long_pair_controls(),
        "claim_scope": {"field": "C", "strict_source_thresholds": [84, 88],
                        "sharp_maximum_dimensions": [56, 60],
                        "arbitrary_complex_linear_spaces": True,
                        "order_ideal_reduction_characteristic_zero": True,
                        "conditional_long_pair_screen_upper": 136,
                        "target_rank_pair_theorem_claimed": False,
                        "all_target_leg_pairs_claimed": False,
                        "target_constructed": False, "improves_omega": False,
                        "independent_external_review": False, "formalized": False},
    }


def replay_saved(document):
    require(document == controls(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = controls()
    if args.write_report:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report, indent=2)+"\n")
    else:
        require(json.loads(RESULT.read_text()) == report, "saved evidence or scope differs from exact replay")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
