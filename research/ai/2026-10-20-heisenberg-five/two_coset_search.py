"""Finite Heisenberg two-left-coset construction search, with integer acceptance."""
import argparse
from itertools import combinations_with_replacement
import json
from pathlib import Path
import sys
import time

from source import group, two_coset_sets, quotients, source_gate, RESEARCH
sys.path.insert(0, str(RESEARCH/'2026-10-20-sl2-seven/imported'))
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas
from search import potential_or_circuit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=300)
    args = parser.parse_args()
    G = group()
    index = {g: i for i, g in enumerate(G['matrices'])}
    first = tuple(sorted(index[a, b, 0] for a in range(5) for b in (0, 1)))
    candidates, count = two_coset_sets(G)
    if first not in candidates:
        raise ArithmeticError('standard first set missing')
    Q0 = quotients(G, first)
    eligible = [(S, quotients(G, S)) for S in candidates if not Q0 & quotients(G, S)]
    report = {'group': G['name'], 'shape': [10]*3, 'source': source_gate(),
        'noncentral_cyclic_subgroups': count, 'two_coset_sets': len(candidates),
        'first_set': first, 'first_quotients': len(Q0),
        'eligible_other_sets': len(eligible), 'seconds_limit': args.seconds,
        'pairs_checked': 0, 'pair_injective_triples': 0, 'exact_farkas_cuts': 0,
        'status': 'running', 'witness': None, 'exponent_improvement': False,
        'scope': 'Finite two-left-coset ansatz with the stated fixed first set; '
                 'no arbitrary-degeneration exclusion.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = args.output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    started = time.monotonic()

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.output)

    checkpoint()
    for (T, QT), (U, QU) in combinations_with_replacement(eligible, 2):
        if time.monotonic()-started >= args.seconds:
            report['status'] = 'time-limit'
            break
        report['pairs_checked'] += 1
        if QT & QU:
            continue
        sets = [list(first), list(T), list(U)]
        for f in range(3):
            pair_map(G, sets[f], sets[(f+1) % 3])
        report['pair_injective_triples'] += 1
        relations, _ = extra_relations(G, sets)
        answer = potential_or_circuit(relations, 30)
        if 'potentials' in answer:
            report['witness'] = {'sets': sets, 'potentials': answer['potentials'],
                'verification': verify_witness(G, sets, answer['potentials'])}
            report['status'] = 'exact-target-witness'
            checkpoint()
            break
        if not verify_farkas(relations, answer['indices'], answer['weights']):
            raise ArithmeticError('invalid circuit')
        record = {'sets': sets, 'relation_vertices':
                  [relations[i]['vertices'] for i in answer['indices']], 'weights': answer['weights']}
        with cut_path.open('a') as stream:
            stream.write(json.dumps(record, separators=(',', ':'))+'\n')
        report['exact_farkas_cuts'] += 1
        if report['pair_injective_triples'] % 50 == 0:
            checkpoint()
            print(json.dumps({k: report[k] for k in
                              ('pair_injective_triples', 'exact_farkas_cuts', 'elapsed_seconds')}), flush=True)
    else:
        report['status'] = 'finite-fixed-first-class-exhausted'
    checkpoint()
    print(json.dumps({k: v for k, v in report.items() if k not in ('source', 'witness')}), flush=True)


if __name__ == '__main__':
    main()
