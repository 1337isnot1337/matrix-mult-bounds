"""Exact finite controls for the full-source sub-2ab slice locus.

The theorem is proved in polynomial_rank_locus.md. These calculations
do not extend its ordinary-map consequences to singular degenerations.
"""
from collections import Counter
from itertools import product
import argparse
import json
from pathlib import Path

from central_minrank import rank_mod_two
from slice_rank_gap import full_matrix
from singular_support import source_terms,rank_mod_prime


def multiply_binary_polynomials(left,right):
    result=0
    while left:
        bit=left&-left
        left^=bit
        result^=right<<(bit.bit_length()-1)
    return result


def symbol_rank_binary_22(f):
    polys=[]
    for k in range(3):
        polys.append(sum((f[(i*3+k)*2+s]&1)<<(3*i+s)
                         for i,s in product(range(2),repeat=2)))
    if not any(polys):
        return 0
    determinant=(multiply_binary_polynomials(polys[0],polys[2])^
                 multiply_binary_polynomials(polys[1],polys[1]))
    return 2 if determinant else 1


def has_constant_coherent_factor(f,a,b,prime=2):
    m=a+b-1
    rows=[[f[(i*m+k)*b+s]%prime for k in range(m)]
          for i,s in product(range(a),range(b))]
    h=next((row for row in rows if any(row)),None)
    if h is None:
        return False
    pivot=next(k for k,v in enumerate(h) if v)
    inverse=pow(h[pivot],-1,prime)
    for row in rows:
        scalar=row[pivot]*inverse%prime
        if any((u-scalar*v)%prime for u,v in zip(row,h)):
            return False
    return rank_mod_prime([[h[p+q] for q in range(b)] for p in range(a)],prime)==1


def exhaustive_binary_22():
    histogram=Counter();symbol_histogram={1:Counter(),2:Counter()}
    below=0
    for bits in range(1,1<<12):
        f=[(bits>>i)&1 for i in range(12)]
        rank=rank_mod_two(full_matrix(f,2,2))
        symbol=symbol_rank_binary_22(f)
        coherent=has_constant_coherent_factor(f,2,2)
        if rank<4*symbol:
            raise ArithmeticError('The polynomial-symbol rank lower bound failed')
        if (rank<8)!=coherent:
            raise ArithmeticError('The complete sub-2ab locus classification failed')
        below+=rank<8
        histogram[rank]+=1
        symbol_histogram[symbol][rank]+=1
    if below!=45:
        raise ArithmeticError('Unexpected number of binary coherent slices')
    return {'a':2,'b':2,'nonzero_slices_checked':4095,
            'slice_rank_histogram':dict(sorted(histogram.items())),
            'symbol_rank_slice_histograms':{k:dict(sorted(v.items())) for k,v in symbol_histogram.items()},
            'slices_below_2ab':below,'all_symbol_rank_bounds_verified':True,
            'entire_sub_2ab_locus_matches_constant_coherent_factor':True}


def sharp_threshold_controls():
    out=[]
    for a,b in ((2,2),(2,3),(3,3),(4,5),(5,5)):
        m=a+b-1
        f=[0]*(a*b*m)
        f[0]=f[(m-1)*b]=1
        rank=rank_mod_two(full_matrix(f,a,b))
        # The scalar Hankel has two disjoint corner blocks and the
        # outer factor is separable, so this is also its exact rank.
        if rank!=2*a*b:
            raise ArithmeticError('The sharp threshold example has incorrect rank')
        out.append({'a':a,'b':b,'outer_factor':'one at i=s=0',
                    'hankel_nonzero_positions':[0,m-1],
                    'exact_rank':2*a*b,'rank_mod_two':rank,
                    'constant_coherent_factor':has_constant_coherent_factor(f,a,b)})
    return out


def coherent_vectors(a,b,point):
    if point is None:
        return ([int(i==a-1) for i in range(a)],
                [int(j==b-1) for j in range(b)])
    return ([point**i for i in range(a)],[point**j for j in range(b)])


