"""Exact blockwise modular slice bounds for S5 with central C2 factors.

Acceptance uses only integer and rational arithmetic. The discovery scripts
are not imported. The previous radical certificate retains its provenance.
"""

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
from itertools import permutations
import json
from pathlib import Path
import sys

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
BASELINE = ROOT / 'results/s5-split-2026-10-21/radical-pilot.json'
PRIOR = PACKAGE.parent / '2026-10-21-s5-split'
SCOPE = ('Coordinate/potential degenerations only; arbitrary source powers and '
         'finite rectangular direct sums are covered by the written argument.')
PROOF_STATUS = 'written proof; unreviewed; not formalized'


def bits(value):
    while value:
        bit = value & -value
        yield bit.bit_length() - 1
        value ^= bit


def xor(values):
    result = 0
    for value in values:
        result ^= value
    return result


def basis(rows):
    output = {}
    for value in rows:
        while value:
            pivot = value.bit_length() - 1
            if pivot not in output:
                output[pivot] = value
                break
            value ^= output[pivot]
    return list(output.values())


@lru_cache(None)
def group():
    elements = list(permutations(range(5)))
    lookup = {p: i for i, p in enumerate(elements)}
    table = [[lookup[tuple(p[q[i]] for i in range(5))]
              for q in elements] for p in elements]
    return table


def multiply(left, right):
    table = group()
    return xor(1 << table[g][h] for g in bits(left) for h in bits(right))


def solve_preimage(vectors, target):
    rows = {}
    for i, value in enumerate(vectors):
        label = 1 << i
        while value:
            pivot = value.bit_length() - 1
            if pivot not in rows:
                rows[pivot] = value, label
                break
            row, old = rows[pivot]
            value ^= row
            label ^= old
    result = 0
    while target:
        pivot = target.bit_length() - 1
        if pivot not in rows:
            raise ValueError('requested image is not in the binary span')
        row, label = rows[pivot]
        target ^= row
        result ^= label
    return result


def central_idempotent(previous):
    table = group()
    inverse = [row.index(0) for row in table]
    unseen = set(range(120))
    classes = []
    while unseen:
        g = min(unseen)
        conjugates = {table[table[h][g]][inverse[h]] for h in range(120)}
        classes.append(sum(1 << h for h in conjugates))
        unseen -= conjugates
    first, second = previous['representation_matrices']
    images = [1 | (first[g] << 1) | (second[g] << 17) for g in range(120)]
    class_images = [xor(images[g] for g in bits(v)) for v in classes]
    # Identity on the first four-dimensional module, zero on the others.
    target = sum(1 << (1 + 5*i) for i in range(4))
    coefficients = solve_preimage(class_images, target)
    value = xor(classes[i] for i in bits(coefficients))
    # J^7=0: (x^2-x)^8=0 implies x^8 is idempotent in characteristic two.
    for unused in range(3):
        value = multiply(value, value)
    return value


def block_dimensions(idempotent, previous):
    powers = [[1 << g for g in range(120)]]
    powers += [[int(v, 16) for v in row] for row in previous['power_bases']]
    return [len(basis(multiply(idempotent, v) for v in power))
            for power in powers]


def comparisons(t=Fraction(4, 5), kappa_upper=Fraction(189, 100)):
    if not 0 < t < 1 or kappa_upper**3 <= Fraction(27, 4):
        raise ValueError('invalid rational filtration parameter or root bound')
    layers = [17, 9, 9, 18, 9, 9, 17]
    principal = sum(value*t**i for i, value in enumerate(layers)) / t**2
    source = principal + 16*kappa_upper
    return {
        'principal_parameter': str(t),
        'c2_parameter': '1/2',
        'kappa_cubed': '27/4',
        'kappa_strict_upper': str(kappa_upper),
        'principal_bound': str(principal),
        'central_factor_upper_bounds': [str(source*kappa_upper**r) for r in range(3)],
        'central_two_bound_strictly_below_389': source*kappa_upper**2 < 389,
        'M20_excluded': 20**6 > (source*kappa_upper**2)**3,
        'M19_not_excluded_by_recorded_upper_bound': 19**6 <= (source*kappa_upper**2)**3,
        'split_13_14_14_not_excluded_by_recorded_upper_bound':
            (13*14*14)**2 <= (source*kappa_upper)**3,
    }


def certificate():
    previous = json.loads(BASELINE.read_text())
    e = central_idempotent(previous)
    small = block_dimensions(e, previous)
    large = block_dimensions(1 ^ e, previous)
    return {
        'source': 'F2[S5]',
        'baseline_path': str(BASELINE.relative_to(ROOT)),
        'baseline_sha256': hashlib.sha256(BASELINE.read_bytes()).hexdigest(),
        'central_idempotent_32': hex(e),
        'block_power_dimensions': [large, small],
        'block_layers': [[a-b for a, b in zip(row, row[1:])] for row in [large, small]],
        'comparison': comparisons(),
        'scope': SCOPE,
        'proof_status': PROOF_STATUS,
        'improves_omega': False,
    }


@lru_cache(None)
def verify_baseline(digest):
    if hashlib.sha256(BASELINE.read_bytes()).hexdigest() != digest:
        raise ValueError('baseline changed before independent replay')
    sys.path.insert(0, str(PRIOR))
    spec = importlib.util.spec_from_file_location('s5_block_prior_replay', PRIOR/'verify_radical.py')
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return helper.verify(json.loads(BASELINE.read_text()))


def verify(report):
    if (report.get('source') != 'F2[S5]'
            or report.get('baseline_path') != str(BASELINE.relative_to(ROOT))
            or report.get('baseline_sha256') != hashlib.sha256(BASELINE.read_bytes()).hexdigest()):
        raise ValueError('wrong baseline source or certificate hash')
    previous = json.loads(BASELINE.read_text())
    if (report['comparison'] != comparisons() or report.get('improves_omega') is not False
            or report.get('scope') != SCOPE or report.get('proof_status') != PROOF_STATUS):
        raise ValueError('incorrect rational bound or exponent status')
    e = int(report['central_idempotent_32'], 16)
    if not 0 < e < 1 << 120 or multiply(e, e) != e:
        raise ValueError('invalid binary idempotent')
    for g in range(120):
        if multiply(e, 1 << g) != multiply(1 << g, e):
            raise ValueError('idempotent is not central')
    # Cache only a full replay at this exact content hash.
    receipt = verify_baseline(report['baseline_sha256'])
    dimensions = [block_dimensions(1 ^ e, previous), block_dimensions(e, previous)]
    if dimensions != [[88, 71, 62, 53, 35, 26, 17, 0], [32, 16, 0, 0, 0, 0, 0, 0]]:
        raise ValueError('incorrect central block or power dimensions')
    layers = [[a-b for a, b in zip(row, row[1:])] for row in dimensions]
    if report['block_power_dimensions'] != dimensions or report['block_layers'] != layers:
        raise ValueError('recorded block dimensions do not replay')
    return {
        'baseline_group_products_checked': receipt['group_products_checked'],
        'baseline_representation_products_checked': receipt['representation_products_checked'],
        'centrality_checks': 120,
        'block_power_dimensions': dimensions,
        'M20_coordinate_target_excluded': True,
        'M19_target_constructed': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify', type=Path)
    args = parser.parse_args()
    if args.verify:
        print(json.dumps(verify(json.loads(args.verify.read_text())), indent=2))
    else:
        report = certificate()
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(report, indent=2))
