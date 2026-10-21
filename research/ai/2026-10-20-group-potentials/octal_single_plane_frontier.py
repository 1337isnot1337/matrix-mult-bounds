"""Complete local packing filter for one changing plane in a fixed F8 base.

All offsets are relaxed independently for each pair quotient. A failure is
therefore necessary, while passing this filter is not a global construction.
Short directions and the other fourteen three-point planes remain fixed.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import time

from mask_packing import exact_pack
from octal_group import fm, inverse, scale


def point_cells(base):
    return [{a: [0, *base[2*f:2*f+2]] if a < 6 else [0, base[2*f]]
             for a in range(1, 8)} for f in range(3)]


def pair_options(cells, f, g, q):
    rows = []
    for a in range(1, 8):
        b = fm(a, q)
        left, right = cells[f][a], cells[g][b]
        points = {scale(inverse(a), x ^ y) for x in left for y in right}
        if len(points) != len(left)*len(right):
            return None
        rows.append(sorted({sum(1 << (shift ^ v) for v in points)
                            for shift in range(64)}))
    return rows


def graph_planes(base, family):
    complement = [v for j, v in enumerate(base) if j // 2 != family]
    values = [0]
    for v in complement:
        values += [x ^ v for x in values]
    for x, y in product(values, repeat=2):
        if x or y:
            yield [0, base[2*family] ^ x, base[2*family+1] ^ y]


def run(base):
    started = time.monotonic()
    records = []
    nodes = 0
    for family in range(3):
        pairs = [(f, g) for f, g in [(0, 1), (1, 2), (2, 0)]
                 if family in (f, g)]
        for scalar in range(2, 6):
            tested = 0
            rejected = {}
            survivors = []
            for plane in graph_planes(base, family):
                tested += 1
                cells = point_cells(base)
                cells[family][scalar] = plane
                receipts = []
                for f, g in pairs:
                    for q in range(1, 8):
                        options = pair_options(cells, f, g, q)
                        packed = exact_pack(options) if options is not None else None
                        if packed is not None:
                            nodes += packed['search_counts']['nodes']
                        if packed is None or not packed['satisfiable']:
                            key = f'{f},{g},q={q}'
                            rejected[key] = rejected.get(key, 0) + 1
                            break
                        receipts.append({'pair': [f, g], 'quotient': q,
                                         'selected_masks': packed['selected_masks']})
                    else:
                        continue
                    break
                else:
                    survivors.append({'points': plane, 'pair_packings': receipts})
            if tested != 255 or sum(rejected.values()) + len(survivors) != tested:
                raise ArithmeticError('incomplete graph-plane coverage')
            records.append({'family': family, 'scalar': scalar,
                            'planes_checked': tested, 'first_failure_counts': rejected,
                            'survivors': survivors})
    return {'group': 'F8^2:C7', 'base_columns': base,
            'only_one_three_point_plane_varies': True,
            'short_directions_fixed': True, 'records': records,
            'planes_checked': sum(x['planes_checked'] for x in records),
            'surviving_planes': sum(len(x['survivors']) for x in records),
            'search_nodes': nodes, 'elapsed_seconds': time.monotonic()-started,
            'scope': __doc__, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-report', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = json.loads(args.base_report.read_text())['base_columns']
    result = run(base)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))
