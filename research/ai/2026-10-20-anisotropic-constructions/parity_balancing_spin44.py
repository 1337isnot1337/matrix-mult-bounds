"""Exact balanced spin module and four-parity original-source lift.

The entire accepted computation uses the Python standard library.  It
rebuilds the polynomial subspace, checks the rational join, and replays
all coefficients of both original-source restrictions.
"""

from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import determinant, horizontal, modular_rank, multiply, transpose, unpack
from spin_module14 import check_product, column_entries, full_terms, pack


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'results/anisotropic-constructions-2026-10-20'
WITNESS = DIRECTORY / 'parity_balancing_spin44_witness.json'
MAPS = DIRECTORY / 'parity_balancing_spin44_full_maps.json'
REPORT = DIRECTORY / 'parity_balancing_spin44_certificate.json'


def j_shift(matrix, shift):
    answer = [[0]*len(matrix[0]) for _ in range(20)]
    for a, j in product(range(4), range(4)):
        answer[4*(a+shift)+j] = matrix[4*a+j][:]
    return answer


def k_shift(matrix, shift):
    return [matrix[5*a+j+shift][:] for a, j in product(range(4), range(4))]


def left(matrix, index):
    p, s = divmod(index, 2)
    shifted = j_shift(matrix, s)
    zero = [[0]*len(matrix[0]) for _ in range(20)]
    return shifted+zero if p == 0 else zero+shifted


def construction(witness, maps, denominators):
    if witness.get('profile') != [3, 3]:
        raise ArithmeticError('The balanced polynomial-chain profile changed')
    generators = witness.get('generators')
    if not isinstance(generators, list) or len(generators) != 2:
        raise ArithmeticError('Exactly two polynomial generators are required')
    columns = []
    for generator in generators:
        if (len(generator) != 2 or any(len(row) != 4 for row in generator)
                or any(type(v) is not int for row in generator for v in row)):
            raise ArithmeticError('Incorrect polynomial generator coordinates')
        for shift in range(3):
            vector = [0]*16
            for a, row in enumerate(generator):
                for j, value in enumerate(row):
                    vector[4*(a+shift)+j] = value
            columns.append(vector)
    U = transpose(columns)
    Q, dq = unpack(witness['U_left_annihilator'], (10, 16))
    if modular_rank(U) != 6 or modular_rank(Q) != 10 or any(any(row) for row in multiply(Q, U)):
        raise ArithmeticError('The exact intermediate subspace or annihilator failed')
    Wfull = horizontal(*(left(U, k) for k in range(4)))
    indices = witness['W_basis_column_indices']
    if (len(indices) != 16 or len(set(indices)) != 16
            or any(type(i) is not int or not 0 <= i < 24 for i in indices)):
        raise ArithmeticError('Incorrect ignored-space basis columns')
    W = [[row[i] for i in indices] for row in Wfull]
    if modular_rank(W) != 16:
        raise ArithmeticError('The ignored-space basis is dependent')
    # Each of two length-three chains has four shifted columns;
    # the two independent p blocks give the matching upper bound16.
    X, Y, Z = maps
    dx, dy, dz = denominators
    expected_X = []
    for k in range(9):
        a,b,c,d,e,f,g,h,i = [int(k == j) for j in range(9)]
        expected_X.append([2*(e+i),4*d-h,b,2*a,2*c,-b,h,2*g,2*i,-h,b-4*f,2*(a+e)])
    if dx != 2 or X != expected_X:
        raise ArithmeticError('The specified first spin map changed')
    reflected = [[0]*12 for _ in range(9)]
    for I,J,i,k,s in product(range(3),range(3),range(2),range(3),range(2)):
        reflected[3*I+J][(i*3+k)*2+s] = X[3*J+I][(s*3+k)*2+i]
    if modular_rank(X+reflected) != 12:
        raise ArithmeticError('The stated first-map transpose compatibility check changed')
    P = [[0,1,0,1],[1,0,0,0],[0,0,1,0],[0,-1,0,1]]
    Pinv2 = [[0,2,0,0],[1,0,0,-1],[0,0,2,0],[1,0,0,1]]
    for k, coefficients in enumerate(X):
        physical = [[coefficients[(i*3+p+q)*2+s] for p,s in product(range(2),range(2))]
                    for i,q in product(range(2),range(2))]
        a,b,c,d,e,f,g,h,i = [int(k == j) for j in range(9)]
        target = [[4*a,4*b,4*c,0],[4*d,4*e,4*f,0],[4*g,4*h,4*i,0],
                  [4*d-2*h,-4*a+4*i,2*b-4*f,4*(a+e+i)]]
        if multiply(multiply(Pinv2, physical), P) != target:
            raise ArithmeticError('The triangular spin-one identity failed')
    plus = transpose([row[20:] for row in Z[:8]])
    minus = transpose([row[:20] for row in Z[16:]])
    if any(any(row[:20]) for row in Z[:8]) or any(any(row[20:]) for row in Z[16:]):
        raise ArithmeticError('The endpoint pair block support changed')
    for alpha, c in product(range(8),range(20)):
        if 2*Z[8+alpha][c] != plus[c][alpha] or 2*Z[8+alpha][20+c] != -minus[c][alpha]:
            raise ArithmeticError('The central right-map row changed')
    v = k_shift(plus, 0)
    difference = [[a-b for a,b in zip(row0,row1)]
                  for row0,row1 in zip(v,k_shift(minus,1))]
    for residual in (k_shift(plus,1),k_shift(minus,0),difference):
        if any(any(row) for row in multiply(Q,residual)):
            raise ArithmeticError('A required endpoint relation failed')
    q0,q1 = [],[]
    for row in Q:
        q0.append([row[4*a+H] if H<4 else 0 for a,H in product(range(4),range(5))])
        q1.append([row[4*a+H-1] if H else 0 for a,H in product(range(4),range(5))])
    equations = [row+[0]*20 for row in q1]+[[0]*20+row for row in q0]
    equations += [a+[-v for v in b] for a,b in zip(q0,q1)]
    if modular_rank(equations) != 30:
        raise ArithmeticError('The endpoint pair space is not ten-dimensional')
    L = [left(v,k) for k in range(4)]
    middle = [[a-b for a,b in zip(row0,row3)] for row0,row3 in zip(L[0],L[3])]
    B = horizontal([[2*dz*a for a in row] for row in W],
                   [[2*a for a in row] for row in L[1]],middle,
                   [[2*a for a in row] for row in L[2]])
    expected = [[2*dy*dz*int(j == 16+i) for j in range(40)] for i in range(24)]
    if multiply(Y,B) != expected:
        raise ArithmeticError('The exact dual join equations failed')
    actual_det = Fraction(determinant(B),(2*dz)**40)
    if actual_det != Fraction(witness['join_determinant']) or not actual_det:
        raise ArithmeticError('The exact square join determinant failed')
    return {'U_dimension':6,'W_dimension':16,'D_dimension':10,'selected_channels':8,
            'join_dimension':40,'join_determinant':str(actual_det),
            'triangular_identity_and_all_endpoint_relations_checked':True,
            'complete_exact_join_duality_checked':True,
            'span_with_short_swapped_transpose_first_map':12}


