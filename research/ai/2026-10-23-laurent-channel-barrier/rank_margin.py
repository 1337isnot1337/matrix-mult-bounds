"""Exact controls for the additional auxiliary border-rank margin.

The general statement is proved in rank_margin.md. This verifier retains
all Laurent coefficients and distinguishes tensor border rank from first
flattening rank in a sharp one-dimensional example.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("laurent_channel_predecessor", HERE / "verify.py")
previous = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(previous)

add, mul, mono, scale = previous.add, previous.mul, previous.mono, previous.scale


def lower_bound(d, h, rho):
    if not (isinstance(d, int) and isinstance(h, int) and isinstance(rho, int)):
        raise TypeError("dimensions and ranks must be integers")
    if d < 0 or h < 2 or not 0 <= rho < h:
        raise ValueError("require d>=0, h>=2 and 0<=rho<h")
    return 0 if d == 0 else d + h - rho - 1


def eye(h):
    return [[mono() if i == j else {} for j in range(h)] for i in range(h)]


def vec(h, j):
    return [mono() if i == j else {} for i in range(h)]


def outer(left, right):
    return [[mul(a, b) for b in right] for a in left]


def matrix_sum(matrices, h):
    return [[add(*(matrix[i][j] for matrix in matrices))
             for j in range(h)] for i in range(h)]


def determinant(matrix):
    h = len(matrix)
    out = {}
    for permutation in itertools.permutations(range(h)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(h) for j in range(i+1, h))
        term = mono(-1 if inversions % 2 else 1)
        for i, j in enumerate(permutation):
            term = mul(term, matrix[i][j])
            if not term:
                break
        out = add(out, term)
    return out


def matrix_product(a, b):
    h = len(a)
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(h)))
             for j in range(h)] for i in range(h)]


def rank_one_encoding_control():
    h, l, r = 3, 2, 3
    b = {(j, alpha): add(mono(1+j+alpha, t=j-alpha),
                         mono(2-alpha, t=-1))
         for j in range(r) for alpha in range(h)}
    c = {(beta, i): add(mono(2+i-beta, t=beta-i),
                        mono(1+beta, t=-2))
         for beta in range(h) for i in range(l)}
    direct = [[{} for _ in range(h)] for _ in range(h)]
    # Encode the full native rank-one B-tensor-C coefficient expansion.
    for j in range(r):
        for i in range(l):
            for alpha in range(h):
                for beta in range(h):
                    term = previous.shift(mul(b[j, alpha], c[beta, i]), x=j, y=i)
                    direct[alpha][beta] = add(direct[alpha][beta], term)
    left = [add(*(previous.shift(b[j, alpha], x=j) for j in range(r)))
            for alpha in range(h)]
    right = [add(*(previous.shift(c[beta, i], y=i) for i in range(l)))
             for beta in range(h)]
    assert direct == outer(left, right)
    minors = 0
    for rows in itertools.combinations(range(h), 2):
        for cols in itertools.combinations(range(h), 2):
            assert not determinant([[direct[a][z] for z in cols] for a in rows])
            minors += 1
    negative = sum(t < 0 for row in direct for p in row for _, _, t in p)
    assert negative > 0
    return {"long_dimensions": [r*h, h*l], "channel_size": h,
            "native_rank_one_coefficient_positions": l*r*h*h,
            "complete_laurent_coefficients": sum(len(p) for row in direct for p in row),
            "negative_coefficients_retained": negative,
            "zero_two_by_two_minors": minors}


def projector_data(h, rho):
    if not 1 <= rho < h:
        raise ValueError("sharp projector control requires 1<=rho<h")
    source_factors = [(vec(h, j), vec(h, j)) for j in range(rho)]
    source_factors[0][0][rho] = mono(t=-1)
    auxiliary_factors = [(vec(h, j), vec(h, j)) for j in range(rho, h)]
    auxiliary_factors[0][1][0] = mono(-1, t=-1)
    source_terms = [outer(a, b) for a, b in source_factors]
    auxiliary_terms = [outer(a, b) for a, b in auxiliary_factors]
    return source_terms, auxiliary_terms


def sharp_projector_control(h, rho):
    source_terms, auxiliary_terms = projector_data(h, rho)
    source = matrix_sum(source_terms, h)
    auxiliary = matrix_sum(auxiliary_terms, h)
    assert matrix_sum([source, auxiliary], h) == eye(h)
    assert matrix_product(source, source) == source
    assert matrix_product(auxiliary, auxiliary) == auxiliary
    source_minor = [[source[i][j] for j in range(rho)] for i in range(rho)]
    auxiliary_minor = [[auxiliary[i][j] for j in range(rho, h)]
                       for i in range(rho, h)]
    assert determinant(source_minor) == mono()
    assert determinant(auxiliary_minor) == mono()
    assert len(source_terms) == rho
    assert len(auxiliary_terms) == h-rho == lower_bound(1, h, rho)
    assert any(t < 0 for row in source for p in row for _, _, t in p)
    assert any(t < 0 for row in auxiliary for p in row for _, _, t in p)
    dropped = []
    for k in range(len(auxiliary_terms)):
        smaller = matrix_sum([source]+auxiliary_terms[:k]+auxiliary_terms[k+1:], h)
        assert not determinant(smaller)
        assert smaller != eye(h)
        dropped.append(k)
    return {"good_subspace_dimension": 1, "middle_width": h,
            "generic_source_channel_rank": rho,
            "auxiliary_first_flattening_rank": 1,
            "auxiliary_border_rank": h-rho,
            "strengthened_border_rank_lower_bound": lower_bound(1, h, rho),
            "source_identity_minor_determinant": 1,
            "auxiliary_identity_minor_determinant": 1,
            "source_and_auxiliary_are_idempotents": True,
            "genuine_poles_cancel": True,
            "each_deleted_auxiliary_term_fails_complete_target": dropped}


def substituted_auxiliary(n):
    """Map the three actual rank-one terms of R(u), then set u=t^n.

    R(u)=a0*b0*(c0+u*c3)+a1*b1*c1+a2*b2*c2. All ai map to
    the single first basis vector; bi maps to e_(i+1); c3 maps to
    t^-5*e0. The three ordinary cj maps realize the auxiliary in (6).
    """
    h = 4
    images = []
    for j in range(3):
        second = vec(h, j+1)
        third = vec(h, j+1)
        if j == 0:
            third[0] = add(mono(-1, t=-1), mono(t=n-5))
        images.append(outer(second, third))
    return matrix_sum(images, h)


def substitution_controls():
    source_terms, auxiliary_terms = projector_data(4, 1)
    source = matrix_sum(source_terms, 4)
    auxiliary = matrix_sum(auxiliary_terms, 4)
    outcomes = []
    for n in (4, 5, 6):
        approximated = substituted_auxiliary(n)
        difference = matrix_sum([approximated,
                                 [[scale(p, -1) for p in row] for row in auxiliary]], 4)
        expected = [[{} for _ in range(4)] for _ in range(4)]
        expected[1][0] = mono(t=n-5)
        assert difference == expected
        total = matrix_sum([source, approximated], 4)
        constant = [[{e: c for e, c in p.items() if e[2] == 0}
                     for p in row] for row in total]
        has_poles = any(t < 0 for row in total for p in row for _, _, t in p)
        correct_constant = constant == eye(4)
        valid_target = not has_poles and correct_constant
        assert has_poles == (n < 5)
        assert correct_constant == (n != 5)
        assert valid_target == (n > 5)
        outcomes.append({"N": n, "local_map_pole_budget": 5,
                         "mapped_error_order": n-5,
                         "total_has_poles": has_poles,
                         "raw_constant_matches_target": correct_constant,
                         "regular_with_correct_target": valid_target})
    return outcomes


def certificate():
    case = dict(name="paired_rank_margin", n=7, m=4, h=4, l=7, r=7, D=0,
                variable_b=False, variable_c=False, exceptions_b=[], exceptions_c=[])
    paired = previous.finite_case(case)
    d, rho = paired["kernel_dimension_lower_bound"], paired["generic_channel_rank_cap"]
    assert (d, rho) == (16, 1)
    paired["strengthened_auxiliary_border_rank_lower_bound"] = lower_bound(d, case["h"], rho)
    assert paired["strengthened_auxiliary_border_rank_lower_bound"] == 18
    pins = json.loads((HERE / "rank-margin-sources.json").read_text())["local_dependencies"]
    for pin in pins:
        assert hashlib.sha256((previous.ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"], pin["path"]
    return {"schema": "laurent-rank-margin-controls-v1",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "independent_review": False, "lean_formalized": False,
            "local_source_pins": pins,
            "zero_good_dimension_supplies_no_bound": lower_bound(0, 4, 1),
            "rank_one_channel_encoding": rank_one_encoding_control(),
            "sharp_projector_cases": [sharp_projector_control(h, rho)
                                      for h, rho in [(4, 1), (5, 2), (5, 4)]],
            "auxiliary_border_substitution": substitution_controls(),
            "paired_control": paired,
            "scope": "Exact finite controls; the general proof is rank_margin.md."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(certificate(), indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
