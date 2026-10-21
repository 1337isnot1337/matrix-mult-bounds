"""Verify exact Newton-window exclusions and a three-weight rank atom.

All acceptance arithmetic uses the Python standard library.  The stored
supporting planes are checked against every admissible integer point;
no numerical hull package or recorded rank claim is trusted.
"""

import argparse
from fractions import Fraction
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location('weight_window_source', HERE / 'parity_balancing_newton_pruning_audit.py')
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)
CERTIFICATE = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_weight_windows.json'


def dot(plane, point):
    return sum(plane[i] * point[i] for i in range(3))


def verify_case(case, planes, polytopes, terms):
    width = case['maximum_source_weight_span']
    selected = case['selected_legs']
    if type(width) is not int or width not in (2, 3, 4):
        raise ArithmeticError('Unexpected source-weight window width')
    if selected not in ([0, 1], [0, 1, 2]):
        raise ArithmeticError('Unexpected selected-leg control')
    masks = [set(range(960)) for _ in range(3)]
    coordinates = [CORE.coordinates(column) for column in range(960)]
    weights = [i + s - k for i, k, s in coordinates]
    expected_starts = list(range(-14, 15 - width))
    stopped = False
    rounds = []
    for step in case['rounds']:
        if stopped:
            raise ArithmeticError('A stored iteration follows a fixed point or contradiction')
        sizes = list(map(len, masks))
        bounds = [27 + sum(sizes[j] - 778 for j in range(3) if j != i) for i in range(3)]
        if step['available_dimensions'] != sizes or step['slice_rank_budgets'] != bounds:
            raise ArithmeticError('A recorded dimension or codimension budget is incorrect')
        ranks = [[0] * 960 for _ in range(3)]
        active = 0
        for term in terms:
            if all(term[i] in masks[i] for i in range(3)):
                active += 1
                for leg in range(3):
                    ranks[leg][term[leg]] += 1
        new_masks = [set(mask) for mask in masks]
        if [entry['leg'] for entry in step['selected_leg_polytopes']] != selected:
            raise ArithmeticError('The actual selected-leg list is incomplete')
        for entry in step['selected_leg_polytopes']:
            leg = entry['leg']
            polytope_ids = entry['polytope_indices']
            if any(type(i) is not int or not 0 <= i < len(polytopes) for i in polytope_ids):
                raise ArithmeticError('An invalid polytope index was supplied')
            selected_polytopes = [polytopes[i] for i in polytope_ids]
            if [poly['minimum_weight'] for poly in selected_polytopes] != expected_starts:
                raise ArithmeticError('Every admissible source-weight interval must be checked')
            keep = set()
            for polytope in selected_polytopes:
                lower = polytope['minimum_weight']
                eligible = [column for column in masks[leg] if lower <= weights[column] <= lower + width]
                good = [column for column in eligible if ranks[leg][column] <= bounds[leg]]
                if len(good) != polytope['admissible_coordinate_count']:
                    raise ArithmeticError('The actual admissible-coordinate count changed')
                plane_ids = polytope['plane_indices']
                if any(type(i) is not int or not 0 <= i < len(planes) for i in plane_ids):
                    raise ArithmeticError('An invalid supporting-plane index was supplied')
                selected_planes = [planes[i] for i in plane_ids]
                for plane in selected_planes:
                    if any(dot(plane, coordinates[column]) > plane[3] for column in good):
                        raise ArithmeticError('A supporting plane cuts an admissible coordinate')
                keep.update(column for column in eligible
                            if all(dot(plane, coordinates[column]) <= plane[3] for plane in selected_planes))
            new_masks[leg] = keep
        retained = list(map(len, new_masks))
        digests = [CORE.digest(mask) for mask in new_masks]
        if retained != step['retained_dimensions'] or digests != step['retained_coordinate_sha256']:
            raise ArithmeticError('The actual retained support differs from the certificate')
        rounds.append({'available_dimensions': sizes, 'slice_rank_budgets': bounds,
                       'retained_dimensions': retained, 'restricted_source_terms': active})
        stopped = new_masks == masks or min(retained) < 778
        masks = new_masks
    if not stopped:
        raise ArithmeticError('The stored calculation stops before a fixed point or contradiction')
    excluded = min(map(len, masks)) < 778
    if case['ordinary_restriction_excluded'] is not excluded:
        raise ArithmeticError('The recorded exclusion claim disagrees with the actual masks')
    return {'maximum_source_weight_span': width, 'selected_legs': selected,
            'rounds': rounds, 'final_available_dimensions': list(map(len, masks)),
            'ordinary_restriction_excluded': excluded}


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
PHI = (Fraction(0), Fraction(1))


def qadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def qneg(x):
    return -x[0], -x[1]


def qmul(x, y):
    return x[0] * y[0] + x[1] * y[1], x[0] * y[1] + x[1] * y[0] + x[1] * y[1]


def qinv(x):
    norm = x[0] * x[0] + x[0] * x[1] - x[1] * x[1]
    if not norm:
        raise ArithmeticError('Division by zero in the exact quadratic field')
    return (x[0] + x[1]) / norm, -x[1] / norm


