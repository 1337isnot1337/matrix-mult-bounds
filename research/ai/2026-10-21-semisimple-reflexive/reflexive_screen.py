"""Credited finite-domain AKM reflexivity bound; ordinary restrictions only."""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

PARENT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PARENT/'2026-10-21-semisimple-low-slices'))
from low_slice_spans import necessary_rank_tests,square_border_factor_screen
from sl2_f8_source import center_engine


def rank_one_span_lower(d,codimension):
    if type(d) is not int or d<1 or type(codimension) is not int or codimension<0:
        raise ValueError('positive dimension and nonnegative codimension required')
    return d*d-sum(min(d,max(codimension-s+1,0)) for s in range(1,d+1))


def screen(degrees,blocks):
    N = sum(d*d for d in degrees)
    records = []
    for leg in range(3):
        rows = [list(row[leg:]+row[:leg]) for row in blocks]
        M = sum(a*b for a,b,c in rows)
        k = N-M
        if k<0:
            raise ValueError('target input dimension exceeds source')
        budgets = []
        for r in sorted(set(degrees+[row[2] for row in rows])):
            lower = sum(rank_one_span_lower(d,k) for d in degrees if d<=r)
            upper = sum(a*b for a,b,c in rows if c<=r)
            budgets.append({'rank_budget':r,'source_span_lower':lower,'target_span_dimension':upper,
                            'excludes_ordinary_restriction':lower>upper})
        records.append({'leg':leg,'codimension':k,'budgets':budgets})
    return {'legs':records,'ordinary_restriction_excluded':any(row['excludes_ordinary_restriction'] for leg in records for row in leg['budgets']),
            'general_border_degeneration_excluded':False}


def candidate(degrees,sides):
    blocks = [(d,d,d) for d in sides]
    tau = Q(221,100);scale = 10**10;root = center_engine().root_floor
    upper = [root(d**tau.numerator*scale**tau.denominator,tau.denominator)+1 for d in degrees]
    lower = [root(d**tau.numerator*scale**tau.denominator,tau.denominator) for d in sides]
    return {'source_degrees':degrees,'target_sides':sides,
            'ordinary_reflexive_screen':screen(degrees,blocks),
            'other_necessary_tests':necessary_rank_tests(degrees,blocks),
            'square_determinant_screen':square_border_factor_screen(degrees,blocks),
            'conditional_gate':{'tau':str(tau),'scale':scale,'source_upper_terms':upper,'target_lower_terms':lower,
                                'strict_margin_numerator':sum(lower)-sum(upper)},
            'joint_degeneration_constructed':False}


def report():
    packet_degrees = [1,7,7,7,7,8,9,9,9]
    packet_blocks = [(8,9,9),(9,8,9),(9,9,8)]*2+[(7,7,7)]
    return {'external_theorem':'AKM10 Theorem2.7 proof equations2.1-2.4; algebraically closed field C',
            'compact_candidates':[candidate([7]*3,[4,11]),candidate([1,7,7,7,7,8],[3,9,9,9])],
            'larger_packet_ordinary_screen':screen(packet_degrees,packet_blocks),
            'sharp_examples':{'d7_k5_rank_one_span':rank_one_span_lower(7,5),'d7_k10_rank_one_span':rank_one_span_lower(7,10)},
            'proof_status':'written, unreviewed ordinary application of an external theorem',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'conditional_margins':[row['conditional_gate']['strict_margin_numerator'] for row in result['compact_candidates']],
                      'improves_omega':False},indent=2))
