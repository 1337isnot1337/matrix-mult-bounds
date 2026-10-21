"""Exact finite certificates used by the central-block polystability proof."""
from itertools import product
import json
from pathlib import Path

import sympy as sp

from coefficients import read_json

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/cyclic-recoupling-2026-10-20"


def cubic(grouped):
    block = next(b for b in grouped["blocks"] if b["degrees"] == [6, 6, 6])
    assert block["multiplicity_dimensions"] == [4, 4, 4]
    tensor = {(i, j, k): (-1)**i*sp.Rational(v)
              for i, j, k, v in block["multiplicity_terms"]}
    for i, j, k in product(range(4), repeat=3):
        assert tensor.get((i, j, k), 0) == tensor.get((j, k, i), 0)
    variables = sp.symbols("x0:4")
    f = sum(v*variables[i]*variables[j]*variables[k]
            for (i, j, k), v in tensor.items())
    primitive = sp.Poly(f, *variables).clear_denoms()[1].primitive()[1]
    return variables, primitive


def encode(poly):
    return [[list(monomial), str(value)] for monomial, value in poly.terms()]


def decode(terms, variables):
    return sum(sp.Rational(value)*sp.prod(x**e for x, e in zip(variables, monomial))
               for monomial, value in terms)


def verify(grouped, certificate):
    variables, f = cubic(grouped)
    assert encode(f) == certificate["cubic_terms"]
    assert certificate["cyclic_symmetry_verified"]
    gradient = [sp.diff(f.as_expr(), x) for x in variables]
    assert [chart["chart"] for chart in certificate["certificates"]] == list(range(4))
    counts = []
    for chart in certificate["certificates"]:
        index = chart["chart"]
        remaining = [x for x in variables if x != variables[index]]
        assert list(map(str, remaining)) == chart["variables"]
        equations = [sp.Poly(g.subs(variables[index], 1), *remaining).primitive()[1]
                     for g in gradient]
        assert [encode(g) for g in equations] == chart["primitive_gradient_equations"]
        assert len(chart["multipliers"]) == 4
        multipliers = [decode(terms, remaining) for terms in chart["multipliers"]]
        identity = sp.expand(sum(p*g.as_expr() for p, g in zip(multipliers, equations)))
        assert identity == 1
        counts.append(sum(len(terms) for terms in chart["multipliers"]))
    return {
        "representation_degrees": [6, 6, 6],
        "multiplicity_dimensions": [4, 4, 4],
        "first_leg_diagonal_change": [1, -1, 1, -1],
        "cyclic_symmetry_verified": True,
        "primitive_cubic": str(f.as_expr()),
        "affine_charts_checked": 4,
        "nullstellensatz_identities_verified": 4,
        "multiplier_nonzero_terms_by_chart": counts,
        "smooth_projective_cubic_certified": True,
        "polystability_status": "written proof using external stability theorems",
        "general_complex_degeneration_to_M2": "excluded by the written proof",
        "independent_mathematical_review": False,
        "lean_formalized": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    data = read_json(RESULTS / "grouped-a4.json.gz")
    certificate = json.loads((RESULTS / "central-cubic-smoothness.json").read_text())
    print(json.dumps(verify(data, certificate), indent=2))
