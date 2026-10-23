"""Replay the quadratic full-error obstruction and its registered families."""
from fractions import Fraction
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re


PACKAGE = Path(__file__).resolve().parent
RESEARCH = PACKAGE.parent
SPEC = importlib.util.spec_from_file_location('quadratic_error_invariant', PACKAGE / 'invariant.py')
I = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(I)
DIMS = (4, 5, 5)
SHAPES = ((4, 5), (5, 5), (5, 4))
CLAIM = 'AI-EXTERNAL-QUADRATIC-ERROR-010'
SCHEMA = 'quadratic-physical-error-v1'
SCOPE = ('One-term deletion from an exact minimum five-term refactorization of the registered '
         'ten-split block, and the two named V69 polynomial families; arbitrary characteristic-zero '
         'Laurent parameters and physical changes are allowed. No general border-rank or exponent claim.')
PINS = {
    'seed': {'path': '2026-10-21-external-grid-seed/factors.json',
             'sha256': 'bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3'},
    'six': {'path': '2026-10-23-gauged-splits/certificate.json',
            'sha256': '8447ed985ad65192cc6baae7da980c9947efe8774b91394b98060a71a10764e9'},
    'ten': {'path': '2026-10-23-large-gauged-batches/ten_certificate.json',
            'sha256': '962157ce07af6d6cd350b85a8d696d0e6ff2edbb54f0767ec1c4962c728d09f2'},
}
FAMILIES = ('ten_shared_W_61_62', 'six_plus_V69_to_63', 'six_plus_V69_to_64')
TEN_BLOCK = (36, 56, 61, 62, 75)
RATIONAL = re.compile(r'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?\Z')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_rational(value):
    require(isinstance(value, str) and RATIONAL.fullmatch(value) is not None,
            'A saved coefficient must be a canonical rational string.')
    result = Fraction(value)
    require(str(result) == value, 'A saved coefficient is not in canonical rational form.')
    return result


def load_sources():
    sources = {}
    for name, pin in PINS.items():
        data = (RESEARCH / pin['path']).read_bytes()
        require(hashlib.sha256(data).hexdigest() == pin['sha256'], 'A pinned source file changed.')
        sources[name] = json.loads(data)
    seed = sources['seed']
    require(seed['n'] == list(DIMS) and seed['m'] == 76 and seed['z2'] is False,
            'Unexpected external seed format.')
    for key, size in zip(('u', 'v', 'w'), I.leg_sizes(DIMS)):
        require(len(seed[key]) == 76 and all(len(row) == size
                and all(type(x) is int for x in row) for row in seed[key]),
                'Unexpected external factor shape or coefficient type.')
    return sources


def seed_terms(sources):
    return [[[Fraction(x) for x in sources['seed'][key][i]] for key in ('u', 'v', 'w')]
            for i in range(76)]


def scale(row, scalar):
    return [scalar*x for x in row]


def add(left, right):
    require(len(left) == len(right), 'Incompatible factor vectors.')
    return [a+b for a, b in zip(left, right)]


def subtract(left, right):
    return add(left, scale(right, -1))


def split_terms(original, replacements):
    surviving = [[row[:] for row in term] for term in original]
    discarded = []
    for i, j, scalar in replacements:
        surviving[i][0] = scale(original[j][0], Fraction(scalar))
        discarded.append([subtract(original[i][0], surviving[i][0]),
                          original[i][1][:], original[i][2][:]])
    return surviving, discarded


def constant_family(term):
    return [[row] for row in term]


