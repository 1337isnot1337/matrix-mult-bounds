"""Exact one/two-point mutations of the known split-cover pair-injective lifts."""
import argparse
import gzip
from itertools import combinations
import json
from pathlib import Path
import time

from ideal import ROOT, verify
from split_source import split_data
from group_exact import pair_map, extra_relations, verify_farkas, verify_witness
from search import potential_or_circuit


def classes(G, points):
    output = set()
    for a, b in combinations(points, 2):
        q = G['mul'][a][G['inv'][b]]
        output.add(min(q, G['inv'][q]))
    return output


def run(output, seconds):
    G, Q, _ = split_data()
    path = ROOT/'results/subgroup-ideal-2026-10-21/certificates.json'
    record = next(r for r in json.loads(path.read_text())['records'] if r['group'] == G['name'])
    verify(G, record)
    cosets = list(map(set, record['cosets']))
    parent = ROOT/'results/sl2-five-native-2026-10-20/split-full-capacity-10.cuts.jsonl.gz'
    seeds = [json.loads(line)['sets'] for line in gzip.decompress(parent.read_bytes()).splitlines()
             if json.loads(line)['type'] == 'exact-farkas']
    output.parent.mkdir(parents=True, exist_ok=True)
    cuts = output.with_suffix('.cuts.jsonl')
    cuts.write_text('')
    report = {'group': G['name'], 'seed_lifts': len(seeds), 'maximum_changed_points': 2,
              'pair_injective_neighbors': 0, 'coset_free_neighbors': 0,
              'exact_farkas_cuts': 0, 'witness': None, 'exponent_improvement': False,
              'scope': 'One- or two-point changes with identity fixed, changing one leg '
                       'whose unchanged legs contain no forbidden coset; no global exclusion.'}
    started, seen = time.monotonic(), set()
    for seed_index, seed in enumerate(seeds):
        for f in range(3):
            if any(C <= set(seed[h]) for h in range(3) if h != f for C in cosets):
                continue
            forbidden = classes(G, seed[(f+1) % 3]) | classes(G, seed[(f+2) % 3])
            for width in (1, 2):
                for removed in combinations([g for g in seed[f] if g], width):
                    kept = sorted(set(seed[f])-set(removed))
                    occupied = {Q['projection'][g] for g in kept}
                    allowed = []
                    for g in range(120):
                        if Q['projection'][g] in occupied:
                            continue
                        if all(min(G['mul'][g][G['inv'][h]],
                                   G['inv'][G['mul'][g][G['inv'][h]]]) not in forbidden for h in kept):
                            allowed.append(g)
                    for inserted in combinations(allowed, width):
                        if time.monotonic()-started > seconds:
                            report['status'] = 'time-limit'
                            break
                        if len({Q['projection'][g] for g in inserted}) != width:
                            continue
                        changed = sorted(kept+list(inserted))
                        key = seed_index, f, tuple(changed)
                        if key in seen or changed == sorted(seed[f]) or classes(G, changed) & forbidden:
                            continue
                        seen.add(key)
                        candidate = [list(s) for s in seed]
                        candidate[f] = changed
                        for h in range(3):
                            pair_map(G, candidate[h], candidate[(h+1) % 3])
                        report['pair_injective_neighbors'] += 1
                        if any(C <= set(S) for S in candidate for C in cosets):
                            continue
                        report['coset_free_neighbors'] += 1
                        relations, _ = extra_relations(G, candidate)
                        answer = potential_or_circuit(relations, 30)
                        if 'potentials' in answer:
                            report['witness'] = {'sets': candidate, 'potentials': answer['potentials'],
                                'verification': verify_witness(G, candidate, answer['potentials'])}
                            report['status'] = 'exact-target-witness'
                            break
                        if not verify_farkas(relations, answer['indices'], answer['weights']):
                            raise ArithmeticError('invalid mutation Farkas circuit')
                        with cuts.open('a') as stream:
                            stream.write(json.dumps({'sets': candidate, 'relation_vertices':
                                [relations[i]['vertices'] for i in answer['indices']],
                                'weights': answer['weights']}, separators=(',', ':'))+'\n')
                        report['exact_farkas_cuts'] += 1
                    if 'status' in report:
                        break
                if 'status' in report:
                    break
            if 'status' in report:
                break
        if 'status' in report:
            break
    report.setdefault('status', 'completed-finite-neighborhood')
    report['elapsed_seconds'] = time.monotonic()-started
    output.write_text(json.dumps(report, indent=2)+'\n')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=120)
    args = parser.parse_args()
    print(json.dumps(run(args.output, args.seconds)))
