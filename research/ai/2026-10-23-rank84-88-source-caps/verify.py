"""Independent literal-source and complete-inventory acceptance for rank84/88 caps."""
from __future__ import annotations

from functools import lru_cache
import gzip
import hashlib
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/rank84-88-source-caps-2026-10-23"
SOURCE = tuple(product(range(4), range(7), range(4)))
SHORT = tuple(product(range(4), repeat=2))
CASES = {84: (57, 1404), 88: (61, 118)}
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
    "research/ai/2026-10-23-torus-rank80/proof.md",
    "research/ai/2026-10-23-torus-rank80/discover.py",
    "research/ai/2026-10-23-source-staircase-spaces/proof.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["field"] == "C", "Changed geometric field")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {e["path"] for e in entries} == DEPENDENCIES, "Changed source inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
                == entry["sha256"], "Source digest mismatch: " + entry["path"])
    for threshold in CASES:
        path = RESULT / f"rank{threshold}-minors.json.gz"
        require(hashlib.sha256(path.read_bytes()).hexdigest()
                == record["certificates"][str(threshold)], "Changed finite certificate")


def literal_bases():
    source = {v: set() for v in SOURCE}
    coherent = {v: set() for v in SHORT}
    for i, j, p, q, r, z in product(range(4), repeat=6):
        source[i, p+q, z].add(((4*j+p)*7+r+z, (4*(i+j)+q)*4+r))
        if p == q == 0:
            coherent[i, z].add((7*j+r+z, 4*(i+j)+r))
    require(sum(map(len, source.values())) == 4096, "Changed literal source")
    require(sum(map(len, coherent.values())) == 256, "Changed coherent source")
    for i, k, z in SOURCE:
        expanded = set()
        for row, column in coherent[i, z]:
            j, ell = divmod(row, 7)
            h, r = divmod(column, 4)
            for p, q in product(range(4), repeat=2):
                if p+q == k:
                    expanded.add(((4*j+p)*7+ell, (4*h+q)*4+r))
        require(expanded == source[i, k, z], "Middle/coherent factorization failed")
    supports = [set().union(*(source[i, k, z] for i, z in SHORT)) for k in (1, 5)]
    row_sets = [{r for r, c in support} for support in supports]
    col_sets = [{c for r, c in support} for support in supports]
    require(not row_sets[0] & row_sets[1] and not col_sets[0] & col_sets[1],
            "The middle1/5 blocks are not disjoint")
    require(list(map(len, row_sets)) == list(map(len, col_sets)) == [56, 56],
            "Changed middle block sizes")
    return source, coherent


@lru_cache(None)
def short_shapes(volume, ceiling=(4, 4, 4, 4)):
    result = []

    def visit(chosen, remaining):
        position = len(chosen)
        if position == 4:
            if remaining == 0:
                result.append(tuple(chosen))
            return
        upper = min(ceiling[position], chosen[-1] if chosen else 4, remaining)
        for height in range(upper+1):
            if remaining-height <= (3-position)*height:
                visit(chosen+[height], remaining-height)

    visit([], volume)
    return tuple(result)


def profiles(volume):
    def visit(chosen, remaining):
        if len(chosen) == 7:
            if remaining == 0:
                yield tuple(chosen)
            return
        for size in range(min(remaining, chosen[-1] if chosen else 16)+1):
            if remaining-size <= (6-len(chosen))*size:
                yield from visit(chosen+[size], remaining-size)
    return visit([], volume)


def acceptance_inventory(threshold, lower):
    """Volume profiles then recursive heights, separate from discovery's shape DAG."""
    dimension = CASES[threshold][0]
    result = []
    for profile in profiles(dimension):
        def visit(chosen):
            k = len(chosen)
            if k == 7:
                result.append(tuple(chosen))
                return
            parent = chosen[-1] if chosen else (4, 4, 4, 4)
            for shape in short_shapes(profile[k], parent):
                if MULTIPLICITIES[k]*lower[shape] >= threshold:
                    continue
                if k == 5 and 2*lower[chosen[1]]+2*lower[shape] >= threshold:
                    continue
                visit(chosen+[shape])
        visit([])
    return sorted(result)


def parse_mask(value, width):
    require(type(value) is str, "Non-string mask")
    mask = int(value, 16)
    require(0 <= mask < 1 << width and hex(mask) == value, "Noncanonical mask")
    return mask


def selected(mask, width):
    return [i for i in range(width) if mask >> i & 1]


def check_minor(record, basis, coordinates, size, target, allowed):
    coefficients = selected(parse_mask(record["coefficient_mask"], len(coordinates)), len(coordinates))
    row_ids = selected(parse_mask(record["minor_rows_mask"], size), size)
    column_ids = selected(parse_mask(record["minor_columns_mask"], size), size)
    require(len(row_ids) == len(column_ids) == target, "Wrong minor dimensions")
    chosen = [coordinates[i] for i in coefficients]
    require(set(chosen) <= allowed, "Witness coefficients leave the claimed ideal")
    if target == 0:
        require(not chosen and not allowed, "Invalid empty coherent control")
        return
    full = [0]*size
    for coordinate in chosen:
        for row, column in basis[coordinate]:
            full[row] ^= 1 << column
    pivots = {}
    for row in row_ids:
        value = sum(((full[row] >> column) & 1) << i for i, column in enumerate(column_ids))
        while value:
            pivot = value.bit_length()-1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    require(len(pivots) == target, "The saved integer minor is even or singular")


