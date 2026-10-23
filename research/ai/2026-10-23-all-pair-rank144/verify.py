"""Exact finite controls for every balanced A4 leading-rank pair <=144."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT_DIR = ROOT / "results/all-pair-rank144-2026-10-23"
CERTIFICATES = RESULT_DIR / "certificates.json"
RESULT = RESULT_DIR / "controls.json"
SOURCE = tuple(product(range(4), range(7), range(4)))
MIDDLE_RANKS = (1, 2, 3, 4, 3, 2, 1)
SOURCE_PATHS = (
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-graded-quantum-flags/saturation.md",
    "research/ai/2026-10-23-torus-low-rank/proof.md",
    "research/ai/2026-10-23-torus-rank-frontier/proof.md",
    "research/ai/2026-10-23-torus-order-ideal/proof.md",
    "research/ai/2026-10-23-rank37-source-spaces/proof.md",
    "research/ai/2026-10-23-rank80-sharp-spaces/proof.md",
)
HEADER = {"schema": "a4-defect12-matching-certificates-v1", "field_of_application": "C",
          "source_layer": 0, "coherent_coordinate_order": "(i,s), 0<=i,s<4",
          "row_index": "7*j+L", "column_index": "4*H+r",
          "row_deletion_budget": 12, "column_deletion_budget": 12}
SOURCE_CAPS = ((24, 8), (37, 16), (48, 24), (64, 32), (80, 44))


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    entries = document["local_dependencies"]
    require(tuple(entry["path"] for entry in entries) == SOURCE_PATHS, "changed source inventory")
    for entry in entries:
        path = ROOT / entry["path"]
        require(path.is_file(), "missing source prerequisite")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"], "source digest mismatch")
    return {entry["path"]: entry["sha256"] for entry in entries}


def literal_source():
    slices = {coordinate: set() for coordinate in SOURCE}
    entries, cyclic = {}, set()
    for i, j, p, q, r, s in product(range(4), repeat=6):
        position = ((4 * j + p) * 7 + r + s, (4 * (i + j) + q) * 4 + r)
        require(position not in entries, "literal coefficient labels overlap")
        entries[position] = (i, p + q, s)
        slices[i, p + q, s].add(position)
        cyclic.add((28 * i + 4 * (p + q) + s, 28 * p + 4 * (r + s) + j,
                    28 * r + 4 * (i + j) + q))
    require(len(entries) == len(cyclic) == 4096, "literal source term count changed")
    require(all((b, c, a) in cyclic for a, b, c in cyclic), "cyclic source symmetry failed")
    return slices, entries


def decode(row, column):
    jp, ell = divmod(row, 7)
    j, p = divmod(jp, 4)
    hq, r = divmod(column, 4)
    h, q = divmod(hq, 4)
    return j, p, ell, h, q, r


def source_controls(slices, entries):
    for (i, k, s), support in slices.items():
        expected = 16 * MIDDLE_RANKS[k]
        require(len(support) == len({row for row, column in support})
                == len({column for row, column in support}) == expected,
                "monomial partial-permutation rank mismatch")
    first_weights = {i + 4 * k + 28 * s for i, k, s in SOURCE}
    second_weights = {i - 16 * k + 256 * s for i, k, s in SOURCE}
    row_weights = {-j - 16 * p + 256 * ell for j, p, ell in product(range(4), range(4), range(7))}
    column_weights = {h - 16 * q - 256 * r for h, q, r in product(range(7), range(4), range(4))}
    require(len(first_weights) == len(second_weights) == len(row_weights) == len(column_weights) == 112,
            "a required torus does not have simple weights")
    for (row, column), (i, k, s) in entries.items():
        j, p, ell, h, q, r = decode(row, column)
        require(-j + 4 * p + 28 * ell + h + 4 * q - 28 * r == i + 4 * k + 28 * s,
                "lowering torus identity failed")
        require(-j - 16 * p + 256 * ell + h - 16 * q - 256 * r == i - 16 * k + 256 * s,
                "simple matrix-leg torus identity failed")
    return {"literal_coefficients": len(entries), "cyclic_symmetry_coefficients": 4096,
            "monomial_slice_ranks": 112, "middle1_rank": 32,
            "first_torus_distinct_parameter_weights": 112,
            "second_torus_distinct_weights": {"parameters": 112, "rows": 112, "columns": 112},
            "torus_coefficient_identities": 8192}


def add_entry(matrix, position, value):
    new = matrix.get(position, 0) + value
    if new:
        matrix[position] = new
    else:
        matrix.pop(position, None)


def lowering_controls(slices):
    counts = Counter()
    for (i, k, s), support in slices.items():
        for direction in ("i", "k", "s"):
            actual = {}
            for row, column in support:
                j, p, ell, h, q, r = decode(row, column)
                if direction == "i":
                    if j < 3:
                        add_entry(actual, ((4 * (j + 1) + p) * 7 + ell, column), -(j + 1))
                    if h > 0:
                        add_entry(actual, (row, (4 * (h - 1) + q) * 4 + r), h)
                elif direction == "k":
                    if p > 0:
                        add_entry(actual, ((4 * j + p - 1) * 7 + ell, column), 4 - p)
                    if q > 0:
                        add_entry(actual, (row, (4 * h + q - 1) * 4 + r), 4 - q)
                else:
                    if ell > 0:
                        add_entry(actual, ((4 * j + p) * 7 + ell - 1, column), ell)
                    if r < 3:
                        add_entry(actual, (row, (4 * h + q) * 4 + r + 1), -(r + 1))
            if direction == "i" and i > 0:
                target, scale = (i - 1, k, s), i
            elif direction == "k" and k > 0:
                target, scale = (i, k - 1, s), 7 - k
            elif direction == "s" and s > 0:
                target, scale = (i, k, s - 1), s
            else:
                target, scale = None, 0
            expected = {position: scale for position in slices[target]} if target else {}
            require(actual == expected, "integer lowering equivariance failed")
            counts[direction] += 1
    require(sum(counts.values()) == 336, "incomplete lowering coverage")
    return {"basis_identities": 336, "identities_per_direction": dict(counts),
            "field_for_exponentiation": "C"}


def short_ideals(volume=10):
    result, selected = [], []

    def visit(remaining):
        if len(selected) == 4:
            if remaining == 0:
                result.append(tuple(selected))
            return
        for height in range(min(selected[-1] if selected else 4, remaining) + 1):
            if remaining - height > 4 * (3 - len(selected)):
                continue
            selected.append(height)
            visit(remaining - height)
            selected.pop()

    visit(volume)
    return tuple(result)


def literal_graph(shape, slices):
    edges = {(7 * j + r + s, 4 * (i + j) + r)
             for i, j, r, s in product(range(4), repeat=4) if s < shape[i]}
    source_edges = set().union(*(slices[i, 0, s] for i in range(4) for s in range(shape[i])))
    embedded = {((row // 7) * 28 + row % 7, (column // 4) * 16 + column % 4)
                for row, column in edges}
    require(embedded == source_edges and len(edges) == 160, "coherent graph differs from literal source")
    return edges


def parse_edge(value, edges):
    require(type(value) is list and len(value) == 2
            and all(type(index) is int and 0 <= index < 28 for index in value), "invalid graph edge")
    edge = tuple(value)
    require(edge in edges, "edge is absent from the literal source graph")
    return edge


def replay_record(record, slices):
    require(set(record) == {"shape", "matching", "forced_cover"}, "changed matching record fields")
    shape = tuple(record["shape"])
    require(shape in short_ideals(), "invalid size10 ideal")
    edges = literal_graph(shape, slices)
    matching = [parse_edge(edge, edges) for edge in record["matching"]]
    require(len(matching) in (24, 28), "unexpected matching size")
    row_match = {row: index for index, (row, column) in enumerate(matching)}
    column_match = {column: index for index, (row, column) in enumerate(matching)}
    require(len(row_match) == len(column_match) == len(matching), "matching endpoints are not disjoint")
    if len(matching) == 28:
        require(record["forced_cover"] is None, "unneeded forced-cover certificate")
        return "large_matching", 28, 0
    forcing = record["forced_cover"]
    require(type(forcing) is dict and set(forcing) == {"side", "steps"}, "missing forced-cover fields")
    side = forcing["side"]
    require(side in ("rows", "columns"), "invalid forced side")
    forced = set()
    for step in forcing["steps"]:
        require(set(step) == {"matching_index", "forcing_edge"}, "changed forcing-step fields")
        index = step["matching_index"]
        require(type(index) is int and 0 <= index < 24 and index not in forced,
                "invalid or repeated forcing index")
        row, column = parse_edge(step["forcing_edge"], edges)
        if side == "rows":
            require(row == matching[index][0], "forcing edge does not meet its claimed row")
            require(column not in column_match or column_match[column] in forced,
                    "forcing step has no prior unselected column")
        else:
            require(column == matching[index][1], "forcing edge does not meet its claimed column")
            require(row not in row_match or row_match[row] in forced,
                    "forcing step has no prior unselected row")
        forced.add(index)
    require(len(forced) == 24, "incomplete one-sided forcing certificate")
    selected = set(row_match) if side == "rows" else set(column_match)
    require(all((row if side == "rows" else column) in selected for row, column in edges),
            "forced vertices do not cover the graph")
    return side, 24, 24


def replay_certificates(document=None, slices=None):
    if document is None:
        document = json.loads(CERTIFICATES.read_text())
    require(set(document) == set(HEADER) | {"size10_ideals"}, "changed certificate fields")
    require(all(document[key] == value for key, value in HEADER.items()), "changed certificate header")
    if slices is None:
        slices, _ = literal_source()
    expected = set(short_ideals())
    require(len(expected) == 7, "size10 ideal inventory changed")
    seen, categories, matching_edges, forcing_steps = set(), Counter(), 0, 0
    for record in document["size10_ideals"]:
        shape = tuple(record["shape"])
        require(shape in expected and shape not in seen, "invalid or duplicate ideal coverage")
        seen.add(shape)
        category, edges, steps = replay_record(record, slices)
        categories[category] += 1
        matching_edges += edges
        forcing_steps += steps
    require(seen == expected, "incomplete size10 ideal coverage")
    require(categories == {"large_matching": 3, "rows": 2, "columns": 2}, "graph certificate census changed")
    return {"complete_size10_ideals": 7, "literal_graph_edges_checked": 1120,
            "disjoint_matching_edges": matching_edges, "forcing_steps": forcing_steps,
            "matching_sizes": [len(record["matching"]) for record in document["size10_ideals"]],
            "categories": dict(categories), "row_and_column_budgets": [12, 12],
            "compression_kernel_dimension_upper": 9, "acceptance_uses_matching_search": False}


def source_cap(rank_ceiling):
    require(type(rank_ceiling) is int and rank_ceiling >= 0, "invalid source rank ceiling")
    for threshold, bound in SOURCE_CAPS:
        if rank_ceiling < threshold:
            return bound
    return 112


def pair_screen(a, b, kind, use_compression=True):
    require(kind in ("mixed", "long"), "unknown target pair")
    maximum_a = 100 if kind == "mixed" else 101
    require(type(a) is int and type(b) is int and 0 <= a <= maximum_a and 0 <= b <= 101,
            "rank lies outside the individually established bounds")
    shared, parameter_dimension = (10, 110) if kind == "mixed" else (11, 100)
    delta = 224 - a - b
    lower = parameter_dimension - (a // shared) * (b // shared)
    upper = source_cap(delta)
    special = use_compression and kind == "mixed" and a == b == 100
    if special:
        upper = min(upper, 9)
    return {"ranks": [a, b], "kind": kind, "source_rank_ceiling": delta,
            "kernel_lower": lower, "kernel_upper": upper,
            "uses_defect12_compression": special, "excluded": lower > upper}


def rank_pair_controls():
    mixed = [pair_screen(a, b, "mixed") for a in range(101) for b in range(102)]
    long = [pair_screen(a, b, "long") for a in range(102) for b in range(102)]
    high_mixed = [record for record in mixed if sum(record["ranks"]) > 144]
    high_long = [record for record in long if sum(record["ranks"]) > 144]
    require(all(record["excluded"] for record in high_mixed + high_long), "universal sum144 screen failed")
    before_special = [record["ranks"] for record in high_mixed
                      if not pair_screen(*record["ranks"], "mixed", use_compression=False)["excluded"]]
    require(before_special == [[100, 100]], "exceptional mixed-pair inventory changed")
    ranges = ((201, 202), (188, 200), (177, 187), (161, 176), (145, 160))
    margins = []
    for lower_sum, upper_sum in ranges:
        for kind, records in (("mixed", high_mixed), ("long", high_long)):
            group = [record for record in records if lower_sum <= sum(record["ranks"]) <= upper_sum
                     and not record["uses_defect12_compression"]]
            margins.append({"kind": kind, "sum_interval": [lower_sum, upper_sum],
                            "cases": len(group), "kernel_lower_minimum": min(record["kernel_lower"] for record in group),
                            "kernel_upper_maximum": max(record["kernel_upper"] for record in group)})
    boundary = [pair_screen(72, 72, "long"), pair_screen(72, 72, "mixed"), pair_screen(100, 44, "mixed")]
    require(all(not record["excluded"] for record in boundary), "strict rank80 boundary was improperly closed")
    require(2 * 216 == 3 * 144 and 100 + 44 == 144, "rank-sum consequence arithmetic failed")
    return {"mixed_rank_pairs_checked": len(mixed), "long_rank_pairs_checked": len(long),
            "mixed_pairs_above144_excluded": len(high_mixed), "long_pairs_above144_excluded": len(high_long),
            "before_compression_exception": before_special, "special_case": pair_screen(100, 100, "mixed"),
            "interval_margins": margins, "boundary_controls": boundary,
            "boundary_controls_are_constructions": False, "every_pair_sum_upper": 144,
            "all_three_rank_sum_upper": 216, "short_rank100_long_rank_upper": 44}


def controls():
    pins = check_sources()
    slices, entries = literal_source()
    return {"schema": "all-pair-rank144-controls-v1", "source_pins": pins,
            "source_controls": source_controls(slices, entries),
            "lowering_controls": lowering_controls(slices),
            "compression_controls": replay_certificates(slices=slices),
            "rank_pair_controls": rank_pair_controls(),
            "certificate_sha256": hashlib.sha256(CERTIFICATES.read_bytes()).hexdigest(),
            "claim_scope": {"claim_id": "AI-A4-ALL-PAIR-RANK144-001", "field": "C",
                            "arbitrary_complex_leading_kernels": True, "arbitrary_finite_Laurent_poles": True,
                            "every_balanced_pair_sum_upper": 144, "total_balanced_rank_upper": 216,
                            "short_rank100_long_rank_upper": 44,
                            "necessary_conditions_only": True, "leading_rank_bounds_sharp": False,
                            "matrix_target_constructed": False, "smaller_exponent_established": False,
                            "independent_external_review": False, "formalized": False}}


def replay_saved(document):
    require(document == controls(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = controls()
    if args.write:
        RESULT_DIR.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report, indent=2) + "\n")
    else:
        require(json.loads(RESULT.read_text()) == report, "saved evidence or scope differs from exact replay")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
