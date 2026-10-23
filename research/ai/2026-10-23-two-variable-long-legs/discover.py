"""Export deterministic finite map controls; acceptance imports none of this code."""
import json
from pathlib import Path
import random

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
RESULT = ROOT / "results/two-variable-long-legs-2026-10-23"


def case(name, n, m, bandwidth=0, prime=101, degree=1, mode="polynomial",
         lookup=False, eb=(), ec=()):
    rng = random.Random(20261023 + sum(map(ord, name)))
    ranks = degree + 1 if mode == "polynomial" else 2
    def stencil():
        return [[[rng.randrange(prime) for _ in range(2*bandwidth+1)]
                 for _ in range(m)] for _ in range(m)]
    profiles = [[1]*(n+m-1),
                [rng.randrange(prime) if lookup else z % prime
                 for z in range(n+m-1)]]
    return {"name": name, "n": n, "m": m, "D": bandwidth, "prime": prime,
            "b_mode": mode, "b_stencils": [stencil() for _ in range(ranks)],
            "b_roots": [2, 3] if mode == "exponential" else [],
            "c_profiles": profiles, "c_stencils": [stencil(), stencil()],
            "b_exceptions": list(eb), "c_exceptions": list(ec)}


if __name__ == "__main__":
    controls = [
        case("two-linear", 11, 5),
        case("lookup-band", 13, 5, bandwidth=1, lookup=True),
        case("exponential-exception", 14, 5, mode="exponential", lookup=True, eb=(7,)),
        case("characteristic-three", 11, 5, prime=3, lookup=True),
        case("characteristic-two", 11, 5, prime=2),
        case("quadratic-lookup", 14, 7, degree=2, lookup=True),
    ]
    record = {"cases": controls, "boundary": case("equality-boundary", 9, 4)}
    RESULT.mkdir(parents=True, exist_ok=True)
    (RESULT / "maps.json").write_text(json.dumps(record, indent=2) + "\n")
