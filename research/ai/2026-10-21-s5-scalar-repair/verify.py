"""Maintained-dependency replay of the scalar repair route and finite controls."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from scalar_repair import ROOT, control, verify_repair, verify_disjoint_circuits, verify_coordinate_packing
from four_colors import data
from commuting_trades import violations
from central_slice import find_match

RESULTS = ROOT/'results/s5-scalar-repair-2026-10-21'


def verify_cost(certificate):
    source_path = ROOT/'results/s5-split-2026-10-21/four-source-certificate.json'
    source = json.loads(source_path.read_text())
    degrees = source['complex_degrees']+[1]*8
    gate = certificate['gate']
    if (certificate['group_source_certificate_sha256'] != hashlib.sha256(source_path.read_bytes()).hexdigest()
            or certificate['complex_block_degrees'] != degrees
            or certificate['source_dimension'] != sum(d*d for d in degrees)
            or gate['shape'] != [18,18,20] or Fraction(gate['tau']) != Fraction(22499,10000)):
        raise ValueError('wrong source or target cost receipt')
    scale = gate['scale']
    if type(scale) is not int or scale <= 0:
        raise ValueError('positive integer root scale required')
    m, q = 22499, 10000
    upper = gate['source_term_upper_numerators']
    if len(upper) != len(degrees) or any(type(u) is not int or u <= 0 for u in upper):
        raise ValueError('one positive upper root bound per matrix block required')
    for d, u in set(zip(degrees, upper)):
        if pow(u, q) < pow(d, m)*pow(scale, q):
            raise ValueError('source root bound is too small')
    lower = gate['target_lower_numerator']
    if type(lower) is not int or lower <= 0 or pow(lower, 3*q) > pow(18*18*20, m)*pow(scale, 3*q):
        raise ValueError('target root bound is too large')
    margin = lower-sum(upper)
    if (margin <= 0 or gate['source_upper_numerator'] != sum(upper)
            or gate['strict_positive_margin_numerator'] != margin):
        raise ValueError('the strict conditional comparison failed')
    return {'auxiliary_scalars': 8, 'tau': gate['tau'], 'scale': scale,
            'strict_positive_margin_numerator': margin,
            'correction_witness_constructed': False, 'exponent_improvement': False}


def replay():
    certificate = json.loads((RESULTS/'source-cost.json').read_text())
    cost = verify_cost(certificate)
    G, small = control()
    saved = json.loads((RESULTS/'laurent-control.json').read_text())
    if small != saved:
        raise ValueError('changed Laurent correction control')
    verify_repair(G, saved['sets'], saved['potentials'], saved['corrections'])
    item = json.loads((RESULTS/'first-trade-free-packing.json').read_text())
    G, _, receipt = data(item['shape'])
    if item['source'] != receipt or item['group'] != G['name']:
        raise ValueError('changed candidate source')
    packing = verify_disjoint_circuits(G, item['sets'], item['circuits'])
    if packing != item['verification'] or packing['disjoint_circuits'] != 9:
        raise ValueError('wrong finite circuit packing')
    item = json.loads((RESULTS/'first-coordinate-packing.json').read_text())
    G, Q, receipt = data(item['shape'])
    if item['source'] != receipt or item['group'] != G['name']:
        raise ValueError('changed coordinate-packet source')
    if violations(G, item['sets']) or find_match(Q, [[g//4 for g in S] for S in item['sets']]) is not None:
        raise ValueError('the stated stronger control does not survive the earlier cuts')
    coordinate_packet = verify_coordinate_packing(G, item['sets'], item['circuits'], item['coordinate_leg'])
    if coordinate_packet != item['verification'] or coordinate_packet['auxiliary_rank_lower_bound'] != 9:
        raise ValueError('wrong auxiliary-rank packet')
    return {'conditional_cost': cost, 'laurent_control': small['verification'],
            'specific_candidate': packing, 'arbitrary_correction_bound': coordinate_packet,
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = replay()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
