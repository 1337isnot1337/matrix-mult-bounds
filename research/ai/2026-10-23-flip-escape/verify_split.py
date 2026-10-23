"""Replay the full exact Laurent identity for the four-split border seed.

All arithmetic uses Fraction and the Python standard library.  The verifier
checks the exported factors directly, as well as their physical construction.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
SEED = PACKAGE.parent / "2026-10-21-external-grid-seed/factors.json"
SEED_SHA256 = "bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3"
SHAPES = ((4, 5), (5, 5), (5, 4))
REPLACEMENTS = [[0, 18, -1], [17, 8, 1], [48, 2, -1], [56, 22, -1]]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rref(matrix):
    work = [list(map(Fraction, row)) for row in matrix]
    require(bool(work), "Expected a matrix with at least one row")
    require(all(len(row) == len(work[0]) for row in work), "Ragged matrix")
    pivot_row = 0
    pivots = []
    for column in range(len(work[0])):
        found = next((i for i in range(pivot_row, len(work)) if work[i][column]), None)
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [x / divisor for x in work[pivot_row]]
        for i in range(len(work)):
            if i != pivot_row and work[i][column]:
                multiple = work[i][column]
                work[i] = [x - multiple * y for x, y in zip(work[i], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work, pivots


def identity(size):
    return [[Fraction(i == j) for j in range(size)] for i in range(size)]


def product(left, right):
    require(len(left[0]) == len(right), "Incompatible matrix product")
    return [[sum(x * right[k][j] for k, x in enumerate(row))
             for j in range(len(right[0]))] for row in left]


def inverse(matrix):
    size = len(matrix)
    require(all(len(row) == size for row in matrix), "Inverse requires a square matrix")
    augmented = [list(row) + unit for row, unit in zip(matrix, identity(size))]
    reduced, pivots = rref(augmented)
    require(pivots == list(range(size)), "Physical basis is singular")
    result = [row[size:] for row in reduced]
    require(product(matrix, result) == identity(size), "Inverse identity failed")
    return result


def determinant(matrix):
    size = len(matrix)
    total = Fraction(0)
    for permutation in itertools.permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term = Fraction(-1 if inversions % 2 else 1)
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        total += term
    return total


def column_basis(matrix):
    _, pivots = rref(matrix)
    return [[row[j] for j in pivots] for row in matrix]


def hstack(matrices):
    require(bool(matrices), "Cannot concatenate an empty matrix list")
    height = len(matrices[0])
    require(all(len(matrix) == height for matrix in matrices), "Unequal row counts")
    return [[value for matrix in matrices for value in matrix[i]]
            for i in range(height)]


def image_flags(discarded):
    """Compute the common descending quiver-image flag over Q."""
    flags = [[identity(4), identity(5), identity(5)]]
    for _ in range(14):
        previous = flags[-1]
        following = [column_basis(hstack([product(term[leg], previous[(leg + 1) % 3])
                                          for term in discarded]))
                     for leg in range(3)]
        flags.append(following)
        old_size = sum(len(matrix[0]) for matrix in previous)
        new_size = sum(len(matrix[0]) for matrix in following)
        if new_size == 0:
            return flags
        require(new_size < old_size, "Discarded arrows are not jointly nilpotent")
    raise ValueError("Image flag did not vanish within total dimension 14")


def adapted_bases(flags):
    bases, weights = [], []
    for leg, size in enumerate((4, 5, 5)):
        basis = [[] for _ in range(size)]
        leg_weights = []
        for depth in range(len(flags) - 1, -1, -1):
            matrix = flags[depth][leg]
            for j in range(len(matrix[0])):
                trial = [row + [matrix[i][j]] for i, row in enumerate(basis)]
                if len(rref(trial)[1]) > len(basis[0]):
                    basis = trial
                    leg_weights.append(-depth)
        require(len(basis[0]) == size, "Adapted basis is incomplete")
        bases.append(basis)
        weights.append(leg_weights)
    return bases, weights


def load_seed():
    data = SEED.read_bytes()
    require(hashlib.sha256(data).hexdigest() == SEED_SHA256, "External seed byte pin differs")
    factors = json.loads(data)
    require(factors["n"] == [4, 5, 5] and factors["m"] == 76,
            "Unexpected external seed dimensions")
    matrices = []
    for index in range(76):
        term = []
        for leg, (height, width) in zip(("u", "v", "w"), SHAPES):
            flat = factors[leg][index]
            require(len(flat) == height * width, "Incorrect factor dimensions")
            term.append([list(map(Fraction, flat[i * width:(i + 1) * width]))
                         for i in range(height)])
        matrices.append(term)
    return matrices


def split_seed(seed, replacements=REPLACEMENTS):
    surviving = [[matrix for matrix in term] for term in seed]
    discarded = []
    changed_indices = [i for i, _, _ in replacements]
    require(len(set(changed_indices)) == len(changed_indices), "Repeated split index")
    for i, j, coefficient in replacements:
        require(i != j and 0 <= i < 76 and 0 <= j < 76, "Invalid replacement index")
        require(j not in changed_indices, "Replacement direction is also removed")
        replacement = [[coefficient * x for x in row] for row in seed[j][0]]
        difference = [[x - y for x, y in zip(row, other)]
                      for row, other in zip(seed[i][0], replacement)]
        surviving[i][0] = replacement
        discarded.append([difference, seed[i][1], seed[i][2]])
    return surviving, discarded


def monomials(matrix, left_weights, right_weights):
    width = len(matrix[0])
    return [[i * width + j, str(value), right_weights[j] - left_weights[i]]
            for i, row in enumerate(matrix) for j, value in enumerate(row) if value]


def transformed_factors(terms, bases, weights):
    inverses = [inverse(matrix) for matrix in bases]
    result = []
    for term in terms:
        result.append([
            monomials(product(product(inverses[leg], term[leg]), bases[(leg + 1) % 3]),
                      weights[leg], weights[(leg + 1) % 3])
            for leg in range(3)])
    return result


def parse_factors(terms, expected_count):
    require(len(terms) == expected_count, "Wrong number of rank-one terms")
    parsed = []
    for term in terms:
        require(len(term) == 3, "A tensor term needs three factors")
        parsed_term = []
        for entries, (height, width) in zip(term, SHAPES):
            require(bool(entries), "A rank-one factor is zero")
            seen = set()
            rows = []
            for coordinate, coefficient, exponent in entries:
                require(type(coordinate) is int and 0 <= coordinate < height * width,
                        "Factor coordinate is out of range")
                require(coordinate not in seen, "Repeated factor coordinate")
                require(type(exponent) is int, "Laurent exponent is not an integer")
                value = Fraction(coefficient)
                require(value != 0, "Stored sparse coefficient is zero")
                rows.append((coordinate, value, exponent))
                seen.add(coordinate)
            parsed_term.append(rows)
        parsed.append(parsed_term)
    return parsed


def contract(terms):
    """Contract every sparse Laurent coefficient, including all off-target entries."""
    output = {}
    for term in terms:
        for (a, x, e), (b, y, f), (c, z, g) in itertools.product(*term):
            key = (e + f + g, a, b, c)
            output[key] = output.get(key, Fraction(0)) + x * y * z
    return {key: value for key, value in output.items() if value}


def target_tensor():
    return {(5 * i + j, 5 * j + k, 4 * k + i): Fraction(1)
            for i in range(4) for j in range(5) for k in range(5)}


def verify_laurent_identity(certificate):
    surviving = parse_factors(certificate["surviving_factors"], 76)
    discarded = parse_factors(certificate["discarded_factors"], 4)
    require(all(exponent >= 1 for term in discarded for factor in term
                for _, _, exponent in factor), "Discarded factor has a nonpositive valuation")
    output = contract(surviving)
    require(not any(degree < 0 for degree, _, _, _ in output),
            "Surviving tensor has a negative Laurent coefficient")
    constant = {key[1:]: value for key, value in output.items() if key[0] == 0}
    require(constant == target_tensor(), "Constant tensor is not exactly M(4,5,5)")
    error = {key: value for key, value in output.items() if key[0] > 0}
    discarded_tensor = contract(discarded)
    require(error == {key: -value for key, value in discarded_tensor.items()},
            "Positive remainder does not equal the negative discarded tensor")
    degrees = {str(degree): count for degree, count in
               sorted(Counter(key[0] for key in output).items())}
    require(degrees == certificate["nonzero_coefficients_by_degree"],
            "Recorded coefficient counts differ")
    require(certificate["negative_coefficients"] == 0
            and certificate["constant_coefficients"] == 100,
            "Incorrect recorded coefficient totals")
    return degrees


def verify(certificate=None):
    if certificate is None:
        certificate = json.loads((PACKAGE / "split_certificate.json").read_text())
    require(certificate["seed_sha256"] == SEED_SHA256, "Certificate seed pin differs")
    require(certificate["dimensions"] == [4, 5, 5] and certificate["rank"] == 76,
            "Certificate dimensions or rank differ")
    require(certificate["replacements"] == REPLACEMENTS, "Unexpected split specification")
    seed = load_seed()
    surviving, discarded = split_seed(seed)
    flags = image_flags(discarded)
    dimensions = [[len(matrix[0]) for matrix in flag] for flag in flags]
    require(dimensions == certificate["rational_image_flag_dimensions"],
            "Common rational image flag differs")
    bases = [[[Fraction(x) for x in row] for row in matrix]
             for matrix in certificate["basis_matrices"]]
    weights = certificate["weights"]
    require(len(bases) == 3 and len(weights) == 3, "Three physical bases are required")
    for matrix, row, size in zip(bases, weights, (4, 5, 5)):
        require(len(matrix) == size and all(len(line) == size for line in matrix),
                "Physical basis has incorrect shape")
        require(len(row) == size and all(type(x) is int for x in row),
                "Physical weights have incorrect shape or type")
    require((bases, weights) == adapted_bases(flags), "Recorded adapted bases differ")
    determinants = [determinant(matrix) for matrix in bases]
    require(determinants == [1, -1, 1], "Physical bases are not the recorded unimodular bases")
    require(transformed_factors(surviving, bases, weights)
            == certificate["surviving_factors"], "Surviving factors differ from physical construction")
    require(transformed_factors(discarded, bases, weights)
            == certificate["discarded_factors"], "Discarded factors differ from physical construction")
    degrees = verify_laurent_identity(certificate)
    directions = set()
    for term in surviving:
        flat = [x for row in term[0] for x in row]
        first = next(x for x in flat if x)
        directions.add(tuple(x / first for x in flat))
    require(len(directions) == 72, "Unexpected first-leg direction count")
    return {
        "seed_sha256": SEED_SHA256,
        "border_rank_upper_bound": 76,
        "intermediate_exact_term_count": 80,
        "distinct_first_leg_directions": len(directions),
        "rational_image_flag_dimensions": dimensions,
        "physical_basis_determinants": [int(value) for value in determinants],
        "negative_coefficients": 0,
        "constant_nonzero_coefficients": 100,
        "constant_positions_checked": 10000,
        "positive_nonzero_coefficients": sum(value for key, value in degrees.items() if key != "0"),
        "nonzero_coefficients_by_degree": degrees,
        "Q64_maps_constructed": False,
        "rank_record_claimed": False,
        "proof_status": "written-unreviewed",
        "improves_omega": False,
    }


def build_certificate():
    seed = load_seed()
    surviving, discarded = split_seed(seed)
    flags = image_flags(discarded)
    bases, weights = adapted_bases(flags)
    saved_surviving = transformed_factors(surviving, bases, weights)
    saved_discarded = transformed_factors(discarded, bases, weights)
    output = contract(parse_factors(saved_surviving, 76))
    certificate = {
        "schema": "exact-split-border-seed-v1",
        "seed_sha256": SEED_SHA256,
        "dimensions": [4, 5, 5], "rank": 76,
        "replacements": REPLACEMENTS,
        "basis_matrices": [[[str(value) for value in row] for row in matrix]
                           for matrix in bases],
        "weights": weights,
        "rational_image_flag_dimensions": [[len(matrix[0]) for matrix in flag] for flag in flags],
        "surviving_factors": saved_surviving,
        "discarded_factors": saved_discarded,
        "nonzero_coefficients_by_degree": {str(degree): count for degree, count in
                                           sorted(Counter(key[0] for key in output).items())},
        "negative_coefficients": sum(key[0] < 0 for key in output),
        "constant_coefficients": sum(key[0] == 0 for key in output),
        "scope": "Explicit rank-76 border seed from an external exact rank-76 algorithm. No rank record, exponent improvement, or Q(6,4) map."
    }
    verify(certificate)
    return certificate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-certificate", type=Path)
    args = parser.parse_args()
    if args.write_certificate:
        certificate = build_certificate()
        args.write_certificate.write_text(json.dumps(certificate, indent=2) + "\n")
    else:
        certificate = None
    print(json.dumps(verify(certificate), indent=2))


if __name__ == "__main__":
    main()
