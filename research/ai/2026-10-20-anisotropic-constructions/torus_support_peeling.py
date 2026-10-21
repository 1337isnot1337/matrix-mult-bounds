"""Exact Newton-support peeling for ordinary graded tensor restrictions.

Discovery uses convex hulls. Certificate verification does not: it checks
integer separating half-planes against every admissible source coordinate,
after independently recomputing all three restricted coordinate-slice ranks.
Only the Python standard library is required.
"""

import argparse
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-support-peeling-a88-m27-m7.json'


@lru_cache(maxsize=None)
def source_data(a, b):
    if type(a) is not int or type(b) is not int or a < 1 or b < 1:
        raise ValueError('Source dimensions must be positive integers')
    m = a + b - 1
    points = tuple(product(range(a), range(m), range(b)))

    def index(i, k, s):
        return (i * m + k) * b + s

    terms = tuple((index(i, p + q, s), index(p, r + s, j), index(r, i + j, q))
                  for i, p, r in product(range(a), repeat=3)
                  for j, q, s in product(range(b), repeat=3))
    groups = defaultdict(list)
    for coordinate, (i, k, s) in enumerate(points):
        groups[i + s - k].append(coordinate)
    return points, terms, {weight: tuple(group) for weight, group in sorted(groups.items())}


def validate_partial_permutations(points, terms):
    """Every two source legs determine a term, so fixed slices are matchings."""
    n = len(points)
    counts = []
    for leg in range(3):
        pairs = {term[leg] * n + term[(leg + 1) % 3] for term in terms}
        if len(pairs) != len(terms):
            raise ArithmeticError('A coordinate slice is not a partial permutation matrix')
        counts.append(len(pairs))
    return counts


def coordinate_ranks(alive, terms, n):
    """Ranks on each leg of the tensor restricted to the common coordinate K."""
    active = [False] * n
    for coordinate in alive:
        active[coordinate] = True
    ranks = [[0] * n for _ in range(3)]
    retained_terms = 0
    for x, y, z in terms:
        if active[x] and active[y] and active[z]:
            ranks[0][x] += 1
            ranks[1][y] += 1
            ranks[2][z] += 1
            retained_terms += 1
    if ranks[0] != ranks[1] or ranks[0] != ranks[2]:
        raise ArithmeticError('The common coordinate restriction lost cyclic rank symmetry')
    return ranks[0], retained_terms


def cross(origin, left, right):
    return ((left[0] - origin[0]) * (right[1] - origin[1])
            - (left[1] - origin[1]) * (right[0] - origin[0]))


def convex_hull(points):
    """Counterclockwise vertices, with collinear interior points removed."""
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def inside_hull(point, hull):
    if not hull:
        return False
    if len(hull) == 1:
        return point == hull[0]
    if len(hull) == 2:
        return cross(hull[0], hull[1], point) == 0 and all(
            min(hull[0][j], hull[1][j]) <= point[j] <= max(hull[0][j], hull[1][j])
            for j in range(2))
    return all(cross(hull[j], hull[(j + 1) % len(hull)], point) >= 0
               for j in range(len(hull)))


def separating_line(point, hull):
    """Return integers A,B,C with A*x+B*y<=C on hull and >C at point."""
    if inside_hull(point, hull):
        raise ValueError('An interior point has no strict separating line')
    if not hull:
        return None
    if len(hull) == 1:
        origin = hull[0]
        aa, bb = point[0] - origin[0], point[1] - origin[1]
        return [aa, bb, aa * origin[0] + bb * origin[1]]
    edges = list(zip(hull, hull[1:] + hull[:1]))
    for origin, end in edges:
        aa, bb = end[1] - origin[1], origin[0] - end[0]
        cc = aa * origin[0] + bb * origin[1]
        if aa * point[0] + bb * point[1] > cc and all(
                aa * vertex[0] + bb * vertex[1] <= cc for vertex in hull):
            return [aa, bb, cc]
    if len(hull) == 2:
        origin, end = hull
        aa, bb = end[0] - origin[0], end[1] - origin[1]
        for sign in (1, -1):
            normal = (sign * aa, sign * bb)
            cc = max(normal[0] * vertex[0] + normal[1] * vertex[1] for vertex in hull)
            if normal[0] * point[0] + normal[1] * point[1] > cc:
                return [normal[0], normal[1], cc]
    raise ArithmeticError('Discovery could not separate an exterior point')


def validate_parameters(target_dimension, maximum_basis_slice_rank, n):
    if type(target_dimension) is not int or not 0 < target_dimension <= n:
        raise ValueError('Target leg dimension must be between one and the source dimension')
    if type(maximum_basis_slice_rank) is not int or maximum_basis_slice_rank < 1:
        raise ValueError('The basis-slice rank bound must be a positive integer')


