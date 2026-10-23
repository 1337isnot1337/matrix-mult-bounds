"""Ordinary-only low-rank span screens and two unconstructed border targets."""
import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

PARENT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PARENT/'2026-10-21-sl2-f8-ideals'))
from packet_assembly import rectangular_rank_profile
from semisimple_koszul import source_ranks,padded_basic_ranks,profile
from sl2_f8_source import center_engine


def ordinary_span_screen(degrees,blocks):
    if not degrees or any(type(d) is not int or d<1 for d in degrees):
        raise ValueError('positive source degrees required')
    if not blocks or any(len(row)!=3 or any(type(x) is not int or x<1 for x in row) for row in blocks):
        raise ValueError('positive rectangular triples required')
    N = sum(d*d for d in degrees)
    records = []
    for leg in range(3):
        rotated = [row[leg:]+row[:leg] for row in blocks]
        M = sum(a*b for a,b,c in rotated)
        k = N-M
        if k<0:
            records.append({'leg':leg,'dimension_exclusion':True,'source_dimension':N,'target_dimension':M})
            continue
        rows = []
        for r in sorted(set([0]+degrees+[row[2] for row in rotated])):
            lower = sum(d*max(d-k,0) for d in degrees if d<=r)
            upper = sum(a*b for a,b,c in rotated if c<=r)
            rows.append({'slice_rank_budget':r,'source_low_rank_span_lower':lower,
                         'target_low_rank_span_dimension':upper,'excludes_ordinary_restriction':lower>upper})
        records.append({'leg':leg,'source_dimension':N,'target_dimension':M,'codimension':k,
                        'dimension_exclusion':False,'rank_budgets':rows})
    excluded = any(row['dimension_exclusion'] or any(x['excludes_ordinary_restriction'] for x in row['rank_budgets']) for row in records)
    return {'legs':records,'ordinary_restriction_excluded':excluded,
            'general_border_degeneration_excluded':False}


def necessary_rank_tests(degrees,blocks):
    N = sum(d*d for d in degrees)
    M = sum(a*b for a,b,c in blocks)
    source = source_ranks(degrees)
    target = [sum(c*padded_basic_ranks(a,b,N)[p] for a,b,c in blocks) for p in range(len(source))]
    target_locus = rectangular_rank_profile(blocks,N)
    return {'full_Koszul_powers':len(source),
            'Koszul_exclusions':[p for p,(s,t) in enumerate(zip(source,target)) if t>s],
            'rank_locus_budgets':N+1,
            'maximum_rank_locus_excess':max(row['dimension']-value-(N-M)
                                          for row,value in zip(profile(degrees),target_locus)),
            'leg_coverage':'The block multiset is cyclically invariant; exterior duality covers remaining powers.'}


def square_border_factor_screen(degrees,blocks):
    if any(len(row)!=3 or row[0]!=row[1] or row[1]!=row[2] for row in blocks):
        return {'applicable':False,'reason':'This certificate requires square target blocks and a nonzero generic slice determinant.',
                'general_border_degeneration_excluded':False}
    ordinary = ordinary_span_screen(degrees,blocks)
    return {'applicable':True,'source_determinant_factors':[{'degree':d,'forced_exponent':max(d-ordinary['legs'][0].get('codimension',0),0)} for d in degrees],
            'degree_budget_certificate':ordinary,
            'general_border_degeneration_excluded':ordinary['ordinary_restriction_excluded'],
            'proof':'Cauchy--Binet minor divisibility and projectively closed homogeneous factorization.'}


def report():
    degrees = [7]*4
    blocks = [(d,d,d) for d in [2,3,4,9,9]]
    tau = Q(56,25)
    scale = 10**10
    root = center_engine().root_floor
    upper = [root(d**tau.numerator*scale**tau.denominator,tau.denominator)+1 for d in degrees]
    lower = [root(d**tau.numerator*scale**tau.denominator,tau.denominator) for d in [2,3,4,9,9]]
    larger_degrees = [1,7,7,7,7,8,9,9,9]
    larger_blocks = [(8,9,9),(9,8,9),(9,9,8)]*2+[(7,7,7)]
    return {'smaller_trade':{'source_degrees':degrees,'target_blocks':blocks,
                            'ordinary_span_screen':ordinary_span_screen(degrees,blocks),
                            'border_factor_screen':square_border_factor_screen(degrees,blocks),
                            'other_necessary_tests':necessary_rank_tests(degrees,blocks),
                            'conditional_gate':{'tau':str(tau),'scale':scale,'source_upper_terms':upper,
                                                'target_lower_terms':lower,'strict_margin_numerator':sum(lower)-sum(upper),
                                                'derivative_lower_bound_on_2_to_9_fourths':str(Q(11,1458))}},
            'larger_packet_target':{'source_degrees':larger_degrees,'target_blocks':larger_blocks,
                                    'ordinary_span_screen':ordinary_span_screen(larger_degrees,larger_blocks)},
            'proof_status':'written, unreviewed; ordinary rectangular screen and closed square determinant-factor screen',
            'missing_premise':'The smaller square trade is excluded even for border maps. No general singular degeneration to the larger rectangular target has been constructed.',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    # JSON roundtrip makes the programmatic report match the stored format.
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'ordinary_exclusions':{k:result[k]['ordinary_span_screen']['ordinary_restriction_excluded']
                                             for k in ['smaller_trade','larger_packet_target']},
                      'improves_omega':False},indent=2))
