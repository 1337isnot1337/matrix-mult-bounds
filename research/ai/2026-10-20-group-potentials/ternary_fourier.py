"""Integer Fourier certificate: no three 4-sets have unique sums in F3^4.

The all-set reduction is proved in ternary_fourier_proof.md. This program
checks the canonical affine-independent Fourier spectrum and every entry of
two elementary scalar inequalities. No solver or floating arithmetic is used.
"""
from collections import Counter
from itertools import product
import argparse
import json
from pathlib import Path


def squared_character_sum(exponents):
    counts=[exponents.count(j) for j in range(3)]
    a,b,c=counts
    return a*a+b*b+c*c-a*b-a*c-b*c


def certificate():
    spectrum=Counter()
    for dual in product(range(3),repeat=4):
        if dual==(0,0,0,0):continue
        spectrum[squared_character_sum([0,*dual[:3]])]+=1
    if spectrum!={1:36,4:18,7:24,16:2}:
        raise ArithmeticError('unexpected Fourier spectrum')
    weights={1:-26,4:37,7:73,16:100}
    checks=[]
    for x,y,z in product(sorted(spectrum),repeat=3):
        basic=1+(x-1)+(y-1)+(z-1)+9*((x>1)+(y>1)+(z>1)-1)
        margin=3*x*y*z-weights[x]-weights[y]-weights[z]
        if x*y*z<basic or margin<0:
            raise ArithmeticError('invalid scalar inequality')
        checks.append({'values':[x,y,z],'threefold_margin':margin})
    n=sum(spectrum.values());total=sum(x*c for x,c in spectrum.items())
    above_one=sum(c for x,c in spectrum.items() if x>1)
    basic_lower=n+3*(total-n)+9*(3*above_one-n)
    transport_lower=sum(weights[x]*c for x,c in spectrum.items())
    required=81*64-4**6
    if not required<basic_lower<=transport_lower:
        raise ArithmeticError('Parseval contradiction failed')
    return {'ambient_group':'C3^4','target_set_sizes':[4,4,4],
        'nontrivial_spectrum':{str(x):spectrum[x] for x in sorted(spectrum)},
        'nontrivial_character_count':n,'spectrum_sum':total,
        'spectrum_values_above_one_count':above_one,
        'unique_sum_parseval_required':required,
        'elementary_lower_bound':basic_lower,
        'stronger_scalar_weights':{str(x):weights[x] for x in sorted(weights)},
        'stronger_lower_bound':transport_lower,
        'scalar_inequalities':checks,
        'conclusion':'No three four-element subsets have an injective sum map.',
        'proof_status':'written-unreviewed; all-set reduction in companion proof',
        'scope':'An abelian-subgroup obstruction to coordinate-potential group '
                'constructions; not an obstruction to arbitrary degeneration.',
        'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=certificate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='scalar_inequalities'},indent=2))