def discover(a=8, b=8, target_dimension=778, maximum_basis_slice_rank=27):
    points, terms, groups = source_data(a, b)
    n = len(points)
    validate_parameters(target_dimension, maximum_basis_slice_rank, n)
    alive = set(range(n))
    rounds = []
    while len(alive) >= target_dimension:
        ranks, retained_terms = coordinate_ranks(alive, terms, n)
        limit = maximum_basis_slice_rank + 2 * (len(alive) - target_dimension)
        removals = []
        good_counts = []
        for weight, group in groups.items():
            good = [coordinate for coordinate in group
                    if coordinate in alive and ranks[coordinate] <= limit]
            hull = convex_hull((points[c][0], points[c][2]) for c in good)
            good_counts.append([weight, len(good)])
            for coordinate in group:
                if coordinate not in alive:
                    continue
                point = (points[coordinate][0], points[coordinate][2])
                if not inside_hull(point, hull):
                    removals.append({'coordinate': coordinate,
                                     'source_point': list(points[coordinate]),
                                     'weight': weight,
                                     'separating_line': separating_line(point, hull)})
        next_alive = alive - {record['coordinate'] for record in removals}
        rounds.append({
            'round': len(rounds),
            'input_dimension': len(alive),
            'rank_limit': limit,
            'retained_source_terms': retained_terms,
            'coordinate_slice_ranks': [[c, ranks[c]] for c in sorted(alive)],
            'good_coordinate_counts_by_weight': good_counts,
            'removed_coordinates': removals,
            'output_dimension': len(next_alive),
            'output_weight_dimensions': [[w, sum(c in next_alive for c in group)]
                                         for w, group in groups.items()],
        })
        if next_alive == alive:
            break
        alive = next_alive
    data = {
        'schema': 'ordinary-graded-newton-support-peeling-v1',
        'source_parameters': [a, b],
        'source_coordinate_order': 'common F(i,k,s), index=(i*(a+b-1)+k)*b+s',
        'source_dimension_each_leg': n,
        'source_terms': len(terms),
        'target_dimension_each_leg': target_dimension,
        'maximum_homogeneous_basis_slice_rank': maximum_basis_slice_rank,
        'target_hypothesis': 'Each leg has a homogeneous basis whose slices have rank at most the displayed bound.',
        'rounds': rounds,
        'remaining_coordinates': sorted(alive),
        'remaining_dimension': len(alive),
        'ordinary_graded_restriction_excluded': len(alive) < target_dimension,
        'ungraded_restrictions_excluded': False,
        'arbitrary_singular_limits_excluded': False,
        'improves_omega': False,
    }
    verify_certificate(data)
    return data


def verify_certificate(data):
    """Check an integer certificate without computing any convex hull.

    Every deletion is justified separately by a displayed separating line.
    It is unnecessary to certify that discovery deleted every possible point.
    """
    if data.get('schema') != 'ordinary-graded-newton-support-peeling-v1':
        raise ValueError('Unknown support-peeling certificate schema')
    a, b = data['source_parameters']
    points, terms, groups = source_data(a, b)
    n = len(points)
    dimension = data['target_dimension_each_leg']
    basis_rank = data['maximum_homogeneous_basis_slice_rank']
    validate_parameters(dimension, basis_rank, n)
    if data['source_dimension_each_leg'] != n or data['source_terms'] != len(terms):
        raise ArithmeticError('The recorded source dimensions are incorrect')
    pair_projection_counts = validate_partial_permutations(points, terms)
    alive = set(range(n))
    separating_inequalities = 0
    removed_count = 0
    summaries = []
    for number, record in enumerate(data['rounds']):
        if len(alive) < dimension:
            raise ArithmeticError('The certificate continues after the dimension contradiction')
        ranks, retained_terms = coordinate_ranks(alive, terms, n)
        limit = basis_rank + 2 * (len(alive) - dimension)
        if record['round'] != number or record['input_dimension'] != len(alive):
            raise ArithmeticError('A peeling round has the wrong input dimension')
        if record['rank_limit'] != limit or record['retained_source_terms'] != retained_terms:
            raise ArithmeticError('The rank limit or restricted source-term count is incorrect')
        if record['coordinate_slice_ranks'] != [[c, ranks[c]] for c in sorted(alive)]:
            raise ArithmeticError('A restricted coordinate-slice rank is incorrect')
        good = {weight: [c for c in group if c in alive and ranks[c] <= limit]
                for weight, group in groups.items()}
        if record['good_coordinate_counts_by_weight'] != [[w, len(good[w])] for w in groups]:
            raise ArithmeticError('The good-coordinate count is incorrect')
        removed = set()
        for deletion in record['removed_coordinates']:
            coordinate = deletion['coordinate']
            if type(coordinate) is not int or coordinate not in alive or coordinate in removed:
                raise ArithmeticError('A deletion is duplicated or outside the current coordinate space')
            i, k, s = points[coordinate]
            weight = i + s - k
            if deletion['source_point'] != [i, k, s] or deletion['weight'] != weight:
                raise ArithmeticError('A deletion has the wrong coordinate or weight')
            line = deletion['separating_line']
            if line is None:
                if good[weight]:
                    raise ArithmeticError('An empty-hull certificate has admissible coordinates')
            else:
                if len(line) != 3 or any(type(value) is not int for value in line):
                    raise ArithmeticError('A separating line must have three integer coefficients')
                aa, bb, cc = line
                if aa * i + bb * s <= cc:
                    raise ArithmeticError('The separating line does not exclude the removed point')
                for candidate in good[weight]:
                    ci, _, cs = points[candidate]
                    if aa * ci + bb * cs > cc:
                        raise ArithmeticError('The separating line excludes an admissible coordinate')
                    separating_inequalities += 1
            removed.add(coordinate)
        next_alive = alive - removed
        if record['output_dimension'] != len(next_alive):
            raise ArithmeticError('A peeling round has the wrong output dimension')
        expected_weights = [[w, sum(c in next_alive for c in group)] for w, group in groups.items()]
        if record['output_weight_dimensions'] != expected_weights:
            raise ArithmeticError('The output weight dimensions are incorrect')
        summaries.append({'round': number, 'input_dimension': len(alive),
                          'rank_limit': limit, 'removed': len(removed),
                          'output_dimension': len(next_alive)})
        removed_count += len(removed)
        alive = next_alive
    if data['remaining_coordinates'] != sorted(alive) or data['remaining_dimension'] != len(alive):
        raise ArithmeticError('The remaining coordinate space is incorrect')
    excluded = len(alive) < dimension
    if data['ordinary_graded_restriction_excluded'] is not excluded:
        raise ArithmeticError('The recorded dimension conclusion is incorrect')
    if data.get('ungraded_restrictions_excluded') or data.get('arbitrary_singular_limits_excluded') or data.get('improves_omega'):
        raise ArithmeticError('The certificate overstates its mathematical scope')
    return {
        'source_pair_projections_checked': pair_projection_counts,
        'rounds': summaries,
        'separating_inequalities_checked': separating_inequalities,
        'removed_coordinates': removed_count,
        'remaining_dimension': len(alive),
        'target_dimension': dimension,
        'ordinary_graded_restriction_excluded': excluded,
        'convex_hull_algorithm_used_by_verifier': False,
    }


