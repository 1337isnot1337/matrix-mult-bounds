"""The split central cover PSL(2,5) x C2, with a rational source certificate."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from data import data, ROOT, SEVEN
from central_lift import quotient
from source_certificate import exponent_gate

RESULTS = ROOT/'results/sl2-five-native-2026-10-20'


def groups():
    original, Q, receipt = data()
    n = len(Q['representatives'])
    base = {'name': 'PSL(2,5)', 'identity': 0,
            'matrices': [(q,) for q in range(n)], 'mul': Q['mul'], 'inv': Q['inv']}
    split = {'name': 'PSL(2,5) x C2', 'identity': 0,
             'matrices': [(q, b) for q in range(n) for b in range(2)],
             'mul': [[2*Q['mul'][q][r]+(a ^ b) for r in range(n) for b in range(2)]
                     for q in range(n) for a in range(2)],
             'inv': [2*Q['inv'][q]+a for q in range(n) for a in range(2)]}
    return base, split, original, Q, receipt


def certificate():
    base, split, original, Q, receipt = groups()
    spec = importlib.util.spec_from_file_location('split_cover_source_certificate',
                                                   SEVEN/'source_certificate.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    helper.group = lambda unused: base
    factor = helper.derive(0)
    if factor['complex_degrees'] != [1, 3, 3, 4, 5]:
        raise ArithmeticError('unexpected quotient character degrees')
    degrees = factor['complex_degrees']*2
    return {'group': split['name'], 'order': 120, 'complex_degrees': degrees,
            'quotient_rational_certificate': factor,
            'derivation': 'Exact rational class-algebra decomposition of the quotient, '
                          'then the two linear characters of the direct C2 factor.',
            'conditional_gate': exponent_gate(degrees, shape=(10, 10, 10)),
            'exponent_improvement': False}


def split_data():
    base, G, original, Q0, receipt = groups()
    Q = quotient(G, 1)
    if Q['mul'] != Q0['mul'] or Q['inv'] != Q0['inv']:
        raise ArithmeticError('split quotient changed its group indexing')
    if any(len(fiber) != 2 for fiber in Q['fibers'].values()):
        raise ArithmeticError('split cover must have two full colors in every inverse class')
    H = [2*q+b for q in receipt['projected_subgroup'] for b in range(2)]
    if len(H) != 24 or any(G['mul'][g][h] not in H for g in H for h in H):
        raise ArithmeticError('incorrect split normalization subgroup')
    coverage = []
    for row in receipt['anchor_coverage']:
        item = dict(row)
        g = 2*Q0['projection'][row['conjugator']]
        q = Q['inv'][item['projected_quotient']] if item['reverse_pair'] else item['projected_quotient']
        image = Q['projection'][G['mul'][G['mul'][g][2*q]][G['inv'][g]]]
        if image != item['anchor']:
            raise ArithmeticError('split anchor conjugation failed')
        item['conjugator'] = g
        coverage.append(item)
    path = RESULTS/'split-source-certificate.json'
    source = json.loads(path.read_text())
    if source['group'] != G['name'] or source['complex_degrees'] != [1, 3, 3, 4, 5]*2:
        raise ArithmeticError('incorrect split source record')
    receipt.update(group=G['name'], inverse_class_fiber_counts={1: 0, 2: 37},
                   subgroup_members=H, anchor_coverage=coverage,
                   complex_degrees=source['complex_degrees'],
                   source_certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                   conditional_gate=exponent_gate(source['complex_degrees'], shape=(10, 10, 10)))
    return G, Q, receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'degrees': result['complex_degrees'], 'gate': result['conditional_gate']}))
