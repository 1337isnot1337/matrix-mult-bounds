"""Finite modular lower ranks and exact independent sets for the A5 pair graph."""
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "results/a5-nondivisor-2026-10-23/pair-graph-discovery.json"
PRIME = 1009
VERTICES = [(i, z) for i in range(5) for z in range(5)]


def matrix(support, coefficients=None):
    values = dict(zip(support, coefficients or [1]*len(support)))
    return [[values.get((h-j, ell-r), 0)
             for h in range(9) for r in range(5)]
            for j in range(5) for ell in range(9)]


def rank_mod(rows):
    a = [row[:] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][col] % PRIME), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col] % PRIME, PRIME-2, PRIME)
        a[rank] = [v*inv % PRIME for v in a[rank]]
        for row in range(rank+1, len(a)):
            factor = a[row][col] % PRIME
            if factor:
                a[row] = [(x-factor*y) % PRIME for x, y in zip(a[row], a[rank])]
        rank += 1
    return rank


def maximum_independent_set(graph):
    @lru_cache(maxsize=200000)
    def search(allowed):
        if not allowed:
            return 0
        indices = [i for i in range(25) if allowed >> i & 1]
        v = max(indices, key=lambda i: (allowed & graph[i]).bit_count())
        remaining = allowed & ~(1 << v)
        take = (1 << v) | search(remaining & ~graph[v])
        leave = search(remaining)
        return take if take.bit_count() >= leave.bit_count() else leave
    return search((1 << 25)-1)


def main():
    graph = [0]*25
    ranks = []
    for a, b in combinations(range(25), 2):
        rank = rank_mod(matrix([VERTICES[a], VERTICES[b]]))
        ranks.append({"vertices": [a, b], "modular_rank": rank})
        if rank >= 35:
            graph[a] |= 1 << b
            graph[b] |= 1 << a
    witness = maximum_independent_set(graph)
    result = {"scope": "Finite pair-graph discovery; modular ranks are lower bounds over C.",
              "prime": PRIME, "vertices": VERTICES, "pair_ranks": ranks,
              "bad_pair_graph": graph, "independence_number": witness.bit_count(),
              "maximum_independent_set": [i for i in range(25) if witness >> i & 1],
              "improves_omega": False}
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"pair_count": len(ranks), "independence_number": witness.bit_count(),
                      "maximum_set": [VERTICES[i] for i in range(25) if witness >> i & 1]}))


if __name__ == "__main__":
    main()
