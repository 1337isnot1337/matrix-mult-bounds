"""SL(2,5) x C2, its normalization subgroup, and exact source accounting."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

SEVEN = Path(__file__).resolve().parents[1]/'2026-10-20-sl2-seven'
sys.path.insert(0, str(SEVEN/'imported'))
from group_exact import group as sl2_group


def group():
    base = sl2_group(5)
    n = 2*len(base['matrices'])
    return {'name': 'SL(2,5) x C2', 'identity': 0,
            'matrices': [(matrix, bit) for matrix in base['matrices'] for bit in (0, 1)],
            'mul': [[2*base['mul'][g//2][h//2]+((g & 1) ^ (h & 1))
                     for h in range(n)] for g in range(n)],
            'inv': [2*base['inv'][g//2]+(g & 1) for g in range(n)]}


def subgroup_certificate(G):
    base = sl2_group(5)
    index = {m: i for i, m in enumerate(base['matrices'])}
    i, j = index[0, 1, 4, 0], index[2, 0, 0, 3]
    k = base['mul'][i][j]
    r = tuple(3*sum(values) % 5 for values in zip(
        base['matrices'][0], base['matrices'][i], base['matrices'][j], base['matrices'][k]))
    generators = [2*i, 2*j, 2*index[r], 1]
    H, todo = {0}, [0]
    while todo:
        x = todo.pop()
        for g in generators:
            y = G['mul'][x][g]
            if y not in H:
                H.add(y)
                todo.append(y)
    if len(H) != 48 or any(G['mul'][g][h] not in H for g in H for h in H):
        raise ArithmeticError('incorrect normalization subgroup')
    center = [z for z in range(240) if all(G['mul'][z][g] == G['mul'][g][z]
                                          for g in range(240))]
    orbits = sorted({tuple(sorted(G['mul'][z][g] for z in center)) for g in range(240)})
    if len(center) != 4 or len(orbits) != 60 or any(len(x) != 4 for x in orbits):
        raise ArithmeticError('incorrect central orbits')
    return {'generators': generators, 'members': sorted(H), 'order': 48, 'index': 5,
            'center': center, 'central_orbits': orbits}


def source_certificate():
    spec = importlib.util.spec_from_file_location('sl2_rational_source', SEVEN/'source_certificate.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    factor = module.derive(5)
    degrees = factor['complex_degrees']*2
    if sum(d*d for d in degrees) != 240:
        raise ArithmeticError('wrong direct-product dimension')
    # Resolve the maintained concurrent rank-locus screen by its actual path.
    research = SEVEN.parent/'2026-10-20-group-potentials'
    sys.path.insert(0, str(research))
    from rank_locus_obstruction import screen
    result = {'group': 'SL(2,5) x C2', 'order': 240,
              'first_factor_rational_certificate': factor,
              'complex_degrees': degrees,
              'degree_interpretation': 'C2 has two one-dimensional complex irreducibles; '
                  'irreducibles of a direct product are tensor products.',
              'conditional_gate': module.exponent_gate(degrees, shape=(13, 13, 15)),
              'concurrent_rank_locus_screen': screen(degrees, [13, 13, 15]),
              'degeneration_constructed': False, 'exponent_improvement': False}
    return result


def central_projection(G, certificate):
    orbits = certificate['central_orbits']
    projection = [None]*len(G['matrices'])
    for i, orbit in enumerate(orbits):
        for g in orbit:
            projection[g] = i
    representatives = [min(orbit) for orbit in orbits]
    inverses = [projection[G['inv'][g]] for g in representatives]
    fibers = {}
    for g, image in enumerate(projection):
        if image:
            c = min(image, inverses[image])
            fibers.setdefault(c, set()).add(min(g, G['inv'][g]))
    return {'representatives': representatives, 'projection': projection,
            'inverse': inverses, 'inverse_class_lifts': {c: sorted(v) for c, v in fibers.items()}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = source_certificate()
    result['normalization_subgroup'] = subgroup_certificate(group())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'group': result['group'], 'gate': result['conditional_gate'],
                      'rank_screen': result['concurrent_rank_locus_screen']}))
