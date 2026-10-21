"""Exact rational reference for the fixed-width product-injection loss.

The maps give M(n-1,4,n-1) only at n=5.  At larger n they give an
explicit projected tensor with a nonzero, exactly computed coefficient
error.  This is a reference identity, not a better exponent.
"""
from fractions import Fraction
from itertools import product
import json

from q54_numeric_replay import contract


def zeros(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def product_and_dual(n):
    if type(n) is not int or n < 5:
        raise ValueError('The stated product reference requires n >= 5.')
    r, m = n-1, n+3
    outer = zeros(r, n)
    for i in range(r-1):
        outer[i][i+1] = 1
    outer[-1][0], outer[-1][-1] = 1, -1
    products = zeros(2*r, m)
    for i, v, p in product(range(r), range(2), range(n)):
        products[2*i+v][p+3*v] += outer[i][p]
    dual = zeros(2*r, m)
    for i, v in product(range(r-1), range(2)):
        exponent = i+1+3*v
        duplicate = 4 <= exponent <= n-2
        dual[2*i+v][exponent] = Fraction(1, 2) if duplicate else 1
        if exponent == 3:
            dual[2*i+v][n+2] = 1
        if exponent == n-1:
            dual[2*i+v][0] = 1
    dual[2*r-2][0] = 1
    dual[2*r-1][n+2] = -1
    projection = [[sum(x*y for x, y in zip(row, product_row))
                   for product_row in products] for row in dual]
    expected = [[int(i == j) for j in range(2*r)] for i in range(2*r)]
    duplicate_pairs = []
    for exponent in range(4, n-1):
        pair = [2*(exponent-1), 2*(exponent-4)+1]
        duplicate_pairs.append(pair)
        for i, j in product(pair, repeat=2):
            expected[i][j] = Fraction(1, 2)
    if projection != expected:
        raise ArithmeticError('The rational dual did not give the asserted block projection.')
    reverse = [[sum(products[k][i]*dual[k][j] for k in range(2*r))
                for j in range(m)] for i in range(m)]
    if reverse != [[int(i == j) for j in range(m)] for i in range(m)]:
        raise ArithmeticError('The product output map is not a right inverse.')
    if sum(projection[i][i] for i in range(2*r)) != m:
        raise ArithmeticError('The reference projection rank changed.')
    return outer, products, dual, projection, duplicate_pairs


def maps(n):
    r, m = n-1, n+3
    outer, _, dual, _, _ = product_and_dual(n)
    first, second, third = [zeros(rows, columns) for rows, columns
                            in [(r*r, n*n), (4*r, 4*m), (4*r, 4*m)]]
    for i, k, p, q in product(range(r), range(r), range(n), range(n)):
        first[r*i+k][n*p+q] = outer[k][p]*outer[i][q]
    for i, y, v, s in product(range(r), range(2), range(2), range(m)):
        second[4*i+2*y+v][m*(3*y)+s] = dual[2*i+v][s]
    for k, y, v, s in product(range(r), range(2), range(2), range(m)):
        third[r*(2*y+v)+k][4*s+3*v] = dual[2*k+y][s]
    return [first, second, third]


def verify(n):
    r, m = n-1, n+3
    _, _, _, projection, pairs = product_and_dual(n)
    actual, target = contract(n, 4, r, maps(n))
    # Check the whole paired coefficient formula, including all zero entries.
    wanted_projection = [0]*len(actual)
    for i, k, ib, jb, jc, kc in product(range(r), range(r), range(r), range(4), range(4), range(r)):
        yb, vb = divmod(jb, 2)
        yc, vc = divmod(jc, 2)
        value = projection[2*ib+vb][2*i+vc]*projection[2*kc+yc][2*k+yb]
        wanted_projection[((r*i+k)*(4*r)+4*ib+jb)*(4*r)+r*jc+kc] = value
    if actual != wanted_projection:
        raise ArithmeticError('The complete paired projection identity failed.')
    norm_actual = sum(x*x for x in actual)
    inner = sum(x*y for x, y in zip(actual, target))
    squared_error = sum((x-y)**2 for x, y in zip(actual, target))
    if (norm_actual, inner, squared_error) != (m*m, m*m, 4*r*r-m*m):
        raise ArithmeticError('The rational projection error formula failed.')
    defect = n-5
    for i, k, ib, kc in product(range(defect), repeat=4):
        position = ((r*i+k)*(4*r)+4*ib+3)*(4*r)+3*r+kc
        expected_error = Fraction(3, 4) if (i, k) == (ib, kc) else 0
        if target[position]-actual[position] != expected_error:
            raise ArithmeticError('The explicit first-flattening repair minor failed.')
    relative_squared = Fraction(squared_error, 4*r*r)
    return {'source': f'Q({n},4)', 'comparison_target': f'M({r},4,{r})',
            'n': n, 'auxiliary_rank': 0, 'coefficient_field': 'Q',
            'product_input_dimension': 2*r, 'product_output_rank': m,
            'duplicate_input_pairs': pairs,
            'all_source_terms_reconstructed': 16*n*n,
            'all_target_coefficient_positions_checked': len(actual),
            'target_nonzero_positions': 4*r*r,
            'actual_squared_norm': int(norm_actual),
            'inner_product_with_target': int(inner),
            'exact_squared_coefficient_error': int(squared_error),
            'exact_relative_squared_error': [relative_squared.numerator, relative_squared.denominator],
            'long_map_ranks': [2*m, 2*m],
            'repair_first_flattening_diagonal_minor_size': defect*defect,
            'repair_minor_diagonal_entry': [3, 4],
            'fixed_reference_repair_border_rank_lower_bound': defect*defect,
            'exact_projection_identity_verified': True,
            'exact_matrix_multiplication_target_reached': n == 5,
            'improves_omega': False}


if __name__ == '__main__':
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, nargs='+', default=[5, 6, 7])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = {'references': [verify(n) for n in args.n],
              'general_formula': 'relative_error_squared = 1-(n+3)^2/(4*(n-1)^2), n>=5',
              'limiting_relative_error_squared': [3, 4],
              'saved_floating_search_maps_certified_exact': False,
              'improves_omega': False}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
