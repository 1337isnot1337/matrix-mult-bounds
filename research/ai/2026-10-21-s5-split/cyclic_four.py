"""The alternative central basis S5 x C4, with unchanged complex degree cost."""
import argparse
import hashlib
import json
from pathlib import Path

from four_colors import certificate as elementary_certificate, data as elementary_data, RESULTS
from group_exact import verify_witness
from s5_source import control as binary_control


def certificate():
    result = elementary_certificate()
    result['group'] = 'S5 x C4'
    result['derivation'] = 'The verified S5 factor times the four linear characters of C4.'
    return result


def data(shape=None):
    G, Q, receipt = elementary_data(shape)
    M, inverse = Q['mul'], Q['inv']
    G['name'] = 'S5 x C4'
    G['mul'] = [[4*M[q][r]+(a+b) % 4 for r in range(120) for b in range(4)]
                for q in range(120) for a in range(4)]
    G['inv'] = [4*inverse[q]+(-a) % 4 for q in range(120) for a in range(4)]
    Q['fibers'] = {q: sorted({min(4*q+c, G['inv'][4*q+c]) for c in range(4)})
                   for q in Q['classes']}
    if sum(map(len, Q['fibers'].values())) != 263:
        raise ArithmeticError('incorrect cyclic-center inverse classes')
    path = RESULTS/'cyclic-four-source-certificate.json'
    if json.loads(path.read_text()) != certificate():
        raise ArithmeticError('changed cyclic-center source certificate')
    receipt.update(group=G['name'], source_certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        central_group='C4', full_inverse_classes=263,
        central_slice_rank_three_cut_applicable=False)
    return G, Q, receipt


def control():
    G, Q, receipt = data()
    known = binary_control()['witness']
    # The old C2 embeds as the order-two subgroup of C4.
    sets = [[4*(g//2)+2*(g % 2) for g in S] for S in known['sets']]
    return {'embedding': 'C2 color b maps to C4 color 2b',
            'witness': {'sets': sets, 'potentials': known['potentials'],
                        'verification': verify_witness(G, sets, known['potentials'])},
            'central_slice_rank_three_cut_applicable': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--control', action='store_true')
    args = parser.parse_args()
    result = control() if args.control else certificate()
    args.output.write_text(json.dumps(result, indent=2)+'\n')
