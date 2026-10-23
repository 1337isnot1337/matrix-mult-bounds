#!/usr/bin/env python3
"""Independent set-based acceptance of the exact aggregation certificate.

This verifier does not import the bit-mask discovery program.  The complete
ordered-triple check establishes the finite combinatorial hypotheses of
proof.md; the uniform tensor identity is proved there.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
import json
import hashlib
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def check_family(data: dict) -> dict:
    d = data["coordinate_count"]
    n = data["part_size"]
    if not isinstance(d, int) or not isinstance(n, int) or d != 3 * n or n <= 0:
        raise ValueError("Expected three positive equally sized coordinate parts")
    universe = frozenset(range(d))
    triples = []
    for row in data["products"]:
        parts = []
        for label in ("U", "V", "W"):
            values = row[label]
            if len(values) != n or len(set(values)) != n:
                raise ValueError("Every coordinate part must have distinct entries and the stated size")
            if any(type(value) is not int for value in values):
                raise ValueError("Coordinate labels must be integers")
            parts.append(frozenset(values))
        u, v, w = parts
        if u | v | w != universe or u & v or u & w or v & w:
            raise ValueError("Each product must be an ordered partition of the coordinate universe")
        triples.append(tuple(parts))
    if not triples:
        raise ValueError("Empty product family")
    for leg in range(3):
        if len({row[leg] for row in triples}) != len(triples):
            raise ValueError("Repeated coordinate part creates an off-diagonal compatible triple")

    corrections = []
    for values in data["correction_subsets"]:
        subset = frozenset(values)
        if len(subset) != len(values) or not subset or not subset <= universe:
            raise ValueError("Invalid correction subset")
        corrections.append(subset)
    if len(set(corrections)) != len(corrections):
        raise ValueError("Duplicate correction subset")
    corrections = frozenset(corrections)
    replicated = Counter()
    centered_killed = 0
    coefficient_checks = 0
    for i, j, k in product(range(len(triples)), repeat=3):
        selected = (triples[i][0], triples[j][1], triples[k][2])
        multiplicities = [sum(r in part for part in selected) for r in universe]
        if i == j == k:
            if any(value != 1 for value in multiplicities):
                raise ValueError("Diagonal is not a matrix product")
            continue
        if all(value == 1 for value in multiplicities):
            raise ValueError(f"Off-diagonal compatible triple {(i, j, k)}")
        if 2 in multiplicities:
            centered_killed += 1
            continue
        common = selected[0] & selected[1] & selected[2]
        if not common:
            raise ValueError("A centered survivor has no replicated coordinate")
        replicated[common] += 1
        coefficient = 1 + sum((-1) ** len(p) for p in corrections if p <= common)
        if coefficient:
            raise ValueError(f"Uncancelled replicated triple {(i, j, k)}: {coefficient}")
        coefficient_checks += 1

    # Check the supplied list is precisely the downward closure used in the proof.
    required = set()
    for common in replicated:
        for flags in product((False, True), repeat=len(common)):
            subset = frozenset(r for r, keep in zip(sorted(common), flags) if keep)
            if subset:
                required.add(subset)
    if corrections != required:
        raise ValueError("Correction list differs from the exact nonempty downward closure")
    counts = Counter(map(len, corrections))
    polynomial = {str(d): 1}
    for size, count in counts.items():
        polynomial[str(d - size)] = count
    if polynomial != data["rank_polynomial_coefficients"]:
        raise ValueError("Advertised multiplication count disagrees with the actual corrections")
    m = len(triples)
    return {
        "accepted": True,
        "coordinate_count": d,
        "part_size": n,
        "products": m,
        "ordered_mixed_triples": m ** 3,
        "diagonal_triples": m,
        "off_diagonal_compatible_triples": 0,
        "off_diagonal_terms_killed_by_centering": centered_killed,
        "off_diagonal_terms_killed_by_corrections": coefficient_checks,
        "distinct_replicated_coordinate_sets": len(replicated),
        "correction_counts_by_size": dict(sorted(counts.items())),
        "rank_polynomial_coefficients": dict(sorted(polynomial.items(), reverse=True)),
        "independent_mathematical_review": False,
        "improves_omega": False,
    }


def check_source_hash(path: Path) -> dict:
    """Require exact bytes of the versioned external comparison witness."""
    sources = json.loads((HERE / "sources.json").read_text())
    source = next(item for item in sources["ancillary_sources"] if item["id"] == "ex28")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != source["sha256"]:
        raise ValueError("External baseline source SHA256 does not match the pinned version")
    return {"source_id": source["id"], "url": source["url"], "sha256": actual, "verified": True}


def baseline_data(path: Path) -> dict:
    """Read the hash-verified external seed only to replay its comparison cost."""
    check_source_hash(path)
    rows = []
    for line in path.read_text().splitlines():
        if re.match(r"^\d+\s*\|", line):
            parts = [list(map(int, re.findall(r"\d+", s))) for s in re.findall(r"\{([^}]*)\}", line)]
            if len(parts) != 3:
                raise ValueError("Unexpected external seed row")
            rows.append(dict(zip(("U", "V", "W"), parts)))
    d = 1 + max(value for row in rows for part in row.values() for value in part)
    common_sets = set()
    for x, y, z in product(rows, repeat=3):
        u, v, w = map(set, (x["U"], y["V"], z["W"]))
        if any(sum(r in part for part in (u, v, w)) == 2 for r in range(d)):
            continue
        common = u & v & w
        for flags in product((False, True), repeat=len(common)):
            part = frozenset(r for r, keep in zip(sorted(common), flags) if keep)
            if part:
                common_sets.add(part)
    counts = Counter(map(len, common_sets))
    polynomial = {str(d): 1, **{str(d - size): count for size, count in counts.items()}}
    return {"coordinate_count": d, "part_size": d // 3, "products": rows,
            "correction_subsets": [sorted(p) for p in common_sets],
            "rank_polynomial_coefficients": polynomial}


def comparison(new: dict, old: dict) -> dict:
    """Exact coefficient proof of a strictly lower cost per output for x>0."""
    m, old_m = len(new["products"]), len(old["products"])
    a, b = new["rank_polynomial_coefficients"], old["rank_polynomial_coefficients"]
    delta = {power: m * b.get(power, 0) - old_m * a.get(power, 0)
             for power in set(a) | set(b)}
    if not delta or any(value < 0 for value in delta.values()) or not any(delta.values()):
        raise ValueError("The claimed positive-coefficient cost comparison does not hold")
    return {"identity": f"{m}*external_rank_bound - {old_m}*new_rank_bound",
            "positive_coefficients": dict(sorted(delta.items(), reverse=True)),
            "strictly_positive_for_x_positive": True}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", nargs="?", type=Path, default=HERE / "witness_29.json")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--export-seed", type=Path, help="Export the external baseline as masks for discovery")
    args = parser.parse_args()
    data = json.loads(args.witness.read_text())
    old = baseline_data(HERE / "baseline_ex28.txt")
    report = {"source_integrity": check_source_hash(HERE / "baseline_ex28.txt"),
              "new_witness": check_family(data), "external_baseline": check_family(old),
              "cost_comparison": comparison(data, old)}
    if args.export_seed:
        lines = [f"{old['coordinate_count']} {len(old['products'])}"]
        lines.extend(" ".join(str(sum(1 << value for value in row[key])) for key in ("U", "V", "W"))
                     for row in old["products"])
        args.export_seed.parent.mkdir(parents=True, exist_ok=True)
        args.export_seed.write_text("\n".join(lines) + "\n")
    result = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    print(result, end="")


if __name__ == "__main__":
    main()
