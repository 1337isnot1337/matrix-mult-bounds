"""Exact first-jet constraints for the normalized order-three/six root flags."""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
from itertools import product
import json
from pathlib import Path

import sympy as sp

V = 112
LONG = (1, 2, 4, 5)
PRIME = 786433


def index(i, j, z):
    return (4*i+j)*7+z


G = [{index(0, 3, z): 1, index(3, 0, z): -1} for z in LONG]
EB = [{index(p, j, z): 1} for p, j, z in product((0, 3), (0, 3), LONG)]
EB += [{index(0, j, z): 1, index(3, j, z-3): 1}
       for j, z in product((1, 2), (4, 5))]
EC = [{index((k//7) % 4, k//28, k % 7): value for k, value in row.items()}
      for row in EB]
A0 = [index(i, s, z) for i, s, z in product((1, 2), (1, 2), (0, 3, 6))]
OUTSIDE = [i for i in range(V) if i not in A0]
TERMS = [(index(i, s, 6-p-q), index(p, j, 6-r-s), index(r, q, 6-i-j))
         for i, j, p, q, r, s in product(range(4), repeat=6)]


def contract(left, right, rows):
    """Contract all 4096 integer source terms, retaining specified first rows."""
    by_left, by_right = defaultdict(list), defaultdict(list)
    for b, row in enumerate(left):
        for k, value in row.items():
            by_left[k].append((b, value))
    for c, row in enumerate(right):
        for k, value in row.items():
            by_right[k].append((c, value))
    positions = {a: i for i, a in enumerate(rows)}
    entries = defaultdict(int)
    for a, b, c in TERMS:
        if a in positions:
            for j, x in by_left[b]:
                for k, y in by_right[c]:
                    entries[positions[a], j*len(right)+k] += x*y
    return sp.MutableSparseMatrix(len(rows), len(left)*len(right), dict(entries))


def rational_rank(matrix):
    return len(matrix.to_DM().rref()[1])


def rank_certificate(matrix):
    """Rational upper rank plus an independently replayable modular minor."""
    pivots, ids, cols = {}, [], []
    for i in range(matrix.rows):
        row = {j: int(matrix[i, j]) % PRIME for j in range(matrix.cols)
               if matrix[i, j] % PRIME}
        while row:
            col = min(row)
            if col not in pivots:
                scale = pow(row[col], -1, PRIME)
                pivots[col] = {j: x*scale % PRIME for j, x in row.items()}
                ids.append(i)
                cols.append(col)
                break
            scale = row[col]
            for j, x in pivots[col].items():
                value = (row.get(j, 0)-scale*x) % PRIME
                if value:
                    row[j] = value
                else:
                    row.pop(j, None)
    rank = rational_rank(matrix)
    if rank != len(ids):
        raise ArithmeticError('Modular minor did not attain the rational rank')
    # All selected pivots were nonzero. Export the actual submatrix indices,
    # and compute its determinant by separate dense modular elimination.
    minor = [[int(matrix[i, j]) % PRIME for j in cols] for i in ids]
    determinant = 1
    for j in range(rank):
        pivot = next(i for i in range(j, rank) if minor[i][j])
        if pivot != j:
            minor[pivot], minor[j] = minor[j], minor[pivot]
            determinant = -determinant
        value = minor[j][j]
        determinant = determinant*value % PRIME
        inverse = pow(value, -1, PRIME)
        for i in range(j+1, rank):
            factor = minor[i][j]*inverse % PRIME
            if factor:
                for k in range(j+1, rank):
                    minor[i][k] = (minor[i][k]-factor*minor[j][k]) % PRIME
    return {'shape': list(matrix.shape), 'rational_rank': rank,
            'minor_rows': ids, 'minor_columns': cols,
            'minor_determinant_mod_prime': determinant % PRIME}


@lru_cache(None)
def matrices():
    first = contract(G, G, range(V))
    identity = [{i: 1} for i in range(V)]
    left = contract(identity, G, OUTSIDE)
    right = contract(G, identity, OUTSIDE)
    cb = sp.Matrix(400, V, lambda r, c: left[r//4, 4*c+r % 4])
    cc = sp.Matrix(400, V, lambda r, c: right[r//4, V*(r % 4)+c])
    annihilator = sp.Matrix.hstack(*first.nullspace()).T
    top = sp.MutableSparseMatrix(400, 896, {})
    for x, k in product(range(100), range(4)):
        for b, u in product(range(4), range(V)):
            value = sum(annihilator[k, 4*b+c]*left[x, 4*u+c] for c in range(4))
            if value:
                top[4*x+k, V*b+u] = value
        for c, v in product(range(4), range(V)):
            value = sum(annihilator[k, 4*b+c]*right[x, V*b+v] for b in range(4))
            if value:
                top[4*x+k, 448+V*c+v] = value
    return first, cb, cc, contract(EB, EC, OUTSIDE), top, annihilator


def root_normalizations():
    path = Path(__file__).resolve().parents[1] / '2026-10-20-graded-quantum-flags/one_leg.py'
    spec = importlib.util.spec_from_file_location('extension_root_flags', path)
    flags = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(flags)
    field, _ = flags.quadratic_field()
    records = []
    for phase in ((6, 1), (3, 1), (3, 2), (6, 5)):
        by_row = defaultdict(dict)
        for (i, j), value in flags.exact_phase_map(phase).items():
            if value:
                by_row[i][j] = value
        if sorted(by_row) != [70, 71, 73, 74]:
            raise ArithmeticError('Changed leading row support')
        for (_, row), expected in zip(sorted(by_row.items()), G):
            scale = row[min(row)]
            if {j: value/scale for j, value in row.items()} != {
                    j: field.convert(value) for j, value in expected.items()}:
                raise ArithmeticError('Root normalization differs from G')
        records.append({'phase': list(phase), 'normalized_rows_equal_G': True})
    return records


def report():
    first, cb, cc, next_term, top, annihilator = matrices()
    support = [i for i in range(V) if any(first.row(i))]
    assert support == A0
    for constraints, basis in ((cb, EB), (cc, EC)):
        b = sp.Matrix(20, V, lambda i, j: basis[i].get(j, 0))
        assert rational_rank(b) == 20
        assert constraints*b.T == sp.zeros(400, 20)
    assert all(next_term[x, 20*b+c] == 0
               for x, b, c in product(range(100), range(16), range(16)))
    records = {name: rank_certificate(matrix) for name, matrix in (
        ('leading', first), ('left_extension_constraints', cb),
        ('right_extension_constraints', cc), ('bilinear_next', next_term),
        ('coupled_top_constraints', top))}
    assert [r['rational_rank'] for r in records.values()] == [12, 92, 92, 25, 364]
    return {'prime': PRIME, 'field': 'Q; root normalization over Q(zeta_6)',
            'source_terms': len(TERMS), 'G': G, 'E_B': EB, 'E_C': EC,
            'leading_first_support': A0, 'root_normalizations': root_normalizations(),
            'rank_certificates': records,
            'leading_rowspace_annihilator': [[int(x) for x in row]
                                            for row in annihilator.tolist()],
            'coupled_top_kernel_dimension': 532,
            'bilinear_next_zero_boundary_square': [16, 16],
            'bilinear_next_matrix_rank_upper_bound': 8,
            'first_jet_solution_dimension_for_110_output_rows': 4772,
            'scope': 'Necessary fixed-leading first-jet conditions, not a degeneration or an exponent improvement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
