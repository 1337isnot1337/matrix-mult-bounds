"""Exact identity-quotient gluing for the stated unequal C29:C4 frontier.

Membership in the third complete packing list checks all possibilities for
that vector after the other two are chosen. Empty fibers contribute empty
masks with every center allowed, so the test remains a necessary relaxation.
"""
import argparse
from itertools import product
import json
from pathlib import Path

from offset_gluing import packing_list


def coherent_triples(allowed):
    order = sorted(range(3),key=lambda i:len(allowed[i]))
    i,j,k = order
    third = set(allowed[k])
    count = checked = 0
    for x,y in product(allowed[i],allowed[j]):
        checked += 1
        if tuple((-a-b) % 29 for a,b in zip(x,y)) in third:
            count += 1
    return count,checked


def run(source):
    data = json.loads(source.read_text())
    records = []
    for base in data['records']:
        for candidate in base['survivors']:
            allowed = [packing_list(candidate['cells'],f,g,1)
                       for f,g in [(0,1),(1,2),(2,0)]]
            coherent,checked = coherent_triples(allowed)
            records.append({'base_directions':base['base_directions'],
                            'family_indices':candidate['family_indices'],
                            'cells':candidate['cells'],
                            'identity_pair_packing_lists':allowed,
                            'pair_combinations_checked':checked,
                            'coherent_packing_triples':coherent})
    return {'claim':'AI-GROUP-C29-RECTANGULAR-010','group':'C29:C4',
            'shape':data['shape'],'local_configurations_checked':len(records),
            'coherent_configurations':sum(r['coherent_packing_triples']>0 for r in records),
            'records':records,'scope':__doc__,'status':'proof-written-unreviewed',
            'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
