"""Exact cubic-span certificate for the fixed singular-unit resolvent."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]


def inverse_integer(matrix):
    """Discover an inverse modulo 1009, then verify it over the integers."""
    n=len(matrix);p=1009
    work=[[x%p for x in row]+[int(i==j) for j in range(n)] for i,row in enumerate(matrix)]
    for column in range(n):
        pivot=next((i for i in range(column,n) if work[i][column]),None)
        if pivot is None:raise ValueError('singular source unit')
        work[column],work[pivot]=work[pivot],work[column]
        scale=pow(work[column][column],-1,p)
        work[column]=[x*scale%p for x in work[column]]
        for i in range(n):
            if i!=column and work[i][column]:
                factor=work[i][column]
                work[i]=[(x-factor*y)%p for x,y in zip(work[i],work[column])]
    inverse=[[x if x<=p//2 else x-p for x in row[n:]] for row in work]
    for left,right in [(matrix,inverse),(inverse,matrix)]:
        if any(sum(left[i][k]*right[k][j] for k in range(n))!=int(i==j)
               for i in range(n) for j in range(n)):
            raise ValueError('lift is not an exact integer inverse')
    return inverse


def multiply(left,right):
    return [[sum(x*right[k][j] for k,x in enumerate(row) if x)
             for j in range(len(right[0]))] for row in left]


def outer_source():
    rows=list(itertools.product(range(4),range(7)))
    columns=list(itertools.product(range(7),range(4)))
    def coefficient(i,s):
        return [[int(H-j==i and L-r==s) for H,r in columns] for j,L in rows]
    unit=[[int(0<=H-j<4 and 0<=L-r<4 and H-j+L-r==3)
           for H,r in columns] for j,L in rows]
    inverse=inverse_integer(unit)
    originals=[coefficient(i,s) for i,s in itertools.product(range(4),repeat=2)]
    normalized=[multiply(inverse,x) for x in originals]
    return unit,originals,normalized


def cubic_space():
    unit,originals,normalized=outer_source()
    S=normalized[0]
    # S*T(F) for all 16 coefficients, followed by T(x),T(x^2),T(x^3).
    matrices=[multiply(unit,multiply(S,x)) for x in normalized]
    matrices += [originals[4],originals[8],originals[12]]
    kept=[j*7+L for j,L in itertools.product(range(4),repeat=2)]
    if any(value for matrix in matrices for i,row in enumerate(matrix) if i not in kept for value in row):
        raise ValueError('the reduced space leaves the sixteen specified rows')
    forms=[[tuple(v for v,matrix in enumerate(matrices) if matrix[i][j]%2)
            for j in range(28)] for i in kept]
    monomials=list(itertools.combinations_with_replacement(range(19),3))
    return forms,{triple:i for i,triple in enumerate(monomials)}


def cubic_minor(rows,columns,forms,monomials):
    # Reduce the integer determinant polynomial modulo two. Its signs
    # coincide there. Repeated monomials cancel by XOR, including those
    # from different permutations or different variable choices.
    value=0
    for permutation in itertools.permutations(range(3)):
        factors=[forms[rows[i]][columns[permutation[i]]] for i in range(3)]
        for triple in itertools.product(*factors):
            value ^= 1 << monomials[tuple(sorted(triple))]
    return value


def check_sources():
    sources=json.loads((PACKAGE/'sources.json').read_text())
    for record in sources['sources']:
        if hashlib.sha256((ROOT/record['path']).read_bytes()).hexdigest()!=record['sha256']:
            raise ValueError('adopted source pin changed')


def verify(certificate):
    check_sources()
    expected={'schema':'resolvent-all-constant-compressions-v1','field':2,
              'variables':19,'cubic_monomials':1330,'target_rows':16,'target_columns':28,
              'all_constant_compression_pairs':True,'moving_compressions_excluded':False,
              'general_A4_excluded':False,'independent_review':False,
              'lean_formalized':False,'improves_omega':False}
    if set(certificate)!=set(expected)|{'minors'} or any(certificate[k]!=v for k,v in expected.items()):
        raise ValueError('certificate scope or source contract changed')
    minors=certificate['minors']
    if len(minors)!=1330:raise ValueError('need 1330 independent cubic minors')
    if len({json.dumps(x) for x in minors})!=1330:raise ValueError('repeated minor')
    forms,monomials=cubic_space();basis={}
    for rows,columns in minors:
        for values,size in [(rows,16),(columns,28)]:
            if len(values)!=3 or len(set(values))!=3 or any(type(i) is not int or not 0<=i<size for i in values):
                raise ValueError('invalid minor coordinate')
        vector=cubic_minor(rows,columns,forms,monomials)
        while vector:
            pivot=vector.bit_length()-1
            if pivot not in basis:
                basis[pivot]=vector;break
            vector^=basis[pivot]
        if not vector:raise ValueError('dependent or zero cubic minor')
    if len(basis)!=1330:raise ValueError('incomplete cubic coefficient span')
    return {'verified':True,'integer_source_inverse':True,'cubic_coefficient_rank_mod_2':1330,
            'all_cubic_forms_over_Q_spanned':True,'nonzero_reduced_matrix_rank_at_least':3,
            'all_constant_compression_pairs':True,'general_A4_excluded':False,
            'moving_compressions_excluded':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(verify(json.loads(args.verify.read_text())),indent=2))
