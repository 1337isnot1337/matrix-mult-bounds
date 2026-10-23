"""Exact controls for the all-C Koszul theorem; standard library only.

The proof, rather than these finite controls, establishes the theorem over C.
Literal modular ranks check conventions and are not characteristic-zero
upper bounds. Run from any directory; the report is written under results/.
The pilot module and its frozen report are local dependencies.
"""

from hashlib import sha256
from math import comb
from pathlib import Path
import json

from full_source_c_leg_pilot import rank_mod2


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS = ROOT / "results/mixed-longlegs-candidate-2026-10-23"


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def kernel_alternating(a, n, m, p):
    return sum(
        (-1) ** (j - a - 1)
        * choose(n + j - 1, j)
        * choose(m, p + 1 - j)
        * choose(j - 2, a - 1)
        for j in range(a + 1, p + 2)
    )


def rank_padded(a, n, m, p):
    m0 = n + a - 1
    d = m - m0
    assert d >= 0
    return sum(
        min(n * choose(m0, j), a * choose(m0, j + 1))
        * choose(d, p - j)
        for j in range(m0)
    )


def check_formula(a, n, m, p):
    domain = n * choose(m, p)
    codomain = a * choose(m, p + 1)
    kernel = kernel_alternating(a, n, m, p)
    rank = rank_padded(a, n, m, p)
    assert rank == domain - kernel, (a, n, m, p, rank, kernel)
    assert 0 <= rank <= min(domain, codomain)
    if p < a:
        assert kernel == 0
    if p >= m - n:
        assert rank == codomain
    if p == a:
        assert kernel == choose(n + a, a + 1)
    return {
        "a": a, "N": n, "M": m, "p": p,
        "domain": domain, "codomain": codomain,
        "rank": rank, "kernel": kernel, "cokernel": codomain - rank,
    }


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    grid_count = 0
    format_count = 0
    for a in range(2, 7):
        for n in range(1, 9):
            for d in range(6):
                m = n + a - 1 + d
                format_count += 1
                for p in range(m + 1):
                    check_formula(a, n, m, p)
                    grid_count += 1

    pilot_path = RESULTS / "full_source_c_leg_pilot.json"
    pilot = json.loads(pilot_path.read_text())
    literal_checks = []
    for row in pilot:
        fresh = rank_mod2(row["a"], row["widths"], row["p"])
        assert fresh == row
        formula = check_formula(row["a"], row["N"], row["M"], row["p"])
        assert fresh["rank_mod2"] == formula["rank"]
        literal_checks.append({
            "a": row["a"], "widths": row["widths"], "p": row["p"],
            "literal_mod2_rank": fresh["rank_mod2"],
            "formula_rank": formula["rank"],
        })
    assert len(literal_checks) == 97

    root_control_expected = [3, 27, 108, 237, 306, 237, 108, 27, 3]
    root_control = []
    for p, expected in enumerate(root_control_expected):
        literal = rank_mod2(3, [1, 1, 1], p)["rank_mod2"]
        formula = check_formula(3, 3, 9, p)["rank"]
        assert literal == formula == expected
        root_control.append(literal)

    candidate = [check_formula(5, 100, 140, p) for p in range(140)]
    assert candidate[5]["kernel"] == 1609344100
    assert candidate[5]["rank"] == 40087208700
    assert candidate[6]["kernel"] == 103457835000
    assert candidate[6]["rank"] == 834714603000
    assert all(row["kernel"] == 0 for row in candidate[:5])
    assert all(row["cokernel"] == 0 for row in candidate[40:])

    files = [
        "source_c_koszul.md",
        "verify_full_source_all_c.py",
        "full_source_c_leg_pilot.py",
    ]
    report = {
        "status": "all checks passed",
        "claim_scope": (
            "Written characteristic-zero proof with same-session audit; finite "
            "checks do not supply a proof, external review, construction, "
            "or an exponent improvement."
        ),
        "sources_sha256": {
            **{str((HERE / name).relative_to(ROOT)): digest(HERE / name) for name in files},
            str(pilot_path.relative_to(ROOT)): digest(pilot_path),
        },
        "formula_grid": {
            "a": [2, 6], "N": [1, 8], "unused_C_dimensions": [0, 5],
            "p": "0 through M inclusive (p=M is a zero-map endpoint control)",
            "formats": format_count, "degree_checks": grid_count,
            "checks": [
                "alternating kernel equals padded positive rank formula",
                "rank lies between zero and both matrix dimensions",
                "injective range p<a",
                "surjective range p>=M-N",
                "critical kernel at p=a",
            ],
        },
        "literal_mod2_scope": (
            "Exact modular convention checks, not characteristic-zero upper bounds"
        ),
        "literal_pilot_checks": literal_checks,
        "independent_root_control": {
            "a": 3, "widths": [1, 1, 1], "ranks": root_control,
        },
        "candidate": {
            "source": "10 Full(5,10)", "format": [5, 100, 140],
            "padded_comparator": "Full(5,100) with 36 unused C coordinates",
            "all_C_degrees_are_universal_maxima_by_written_proof": True,
            "includes_independent_invertible_source_first_identifications": True,
            "no_C_Koszul_obstruction_for_any_same_format_target": True,
            "degrees": candidate,
        },
    }
    out = RESULTS / "full_source_all_c_controls.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"],
        "grid_formats": format_count,
        "formula_degree_checks": grid_count,
        "literal_pilot_checks": len(literal_checks),
        "additional_literal_checks": len(root_control),
        "candidate_degrees": len(candidate),
        "report": str(out),
    }, indent=2))


if __name__ == "__main__":
    main()
