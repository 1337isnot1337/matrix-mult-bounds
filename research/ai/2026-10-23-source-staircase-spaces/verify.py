"""Exact literal support replay for the all-size staircase source spaces."""

from __future__ import annotations

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULT = ROOT / "results/source-staircase-spaces-2026-10-23/controls.json"
SOURCE_PATHS = ("research/ai/2026-10-20-koszul/cyclic_finite_target.md",
                "research/ai/2026-10-23-torus-rank80/proof.md")


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def check_sources(document=None):
    if document is None:
        document = json.loads((HERE / "sources.json").read_text())
    entries = document["local_dependencies"]
    require(tuple(item["path"] for item in entries) == SOURCE_PATHS, "changed source inventory")
    for item in entries:
        path = ROOT / item["path"]
        require(path.is_file(), "missing source prerequisite")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], "source digest mismatch")
    return {item["path"]: item["sha256"] for item in entries}


def literal_columns(a):
    require(type(a) is int and a >= 2, "invalid source size")
    columns = {coordinate: set() for coordinate in product(range(a), range(2 * a - 1), range(a))}
    seen = set()
    for i, j, p, q, r, s in product(range(a), repeat=6):
        row = (a * j + p) * (2 * a - 1) + r + s
        column = (a * (i + j) + q) * a + r
        require((row, column) not in seen, "overlapping literal coefficient labels")
        seen.add((row, column))
        columns[i, p + q, s].add(column)
    require(len(seen) == a ** 6 and all(columns.values()), "incomplete literal source")
    return columns


def family(a, d, m, columns=None):
    require(type(a) is int and a >= 2 and type(d) is int and 1 <= d < a
            and type(m) is int and 0 <= m <= 2 * a - 1, "invalid staircase parameters")
    if columns is None:
        columns = literal_columns(a)
    coordinates = [coordinate for coordinate in columns
                   if coordinate[0] < d or (coordinate[0] == d and coordinate[1] < m)]
    actual = set().union(*(columns[coordinate] for coordinate in coordinates))
    expected = {(a * h + q) * a + r
                for h, q, r in product(range(2 * a - 1), range(a), range(a))
                if h < a + d - 1 or (h == a + d - 1 and q < min(m, a))}
    require(actual == expected, "literal joint column support differs from the formula")
    dimension = a * (d * (2 * a - 1) + m)
    bound = a * a * (a + d - 1) + a * min(m, a)
    require(len(coordinates) == dimension and len(actual) == bound, "family dimension or support count changed")
    return {"a": a, "d": d, "m": m, "dimension": dimension,
            "supported_columns": bound, "uniform_rank_upper": bound}


def replay_counterexample(record):
    require(set(record) == {"coordinate_mask", "dimension", "uniform_rank_upper", "strict_rank_threshold",
                            "disproved_dimension_upper"}, "changed counterexample fields")
    value = record["coordinate_mask"]
    require(type(value) is str, "invalid coordinate mask")
    try:
        mask = int(value, 16)
    except ValueError as error:
        raise ArithmeticError("invalid coordinate mask") from error
    require(0 <= mask < 1 << 112 and value == hex(mask), "invalid coordinate mask")
    columns = literal_columns(4)
    coordinates = list(columns)
    selected = [coordinate for index, coordinate in enumerate(coordinates) if (mask >> index) & 1]
    actual = set().union(*(columns[coordinate] for coordinate in selected)) if selected else set()
    require(len(selected) == record["dimension"] == 68, "counterexample dimension changed")
    require(len(actual) == record["uniform_rank_upper"] == 92, "counterexample column support changed")
    require(record["strict_rank_threshold"] == 96 and record["disproved_dimension_upper"] == 57,
            "counterexample scope changed")
    require(mask == (1 << 68) - 1, "counterexample is not the stated staircase")
    require(len(actual) < record["strict_rank_threshold"]
            and len(selected) > record["disproved_dimension_upper"], "counterexample inequalities failed")


def report():
    records = []
    for a in range(2, 7):
        columns = literal_columns(a)
        for d in range(1, a):
            for m in range(2 * a):
                records.append(family(a, d, m, columns))
    require(len(records) == 140, "finite family inventory changed")
    counter = {"coordinate_mask": hex((1 << 68) - 1), "dimension": 68,
               "uniform_rank_upper": 92, "strict_rank_threshold": 96, "disproved_dimension_upper": 57}
    replay_counterexample(counter)
    return {"schema": "source-staircase-spaces-v1", "field": "C",
            "source_sha256": check_sources(),
            "coverage": {"source_sizes": [2, 3, 4, 5, 6], "parameter_triples": len(records),
                         "literal_terms_reconstructed": sum(a ** 6 for a in range(2, 7)),
                         "all_dimensions_and_exact_column_supports_checked": True,
                         "records_sha256": hashlib.sha256(json.dumps(records, sort_keys=True).encode()).hexdigest()},
            "a4_table": [family(4, 2, m) for m in range(4)],
            "a4_counterexample": counter,
            "boundary_control": {**family(4, 2, 4), "column_count_proves_rank_below_96": False},
            "claim_scope": {"all_size_supported_column_construction": True,
                            "rank96_dimension57_cap_disproved": True,
                            "blocks_every_source_cap_refinement": False,
                            "rank_upper_attainment_claimed": False,
                            "target_kernel_realization_claimed": False, "target_constructed": False,
                            "improves_omega": False, "independent_review": False,
                            "proof_status": "proof-written-unreviewed"}}


def replay_saved(document):
    require(document["schema"] == "source-staircase-spaces-v1", "unknown evidence schema")
    replay_counterexample(document["a4_counterexample"])
    require(document == report(), "saved evidence or scope differs from exact replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2) + "\n")
    replay_saved(json.loads(RESULT.read_text()))
    print("PASS: all140 staircase cases for a2..6 and the68-dimensional A4 counterexample with92 supported columns.")
    print("The proposed universal cap57 below rank96 is false; more selective source-cap and kernel arguments remain open.")


if __name__ == "__main__":
    main()
