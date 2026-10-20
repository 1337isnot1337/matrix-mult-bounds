"""Exact source-action orbits and strictly conditional exponent gates."""
from fractions import Fraction as Q
import argparse
import json
from pathlib import Path

from octal_group import scale
from fourier_certificate import power_interval


def source(dimension,target):
    order=8**dimension;remaining=set(range(1,order));orbits=[]
    while remaining:
        first=min(remaining);orbit={scale(a,first) for a in range(1,8)}
        if len(orbit)!=7 or not orbit.issubset(remaining):raise ArithmeticError('not a free scalar orbit')
        remaining.difference_update(orbit);orbits.append(sorted(orbit))
    degrees=[1]*7+[7]*len(orbits);N=7*order
    if sum(d*d for d in degrees)!=N:raise ArithmeticError('wrong sum of irrep squares')
    bound=Q(2249,1000);lo,hi=power_interval(7,bound.numerator,bound.denominator,10**10)
    source_hi=7+len(orbits)*hi
    target_lo=power_interval(target,bound.numerator,bound.denominator,10**10)[0]
    if source_hi>=target_lo:raise ArithmeticError('conditional gate fails')
    return {'group':f'F8^{dimension}:C7','order':N,
       'normal_nonzero_scalar_orbits':orbits,'irreducible_degrees':degrees,
       'source_bridge':'Free scalar action on the nontrivial additive dual characters; '
                       'induction gives degree-seven irreducibles, plus seven quotient characters.',
       'target_shape':[target]*3,'conditional_bound':str(bound),
       'source_power_sum_upper':str(source_hi),'target_power_lower':str(target_lo),
       'strict_gate_margin_lower':str(target_lo-source_hi),
       'prerequisite':'A full verified target degeneration, UNCONSTRUCTED in these reports.',
       'actual_improvement_established':False}


def report():return {'sources':[source(2,19),source(3,48)],'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in row.items() if k not in ['normal_nonzero_scalar_orbits','irreducible_degrees']}
                      for row in result['sources']],indent=2))
