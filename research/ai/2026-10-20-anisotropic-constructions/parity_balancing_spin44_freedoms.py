"""Exact low-coordinate freedoms of the published balanced32 restriction.

This standard-library replay was reconstructed from the published116 maps
after the execution environment restored an earlier filesystem snapshot.
It recomputes every response used by the rank and kernel certificates.
"""

from collections import Counter, defaultdict
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity_balancing_spin_assembly as source


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'results/anisotropic-constructions-2026-10-20'
MAPS = DIRECTORY / 'parity_balancing_spin44_full_maps.json'
CERTIFICATE = DIRECTORY / 'parity_balancing_spin44_freedoms_certificate.json'
REPORT = DIRECTORY / 'parity_balancing_spin44_freedoms_report.json'
PRIME = 1000000007
RETAINED = tuple(range(27))
DELETED = tuple(range(27, 32))


def low_domains():
    return ([source.coordinate(p, L, j) for p, L, j in product(range(2), range(10), range(8))],
            [source.coordinate(r, H, q) for r, H, q in product(range(8), range(10), range(2))])


def parse_full(exported):
    restrictions = exported.get('restrictions')
    if not isinstance(restrictions, list) or len(restrictions) != 2:
        raise ArithmeticError('The published two-source export is required')
    item = restrictions[1]
    if item.get('source') != [8, 8] or item.get('target') != [3, 3, 32]:
        raise ArithmeticError('The balanced32 source or target changed')
    parsed = [source.parse(item['maps'][name], (rows, 960))
              for name, rows in zip('XYZ', (9, 96, 96))]
    maps, denominators = [a for a, d in parsed], [d for a, d in parsed]
    domains = low_domains()
    if any(c not in set(domains[leg-1]) for leg in (1, 2) for _, c, _ in maps[leg]):
        raise ArithmeticError('An exported second or third map leaves its low domain')
    return maps, denominators


def low_responses(maps):
    """Return actual low-coordinate responses against all32 channels."""
    inv = [source.inverse(m) for m in maps]
    domains = [set(v) for v in low_domains()]
    answers = [defaultdict(Counter), defaultdict(Counter)]
    for x, y, z in source.source(8, 8):
        xx = inv[0].get(x, ())
        if not xx:
            continue
        if y in domains[0]:
            for (tx, vx), (tz, vz) in product(xx, inv[2].get(z, ())):
                answers[0][y][96*tx+tz] += vx*vz
        if z in domains[1]:
            for (tx, vx), (ty, vy) in product(xx, inv[1].get(y, ())):
                answers[1][z][96*tx+ty] += vx*vy
    return [{c: {k: v for k, v in row.items() if v}
             for c, row in answer.items() if any(row.values())} for answer in answers]


def trim_response(response):
    answer = {}
    for c, row in response.items():
        values = {}
        for output, value in row.items():
            first, opposite = divmod(output, 96)
            vertex, channel = divmod(opposite, 32)
            if channel < 27:
                values[81*first+27*vertex+channel] = value
        if values:
            answer[c] = values
    return answer


def select_rows(entries, channels):
    channels = list(channels)
    if not source.distinct_indices(channels, 32):
        raise ArithmeticError('The selected channel list is malformed')
    lookup = {channel: index for index, channel in enumerate(channels)}
    selected = []
    for row, column, value in entries:
        vertex, channel = divmod(row, 32)
        if channel in lookup:
            selected.append((len(channels)*vertex+lookup[channel], column, value))
    return selected


def omitted_rows(entries, domain):
    rows = [Counter() for _ in range(15)]
    allowed = set(domain)
    for row, column, value in entries:
        vertex, channel = divmod(row, 32)
        if channel >= 27:
            if column not in allowed:
                raise ArithmeticError('An omitted row leaves the literal low domain')
            rows[5*vertex+channel-27][column] += value
    return [dict(v) for v in rows]


def check_minor(response, record, domain, rank, width):
    rows, columns = record.get('rows'), record.get('columns')
    if (record.get('prime') != PRIME or record.get('rank') != rank
            or not source.distinct_indices(rows, 960)
            or not source.distinct_indices(columns, width)
            or len(rows) != rank or len(columns) != rank
            or any(c not in set(domain) for c in rows)):
        raise ArithmeticError('A response minor has incorrect coordinates or dimensions')
    matrix = [[response.get(c, {}).get(k, 0) for k in columns] for c in rows]
    if source.modular_rank(matrix, PRIME) != rank:
        raise ArithmeticError('An actual response minor is singular')


def check_deleted_kernel(response, rows, domain):
    if len(rows) != 15 or len(domain) != 160:
        raise ArithmeticError('The complete omitted-row kernel needs15 vectors in160 coordinates')
    allowed = set(domain)
    dense = []
    for row in rows:
        if (not isinstance(row, dict) or any(c not in allowed or type(v) is not int or not v
                                            for c, v in row.items())):
            raise ArithmeticError('An omitted-row kernel vector is malformed')
        total = Counter()
        for c, value in row.items():
            for output, coefficient in response.get(c, {}).items():
                total[output] += value*coefficient
        if any(total.values()):
            raise ArithmeticError('An omitted row has a nonzero exact retained response')
        dense.append([row.get(c, 0) for c in domain])
    if source.modular_rank(dense, PRIME) != 15:
        raise ArithmeticError('The fifteen actual omitted rows are dependent')


