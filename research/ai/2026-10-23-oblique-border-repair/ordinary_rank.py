#!/usr/bin/env python3
"""Exact finite inputs to ordinary_rank.md, using only integers.

The output checks the explicit identities and minors used by the proof.
The exclusion of all six-term decompositions is the written argument,
not a finite search performed by this program.
"""

import argparse
import itertools
import json
from pathlib import Path


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for key, value in polynomial.items():
            result[key] = result.get(key, 0) + value
    return {key: value for key, value in result.items() if value}


def scale(polynomial, coefficient):
    return {key: value * coefficient for key, value in polynomial.items()
            if value * coefficient}


def multiply(first, second):
    result = {}
    for left, a in first.items():
        for right, b in second.items():
            key = tuple(x + y for x, y in zip(left, right))
            result[key] = result.get(key, 0) + a * b
    return {key: value for key, value in result.items() if value}


def determinant(matrix):
    size = len(matrix)
    result = {}
    for permutation in itertools.permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term = {(0, 0, 0): (-1) ** inversions}
        for row, column in enumerate(permutation):
            term = multiply(term, matrix[row][column])
        result = add(result, term)
    return result


def rank_one(first, second, third):
    return {(i, j, k): a * b * c
            for i, a in first.items()
            for j, b in second.items()
            for k, c in third.items()}


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def canonical_core():
    # A: u,v,w. B: X,Z,a,eta,y. C: P,Q,R,S,T.
    return {index: 1 for index in [
        (0, 0, 0), (0, 1, 1), (1, 2, 2), (1, 3, 3),
        (2, 0, 1), (2, 1, 4), (2, 3, 2), (2, 4, 3), (2, 0, 2),
    ]}


def ordinary_terms():
    return [
        ({0: 1, 2: 1}, {0: 1, 1: 1}, {1: 1}),
        ({0: 1}, {0: 1}, {0: 1, 1: -1}),
        ({2: 1}, {1: 1}, {4: 1, 1: -1}),
        ({1: 1, 2: 1}, {3: 1}, {2: 1, 3: 1}),
        ({1: 1}, {2: 1, 3: -1}, {2: 1}),
        ({2: 1}, {4: 1, 3: -1}, {3: 1}),
        ({2: 1}, {0: 1}, {2: 1}),
    ]


def check(core=None, terms=None):
    core = canonical_core() if core is None else core
    terms = ordinary_terms() if terms is None else terms
    reconstructed = add(*(rank_one(*term) for term in terms))
    require(core == canonical_core(), "Wrong canonical core coefficients")
    require(len(terms) == 7, "The certificate requires seven ordinary terms")
    require(reconstructed == core, "The ordinary products do not equal the core")

    u, v, w = ({(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1})
    variables = [u, v, w]
    matrix = [[{} for _ in range(5)] for _ in range(5)]
    for (first, second, third), coefficient in core.items():
        matrix[second][third] = add(matrix[second][third],
                                     scale(variables[first], coefficient))
    right = [multiply(w, w), scale(multiply(u, w), -1), {}, {}, multiply(u, u)]
    left = [{}, {}, multiply(w, w), scale(multiply(v, w), -1), multiply(v, v)]
    right_image = [add(*(multiply(matrix[i][j], right[j]) for j in range(5)))
                   for i in range(5)]
    left_image = [add(*(multiply(left[i], matrix[i][j]) for i in range(5)))
                  for j in range(5)]
    require(right_image == [{}] * 5, "The right polynomial kernel is incorrect")
    require(left_image == [{}] * 5, "The left polynomial kernel is incorrect")
    generic_minor = determinant([[matrix[i][j] for j in range(4)]
                                 for i in range(4)])
    require(generic_minor == {(2, 2, 0): 1}, "The generic slice minor is incorrect")

    b_coordinates = [(0, 0), (0, 1), (1, 2), (1, 3), (2, 3)]
    b_minor = [[core.get((i, b, c), 0) for i, c in b_coordinates]
               for b in range(5)]
    c_coordinates = [(0, 0), (0, 1), (1, 2), (1, 3), (2, 1)]
    c_minor = [[core.get((i, b, c), 0) for i, b in c_coordinates]
               for c in range(5)]
    identity_five = [[int(i == j) for j in range(5)] for i in range(5)]
    require(b_minor == identity_five, "The second-leg concision minor is incorrect")
    require(c_minor == identity_five, "The third-leg concision minor is incorrect")

    top_left = {key: value for key, value in core.items()
                if key[1] in (0, 1) and key[2] in (0, 1, 4)}
    bottom_right = {key: value for key, value in core.items()
                    if key[1] in (2, 3, 4) and key[2] in (2, 3)}

    def functional(tensor):
        return (tensor.get((2, 0, 2), 0) - tensor.get((0, 1, 2), 0)
                - tensor.get((1, 0, 3), 0))

    graph_basis_values = []
    for old_c in (0, 1, 4):
        for new_c in (2, 3):
            mapped = {(a, b, new_c): value
                      for (a, b, c), value in top_left.items() if c == old_c}
            graph_basis_values.append(functional(mapped))
    for old_b in (2, 3, 4):
        for new_b in (0, 1):
            mapped = {(a, new_b, c): value
                      for (a, b, c), value in bottom_right.items() if b == old_b}
            graph_basis_values.append(functional(mapped))
    require(graph_basis_values == [0] * 12, "A graph image has nonzero functional")
    require(functional(core) == 1, "The actual mixed block is not separated")

    residual_rows, residual_columns = (0, 1, 4), (2, 4, 3)
    residual_minor = [[core.get((2, b, c), 0) for c in residual_columns]
                      for b in residual_rows]
    require(residual_minor == [[int(i == j) for j in range(3)] for i in range(3)],
            "The shared-w residual minor is incorrect")
    require(not set(residual_columns).intersection((0, 1)),
            "The u correction meets the selected columns")
    require(not set(residual_rows).intersection((2, 3)),
            "The v correction meets the selected rows")

    return {
        "claim": "AI-OBLIQUE-CORE-RANK-SEVEN-003",
        "statement": "The isolated core has ordinary tensor rank seven over every field.",
        "verification_scope": "Exact inputs to the written proof; not a finite decomposition search.",
        "ordinary_rank_one_terms": len(terms),
        "ordinary_rank_upper_bound": 7,
        "ordinary_rank_lower_bound_from_written_proof": 7,
        "tensor_coordinates_compared": 3 * 5 * 5,
        "seven_term_identity": reconstructed == core,
        "right_kernel_identity": right_image == [{}] * 5,
        "left_kernel_identity": left_image == [{}] * 5,
        "generic_slice_minor": "u^2*v^2",
        "second_leg_concision_minor": b_minor,
        "third_leg_concision_minor": c_minor,
        "graph_map_basis_functional_values": graph_basis_values,
        "actual_mixed_block_functional_value": functional(core),
        "shared_w_residual_minor": residual_minor,
        "field_scope": "The displayed identities and minors hold over the integers and every field.",
        "whole_residual_rank_lower_bound_claimed": False,
        "independent_mathematical_review": False,
        "formalized": False,
        "improves_omega": False,
    }


def verify_saved(path):
    actual = check()
    require(json.loads(Path(path).read_text()) == actual,
            "Saved ordinary-rank certificate does not replay")
    return actual


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("ordinary-rank-certificate.json"))
    args = parser.parse_args()
    result = check()
    output = args.output
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"certificate": str(output), "passed": True,
                      "ordinary_rank": 7, "whole_residual_claim": False}))
