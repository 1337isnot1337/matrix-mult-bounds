"""Exact support degenerations and conditional arithmetic.

These degenerations produce explicit intermediate tensors. They do not
construct any exponent-improving multiplication target.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def source_terms(a,b):
    m=a+b-1
    for i,j,p,q,r,s in product(range(a),range(b),range(a),range(b),range(a),range(b)):
        coordinates=((i*m+p+q)*b+s,(j*a+p)*m+r+s,((i+j)*b+q)*a+r)
        weights=(p+q-i-s,r+s-j-p,i+j-q-r)
        yield coordinates,weights


def valuation(weights,mode):
    if mode=='full':
        return 0
    if mode=='step':
        return sum(w<c for w,c in zip(weights,(0,0,1)))
    if mode=='parity000':
        return sum(w//2 for w in weights)
    if mode=='parity110':
        return sum((w+c)//2 for w,c in zip(weights,(1,1,0)))
    raise ValueError('Unknown support mode')


def support_points(a,b,mode):
    minimum={'full':0,'step':1,'parity000':-1,'parity110':0}[mode]
    return [point for point,weights in source_terms(a,b)
            if valuation(weights,mode)==minimum]


def character_counts(a,b):
    return Counter(k-i-s for i,k,s in product(range(a),range(a+b-1),range(b)))


def support_report(a,b,mode):
    n=a*b*(a+b-1)
    levels=Counter()
    for _,weights in source_terms(a,b):
        if sum(weights)!=0:
            raise ArithmeticError('Source torus weights do not sum to zero')
        levels[valuation(weights,mode)]+=1
    minimum=min(levels)
    points=support_points(a,b,mode)
    if len(points)!=levels[minimum]:
        raise ArithmeticError('Retained support is not the minimum valuation level')
    counts=[Counter(p[axis] for p in points) for axis in range(3)]
    patterns=Counter(''.join(str(w%2) for w in weights)
                     for _,weights in source_terms(a,b)
                     if valuation(weights,mode)==minimum)
    return {'a':a,'b':b,'source_leg_dimension':n,'mode':mode,
            'valuation_counts':dict(sorted(levels.items())),
            'minimum_valuation':minimum,'retained_terms':len(points),
            'retained_parity_patterns':dict(sorted(patterns.items())),
            'active_leg_dimensions':[len(c) for c in counts],
            'minimum_coordinate_slice_ranks':[min(c.values()) for c in counts]}


def frac_record(x):
    return [str(x.numerator),str(x.denominator)]


def score_capacity(a,b,z,t,cutoffs=(0,0,1)):
    counts=character_counts(a,b)
    sums=[sum((c*z**(w<cutoff)*t**w for w,c in counts.items()),Fraction(0))
          for cutoff in cutoffs]
    cubed=sums[0]*sums[1]*sums[2]/z
    return sums,cubed


def exact_step_certificates():
    out=[]
    for a,b,t,shape in ((4,4,Fraction(3,4),(10,10,11)),
                        (4,5,Fraction(3,4),(12,12,13)),
                        (5,5,Fraction(25,32),(14,14,14))):
        z=Fraction(1,7)
        sums,bound=score_capacity(a,b,z,t)
        volume=shape[0]*shape[1]*shape[2]
        if not bound<volume**2:
            raise ArithmeticError('The rational score certificate does not exclude its target')
        out.append({'a':a,'b':b,'mode':'step','score_z':frac_record(z),
                    'score_t':frac_record(t),'partition_sums':[frac_record(x) for x in sums],
                    'capacity_cubed':frac_record(bound),'excluded_target':list(shape),
                    'target_volume_squared':volume**2,
                    'integer_comparison':{'left':str(bound.numerator),
                                          'right':str(volume**2*bound.denominator)},
                    'strict_comparison_verified':True})
    return out


def exact_parity_certificates():
    n=225
    records=[]
    for mode,even,odd,z in (('parity000',(113,)*3,(112,)*3,Fraction(113,56)),
                           ('parity110',(112,112,113),(113,113,112),Fraction(2))):
        sums=[e+o*z for e,o in zip(even,odd)]
        bound=sums[0]*sums[1]*sums[2]/z**2
        target=14**2+4**2
        records.append({'mode':mode,'source_leg_dimension':n,
                        'shifted_even_dimensions':list(even),'shifted_odd_dimensions':list(odd),
                        'score_z':frac_record(z),'score_product':frac_record(z*z),
                        'partition_sums':[frac_record(x) for x in sums],
                        'capacity_cubed':frac_record(bound),
                        'target_direct_sum_sizes':[14,4],'target_leg_dimension':target,
                        'target_leg_dimension_cubed':target**3,
                        'not_excluded_by_this_bound':target**3<=bound,
                        'target_constructed':False})
    return records


def conditional_direct_sum_certificates():
    out=[]
    for a,b,sizes,p,q,lower in ((5,5,(14,4),2243,1000,(20708,1246)),
                               (4,5,(12,3),281,125,(14972,663)),
                               (4,4,(10,3),5623,2500,(9986,665))):
        checks=[(6*n)**p>lo**q for n,lo in zip(sizes,lower)]
        base=(3*(a+b)-2)**3
        if not all(checks) or sum(lower)<=base:
            raise ArithmeticError('Conditional exponent arithmetic failed')
        out.append({'a':a,'b':b,'target_direct_sum_sizes':list(sizes),
                    'conditional_exponent':[p,q],'term_lower_integers':list(lower),
                    'strict_power_comparisons':checks,'lower_integer_sum':sum(lower),
                    'source_comparison_cube':base,'target_constructed':False,
                    'new_exponent_established':False})
    return out


def exact_monomial_control(a,b):
    """The parity110 source contains M(a,a,b) for a<=b."""
    if not 1<=a<=b:
        raise ValueError('Require 1<=a<=b')
    m=a+b-1
    picks=[[(i*m+i+j)*b+j for i,j in product(range(a),range(a))],
           [(k*a+j)*m+j for j,k in product(range(a),range(b))],
           [((i+k)*b+i)*a for k,i in product(range(b),range(a))]]
    inverse=[{value:i for i,value in enumerate(p)} for p in picks]
    if any(len(inv)!=len(p) for inv,p in zip(inverse,picks)):
        raise ArithmeticError('Control coordinate maps are not injective')
    actual=Counter(tuple(inverse[axis][pt[axis]] for axis in range(3))
                   for pt in support_points(a,b,'parity110')
                   if all(pt[axis] in inverse[axis] for axis in range(3)))
    expected=Counter((i*a+j,j*b+k,k*a+i) for i,j,k in product(range(a),range(a),range(b)))
    if actual!=expected:
        raise ArithmeticError('An actual target coefficient differs from the monomial control')
    return {'source_lengths':[a,b],'source_mode':'parity110','target_shape':[a,a,b],
            'source_coordinates_per_target_leg':picks,
            'all_target_coefficients_checked':a**4*b**2,'nonzero_target_coefficients':a*a*b,
            'exact_integer_control_verified':True,'new_exponent_established':False}


def rank_mod_prime(matrix,prime):
    """Exact Gaussian elimination over a prime field."""
    matrix=[[int(x)%prime for x in row] for row in matrix]
    rank=0
    for column in range(len(matrix[0])):
        pivot=next((r for r in range(rank,len(matrix)) if matrix[r][column]),None)
        if pivot is None:
            continue
        matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
        inverse=pow(matrix[rank][column],-1,prime)
        matrix[rank][column:]=[x*inverse%prime for x in matrix[rank][column:]]
        lead=matrix[rank]
        for r in range(rank+1,len(matrix)):
            coefficient=matrix[r][column]
            if coefficient:
                matrix[r][column:]=[(x-coefficient*y)%prime
                                   for x,y in zip(matrix[r][column:],lead[column:])]
        rank+=1
        if rank==len(matrix):
            break
    return rank


def parity_slice_controls():
    """Deterministic exact rank checks, not a generic-rank assumption."""
    out=[]
    for mode in ('parity000','parity110'):
        points=support_points(5,5,mode)
        records=[]
        for axis in range(3):
            seed=2026102800+axis
            state=seed
            coefficients=[]
            for _ in range(225):
                state^=(state<<13)&0xffffffff
                state^=state>>17
                state^=(state<<5)&0xffffffff
                coefficients.append(state%101)
            others=[j for j in range(3) if j!=axis]
            matrix=[[0]*225 for _ in range(225)]
            for point in points:
                matrix[point[others[0]]][point[others[1]]]+=coefficients[point[axis]]
            rank=rank_mod_prime(matrix,101)
            expected=224 if mode=='parity000' else 225
            if rank!=expected:
                raise ArithmeticError('An archived exact parity slice rank did not replay')
            records.append({'axis':axis,'xorshift32_seed':seed,'prime':101,
                            'exact_rank_mod_prime':rank,'rational_rank_lower_bound':rank})
        out.append({'source_lengths':[5,5],'source_mode':mode,
                    'coefficient_generator':'xorshift32(13,17,5), unsigned state modulo101',
                    'slices':records})
    return out


def report():
    return {'new_exponent_established':False,'improving_target_constructed':False,
            'support_degenerations':[support_report(a,b,mode)
                                    for a,b in ((2,2),(4,4),(4,5),(5,5))
                                    for mode in ('step','parity000','parity110')],
            'exact_step_score_certificates':exact_step_certificates(),
            'exact_parity_score_certificates':exact_parity_certificates(),
            'conditional_direct_sum_certificates':conditional_direct_sum_certificates(),
            'exact_parity_slice_controls':parity_slice_controls(),
            'exact_monomial_controls':[exact_monomial_control(a,b) for a,b in ((2,2),(2,3),(5,5))]}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    payload=json.dumps(report(),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload,end='')
