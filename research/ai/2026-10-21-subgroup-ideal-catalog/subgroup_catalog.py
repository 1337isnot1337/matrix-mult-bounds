"""Enumerate exact subgroup lattices and certify their averaging ideals."""
import argparse
import gzip
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'catalog_subgroup_ideal', HERE.parent/'2026-10-21-subgroup-ideal/ideal.py')
ideal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ideal)


def generated(G, generators):
    """Right multiplication suffices for a finite generated subgroup."""
    members, queue = {0}, [0]
    for x in queue:
        for g in generators:
            y = G['mul'][x][g]
            if y not in members:
                members.add(y)
                queue.append(y)
    return tuple(sorted(members))


def lattice(G):
    found, queue = {(0,): ()}, [(0,)]
    for H in queue:
        covered = set(H)
        for g in range(len(G['mul'])):
            if g in covered:
                continue
            # <H,h*g> = <H,g> for h in H. Skip only this one H-coset.
            covered.update(G['mul'][h][g] for h in H)
            generators = found[H]+(g,)
            K = generated(G, generators)
            if K not in found:
                found[K] = generators
                queue.append(K)
    return [{'members': list(H), 'generators': list(generators)}
            for H, generators in sorted(found.items(), key=lambda x: (len(x[0]), x[0]))]


def minimal_cosets(records, shape):
    """Keep every inclusion-minimal forbidden set, separately in each leg."""
    result = []
    for f, size in enumerate(shape):
        other = shape[(f+1) % 3]*shape[(f+2) % 3]
        candidates = {tuple(C) for r in records if r['ideal_dimension'] < other
                      for C in r['cosets'] if len(C) <= size}
        minimal, sets = [], []
        for C in sorted(candidates, key=lambda C: (len(C), C)):
            points = set(C)
            if not any(K <= points for K in sets):
                minimal.append(list(C))
                sets.append(points)
        result.append(minimal)
    return result


def derive(G, shape):
    subgroups = lattice(G)
    remaining = {tuple(r['members']) for r in subgroups}
    records = []
    while remaining:
        H = min(remaining, key=lambda H: (len(H), H))
        record = ideal.derive(G, list(H))
        remaining.difference_update(map(tuple, record['conjugate_subgroups']))
        records.append(record)
    return {'group': G['name'], 'target_shape': shape, 'subgroups': subgroups,
            'ideal_classes': records, 'minimal_forbidden_cosets': minimal_cosets(records, shape)}


def read(path):
    return json.loads(gzip.decompress(Path(path).read_bytes()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    records = [derive(G, shape) for G, shape in zip(
        ideal.sources(), ([10, 10, 10], [10, 10, 10], [13, 13, 15]))]
    report = {'base_commit': '00d51337ddfe581a6e53ff9bc71bb1ece6ad8ee8',
              'records': records, 'exponent_improvement': False,
              'scope': 'Complete finite subgroup-ideal coset cuts for the stated '
                       'coordinate/potential targets; not a target exclusion.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(report, separators=(',', ':'))+'\n').encode()
    args.output.write_bytes(gzip.compress(raw, mtime=0))
    print(json.dumps([{'group': r['group'], 'subgroups': len(r['subgroups']),
                       'classes': len(r['ideal_classes']),
                       'minimal_cosets_per_leg': list(map(len, r['minimal_forbidden_cosets']))}
                      for r in records]))
