"""Replay Gaussian operations invertible over Q[a,t,t^-1]."""
import sympy as sp


def canonical(matrix):
    return sp.SparseMatrix(matrix.applyfunc(sp.expand))


def laurent(value, a, t, require_unit=False):
    numerator, denominator = sp.fraction(sp.cancel(value))
    numerator, denominator = sp.Poly(numerator, a, t), sp.Poly(denominator, a, t)
    if len(denominator.terms()) != 1 or denominator.terms()[0][0][0]:
        return False
    return not require_unit or (not numerator.is_zero and len(numerator.terms()) == 1
                                and numerator.terms()[0][0][0] == 0)


def replay(matrix, steps, a, t, row_basis=False):
    """Every division is by a nonzero rational times a power of t."""
    rows = [{} for _ in range(matrix.rows)]
    for (i, j), value in matrix.todok().items():
        value = sp.cancel(value)
        if not laurent(value, a, t):
            raise ArithmeticError('Input coefficient is not Laurent in t')
        if value:
            rows[i][j] = value
    pivot_rows, pivot_columns = [], []
    transform, inverse = sp.SparseMatrix.eye(matrix.cols), sp.SparseMatrix.eye(matrix.cols)
    for step in steps:
        if step[0] == 'column':
            _, j, k, encoded = step
            ratio = sp.sympify(encoded, locals={'a': a, 't': t})
            if (j == k or not 0 <= j < matrix.cols or not 0 <= k < matrix.cols
                    or j in pivot_columns or k in pivot_columns or not laurent(ratio, a, t)):
                raise ArithmeticError('Invalid Laurent column operation')
            for row in rows:
                value = sp.expand(row.get(j, 0)-ratio*row.get(k, 0))
                if value:
                    row[j] = value
                else:
                    row.pop(j, None)
            transform[:, j] -= ratio*transform[:, k]
            inverse[k, :] += ratio*inverse[j, :]
            continue
        i, j, encoded = step
        scale = sp.sympify(encoded, locals={'a': a, 't': t})
        if (not 0 <= i < matrix.rows or not 0 <= j < matrix.cols
                or i in pivot_rows or j in pivot_columns or not laurent(scale, a, t, True)):
            raise ArithmeticError('Gaussian pivot is not a Laurent unit')
        if sp.cancel(rows[i].get(j, 0)-scale) != 0:
            raise ArithmeticError('Incorrect Gaussian pivot value')
        rows[i] = {k: sp.expand(value/scale) for k, value in rows[i].items()}
        for k, row in enumerate(rows):
            if k == i or j not in row:
                continue
            multiplier = row[j]
            for column, value in rows[i].items():
                updated = sp.expand(row.get(column, 0)-multiplier*value)
                if updated:
                    row[column] = updated
                else:
                    row.pop(column, None)
        pivot_rows.append(i)
        pivot_columns.append(j)
    if any(row for i, row in enumerate(rows) if i not in pivot_rows):
        raise ArithmeticError('Laurent elimination has nonzero residual rows')
    free = [j for j in range(matrix.cols) if j not in pivot_columns]
    if row_basis:
        reduced = sp.SparseMatrix(len(pivot_rows), matrix.cols,
            {(k, j): value for k, i in enumerate(pivot_rows) for j, value in rows[i].items()})
        basis, projection = canonical(reduced*inverse), transform[:, pivot_columns]
        if canonical(matrix-matrix*projection*basis).todok() or canonical(basis*projection-sp.eye(len(pivot_rows))).todok():
            raise ArithmeticError('Invalid complete Laurent row basis')
        return basis, projection
    kernel = sp.MutableSparseMatrix.zeros(matrix.cols, len(free))
    for k, column in enumerate(free):
        kernel[column, k] = 1
        for i, j in zip(pivot_rows, pivot_columns):
            kernel[j, k] = -rows[i].get(column, 0)
    kernel = canonical(transform*kernel)
    if canonical(matrix*kernel).todok():
        raise ArithmeticError('Invalid complete Laurent kernel')
    return kernel
