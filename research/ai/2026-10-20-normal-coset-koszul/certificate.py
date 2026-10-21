"""Explicit three-slice Koszul obstruction for abelian normal coset fibers.

Classical Strassen commutator bound, with explicit block matrices and new
scoped applications. Standard library only; no exponent improvement.
"""
import argparse
from itertools import product
import json
from math import isqrt
from pathlib import Path


def rank_mod(matrix, prime=101):
    if prime < 2 or any(prime % d == 0 for d in range(2,isqrt(prime)+1)):
        raise ValueError('prime modulus required')
    rows = [[x % prime for x in row] for row in matrix]
    if not rows:
        return 0
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank,len(rows)) if rows[i][column]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot] = rows[pivot],rows[rank]
        inverse = pow(rows[rank][column],-1,prime)
        rows[rank] = [(x*inverse) % prime for x in rows[rank]]
        for i in range(rank+1,len(rows)):
            scalar = rows[i][column]
            if scalar:
                rows[i] = [(a-scalar*b) % prime for a,b in zip(rows[i],rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def three_slice_matrix(blocks):
    if not blocks or any(not isinstance(k,int) or k < 1 for k in blocks):
        raise ValueError('positive matrix block sizes required')
    dimension = sum(k*k for k in blocks)
    # A and B act by left multiplication by diag(0,...,k-1) and a cycle.
    A = [[0]*dimension for _ in range(dimension)]
    B = [[0]*dimension for _ in range(dimension)]
    offset = 0
    for k in blocks:
        for i,j in product(range(k),repeat=2):
            column = offset+i*k+j
            A[column][column] = i
            B[offset+((i+1) % k)*k+j][column] = 1
        offset += k*k
    # K_1 on three slices I,A,B:
    # (-A v0+v1, -B v0+v2, -B v1+A v2).
    matrix = [[0]*(3*dimension) for _ in range(3*dimension)]
    for i in range(dimension):
        matrix[i][dimension+i] = 1
        matrix[dimension+i][2*dimension+i] = 1
        for j in range(dimension):
            matrix[i][j] = -A[i][j]
            matrix[dimension+i][j] = -B[i][j]
            matrix[2*dimension+i][dimension+j] = -B[i][j]
            matrix[2*dimension+i][2*dimension+j] = A[i][j]
    return matrix


def block_certificate(blocks, normal_order, prime=101):
    if max(blocks) >= prime:
        raise ValueError('choose a prime greater than every block size')
    dimension = sum(k*k for k in blocks)
    singles = blocks.count(1)
    expected = 3*dimension-singles
    rank = rank_mod(three_slice_matrix(blocks),prime)
    if rank != expected:
        raise ArithmeticError('explicit Koszul rank disagrees with commutator calculation')
    return {'blocks':blocks,'algebra_dimension':dimension,'scalar_blocks':singles,
            'matrix_format':[3*dimension]*2,'modulus':prime,
            'rank_mod_prime':rank,'proved_characteristic_zero_rank':expected,
            'rank_one_contribution_at_most':2,'abelian_source_order':normal_order,
            'source_Koszul_rank_at_most':2*normal_order,
            'excluded':rank>2*normal_order}


def rectangular_three_slice_matrix(blocks):
    """Explicit three slices for a direct sum of rectangular products.

    A block M(a,b,c) has B dimension b*c and C dimension a*c. For min(a,b)
    >=2 use an embedded square unit, diagonal, and cycle. A 1-by-b or
    a-by-1 block uses two elementary matrices when a*b>=2.
    """
    if any(len(row)!=3 or any(not isinstance(n,int) or n<0 for n in row) for row in blocks):
        raise ValueError('nonnegative rectangular sizes required')
    blocks = [row for row in blocks if all(row)]
    Bdim = sum(b*c for a,b,c in blocks)
    Cdim = sum(a*c for a,b,c in blocks)
    slices = [[[0]*Bdim for _ in range(Cdim)] for _ in range(3)]
    boff = coff = 0
    for a,b,c in blocks:
        k = min(a,b)
        for j in range(k):
            for t in range(c):
                slices[0][coff+j*c+t][boff+j*c+t] = 1
                if k>=2:
                    slices[1][coff+j*c+t][boff+j*c+t] = j
                    slices[2][coff+((j+1)%k)*c+t][boff+j*c+t] = 1
        if k==1 and a*b>=2:
            for t in range(c):
                if a>=2:
                    slices[1][coff+c+t][boff+t] = 1
                else:
                    slices[1][coff+t][boff+c+t] = 1
        boff += b*c
        coff += a*c
    J,X,Y = slices
    matrix = [[0]*(3*Bdim) for _ in range(3*Cdim)]
    for i in range(Cdim):
        for j in range(Bdim):
            matrix[i][j] = -X[i][j]
            matrix[i][Bdim+j] = J[i][j]
            matrix[Cdim+i][j] = -Y[i][j]
            matrix[Cdim+i][2*Bdim+j] = J[i][j]
            matrix[2*Cdim+i][Bdim+j] = -Y[i][j]
            matrix[2*Cdim+i][2*Bdim+j] = X[i][j]
    return matrix


def seven_fiber_patterns():
    patterns = [row for row in product(range(1,4),repeat=7) if sum(row)==19]
    normalized = []
    for row in patterns:
        first = next(i for i,v in enumerate(row) if v<3)
        normalized.append(row[first:]+row[:first])
    checked = 0
    minimum = None
    by_types = {}
    witness = None
    for rows in product(normalized,repeat=3):
        checked += 1
        blocks = [min(values) for values in zip(*rows)]
        D = sum(k*k for k in blocks)
        rank = 3*D-blocks.count(1)
        types = sum(1 in row for row in rows)
        by_types[types] = min(by_types.get(types,rank),rank)
        if minimum is None or rank < minimum:
            minimum,witness = rank,[list(row) for row in rows]
    if len(patterns)!=28 or checked!=21952:
        raise ArithmeticError('incomplete seven-fiber pattern coverage')
    return {'family_patterns':len(patterns),'ordered_pattern_triples_checked':checked,
            'alignment':'Independently cyclically shift the first deficient fiber to scalar one.',
            'minimum_Koszul_rank':minimum,
            'minimum_rank_by_count_of_one_point_families':{str(k):v for k,v in sorted(by_types.items())},
            'minimum_witness_patterns':witness,
            'abelian_source_Koszul_upper':128,'all_excluded':minimum>128}


def report():
    return {'claim':'AI-GROUP-NORMAL-KOSZUL-011','status':'proof-written-unreviewed',
            'classical_bound':'2*border_rank >= 3*sum(k_i^2)-number_of_size_one_blocks',
            'applications':{
                'F8_squared_maximum_three':block_certificate([2]*4+[3]*3,64),
                'F4_cubed_index_three_size_twelve':block_certificate([4]*3,64),
                'C31_index_six_minimum_two':block_certificate([2]*6,31)},
            'all_F8_seven_fiber_size_patterns':seven_fiber_patterns(),
            'scope':'Injective pair-map group construction with strict vertex potentials, '
                    'restricted to identity-quotient fibers of an abelian normal subgroup. '
                    'The F8 size-nineteen exclusion assumes every normal fiber has size at most three.',
            'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