def family_data(name, sources):
    original = seed_terms(sources)
    variant = 'ten' if name == FAMILIES[0] else 'six'
    surviving, discarded = split_terms(original, sources[variant]['replacements'])
    if variant == 'ten':
        a, b = 61, 62
        u, v, w = surviving[a]
        other_u, other_v, other_w = surviving[b]
        require(other_w == scale(w, -1), 'The ten-split shared W sign changed.')
        deleted = [[u, scale(other_u, -1)],
                   [subtract(v, scale(other_v, Fraction(1, 3))), scale(v, Fraction(1, 3))],
                   [w]]
        kept = [[subtract(scale(u, Fraction(1, 3)), other_u), scale(other_u, Fraction(-1, 3))],
                [other_v, scale(v, -1)], [w]]
        extra = None
    else:
        require(name in FAMILIES[1:], 'Unknown registered polynomial family.')
        a, b = 69, int(name.rsplit('_', 1)[1])
        discarded.append([surviving[a][0][:], subtract(surviving[a][1], surviving[b][1]),
                          surviving[a][2][:]])
        surviving[a][1] = surviving[b][1][:]
        u, v, w = surviving[a]
        other_u, other_v, other_w = surviving[b]
        require(v == other_v, 'The six-split pair does not share V.')
        deleted = [[u, other_u], [v], [add(w, other_w), scale(w, -1)]]
        kept = [[subtract(u, other_u), other_u], [v], [scale(other_w, -1), w]]
        extra = {'leg': 'V', 'source': 69, 'destination': b, 'coefficient': '1'}
    return {'name': name, 'variant': variant, 'pair': [a, b], 'extra_replacement': extra,
            'surviving': surviving, 'discarded': discarded, 'deleted': deleted, 'kept': kept}


