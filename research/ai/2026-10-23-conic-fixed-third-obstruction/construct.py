"""Export the explicit dual functional and its two exact linear branches."""
import argparse
import hashlib
import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[3]
PRESCRIBED = 'results/conic-third-jets-2026-10-23/mixed-family.json'
PRESCRIBED_SHA256 = '0571cd47916d19c60a0f9493a6ddccaecb8053aea8a139137c05b3def9df1d5e'
A, B, D = s.symbols('a b d')
SYMBOLS = {'a': A, 'b': B, 'd': D}


def construct():
    payload = (ROOT / PRESCRIBED).read_bytes()
    if hashlib.sha256(payload).hexdigest() != PRESCRIBED_SHA256:
        raise ValueError('changed prescribed third-jet source')
    prescribed = json.loads(payload)
    # P(M)=d^3(M15-M11-M51)+M17-M13-M53, Q=P+d^3 M55+M57.
    p = {(1, 1): -D**3, (1, 3): -1, (1, 5): D**3,
         (1, 7): 1, (5, 1): -D**3, (5, 3): -1}
    q = dict(p)
    q.update({(5, 5): D**3, (5, 7): 1})
    weights = []
    for source, scale, form in ((36, D**4, p), (37, -D**3, p),
                                (39, D, q), (40, -1, q)):
        for (br, cr), coefficient in sorted(form.items()):
            weights.append([source, br, cr, str(s.expand(scale*coefficient))])
    branches = []
    for label, substitution in (('a=-d^3', {A: -D**3}),
                                ('b=d^3', {B: D**3})):
        maps = {}
        for side in ('B', 'C'):
            maps[side] = []
            for order in range(2):
                entries = []
                for i, j, text in prescribed[side][order]['entries']:
                    value = s.expand(s.sympify(text, locals=SYMBOLS).subs(substitution))
                    if value:
                        entries.append([i, j, str(value)])
                maps[side].append({'shape': [14, 112], 'entries': entries})
        branches.append({'component': label, **maps,
                         'kernel': 'fixed', 'complete_map_degrees': [1, 1]})
    return {
        'schema': 'conic-prescribed-third-obstruction-v1',
        'claim_id': 'AI-CONIC-FIXED-THIRD-OBSTRUCTION-001',
        'chart': 'd!=0; c=-d^3',
        'coefficient_ring': 'Q[a,b,d,d^-1]',
        'prescribed_source': PRESCRIBED,
        'prescribed_sha256': PRESCRIBED_SHA256,
        'functional_coordinates': '[source coordinate, B output row, C output row, coefficient]; zero-based',
        'functional': weights,
        'fourth_residual': '-d*(a+d**3)**4*(b-d**3)**3/3',
        'linear_branches': branches,
        'extension_criterion': '(a+d^3)*(b-d^3)=0',
        'independent_mathematical_review': False,
        'matrix_target_constructed': False,
        'exponent_improvement': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(construct(), indent=2)+'\n')
