"""Exact leading-flag obstruction for a specified strict target grading."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def inspect(m,B,eta,beta=1):
    if m<2 or B<1 or len(eta)!=m or beta<=0:
        raise ValueError('positive dimensions, m offsets and a positive shared slope required')
    points=[(a,d-a) for d in range(m) for a in range(d+1)]
    n=len(points)
    if B<n:raise ValueError('target input dimension exceeds source input')
    wy=[eta[a+b]-beta*a for a,b in points]
    wz=[-eta[m-1-c-d]-beta*c for c,d in points]
    if len(set(wy))!=n or len(set(wz))!=n:
        raise ValueError('strict coordinate weights required; perturb ties separately')
    rank_y={value:index for index,value in enumerate(sorted(wy))}
    rank_z={value:index for index,value in enumerate(sorted(wz))}
    certificates=[];forced=0
    for p in range(m):
        for y,(a,b) in enumerate(points):
            first_degree=m-1-p
            second_degree=B-1-rank_y[wy[y]]
            for z,(c,d) in enumerate(points):
                output_pivot=rank_z[wz[z]]
                if first_degree+second_degree!=output_pivot:continue
                forced+=1;weight=beta*p+wy[y]+wz[z]
                wanted=p==a+c and a+b+c+d==m-1
                if weight<0 or(weight==0 and not wanted):
                    certificates.append({'p':p,'y':[a,b],'z':[c,d],
                                         'source_input_degrees':[first_degree,second_degree],
                                         'source_output_pivot':output_pivot,
                                         'weight':str(weight),'target_coefficient':int(wanted)})
    return {'m':m,'B':B,'eta':list(map(str,eta)),'beta':str(beta),
            'forced_nonzero_entries':forced,'forbidden_entries':certificates,
            'excluded_in_stated_constant_matrix_class':bool(certificates),
            'proof_status':'Written proof, unreviewed; normal_form.md',
            'excludes_general_Laurent_inputs':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--m',type=int,default=4);parser.add_argument('--B',type=int,default=10)
    parser.add_argument('--eta',default='7,14,21,0');parser.add_argument('--beta',type=Fraction,default=Fraction(1))
    parser.add_argument('--output',type=Path)
    args=parser.parse_args();report=inspect(args.m,args.B,list(map(Fraction,args.eta.split(','))),args.beta)
    text=json.dumps(report,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')
