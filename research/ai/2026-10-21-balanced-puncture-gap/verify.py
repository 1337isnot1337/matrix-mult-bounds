"""Exact controls for the written balanced-puncture gap theorem."""
import argparse
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
S,T = sp.symbols('s t')


def encode(matrix):
    return {'shape':list(matrix.shape),'entries':[
        [i,j,str(value)] for (i,j),value in sorted(matrix.todok().items()) if value]}


def decode(record):
    return sp.MutableSparseMatrix(*record['shape'],{
        (i,j):sp.sympify(value,locals={'s':S,'t':T})
        for i,j,value in record['entries']})


def rank(matrix):
    return len(matrix.to_DM().rref()[1])


def flat(matrix):
    return sp.Matrix(1,matrix.rows*matrix.cols,list(matrix))


def pencil_spaces():
    l2 = sp.Matrix([[S,T,0],[0,S,T]])
    doubled = sp.Matrix([[S,T,0,0],[0,0,S,T]])
    skew = sp.Matrix([[0,S,T],[-S,0,0],[-T,0,0]])
    return {'L2':l2,'L2_transpose':l2.T,
            'L1_plus_L1':doubled,'L1T_plus_L1T':doubled.T,
            'L1_plus_L1T_as_skew':skew}


def amplified_images(matrices,row_kernel,column_kernel):
    m,n = matrices[0].shape
    if (len(set(row_kernel))!=2 or len(set(column_kernel))!=2
            or not all(0<=i<2*m for i in row_kernel)
            or not all(0<=j<2*n for j in column_kernel)):
        raise ValueError('both coordinate quotient kernels must have dimension two')
    rows = [i for i in range(2*m) if i not in row_kernel]
    columns = [j for j in range(2*n) if j not in column_kernel]
    images = []
    for matrix in matrices:
        for i,j in itertools.product(range(2),repeat=2):
            unit = sp.zeros(2);unit[i,j] = 1
            images.append(sp.kronecker_product(matrix,unit).extract(rows,columns))
    return images


def case(name,matrices,row_kernel,column_kernel,expected):
    images = amplified_images(matrices,row_kernel,column_kernel)
    dimension = rank(sp.Matrix.vstack(*(flat(m) for m in images)))
    if dimension!=expected:
        raise ArithmeticError(name+' projected dimension changed')
    return {'name':name,'matrix_basis':[encode(m) for m in matrices],
            'row_kernel':row_kernel,'column_kernel':column_kernel,
            'projected_matrices':[encode(m) for m in images],
            'projected_first_dimension':dimension}


@lru_cache(None)
def reports():
    canonical = []
    for name,matrix in pencil_spaces().items():
        witnesses = {}
        for rows in itertools.combinations(range(matrix.rows),2):
            for columns in itertools.combinations(range(matrix.cols),2):
                determinant = sp.expand(matrix.extract(rows,columns).det())
                for variable in [S,T]:
                    for sign in [1,-1]:
                        if determinant==sign*variable**2:
                            witnesses.setdefault(str(variable),{
                                'rows':list(rows),'columns':list(columns),
                                'determinant':str(determinant)})
        if set(witnesses)!={'s','t'}:
            raise ArithmeticError('constant rank two certificate incomplete')
        minor_count = 0
        for rows in itertools.combinations(range(matrix.rows),3):
            for columns in itertools.combinations(range(matrix.cols),3):
                minor_count += 1
                if sp.expand(matrix.extract(rows,columns).det())!=0:
                    raise ArithmeticError('canonical pencil exceeds rank two')
        canonical.append({'name':name,'matrix':encode(matrix),
                          'rank_lower_minor_witnesses':witnesses,
                          'rank_upper_three_minors_checked':minor_count,
                          'all_nonzero_complex_members_rank':2})
    l2 = pencil_spaces()['L2']
    skew = pencil_spaces()['L1_plus_L1T_as_skew']
    basis = lambda m:[m.subs({S:1,T:0}),m.subs({S:0,T:1})]
    rank_one = [sp.Matrix([[1,0,0],[0,0,0],[0,0,0]]),
                sp.Matrix([[0,1,0],[0,0,0],[0,0,0]])]
    controls = [
        case('sharp_three_L2',basis(l2),[1,3],[0,2],3),
        case('skew_complete_cancellation',basis(skew),[0,1],[0,1],0),
        case('skew_sharp_four',basis(skew),[0,1],[0,2],4),
        case('dimension_one_rank_three_counterexample',[sp.eye(3)],[0,2],[4,5],2),
        case('rank_four_auxiliary_lower_bound_sharp',[sp.eye(4)],[0,2],[4,6],3),
        case('rank_one_exclusion_is_essential',rank_one,[0,2],[0,2],2),
        case('real_constant_rank_two_counterexample',
             [sp.eye(2),sp.Matrix([[0,-1],[1,0]])],[1,3],[1,3],2),
    ]
    return {'canonical_pencils':canonical,'sharpness_and_hypothesis_controls':controls,
            'complex_field_required':True,
            'real_counterexample_determinant':'s**2 + t**2',
            'scope':'Finite exact controls for a written proof using the external complex Kronecker theorem; no formal verification or improved exponent.'}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(reports(),indent=2)+'\n')
    print('canonical pencils and seven exact controls written',flush=True)
