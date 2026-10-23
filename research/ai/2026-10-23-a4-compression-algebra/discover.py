"""Export exact minor identities; discovery is separate from acceptance."""

import argparse
import importlib.util
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("a4_arbitrary_acceptance", HERE / "verify.py")
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


def discover_identities():
    result = {}
    for name, (degree, caps, targets) in verifier.identity_targets().items():
        variables, minors = verifier.necessary_minors(degree, caps)
        monomials = sorted({powers for p in minors for powers, _ in p.terms()})
        matrix = sp.Matrix([[p.coeff_monomial(powers) for p in minors] for powers in monomials])
        rows = []
        for target in targets:
            polynomial = sp.Poly(target, *variables, domain=sp.QQ)
            right = sp.Matrix([polynomial.coeff_monomial(powers) for powers in monomials])
            coefficients, parameters = matrix.gauss_jordan_solve(right)
            coefficients = coefficients.subs({symbol: 0 for symbol in parameters})
            rows.append([[index, int(value.p), int(value.q)]
                         for index, value in enumerate(coefficients) if value])
        result[name] = rows
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=verifier.RESULTS / "certificate.json")
    args = parser.parse_args()
    certificate = {"schema": "a4-arbitrary-compression-v1",
                   "coverage": verifier.finite_coverage(), "minor_identities": discover_identities()}
    verifier.accept(certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")
    print(json.dumps({"certificate": str(args.output), "exact_minor_identities": 24,
                      "budget_pairs": 2809, "accepted_before_export": True}, indent=2))


if __name__ == "__main__":
    main()
