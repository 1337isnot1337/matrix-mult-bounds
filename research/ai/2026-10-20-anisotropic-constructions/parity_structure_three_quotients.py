"""Exact A22 three-quotient scalar-defect controls, standard library only.

The proof gives det(C_out,in)=(Delta_in/Delta_out)^2 and cyclic
determinant product one.  The finite replay checks the lifts, scalar
actions, and every coefficient of the resulting trilinear forms.
"""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def multiply(left, right):
    return [[sum(left[i][k]*right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def determinant3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def delta(kernel):
    return kernel[3]-kernel[1]*kernel[2]


def projection(kernel):
    if kernel[0] != 1 or not delta(kernel):
        raise ValueError('Use a regular kernel in the first-coordinate-one chart.')
    return [[-kernel[i+1]]+[int(i == j) for j in range(3)] for i in range(3)]


def scalar_coefficients(output_kernel, input_kernel):
    _, x, y, z = output_kernel
    _, u, v, w = input_kernel
    denominator, input_delta = delta(output_kernel), delta(input_kernel)
    numerator = [[z*input_delta, -v*(y+z*v), -w*(y+z*v)],
                 [0, 1+x*v, u+x*w],
                 [-x*input_delta, v*(1+x*v), w*(1+x*v)]]
    return [[Fraction(entry, denominator) for entry in row] for row in numerator]


def lift(matrix, output_kernel, input_kernel):
    """Solve pi_out J=matrix pi_in in the 12-dimensional Hankel space."""
    _, x, y, z = output_kernel
    denominator = delta(output_kernel)
    initial = [[Fraction(0) for _ in range(4)]]+multiply(matrix, projection(input_kernel))
    ell = [Fraction(0) for _ in range(4)]
    for s in range(2):
        first = initial[1][s]-initial[0][2+s]
        second = initial[3][s]-initial[2][2+s]
        ell[s] = Fraction(y*first-second, denominator)
        ell[2+s] = Fraction(z*first-x*second, denominator)
    result = [[initial[i][j]+output_kernel[i]*ell[j] for j in range(4)]
              for i in range(4)]
    scalar = sum(ell[i]*input_kernel[i] for i in range(4))
    return result, scalar


def unit_matrix(index):
    row, col = divmod(index, 3)
    return [[Fraction(int(i == row and j == col)) for j in range(3)] for i in range(3)]


def rational_string(value):
    return str(Fraction(value))


def verify_case(kernels):
    lifts, scalars, coefficients, determinants = [], [], [], []
    for leg in range(3):
        output_kernel, input_kernel = kernels[leg], kernels[(leg+1) % 3]
        pi_out, pi_in = projection(output_kernel), projection(input_kernel)
        coefficient = scalar_coefficients(output_kernel, input_kernel)
        coefficient_determinant = determinant3(coefficient)
        if coefficient_determinant != Fraction(delta(input_kernel), delta(output_kernel))**2:
            raise ValueError('The scalar coefficient determinant identity failed.')
        leg_lifts, leg_scalars = [], []
        for index in range(9):
            matrix = unit_matrix(index)
            physical, scalar = lift(matrix, output_kernel, input_kernel)
            if any(physical[2*i+1][s] != physical[2*i][2+s]
                   for i, s in product(range(2), repeat=2)):
                raise ValueError('The lift left the A22 physical matrix space.')
            if multiply(pi_out, physical) != multiply(matrix, pi_in):
                raise ValueError('The quotient equation failed.')
            if multiply(physical, [[value] for value in input_kernel]) != [[value*scalar] for value in output_kernel]:
                raise ValueError('The scalar kernel action failed.')
            row, col = divmod(index, 3)
            if scalar != coefficient[row][col]:
                raise ValueError('The closed scalar coefficient formula failed.')
            leg_lifts.append(physical)
            leg_scalars.append(scalar)
        lifts.append(leg_lifts)
        scalars.append(leg_scalars)
        coefficients.append(coefficient)
        determinants.append(coefficient_determinant)
    if determinants[0]*determinants[1]*determinants[2] != 1:
        raise ValueError('The cyclic scalar determinant product is not one.')
    coefficient_checks = 0
    for first, second in product(range(9), repeat=2):
        paired = multiply(lifts[0][first], lifts[1][second])
        for third in range(9):
            actual = sum(paired[i][j]*lifts[2][third][j][i] for i, j in product(range(4), repeat=2))
            matrix_product_coefficient = int(first % 3 == second//3
                                             and second % 3 == third//3
                                             and third % 3 == first//3)
            expected = matrix_product_coefficient+scalars[0][first]*scalars[1][second]*scalars[2][third]
            if actual != expected:
                raise ValueError('The complete trace tensor identity failed.')
            coefficient_checks += 1
    norm_squared = Fraction(1)
    for coefficient in coefficients:
        norm_squared *= sum(value*value for row in coefficient for value in row)
    if norm_squared < 27:
        raise ValueError('The scalar-defect norm violated the determinant bound.')
    return {'kernel_vectors': [list(kernel) for kernel in kernels],
            'kernel_deltas': [delta(kernel) for kernel in kernels],
            'scalar_coefficient_matrices': [[[rational_string(value) for value in row]
                                             for row in coefficient] for coefficient in coefficients],
            'scalar_coefficient_determinants': [rational_string(value) for value in determinants],
            'cyclic_determinant_product': '1',
            'target_matrix_units_checked_per_leg': 9,
            'all_hankel_lift_constraints_exact': True,
            'all_quotient_equations_exact': True,
            'all_kernel_actions_exact': True,
            'complete_trilinear_coefficients_checked': coefficient_checks,
            'all_trilinear_coefficients_exact': True,
            'scalar_defect_frobenius_norm_squared': rational_string(norm_squared),
            'target_M3_frobenius_norm_squared': 27,
            'normalized_relative_residual_at_least_one': True}


def verify():
    examples = [verify_case(kernels) for kernels in (
        ((1, 0, 0, 1),)*3,
        ((1, 1, 2, 5), (1, -2, 3, 1), (1, 3, -1, 2)),
        ((1, 2, -1, 3), (1, 1, 1, -1), (1, -3, 2, 4)))]
    if examples[0]['scalar_defect_frobenius_norm_squared'] != '27':
        raise ValueError('The equality control failed.')
    return {'claim': 'cyclic product of the three A22 scalar-defect coefficient determinants equals one',
            'scope': 'regular exact-MM quotient lifts with arbitrary three quotient kernels and cyclic target bases',
            'arithmetic': 'Python exact rational arithmetic; standard library only',
            'examples': examples, 'complete_trilinear_coefficients_checked': 3*729,
            'uniform_normalized_relative_residual_lower_bound': '1',
            'arbitrary_A22_degeneration_excluded': False,
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
