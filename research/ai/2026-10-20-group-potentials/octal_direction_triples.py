"""Exact constant-direction triple frontier from normalized pair survivors."""
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path
import time

from octal_fixed_frontier import options
from mask_packing import exact_pack
from quaternary_directions import sumspace


def frontier(source):
    start=time.monotonic();data=json.loads(source.read_text())
    # The other three normalized first-plane types have no pair survivors.
    if any(row['first_template_ratio']!=8 for row in data['survivors']):
        raise ValueError('unexpected first-plane type; extend the reduction')
    rows=data['survivors'];counts={'ordered_pair_candidates':len(rows)**2,
            'complementary_direction_triples':0,'exact_third_pair_checks':0}
    survivors=[];Aplane=[0,1,8,9]
    for left,right in product(rows,repeat=2):
        Bplane=left['second_plane'];Cplane=right['second_plane']
        if len(sumspace(Aplane,Bplane,Cplane))!=64:continue
        counts['complementary_direction_triples']+=1
        v=left['second_short_direction'];w=min(x for x in Bplane[1:] if x!=v);B=[0,v,w]
        u=right['second_short_direction'];z=min(x for x in Cplane[1:] if x!=u);C=[0,u,z]
        result=exact_pack(options(B,C,v,u))
        counts['exact_third_pair_checks']+=1
        if not result['satisfiable']:continue
        survivors.append({'base_columns':[1,8,v,w,u,z],
             'third_pair_local_packing':result['selected_masks']})
    return {'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
       'counts':counts,'surviving_direction_triples':survivors,
       'surviving_count':len(survivors),'elapsed_seconds':time.monotonic()-start,
       'scope':'Complete local triple frontier for the stated constant-direction, '
               'common-short-fiber pattern and normalization. No global offset '
               'assignment or potential witness. No exponent improvement.',
       'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=frontier(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='surviving_direction_triples'},indent=2))