def graph_entries(entries):
    if not isinstance(entries, list):
        raise ArithmeticError('A graph must be an explicit sparse list')
    seen = set()
    result = []
    for entry in entries:
        if (not isinstance(entry, (list, tuple)) or len(entry) != 4
                or any(type(v) is not int for v in entry)):
            raise ArithmeticError('Graph entries must be four integers')
        row, vertex, channel, value = entry
        if not 0 <= row < 81 or not 0 <= vertex < 3 or not 0 <= channel < 5 or not value:
            raise ArithmeticError('A graph entry has an invalid index or zero coefficient')
        key = row, vertex, channel
        if key in seen:
            raise ArithmeticError('Duplicate graph coordinate')
        seen.add(key)
        result.append((row, vertex, channel, value))
    return result


def graph_residual(a, b):
    answer = Counter()
    for row, J, d, value in graph_entries(a):
        for column, I, e, coefficient in graph_entries(b):
            if d == e:
                answer[3*I+J, row, column] += value*coefficient
    return {point: value for point, value in answer.items() if value}


def apply_graph(maps, a, b):
    result = [maps[0][:]]
    domains = low_domains()
    for leg, entries in ((1, a), (2, b)):
        changed = Counter({(r, c): v for r, c, v in select_rows(maps[leg], RETAINED)})
        deleted = omitted_rows(maps[leg], domains[leg-1])
        for row, vertex, channel, coefficient in graph_entries(entries):
            for column, value in deleted[5*vertex+channel].items():
                changed[row, column] += coefficient*value
        result.append([(r, c, v) for (r, c), v in sorted(changed.items()) if v])
    return result


def positive_graph():
    # Both maps change on every retained row. The omitted outer label varies
    # with the channel, so these are not merely common middle-basis changes.
    a, b = [], []
    for row in range(81):
        vertex, channel = divmod(row, 27)
        a.append([row, (vertex+channel+1) % 3, channel % 2, 1 if channel % 2 else -1])
        b.append([row, (vertex+2*channel+1) % 3, 2+channel % 3, 1 if channel % 2 else -1])
    return a, b


def verify(certificate=None, exported=None):
    certificate = json.loads(CERTIFICATE.read_text()) if certificate is None else certificate
    exported = json.loads(MAPS.read_text()) if exported is None else exported
    if (certificate.get('claim_id') != 'AI-BALANCED-SPIN-FREEDOMS-120'
            or certificate.get('new_exponent_established') is not False
            or certificate.get('retained_channels') != list(RETAINED)
            or certificate.get('deleted_channels') != list(DELETED)):
        raise ArithmeticError('The retained channels or claim scope changed')
    maps, denominators = parse_full(exported)
    full_replay = source.full_contraction(source.source(8, 8), maps, denominators, 32)
    responses, domains = low_responses(maps), low_domains()
    ranks = {}
    for leg, name in ((1, 'Y'), (2, 'Z')):
        response, domain = responses[leg-1], domains[leg-1]
        if not set(response) <= set(domain) or len(domain) != 160:
            raise ArithmeticError('The literal low domain differs')
        check_minor(response, certificate['ranks'][name]['full'], domain, 160, 864)
        trimmed = trim_response(response)
        check_minor(trimmed, certificate['ranks'][name]['trimmed'], domain, 145, 729)
        rows = omitted_rows(maps[leg], domain)
        check_deleted_kernel(trimmed, rows, domain)
        actual_support = len({c for _, c, _ in select_rows(maps[leg], RETAINED)})
        ranks[name] = {'literal_low_domain_dimension': 160,
                       'all32_exact_response_rank': 160, 'all32_common_fiber_dimension': 0,
                       'retained27_exact_response_rank': 145,
                       'retained27_exact_kernel_dimension': 15,
                       'kernel_basis_is_exactly_actual_omitted_rows': True,
                       'retained_map_nonzero_coordinate_support': actual_support}
    a, b = positive_graph()
    if graph_residual(a, b):
        raise ArithmeticError('The disjoint-channel positive graph has a residual')
    changed = apply_graph(maps, a, b)
    graph_replay = source.full_contraction(source.source(8, 8), changed, denominators, 27)
    for leg in (1, 2):
        original = defaultdict(dict)
        modified = defaultdict(dict)
        for r, c, v in select_rows(maps[leg], RETAINED): original[r][c] = v
        for r, c, v in changed[leg]: modified[r][c] = v
        if any(original[r] == modified[r] for r in range(81)):
            raise ArithmeticError('The positive graph must change every retained row on both legs')
    bad_a, bad_b = [[1, 1, 0, 1]], [[2, 2, 0, 1]]
    if graph_residual(bad_a, bad_b) != {(7, 1, 2): 1}:
        raise ArithmeticError('The overlapping-channel negative control changed')
    bad_maps = apply_graph(maps, bad_a, bad_b)
    rejected = False
    try:
        source.full_contraction(source.source(8, 8), bad_maps, denominators, 27)
    except ArithmeticError:
        rejected = True
    if not rejected:
        raise ArithmeticError('Full source replay accepted the nonzero graph residual')
    return {'claim_id': 'AI-BALANCED-SPIN-FREEDOMS-120',
            'source': [8, 8], 'original_target': [3, 3, 32], 'retained_target': [3, 3, 27],
            'map_denominators': denominators, 'full_source_replay': full_replay,
            'low_coordinate_freedoms': ranks,
            'graph_condition': 'A_J B_I^T = 0 for every I,J; only individually neutral low-coordinate graphs',
            'positive_graph_changed_rows_each_leg': 81,
            'positive_graph_full_source_replay': graph_replay,
            'nonzero_graph_residual_rejected_by_full_source_replay': True,
            'reconstruction': 'Recomputed from the published116 maps after filesystem rollback',
            'external_independent_review': False, 'larger_square_constructed': False,
            'new_exponent_established': False}


if __name__ == '__main__':
    report = verify()
    REPORT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
