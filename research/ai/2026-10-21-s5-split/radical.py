"""Exact defining-characteristic ideal-power exploration in F2[S5]."""
import argparse
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path

from s5_source import group


def insert(value, basis):
    while value:
        p = value.bit_length()-1
        if p not in basis:
            basis[p] = value
            return True
        value ^= basis[p]
    return False


def kernel(rows, n):
    basis = {}
    for row in rows:
        insert(row, basis)
    output = []
    for free in sorted(set(range(n))-set(basis)):
        value = 1 << free
        for pivot in sorted(basis):
            if (basis[pivot] & value).bit_count() % 2:
                value |= 1 << pivot
        if any((row & value).bit_count() % 2 for row in rows):
            raise ArithmeticError('incorrect binary kernel')
        output.append(value)
    return output


def coordinates(vectors):
    basis = {}
    for i, value in enumerate(vectors):
        label = 1 << i
        while value:
            p = value.bit_length()-1
            if p not in basis:
                basis[p] = value, label
                break
            row, old = basis[p]
            value ^= row
            label ^= old
        if not value:
            raise ArithmeticError('dependent proposed module basis')

    def express(value):
        label = 0
        while value:
            p = value.bit_length()-1
            if p not in basis:
                raise ArithmeticError('module subspace is not invariant')
            row, old = basis[p]
            value ^= row
            label ^= old
        return label
    return express


def act(value, permutation):
    output = 0
    while value:
        bit = value & -value
        output ^= 1 << permutation[bit.bit_length()-1]
        value ^= bit
    return output


def matrix_product(A, B, d=4):
    output = 0
    for j in range(d):
        column = (B >> (d*j)) & ((1 << d)-1)
        value = 0
        for i in range(d):
            if column >> i & 1:
                value ^= (A >> (d*i)) & ((1 << d)-1)
        output |= value << (d*j)
    return output


def representations(G):
    standard = [(1 << i) | (1 << 4) for i in range(4)]
    std_coordinates = coordinates(standard)
    edges = list(combinations(range(5), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    constraints = [sum(1 << i for i, e in enumerate(edges) if v in e) for v in range(5)]
    constraints.append((1 << 10)-1)
    W = kernel(constraints, 10)
    span, vectors = {}, [(1 << 10)-1]
    insert(vectors[0], span)
    for v in W:
        if insert(v, span):
            vectors.append(v)
    if len(vectors) != 5:
        raise ArithmeticError('incorrect even cycle module dimension')
    cycle_coordinates = coordinates(vectors)
    first, second = [], []
    for p in G['matrices']:
        first.append(sum(std_coordinates(act(v, p)) << (4*i) for i, v in enumerate(standard)))
        edge_action = [edge_index[tuple(sorted((p[a], p[b])))] for a, b in edges]
        if act(vectors[0], edge_action) != vectors[0]:
            raise ArithmeticError('constant edge line is not invariant')
        second.append(sum((cycle_coordinates(act(v, edge_action)) >> 1) << (4*i)
                          for i, v in enumerate(vectors[1:])))
    checked = 0
    for rep in (first, second):
        for g in range(120):
            for h in range(120):
                if matrix_product(rep[g], rep[h]) != rep[G['mul'][g][h]]:
                    raise ArithmeticError('binary representation is not multiplicative')
                checked += 1
    return first, second, {'representation_products_checked': checked,
                            'even_cycle_subspace_dimension': 5,
                            'quotient_module_dimension': 4}


def explore():
    G = group()
    first, second, receipt = representations(G)
    constraints = [(1 << 120)-1]
    for rep in (first, second):
        constraints.extend(sum(1 << g for g in range(120) if rep[g] >> i & 1)
                           for i in range(16))
    J = kernel(constraints, 120)
    translates = [[act(v, G['mul'][g]) for v in J] for g in range(120)]
    powers, previous = [120, len(J)], J
    power_bases = [list(J)]
    for exponent in range(2, 121):
        basis = {}
        for a in previous:
            support = [g for g in range(120) if a >> g & 1]
            for j in range(len(J)):
                value = 0
                for g in support:
                    value ^= translates[g][j]
                insert(value, basis)
        current = list(basis.values())
        powers.append(len(current))
        power_bases.append(current)
        if not current or len(current) == len(previous):
            break
        previous = current
    nilpotent = powers[-1] == 0
    report = {'group': G['name'], 'field': 'F2', **receipt,
              'kernel_dimension': len(J), 'ideal_power_dimensions': powers,
              'representation_matrices': [first, second],
              'power_bases': [[hex(v) for v in basis] for basis in power_bases],
              'nilpotent': nilpotent, 'exponent_improvement': False,
              'scope': 'Exact finite discovery; no source degeneration or optimal filtration claimed.'}
    if nilpotent:
        layers = [powers[i]-powers[i+1] for i in range(len(powers)-1)]
        # Tensor with F2[C2], whose augmentation polynomial is 1+t.
        split_layers = [0]*(len(layers)+1)
        for i, value in enumerate(layers):
            split_layers[i] += value
            split_layers[i+1] += value
        D = len(split_layers)-1
        candidates = []
        for k in range(1, 100):
            t = Fraction(k, 100)
            F = sum(value*t**i for i, value in enumerate(split_layers))
            candidates.append((F**3/t**D, t))
        Q, t = min(candidates)
        report.update(radical_layers=layers, split_layers=split_layers,
                      parameter=str(t), conditional_slice_bound_cubed=str(Q),
                      target_volume_squared=(13*14*14)**2,
                      excludes_target_by_this_bound=(13*14*14)**2 > Q)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = explore()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
