"""Optional NumPy control for the numerical weight-preserving gauge.

Run explicitly in an environment with NumPy. This is outside the
default exact test suite and does not change maintained dependencies.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import numpy as np
from q64_experiment_replay import contraction,degrees,row_powers
from q64_weighted_laurent import weighted_gauge


def control():
    maps=[np.zeros((rows,137),dtype=complex) for rows in [25,20,20]]
    for term,(i,j,k) in enumerate(product(range(5),range(4),range(5))):
        for axis,row in enumerate([5*i+k,4*i+j,5*j+k]):
            maps[axis][row,36+term]=1
    for i,k in product(range(4),repeat=2):
        maps[0][5*i+k,136]=1+i+1j*k
    maps[1][16:20,136]=[1,2,3,4]
    for j,k in product(range(4),repeat=2):
        maps[2][5*j+k,136]=1+j+1j*k
    transformed=weighted_gauge(maps)
    actual,target=contraction([matrix.tolist() for matrix in transformed],101)
    power=degrees(row_powers())
    residual=max(abs(a-t) for a,t,p in zip(actual,target,power) if p<=0)
    positive=max(abs(a) for a,p in zip(actual,power) if p>0)
    if residual>=1e-11 or positive<=0.1:
        raise ArithmeticError('The numerical block gauge did not preserve its stated chart.')
    return {'optional_dependency':'NumPy','numpy_version':np.__version__,
            'maximum_nonpositive_coefficient_error':residual,
            'maximum_positive_coefficient_magnitude':positive,
            'explicit_scalar_control_cost':101,'control_passed':True,
            'default_exact_suite_requires_numpy':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report=control()
    if args.output:
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
