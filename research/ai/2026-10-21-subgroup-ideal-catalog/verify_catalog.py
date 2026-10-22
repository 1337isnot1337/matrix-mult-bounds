"""Replay subgroup completeness, integer rank certificates and minimal cuts."""
import argparse
from collections import Counter
import json
from pathlib import Path

from subgroup_catalog import ideal, read


def verify_lattice(G, records):
    n, M = len(G['mul']), G['mul']
    listed = {tuple(r['members']) for r in records}
    if len(listed) != len(records) or (0,) not in listed:
        raise ValueError('duplicate subgroup or missing trivial subgroup')
    # Independently build closures using left multiplication.
    def closure(generators):
        points, todo = {0}, [0]
        for x in todo:
            for g in generators:
                y = M[g][x]
                if y not in points:
                    points.add(y)
                    todo.append(y)
        return tuple(sorted(points))
    for row in records:
        H, generators = row['members'], row['generators']
        if (H != sorted(set(H)) or not H or H[0] != 0 or
                any(type(g) is not int or not 0 <= g < n for g in H+generators)
                or closure(generators) != tuple(H)):
            raise ValueError('invalid generated subgroup')
        covered = set(H)
        for g in range(n):
            if g in covered:
                continue
            # Right H-cosets give the same generated supergroup as g.
            covered.update(M[g][h] for h in H)
            if closure(generators+[g]) not in listed:
                raise ValueError('subgroup lattice is not extension-complete')
    return listed


def verify(G, record):
    if record['group'] != G['name']:
        raise ValueError('wrong source group')
    listed = verify_lattice(G, record['subgroups'])
    assigned, forbidden, dimensions = set(), [set() for _ in range(3)], {}
    shape = record['target_shape']
    if len(shape) != 3 or any(type(s) is not int or s <= 0 for s in shape):
        raise ValueError('invalid target dimensions')
    for item in record['ideal_classes']:
        ideal.verify(G, item)
        conjugates = set(map(tuple, item['conjugate_subgroups']))
        if assigned & conjugates or not conjugates <= listed:
            raise ValueError('duplicate or unlisted conjugacy class')
        assigned.update(conjugates)
        for C in item['cosets']:
            dimensions[tuple(C)] = item['ideal_dimension']
        for f, size in enumerate(shape):
            if item['ideal_dimension'] < shape[(f+1) % 3]*shape[(f+2) % 3]:
                forbidden[f].update(tuple(C) for C in item['cosets'] if len(C) <= size)
    if assigned != listed:
        raise ValueError('ideal classes do not cover the subgroup lattice')
    if len(record['minimal_forbidden_cosets']) != 3:
        raise ValueError('three target legs are required')
    summary = []
    for f, saved in enumerate(record['minimal_forbidden_cosets']):
        proposed = set(map(tuple, saved))
        if len(proposed) != len(saved) or not proposed <= forbidden[f]:
            raise ValueError('invalid forbidden coset')
        # Check minimality and coverage separately, without rerunning the
        # generator's greedy subset selection.
        sets = [set(C) for C in proposed]
        if any(A < B for A in sets for B in sets):
            raise ValueError('redundant purported minimal coset')
        if any(not any(A <= set(C) for A in sets) for C in forbidden[f]):
            raise ValueError('missing minimal forbidden coset')
        counts = Counter((len(C), dimensions[C]) for C in proposed)
        summary.append([{'order': k, 'ideal_dimension': d, 'cosets': count}
                        for (k, d), count in sorted(counts.items())])
    return {'group': G['name'], 'target_shape': shape, 'subgroups': len(listed),
            'conjugacy_classes': len(record['ideal_classes']),
            'minimal_cosets_per_leg': list(map(len, record['minimal_forbidden_cosets'])),
            'minimal_classes_per_leg': summary}


def verify_report(report):
    groups = ideal.sources()
    if len(report['records']) != len(groups) or report['exponent_improvement'] is not False:
        raise ValueError('wrong source count or exponent status')
    expected = ([10, 10, 10], [10, 10, 10], [13, 13, 15])
    receipts = []
    for G, record, shape in zip(groups, report['records'], expected):
        if record['target_shape'] != shape:
            raise ValueError('incorrect catalog target')
        receipts.append(verify(G, record))
    return receipts


def split_search_record(G, record):
    """A common valid upper bound lets the existing M10 runner use all cuts."""
    receipt = verify(G, record)
    if (G['name'] != 'PSL(2,5) x C2' or record['target_shape'] != [10]*3
            or any(C != record['minimal_forbidden_cosets'][0]
                   for C in record['minimal_forbidden_cosets'])):
        raise ValueError('the search adapter requires the split-cover M10 target')
    cosets = record['minimal_forbidden_cosets'][0]
    selected = set(map(tuple, cosets))
    upper = max(r['ideal_dimension'] for r in record['ideal_classes']
                if selected.intersection(map(tuple, r['cosets'])))
    return {'group': G['name'], 'ideal_dimension': upper, 'cosets': cosets}, receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipts = verify_report(read(args.report))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipts, indent=2)+'\n')
    print(json.dumps(receipts))
