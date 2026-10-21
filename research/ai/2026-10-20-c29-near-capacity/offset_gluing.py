"""Exact modular gluing of all local pair-quotient packing choices.

Each allowed relative-translation triple gives three linear equations in
the eight normalized offset variables over F29. All compatible affine
systems are explored; no SAT or numerical optimization is needed.
"""
import argparse
from itertools import product
import json
from pathlib import Path

from cyclic_packing import rotate
from fiber_frontier import P, SCALARS, points

VARIABLES = [(f,i) for f in range(3) for i in range(1,4) if (f,i) != (0,1)]


def packing_list(cells,f,g,q):
    masks = []
    for i,a in enumerate(SCALARS):
        j = SCALARS.index(a*q % P)
        values = {(pow(a,-1,P)*(y-x)) % P
                  for x,y in product(points(cells[f][i]),points(cells[g][j]))}
        if len(values) != cells[f][i][0]*cells[g][j][0]:
            raise ArithmeticError('pair fiber has repeated labels')
        masks.append(sum(1 << v for v in values))
    shifted = [[rotate(mask,t,P) for t in range(P)] for mask in masks]
    allowed = []
    for x in range(P):
        a,b = shifted[0][0],shifted[1][x]
        if a & b:
            continue
        for y in range(P):
            c = shifted[2][y]
            if c & (a | b):
                continue
            for z in range(P):
                d = shifted[3][z]
                if not d & (a | b | c):
                    allowed.append((x,y,z))
    return allowed


def coefficient_rows(f,g,q):
    rows = []
    j0 = SCALARS.index(q)
    for i,a in enumerate(SCALARS[1:],1):
        j = SCALARS.index(a*q % P)
        row = [0]*len(VARIABLES)
        for cell,value in [((g,j),pow(a,-1,P)),((f,i),-pow(a,-1,P)),
                           ((g,j0),-1),((f,0),1)]:
            if cell in VARIABLES:
                k = VARIABLES.index(cell)
                row[k] = (row[k]+value) % P
        rows.append(row)
    return rows


def extend(basis,coefficients,values):
    """Canonical reduced row echelon form; return None on inconsistency."""
    basis = {pivot:list(row) for pivot,row in basis}
    for coefficients,value in zip(coefficients,values):
        row = [x % P for x in coefficients]+[value % P]
        for pivot,old in sorted(basis.items()):
            scalar = row[pivot]
            row = [(a-scalar*b) % P for a,b in zip(row,old)]
        pivot = next((i for i,v in enumerate(row[:-1]) if v),None)
        if pivot is None:
            if row[-1]:
                return None
            continue
        scalar = pow(row[pivot],-1,P)
        row = [(v*scalar) % P for v in row]
        for old_pivot,old in list(basis.items()):
            scalar = old[pivot]
            basis[old_pivot] = [(a-scalar*b) % P for a,b in zip(old,row)]
        basis[pivot] = row
    return tuple((pivot,tuple(row)) for pivot,row in sorted(basis.items()))


def solve(cells):
    constraints = []
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in SCALARS:
            allowed = packing_list(cells,f,g,q)
            constraints.append({'families':[f,g],'quotient':q,
                                'coefficients':coefficient_rows(f,g,q),
                                'allowed':allowed})
    systems = []
    visited = 0
    failed = set()

    def search(basis,remaining):
        nonlocal visited
        visited += 1
        state = basis,remaining
        if state in failed:
            return
        if not remaining:
            systems.append(basis)
            return
        chosen = None
        extensions = None
        for i in remaining:
            constraint = constraints[i]
            following = {extend(basis,constraint['coefficients'],row)
                         for row in constraint['allowed']}
            following.discard(None)
            if not following:
                failed.add(state)
                return
            if extensions is None or len(following) < len(extensions):
                chosen,extensions = i,following
        rest = tuple(i for i in remaining if i != chosen)
        for following in sorted(extensions):
            search(following,rest)

    search((),tuple(range(len(constraints))))
    return {'variables':[list(x) for x in VARIABLES],
            'constraints':constraints,'affine_systems':systems,
            'search_states':visited,'inconsistent_states':len(failed),
            'complete':True}


def run(source):
    report = json.loads(source.read_text())
    records = []
    for base in report['records']:
        for candidate in base['survivors']:
            result = solve(candidate['cells'])
            records.append({'base_directions':base['base_directions'],
                            'family_indices':candidate['family_indices'],
                            'cells':candidate['cells'],**result})
    return {'group':'C29:C4','shape':[10]*3,'candidates_checked':len(records),
            'compatible_affine_systems':sum(len(r['affine_systems']) for r in records),
            'records':records,'scope':__doc__,'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run(args.source)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'records'},indent=2))
