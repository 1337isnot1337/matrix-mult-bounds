"""Coupled exact repairs of split-cover pair-injective lifts, with a time budget."""
import argparse
import gzip
from itertools import combinations, product
import json
from pathlib import Path
import time

from ideal import ROOT, verify
from split_source import split_data
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas
from search import potential_or_circuit


def run(output, seconds):
    G, Q, _ = split_data()
    M, inv = G['mul'], G['inv']
    difference = [[min(M[g][inv[h]], inv[M[g][inv[h]]]) for h in range(120)]
                  for g in range(120)]

    def classes(points):
        return {difference[g][h] for g, h in combinations(points, 2)}

    record = next(r for r in json.loads((ROOT/'results/subgroup-ideal-2026-10-21/certificates.json').read_text())['records']
                  if r['group'] == G['name'])
    verify(G, record)
    cosets = record['cosets']
    cosets = [sum(1 << g for g in C) for C in cosets]
    parent = ROOT/'results/sl2-five-native-2026-10-20/split-full-capacity-10.cuts.jsonl.gz'
    items = [json.loads(line) for line in gzip.decompress(parent.read_bytes()).splitlines()]
    seeds = [r['sets'] for r in items if r['type'] == 'exact-farkas']
    report = {'group': G['name'], 'seed_lifts': len(seeds), 'maximum_total_removals': 4,
              'maximum_removals_per_leg': 2, 'identity_points_fixed': True,
              'removal_patterns': 0, 'backtracking_nodes': 0, 'coset_free_pair_models': 0,
              'exact_farkas_cuts': 0, 'witness': None, 'exponent_improvement': False,
              'scope': 'Bounded local coupled repair, not a global exclusion.'}
    output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    seen, started = set(), time.monotonic()

    def stopped():
        return report['witness'] is not None or time.monotonic()-started > seconds

    def visit(points, used, masks, need, last):
        if stopped():
            return
        report['backtracking_nodes'] += 1
        if not any(need):
            candidate = [sorted(row) for row in points]
            key = tuple(map(tuple, candidate))
            if key in seen:
                return
            seen.add(key)
            for f in range(3):
                pair_map(G, candidate[f], candidate[(f+1) % 3])
            report['coset_free_pair_models'] += 1
            relations, _ = extra_relations(G, candidate)
            answer = potential_or_circuit(relations, 30)
            if 'potentials' in answer:
                report['witness'] = {'sets': candidate, 'potentials': answer['potentials'],
                    'verification': verify_witness(G, candidate, answer['potentials'])}
                return
            if not verify_farkas(relations, answer['indices'], answer['weights']):
                raise ArithmeticError('invalid exact repair circuit')
            with cut_path.open('a') as stream:
                stream.write(json.dumps({'sets': candidate, 'relation_vertices':
                    [relations[i]['vertices'] for i in answer['indices']],
                    'weights': answer['weights']}, separators=(',', ':'))+'\n')
            report['exact_farkas_cuts'] += 1
            return
        choices = []
        for f in range(3):
            if not need[f]:
                continue
            occupied = {Q['projection'][g] for g in points[f]}
            forbidden = used[(f+1) % 3] | used[(f+2) % 3]
            allowed = []
            for g in range(last[f]+1, 120):
                if Q['projection'][g] in occupied:
                    continue
                if any(difference[g][h] in forbidden for h in points[f]):
                    continue
                new_mask = masks[f] | (1 << g)
                if any(new_mask & C == C for C in cosets):
                    continue
                allowed.append(g)
            if len(allowed) < need[f]:
                return
            choices.append((len(allowed), f, allowed))
        _, f, allowed = min(choices)
        old_used, old_mask, old_last = used[f], masks[f], last[f]
        need[f] -= 1
        for g in allowed:
            used[f] = old_used | {difference[g][h] for h in points[f]}
            points[f].append(g)
            masks[f], last[f] = old_mask | (1 << g), g
            visit(points, used, masks, need, last)
            points[f].pop()
            if stopped():
                break
        used[f], masks[f], last[f] = old_used, old_mask, old_last
        need[f] += 1

    for seed in seeds:
        options = []
        for S in seed:
            mask = sum(1 << g for g in S)
            full = [C for C in cosets if mask & C == C]
            leg = {}
            for width in range(3):
                leg[width] = []
                for removed in combinations([g for g in S if g], width):
                    removed_mask = sum(1 << g for g in removed)
                    if all(C & removed_mask for C in full):
                        leg[width].append(removed)
            options.append(leg)
        for counts in sorted(product(range(3), repeat=3), key=lambda row: (sum(row), row)):
            if not 1 <= sum(counts) <= 4:
                continue
            for removed in product(*(options[f][counts[f]] for f in range(3))):
                points = [sorted(set(seed[f])-set(removed[f])) for f in range(3)]
                report['removal_patterns'] += 1
                visit(points, [classes(S) for S in points],
                      [sum(1 << g for g in S) for S in points], list(counts), [-1]*3)
                if stopped():
                    break
            if stopped():
                break
        if stopped():
            break
    report['elapsed_seconds'] = time.monotonic()-started
    report['status'] = ('exact-target-witness' if report['witness'] else
                        'time-limit' if report['elapsed_seconds'] > seconds else
                        'completed-local-neighborhood')
    output.write_text(json.dumps(report, indent=2)+'\n')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=120)
    args = parser.parse_args()
    print(json.dumps(run(args.output, args.seconds)))
