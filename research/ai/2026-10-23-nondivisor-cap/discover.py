"""Bounded modular discovery on all size11 Ferrers ideals of the A5 grid."""
from itertools import product
import json
from pathlib import Path
from random import Random

ROOT = Path(__file__).resolve().parents[3]


def ideals(a, size, previous=None):
    if a == 0:
        if size == 0:
            yield ()
        return
    maximum = 5 if previous is None else previous
    for first in range(min(maximum, size), -1, -1):
        for rest in ideals(a-1, size-first, first):
            yield (first,)+rest


def biform(coefficients, a=5):
    m = 2*a-1
    return [[coefficients.get((height-j, ell-r), 0)
             for height, r in product(range(m), range(a))]
            for j, ell in product(range(a), range(m))]


def modular_rank(matrix, prime=1009):
    work = [[x % prime for x in row] for row in matrix]
    pivots = 0
    for column in range(len(work[0])):
        row = next((i for i in range(pivots, len(work)) if work[i][column]), None)
        if row is None:
            continue
        work[pivots], work[row] = work[row], work[pivots]
        factor = pow(work[pivots][column], -1, prime)
        work[pivots] = [(x*factor) % prime for x in work[pivots]]
        for i in range(pivots+1, len(work)):
            factor = work[i][column]
            if factor:
                work[i] = [(x-factor*y) % prime for x, y in zip(work[i], work[pivots])]
        pivots += 1
    return pivots


def main():
    rng = Random(20261023)
    records = []
    for shape in ideals(5, 11):
        positions = [(i, j) for i, length in enumerate(shape) for j in range(length)]
        best_rank, best = -1, None
        tried = 0
        for _ in range(16):
            coeff = {position: rng.randrange(-3, 4) for position in positions}
            rank = modular_rank(biform(coeff))
            tried += 1
            if rank > best_rank:
                best_rank, best = rank, coeff
            if rank >= 35:
                break
        records.append({"shape": shape, "best_modular_rank": best_rank,
                        "attempts": tried,
                        "coefficients": [[i, j, value] for (i, j), value in best.items()]})
    report = {"scope": "Bounded discovery only; no unverified upper ranks or cap theorem.",
              "prime": 1009, "seed": 20261023, "ideal_dimension": 11,
              "records": records}
    destination = ROOT / "results/local/nondivisor-cap/discovery.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"ideals": len(records),
                      "witnessed_rank_at_least35": sum(r["best_modular_rank"] >= 35 for r in records),
                      "unresolved_shapes": [r["shape"] for r in records if r["best_modular_rank"] < 35]}))


if __name__ == "__main__":
    main()
