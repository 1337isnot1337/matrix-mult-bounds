"""Complete affine-coordinate classification of 5x5 binary matrices with margins two."""
from collections import Counter
from itertools import combinations, product
import json


def derive():
    configurations, histogram = set(), Counter()
    for rows in product(list(combinations(range(5), 2)), repeat=5):
        if any(sum(c in row for row in rows) != 2 for c in range(5)):
            continue
        S = tuple(5*r+c for r, row in enumerate(rows) for c in row)
        configurations.add(S)
        directions = [(1, k) for k in range(5)]+[(0, 1)]
        balanced = sum(all(sum((a*(q % 5)-b*(q//5)) % 5 == k for q in S) == 2
                           for k in range(5)) for a, b in directions)
        histogram[balanced] += 1
    remaining, orbits = set(configurations), []
    while remaining:
        S = min(remaining)
        orbit = set()
        for a, c in product(range(1, 5), repeat=2):
            for b, d in product(range(5), repeat=2):
                R = tuple(sorted(5*((a*(q//5)+b) % 5)+(c*(q % 5)+d) % 5 for q in S))
                orbit.add(R)
                orbit.add(tuple(sorted(5*(q % 5)+q//5 for q in R)))
        if not orbit <= remaining:
            raise ArithmeticError('affine coordinate orbits overlap or leave the class')
        orbits.append({'representative': min(orbit), 'size': len(orbit)})
        remaining -= orbit
    return {'row_and_column_sum_two_sets': len(configurations),
            'balanced_direction_histogram': dict(histogram), 'affine_coordinate_orbits': orbits,
            'scope': 'Finite projected-support classification only; central colors and potentials are free.'}


if __name__ == '__main__':
    print(json.dumps(derive(), indent=2))
