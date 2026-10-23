"""Accept the complete polynomial source identity and prescribed first jet.

Reuse only the preceding exact parser, sparse polynomial arithmetic and
literal-source contraction. No constructor or gauge formula is imported.
"""
import argparse
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
HELPERS = ROOT / 'research/ai/2026-10-23-conic-polynomial-curve/verify.py'
spec = importlib.util.spec_from_file_location('fixed_first_source_arithmetic', HELPERS)
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)


def verify(record):
    if record.get('schema') != 'conic-fixed-first-curve-v1' or record.get('base') != 'c=-d^3':
        raise ValueError('wrong fixed-first curve schema or base')
    if len(record['B']) != 4 or len(record['C']) != 4:
        raise ValueError('wrong complete polynomial degrees')
    bs, cs = [[f.decode(matrix) for matrix in record[key]] for key in ('B', 'C')]
    if not bs[-1] or not cs[-1]:
        raise ValueError('missing highest polynomial coefficient')
    prior_bytes = f.PRIOR.read_bytes()
    if hashlib.sha256(prior_bytes).hexdigest() != f.PRIOR_SHA256:
        raise ValueError('credited predecessor bytes changed')
    prior = json.loads(prior_bytes)
    for side, maps in (('B', bs), ('C', cs)):
        for order in (0, 1):
            if maps[order] != f.decode(prior[side][order]):
                raise ValueError(f'changed credited full coefficient {side}{order}')
    if (cs[1].get((0, 102), f.ZERO) != f.expression('-1')
            or cs[1].get((0, 95), f.ZERO) != -f.SYMBOLS['d']):
        raise ValueError('missing universal normal anchors')
    terms = f.source_terms()
    fs = [f.add(*(f.contract(bs[i], cs[k-i], terms)
                  for i in range(4) if 0 <= k-i < 4)) for k in range(7)]
    for order, matrix in enumerate(fs):
        if any(row in f.OUTSIDE for row, col in matrix):
            raise ValueError(f'nonzero full-source kernel coefficient at order {order}')
    boundary_b = [28*p+7*j+z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    boundary_c = [28*j+7*p+z for p, j, z in product((0, 3), (0, 3), (1, 2, 4, 5))]
    determinants = [f.determinant(bs[0], list(range(14)), boundary_b[2:]),
                    f.determinant(cs[0], list(range(14)), boundary_c[2:]),
                    f.determinant(fs[0], f.FIRST, f.PIVOTS)]
    if determinants != [1, 1, -1]:
        raise ValueError('wrong constant leading minors')
    return {
        'claim_id': 'AI-CONIC-FIXED-FIRST-CURVE-001',
        'coefficient_ring': 'Q[a,b,d]',
        'scope': 'Every complex a,b,d, with c=-d^3',
        'source_terms': len(terms),
        'map_degrees_in_t': [3, 3],
        'complete_product_orders_checked': list(range(7)),
        'source_kernel_coordinates_per_order': 100*196,
        'fixed_source_kernel_dimension': 100,
        'leading_minor_determinants': list(map(str, determinants)),
        'leading_map_ranks': [14, 14],
        'formal_first_source_rank': 12,
        'coefficient_entry_counts': {'B': list(map(len, bs)), 'C': list(map(len, cs))},
        'normal_class': '[1:d]',
        'full_first_jet_preserved': True,
        'prescribed_second_jet_preserved': False,
        'all_order_lift_established': True,
        'matrix_target_constructed': False,
        'exponent_improvement': False,
        'independent_mathematical_review': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.witness.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
