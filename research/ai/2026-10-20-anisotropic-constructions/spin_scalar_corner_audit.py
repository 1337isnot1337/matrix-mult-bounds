"""Second-agent exact replay of the exported claim125 maps.

This checker imports no discovery or acceptance helper. It reconstructs the
six-index source and the residue lift directly from their stated formulas.
It is an audit within the same generating session, not external review.
"""

from collections import Counter, defaultdict
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'


def run():
    certificate = json.loads((RESULTS / 'spin-scalar-corner-certificate.json').read_text())
    inverse = [defaultdict(list) for _ in range(3)]
    for leg, rows in enumerate(certificate['maps']):
        for row, entries in enumerate(rows):
            assert len(entries) == 1 and entries[0][1] == 1
            flat = entries[0][0]
            outer, tail = divmod(flat, 120)
            middle, inner = divmod(tail, 8)
            inverse[leg][(outer, middle, inner)].append(row)
    lift_inverse = [dict() for _ in range(3)]
    for i, k, s in product(range(3), repeat=3):
        lift_inverse[0][(3 * i, k, 3 * s)] = (3 * i + k) * 3 + s
    for e, f in product(range(3), repeat=2):
        channel = 3 * e + f
        for p, ell, j in product(range(2), range(4), range(2)):
            lift_inverse[1][(p, e + 3 * ell, f + 3 * j)] = 16 * channel + (4 * p + ell) * 2 + j
        for r, h, q in product(range(2), range(4), range(2)):
            lift_inverse[2][(e + 3 * r, f + 3 * h, q)] = 16 * channel + (4 * r + h) * 2 + q
    tensor = Counter()
    lifted = Counter()
    response = [defaultdict(Counter) for _ in range(3)]
    mixed = Counter()
    source_count = 0
    for i, p, q, r, j, s in product(range(8), repeat=6):
        source_count += 1
        point = ((i, p + q, s), (p, r + s, j), (r, i + j, q))
        rows = [inverse[leg].get(point[leg], ()) for leg in range(3)]
        for target in product(*rows):
            tensor[target] += 1
        core_membership = (p + q <= 2, p <= 1 and j <= 5, r <= 5 and q <= 1)
        for free in range(3):
            fixed = tuple(leg for leg in range(3) if leg != free)
            for pair in product(*(rows[leg] for leg in fixed)):
                response[free][point[free]][pair] += 1
            for core in fixed:
                corner = 3 - free - core
                if core_membership[core]:
                    mixed[(free, core, corner)] += len(rows[corner])
        if all(point[leg] in lift_inverse[leg] for leg in range(3)):
            lifted[tuple(lift_inverse[leg][point[leg]] for leg in range(3))] += 1
    assert tensor == {(0, channel, channel): 1 for channel in range(9)}
    assert not any(mixed.values())
    ranks = []
    for leg in response:
        occupied = set()
        for column in leg.values():
            assert all(value == 1 for value in column.values())
            assert occupied.isdisjoint(column)
            occupied.update(column)
        ranks.append(len(leg))
    assert ranks == [15, 9, 9]
    expected = Counter()
    for channel in range(9):
        for i, s in product(range(3), repeat=2):
            for p, q, r, j in product(range(2), repeat=4):
                expected[((3 * i + p + q) * 3 + s,
                          16 * channel + (4 * p + r + s) * 2 + j,
                          16 * channel + (4 * r + i + j) * 2 + q)] += 1
    assert lifted == expected and all(value == 1 for value in lifted.values())
    return {
        'claim_id': 'AI-SPIN-SCALAR-CORNER-125',
        'review_scope': 'Checked by a second agent in this generating session; no external independent review',
        'source_terms_checked': source_count,
        'exported_map_coefficients_replayed': True,
        'target_coefficients_checked': 81,
        'nonzero_target_coefficients': len(tensor),
        'full_response_ranks_by_disjoint_unit_supports': ranks,
        'six_full_mixed_response_maps_zero': True,
        'mixed_response_coefficients_checked': 6773760,
        'residue_lift_coefficients_checked': 27 * 144 * 144,
        'nonzero_lift_coefficients': len(lifted),
        'shared_verification_helpers_imported': False,
        'conditional_reduced_maps_constructed': False,
        'new_exponent_established': False,
    }


if __name__ == '__main__':
    report = run()
    (RESULTS / 'spin-scalar-corner-audit.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))
