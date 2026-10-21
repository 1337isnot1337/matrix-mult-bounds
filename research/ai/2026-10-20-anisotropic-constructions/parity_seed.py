"""Embed the exact mixed M9 parity face in a larger matrix target.

This creates a partial-target search seed, not an improving restriction.
"""
import argparse
import hashlib
from itertools import product
import json
from pathlib import Path

import numpy as np

from dense_als import DenseProblem


def embedded_seed(matrix_sizes=(14,4)):
    if matrix_sizes[0]<9:
        raise ValueError('The first target block must contain nine vertices')
    exact_path=Path(__file__).with_name('parity_structure_m9_maps.npz')
    exact=np.load(exact_path)
    d=sum(n*n for n in matrix_sizes)
    maps=[np.zeros((d,225),dtype=np.int64) for _ in range(3)]
    first=matrix_sizes[0]
    for result,name in zip(maps,'ABC'):
        for i,j in product(range(9),repeat=2):
            result[first*i+j]=exact[name][9*i+j]
    problem=DenseProblem(5,5,source_mode='parity110',direct_sum=matrix_sizes)
    actual=(maps[0]@problem.contraction(maps,0)).reshape(problem.target_dims)
    expected=np.zeros(problem.target_dims,dtype=np.int64)
    grades=exact['vertex_grades']
    retained=0
    for i,j,k in product(range(9),repeat=3):
        parity=((int(grades[j])-int(grades[i]))%2,
                (int(grades[k])-int(grades[j]))%2,
                (int(grades[i])-int(grades[k]))%2)
        if parity!=(1,1,0):
            expected[first*i+j,first*j+k,first*k+i]=1
            retained+=1
    if not np.array_equal(actual,expected):
        raise ArithmeticError('The embedded seed has an incorrect or extraneous coefficient')
    target_terms=sum(n**3 for n in matrix_sizes)
    theoretical=((target_terms-retained)/target_terms)**0.5
    residual=problem.residual(maps)
    if abs(residual-theoretical)>1e-14:
        raise ArithmeticError('The full seed objective does not match the exact term count')
    report={'source_lengths':[5,5],'source_mode':'parity110',
            'target_direct_sum_sizes':list(matrix_sizes),
            'exact_seed_file':str(exact_path),
            'exact_seed_sha256':hashlib.sha256(exact_path.read_bytes()).hexdigest(),
            'partial_target_terms':retained,'full_target_terms':target_terms,
            'full_coefficient_count':int(np.prod(problem.target_dims)),
            'exact_partial_target_verified':True,'extraneous_coefficients':0,
            'full_relative_error':residual,'theoretical_relative_error':theoretical,
            'improving_target_constructed':False,'new_exponent_established':False}
    return maps,report


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--sizes',type=int,nargs='+',default=[14,4])
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    maps,report=embedded_seed(tuple(args.sizes))
    args.output.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(args.output/'seed.npz',**dict(zip('ABC',maps)))
    (args.output/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
