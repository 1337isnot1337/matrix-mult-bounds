"""Exact source rank-locus dimension screen for semisimple group algebras.

Source: direct sum of square matrix-multiplication tensors of degrees d_i.
Its input space has dimension N=sum d_i^2 and regular slices have rank
sum d_i rank(X_i). See rank_locus_proof.md for the all-size argument.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import isqrt,prod
from pathlib import Path

from fourier_certificate import source_certificate,power_interval
from determinant_obstruction import frobenius_degrees


def profile(degrees):
    if not degrees or any(not isinstance(d,int) or d<1 for d in degrees):
        raise ValueError('positive integer source degrees required')
    N=sum(d*d for d in degrees)
    values=[None]*(N+1);values[0]=(0,[])
    for d in degrees:
        updated=[None]*(N+1)
        for r,record in enumerate(values):
            if record is None:continue
            dimension,ks=record
            for k in range(d+1):
                cost=r+d*k
                value=dimension+k*(2*d-k)
                if cost<=N and (updated[cost] is None or value>updated[cost][0]):
                    updated[cost]=(value,ks+[k])
        values=updated
    for r in range(1,N+1):
        if values[r-1] is not None and (values[r] is None or values[r-1][0]>values[r][0]):
            values[r]=values[r-1]
    return [{'rank_budget':r,'dimension':rec[0],'block_ranks':rec[1],
             'actual_regular_rank':sum(d*k for d,k in zip(degrees,rec[1]))}
            for r,rec in enumerate(values)]


def screen(degrees,shape,source_profile=None):
    if len(shape)!=3 or min(shape)<1:raise ValueError('three positive dimensions required')
    a,b,c=sorted(shape);N=sum(d*d for d in degrees)
    if b*c>N:
        return {'shape':[a,b,c],'source_dimension':N,'excluded':True,
                'reason':'ordinary flattening dimension'}
    records=source_profile if source_profile is not None else profile(degrees)
    rec=records[min(a-1,N)]
    required=b*c+rec['dimension']
    return {'shape':[a,b,c],'source_dimension':N,
            'largest_target_input':b*c,'target_minimum_nonzero_slice_rank':a,
            'low_rank_locus':rec,
            'source_dimension_required':required,
            'dimension_deficit':required-N,
            'excluded':required>N,
            'scope':'Arbitrary complex tensor degenerations, not only coordinate weights.',
            'proof_status':'written proof; unreviewed; not Lean formalized',
            'improves_omega':False}


def gate_9_fourths(degrees,shape,scale=10**12):
    # Exact intervals decide the potential improvement gate, never a float.
    src=[power_interval(d,9,4,scale) for d in degrees]
    source_lo=sum((x[0] for x in src),Q(0))
    source_hi=sum((x[1] for x in src),Q(0))
    target_lo,target_hi=power_interval(prod(shape),3,4,scale)
    if source_hi<target_lo:return True
    if source_lo>=target_hi:return False
    raise ArithmeticError('gate interval inconclusive; refine precision')


def report():
    source=source_certificate();degrees=source['irreducible_degrees'];N=source['order']
    ranks=profile(degrees)
    frontier=[]
    for b in range(2,isqrt(N)+1):
        for c in range(b,N//b+1):
            for a in range(2,b+1):
                shape=[a,b,c]
                if gate_9_fourths(degrees,shape):frontier.append(screen(degrees,shape,ranks))
    return {'source':'SL(2,5)','source_degrees':degrees,'source_dimension':N,
            'source_pin':'fourier_and_conditional_gates.json primitive central idempotents',
            'all_size_theorem':'A degeneration to M(a,b,c), a<=b<=c, requires '
                 'N >= b*c + D(a-1), where D(r)=max sum k_i(2d_i-k_i) '
                 'subject to sum d_i*k_i <=r and 0<=k_i<=d_i.',
            'frontier_coverage':'Every sorted integer shape with a>=2 and b*c<=120 '
                 'whose exact character-degree comparison is strict at 9/4.',
            'potential_improvement_shapes':frontier,
            'surviving_shapes':[r['shape'] for r in frontier if not r['excluded']],
            'affine_examples':[
                {'source':f'C{p}:C{r}','degrees':frobenius_degrees(p,r),
                 'screen':screen(frobenius_degrees(p,r),shape)}
                for p,r,shape in [(13,3,[6,6,6]),(17,4,[8,8,8]),
                    (17,4,[7,7,9]),(17,4,[7,8,8]),(19,3,[6,6,9]),
                    (19,3,[6,7,8]),(29,4,[10,10,10]),(31,5,[12,12,12]),
                    (31,6,[13,13,13]),(31,6,[12,13,13])]],
            'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'surviving_shapes':result['surviving_shapes'],
      'frontier':[(r['shape'],r.get('source_dimension_required'),r['excluded'])
                  for r in result['potential_improvement_shapes']],
      'affine_examples':[(r['source'],r['screen']['shape'],r['screen']['excluded'])
                         for r in result['affine_examples']]},indent=2))
