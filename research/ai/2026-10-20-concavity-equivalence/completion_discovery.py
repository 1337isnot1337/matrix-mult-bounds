"""Floating beam discovery for the external September completion recurrences.

Only exact integer replay can certify an exponent consequence.
"""
import argparse
import json
import math
from pathlib import Path


def log_updated(center, other, m):
    difference = other-center
    if difference < -700:
        return (m-1)*center+other+math.log(m)
    if difference <= 0:
        return m*center+math.log(math.expm1(m*math.log1p(math.exp(difference))))
    s = difference+math.log1p(math.exp(-difference))
    return m*(center+s)+math.log1p(-math.exp(-m*s))


def score(logs, factors, rank):
    top = sorted(logs)[-2:]
    return 3*factors*math.log(rank)/(top[1]+math.log1p(math.exp(top[0]-top[1])))


def beam(rank, depth, width, sizes):
    initial = (0., 0., 0.) if rank == 2 else (0., math.log(2), math.log(2))
    states = [(initial, 1, [])]
    best = (score(initial, 1, rank), states[0])
    history = []
    for level in range(depth):
        pool = {}
        for logs, factors, recipe in states:
            for center in range(3):
                if center and logs[center] == logs[center-1]:
                    continue
                for m in sizes:
                    updated = tuple(sorted(m*logs[i] if i == center
                        else log_updated(logs[center], logs[i], m) for i in range(3)))
                    count = m*factors
                    rec = recipe+[[center, m]]
                    # Retain b in the key: entropy gains depend on the absolute scale.
                    key = (count, *(round(x/count, 13) for x in updated))
                    value = score(updated, count, rank)
                    previous = pool.get(key)
                    if previous is None or value < previous[0]:
                        pool[key] = (value, (updated, count, rec))
        selected = sorted(pool.values(), key=lambda item: item[0])[:width]
        if selected[0][0] < best[0]:
            best = selected[0]
        history.append({'depth': level+1, 'unique_pool': len(pool),
                        'best_descriptive_exponent': selected[0][0]})
        print(rank, level+1, selected[0][0], 'b=', selected[0][1][1], flush=True)
        states = [state for _, state in selected]
    return {'rank': rank, 'best_descriptive_exponent': best[0],
            'factors': best[1][1], 'recipe': best[1][2], 'history': history,
            'status': 'floating discovery only; exact integer replay required'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--depth', type=int, default=15)
    parser.add_argument('--width', type=int, default=4000)
    parser.add_argument('--sizes', type=int, nargs='+', default=[2, 3])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    reports = []
    for rank in (2, 3):
        reports.append(beam(rank, args.depth, args.width, args.sizes))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(reports, indent=2)+'\n')


if __name__ == '__main__':
    main()
