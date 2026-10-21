"""Finite cyclic low/high section parents, with exact witness/circuit acceptance."""
import argparse
from itertools import product
import json
from pathlib import Path
import sys
import time

from source_data import group, subgroup_certificate, SEVEN
sys.path.insert(0, str(SEVEN/'imported'))
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas


def enumerate_sections(G, certificate):
    M, inv = G['mul'], G['inv']
    center, H0 = certificate['center'], certificate['members']
    conjugates = sorted({tuple(sorted(M[M[g][h]][inv[g]] for h in H0))
                         for g in range(240)})
    if len(conjugates) != 5:
        raise ArithmeticError('expected five normalization subgroups')
    H = [set(h) for h in conjugates[:3]]
    K = [set(g for g in H[i] & H[(i+1) % 3] if M[M[g][g]][g] == 0)
         for i in range(3)]
    if any(len(k) != 3 for k in K):
        raise ArithmeticError('expected order-three intersection subgroups')
    rows, summaries = [], []
    for i in range(3):
        outgoing, incoming = K[i], K[(i-1) % 3]
        preimage = {M[k][z] for k in outgoing for z in center}
        blocks = sorted({tuple(sorted(M[l][r] for l in preimage)) for r in H[i]})
        if len(blocks) != 4:
            raise ArithmeticError('wrong section blocks')
        representatives = [min(b) for b in blocks]
        candidates, closure_counts = set(), {}
        for choices in product(center, repeat=3):
            closure = {M[k][M[z][r]] for k in outgoing
                       for z, r in zip((0,)+choices, representatives)}
            incoming_cosets = {tuple(sorted(M[k][s] for k in incoming)) for s in closure}
            high_max = len(incoming_cosets)
            closure_counts[high_max] = closure_counts.get(high_max, 0)+1
            if high_max != 10:
                continue
            groups = [sorted(closure & set(c)) for c in sorted(incoming_cosets)]
            for selected in product(*groups):
                canonical = min(tuple(sorted(M[s][inv[p]] for s in selected)) for p in selected)
                candidates.add(canonical)
        for selected in candidates:
            quotients = {M[x][inv[y]] for x in selected for y in selected}
            if (len(selected) != 10 or quotients & (incoming-{0}) or
                    quotients & preimage != outgoing):
                raise ArithmeticError('wrong low/high section')
        rows.append(sorted(candidates))
        summaries.append({'leg': i, 'closures': 64, 'high_max_histogram': closure_counts,
                          'canonical_ten_point_sections': len(candidates)})
    return rows, {'conjugate_subgroups': [list(h) for h in conjugates],
                  'outgoing_order_three': [sorted(k) for k in K], 'section_summaries': summaries}


def main():
    from search import potential_or_circuit
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--max-triples', type=int, default=1000)
    args = parser.parse_args()
    G = group()
    choices, enumeration = enumerate_sections(G, subgroup_certificate(G))
    total = len(choices[0])*len(choices[1])*len(choices[2])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cuts_path = args.output.with_suffix('.cuts.jsonl')
    cuts_path.write_text('')
    started = time.monotonic()
    report = {'group': G['name'], 'shape': [10, 10, 10], 'enumeration': enumeration,
              'canonical_triples': total, 'tested': 0, 'exact_cuts': 0,
              'status': 'running', 'witness': None, 'exponent_improvement': False,
              'scope': 'Structured ten-point parents. No unrestricted degeneration exclusion.'}

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.output)

    checkpoint()
    for triple in product(*choices):
        if report['tested'] >= args.max_triples:
            break
        sets = list(map(list, triple))
        for f in range(3):
            pair_map(G, sets[f], sets[(f+1) % 3])
        relations, _ = extra_relations(G, sets)
        answer = potential_or_circuit(relations, 30)
        report['tested'] += 1
        if 'potentials' in answer:
            report['witness'] = {'sets': sets, 'potentials': answer['potentials'],
                                 'verification': verify_witness(G, sets, answer['potentials'])}
            report['status'] = 'exact-parent-witness; not the improving target'
            break
        if not verify_farkas(relations, answer['indices'], answer['weights']):
            raise ArithmeticError('invalid parent rejection')
        item = {'sets': sets, 'relation_vertices': [relations[j]['vertices']
                                                  for j in answer['indices']],
                'weights': answer['weights']}
        with cuts_path.open('a') as stream:
            stream.write(json.dumps(item, separators=(',', ':'))+'\n')
        report['exact_cuts'] += 1
        if report['tested'] % 50 == 0:
            checkpoint()
            print(json.dumps({'tested': report['tested'], 'total': total}), flush=True)
    if report['status'] == 'running':
        report['status'] = ('all-canonical-triples-rejected' if report['tested'] == total
                            else 'triple-budget; incomplete parent class')
    checkpoint()
    print(json.dumps({'status': report['status'], 'tested': report['tested'],
                      'exact_cuts': report['exact_cuts']}), flush=True)


if __name__ == '__main__':
    main()
