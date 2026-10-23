"""Reproduce polynomial row reduction and the complete coordinate census.

This is discovery, not acceptance. verify.py reconstructs and checks every
exported polynomial transformation and every compressed modular rank.
"""

import argparse
from collections import deque
from fractions import Fraction
from itertools import combinations
import json
from math import lcm
from pathlib import Path

import verify


def add_shifted(target, source, coefficient, shift):
    for (degree, position), value in source.items():
        key = (degree + shift, position)
        target[key] = target.get(key, 0) + coefficient * value
        if not target[key]:
            del target[key]


def polynomial_basis(family):
    pending = deque((dict((key, Fraction(value)) for key, value in row.items()),
                     {(0, index): Fraction(1)}) for index, row in enumerate(family))
    reducers = {}
    while pending:
        polynomial, transform = pending.popleft()
        while polynomial:
            degree, position = max(polynomial)
            if position not in reducers:
                reducers[position] = polynomial, transform
                break
            earlier, earlier_transform = reducers[position]
            earlier_degree, _ = max(earlier)
            if degree < earlier_degree:
                reducers[position] = polynomial, transform
                polynomial, transform = earlier, earlier_transform
                earlier, earlier_transform = reducers[position]
                degree, position = max(polynomial)
                earlier_degree, _ = max(earlier)
            coefficient = -polynomial[degree, position] / earlier[earlier_degree, position]
            add_shifted(polynomial, earlier, coefficient, degree - earlier_degree)
            add_shifted(transform, earlier_transform, coefficient, degree - earlier_degree)
        else:
            raise ValueError('a source direction vanished during polynomial reduction')
    result = []
    for position, (polynomial, transform) in sorted(reducers.items()):
        denominator = lcm(*(value.denominator for value in
                            list(polynomial.values()) + list(transform.values())))
        degree = max(polynomial)[0]
        leading = [[key, int(value * denominator)] for (power, key), value in
                   sorted(polynomial.items()) if power == degree]
        result.append({
            'degree': degree,
            'pivot': position,
            'leading': leading,
            'transform': [[power, index, int(value * denominator)]
                          for (power, index), value in sorted(transform.items())],
        })
    return result


def discover():
    basis, nilpotent = verify.build_source()
    rows = polynomial_basis(verify.conjugated_source(basis, nilpotent))
    leading = [dict(row['leading']) for row in rows]
    records = []
    for first, second in combinations(range(verify.SIZE), 2):
        holes = {first, second}
        projected = ({key: value for key, value in matrix.items()
                      if key // verify.SIZE not in holes and key % verify.SIZE not in holes}
                     for matrix in leading)
        records.append([first, second, verify.modular_rank(projected)])
    return {
        'schema': 'a4-conjugation-limit-v1',
        'size': verify.SIZE,
        'source_order': 'k,i,s',
        'nilpotent_source_index': 0,
        'scalar_coordinates': list(range(100, 112)),
        'basis': rows,
        'census_prime': verify.PRIME,
        'principal_compressions': records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=verify.ROOT / 'results/local/conjugation-limit/certificate.json')
    arguments = parser.parse_args()
    certificate = discover()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(certificate, separators=(',', ':')) + '\n')
    print(arguments.output)


if __name__ == '__main__':
    main()
