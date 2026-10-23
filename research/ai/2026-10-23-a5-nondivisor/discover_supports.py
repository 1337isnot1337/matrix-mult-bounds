"""Enumerate pair-admissible supports and search exact rank35 minor witnesses."""
from itertools import combinations
import json
from pathlib import Path
import random

from discover_graph import PRIME, VERTICES, matrix

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "results/a5-nondivisor-2026-10-23"


def supports(graph, size):
    def visit(allowed, chosen):
        if len(chosen) == size:
            yield chosen
            return
        while allowed.bit_count() >= size-len(chosen):
            bit = allowed & -allowed
            v = bit.bit_length()-1
            allowed ^= bit
            yield from visit(allowed & ~graph[v], chosen+[v])
    yield from visit((1 << 25)-1, [])


def minor_witness(rows):
    a = [row[:] for row in rows]
    order = list(range(45))
    columns = []
    rank = 0
    for col in range(45):
        pivot = next((i for i in range(rank, 45) if a[i][col] % PRIME), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        order[rank], order[pivot] = order[pivot], order[rank]
        inv = pow(a[rank][col] % PRIME, PRIME-2, PRIME)
        a[rank] = [v*inv % PRIME for v in a[rank]]
        for row in range(rank+1, 45):
            factor = a[row][col] % PRIME
            if factor:
                a[row] = [(x-factor*y) % PRIME for x, y in zip(a[row], a[rank])]
        columns.append(col)
        rank += 1
        if rank == 35:
            return {"rows": order[:35], "columns": columns}
    return None


def main():
    graph = json.loads((RESULT / "pair-graph-discovery.json").read_text())["bad_pair_graph"]
    for size in (13, 12, 11):
        candidates = list(supports(graph, size))
        records, unresolved = [], []
        print("size", size, "candidate_count", len(candidates), flush=True)
        for support in candidates:
            points = [VERTICES[v] for v in support]
            rng = random.Random(20261023+sum(1 << v for v in support))
            for attempt in range(8):
                coefficients = [1]*size if attempt == 0 else [rng.randrange(1, 8) for _ in support]
                witness = minor_witness(matrix(points, coefficients))
                if witness is not None:
                    records.append({"support": support, "coefficients": coefficients, **witness})
                    break
            else:
                unresolved.append(support)
            if (len(records)+len(unresolved)) % 100 == 0:
                print("processed", len(records)+len(unresolved), "unresolved", len(unresolved), flush=True)
        report = {"scope": "Finite discovery; minor replay and complete source proof pending.",
                  "prime": PRIME, "support_size": size, "candidate_count": len(candidates),
                  "witnesses": records, "unresolved_supports": unresolved, "improves_omega": False}
        (RESULT / f"support-{size}-discovery.json").write_text(json.dumps(report, indent=2)+"\n")
        print("completed", size, "witnesses", len(records), "unresolved", len(unresolved), flush=True)


if __name__ == "__main__":
    main()