def corner_and_torus_controls(a=8, b=8):
    """Independent explanation of the first round's exposed corner ranks."""
    points, terms, _ = source_data(a, b)
    index = {point: c for c, point in enumerate(points)}
    low = (0, b - 1, b - 1)
    high = (a - 1, a - 1, 0)
    actual_low, actual_high = set(), set()
    weight_identity_checks = 0
    for x, y, z in terms:
        xi, xk, xs = points[x]
        yi, yk, ys = points[y]
        zi, zk, zs = points[z]
        if (xk + xs) + (-yi - yk) + (zi - zs) != 0:
            raise ArithmeticError('The corner-exposing source torus does not preserve a term')
        weight_identity_checks += 1
        if z == index[low]:
            actual_low.add((x, y))
        if z == index[high]:
            actual_high.add((x, y))
    expected_low = {(index[i, p + b - 1, s], index[p, s, b - 1 - i])
                    for i in range(min(a, b)) for p in range(a) for s in range(b)}
    expected_high = {(index[i, p, s], index[p, a - 1 + s, a - 1 - i])
                     for i in range(max(0, a - b), a) for p in range(a) for s in range(b)}
    if actual_low != expected_low or actual_high != expected_high:
        raise ArithmeticError('An exposed corner slice disagrees with its exact matching')
    size = a * b * min(a, b)
    for pairs in (actual_low, actual_high):
        if len(pairs) != size or len({x for x, _ in pairs}) != size or len({y for _, y in pairs}) != size:
            raise ArithmeticError('An exposed corner does not have the asserted matching rank')
    low_weight_ranks = Counter(points[x][0] + points[x][2] - points[x][1] for x, _ in actual_low)
    return {
        'source_torus_weight_identities_checked': weight_identity_checks,
        'low_corner': list(low), 'high_corner': list(high),
        'full_rank_of_each_corner_slice': size,
        'low_corner_slice_ranks_by_first_leg_weight': [[w, r] for w, r in sorted(low_weight_ranks.items())],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT)
    parser.add_argument('--verify', type=Path)
    args = parser.parse_args()
    if args.verify:
        data = json.loads(args.verify.read_text())
    else:
        data = discover()
        data['corner_controls'] = corner_and_torus_controls()
        args.output.write_text(json.dumps(data, indent=2) + '\n')
    result = verify_certificate(data)
    if 'corner_controls' in data and data['corner_controls'] != corner_and_torus_controls(*data['source_parameters']):
        raise ArithmeticError('The recorded corner controls are incorrect')
    print(json.dumps({'certificate': str(args.verify or args.output), **result}, indent=2))


if __name__ == '__main__':
    main()
