"""Exact finite affine-group target frontier, before constructive search.

Every surviving shape is conditional on an unconstructed target degeneration.
No negative SAT result is used as a mathematical exclusion.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt,prod
import json
from pathlib import Path

from determinant_obstruction import frobenius_degrees,abelian_coset_bounds,obstruction
from rank_locus_obstruction import profile,screen
from fourier_certificate import power_interval


@lru_cache(None)
def volume_interval(volume):return power_interval(volume,3,4,10**12)


def frontier(max_prime=61,max_order=250):
    counts={'groups':0,'sorted_shapes':0,'strict_gate_shapes':0,
            'coset_excluded':0,'rank_locus_excluded':0,'determinant_excluded':0}
    survivors=[]
    for p in range(3,max_prime+1):
        if any(p%d==0 for d in range(2,isqrt(p)+1)):continue
        for r in range(2,p):
            N=p*r
            if (p-1)%r or N>max_order:continue
            counts['groups']+=1
            degrees=frobenius_degrees(p,r)
            ranks=profile(degrees)
            lo,hi=power_interval(r,9,4,10**12)
            source_lo=r+((p-1)//r)*lo
            source_hi=r+((p-1)//r)*hi
            for b in range(2,isqrt(N)+1):
                for c in range(b,N//b+1):
                    for a in range(2,b+1):
                        counts['sorted_shapes']+=1
                        shape=[a,b,c];V=a*b*c
                        vlo,vhi=volume_interval(V)
                        if source_lo>=vhi:continue
                        if source_hi>=vlo:raise ArithmeticError('refine gate precision')
                        counts['strict_gate_shapes']+=1
                        coset=abelian_coset_bounds(p,r,shape)
                        if coset['excluded']:
                            counts['coset_excluded']+=1;continue
                        rank=screen(degrees,shape,ranks)
                        if rank['excluded']:
                            counts['rank_locus_excluded']+=1;continue
                        rejected=False
                        for n,k in [(a,c),(a,b),(b,a)]:
                            if obstruction(N,degrees,n,k)['excluded']:
                                rejected=True;break
                        if rejected:
                            counts['determinant_excluded']+=1;continue
                        survivors.append({'prime':p,'index':r,'source_dimension':N,
                          'shape':shape,'volume':V,'strict_gate_margin_lower':str(vlo-source_hi),
                          'rank_locus_dimension':rank['low_rank_locus']['dimension'],
                          'rank_locus_dimension_slack':N-rank['source_dimension_required'],
                          'max_coset_size_lower':coset['max_coset_size_lower'],
                          'max_coset_size_upper':coset['max_coset_size_upper'],
                          'status':'unconstructed candidate; not an exponent result'})
    survivors.sort(key=lambda x:(x['source_dimension'],sum(x['shape']),x['volume'],x['shape']))
    return {'max_prime':max_prime,'max_order':max_order,'counts':counts,
            'survivors':survivors,'surviving_shapes':len(survivors),
            'filter_order':['strict degree-sum gate at 9/4','abelian coset ceiling',
                            'rank-locus dimension','determinant divisor'],
            'scope':'Finite complete frontier within the stated prime/order range and '
                    'coordinate-potential search class. The rank-locus and determinant '
                    'screens also apply to arbitrary complex degeneration. No SAT '
                    'negative, claimed board result or floating estimate is a filter.',
            'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-prime',type=int,default=61)
    parser.add_argument('--max-order',type=int,default=250)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=frontier(args.max_prime,args.max_order)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='survivors'},indent=2))
    print(json.dumps(result['survivors'][:16],indent=2))
