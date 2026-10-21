"""Exact telescoping obstruction for the twelve local C29:C4 survivors.

At identity quotient the three cyclic pair-center differences sum to zero
in each scalar fiber. The same holds after subtracting the identity-fiber
centers. None of the enumerated relative packing triples satisfies it.
"""
import argparse
from itertools import product
import json
from pathlib import Path

from offset_gluing import packing_list


def run(source):
    data = json.loads(source.read_text())
    records = []
    for base in data['records']:
        for candidate in base['survivors']:
            allowed = [packing_list(candidate['cells'],f,g,1)
                       for f,g in [(0,1),(1,2),(2,0)]]
            tested = coherent = 0
            for rows in product(*allowed):
                tested += 1
                if all(sum(column) % 29 == 0 for column in zip(*rows)):
                    coherent += 1
            records.append({'base_directions':base['base_directions'],
                            'family_indices':candidate['family_indices'],
                            'cells':candidate['cells'],
                            'identity_pair_packing_lists':allowed,
                            'packing_triples_checked':tested,
                            'coherent_triples':coherent})
    return {'claim':'AI-GROUP-C29-TARGET-009','group':'C29:C4','shape':[10]*3,
            'local_configurations_checked':len(records),'records':records,
            'coherent_configurations':sum(r['coherent_triples'] for r in records),
            'scope':__doc__,'status':'proof-written-unreviewed','improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'records'},indent=2))
