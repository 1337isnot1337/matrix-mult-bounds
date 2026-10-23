"""Exact recognition of coefficient-one convolution supports up to relabeling.

Discovery uses a rational kernel. Acceptance only replays integer bijections
against the complete canonical support. No tensor coefficients are inferred
from the support: callers must separately ensure that every coefficient is one.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from fractions import Fraction


def _nullspace(rows):
    """A rational kernel basis from sparse forward elimination."""
    width = len(rows[0])
    pivots = {}
    for values in rows:
        row = {i: Fraction(v) for i, v in enumerate(values) if v}
        while row:
            column = min(row)
            if column not in pivots:
                scale = row[column]
                pivots[column] = {i: v / scale for i, v in row.items()}
                break
            scale = row[column]
            for i, value in pivots[column].items():
                updated = row.get(i, 0) - scale * value
                if updated:
                    row[i] = updated
                else:
                    row.pop(i, None)
    basis = []
    for free in range(width):
        if free in pivots:
            continue
        vector = [Fraction(0)] * width
        vector[free] = Fraction(1)
        for column in sorted(pivots, reverse=True):
            vector[column] = -sum(value * vector[i]
                                  for i, value in pivots[column].items() if i != column)
        basis.append(vector)
    return basis


def _support(terms):
    try:
        terms = [tuple(term) for term in terms]
    except TypeError as exc:
        raise ValueError('expected an iterable of integer triples') from exc
    if not terms or any(len(t) != 3 or any(type(v) is not int for v in t)
                        for t in terms):
        raise ValueError('expected a nonempty support of integer triples')
    if len(set(terms)) != len(terms):
        raise ValueError('duplicate terms are not coefficient-one support')
    return sorted(terms)


def verify(terms, certificate):
    """Replay a certificate without solving any recognition equations.

    Raise ValueError for a malformed or false certificate; return True otherwise.
    The three explicit maps must be bijections onto complete integer intervals.
    """
    terms = _support(terms)
    try:
        if certificate['schema'] != 'convolution-support-v1':
            raise ValueError('unknown certificate schema')
        output = certificate['output_axis']
        a, b = certificate['a'], certificate['b']
        if type(output) is not int or output not in range(3):
            raise ValueError('invalid output axis')
        if any(type(n) is not int or n < 1 for n in (a, b)):
            raise ValueError('invalid convolution dimensions')
        inputs = [axis for axis in range(3) if axis != output]
        dimensions = [None] * 3
        dimensions[inputs[0]], dimensions[inputs[1]] = a, b
        dimensions[output] = a + b - 1
        maps = certificate['maps']
        if len(maps) != 3:
            raise ValueError('expected three coordinate maps')
        mapping = []
        for axis, pairs in enumerate(maps):
            if any(len(p) != 2 or any(type(x) is not int for x in p) for p in pairs):
                raise ValueError('coordinate maps require integer pairs')
            values = dict(pairs)
            if (len(values) != len(pairs) or len(values) != dimensions[axis]
                    or set(values) != {t[axis] for t in terms}
                    or sorted(values.values()) != list(range(len(values)))):
                raise ValueError('coordinate map is not the required bijection')
            mapping.append(values)
        actual = {tuple(mapping[k][t[k]] for k in range(3)) for t in terms}
        expected = set()
        for i in range(a):
            for j in range(b):
                t = [0] * 3
                t[inputs[0]], t[inputs[1]], t[output] = i, j, i + j
                expected.add(tuple(t))
        if actual != expected:
            raise ValueError('mapped support is not the complete convolution')
    except (KeyError, TypeError, IndexError) as exc:
        raise ValueError('malformed convolution certificate') from exc
    return True


def recognize(terms):
    """Return a replayable convolution certificate, or None.

    All independent coordinate permutations and all output-axis choices are
    covered, including one-dimensional inputs. Labels are arbitrary integers.
    The certificate is deterministic for a given labeled support, but is not a
    canonical choice among its automorphisms.
    """
    terms = _support(terms)
    labels = [sorted({t[k] for t in terms}) for k in range(3)]
    dims = list(map(len, labels))
    offsets = [0, dims[0], dims[0] + dims[1]]
    positions = [{v: offsets[k] + i for i, v in enumerate(labels[k])}
                 for k in range(3)]
    for output in range(3):
        inputs = [k for k in range(3) if k != output]
        a, b = (dims[k] for k in inputs)
        if dims[output] != a + b - 1 or len(terms) != a * b:
            continue
        if len({(t[inputs[0]], t[inputs[1]]) for t in terms}) != a * b:
            continue
        if min(a, b) == 1:
            varying = inputs[1] if a == 1 else inputs[0]
            maps = [{v: i for i, v in enumerate(axis)} for axis in labels]
            maps[output] = {t[output]: maps[varying][t[varying]] for t in terms}
            candidates = [maps]
        else:
            equations = []
            for t in terms:
                row = [0] * sum(dims)
                for k in inputs:
                    row[positions[k][t[k]]] = 1
                row[positions[output][t[output]]] = -1
                equations.append(row)
            kernel = _nullspace(equations)
            candidates = []
            for vector in kernel:
                coordinates = [[vector[positions[k][v]] for v in labels[k]]
                               for k in range(3)]
                first = sorted(set(coordinates[inputs[0]]))
                if len(first) != a:
                    continue
                step = first[1] - first[0]
                low = [min(values) for values in coordinates]
                low[output] = low[inputs[0]] + low[inputs[1]]
                scaled = [[(v - low[k]) / step for v in values]
                          for k, values in enumerate(coordinates)]
                if any(v.denominator != 1 for values in scaled for v in values):
                    continue
                candidates.append([{label: int(value) for label, value in zip(axis, values)}
                                   for axis, values in zip(labels, scaled)])
        for maps in candidates:
            certificate = {'schema': 'convolution-support-v1', 'a': a, 'b': b,
                           'output_axis': output,
                           'maps': [sorted(m.items()) for m in maps]}
            try:
                verify(terms, certificate)
            except ValueError:
                continue
            return certificate
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('support', type=Path, help='JSON array of integer triples')
    parser.add_argument('--certificate', type=Path, help='replay this JSON certificate')
    args = parser.parse_args()
    terms = json.loads(args.support.read_text())
    if args.certificate:
        verify(terms, json.loads(args.certificate.read_text()))
        print(json.dumps({'verified': True}))
    else:
        print(json.dumps(recognize(terms), indent=2))


if __name__ == '__main__':
    main()
