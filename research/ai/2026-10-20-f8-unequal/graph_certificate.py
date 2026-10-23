"""Independent exact checks for the unequal normal-graph parameterization."""
from itertools import product
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-10-20-group-potentials'))
from octal_group import group,fm
from group_exact import pair_map


def scalar_order():
    values = [1]
    for _ in range(6):
        values.append(fm(values[-1],3))
    return values


def check(base,counts,sets,require_pairs=True):
    if len(base)!=6 or len(counts)!=3 or any(len(row)!=7 for row in counts):
        raise ValueError('six base columns and three seven-fiber patterns required')
    coordinate = {}
    for word in range(64):
        value = 0
        for j in range(6):
            if word & (1 << j):
                value ^= base[j]
        if value in coordinate:
            raise ValueError('dependent base columns')
        coordinate[value] = word
    H = scalar_order()
    shape = list(map(sum,counts))
    if list(map(len,sets))!=shape:
        raise ValueError('wrong subset cardinalities')
    cells = [{},{},{}]
    nonlinear = 0
    for f,row in enumerate(sets):
        if len(set(row))!=len(row) or any(not isinstance(g,int) or not 0<=g<448 for g in row):
            raise ValueError('invalid group subset')
        for i,a in enumerate(H):
            cell = {g % 64 for g in row if g//64+1==a}
            if len(cell)!=counts[f][i]:
                raise ValueError('wrong normal-fiber size')
            projection = {(coordinate[v]>>(2*f)) & 3 for v in cell}
            if len(projection)!=len(cell):
                raise ValueError('fiber is not a graph over its own base plane')
            cells[f][a] = cell
            if len(cell)==4:
                parity = 0
                for v in cell:
                    parity ^= v
                nonlinear += parity!=0
        n = counts[f][0]
        expected = {0,base[2*f],base[2*f+1]}
        if n==4:
            expected.add(base[2*f]^base[2*f+1])
        if cells[f][1]!=expected:
            raise ValueError('identity fiber does not match its normalized base')
    triples = 0
    for a,b,c in product(H,repeat=3):
        rows = cells[0][a],cells[1][b],cells[2][c]
        if not all(rows):
            continue
        sums = {x^y^z for x,y,z in product(*rows)}
        if len(sums)!=len(rows[0])*len(rows[1])*len(rows[2]):
            raise ValueError('normal-fiber triple sum is not injective')
        triples += 1
    G = group()
    sizes = []
    for f,g in [(0,1),(1,2),(2,0)]:
        try:
            sizes.append(len(pair_map(G,sets[f],sets[g])))
        except ValueError:
            if require_pairs:
                raise
            sizes.append(None)
    return {'shape':shape,'normal_fiber_triples_checked':triples,
            'pair_map_sizes':sizes,'non_affine_four_point_fibers':nonlinear,
            'scope':'Graph and group pair-injection checks only; no strict potential is inferred.'}
