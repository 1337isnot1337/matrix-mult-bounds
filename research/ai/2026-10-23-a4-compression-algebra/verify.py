"""Exact acceptance for all constant rank-26 compressions of the A4 outer space.

This program reconstructs the literal source, not a sampled compression.
The written proof supplies the torus-limit, isotropic-subspace, and
shared-flag deductions. Acceptance uses rational arithmetic only; it does
not use a Groebner basis, numerical optimization, or a modular upper bound.
"""

import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations, combinations_with_replacement, product
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULTS = ROOT / "results/a4-compression-algebra-2026-10-23"
DEGREES = tuple(range(-3, 10))
WEIGHTS = tuple(range(-3, 7))
WEIGHT_SIZES = (1, 2, 3, 4, 4, 4, 4, 3, 2, 1)
DEGREE_SIZES = (1, 2, 3, 5, 5, 5, 5, 5, 5, 4, 3, 2, 1)
SPECIAL_PAIRS = {(0, 49): "A", (10, 49): "B", (10, 52): "C"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sparse_entries(matrix):
    return [[i, j, int(matrix[i, j])] for i in range(matrix.rows)
            for j in range(matrix.cols) if matrix[i, j]]


@lru_cache(maxsize=1)
def reconstruct():
    """Rebuild S, K and E directly from their literal coefficient formula."""
    literal = []
    for i, s in product(range(4), repeat=2):
        matrix = sp.zeros(28)
        for j, r in product(range(4), repeat=2):
            matrix[7 * j + s + r, 4 * (i + j) + r] = 1
        literal.append(matrix)
    unit = sum((literal[4 * i + 3 - i] for i in range(4)), sp.zeros(28))
    require(abs(unit.det()) == 1, "the literal source unit is not unimodular")
    inverse = unit.inv()
    outer = [inverse * matrix for matrix in literal]
    require(all(unit * matrix == source for matrix, source in zip(outer, literal)),
            "source normalization failed")
    fixed = outer[0]
    matrices = list(outer)
    labels = [["plain", i, s] for i, s in product(range(4), repeat=2)]
    degrees = [3 - i - s for _, i, s in labels]
    for i, s in product(range(4), repeat=2):
        if (i, s) in ((0, 0), (0, 3)):
            continue
        matrices.append(outer[4 * i + s] * fixed - fixed * outer[4 * i + s])
        labels.append(["commutator", i, s])
        degrees.append(6 - i - s)
    for i, s in product(range(4), repeat=2):
        matrices.append(fixed * outer[4 * i + s] * fixed)
        labels.append(["sandwich", i, s])
        degrees.append(9 - i - s)
    require(len(matrices) == 46, "wrong source-basis count")
    vectors = sp.Matrix.hstack(*(matrix.reshape(784, 1) for matrix in matrices))
    require(vectors.rank() == 46, "the 46 source matrices are dependent")
    groups = {w: [k for k in range(28) if k // 4 - k % 4 == w] for w in WEIGHTS}
    require(tuple(map(len, groups.values())) == WEIGHT_SIZES, "wrong weight dimensions")
    for matrix, degree in zip(matrices, degrees):
        require(all((r // 4 - r % 4) - (c // 4 - c % 4) == degree
                    for r, c, _ in sparse_entries(matrix)), "a source matrix is not homogeneous")
    pieces = {}
    for degree in DEGREES:
        indices = [k for k, d in enumerate(degrees) if d == degree]
        blocks = []
        for input_weight in WEIGHTS:
            output_weight = input_weight + degree
            if output_weight not in groups:
                continue
            rows, columns = groups[output_weight], groups[input_weight]
            coefficients = sp.Matrix([[matrices[k][r, c] for k in indices]
                                      for r in rows for c in columns])
            if coefficients.is_zero_matrix:
                continue
            blocks.append({"input": input_weight, "output": output_weight,
                           "rows": len(rows), "columns": len(columns),
                           "coefficients": coefficients})
        pieces[degree] = {"dimension": len(indices), "blocks": blocks,
                          "labels": [labels[k] for k in indices]}
    require(tuple(pieces[d]["dimension"] for d in DEGREES) == DEGREE_SIZES,
            "wrong homogeneous source dimensions")
    fingerprint = hashlib.sha256(canonical_bytes({
        "labels": labels, "matrices": [sparse_entries(x) for x in matrices]})).hexdigest()
    return pieces, fingerprint


def budget_patterns():
    result = []
    for first, second in combinations_with_replacement(range(10), 2):
        budget = [0] * 10
        budget[first] += 1
        budget[second] += 1
        if all(a <= b for a, b in zip(budget, WEIGHT_SIZES)):
            result.append(tuple(budget))
    require(len(result) == 53 and len(set(result)) == 53, "incomplete budget enumeration")
    return tuple(result)


def caps_for(piece, a, b):
    return tuple(a[block["input"] + 3] + b[block["output"] + 3]
                 for block in piece["blocks"])


@lru_cache(maxsize=None)
def zero_block_nullspace(degree, caps):
    piece = reconstruct()[0][degree]
    require(len(caps) == len(piece["blocks"]), "wrong block-cap count")
    equations = set()
    for block, cap in zip(piece["blocks"], caps):
        if cap == 0:
            equations.update(tuple(row) for row in block["coefficients"].tolist())
    if not equations:
        return sp.eye(piece["dimension"])
    matrix = sp.Matrix(sorted(equations))
    basis = matrix.nullspace()
    return sp.Matrix.hstack(*basis) if basis else sp.zeros(piece["dimension"], 0)


def primitive_polynomial(expression, variables):
    polynomial = sp.Poly(expression, *variables, domain=sp.QQ)
    if polynomial.is_zero:
        return None
    polynomial = polynomial.clear_denoms()[1].primitive()[1]
    return -polynomial if polynomial.LC() < 0 else polynomial


@lru_cache(maxsize=None)
def necessary_minors(degree, caps):
    piece = reconstruct()[0][degree]
    basis = zero_block_nullspace(degree, caps)
    if basis.cols == 0:
        return (), ()
    variables = sp.symbols("z:" + str(basis.cols))
    coordinate = basis * sp.Matrix(variables)
    result = {}
    for block, cap in zip(piece["blocks"], caps):
        order = cap + 1
        if cap == 0 or order > min(block["rows"], block["columns"]):
            continue
        matrix = (block["coefficients"] * coordinate).reshape(block["rows"], block["columns"])
        for rows in combinations(range(matrix.rows), order):
            for columns in combinations(range(matrix.cols), order):
                polynomial = primitive_polynomial(matrix.extract(rows, columns).det(), variables)
                if polynomial is not None:
                    result[tuple(polynomial.terms())] = polynomial
    return variables, tuple(result.values())


@lru_cache(maxsize=None)
def homogeneous_bound(degree, caps):
    dimension = zero_block_nullspace(degree, caps).cols
    if not dimension:
        return {"linear": 0, "quadratic": 0, "hessian_rank": 0, "minors": 0}
    variables, polynomials = necessary_minors(degree, caps)
    quadratic_sum = sum((p.as_expr() for p in polynomials if p.total_degree() == 2), sp.Integer(0))
    rank = sp.hessian(quadratic_sum, variables).rank()
    bound = min(dimension - (rank + 1) // 2, dimension - bool(polynomials))
    return {"linear": int(dimension), "quadratic": int(bound),
            "hessian_rank": int(rank), "minors": len(polynomials)}


@lru_cache(maxsize=1)
def finite_coverage():
    pieces, fingerprint = reconstruct()
    patterns = budget_patterns()
    coarse = []
    quadratic = []
    histogram = Counter()
    for ai, a in enumerate(patterns):
        for bi, b in enumerate(patterns):
            caps = [caps_for(pieces[d], a, b) for d in DEGREES]
            linear = [zero_block_nullspace(d, cap).cols for d, cap in zip(DEGREES, caps)]
            coarse.append([ai, bi, list(map(int, linear))])
            histogram[sum(linear)] += 1
            if sum(linear) <= 8:
                continue
            bounds = [{"degree": d, "caps": list(cap), **homogeneous_bound(d, cap)}
                      for d, cap in zip(DEGREES, caps)]
            quadratic.append({"a_index": ai, "b_index": bi, "degrees": bounds,
                              "total": sum(x["quadratic"] for x in bounds)})
    unresolved = {(row["a_index"], row["b_index"]) for row in quadratic if row["total"] > 8}
    require(unresolved == set(SPECIAL_PAIRS), "the exceptional budget list changed")
    require(len(quadratic) == 28, "wrong number of nontrivial minor cases")
    return {"basis_sha256": fingerprint, "patterns": [list(x) for x in patterns],
            "coarse": coarse, "coarse_histogram": {str(k): v for k, v in sorted(histogram.items())},
            "quadratic": quadratic}


def identity_targets():
    z0, z1, z2, z3, z4 = sp.symbols("z:5")
    six = [z2 * (z2 - 2*z3 + z4), z2 * (z1 + 3*z2 - 3*z3 + z4),
           z2 * (z0 - 2*z1 - 3*z2 + z3), z4 * (z2 - 2*z3 + z4),
           z4 * (z0 + z3 - 2*z4), z4 * (z0 - z1 - z4)]
    degree4 = [z0**2-z0*z2+z1*z2-z3**2-3*z4**2,
               z0*z1-z0*z2+z2**2-3*z3**2-z4**2,
               -z0*z2+z1**2-z1*z2+z2**2-z3**2+z4**2,
               z0*z3+z3**2, z1*z3+z3**2, z2*z3+2*z3**2,
               z0*z4-2*z4**2, z1*z4-z4**2, z2*z4-z4**2, z3*z4]
    return {
        "degree4_caps1111": (4, (1, 1, 1, 1), degree4),
        "degree5_caps111": (5, (1, 1, 1), six + [z2**2-4*z3**2+z4**2, z0*z1-3*z3**2]),
        "degree5_caps121": (5, (1, 2, 1), six),
    }


def accept_identities(certificate):
    targets = identity_targets()
    require(isinstance(certificate, dict) and set(certificate) == set(targets),
            "missing or extraneous minor-identity cases")
    checked = 0
    for name, (degree, caps, formulas) in targets.items():
        variables, minors = necessary_minors(degree, caps)
        require(zero_block_nullspace(degree, caps) == sp.eye(5),
                "special-case coordinates are not the literal ordered basis")
        rows = certificate[name]
        require(isinstance(rows, list) and len(rows) == len(formulas), "wrong identity coverage")
        for row, target in zip(rows, formulas):
            require(isinstance(row, list), "invalid identity row")
            value = sp.Integer(0)
            used = set()
            for entry in row:
                require(isinstance(entry, list) and len(entry) == 3
                        and all(type(x) is int for x in entry), "invalid rational identity coefficient")
                index, numerator, denominator = entry
                require(0 <= index < len(minors) and index not in used
                        and numerator != 0 and denominator > 0, "invalid minor index or coefficient")
                used.add(index)
                value += sp.Rational(numerator, denominator) * minors[index].as_expr()
            require(sp.Poly(value-target, *variables, domain=sp.QQ).is_zero,
                    "a necessary-minor identity is false")
            checked += 1
    return checked


def symbolic_blocks(degree):
    piece = reconstruct()[0][degree]
    variables = sp.symbols("z:" + str(piece["dimension"]))
    return variables, {(b["input"], b["output"]):
                       (b["coefficients"] * sp.Matrix(variables)).reshape(b["rows"], b["columns"])
                       for b in piece["blocks"]}


def accept_special_blocks():
    pieces, _ = reconstruct()
    require(pieces[4]["labels"] == [["commutator", 0, 2], ["commutator", 1, 1],
                                     ["commutator", 2, 0], ["sandwich", 2, 3], ["sandwich", 3, 2]],
            "wrong degree-four coordinate order")
    require(pieces[5]["labels"] == [["commutator", 0, 1], ["commutator", 1, 0],
                                     ["sandwich", 1, 3], ["sandwich", 2, 2], ["sandwich", 3, 1]],
            "wrong degree-five coordinate order")
    variables, blocks = symbolic_blocks(5)
    z0, z1, z2, z3, z4 = variables
    determinant = primitive_polynomial(blocks[(-1, 4)].det(), variables).as_expr()
    require(sp.expand(determinant.subs({z2: 0, z4: 0})
                      - z3*(z0*z1-z0*z3+z1*z3+3*z3**2)) == 0,
            "wrong degree-five cubic restriction")

    variables, blocks = symbolic_blocks(6)
    z0, x, y, z3 = variables
    require(set(blocks) == {(-3, 3), (-2, 4), (-1, 5), (0, 6)}, "wrong degree-six block support")
    require(blocks[(-3, 3)] == sp.Matrix([z0, -z0, 0, 0])
            and blocks[(0, 6)] == sp.Matrix([[z3, 0, 0, 0]]), "wrong degree-six boundary blocks")
    lower = blocks[(-2, 4)].subs({z0: 0, z3: 0})
    upper = blocks[(-1, 5)].subs({z0: 0, z3: 0})
    require(lower == sp.Matrix([[-x+2*y, x-2*y], [3*x-3*y, -3*x+3*y], [-3*x, 4*x]]),
            "wrong degree-six first coupled block")
    u, e2 = sp.Matrix([1, -2]), sp.Matrix([0, 1])
    r, s, e3 = sp.Matrix([[2, -1, -1]]), sp.Matrix([[-1, 2, -1]]), sp.Matrix([[0, 0, 1]])
    require(upper == u*(x*r+y*s) + y*e2*e3, "wrong degree-six second coupled block")
    require(sp.Matrix.vstack(r, s, e3).det() == 3, "the degree-six covectors are dependent")
    a, b = sp.symbols("a b")
    evaluated = lower * sp.Matrix([a, b])
    coefficient = evaluated.jacobian([x, y])
    require(sp.expand(coefficient[:2, :].det()+3*(a-b)**2) == 0,
            "wrong degree-six coefficient determinant")

    variables, blocks = symbolic_blocks(7)
    z0, z1, z2 = variables
    q = -z0+2*z1-z2
    require(set(blocks) == {(-3, 4), (-2, 5), (-1, 6)}, "wrong degree-seven block support")
    require(blocks[(-3, 4)] == sp.Matrix([0, 0, z0])
            and blocks[(-1, 6)] == sp.Matrix([[0, 0, z2]])
            and blocks[(-2, 5)] == sp.Matrix([[q, -q], [-2*q, 2*q+z1]]),
            "wrong degree-seven shared-flag identities")
    variables, blocks = symbolic_blocks(8)
    z0, z1 = variables
    require(set(blocks) == {(-3, 5), (-2, 6)}
            and blocks[(-3, 5)] == sp.Matrix([0, z0])
            and blocks[(-2, 6)] == sp.Matrix([[0, z1]]), "wrong degree-eight blocks")
    return {"degree5_cubic_identity": True, "degree6_to_8_blocks_checked": 9,
            "degree6_determinants_checked": 2}


def check_source_pins():
    data = json.loads((PACKAGE / "sources.json").read_text())
    require(data.get("schema") == "a4-compression-algebra-sources-v1", "wrong source manifest")
    for source in data["repository_inputs"]:
        path = ROOT / source["path"]
        require(hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"],
                "a pinned prior source has changed: " + source["path"])
    return len(data["repository_inputs"])


def accept(certificate):
    require(certificate.get("schema") == "a4-arbitrary-compression-v1", "wrong certificate schema")
    pins = check_source_pins()
    coverage = finite_coverage()
    require(certificate.get("coverage") == coverage, "finite coverage or a rational rank certificate changed")
    identities = accept_identities(certificate.get("minor_identities"))
    block_report = accept_special_blocks()
    # The exceptional budgets must have exactly the homogeneous dimensions
    # used by the three written deductions, with all omitted degrees zero.
    rows = {(x["a_index"], x["b_index"]): x for x in coverage["quadratic"]}
    for key in [(0, 49), (10, 52)]:
        row = rows[key]
        degree5 = next(x for x in row["degrees"] if x["degree"] == 5)
        require(degree5["caps"] == [1, 1, 1] and degree5["quadratic"] == 2
                and row["total"] == 9, "wrong degree-five exceptional case")
    row = rows[(10, 49)]
    require([(x["degree"], x["linear"], x["caps"]) for x in row["degrees"] if x["linear"]]
            == [(4, 5, [1, 1, 1, 1]), (5, 5, [1, 2, 1]), (6, 2, [0, 2, 2, 0]),
                (7, 3, [1, 2, 1]), (8, 2, [1, 1])], "wrong final shared-flag case")
    patterns = budget_patterns()
    require(patterns[10] == (0, 1, 1, 0, 0, 0, 0, 0, 0, 0)
            and patterns[49] == (0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
            "the final flag budgets do not match the proof")
    return {"schema": "a4-arbitrary-compression-verification-v1", "accepted": True,
            "field": "complex numbers", "source_dimension": 46, "matrix_size": 28,
            "basis_sha256": coverage["basis_sha256"], "pinned_repository_inputs": pins,
            "input_budgets": 53, "output_budgets": 53, "budget_pairs_checked": 2809,
            "pairs_closed_by_zero_blocks": 2781, "additional_pairs_closed_by_quadratic_bounds": 25,
            "additional_pairs_closed_by_degree5_identities": 2, "shared_flag_cases": 1,
            "exact_minor_identities_checked": identities, **block_report,
            "universal_compression_kernel_dimension_at_most": 8,
            "universal_rank26_compression_image_dimension_at_least": 38,
            "fixed_full_limit_rank110_compression_image_dimension_at_least": 104,
            "constant_compressions_of_specified_conjugation_family_excluded": True,
            "arbitrary_moving_long_factor_maps_excluded": False,
            "matrix_multiplication_target_constructed": False,
            "exponent_improvement_claimed": False,
            "evidence_status": "written proof with exact acceptance; unreviewed"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--certificate", type=Path, default=RESULTS / "certificate.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = accept(json.loads(args.certificate.read_text()))
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
