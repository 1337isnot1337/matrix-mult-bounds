"""Exact physical-stabilizer invariants of matrix multiplication format.

Tensor coordinates are flat indices for U in Mat(r,s), V in Mat(s,t),
and W in Mat(t,r).  All acceptance arithmetic uses rational numbers.
There is no expression evaluator or optional numerical dependency.
"""
from fractions import Fraction
from itertools import product


def dimensions(value):
    if (not isinstance(value, (tuple, list)) or len(value) != 3
            or any(type(n) is not int or n <= 0 for n in value)):
        raise ValueError('Dimensions must be three positive integers.')
    return tuple(value)


def rational(value):
    if type(value) is int or isinstance(value, Fraction):
        return Fraction(value)
    raise ValueError('Coefficients must be exact integers or Fractions.')


def leg_sizes(dims):
    r, s, t = dimensions(dims)
    return r*s, s*t, t*r


def coordinate(key, dims):
    sizes = leg_sizes(dims)
    if (not isinstance(key, tuple) or len(key) != 3
            or any(type(i) is not int or not 0 <= i < n for i, n in zip(key, sizes))):
        raise ValueError('Tensor coordinate is outside its stated shape.')
    return key


def validate_tensor(tensor, dims):
    dimensions(dims)
    if not isinstance(tensor, dict):
        raise ValueError('A sparse tensor must be a coordinate dictionary.')
    for key, value in tensor.items():
        coordinate(key, dims)
        rational(value)
    return tensor


def involution(key, dims):
    """(ij,lm,kn) -> (nl,jk,mi), in row-major matrix coordinates."""
    r, s, t = dimensions(dims)
    a, b, c = coordinate(key, dims)
    i, j = divmod(a, s)
    ell, m = divmod(b, t)
    k, n = divmod(c, r)
    return n*s + ell, j*t + k, m*r + i


def pairing(left, right, dims):
    """Bilinear C(left,right), computed directly from tensor coordinates."""
    validate_tensor(left, dims)
    validate_tensor(right, dims)
    return sum((rational(value) * right.get(involution(key, dims), 0)
                for key, value in left.items()), Fraction(0))


def quadratic(tensor, dims):
    return pairing(tensor, tensor, dims)


def target(dims):
    r, s, t = dimensions(dims)
    return {(i*s+j, j*t+k, k*r+i): Fraction(1)
            for i in range(r) for j in range(s) for k in range(t)}


def trace_tensor(tensor, dims):
    validate_tensor(tensor, dims)
    return sum((tensor.get(key, 0) for key in target(dims)), Fraction(0))


def reshape(tensor, dims):
    """Sparse rst-by-rst matrix, row (i,l,k), column (n,j,m)."""
    validate_tensor(tensor, dims)
    r, s, t = dimensions(dims)
    output = {}
    for (a, b, c), value in tensor.items():
        i, j = divmod(a, s)
        ell, m = divmod(b, t)
        k, n = divmod(c, r)
        if value:
            output[((i*s+ell)*t+k, (n*s+j)*t+m)] = rational(value)
    return output


def sparse_matrix_product(left, right):
    """Internal exact sparse matrix product; indices come from reshape."""
    right_rows = {}
    for (i, j), value in right.items():
        right_rows.setdefault(i, []).append((j, value))
    output = {}
    for (i, k), value in left.items():
        for j, other in right_rows.get(k, ()):
            key = i, j
            output[key] = output.get(key, Fraction(0)) + value*other
    return {key: value for key, value in output.items() if value}


def trace_power(tensor, exponent, dims):
    if type(exponent) is not int or exponent < 1:
        raise ValueError('The trace power must be a positive integer.')
    matrix = reshape(tensor, dims)
    power = matrix
    for _ in range(exponent - 1):
        power = sparse_matrix_product(power, matrix)
    return sum((value for (i, j), value in power.items() if i == j), Fraction(0))


def add_tensors(*tensors):
    output = {}
    for tensor in tensors:
        for key, value in tensor.items():
            output[key] = output.get(key, Fraction(0)) + value
    return {key: value for key, value in output.items() if value}


def validate_factors(term, dims):
    if not isinstance(term, (list, tuple)) or len(term) != 3:
        raise ValueError('A rank-one term must have three factors.')
    for row, size in zip(term, leg_sizes(dims)):
        if not isinstance(row, (list, tuple)) or len(row) != size:
            raise ValueError('A factor does not have its stated matrix shape.')
        for value in row:
            rational(value)


def tensor_from_factors(terms, dims):
    output = {}
    for term in terms:
        validate_factors(term, dims)
        sparse = [[(i, rational(x)) for i, x in enumerate(row) if x] for row in term]
        for (i, u), (j, v), (k, w) in product(*sparse):
            key = i, j, k
            output[key] = output.get(key, Fraction(0)) + u*v*w
    return {key: value for key, value in output.items() if value}


