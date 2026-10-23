"""Exact target slice ranks for two rectangular matrix summands."""
from itertools import combinations_with_replacement, permutations, product


AXIS_PERMUTATIONS = tuple(permutations(range(3)))
PERMUTATION_INDEX = {item: index for index, item in enumerate(AXIS_PERMUTATIONS)}


def orientation_orbits(power):
    """Partition orientation multisets by a common reordering of all legs."""
    orbits = {}
    for orientation in combinations_with_replacement(range(6), power):
        orbit = set()
        for common in AXIS_PERMUTATIONS:
            moved = tuple(sorted(PERMUTATION_INDEX[
                tuple(AXIS_PERMUTATIONS[index][common[axis]] for axis in range(3))]
                for index in orientation))
            orbit.add(moved)
        representative = min(orbit)
        if representative in orbits and orbits[representative] != orbit:
            raise ArithmeticError('overlapping orientation orbits')
        orbits[representative] = orbit
    return orbits


def direct_sum_power_slice_rank(shapes, orientation, power):
    total = 0
    for choices in product((0, 1), repeat=power):
        legs = [1, 1, 1]
        for permutation_index, choice in zip(orientation, choices):
            shape = shapes[choice]
            for axis, input_axis in enumerate(AXIS_PERMUTATIONS[permutation_index]):
                legs[axis] *= shape[input_axis]
        total += min(legs[0]*legs[1], legs[1]*legs[2], legs[2]*legs[0])
    return total


def maximum_direct_sum_power_slice_rank(shapes, power):
    orbits = orientation_orbits(power)
    representatives = tuple(sorted(orbits))
    full_count = len(tuple(combinations_with_replacement(range(6), power)))
    if sum(len(orbit) for orbit in orbits.values()) != full_count:
        raise ArithmeticError('common-leg symmetry orbits do not partition all orientation multisets')
    if power == 5 and (len(representatives)*6 != full_count
                       or any(len(orbit) != 6 for orbit in orbits.values())):
        raise ArithmeticError('power-five leg-permutation orbits do not all have size six')
    values = [(direct_sum_power_slice_rank(shapes, orientation, power), orientation)
              for orientation in representatives]
    maximum = max(value for value, orientation in values)
    witnesses = [[list(AXIS_PERMUTATIONS[index]) for index in orientation]
                 for value, orientation in values if value == maximum]
    return {'power': power, 'orientation_multisets_checked': len(representatives),
            'full_orientation_multisets': full_count,
            'maximum_slice_rank': maximum,
            'maximizing_orientation_multisets': witnesses}
