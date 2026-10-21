"""Exact S5 and S5 x C2 source data; no target degeneration is supplied."""
import argparse
import hashlib
import importlib.util
from itertools import permutations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SEVEN = Path(__file__).resolve().parents[1]/'2026-10-20-sl2-seven'
sys.path.insert(0, str(SEVEN))
sys.path.insert(0, str(SEVEN/'imported'))
NATIVE = Path(__file__).resolve().parents[1]/'2026-10-20-sl2-five-native-parity'
sys.path.insert(0, str(NATIVE))
from central_lift import quotient


def group(split=False):
    P = list(permutations(range(5)))
    lookup = {p: i for i, p in enumerate(P)}
    M = [[lookup[tuple(p[q[i]] for i in range(5))] for q in P] for p in P]
    inverse = [next(j for j in range(120) if M[i][j] == 0) for i in range(120)]
    if not split:
        return {'name': 'S5', 'identity': 0, 'matrices': P, 'mul': M, 'inv': inverse}
    return {'name': 'S5 x C2', 'identity': 0,
            'matrices': [(p, b) for p in P for b in range(2)],
            'mul': [[2*M[p][q]+(a ^ b) for q in range(120) for b in range(2)]
                    for p in range(120) for a in range(2)],
            'inv': [2*inverse[p]+a for p in range(120) for a in range(2)]}


def certificate():
    spec = importlib.util.spec_from_file_location('s5_rational_source', SEVEN/'source_certificate.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    helper.group = lambda unused: group()
    factor = helper.derive(0)
    if factor['complex_degrees'] != [1, 1, 4, 4, 5, 5, 6]:
        raise ArithmeticError('unexpected S5 rational central decomposition')
    degrees = factor['complex_degrees']*2
    return {'group': 'S5 x C2', 'order': 240, 'complex_degrees': degrees,
            'first_factor_rational_certificate': factor,
            'conditional_gate': helper.exponent_gate(degrees, shape=(13, 14, 14)),
            'degeneration_constructed': False, 'exponent_improvement': False}


def data():
    G = group(split=True)
    Q = quotient(G, 1)
    if len(Q['classes']) != 72 or any(len(f) != 2 for f in Q['fibers'].values()):
        raise ArithmeticError('incorrect split S5 inverse-class colors')
    H = [g for g, (p, b) in enumerate(G['matrices']) if p[4] == 4]
    projected = sorted({Q['projection'][g] for g in H})
    orbits, coverage = [], []
    pending = set(projected)-{0}
    while pending:
        q = min(pending)
        orbit = {Q['projection'][G['mul'][G['mul'][g][2*q]][G['inv'][g]]] for g in H}
        orbits.append(min(orbit))
        pending -= orbit
    if len(H) != 48 or len(projected) != 24 or len(orbits) != 4:
        raise ArithmeticError('wrong index-five subgroup or pair orbits')
    for q in projected:
        if not q:
            continue
        for g in H:
            image = Q['projection'][G['mul'][G['mul'][g][2*q]][G['inv'][g]]]
            if image in orbits:
                coverage.append({'projected_quotient': q, 'conjugator': g,
                                 'reverse_pair': False, 'anchor': image})
                break
        else:
            raise ArithmeticError('uncovered first-pair orbit')
    path = ROOT/'results/s5-split-2026-10-21/source-certificate.json'
    cert = json.loads(path.read_text())
    return G, Q, {'group': G['name'], 'projected_order': 120,
        'inverse_class_fiber_counts': {1: 0, 2: 72}, 'subgroup_order': 48,
        'subgroup_index': 5, 'subgroup_members': H, 'projected_subgroup': projected,
        'first_pair_anchor_disjunction': orbits, 'anchor_coverage': coverage,
        'complex_degrees': cert['complex_degrees'],
        'source_certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'conditional_gate': cert['conditional_gate'], 'exponent_improvement': False}


def rank_screen():
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'2026-10-20-group-potentials'))
    from rank_locus_obstruction import screen
    return screen([1, 1, 4, 4, 5, 5, 6]*2, [13, 14, 14])


def control():
    # Embed the existing quotient group by its faithful action on five cosets.
    from data import data as old_data
    old, A, receipt = old_data()
    H = receipt['projected_subgroup']
    cosets = sorted({tuple(sorted(A['mul'][g][h] for h in H)) for g in range(60)})
    coset_index = {g: i for i, C in enumerate(cosets) for g in C}
    P = group()
    lookup = {p: i for i, p in enumerate(P['matrices'])}
    image = [lookup[tuple(coset_index[A['mul'][q][C[0]]] for C in cosets)] for q in range(60)]
    if len(set(image)) != 60 or any(P['mul'][image[q]][image[r]] != image[A['mul'][q][r]]
                                  for q in range(60) for r in range(60)):
        raise ArithmeticError('five-coset action is not a faithful homomorphism')
    if any(sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2
           for p in (P['matrices'][g] for g in image)):
        raise ArithmeticError('quotient image is not alternating')
    previous = ROOT/'results/sl2-five-native-2026-10-20/split-control3.json'
    known = json.loads(previous.read_text())['witness']
    sets = [[2*image[g//2]+g % 2 for g in row] for row in known['sets']]
    from group_exact import verify_witness
    return {'group': 'S5 x C2', 'inherited_control': str(previous.relative_to(ROOT)),
            'quotient_action_image': image,
            'witness': {'sets': sets, 'potentials': known['potentials'],
                        'verification': verify_witness(group(split=True), sets, known['potentials'])},
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'degrees': report['complex_degrees'], 'gate': report['conditional_gate']}))