def matrix(row, rows, columns):
    if len(row) != rows*columns:
        raise ValueError('Invalid flat matrix size.')
    return [[rational(x) for x in row[i*columns:(i+1)*columns]] for i in range(rows)]


def matrix_product(left, right):
    if not left or not right or len(left[0]) != len(right):
        raise ValueError('Incompatible matrix product.')
    output = [[Fraction(0) for _ in right[0]] for _ in left]
    for i, row in enumerate(left):
        for k, value in enumerate(row):
            if value:
                for j, other in enumerate(right[k]):
                    if other:
                        output[i][j] += value*other
    return output


def factor_pairing(left, right, dims):
    """Independent backend: tr(U V' W U' V W')."""
    validate_factors(left, dims)
    validate_factors(right, dims)
    r, s, t = dimensions(dims)
    shapes = ((r, s), (s, t), (t, r))
    a = [matrix(row, *shape) for row, shape in zip(left, shapes)]
    b = [matrix(row, *shape) for row, shape in zip(right, shapes)]
    result = a[0]
    for factor in (b[1], a[2], b[0], a[1], b[2]):
        result = matrix_product(result, factor)
    return sum((result[i][i] for i in range(r)), Fraction(0))


def polynomial_terms(family, dims):
    """Expand three vector-valued polynomials into weighted rank-one terms.

    family[leg][degree][coordinate] is a rational coefficient.  The
    result consists of (degree, three constant factors), with zero terms
    omitted.  This does not evaluate or sample the free parameter.
    """
    if not isinstance(family, (list, tuple)) or len(family) != 3:
        raise ValueError('A polynomial term must have three factor polynomials.')
    for polynomial, size in zip(family, leg_sizes(dims)):
        if not isinstance(polynomial, (list, tuple)) or not polynomial:
            raise ValueError('A factor polynomial needs a constant coefficient row.')
        for row in polynomial:
            if not isinstance(row, (list, tuple)) or len(row) != size:
                raise ValueError('Invalid polynomial factor shape.')
            for value in row:
                rational(value)
    output = []
    for choices in product(*(enumerate(polynomial) for polynomial in family)):
        if all(any(row) for _, row in choices):
            output.append((sum(degree for degree, _ in choices),
                           [row for _, row in choices]))
    return output


def polynomial_tensor(families, dims):
    output = {}
    for family in families:
        for degree, term in polynomial_terms(family, dims):
            output[degree] = add_tensors(output.get(degree, {}), tensor_from_factors([term], dims))
    return {degree: tensor for degree, tensor in output.items() if tensor}


def polynomial_pairing(left, right, dims):
    """Pair integer-degree coefficient maps, also allowing Laurent poles."""
    for polynomial in (left, right):
        if not isinstance(polynomial, dict) or any(type(k) is not int for k in polynomial):
            raise ValueError('Polynomial or Laurent exponents must be integers.')
    output = {}
    for a, tensor in left.items():
        for b, other in right.items():
            output[a+b] = output.get(a+b, Fraction(0)) + pairing(tensor, other, dims)
    return {degree: value for degree, value in output.items() if value}


def matrix_polynomial_pairing(left, right, dims):
    """Polynomial pairing by expanded factors and ordinary matrix traces."""
    a = [entry for family in left for entry in polynomial_terms(family, dims)]
    b = [entry for family in right for entry in polynomial_terms(family, dims)]
    output = {}
    for i, term in a:
        for j, other in b:
            output[i+j] = output.get(i+j, Fraction(0)) + factor_pairing(term, other, dims)
    return {degree: value for degree, value in output.items() if value}


def cyclic_product(family, dims):
    """Matrix polynomial U(z)V(z)W(z), before taking its trace."""
    r, s, t = dimensions(dims)
    output = {}
    for degree, term in polynomial_terms(family, dims):
        u, v, w = [matrix(row, *shape) for row, shape in zip(term, ((r, s), (s, t), (t, r)))]
        value = matrix_product(matrix_product(u, v), w)
        if degree not in output:
            output[degree] = [[Fraction(0) for _ in range(r)] for _ in range(r)]
        for i in range(r):
            for j in range(r):
                output[degree][i][j] += value[i][j]
    return {degree: value for degree, value in output.items() if any(map(any, value))}


def square_matrix_polynomial(polynomial):
    output = {}
    for a, left in polynomial.items():
        for b, right in polynomial.items():
            product_matrix = matrix_product(left, right)
            if a+b not in output:
                output[a+b] = [[Fraction(0) for _ in row] for row in product_matrix]
            for i, row in enumerate(product_matrix):
                for j, value in enumerate(row):
                    output[a+b][i][j] += value
    return {degree: value for degree, value in output.items() if any(map(any, value))}
