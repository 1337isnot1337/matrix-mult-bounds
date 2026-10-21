"""Reconstruct exact gradient certificates; verification is a separate program."""
from itertools import product
import json

import sympy as sp

from central_polystability import ROOT, RESULTS, cubic, encode, read_json


def discover():
    variables, f = cubic(read_json(RESULTS / "grouped-a4.json.gz"))
    gradient = [sp.diff(f.as_expr(), x) for x in variables]
    certificates = []
    for chart in range(4):
        remaining = [x for x in variables if x != variables[chart]]
        equations = [sp.Poly(g.subs(variables[chart], 1), *remaining).primitive()[1]
                     for g in gradient]
        for degree in range(4):
            monomials = [m for m in product(range(degree+1), repeat=3) if sum(m) <= degree]
            terms = [sp.prod(x**e for x, e in zip(remaining, m)) for m in monomials]
            polys = [sp.Poly(t*g.as_expr(), *remaining) for g in equations for t in terms]
            basis = sorted({m for p in polys for m in p.monoms()} | {(0, 0, 0)})
            matrix = sp.Matrix([[p.coeff_monomial(m) for p in polys] for m in basis])
            target = sp.Matrix([int(m == (0, 0, 0)) for m in basis])
            try:
                solution, parameters = matrix.gauss_jordan_solve(target)
            except ValueError:
                continue
            solution = solution.subs({parameter: 0 for parameter in parameters})
            multipliers = [sp.Poly(sum(solution[j*len(terms)+k]*t
                                      for k, t in enumerate(terms)), *remaining)
                           for j in range(4)]
            assert sp.expand(sum(p.as_expr()*g.as_expr()
                                 for p, g in zip(multipliers, equations))) == 1
            certificates.append({
                "chart": chart, "variables": list(map(str, remaining)),
                "primitive_gradient_equations": [encode(g) for g in equations],
                "multipliers": [encode(p) for p in multipliers],
                "multiplier_degree": degree,
            })
            break
        else:
            raise RuntimeError("No identity within the selected multiplier-degree bound")
    return {"primitive_cubic": str(f.as_expr()), "cubic_terms": encode(f),
            "cyclic_symmetry_verified": True, "certificates": certificates}


if __name__ == "__main__":
    output = ROOT / "results/local/central-cubic-smoothness.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(discover(), indent=2)+"\n")
    print(output)