def reduced_terms():
    for i,p,q,s,a,j in product(range(2),range(2),range(2),range(2),range(4),range(4)):
        yield ((i*3+p+q)*2+s,(p*5+a+s)*4+j,(q*4+a)*5+i+j)


def lift(maps, doubled):
    step = 2 if doubled else 1
    n = 8 if doubled else 4
    m, middle = 2*n-1, 8*step*step
    answer = [[[0]*(n*n*m) for _ in range(rows)] for rows in (9,3*middle,3*middle)]
    for c, entries in column_entries(maps[0]).items():
        ik,s = divmod(c,2)
        i,k = divmod(ik,3)
        column = (step*i*m+k)*n+step*s
        for row,value in entries:
            answer[0][row][column] = value
    for e,f in product(range(step),range(step)):
        copy = step*e+f
        for c,entries in column_entries(maps[1]).items():
            pL,j = divmod(c,4)
            p,L = divmod(pL,5)
            column = (p*m+e+step*L)*n+f+step*j
            for row,value in entries:
                vertex,alpha = divmod(row,8)
                answer[1][vertex*middle+8*copy+alpha][column] = value
        for c,entries in column_entries(maps[2]).items():
            qa,H = divmod(c,5)
            q,a = divmod(qa,4)
            column = ((e+step*a)*m+f+step*H)*n+q
            for row,value in entries:
                vertex,alpha = divmod(row,8)
                answer[2][vertex*middle+8*copy+alpha][column] = value
    return n,middle,answer


def verify(witness=None, exported=None):
    witness = json.loads(WITNESS.read_text()) if witness is None else witness
    if (witness.get('new_exponent_established') is not False
            or witness.get('source_format') != [12,40,40]
            or witness.get('target') != [3,3,8]):
        raise ArithmeticError('The source, target, or claim scope changed')
    parsed = [unpack(witness[name],shape) for name,shape in zip('XYZ',((9,12),(24,40),(24,40)))]
    maps,denominators = [a for a,d in parsed],[d for a,d in parsed]
    checks = construction(witness,maps,denominators)
    scale = denominators[0]*denominators[1]*denominators[2]
    reduced = check_product(reduced_terms(),maps,scale,8)
    reduced.pop('response_support_coordinates')
    report = {'source_parameters':[2,4,4],'source_format':[12,40,40],
              'reduced_target':[3,3,8],'map_denominators':denominators,
              'integer_coefficient_scale':scale,'construction_checks':checks,
              'reduced_coefficient_replay':reduced,'original_source_replays':[],
              'larger_square_target_constructed':False,'new_exponent_established':False}
    export = {'field':'Q','source_coordinate_order':'F(i,k,s) -> (i*(2*n-1)+k)*n+s',
              'target_coordinate_orders':['3*I+J','middle*J+alpha','middle*I+alpha'],
              'last_leg_convention':'row middle*I+alpha denotes Z_(alpha,I)',
              'restrictions':[],'new_exponent_established':False}
    for doubled in (False,True):
        n,middle,full = lift(maps,doubled)
        replay = check_product(full_terms(n,n),full,scale,middle)
        replay.pop('response_support_coordinates')
        report['original_source_replays'].append({'source':[n,n],'target':[3,3,middle],**replay})
        export['restrictions'].append({'source':[n,n],'target':[3,3,middle],
                                      'maps':{name:pack(matrix,denominator)
                                              for name,matrix,denominator in zip('XYZ',full,denominators)}})
    if exported is not None and exported != export:
        raise ArithmeticError('The actual full-source export differs from the verified lift')
    return report,export


if __name__ == '__main__':
    report,exported = verify()
    MAPS.write_text(json.dumps(exported,indent=2)+'\n')
    replayed,_ = verify(exported=json.loads(MAPS.read_text()))
    if report != replayed:
        raise ArithmeticError('The saved-map replay differs')
    report['witness_sha256'] = hashlib.sha256(WITNESS.read_bytes()).hexdigest()
    report['full_maps_sha256'] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