def three_leg_controls():
    records=[]
    for a,b,points in ((2,3,(2,-1,3)),(3,3,(None,2,-1)),(5,5,(2,None,3))):
        ax,bx=coherent_vectors(a,b,points[0])
        cy,dy=coherent_vectors(a,b,points[1])
        ez,fz=coherent_vectors(a,b,points[2])
        fx=[[((3*i+2*s+1)%7)-3 for s in range(b)] for i in range(a)]
        fy=[[((2*j+5*p+2)%11)-5 for p in range(a)] for j in range(b)]
        fz_matrix=[[((4*q+3*r+1)%13)-6 for r in range(a)] for q in range(b)]
        direct=sum(fx[i][s]*fy[j][p]*fz_matrix[q][r]*ax[p]*bx[q]*cy[r]*dy[s]*ez[i]*fz[j]
                   for i,j,p,q,r,s in product(range(a),range(b),range(a),range(b),range(a),range(b)))
        factors=(sum(fx[i][s]*ez[i]*dy[s] for i,s in product(range(a),range(b))),
                 sum(fy[j][p]*fz[j]*ax[p] for j,p in product(range(b),range(a))),
                 sum(fz_matrix[q][r]*bx[q]*cy[r] for q,r in product(range(b),range(a))))
        separated=factors[0]*factors[1]*factors[2]
        if direct!=separated:
            raise ArithmeticError('Three coherent factors did not separate the tensor')
        records.append({'a':a,'b':b,'coherent_points':list(points),
                        'source_terms_checked':(a*b)**3,'direct_integer_value':str(direct),
                        'three_linear_factors':list(factors),'separated_integer_value':str(separated),
                        'exact_factorization_verified':True})
    return records


def rectangular_screen(a,b,shape):
    n_source=a*b*(a+b-1)
    l,h,n=shape
    dims=(l*h,h*n,n*l)
    records=[]
    for axis,(block_leg,rank_one) in enumerate(zip(dims,(n,l,h))):
        others=[j for j in range(3) if j!=axis]
        lifted=rank_one+sum(n_source-dims[j] for j in others)
        excluded=block_leg>a*b and lifted<2*a*b
        records.append({'axis':axis,'block_leg_dimension':block_leg,
                        'lifted_rank_one_slice_upper_bound':lifted,
                        'threshold_2ab':2*a*b,'excluded_on_this_leg':excluded})
    return {'source_lengths':[a,b],'target_shape':list(shape),'ordinary_only':True,
            'legs':records,'ordinary_restriction_excluded':any(r['excluded_on_this_leg'] for r in records),
            'singular_degeneration_excluded':False}


def square_subsum_screen(a,b,sizes,indices):
    n_source=a*b*(a+b-1)
    d=sum(n*n for n in sizes)
    chosen=sum(sizes[i]**2 for i in indices)
    loss=n_source-d
    upper=chosen+2*loss
    return {'source_lengths':[a,b],'target_square_sizes':list(sizes),
            'common_leg_dimension':d,'kernel_dimension_per_leg':loss,
            'selected_block_indices':list(indices),'selected_common_leg_dimension':chosen,
            'maximum_lifted_slice_rank':upper,'threshold_2ab':2*a*b,
            'ordinary_restriction_excluded':chosen>=2 and upper<2*a*b,
            'reason':'three lifted subspaces have coherent long factors, forcing tensor rank at most one',
            'singular_degeneration_excluded':False}


def square_block_rank_one_screen(a,b,sizes):
    n_source=a*b*(a+b-1)
    d=sum(n*n for n in sizes)
    loss=n_source-d
    blocks=[{'size':n,'lifted_rank_one_slice_upper_bound':n+2*loss,
             'threshold_2ab':2*a*b,'excluded':n+2*loss<2*a*b}
            for n in sizes if n>=2]
    return {'source_lengths':[a,b],'target_square_sizes':list(sizes),
            'common_leg_dimension':d,'kernel_dimension_per_leg':loss,
            'non_scalar_block_tests':blocks,
            'ordinary_restriction_excluded':any(b['excluded'] for b in blocks),
            'singular_degeneration_excluded':False}


def report():
    selected=[square_subsum_screen(5,5,(14,3),(1,)),
              square_subsum_screen(5,5,(14,4),(1,)),
              square_subsum_screen(5,5,(14,1,1,1,1,1,1,1,1,1,1,1),(1,2))]
    if not all(r['ordinary_restriction_excluded'] for r in selected):
        raise ArithmeticError('A selected ordinary direct-sum exclusion failed')
    rectangular=[rectangular_screen(5,5,shape) for shape in ((13,14,16),(13,15,15),(14,14,15),(14,15,15))]
    if not all(r['ordinary_restriction_excluded'] for r in rectangular):
        raise ArithmeticError('A selected rectangular exclusion failed')
    return {'new_exponent_established':False,'improving_target_constructed':False,
            'binary_exhaustive_control':exhaustive_binary_22(),
            'sharp_threshold_controls':sharp_threshold_controls(),
            'three_leg_factorization_controls':three_leg_controls(),
            'ordinary_rectangular_exclusions':rectangular,
            'ordinary_square_subsum_exclusions':selected,
            'square_block_rank_one_screen_controls':[
                square_block_rank_one_screen(5,6,(16,3,3)),
                square_block_rank_one_screen(5,6,(16,4))],
            'singular_exclusion_claimed':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    payload=json.dumps(report(),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload,end='')
