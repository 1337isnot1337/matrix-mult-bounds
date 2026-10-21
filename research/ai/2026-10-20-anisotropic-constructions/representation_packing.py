"""Exact SL2 multiplicity packing for cyclic anisotropic convolutions.

This is a necessary test for the specifically equivariant construction ansatz,
not a tensor degeneration certificate and not an obstruction to general maps.
"""

from collections import Counter
from functools import lru_cache
from itertools import product
import json
import math


def tensor_product(left, right):
    result = Counter()
    for d, md in left.items():
        for e, me in right.items():
            for f in range(abs(d-e), d+e+1, 2):
                result[f] += md*me
    return dict(result)


def source_multiplicities(a, b):
    return tensor_product(tensor_product({a-1: 1}, {b-1: 1}), {a+b-2: 1})


def two_factor_sources(a,b):
    m=a+b-1
    pairs = ((a-1,b-1,m),(b-1,m-1,a),(m-1,a-1,b))
    return [{d: mult*copies for d,mult in tensor_product({p:1},{q:1}).items()}
            for p,q,copies in pairs]


def fits(left, right, source):
    value = tensor_product(left, right)
    return all(m <= source.get(d, 0) for d, m in value.items())


@lru_cache(maxsize=None)
def representations(dimension, maximum_degree, parity):
    """All representations of a fixed center parity and bounded top degree."""
    degrees = tuple(range(parity, maximum_degree+1, 2))
    out = []

    def visit(pos, remaining, terms):
        if pos == len(degrees):
            if remaining == 0:
                out.append(tuple(terms))
            return
        degree = degrees[pos]
        for multiplicity in range(remaining//(degree+1)+1):
            if multiplicity:
                terms.append((degree, multiplicity))
            visit(pos+1, remaining-multiplicity*(degree+1), terms)
            if multiplicity:
                terms.pop()

    visit(0, dimension, [])
    return tuple(out)


def target_shapes(a, b):
    n = a*b*(a+b-1)
    base = 3*(a+b)-2
    for l in range(2, math.isqrt(n)+1):
        for h in range(l, math.isqrt(n)+1):
            for r in range(h, n//h+1):
                if 216*l*h*r > base**4:
                    yield l, h, r


def ordinary_rank_screen(a, b, shape):
    n = a*b*(a+b-1)
    l, h, r = shape
    return all(z*(x+y-1) <= 2*n-a*b
               for x, y, z in ((l,h,r),(h,r,l),(r,l,h)))


def equivariant_packing(a, b, shape, two_factor=False):
    source = source_multiplicities(a,b)
    sources = two_factor_sources(a,b) if two_factor else [source]*3
    maximum = max(max(x) for x in sources)
    report = {"source": [a,b], "target": list(shape),
              "source_leg_dimension": a*b*(a+b-1),
              "source_multiplicities": sources,
              "two_factor_action": two_factor,
              "representations": [], "fitting_pairs": 0,
              "fitting_triples": 0, "witness": None}
    for parities in product((0,1),repeat=3):
        if any((parities[i]+parities[j])%2 != next(iter(sources[axis]))%2
               for axis,(i,j) in enumerate(((0,1),(1,2),(2,0)))):
            continue
        lists = [tuple(dict(rep) for rep in representations(d,maximum,parity))
                 for d,parity in zip(shape,parities)]
        # Every pairwise tensor product must fit. In particular its highest
        # degree and trivial multiplicity obey the exact source bounds.
        neighbors_01 = [[] for _ in lists[0]]
        neighbors_02 = [[] for _ in lists[0]]
        neighbors_12 = [set() for _ in lists[1]]
        for i, rep0 in enumerate(lists[0]):
            for j, rep1 in enumerate(lists[1]):
                if fits(rep0,rep1,sources[0]):
                    neighbors_01[i].append(j)
            for k, rep2 in enumerate(lists[2]):
                if fits(rep0,rep2,sources[2]):
                    neighbors_02[i].append(k)
        for j, rep1 in enumerate(lists[1]):
            for k, rep2 in enumerate(lists[2]):
                if fits(rep1,rep2,sources[1]):
                    neighbors_12[j].add(k)
        report["representations"].append([len(x) for x in lists])
        report["fitting_pairs"] += sum(map(len,neighbors_01))+sum(map(len,neighbors_02))+sum(map(len,neighbors_12))
        for i, js in enumerate(neighbors_01):
            for j in js:
                for k in set(neighbors_02[i]) & neighbors_12[j]:
                    report["fitting_triples"] += 1
                    if report["witness"] is None:
                        report["witness"] = [lists[0][i], lists[1][j], lists[2][k]]
    return report


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("a",type=int)
    parser.add_argument("b",type=int)
    parser.add_argument("shape",type=int,nargs=3)
    parser.add_argument("--two-factor",action="store_true")
    args=parser.parse_args()
    print(json.dumps(equivariant_packing(args.a,args.b,args.shape,args.two_factor),indent=2))
