"""Universal auxiliary splitting and joint-support certificates at A4 flags."""
import argparse
from collections import defaultdict
from functools import lru_cache
import gzip
import importlib.util
from itertools import combinations
import json
from pathlib import Path

import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / 'results/asymmetric-boundary-2026-10-23'
PRIME = 32003


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode(matrix):
    return {'shape': list(matrix.shape), 'entries': [
        [i, j, str(z)] for (i, j), z in sorted(matrix.todok().items()) if z]}


def decode(record):
    return sp.MutableSparseMatrix(*record['shape'], {
        (i, j): sp.Rational(z) for i, j, z in record['entries']})


def rank(matrix):
    return len(matrix.to_DM().rref()[1])


@lru_cache(None)
def predecessor():
    return load('research/ai/2026-10-21-biform-third-core/verify.py',
                'asymmetric_biform_source')


@lru_cache(None)
def split_obstruction():
    old = predecessor().previous_minors()
    data = old.normal.data()
    left, right = (data[key][:2400, :] for key in
                   ('left_obstruction', 'right_obstruction'))
    kernel, _ = old.normal.sparse_nullspace(left)
    assert kernel.cols == 100 and not (left * kernel).todok()
    coefficient = right * kernel
    halves = [sp.MutableSparseMatrix(200, 600, {
        (flat % 200, 6*k + (flat//200)//2): z
        for (flat, k), z in coefficient.todok().items()
        if flat//200 % 2 == parity}) for parity in (0, 1)]
    rows = list(halves[0].T.to_DM().rref()[1])
    assert len(rows) == 42
    half = halves[0][rows, :]
    columns = list(half.to_DM().rref()[1])
    inverse = half[:, columns].inv()
    transforms = [h[:, columns] * inverse for h in halves]
    assert all(t * half == h for t, h in zip(transforms, halves))
    embedding = sp.MutableSparseMatrix(200, 84, {
        (i, 2*j + parity): z for parity, t in enumerate(transforms)
        for (i, j), z in t.todok().items()})
    assert rank(embedding) == 84
    reduced = sp.MutableSparseMatrix(252, 100, {
        (42*j+i, k): z for (i, flat), z in half.todok().items()
        for k, j in [divmod(flat, 6)]})
    assert rank(reduced) == 72
    zero, _ = old.normal.sparse_nullspace(reduced)
    assert zero.cols == 28 and not (coefficient * zero).todok()
    control = next(k for k in range(100) if rank(sp.Matrix(
        42, 6, lambda i, j: reduced[42*j+i, k])) == 2)
    control_matrix = sp.Matrix(42, 6, lambda i, j: reduced[42*j+i, control])
    small_span, _ = old.normal.sparse_nullspace(control_matrix)
    assert small_span.cols == 4
    return {
        'full_side_kernel': encode(kernel),
        'other_side_coefficient_map': encode(coefficient),
        'half_coefficient_map': encode(reduced),
        'embedding': encode(embedding),
        'embedding_rank': 84,
        'half_shape': [42, 6], 'half_coefficient_rank': 72,
        'zero_kernel': encode(zero),
        'sharp_normal_parameter': control,
        'sharp_product_first_span': encode(sp.kronecker_product(small_span, sp.eye(2))),
        'sharp_obstruction_rank': 4,
    }


def repeated_cubes(coefficient):
    """Only force forms with exact triangular cubic determinant identities."""
    old = predecessor().previous_minors()
    current = coefficient
    stages = []
    while current.todok():
        byrow = defaultdict(dict)
        for (i, j), z in current.todok().items():
            byrow[i][j] = z
        forms, indices, positions = [], {}, defaultdict(list)
        table = [[0]*6 for _ in range(24)]
        for flat, row in sorted(byrow.items()):
            form = old.primitive_form(row)
            if form not in indices:
                indices[form] = len(forms) + 1
                forms.append(form)
            index = indices[form]
            i, j = divmod(flat, 6)
            table[i][j] = index
            positions[index].append((i, j))
        chosen, minors = [], []
        for index, form in enumerate(forms, 1):
            witness = old.triangular_witness(table, positions[index], size=3)
            if witness is None:
                continue
            linear = sp.MutableSparseMatrix(1, current.cols,
                {(0, j): z for j, z in form})
            scales = []
            for k, (i, j) in enumerate(witness):
                column, value = form[0]
                scale = current[6*i+j, column] / value
                assert scale and current[6*i+j, :] == scale * linear
                assert all(not current[6*i+future, :].todok()
                           for _, future in witness[k+1:])
                scales.append(scale)
            chosen.append(linear)
            minors.append({'positions': [list(x) for x in witness],
                           'linear_form': encode(linear),
                           'determinant_ratio': str(sp.prod(scales))})
        if not chosen:
            break
        constraints = sp.Matrix.vstack(*chosen)
        kernel, _ = old.normal.sparse_nullspace(constraints)
        stages.append({'parameter_dimension': current.cols,
                       'forced_rank': current.cols-kernel.cols,
                       'minors': minors, 'kernel': encode(kernel)})
        current = current * kernel
    return current, stages


def independent_modular_rows(matrix):
    """Export a square coefficient minor with a nonzero modular determinant."""
    pivots, selected, determinant = {}, [], 1
    for index in range(matrix.rows):
        row = {j: int(z) % PRIME for j, z in matrix.row(index).todok().items()}
        # Matrix row dictionaries use (0,j) keys.
        row = {j[1]: z for j, z in row.items() if z}
        for column, pivot in pivots.items():
            factor = row.get(column, 0)
            if factor:
                for j, z in pivot.items():
                    value = (row.get(j, 0) - factor*z) % PRIME
                    if value:
                        row[j] = value
                    else:
                        row.pop(j, None)
        if not row:
            continue
        column = min(row)
        scale = row[column]
        determinant = determinant * scale % PRIME
        inverse = pow(scale, -1, PRIME)
        pivots[column] = {j: z*inverse % PRIME for j, z in row.items()}
        selected.append(index)
        if len(selected) == matrix.cols:
            break
    assert len(selected) == matrix.cols
    # The selected pivots can appear in a permutation of the column order.
    order = list(pivots)
    inversions = sum(order[i] > order[j] for i in range(len(order))
                     for j in range(i+1, len(order)))
    if inversions % 2:
        determinant = -determinant % PRIME
    assert determinant
    return selected, determinant


def support_certificate(coefficient):
    current, stages = repeated_cubes(coefficient)
    columns = list(current.to_DM().rref()[1])
    basis = current[:, columns]
    assert basis.cols == 12
    rows = list(basis.T.to_DM().rref()[1])
    parameter_map = basis[rows, :].inv() * current[rows, :]
    assert basis * parameter_map == current and rank(parameter_map) == 12
    polynomial_ring, *variables = ring('x:12', QQ)
    table = [[sum((polynomial_ring(z) * variables[k] for k in range(12)
                   if (z := basis[6*i+j, k])), polynomial_ring.zero)
              for j in range(6)] for i in range(24)]
    unique = {}
    for selected_rows in combinations(range(24), 3):
        for selected_columns in combinations(range(6), 3):
            a, b, c = [[table[i][j] for j in selected_columns] for i in selected_rows]
            minor = (a[0]*(b[1]*c[2]-b[2]*c[1])
                     - a[1]*(b[0]*c[2]-b[2]*c[0])
                     + a[2]*(b[0]*c[1]-b[1]*c[0]))
            if minor:
                # Primitive normalization avoids modular division by a denominator.
                _, primitive = minor.primitive()
                if primitive.LC < 0:
                    primitive = -primitive
                unique.setdefault(tuple(sorted(primitive.items())),
                                  (primitive, selected_rows, selected_columns))
    monomials = sorted({mon for f, _, _ in unique.values() for mon in f})
    assert len(monomials) == 364
    lookup = {mon: i for i, mon in enumerate(monomials)}
    coefficients = sp.MutableSparseMatrix(len(unique), 364, {
        (i, lookup[mon]): sp.Rational(z.numerator, z.denominator)
        for i, (f, _, _) in enumerate(unique.values()) for mon, z in f.items()})
    selected, determinant = independent_modular_rows(coefficients)
    all_minors = list(unique.values())
    sharp = next(j for j in range(coefficient.cols) if rank(sp.Matrix(
        24, 6, lambda i, k: coefficient[6*i+k, j])) == 3)
    return {
        'initial_shape': [24, 6], 'stages': stages,
        'remaining_coefficient_map': encode(current),
        'basis': encode(basis), 'parameter_map': encode(parameter_map),
        'cubic_monomials': [list(mon) for mon in monomials],
        'candidate_minor_count': len(unique),
        'selected_minors': [{'rows': list(all_minors[i][1]),
                             'columns': list(all_minors[i][2])} for i in selected],
        'coefficient_matrix': encode(coefficients[selected, :]),
        'prime': PRIME, 'determinant_mod_prime': determinant,
        'minimum_nonzero_joint_support': 3,
        'sharp_original_parameter': sharp,
    }


def projection_controls():
    skew = []
    for j in (1, 2):
        m = sp.zeros(3)
        m[0, j], m[j, 0] = 1, -1
        skew.append(m)
    amplified = [sp.kronecker_product(m, sp.eye(2)[:, [i]] * sp.eye(2)[[j], :])
                 for m in skew for i in range(2) for j in range(2)]
    def image_rank(matrices, columns):
        return rank(sp.Matrix.vstack(*[sp.Matrix(1, 6*len(columns),
                    list(m[:, columns])) for m in matrices]))
    positive = image_rank(amplified, [4, 5])
    excessive_loss = image_rank(amplified, [4])
    assert positive == 4 and excessive_loss == 2
    return {'sharp_positive_first_rank': positive,
            'five_dimensional_loss_first_rank': excessive_loss,
            'base_matrices': [encode(m) for m in skew]}


@lru_cache(None)
def reports():
    # Rebuild every core coefficient against the predecessor source tensor.
    structure = predecessor().biform_structure()
    core = predecessor().decode(structure['core'])
    transposed = core[[36*k+6*j+i for k in range(4)
                       for i in range(6) for j in range(6)], :]
    return {'split_obstruction': split_obstruction(),
            'joint_row_support': support_certificate(core),
            'joint_column_support': support_certificate(transposed),
            'projection_controls': projection_controls()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = reports()
    path = RESULTS / 'certificates.json.gz'
    if args.write:
        RESULTS.mkdir(parents=True, exist_ok=True)
        payload = (json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n').encode()
        path.write_bytes(gzip.compress(payload, mtime=0))
    else:
        assert result == json.loads(gzip.decompress(path.read_bytes()))
    print(json.dumps({'verified': True, 'half_shape': [42, 6],
                      'joint_support_minimum': 3, 'exponent_improvement': False}))


if __name__ == '__main__':
    main()
