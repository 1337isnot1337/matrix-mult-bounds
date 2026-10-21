"""Exact all-size degree-gate and rank-locus frontier for F8^2:C7."""
import argparse
import json
from math import isqrt
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-10-20-group-potentials'))
from rank_locus_obstruction import profile,screen,gate_9_fourths


def report():
    degrees = [1]*7+[7]*9
    N = sum(d*d for d in degrees)
    ranks = profile(degrees)
    checked = 0
    improving = []
    for b in range(2,isqrt(N)+1):
        for c in range(b,N//b+1):
            for a in range(2,b+1):
                checked += 1
                shape = [a,b,c]
                if gate_9_fourths(degrees,shape):
                    improving.append(screen(degrees,shape,ranks))
    survivors = sorted(row['shape'] for row in improving if not row['excluded'])
    minimal = [row for row in survivors if not any(
        other!=row and all(x<=y for x,y in zip(other,row)) for other in survivors)]
    return {'source':'F8^2:C7','source_degrees':degrees,'source_dimension':N,
            'all_sorted_shapes_checked':checked,'improving_shape_count':len(improving),
            'rank_locus_surviving_shapes':survivors,'minimal_surviving_shapes':minimal,
            'scope':'Every sorted integer shape a>=2 with b*c<=448. Exact degree comparison at 9/4 and the existing general complex rank-locus necessary bound. No constructions.',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