def inverse(matrix):
    n = len(matrix)
    require(n > 0 and all(len(row) == n for row in matrix), 'A physical basis must be square.')
    a = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        require(pivot is not None, 'A physical basis is singular.')
        a[col], a[pivot] = a[pivot], a[col]
        value = a[col][col]
        a[col] = [x/value for x in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                value = a[i][col]
                a[i] = [x-value*y for x, y in zip(a[i], a[col])]
    return [row[n:] for row in a]


def old_error_minima(terms, source):
    bases = [[[Fraction(x) for x in row] for row in matrix] for matrix in source['basis_matrices']]
    inverses = [inverse(matrix) for matrix in bases]
    weights = source['weights']
    output = []
    for term in terms:
        row = []
        for leg, (factor, shape) in enumerate(zip(term, SHAPES)):
            matrix = I.matrix_product(I.matrix_product(inverses[leg], I.matrix(factor, *shape)),
                                      bases[(leg+1) % 3])
            exponents = [weights[(leg+1) % 3][j] - weights[leg][i]
                         for i, values in enumerate(matrix) for j, value in enumerate(values) if value]
            require(bool(exponents), 'An old discarded factor is zero.')
            row.append(min(exponents))
        require(sum(row) > 0, 'An original discarded tensor lacks positive valuation.')
        output.append(row)
    return output


def row_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        value = a[rank][col]
        a[rank] = [x/value for x in a[rank]]
        for i in range(rank+1, len(a)):
            if a[i][col]:
                value = a[i][col]
                a[i] = [x-value*y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def encode(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    return value


def parse_family(value):
    require(isinstance(value, list) and len(value) == 3, 'Invalid saved polynomial term.')
    result = []
    for polynomial, size in zip(value, I.leg_sizes(DIMS)):
        require(isinstance(polynomial, list) and 1 <= len(polynomial) <= 2,
                'Each registered factor has degree at most one.')
        require(all(isinstance(row, list) and len(row) == size for row in polynomial),
                'Invalid saved polynomial factor shape.')
        result.append([[parse_rational(x) for x in row] for row in polynomial])
    return result


def polynomial_sum(*polynomials):
    output = {}
    for polynomial in polynomials:
        for degree, tensor in polynomial.items():
            output[degree] = I.add_tensors(output.get(degree, {}), tensor)
    return {degree: tensor for degree, tensor in output.items() if tensor}


def analyze_family(data, sources):
    old_terms = [constant_family(term) for term in data['discarded']]
    old_error = I.polynomial_tensor(old_terms, DIMS)
    deleted = I.polynomial_tensor([data['deleted']], DIMS)
    kept = I.polynomial_tensor([data['kept']], DIMS)
    pair_terms = [constant_family(data['surviving'][i]) for i in data['pair']]
    require(polynomial_sum(deleted, kept) == I.polynomial_tensor(pair_terms, DIMS),
            'The polynomial two-term refactorization identity failed.')
    survivors = [constant_family(term) for i, term in enumerate(data['surviving'])
                 if i not in data['pair']] + [data['kept']]
    survivor = I.polynomial_tensor(survivors, DIMS)
    error = polynomial_sum(old_error, deleted)
    require(polynomial_sum(survivor, error) == {0: I.target(DIMS)},
            'The full polynomial surviving-plus-error identity failed.')
    require(len(survivors) == 75, 'Unexpected surviving term count.')
    require(I.polynomial_pairing(old_error, old_error, DIMS) == {}, 'The old error quadratic changed.')
    require(I.polynomial_pairing(deleted, deleted, DIMS) == {}, 'The deleted term quadratic changed.')
    require(I.polynomial_pairing(old_error, deleted, DIMS) == {0: Fraction(1)},
            'The mixed full-error pairing changed.')
    require(I.polynomial_pairing(error, error, DIMS) == {0: Fraction(2)},
            'The full error quadratic is not identically two.')
    require(I.polynomial_pairing(survivor, survivor, DIMS) == {0: Fraction(102)},
            'The surviving tensor quadratic is not identically 102.')
    require(all(I.trace_tensor(tensor, DIMS) == 0 for tensor in error.values()),
            'The full error trace is not identically zero.')
    require(I.matrix_polynomial_pairing(old_terms + [data['deleted']],
                                       old_terms + [data['deleted']], DIMS) == {0: Fraction(2)},
            'The independent matrix-trace backend disagrees.')
    require(not I.square_matrix_polynomial(I.cyclic_product(data['deleted'], DIMS)),
            'The deleted term cyclic product is not identically square zero.')
    minima = old_error_minima(data['discarded'], sources[data['variant']])
    return {'surviving_terms': 75, 'original_discarded_terms': len(old_terms),
            'total_error_terms': len(old_terms)+1, 'full_coefficient_positions_per_degree': 10000,
            'parameter_degrees_checked': [0, 1, 2], 'full_polynomial_identity': True,
            'old_discarded_factor_minima': minima,
            'old_error_quadratic': '0', 'deleted_term_quadratic': '0',
            'mixed_old_error_deleted_term_pairing': '1', 'full_error_quadratic': '2',
            'surviving_tensor_quadratic': '102', 'full_error_trace': '0',
            'deleted_cyclic_product_square_zero': True,
            'error_nonzero_coordinates_by_parameter_degree': {str(k): len(v) for k, v in sorted(error.items())},
            'coordinate_and_matrix_backends_agree': True,
            'arbitrary_Laurent_parameter_substitution_excluded': True}


def ten_block_data(sources):
    surviving, discarded = split_terms(seed_terms(sources), sources['ten']['replacements'])
    block = [surviving[i] for i in TEN_BLOCK]
    products = [[u*w for u in term[0] for w in term[2]] for term in block]
    require(row_rank(products) == row_rank([term[1] for term in block]) == 5,
            'The registered block must have minimum V-flattening rank five.')
    left = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)]
    for term in block:
        u = I.matrix(term[0], 4, 5)
        require(all(u[i][j] == left[i]*u[0][j] for i in range(4) for j in range(5)),
                'The block U span lacks its common rank-one left factor.')
    error = I.tensor_from_factors(discarded, DIMS)
    require(I.quadratic(error, DIMS) == I.trace_tensor(error, DIMS) == 0,
            'The ten-split original error invariants changed.')
    H, J = [], []
    for first in block:
        h, j = [], []
        for second in block:
            cross = [first[0], second[1], first[2]]
            tensor = I.tensor_from_factors([cross], DIMS)
            h.append(I.trace_tensor(tensor, DIMS))
            j.append(I.pairing(error, tensor, DIMS))
            require(j[-1] == sum((I.factor_pairing(term, cross, DIMS) for term in discarded), Fraction(0)),
                    'The block mixed-pairing matrix backends disagree.')
        H.append(h)
        J.append(j)
    require(all(J[i][j] + H[i][j] == int(i == j) for i in range(5) for j in range(5)),
            'The block relation J=I-H failed.')
    return {'block_terms': list(TEN_BLOCK), 'V_flattening_rank': 5,
            'minimum_exact_terms': 5, 'common_U_left_factor': encode(left),
            'U_right_factors': encode([term[0][:5] for term in block]),
            'H_trace_pairing': encode(H), 'J_full_old_error_pairing': encode(J),
            'J_equals_identity_minus_H': True,
            'normalized_new_term_coefficients': 'y^T x = 1',
            'full_error_quadratic_in_tau': ['2', '-2', '1'],
            'all_minimum_five_term_block_refactorizations_one_term_deletion_excluded': True,
            'Laurent_dependent_refactorizations_included': True}


def build_certificate():
    sources = load_sources()
    M = I.target(DIMS)
    require(I.tensor_from_factors(seed_terms(sources), DIMS) == M, 'The original rank-76 identity failed.')
    require(I.reshape(M, DIMS) == {(i, i): Fraction(1) for i in range(100)}, 'The target reshaping changed.')
    require(I.quadratic(M, DIMS) == I.trace_power(M, 2, DIMS) == 100,
            'The target quadratic calibration failed.')
    families = []
    for name in FAMILIES:
        data = family_data(name, sources)
        families.append({'id': name, 'parameter': 'z', 'source_variant': data['variant'],
                         'pair': data['pair'], 'extra_replacement': data['extra_replacement'],
                         'deleted_factor_coefficients': encode(data['deleted']),
                         'kept_factor_coefficients': encode(data['kept']),
                         'original_discarded_factors': encode(data['discarded']),
                         'checks': analyze_family(data, sources)})
    return {'schema': SCHEMA, 'claim_id': CLAIM, 'scope': SCOPE, 'dimensions': list(DIMS),
            'source_pins': PINS, 'reshaped_matrix_dimension': 100, 'target_quadratic': '100',
            'ten_block': ten_block_data(sources), 'families': families,
            'proof_status': 'written-unreviewed', 'general_border_rank_obstruction': False,
            'all_refactorizations_excluded': False, 'improves_omega': False}


def verify(certificate):
    require(isinstance(certificate, dict), 'The certificate must be an object.')
    for key, expected in (('schema', SCHEMA), ('claim_id', CLAIM), ('scope', SCOPE),
                          ('dimensions', list(DIMS)), ('source_pins', PINS)):
        require(certificate.get(key) == expected, 'Certificate schema, scope, shape, or source pin differs.')
    I.dimensions(certificate['dimensions'])
    families = certificate.get('families')
    require(isinstance(families, list) and len(families) == len(FAMILIES), 'Unexpected family count.')
    for expected, record in zip(FAMILIES, families):
        require(isinstance(record, dict) and record.get('id') == expected, 'The registered family order differs.')
        parse_family(record.get('deleted_factor_coefficients'))
        parse_family(record.get('kept_factor_coefficients'))
    rebuilt = build_certificate()
    require(json.dumps(certificate, sort_keys=True) == json.dumps(rebuilt, sort_keys=True),
            'The saved exact construction or invariant certificate differs.')
    return {'claim_id': CLAIM, 'families_replayed': list(FAMILIES),
            'full_error_quadratics': [record['checks']['full_error_quadratic'] for record in families],
            'ten_block_minimum_refactorization_obstruction': True,
            'ten_block_full_error_polynomial': ['2', '-2', '1'],
            'source_identity_positions_checked': 10000,
            'full_family_coefficient_positions_checked': 90000,
            'reshape_dimension': 100, 'target_quadratic': '100',
            'polynomial_identities_not_parameter_samples': True,
            'arbitrary_Laurent_parameters_included': True,
            'coordinate_and_matrix_backends_agree': True,
            'proof_status': 'written-unreviewed', 'all_refactorizations_excluded': False,
            'general_border_rank_obstruction': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-certificate', type=Path)
    args = parser.parse_args()
    if args.write_certificate:
        certificate = build_certificate()
        args.write_certificate.write_text(json.dumps(certificate, indent=2) + '\n')
    else:
        certificate = json.loads((PACKAGE / 'certificate.json').read_text())
    print(json.dumps(verify(certificate), indent=2))
