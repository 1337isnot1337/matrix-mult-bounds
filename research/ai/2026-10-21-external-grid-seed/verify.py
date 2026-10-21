"""Integer replay and finite controls for a fixed external algorithm seed.

The exhaustive flat count is reproduced by the separate C99 program.
This quick verifier does not silently rerun that enumeration.
"""
from fractions import Fraction
from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import argparse
import json

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
REPORT = ROOT / 'results/external-grid-seed-2026-10-21/four-flats.json'


def rank(rows, prime=None):
    a = [[x % prime if prime else Fraction(x) for x in row] for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        k = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        scale = pow(a[pivot][col], -1, prime) if prime else 1 / a[pivot][col]
        a[pivot] = [(x * scale) % prime if prime else x * scale for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            value = a[i][col]
            if value:
                row = [x - value * y for x, y in zip(a[i], a[pivot])]
                a[i] = [x % prime for x in row] if prime else row
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def integer_tensor(factors):
    actual = [0] * 10000
    for a, b, c in zip(factors['u'], factors['v'], factors['w']):
        sparse = [[(i, x) for i, x in enumerate(row) if x] for row in [a, b, c]]
        for (i, x), (j, y), (k, z) in product(*sparse):
            actual[(i * 25 + j) * 20 + k] += x * y * z
    expected = [0] * 10000
    for i, j, k in product(range(4), range(5), range(5)):
        expected[((5 * i + j) * 25 + 5 * j + k) * 20 + 4 * k + i] = 1
    return actual, expected


def term_traces(factors):
    """The linear trace invariant after regrouping into End(U tensor V tensor W)."""
    return [sum(a[5*i+j] * b[5*j+k] * c[4*k+i]
                for i, j, k in product(range(4), range(5), range(5)))
            for a, b, c in zip(factors['u'], factors['v'], factors['w'])]


def verify():
    raw = (PACKAGE / 'factors.json').read_bytes()
    data = json.loads(raw)
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    if sha256(raw).hexdigest() != sources['retained_factors_sha256']:
        raise ArithmeticError('External factor arrays differ from the pinned extraction.')
    if data['n'] != [4, 5, 5] or data['m'] != 76 or data['z2'] is not False:
        raise ArithmeticError('Unexpected external algorithm format or field.')
    for key, width in [('u', 20), ('v', 25), ('w', 20)]:
        if len(data[key]) != 76 or any(len(row) != width for row in data[key]):
            raise ArithmeticError('Invalid external factor dimensions.')
        if any(type(x) is not int for row in data[key] for x in row):
            raise ArithmeticError('The external coefficient replay must use integers.')
    actual, expected = integer_tensor(data)
    if actual != expected:
        raise ArithmeticError('The external factorization fails the full integer identity.')
    traces = Counter(term_traces(data))
    if traces != {1: 52, 2: 24}:
        raise ArithmeticError('Unexpected termwise trace-invariant values.')
    report = json.loads(REPORT.read_text())
    if (report['prime'], report['vectors'], report['dimension']) != (101, 76, 20):
        raise ArithmeticError('Unexpected flat-enumeration parameters.')
    if rank(data['u'], 101) != 20:
        raise ArithmeticError('The finite-field factor span is not full.')
    if report['four_subsets'] != comb(76, 4):
        raise ArithmeticError('The stored run does not cover all four-subsets.')
    counts = {int(k): v for k, v in report['basis_weighted_histogram'].items()}
    if sum(counts.values()) != report['independent_four_subsets']:
        raise ArithmeticError('The enumeration counters disagree.')
    if max(counts) != report['maximum_flat_cardinality'] or max(counts) != 8:
        raise ArithmeticError('The stored maximum does not equal eight.')
    basis = [data['u'][i] for i in report['witness_basis']]
    members = [i for i, vector in enumerate(data['u']) if rank(basis + [vector], 101) == 4]
    if members != report['witness_members'] or len(members) != 8:
        raise ArithmeticError('The recorded finite-field flat witness is incorrect.')
    if rank([data['u'][i] for i in members]) != 4:
        raise ArithmeticError('The displayed extremal flat is not rational rank four.')
    outside = next(i for i in range(76) if i not in members)
    if rank([data['u'][i] for i in members + [outside]]) != 5:
        raise ArithmeticError('The nine-vector negative control did not leave rank four.')
    return {
        'integer_identity_verified': True,
        'target_coefficient_positions_checked': 10000,
        'external_rank_one_terms': 76,
        'term_trace_invariant_histogram': dict(traces),
        'nonempty_subset_deletion_by_target_stabilizer_excluded': True,
        'target_nonzero_coefficients': sum(bool(x) for x in expected),
        'u_span_rank_mod_101': 20,
        'stored_exhaustive_four_subsets': report['four_subsets'],
        'stored_maximum_four_flat_cardinality': 8,
        'extremal_flat_verified_over_rationals': True,
        'nine_vector_negative_control_rank': 5,
        'nine_groups_upper_capacity': 72,
        'termwise_evaluation_grid_seed_excluded': True,
        'exhaustive_enumeration_rerun_by_this_command': False,
        'general_Q64_maps_excluded': False,
        'new_matrix_algorithm': False,
        'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-u', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = verify()
    if args.write_u:
        data = json.loads((PACKAGE / 'factors.json').read_text())
        args.write_u.write_text('\n'.join(' '.join(map(str, row)) for row in data['u']) + '\n')
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
