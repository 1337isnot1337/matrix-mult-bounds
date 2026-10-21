"""Deterministic even-slice pencil discovery and count-cover input export."""
import argparse
from itertools import product
import json
from math import comb
from pathlib import Path
import random

from closure_certificate import koszul_matrix,rank_mod,tables,source_frontier


def discover():
    records = []
    for d,p in [(4,1),(6,2)]:
        for a,b in product(range(1,5),repeat=2):
            best = None
            for attempt in range(3):
                seed = 20261021+10000*d+100*a+10*b+attempt
                rng = random.Random(seed)
                slices = [[[rng.randrange(-2,3) for _ in range(b)] for _ in range(a)] for _ in range(d)]
                matrix = koszul_matrix(slices,p)
                rank = rank_mod(matrix,101)
                row = {'a':a,'b':b,'slice_dimension':d,'p':p,'integer_slices':slices,
                       'rank_lower_bound':rank,'rank_one_contribution':comb(d-1,p),
                       'matrix_format':[len(matrix),len(matrix[0])],'seed':seed,'modulus':101}
                if best is None or rank>best['rank_lower_bound']:
                    best = row
                if rank==min(len(matrix),len(matrix[0])):
                    break
            records.append(best)
    return {'records':records}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base_pencils',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--table-output',type=Path,required=True)
    parser.add_argument('--shape-output',type=Path,required=True)
    args = parser.parse_args()
    even = discover()
    base = json.loads(args.base_pencils.read_text())
    levels = tables(base,even)
    for path in [args.output,args.table_output,args.shape_output]:
        path.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(even,indent=2)+'\n')
    args.table_output.write_text(str(len(levels))+'\n'+'\n'.join(
        str(divisor)+' '+' '.join(str(v) for row in table for v in row)
        for d,p,divisor,table in levels)+'\n')
    args.shape_output.write_text('\n'.join(' '.join(map(str,row))
        for row in source_frontier()['minimal_surviving_shapes'])+'\n')
