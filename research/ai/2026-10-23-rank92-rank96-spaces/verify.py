"""Independent integer acceptance for sharp A4 source caps below ranks92/96."""
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
RESULT_DIR = ROOT / "results/rank92-rank96-spaces-2026-10-23"
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
HEADER = {"schema": "rank92-rank96-source-caps-v1",
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


def dominating_profile(profile, threshold):
    require(threshold in (92, 96), "unsupported theorem threshold")
    if profile[2] >= 13:
        return "n2>=13", (16, 16, 16, 8, 8, 4, 0)
    if profile[1] >= 13:
        return "n2<=12,n1>=13", (16, 16, 12, 8, 8, 4, 4)
    if threshold == 96:
        return "n1<=12", (16, 12, 12, 8, 8, 8, 8)
    if profile[2] >= 9:
        return "n1<=12,9<=n2<=12", (16, 12, 12, 8, 8, 8, 4)
    return "n1<=12,n2<=8", (16, 12, 8, 8, 8, 8, 8)


@lru_cache(maxsize=1)
def profile_controls():
    counts = {92: Counter(), 96: Counter()}
    cases = {92: Counter(), 96: Counter()}
    maximal = {92: [], 96: []}
    total = 0
    for profile in layer_profiles():
        total += 1
        ranks = tuple(map(coherent_rank_lower, profile))
        peak = max([MULTIPLICITIES[k]*ranks[k] for k in range(7)] +
                   [ranks[0]+3*ranks[4], 2*ranks[1]+2*ranks[5], 3*ranks[2]+ranks[6]])
        volume = sum(profile)
        for threshold, target in ((92, 68), (96, 72)):
            if peak >= threshold:
                continue
            name, bound = dominating_profile(profile, threshold)
            require(all(n <= b for n, b in zip(profile, bound)) and sum(bound) <= target,
                    "written case split failed on an admissible profile")
            counts[threshold][volume] += 1
            cases[threshold][name] += 1
            if volume == target:
                maximal[threshold].append(list(profile))
    require(total == 245157, "complete layer profile inventory changed")
    result = {}
    for threshold, number, maximum, maximizers in ((92, 119381, 68, 4), (96, 121481, 72, 1)):
        census = counts[threshold]
        require((sum(census.values()), max(census), census[maximum]) ==
                (number, maximum, maximizers), "profile bound or census changed")
        result[str(threshold)] = {
            "admissible_profiles": number, "maximum_volume": maximum,
            "profiles_at_maximum": maximizers, "maximizing_profiles": sorted(maximal[threshold]),
            "written_case_counts": dict(sorted(cases[threshold].items())),
            "volume_histogram": {str(size): census[size] for size in sorted(census)},
        }
    return {"all_nonincreasing_layer_size_profiles": total,
            "constraints": "strict pure-layer and three disjoint-middle-pair lower bounds",
            "thresholds": result, "enumeration_uses_discovery": False,
            "upper_proof_is_written_case_split": True}


def family_coordinates(m):
    require(type(m) is int and m in (2, 3), "cover family is scoped to m=2 or m=3")
    return {(i, k, s) for i, k, s in SOURCE
            if i < 2 or (i == 2 and k < m) or (i == 3 and k == 0)}


def check_cover(allowed, rows, columns, source):
    terms = 0
    for coordinate in allowed:
        for row, column in source[coordinate]:
            require(row in rows or column in columns, "row-and-column cover misses a literal entry")
            terms += 1
    return terms


def sharpness_controls(records, source):
    require(isinstance(records, list) and len(records) == 2, "incomplete sharp space inventory")
    require([record.get("m") for record in records] == [2, 3], "sharp spaces are missing or reordered")
    summaries = []
    for record, dimension, rank in zip(records, (68, 72), (91, 95)):
        require(set(record) == {"m", "dimension", "rank_upper", "row_cover_mask", "column_cover_mask"}
                | MINOR_FIELDS, "changed sharp space fields")
        m = record["m"]
        allowed = family_coordinates(m)
        require(type(record["dimension"]) is int and record["dimension"] == dimension == len(allowed)
                and type(record["rank_upper"]) is int and record["rank_upper"] == rank,
                "sharp dimension or rank budget changed")
        rows = set(indices(parse_mask(record["row_cover_mask"], 112), 112))
        columns = set(indices(parse_mask(record["column_cover_mask"], 112), 112))
        require(rows == {(4*3+0)*7+ell for ell in range(7)}, "changed row-cover formula")
        expected_columns = {(4*h+q)*4+r for h, q, r in product(range(7), range(4), range(4))
                            if h <= 4 or (h == 5 and q < m-1)}
        require(columns == expected_columns and len(rows) == 7 and len(columns) == 76+4*m
                and len(rows)+len(columns) == rank, "changed column-cover formula or budget")
        terms = check_cover(allowed, rows, columns, source)
        replay_minor({key: record[key] for key in MINOR_FIELDS}, source, SOURCE, 112, rank, allowed)
        summaries.append({"m": m, "dimension": dimension, "cover_rows": len(rows),
                          "cover_columns": len(columns), "literal_terms_covered": terms,
                          "uniform_rank_upper": rank, "attained_rank": rank,
                          "strict_threshold": rank+1})
    # The displayed columns cannot be extended to m=1 without a new argument.
    coordinate, position = (3, 0, 0), ((4*2+0)*7, (4*5+0)*4)
    naive_rows = {(4*3+0)*7+ell for ell in range(7)}
    naive_columns = {(4*h+q)*4+r for h, q, r in product(range(5), range(4), range(4))}
    require(position in source[coordinate] and position[0] not in naive_rows
            and position[1] not in naive_columns, "unsupported m=1 extension was not detected")
    return {"sharp_spaces": summaries, "integer_sharpness_minors_replayed": 2,
            "rejected_proposed_dimension_caps": {"rank<92": 64, "rank<96": 68},
            "m1_naive_cover_uncovered_entry": {"coordinate": list(coordinate), "position": list(position)},
            "field_transfer": "Odd integer minors are nonzero over C; support covers work over every field."}


def source_dimension_cap(rank_upper):
    require(type(rank_upper) is int and 0 <= rank_upper <= 112, "invalid matrix rank upper bound")
    if rank_upper < 92:
        return 68
    if rank_upper < 96:
        return 72
    return 112


def controls(document=None):
    pins = check_sources()
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | set(COHERENT_FAMILIES) | {"sharp_spaces"},
            "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    coherent, source = literal_bases()
    return {
        "schema": "rank92-rank96-controls-v1", "source_pins": pins,
        "certificate_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
        "source_controls": source_controls(coherent, source),
        "coherent_controls": coherent_controls(document, coherent),
        "profile_controls": profile_controls(),
        "sharpness_controls": sharpness_controls(document["sharp_spaces"], source),
        "strict_threshold_controls": {str(rank): source_dimension_cap(rank) for rank in (91, 92, 95, 96)},
        "claim_scope": {"field": "C", "strict_source_thresholds": [92, 96],
                        "sharp_maximum_dimensions": [68, 72],
                        "arbitrary_complex_linear_spaces": True,
                        "order_ideal_reduction_characteristic_zero": True,
                        "all_extremizers_classified": False,
                        "target_rank_pair_theorem_claimed": False, "target_constructed": False,
                        "improves_omega": False, "independent_external_review": False, "formalized": False},
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
