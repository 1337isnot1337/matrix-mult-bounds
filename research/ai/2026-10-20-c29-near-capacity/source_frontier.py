"""Exact one-source degree-sum and rank-locus frontier for C29:C4."""
import argparse
import json
from math import isqrt
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-10-20-group-potentials'))
from rank_locus_obstruction import profile, screen, gate_9_fourths


def run():
    degrees = [1]*4+[4]*7
    order = sum(d*d for d in degrees)
    ranks = profile(degrees)
    improving = []
    checked = 0
    for b in range(2,isqrt(order)+1):
        for c in range(b,order//b+1):
            for a in range(2,b+1):
                checked += 1
                shape = [a,b,c]
                if gate_9_fourths(degrees,shape):
                    improving.append(screen(degrees,shape,ranks))
    return {'group':'C29:C4','source_order':order,'source_degrees':degrees,
            'sorted_shapes_with_minimum_two_checked':checked,
            'improving_shapes':improving,
            'surviving_shapes':[x['shape'] for x in improving if not x['excluded']],
            'coverage':'All sorted positive integer shapes with a>=2 and b*c<=116. '
                       'Shapes with a=1 have volume<=116 and cannot pass the gate.',
            'dependencies':['Existing exact degree-sum interval checker',
                            'AI-GROUP-RANKLOCUS-002 written unreviewed rank-locus obstruction'],
            'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='improving_shapes'},indent=2))