def verify_document(document, source, coherent):
    require(document["schema"] == "rank84-88-source-caps-v1"
            and document["field_of_geometric_reduction"] == "C"
            and document["coefficient_domain"] == "integers zero and one"
            and document["verification_modulus"] == 2, "Changed certificate model")
    threshold = document["threshold"]
    require(threshold in CASES and document["dimension"] == CASES[threshold][0],
            "Changed threshold or dimension")
    controls = document["coherent_minors"]
    expected_shapes = sorted(shape for n in range(17) for shape in short_shapes(n))
    require(len(controls) == 70 and [tuple(c["shape"]) for c in controls] == expected_shapes,
            "Incomplete coherent control inventory")
    lower = {}
    for control in controls:
        shape = tuple(control["shape"])
        rank_lower = control["rank_lower"]
        require(type(rank_lower) is int and 0 <= rank_lower <= 28, "Invalid coherent rank")
        allowed = {v for v in SHORT if v[1] < shape[v[0]]}
        check_minor(control, coherent, SHORT, 28, rank_lower, allowed)
        lower[shape] = rank_lower
    inventory = acceptance_inventory(threshold, lower)
    require(len(inventory) == CASES[threshold][1], "Changed complete ideal inventory")
    records = document["source_minors"]
    actual_shapes = [tuple(tuple(layer) for layer in record["shape"]) for record in records]
    require(actual_shapes == inventory, "Missing, duplicated or reordered source ideal")
    for shape, record in zip(inventory, records):
        allowed = {v for v in SOURCE if v[2] < shape[v[1]][v[0]]}
        require(len(allowed) == CASES[threshold][0], "Wrong source-ideal volume")
        check_minor(record, source, SOURCE, 112, threshold, allowed)
    return {"threshold": threshold, "dimension_cap": CASES[threshold][0]-1,
            "coherent_shapes": 70, "source_ideals": len(inventory)}


def sharp_spaces(source):
    records = []
    for extra, dimension, columns in ((0, 56, 80), (1, 60, 84), (2, 64, 88)):
        allowed = [v for v in SOURCE if v[0] < 2 or (v[0] == 2 and v[1] < extra)]
        joint = set().union(*(source[v] for v in allowed))
        actual_columns = {column for row, column in joint}
        require(len(allowed) == dimension and len(actual_columns) == columns,
                "Staircase sharpness or boundary control failed")
        records.append({"extra_middle_layers": extra, "dimension": dimension,
                        "joint_column_count": columns, "uniform_rank_upper": columns})
    return records


def target_controls():
    counts = {84: 0, 88: 0}
    margins = {84: 112, 88: 112}
    for b, c in product(range(111), repeat=2):
        total = b+c
        if not 137 <= total <= 144:
            continue
        threshold = 84 if total >= 141 else 88
        cap = CASES[threshold][0]-1
        require(224-total < threshold, "Strict source threshold failed")
        slack = 112-cap-(12+(b//11)*(c//11))
        require(slack > 0, "A supposedly excluded target pair survives")
        counts[threshold] += 1
        margins[threshold] = min(margins[threshold], slack)
    require(counts == {84: 314, 88: 330}, "Target interval census changed")
    return {"previous_long_sum_upper": 144, "new_long_sum_upper": 136,
            "excluded_pairs": sum(counts.values()),
            "rank84_interval_pairs": counts[84], "rank88_interval_pairs": counts[88],
            "minimum_rank84_margin": margins[84], "minimum_rank88_margin": margins[88],
            "boundary_control": {"balanced_ranks": [68, 68], "kernel_dimension": 64,
                                 "rank_upper": 88, "rank_budget": 88,
                                 "required_kernel_dimension": 64,
                                 "realized_compression_kernel": False,
                                 "target_constructed": False}}


def report():
    source, coherent = literal_bases()
    caps = []
    for threshold in CASES:
        document = json.loads(gzip.decompress((RESULT / f"rank{threshold}-minors.json.gz").read_bytes()))
        caps.append(verify_document(document, source, coherent))
    return {"proof_status": "proof-written-unreviewed", "independent_review": False,
            "lean_formalized": False, "improves_omega": False, "target_constructed": False,
            "literal_source_terms": 4096, "basis_factorizations": 112,
            "source_caps": caps, "staircase_controls": sharp_spaces(source),
            "target_controls": target_controls()}


def verify(record=None):
    check_sources()
    if record is None:
        record = json.loads((RESULT / "verification.json").read_text())
    require(record == report(), "Changed evidence or inflated scope")
    return record


if __name__ == "__main__":
    print(json.dumps(verify(), sort_keys=True))
