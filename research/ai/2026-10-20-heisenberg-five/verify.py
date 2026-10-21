"""Integer-only source, normalization, and complete finite two-coset replay."""
import argparse
from itertools import combinations_with_replacement
import json
from pathlib import Path
import sys

from source import group, two_coset_sets, quotients, source_gate, RESEARCH
sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven'))
from verify_projected_reports import verify_farkas_record


def source_characters(G):
    p = G['p']
    descriptors = [('linear', r, s) for r in range(p) for s in range(p)]
    descriptors += [('shift', k) for k in range(1, p)]
    characters = []
    for label in descriptors:
        if label[0] == 'linear':
            characters.append([(1, (label[1]*a+label[2]*b) % p)
                               for a, b, c in G['matrices']])
        else:
            characters.append([(p, label[1]*c % p) if a == b == 0 else (0, 0)
                               for a, b, c in G['matrices']])
    checked = 0
    for i, first in enumerate(characters):
        for j, second in enumerate(characters):
            coefficients = [0]*p
            for (m, e), (n, f) in zip(first, second):
                coefficients[(e-f) % p] += m*n
            # Reduction by Phi_p=1+X+...+X^(p-1), with no complex numerics.
            reduced = [c-coefficients[-1] for c in coefficients[:-1]]
            expected = [p**3 if i == j else 0]+[0]*(p-2)
            if reduced != expected:
                raise ValueError('character inner products are not orthonormal')
            checked += 1
    products = 0
    for k in range(1, p):
        for i, (a, b, c) in enumerate(G['matrices']):
            for j, (x, y, z) in enumerate(G['matrices']):
                aa, bb, cc = G['matrices'][G['mul'][i][j]]
                for t in range(p):
                    if (aa != (a+x) % p or
                            k*(c+b*t+z+y*(t+a)-cc-bb*t) % p):
                        raise ValueError('shift/phase group representation law failed')
                    products += 1
    return {'characters': len(descriptors), 'exact_inner_products': checked,
            'shift_phase_products_at_basis_positions': products,
            'degree_squares_sum': p*p+(p-1)*p*p,
            'cyclotomic_reduction': [1]*p, 'floating_point_used': False}


def automorphism_normalizations(G):
    p, M, inv = G['p'], G['mul'], G['inv']
    identity = 0
    fixed = {i for i, (a, b, c) in enumerate(G['matrices']) if b in (0, 1) and c == 0}
    representatives = {}
    for l, (a, b, c) in enumerate(G['matrices']):
        if a == b == 0:
            continue
        powers = [identity]
        for _ in range(p-1):
            powers.append(M[powers[-1]][l])
        representatives.setdefault(tuple(sorted(powers)), l)
    images, checks = set(), 0
    for L, l in sorted(representatives.items()):
        for coset in sorted({tuple(sorted(M[g][h] for h in L)) for g in range(p**3)}):
            g = min(coset)
            if g in L or {M[M[g][h]][inv[g]] for h in L} == set(L):
                continue
            z = M[M[M[l][g]][inv[l]]][inv[g]]
            powers = []
            for v in (l, g, z):
                row = [0]
                for _ in range(p-1):
                    row.append(M[row[-1]][v])
                powers.append(row)
            phi = [M[M[powers[1][b]][powers[0][a]]][powers[2][c]]
                   for a, b, c in G['matrices']]
            if len(set(phi)) != p**3 or {phi[h] for h in fixed} != set(L) | set(coset):
                raise ValueError('normalization map is not the claimed bijection')
            for x in range(p**3):
                for y in range(p**3):
                    if phi[M[x][y]] != M[phi[x]][phi[y]]:
                        raise ValueError('normalization map is not an automorphism')
                    checks += 1
            images.add(tuple(sorted(phi[h] for h in fixed)))
    expected, _ = two_coset_sets(G)
    if images != set(expected):
        raise ValueError('automorphisms do not cover the finite two-coset class')
    return {'first_set_images': len(images), 'group_product_checks': checks}


def verify_cut(G, record):
    points = set()
    for s, t, tt, u, uu, ss in record['relation_vertices']:
        points.update(((0, record['sets'][0][s]), (0, record['sets'][0][ss]),
                       (1, record['sets'][1][t]), (1, record['sets'][1][tt]),
                       (2, record['sets'][2][u]), (2, record['sets'][2][uu])))
    return verify_farkas_record(G, dict(record, blocked_lift_points=sorted(points)))


def replay(path):
    report = json.loads(path.read_text())
    G = group()
    if (report['group'] != G['name'] or report['shape'] != [10]*3 or report['witness']
            or report['status'] != 'finite-fixed-first-class-exhausted'):
        raise ValueError('wrong source, target or finite experiment status')
    if report['source'] != source_gate():
        raise ValueError('source gate changed')
    first = tuple(i for i, (a, b, c) in enumerate(G['matrices']) if b in (0, 1) and c == 0)
    candidates, subgroups = two_coset_sets(G)
    q0 = quotients(G, first)
    eligible = [(S, quotients(G, S)) for S in candidates if not q0 & quotients(G, S)]
    expected = {(first, T, U) for (T, qt), (U, qu) in combinations_with_replacement(eligible, 2)
                if not qt & qu}
    seen = set()
    for line in path.with_suffix('.cuts.jsonl').read_text().splitlines():
        record = json.loads(line)
        key = tuple(map(tuple, record['sets']))
        if key not in expected or key in seen:
            raise ValueError('unexpected or repeated finite candidate')
        verify_cut(G, record)
        seen.add(key)
    if (seen != expected or report['pair_injective_triples'] != len(seen)
            or report['exact_farkas_cuts'] != len(seen)
            or report['two_coset_sets'] != len(candidates)
            or report['noncentral_cyclic_subgroups'] != subgroups
            or report['eligible_other_sets'] != len(eligible)
            or report['pairs_checked'] != len(eligible)*(len(eligible)+1)//2):
        raise ValueError('incomplete finite coverage')
    return {'source': source_characters(G), 'normalization': automorphism_normalizations(G),
            'finite_triples_replayed': len(seen), 'finite_class_complete': True,
            'scope': 'The stated two-left-coset family only; arbitrary colorings and '
                     'general tensor degenerations are not excluded.',
            'exponent_improvement': False}


def replay_progressions(path):
    report = json.loads(path.read_text())
    p = int(report['group'].removeprefix('Heisenberg(').removesuffix(')'))
    G = group(p)
    if report['source'] != source_gate(p, tuple(report['shape'])):
        raise ValueError('wrong progression source gate')
    short = long = 0
    for line in path.with_suffix('.cuts.jsonl').read_text().splitlines():
        record = json.loads(line)
        if list(map(len, record['sets'])) != report['shape']:
            raise ValueError('wrong progression candidate shape')
        verify_cut(G, record)
        if len(record['weights']) == 2:
            short += 1
        else:
            long += 1
    if (short != report['exact_two_trade_cuts'] or long != report['exact_long_farkas_cuts']
            or short+long+len(report['unresolved'])+int(bool(report['witness'])) !=
            report['pair_injective_triples']):
        raise ValueError('progression coverage differs from the report')
    if report['witness']:
        sys.path.insert(0, str(RESEARCH/'2026-10-20-group-potentials'))
        from stream_potentials import verify_stream_witness
        witness = report['witness']
        verify_stream_witness(G, witness['sets'], witness['potentials'])
    return {'short_circuits_checked': short, 'long_circuits_checked': long,
            'complete_source_exclusion': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
