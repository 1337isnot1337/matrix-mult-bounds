"""Reuse verified parity cuts and their independent right-translation orbits."""
import gzip
import hashlib
from itertools import permutations
import json
from pathlib import Path

from verify_projected_reports import verify_parity


def canonical_pattern(Q, points):
    if not points:
        return ()
    return min(tuple(sorted(Q['mul'][p][Q['inv'][anchor]] for p in points))
               for anchor in points)


def read_verified(Q, report_path):
    report_path = Path(report_path)
    report = json.loads(report_path.read_text())
    path = report_path.with_suffix('.cuts.jsonl')
    if path.exists():
        encoded = payload = path.read_bytes()
    else:
        path = Path(str(path)+'.gz')
        encoded = path.read_bytes()
        payload = gzip.decompress(encoded)
    items = []
    for line in payload.splitlines():
        item = json.loads(line)
        if item['type'] == 'exact-parity':
            verify_parity(Q, item)
            items.append(item)
    if len(items) != report['exact_parity_cuts']:
        raise ValueError('wrong reused parity count')
    return items, {'report': str(report_path),
                   'report_sha256': hashlib.sha256(report_path.read_bytes()).hexdigest(),
                   'cut_file': str(path), 'cut_sha256': hashlib.sha256(encoded).hexdigest(),
                   'exact_parity_cuts': len(items)}


def append_templates(Q, items, pool, members, clauses, maximum_support=18):
    before = len(clauses)
    triples = set()
    for item in items:
        support = [tuple(x) for x in item['blocked_points']]
        clauses.append([-members[f][p] for f, p in support])
        if len(support) <= maximum_support:
            patterns = [canonical_pattern(Q, [p for h, p in support if h == f])
                        for f in range(3)]
            triples.update(permutations(patterns))
    flags, orbit_clauses = {}, 0

    def flag(f, pattern):
        nonlocal orbit_clauses
        if len(pattern) <= 1:
            return None  # Every target set is nonempty.
        key = f, pattern
        if key not in flags:
            variable = pool.id(('parity-pattern', f, pattern))
            flags[key] = variable
            translates = {tuple(sorted(Q['mul'][p][g] for p in pattern))
                          for g in range(len(Q['representatives']))}
            for points in sorted(translates):
                clauses.append([-members[f][p] for p in points]+[variable])
                orbit_clauses += 1
        return flags[key]

    for triple in sorted(triples):
        variables = [flag(f, pattern) for f, pattern in enumerate(triple)]
        clauses.append([-v for v in variables if v is not None])
    return {'maximum_core_support': maximum_support,
            'reused_specific_cuts': len(items), 'template_triples': len(triples),
            'pattern_flags': len(flags), 'right_translation_trigger_clauses': orbit_clauses,
            'additional_clauses': len(clauses)-before}
