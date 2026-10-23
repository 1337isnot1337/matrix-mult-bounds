"""Exact SL(2,5) central quotient and a finite normalization certificate."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SEVEN = Path(__file__).resolve().parents[1]/'2026-10-20-sl2-seven'
sys.path.insert(0, str(SEVEN/'imported'))
sys.path.insert(0, str(SEVEN))
from group_exact import group
from central_lift import quotient
from source_certificate import exponent_gate


def data():
    G = group(5)
    z = G['matrices'].index((4, 0, 0, 4))
    Q = quotient(G, z)
    counts = {n: sum(len(v) == n for v in Q['fibers'].values()) for n in (1, 2)}
    if counts != {1: 15, 2: 22}:
        raise ArithmeticError('wrong inverse-class fibers')
    path = ROOT/'results/sl2-five-c2-2026-10-20/subgroup-certificate.json'
    product = json.loads(path.read_text())
    H = sorted({g//2 for g in product['members']})
    if (len(H) != 24 or any(G['mul'][g][h] not in H for g in H for h in H)
            or z not in H):
        raise ArithmeticError('incorrect order-24 normalization subgroup')
    projected = sorted({Q['projection'][g] for g in H})
    anchors = [min(q for q in projected if q and Q['inv'][q] == q),
               min(q for q in projected if q and Q['mul'][Q['mul'][q][q]][q] == 0)]
    coverage = []
    for q in projected:
        if not q:
            continue
        found = None
        for g in H:
            for reverse in (False, True):
                r = Q['representatives'][Q['inv'][q] if reverse else q]
                image = Q['projection'][G['mul'][G['mul'][g][r]][G['inv'][g]]]
                if image in anchors:
                    found = {'projected_quotient': q, 'conjugator': g,
                             'reverse_pair': reverse, 'anchor': image}
                    break
            if found:
                break
        if not found:
            raise ArithmeticError('projected anchor orbit not covered')
        coverage.append(found)
    source_path = ROOT/'results/sl2-five-c2-2026-10-20/source-certificate.json'
    certificate = json.loads(source_path.read_text())['first_factor_rational_certificate']
    degrees = certificate['complex_degrees']
    if certificate['order'] != 120 or sum(d*d for d in degrees) != 120:
        raise ArithmeticError('wrong source degree certificate')
    receipt = {'group': G['name'], 'projected_order': len(Q['representatives']),
        'inverse_class_fiber_counts': counts, 'subgroup_order': len(H),
        'subgroup_index': 5, 'subgroup_members': H, 'projected_subgroup': projected,
        'first_pair_anchor_disjunction': anchors, 'anchor_coverage': coverage,
        'complex_degrees': degrees,
        'source_certificate_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
        'conditional_gate': exponent_gate(degrees, shape=(10, 10, 10)),
        'exponent_improvement': False}
    return G, Q, receipt
