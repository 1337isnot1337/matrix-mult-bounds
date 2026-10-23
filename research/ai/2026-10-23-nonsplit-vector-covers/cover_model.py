"""Exact degree-class hypergraph for finite nonsplit cube covers."""
from collections import Counter
from itertools import product
from math import comb


PRINCIPAL = [9, 8, 10, 8, 18, 8, 10, 8, 9]


def classes(j):
    if type(j) is not int or not 0 <= j <= 3:
        raise ValueError('principal factor count must be 0, 1, 2 or 3')
    counts = Counter({0: 1})
    for _ in range(j):
        following = Counter()
        for a, x in counts.items():
            for b, y in enumerate(PRINCIPAL):
                following[a+b] += x*y
        counts = following
    return {(p, b, e): count*16**(3-j)*comb(3-j, b)*comb(3, e)
            for p, count in sorted(counts.items())
            for b in range(4-j) for e in range(4)}


def triples(cap):
    return [(a, b, c) for a in range(cap+1)
            for b in range(cap+1-a) for c in range(cap+1-a-b)]


def edges(j, even_principal=False):
    for p, b, e in product(triples(8*j), triples(3-j), triples(3)):
        if even_principal and sum(p) % 2:
            continue
        yield tuple(zip(p, b, e))


def verify_block(j, selected, even_principal=False):
    counts = classes(j)
    if (len(selected) != 3 or any(len(leg) != len(set(map(tuple, leg)))
                                 for leg in selected)):
        raise ValueError('wrong cover format or duplicate class')
    sets = [set(map(tuple, leg)) for leg in selected]
    if any(not leg <= counts.keys() for leg in sets):
        raise ValueError('unknown degree class')
    checked = 0
    for edge in edges(j, even_principal):
        if all(label not in sets[leg] for leg, label in enumerate(edge)):
            raise ValueError('uncovered admissible degree triple')
        checked += 1
    dimension = 88**j*32**(3-j)*8
    if sum(counts.values()) != dimension:
        raise ArithmeticError('incomplete one-leg class multiplicity')
    return {'principal_factors': j, 'even_principal': even_principal,
            'classes_per_leg': len(counts),
            'one_leg_dimension': dimension, 'admissible_triples_checked': checked,
            'per_word_slices': sum(counts[label] for leg in sets for label in leg)}
