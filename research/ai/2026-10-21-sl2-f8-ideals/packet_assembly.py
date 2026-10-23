"""A conditional simultaneous target and a dense coordinate-face obstruction.

The target is unconstructed. Individual packet witnesses cannot be added
without one joint source degeneration and all cross terms checked.
"""
import argparse
from fractions import Fraction as Q
import json
from math import prod
from pathlib import Path

from sl2_f8_ideal_certificate import group
from sl2_f8_source import center_engine
from semisimple_koszul import source_ranks,padded_basic_ranks,profile


def dense_marginal_bound(order,deleted,eta):
    if any(type(v) is not int for v in [order,deleted]) or not 0<=deleted<order:
        raise ValueError('positive order and 0<=deleted<order required')
    eta = Q(eta)
    if eta<0:
        raise ValueError('nonnegative relative marginal deviation required')
    m = order-deleted
    rhs = order-6*deleted
    lhs = 3*(deleted+m*eta)
    available = rhs>0 and lhs<rhs
    return {'source_order':order,'selected_labels_per_leg':m,'deleted_per_leg':deleted,
            'relative_marginal_deviation':str(eta),'strict_positivity_lhs':str(lhs),
            'strict_positivity_rhs':rhs,'positive_completion_certified':available,
            'positive_edge_mass_factor_lower_bound':str(1-lhs/rhs) if available else None}


def rectangular_rank_profile(blocks,ambient):
    values = [None]*(ambient+1)
    values[0] = 0
    for a,b,c in blocks:
        updated = [None]*(ambient+1)
        for r,value in enumerate(values):
            if value is None:
                continue
            for k in range(min(a,b)+1):
                cost = r+c*k
                if cost<=ambient:
                    dimension = value+k*(a+b-k)
                    if updated[cost] is None or dimension>updated[cost]:
                        updated[cost] = dimension
        values = updated
    for r in range(1,ambient+1):
        if values[r] is None or values[r]<values[r-1]:
            values[r] = values[r-1]
    return values


def report():
    degrees = [1,7,7,7,7,8,9,9,9]
    blocks = [(8,9,9),(9,8,9),(9,9,8)]*2+[(7,7,7)]
    N = sum(d*d for d in degrees)
    dimensions = [sum(row[i]*row[(i+1)%3] for row in blocks) for i in range(3)]
    source = source_ranks(degrees)
    target = [0]*len(source)
    for a,b,c in blocks:
        for p,rank in enumerate(padded_basic_ranks(a,b,N)):
            target[p] += c*rank
    failures = [p for p,(s,t) in enumerate(zip(source,target)) if t>s]
    source_locus = profile(degrees)
    target_locus = rectangular_rank_profile(blocks,N)
    excess = max(source_locus[r]['dimension']-target_locus[r]-(N-dimensions[0]) for r in range(N+1))
    tau = Q(56,25)
    numerator,denominator = tau.numerator,tau.denominator
    scale = 10**10
    root = center_engine().root_floor
    upper = [root(d**numerator*scale**denominator,denominator)+1 for d in degrees]
    lower = [root(prod(row)**numerator*scale**(3*denominator),3*denominator) for row in blocks]
    masses = [Q(75,499)]*6+[Q(49,499)]
    eta = max(abs(Q(dimensions[j])*mass/(row[j]*row[(j+1)%3])-1)
              for mass,row in zip(masses,blocks) for j in range(3))
    dense = dense_marginal_bound(N,N-dimensions[0],eta)
    return {'source':'C[SL(2,F8)]','source_degrees':degrees,'source_leg_dimension':N,
            'target_blocks':[list(row) for row in blocks],'target_leg_dimensions':dimensions,
            'conditional_gate':{'tau':str(tau),'scale':scale,
                                'source_upper_terms':upper,'target_lower_terms':lower,
                                'source_upper_numerator':sum(upper),'target_lower_numerator':sum(lower),
                                'strict_margin_numerator':sum(lower)-sum(upper),
                                'normalized_difference_derivative_lower_bound':str(Q(557,8748))},
            'necessary_tests':{'full_Koszul_powers_tested':len(source),'Koszul_exclusion_powers':failures,
                               'all_rank_locus_budgets_tested':N+1,'maximum_rank_locus_excess':excess},
            'target_component_masses':list(map(str,masses)),
            'dense_coordinate_obstruction':dense,
            'scope':'A single joint source degeneration would imply omega<=2.24. It is missing. Injective group-basis coordinate maps and diagonal weights cannot realize this dense target; general input mixing remains open.',
            'proof_status':'written conditional implication and coordinate obstruction; unreviewed',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
