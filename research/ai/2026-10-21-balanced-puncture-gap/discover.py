"""Registered exhaustive binary-kernel pilot, with exact rational replay."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path
import time

import sympy as sp


def spaces():
    out = []
    for p,q in itertools.combinations(range(6),2):
        free = [(0,j) for j in range(p+1,6) if j!=q]
        free += [(1,j) for j in range(q+1,6)]
        for choices in itertools.product(range(2),repeat=len(free)):
            rows = [1<<p,1<<q]
            for (i,j),value in zip(free,choices):
                rows[i] |= value<<j
            nonpivots = [j for j in range(6) if j not in [p,q]]
            quotient = [(1<<j)|(((rows[0]>>j)&1)<<p)|(((rows[1]>>j)&1)<<q)
                        for j in nonpivots]
            columns = [sum(((row>>j)&1)<<i for i,row in enumerate(quotient))
                       for j in range(6)]
            out.append({'pivots':[p,q], 'rows':rows, 'columns':columns})
    if len(out)!=651 or len({tuple(r['rows']) for r in out})!=651:
        raise ArithmeticError('binary Grassmannian enumeration changed')
    return out


OUTER = [[sum(((left>>i)&1)*right<<(4*i) for i in range(4))
          for right in range(16)] for left in range(16)]


def binary_rank(vectors):
    basis = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length()-1
            if pivot not in basis:
                basis[pivot] = vector
                break
            vector ^= basis[pivot]
    return len(basis)


def image_vectors(left,right):
    l,r = left['columns'],right['columns']
    return [OUTER[l[i]][r[2*k+j]] ^ OUTER[l[2*k+i]][r[j]]
            for k in [1,2] for i,j in itertools.product(range(2),repeat=2)]


def rational_quotient(space):
    p,q = space['pivots']
    rows = space['rows']
    nonpivots = [j for j in range(6) if j not in [p,q]]
    matrix = sp.zeros(4,6)
    for i,j in enumerate(nonpivots):
        matrix[i,j] = 1
        matrix[i,p] = -((rows[0]>>j)&1)
        matrix[i,q] = -((rows[1]>>j)&1)
    return matrix


def rational_image(left,right,rank_one=False):
    l,r = rational_quotient(left),rational_quotient(right)
    matrices = []
    for k in [1,2]:
        matrix = sp.zeros(3)
        if rank_one:
            matrix[0,k-1] = 1
        else:
            matrix[0,k] = 1
            matrix[k,0] = -1
        for i,j in itertools.product(range(2),repeat=2):
            unit = sp.zeros(2);unit[i,j] = 1
            image = l*sp.kronecker_product(matrix,unit)*r.T
            matrices.append(sp.Matrix(1,16,list(image)))
    full = sp.Matrix.vstack(*matrices)
    return len(full.to_DM().rref()[1])


def run():
    start = time.time()
    kernel_spaces = spaces()
    by_rows = {tuple(record['rows']):record for record in kernel_spaces}
    complete = by_rows[1,2]
    rank_one = by_rows[1,4]
    if rational_image(complete,complete)!=0:
        raise ArithmeticError('known complete cancellation control failed')
    if rational_image(rank_one,rank_one,rank_one=True)!=2:
        raise ArithmeticError('nonzero low-image positive control failed')
    histogram = Counter()
    low_candidates = []
    rational_histogram = Counter()
    for i,left in enumerate(kernel_spaces):
        for j,right in enumerate(kernel_spaces):
            dimension = binary_rank(image_vectors(left,right))
            histogram[dimension] += 1
            if dimension<=2:
                actual = rational_image(left,right)
                rational_histogram[actual] += 1
                low_candidates.append({'left_index':i,'right_index':j,
                                       'binary_dimension':dimension,
                                       'rational_dimension':actual})
    return {'model':'Signed skew pencil tensor Mat2; binary RREF kernel lifts',
            'kernel_spaces_each':651,'ordered_kernel_pairs':651**2,
            'binary_image_dimension_histogram':dict(sorted(histogram.items())),
            'rational_replay_histogram':dict(sorted(rational_histogram.items())),
            'all_modular_dimension_at_most_two_candidates':low_candidates,
            'nonzero_rational_low_image_counterexamples':[row for row in low_candidates
                if 0<row['rational_dimension']<=2],
            'kernel_space_enumeration':kernel_spaces,
            'controls':{'complete_cancellation_dimension':0,
                        'rank_one_pencil_nonzero_projected_dimension':2},
            'elapsed_seconds':time.time()-start,
            'scope':'Finite deterministic discovery only; not an arbitrary-complex-subspace exclusion.'}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:value for k,value in report.items()
                     if k not in ['kernel_space_enumeration',
                                  'all_modular_dimension_at_most_two_candidates']}),flush=True)