def qrank(matrix):
    matrix = [list(row) for row in matrix]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(rank, len(matrix)) if matrix[row][column] != ZERO), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = qinv(matrix[rank][column])
        matrix[rank] = [qmul(value, inverse) for value in matrix[rank]]
        for row in range(len(matrix)):
            if row != rank and matrix[row][column] != ZERO:
                factor = matrix[row][column]
                matrix[row] = [qadd(value, qneg(qmul(factor, other)))
                               for value, other in zip(matrix[row], matrix[rank])]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def verify_atom(atom, terms):
    if atom['field_polynomial'] != [1, -1, -1]:
        raise ArithmeticError('The rank atom requires phi^2-phi-1=0')
    coefficients = {}
    for index, value in atom['hankel_coefficients']:
        if type(index) is not int or not 0 <= index < 15 or index in coefficients:
            raise ArithmeticError('An invalid Hankel coefficient index was supplied')
        if len(value) != 2 or any(type(v) is not int for v in value):
            raise ArithmeticError('Integer quadratic-field coordinates are required')
        coefficients[index] = tuple(Fraction(v) for v in value)
    if set(coefficients) != {5, 7, 9} or any(value == ZERO for value in coefficients.values()):
        raise ArithmeticError('The atom must have exactly its three nonzero Hankel coefficients')
    hankel = [[coefficients.get(p + q, ZERO) for q in range(8)] for p in range(8)]
    rank = qrank(hankel)
    if rank != 6:
        raise ArithmeticError('The actual Hankel rank is not six')
    block = [[PHI if i == j else ONE if abs(i - j) == 1 else ZERO for j in range(4)] for i in range(4)]
    kernel = [ONE, qneg(PHI), PHI, qneg(ONE)]
    if any(sum_field(qmul(value, vector) for value, vector in zip(row, kernel)) != ZERO for row in block):
        raise ArithmeticError('The explicit tridiagonal kernel vector failed')
    minor = qadd(qmul(qmul(PHI, PHI), PHI), qneg(qadd(PHI, PHI)))
    if minor != ONE:
        raise ArithmeticError('The explicit three-by-three minor is not one')
    for a in range(4):
        for b in range(4):
            if hankel[2 * a][2 * (3 - b) + 1] != block[a][b]:
                raise ArithmeticError('The actual odd-even block is not the claimed tridiagonal matrix')
            if hankel[2 * a + 1][2 * (3 - b)] != block[a][b]:
                raise ArithmeticError('The actual even-odd block is not the claimed tridiagonal matrix')
    actual = {}
    middle_terms = 0
    for x, y, z in terms:
        i, k, s = CORE.coordinates(x)
        if (i, s) != (0, 7):
            continue
        if k == 7:
            middle_terms += 1
        if k in coefficients:
            if (y, z) in actual:
                raise ArithmeticError('The source-slice coefficient is repeated')
            actual[y, z] = coefficients[k]
    expected = {}
    for r in range(8):
        for j in range(8):
            for p in range(8):
                for q in range(8):
                    value = hankel[p][q]
                    if value != ZERO:
                        expected[CORE.index(p, r + 7, j), CORE.index(r, j, q)] = value
    if actual != expected or len(actual) != 1280 or middle_terms != 512:
        raise ArithmeticError('The complete source slice does not equal 64 disjoint Hankel blocks')
    return {'field': 'Q(phi), phi^2=phi+1', 'source_weights': [-2, 0, 2],
            'actual_hankel_rank': rank, 'actual_disjoint_hankel_blocks': 64,
            'tridiagonal_three_by_three_minor': 1,
            'actual_source_slice_rank': 64 * rank, 'middle_component_slice_rank': middle_terms,
            'initial_full_target_slice_rank_budget': 391,
            'rank_atom_fits_initial_budget': 64 * rank <= 391,
            'middle_component_alone_exceeds_initial_budget': middle_terms > 391,
            'full_target_construction': False}


def sum_field(values):
    total = ZERO
    for value in values:
        total = qadd(total, value)
    return total


def verify(data=None):
    data = json.loads(CERTIFICATE.read_text()) if data is None else data
    if data['format'] != 'exact-source-weight-window-certificate-v1':
        raise ArithmeticError('Unexpected certificate format')
    if data.get('source') != 'A(8,8)' or data.get('target') != 'M27 direct_sum M7':
        raise ArithmeticError('Unexpected source or target label')
    planes = data['supporting_planes']
    if any(not isinstance(plane, list) or len(plane) != 4 or any(type(v) is not int for v in plane) for plane in planes):
        raise ArithmeticError('All supporting planes must have four integer coefficients')
    terms = CORE.source()
    cases = [verify_case(case, planes, data['window_polytopes'], terms) for case in data['cases']]
    if len(cases) != 6 or {(case['maximum_source_weight_span'], tuple(case['selected_legs'])) for case in cases} != {
            (width, selected) for width in (2, 3, 4) for selected in ((0, 1), (0, 1, 2))}:
        raise ArithmeticError('The six documented window controls are required')
    atom = verify_atom(data['three_weight_rank_atom'], terms)
    return {'complete_source_terms_enumerated': len(terms),
            'supporting_planes_checked_exactly': len(planes),
            'all_admissible_weight_intervals_replayed': True,
            'cases': cases, 'three_weight_rank_atom': atom,
            'arbitrary_ungraded_restrictions_excluded': False,
            'arbitrary_degenerations_excluded': False,
            'new_exponent_established': False,
            'external_independent_review': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=CERTIFICATE)
    args = parser.parse_args()
    report = verify(json.loads(args.certificate.read_text()))
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
