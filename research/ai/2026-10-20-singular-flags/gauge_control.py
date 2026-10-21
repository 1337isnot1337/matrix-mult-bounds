"""Exact coefficient evaluation of a misleading masked-residual sequence."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def evaluate(t):
    t=Fraction(t)
    if t<=0:raise ValueError('positive torus scale required')
    points=[(0,0),(0,1),(1,0)]
    xp=[0,1];yp=[1,0,2]
    rows=[{0,1,3},{1},{2}]
    wx=[0,1];wy=[0,3,2];wz=[-3,0,-1]
    masked=full=Fraction(0);unwanted=[];checked=0
    for p in range(2):
        for y,(a,b) in enumerate(points):
            for z,(c,d) in enumerate(points):
                wanted=int(p==a+c and a+b+c+d==1)
                actual=int(xp[p]+yp[y] in rows[z])
                weight=wx[p]+wy[y]+wz[z]
                if wanted and weight!=0:raise ArithmeticError('target not stabilized')
                if weight==0 and actual!=wanted:raise ArithmeticError('zero-weight fit incorrect')
                value=actual*t**weight
                error=(value-wanted)**2
                if weight<=0:masked+=error
                full+=error;checked+=1
                if actual and not wanted:unwanted.append(weight)
    return {'scale':str(t),'coefficients_checked':checked,
            'masked_squared_error':str(masked),'full_squared_error':str(full),
            'unwanted_weights':sorted(unwanted),
            'pole_in_original_parameter_direction':any(w<0 for w in unwanted)}


def run():
    return {'scope':'Exact source-family negative calibration; not an exponent or source nonexistence result.',
            'cases':[evaluate(t) for t in [1,2,4,8,16,32]],
            'floating_values_used_for_acceptance':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path)
    args=parser.parse_args();text=json.dumps(run(),indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')
