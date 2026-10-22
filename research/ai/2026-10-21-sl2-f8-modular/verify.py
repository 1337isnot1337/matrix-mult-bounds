"""Independent binary replay of the modular SL2(F8) source certificate.

The verifier reads witnesses; it does not invoke module or power discovery.
It checks every representation product and every bit-permutation column.
"""

import argparse
from collections import deque
from fractions import Fraction
import json
from pathlib import Path
import sys

PACKAGE = Path(__file__).resolve().parent
RESULTS = PACKAGE.parents[2]/'results/sl2-f8-modular-2026-10-21'
sys.path.insert(0, str(PACKAGE.parent/'2026-10-21-semisimple-koszul'))
from sl2_f8_source import group
from bit_permutations import route, apply


def bits(value):
    while value:
        bit = value & -value
        yield bit.bit_length()-1
        value ^= bit


def xor(values):
    result = 0
    for value in values:
        result ^= value
    return result


def insert(value, span):
    while value:
        pivot = value.bit_length()-1
        if pivot not in span:
            span[pivot] = value
            return value
        value ^= span[pivot]
    return 0


def reduce(value, span):
    while value:
        pivot = value.bit_length()-1
        if pivot not in span:
            return value
        value ^= span[pivot]
    return 0


def binary_basis(values):
    span = {}
    for value in values:
        insert(value, span)
    return span


def field_product(a, b):
    # Carryless polynomial multiplication, then reduction modulo t^3+t+1.
    value = xor(a << i for i in bits(b))
    for i in range(4, 2, -1):
        if value >> i & 1:
            value ^= 0b1011 << (i-3)
    return value


FIELD = [[field_product(a, b) for b in range(8)] for a in range(8)]


def matrix_product(A, B, n):
    return [xor(FIELD[A[row+n*k]][B[k+n*column]] for k in range(n))
            for column in range(n) for row in range(n)]


def binary_matrix_product(A, B):
    return sum(xor((A >> (8*k)) & 255 for k in bits((B >> (8*j)) & 255)) << (8*j)
               for j in range(8))


def decode_words(rows):
    vectors = [[int(value, 16) for value in row] for row in rows]
    if any(type(v) is not int or not 0 < v < 1 << 504 for row in vectors for v in row):
        raise ValueError('invalid binary group-algebra coefficient vector')
    return vectors


