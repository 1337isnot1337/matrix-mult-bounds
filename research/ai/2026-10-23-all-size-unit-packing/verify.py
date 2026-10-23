"""Exact finite checks supporting the all-size polynomial unit proof."""
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/all-size-unit-packing-2026-10-23/controls.json"
CAP = ROOT / "research/ai/2026-10-23-source-singular-space-cap"
SPEC = importlib.util.spec_from_file_location("all_size_packing_predecessor", CAP / "verify.py")
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
require = prior.require


def check_sources(record=None):
    record = json.loads((PACKAGE / "sources.json").read_text()) if record is None else record
    expected = {"research/ai/2026-10-23-source-singular-space-cap/proof.md",
                "research/ai/2026-10-23-source-singular-space-cap/verify.py",
                "research/ai/2026-10-21-cyclic-slice-determinants/certify.py"}
    entries = record["local_dependencies"]
    require(len(entries) == 3 and {x["path"] for x in entries} == expected,
            "Changed source inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest() == entry["sha256"],
                "Changed source: " + entry["path"])
    return len(entries)


def short_matrix(a, c):
    require(type(a) is int and a >= 1 and type(c) is int and 0 <= c < a,
            "Invalid size or short residue")
    return s.Matrix([[int(0 <= h-j < a and 0 <= ell-r < a
                           and (h-j+ell-r) % a == c)
                      for h, r in product(range(2*a-1), range(a))]
                     for j, ell in product(range(a), range(2*a-1))])


def recurrence(a, c):
    """Check every coefficient of the formal linear identity in independent U's."""
    y = s.Symbol("y")
    u = s.symbols("u:" + str(2*a-1))
    f = [y**((c-i) % a) for i in range(a)]
    equations = [sum(f[i]*u[j+i] for i in range(a)) for j in range(a)]
    for j in range(a-1):
        if c == a-1:
            rhs = y**a*u[j]-u[j+a]
        else:
            rhs = y**(c+1)*(u[j]-u[j+a])+(y**a-1)*u[j+c+1]
        require(s.expand(y*equations[j]-equations[j+1]-rhs) == 0,
                "Formal kernel recurrence identity failed")
    require(f[c] == 1, "Terminal surviving coordinate lost its unit coefficient")
    require(s.gcd(y**(c+1), y**a-1) == 1, "Polynomial divisibility hypothesis failed")
    return {"size": a, "residue": c, "formal_successive_identities": a-1,
            "terminal_unit_coefficient": 1, "coprime_polynomial_pair": True}


def packing(a):
    n = a*a*(2*a-1)
    coordinates = list(product(range(a), range(2*a-1), range(a)))
    groups = {(c, d): [] for c, d in product(range(a), repeat=2)}
    for i, k, z in coordinates:
        groups[(i+z) % a, k % a].append((i, k, z))
    require(sum(map(len, groups.values())) == n and all(groups.values()),
            "Disjoint packing inventory failed")
    weights = [i+a*k+a*(2*a-1)*z for i, k, z in coordinates]
    require(sorted(weights) == list(range(n)), "All-size source weights not distinct")
    kernel_constraints = {(i, k, 0) for i, k in product(range(a), repeat=2)}
    require(len(kernel_constraints) == a*a and
            all(len(kernel_constraints.intersection(g)) == 1 for g in groups.values()),
            "Sharp kernel fails to hit every unit support exactly once")
    return {"size": a, "source_dimension": n, "disjoint_unit_count": a*a,
            "all_singular_subspace_cap": n-a*a,
            "sharp_kernel_dimension": n-a*a,
            "source_weights_distinct": True,
            "supports_with_a_coefficients": sum(len(g) == a for g in groups.values()),
            "supports_with_2a_coefficients": sum(len(g) == 2*a for g in groups.values())}


def report():
    check_sources()
    prior.verify(json.loads(prior.RESULT.read_text()))
    short_controls, identities = [], []
    for a in range(1, 7):
        for c in range(a):
            matrix = short_matrix(a, c)
            determinant = int(matrix.det(method="domain-ge"))
            require(abs(determinant) == 1, "Finite short unit determinant is not a unit")
            modular = {str(p): prior.determinant_mod(matrix.tolist(), p) for p in (2, 3, 5)}
            require(all(modular[str(p)] == determinant % p for p in (2, 3, 5)),
                    "Independent modular determinant disagrees")
            short_controls.append({"size": a, "residue": c, "dimension": matrix.rows,
                                   "integer_determinant": determinant,
                                   "independent_modular_determinants": modular})
            identities.append(recurrence(a, c))
    return {"scope": "Finite controls througha6 and packing bookkeeping througha12; all-size theorem is the written degree/divisibility proof.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "all_field_unit_claim": True, "complex_subspace_claim": True,
            "short_matrices": short_controls, "formal_recurrence_controls": identities,
            "packing_and_sharp_kernel_controls": [packing(a) for a in range(1, 13)],
            "all_size_cap_formula": "a^2*(2*a-2)", "source_dimension_formula": "a^2*(2*a-1)"}


def verify(record):
    require(record == report(), "Changed exact units, recurrence, cap or scope")
    return {"short_integer_determinants": len(record["short_matrices"]),
            "independent_modular_checks": 3*len(record["short_matrices"]),
            "formal_successive_identities": sum(x["formal_successive_identities"]
                                                for x in record["formal_recurrence_controls"]),
            "packing_sizes": len(record["packing_and_sharp_kernel_controls"]),
            "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
