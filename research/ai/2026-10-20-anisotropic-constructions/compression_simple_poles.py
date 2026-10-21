"""Standard-library exact controls for the fixed-compression pole proof."""

from itertools import product
import json
from pathlib import Path


Q2 = [[0, 0, 1], [0, 2, 0], [1, 0, 0]]
I3 = [[int(i == j) for j in range(3)] for i in range(3)]
UNITS = [[[int(3*i+j == k) for j in range(3)] for i in range(3)]
         for k in range(9)]


def multiply(left, right):
    return [[sum(left[i][k]*right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def apply(matrix, vector):
    return [sum(x*y for x, y in zip(row, vector)) for row in matrix]


def dot(left, right):
    return sum(x*y for x, y in zip(left, right))


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def ell2(matrix):
    (a,b,_), (d,_,f), (_,h,i) = matrix
    return [2*d-h, -2*a+2*i, b-2*f]


def shifted(matrix):
    t = trace(matrix)
    return [[matrix[i][j]+t*int(i == j) for j in range(3)] for i in range(3)]


def block2(matrix, vector):
    result = [[2*x for x in row]+[2*vector[i]] for i, row in enumerate(matrix)]
    row = [x+y for x, y in zip(ell2(matrix), apply(Q2, vector))]
    result.append(row+[2*trace(matrix)])
    return result


def linear2(matrices, values):
    total = 0
    for i in range(3):
        a, b, c = [matrices[(i+j)%3] for j in range(3)]
        ub, uc = values[(i+1)%3], values[(i+2)%3]
        vector = [x+trace(c)*y for x, y in zip(apply(b, uc), ub)]
        total += dot(ell2(a), vector)
    return total


def quadratic2(matrices, values):
    total = 0
    for i in range(3):
        middle = matrices[(i+1)%3]
        total += dot(values[i], apply(Q2, apply(shifted(middle), values[(i+2)%3])))
    return total


def evaluate(parameters, matrix):
    coordinates = sum(matrix, [])
    return [sum(coordinates[k]*parameters[k][j] for k in range(9)) for j in range(3)]


def sample_maps():
    return [[[(7*leg+3*k+5*j+2*k*j) % 11-5 for j in range(3)]
             for k in range(9)] for leg in range(3)]


def full_defect_formula_control():
    maps = sample_maps()
    checks = 0
    for indices in product(range(9), repeat=3):
        matrices = [UNITS[k] for k in indices]
        values = [maps[i][indices[i]] for i in range(3)]
        blocks = [block2(a, u) for a, u in zip(matrices, values)]
        actual = trace(multiply(multiply(blocks[0], blocks[1]), blocks[2]))
        actual -= 8*trace(multiply(multiply(matrices[0], matrices[1]), matrices[2]))
        expected = 8*trace(matrices[0])*trace(matrices[1])*trace(matrices[2])
        expected += 4*linear2(matrices, values)+4*quadratic2(matrices, values)
        if actual != expected:
            raise AssertionError("The corrected linear/quadratic defect formula failed.")
        checks += 1
    return {"complete_trilinear_coefficients_checked": checks,
            "three_distinct_integer_parameter_maps": maps,
            "corrected_defect_identity_exact": True}


def upper(t):
    return [[1, -2*t, -t*t], [0, 1, t], [0, 0, 1]]


def lower(t):
    return [[1, 0, 0], [t, 1, 0], [-t*t, -2*t, 1]]


def conjugate(matrix, r, rinverse):
    return multiply(multiply(r, matrix), rinverse)


def normal_form_controls():
    forms = [([1,0,0], [[2,0,0],[0,0,0],[0,0,-1]], UNITS[7], -1),
             ([0,1,0], [[1,0,0],[0,-1,0],[0,0,1]],
              [[1,0,0],[0,0,0],[0,0,-1]], -4)]
    changes = [(I3, I3), (upper(2), upper(-2)), (lower(1), lower(-1))]
    records = []
    for w0, a0, b0, expected in forms:
        for r, inverse in changes:
            if multiply(r, inverse) != I3 or multiply(multiply(transpose(r), Q2), r) != Q2:
                raise AssertionError("The chosen exact orthogonal change of basis failed.")
            for unit in UNITS:
                left = ell2(conjugate(unit, r, inverse))
                right = multiply([ell2(unit)], inverse)[0]
                if left != right:
                    raise AssertionError("The explicit ell covariance control failed.")
            w, a, b = apply(r, w0), conjugate(a0, r, inverse), conjugate(b0, r, inverse)
            left = multiply([apply(Q2, w)], shifted(a))[0]
            right = apply(shifted(b), w)
            value = trace(a)*dot(ell2(b), w)-trace(b)*dot(ell2(a), w)
            if any(left) or any(right) or value != expected:
                raise AssertionError("The transported next-order obstruction failed.")
            records.append({"w":w, "A":a, "B":b,
                            "left_kernel_condition_exact":True,
                            "right_kernel_condition_exact":True,
                            "twice_nonzero_linear_obstruction":value,
                            "ell_covariance_matrix_units_checked":9})
    return records


def beta2(first, second, matrix):
    return dot(first, apply(Q2, apply(shifted(matrix), second)))


def leading_family(vectors, coefficients=(2,2,-1)):
    maps = []
    for i in range(3):
        first, second = vectors[(i+2)%3], vectors[(i+1)%3]
        maps.append([[coefficients[i]*beta2(first, second, unit)*x for x in vectors[i]]
                     for unit in UNITS])
    return maps


def leading_control(normal):
    vectors = [[1,1,0], [0,1,1], normal["w"]]
    maps = leading_family(vectors)
    for indices in product(range(9), repeat=3):
        if quadratic2([UNITS[k] for k in indices], [maps[i][indices[i]] for i in range(3)]):
            raise AssertionError("A complete rank-one leading family failed quadratic cancellation.")
    a, b = normal["A"], normal["B"]
    ci = next(i for i in range(9) if any(maps[2][i]))
    matrices = [a, b, UNITS[ci]]
    f = [evaluate(maps[i], matrices[i]) for i in range(3)]
    g = [evaluate(sample_maps()[i], matrices[i]) for i in range(3)]
    summed = [[x+y for x, y in zip(fi, gi)] for fi, gi in zip(f, g)]
    polar = quadratic2(matrices, summed)-quadratic2(matrices, f)-quadratic2(matrices, g)
    obstruction = linear2(matrices, f)
    if any(f[0]) or any(f[1]) or polar or not obstruction:
        raise AssertionError("The leading-family next-order contradiction failed.")
    return {"leading_image_vectors":vectors,
            "leading_scalar_coefficients":[2,2,-1],
            "quadratic_coefficients_checked":729,
            "quadratic_leading_tensor_exactly_zero":True,
            "first_two_leading_values_zero":True,
            "quadratic_polar_term_zero":True,
            "twice_nonzero_linear_obstruction":obstruction,
            "third_test_matrix_unit":ci}


def report():
    normal = normal_form_controls()
    return {"claim":"No nonzero simple pole has a finite trace-tensor limit in the fixed spin-1 compression chart.",
            "defect_formula":full_defect_formula_control(),
            "two_normal_forms_and_four_transports":normal,
            "complete_rank_one_leading_controls":[leading_control(row) for row in normal],
            "several_negative_orders_excluded":False,
            "moving_physical_bases_excluded":False,
            "arbitrary_degenerations_excluded":False,
            "new_exponent_established":False}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[3]
    path = root / "results/anisotropic-constructions-2026-10-20/compression-simple-poles-controls.json"
    path.write_text(json.dumps(report(), indent=2)+"\n")
    print(path)