def verify(modules, generators, central):
    G = group()
    table = G['mul']
    if modules.get('group') != 'SL(2,F8)':
        raise ValueError('incorrect source group')
    first, second, last = (modules[k] for k in ['natural', 'tensor', 'steinberg'])
    for matrices, n in [(first, 2), (second, 4)]:
        if (len(matrices) != 504 or any(len(A) != n*n for A in matrices)
                or any(type(x) is not int or not 0 <= x < 8 for A in matrices for x in A)):
            raise ValueError('invalid F8 representation matrix')
        for g in range(504):
            for h in range(504):
                if matrix_product(matrices[g], matrices[h], n) != matrices[table[g][h]]:
                    raise ValueError('F8 representation product failed')
    if len(last) != 504 or any(type(A) is not int or not 0 <= A < 1 << 64 for A in last):
        raise ValueError('invalid binary representation matrix')
    for g in range(504):
        for h in range(504):
            if binary_matrix_product(last[g], last[h]) != last[table[g][h]]:
                raise ValueError('binary representation product failed')
    if (modules['field_representation_products_checked'] != 2*504**2
            or modules['binary_representation_products_checked'] != 504**2):
        raise ValueError('incorrect representation coverage')
    images = [1 | (sum(v << (3*i) for i, v in enumerate(N)) << 1)
              | (sum(v << (3*i) for i, v in enumerate(A)) << 13) | (S << 61)
              for N, A, S in zip(first, second, last)]
    if len(binary_basis(images)) != 125 or modules['image_dimension'] != 125:
        raise ValueError('image does not fill the semisimple product of dimension125')
    powers = decode_words(modules['powers'])
    expected = [504, 379, 319, 256, 184, 121, 61, 0]
    if [504]+list(map(len, powers)) != expected or modules['power_dimensions'] != expected:
        raise ValueError('incorrect power dimensions')
    for row in powers:
        if len(binary_basis(row)) != len(row):
            raise ValueError('dependent ideal-power basis')
    if any(xor(images[g] for g in bits(v)) for v in powers[0]):
        raise ValueError('first basis is not the representation kernel')

    networks = [route(row+list(range(504, 512))) for row in table]
    for g in range(504):
        for h in range(504):
            if apply(1 << h, networks[g]) != 1 << table[g][h]:
                raise ValueError('bit action disagrees with direct group multiplication')

    def multiply(a, b):
        return xor(apply(b, networks[g]) for g in bits(a))

    group_generators = generators['group_generators']
    if (not group_generators
            or any(type(g) is not int or not 0 <= g < 504 for g in group_generators)):
        raise ValueError('invalid group generators')
    seen, queue = {0}, deque([0])
    while queue:
        h = queue.popleft()
        for g in group_generators:
            k = table[g][h]
            if k not in seen:
                seen.add(k)
                queue.append(k)
    if len(seen) != 504:
        raise ValueError('group generators do not generate the full source')

    def left_closure(values):
        span, queue = {}, deque()
        for v in values:
            added = insert(v, span)
            if added:
                queue.append(added)
        while queue:
            value = queue.popleft()
            for g in group_generators:
                added = insert(apply(value, networks[g]), span)
                if added:
                    queue.append(added)
        return span

    left = decode_words([generators['radical_left_generators']])[0]
    kernel_span = binary_basis(powers[0])
    if any(reduce(v, kernel_span) for v in left) or len(left_closure(left)) != 379:
        raise ValueError('proposed left generators do not generate the kernel')
    products_checked = 0
    for index in range(1, len(powers)):
        span = left_closure(multiply(l, v) for l in left for v in powers[index-1])
        products_checked += len(left)*len(powers[index-1])
        if len(span) != len(powers[index]) or any(reduce(v, span) for v in powers[index]):
            raise ValueError('next power is not exactly the left-generated product span')
    if generators['dimensions'] != expected:
        raise ValueError('inconsistent power certificate')

    e = int(central['central_steinberg_idempotent'], 16)
    if not 0 < e < 1 << 504 or multiply(e, e) != e:
        raise ValueError('invalid central idempotent')
    right_columns = [apply(e, networks[g]) for g in range(504)]
    if any(v != multiply(e, 1 << g) for g, v in enumerate(right_columns)):
        raise ValueError('idempotent is not central')
    if len(binary_basis(right_columns)) != 64 or central['ideal_dimension'] != 64:
        raise ValueError('incorrect Steinberg ideal dimension')
    target_image = sum(1 << (61+9*i) for i in range(8))
    if xor(images[g] for g in bits(e)) != target_image:
        raise ValueError('wrong simple-factor images of the central idempotent')
    layers = [61, 60, 63, 72, 63, 60, 61]
    t = Fraction(3, 4)
    bound = 64 + sum(c*t**i for i, c in enumerate(layers))/t**2
    lower = central['packet_score_lower_certificate']
    if (central['principal_layers'] != layers or central['parameter'] != str(t)
            or central['source_bound'] != str(bound) or central['below450'] is not True
            or not bound < 450 or central['packet_lower_score'] != 493
            or lower != {'rational_term': 74, 'cube': 74**3, 'squared_volume': 648**2}
            or not 74**3 < 648**2 or not 6*74+49 > bound
            or central['field_scope'] != 'Coordinate/potential constructions, not arbitrary complex maps.'):
        raise ValueError('incorrect exact bound or mathematical scope')
    return {
        'representation_products_checked': 3*504**2,
        'group_action_columns_checked': 504**2,
        'image_dimension': 125,
        'radical_power_dimensions': expected,
        'radical_left_generators': len(left),
        'power_products_checked': products_checked,
        'semisimple_block_dimension': 64,
        'principal_block_dimension': 440,
        'source_strict_upper_450': True,
        'six_packets_plus_M7_coordinate_excluded': True,
        'arbitrary_complex_maps_excluded': False,
        'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--results', type=Path, default=RESULTS)
    args = parser.parse_args()
    files = ['modules-powers.json', 'left-generators.json', 'central.json']
    values = [json.loads((args.results/name).read_text()) for name in files]
    print(json.dumps(verify(*values), indent=2))
