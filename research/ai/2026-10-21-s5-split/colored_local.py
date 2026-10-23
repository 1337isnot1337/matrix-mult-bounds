"""Heat-bath discovery on actual colored points; exact acceptance only."""
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from four_colors import data
from group_exact import pair_map, extra_relations, verify_farkas, verify_witness
from search import potential_or_circuit
from verify_projected_reports import verify_farkas_record


def run(output, seconds, seed, shape=(18, 18, 20), data_provider=data,
        warm_path=None, amplitude=0.6, use_trades=False, trade_multiplicity=False):
    G, Q, receipt = data_provider(shape)
    if receipt['conditional_gate']['strict_positive_margin_numerator'] <= 0:
        raise ValueError('target must pass the improving conditional gate')
    rng = np.random.default_rng(seed)
    table = np.array(G['mul'], dtype=np.int16)
    inverse = np.array(G['inv'], dtype=np.int16)
    candidates = np.arange(480)
    sets = [np.r_[0, 4*rng.choice(np.arange(1, 120), n-1, replace=False)
                  +rng.integers(0, 4, n-1)].astype(np.int16) for n in shape]
    if warm_path is not None:
        warm = json.loads(warm_path.read_text())
        sets = [np.array(S, dtype=np.int16) for S in warm['best_sets']]
        if (list(map(len, sets)) != list(shape) or any(S[0] != 0 or len(set(S//4)) != len(S)
                or np.any(S < 0) or np.any(S >= 480) for S in sets)):
            raise ValueError('invalid warm-start point sets')

    def histogram():
        return np.array([np.bincount(table[inverse[S][:, None], T[None, :]].ravel(), minlength=480)
                         for S, T in zip(sets, sets[1:]+sets[:1])])

    def owner_histogram():
        rows = []
        for S in sets:
            labels = table[S[:, None], inverse[S][None, :]][np.triu_indices(len(S), 1)]
            rows.append(np.bincount(np.minimum(labels, inverse[labels]), minlength=480))
        return np.array(rows)

    if use_trades:
        from commuting_trades import templates
        trades = np.array(templates(G), dtype=np.int16)
        owners = owner_histogram()

    def trade_energy(hist):
        if trade_multiplicity:
            return int(np.prod(hist[np.arange(3), trades], axis=1).sum())
        return int(np.all(hist[np.arange(3), trades] > 0, axis=1).sum())

    counts = histogram()
    current = int((counts*(counts-1)).sum()//2)
    if use_trades:
        current = 20*current+trade_energy(owners)
    report = {'group': G['name'], 'shape': list(shape), 'source_and_normalization': receipt,
        'method': 'Actual colored-point heat-bath pair-collision search',
        'normalizations_used': 'Identity and one point per central fiber in each sampled vertex set',
        'seed': seed, 'seconds_limit': seconds, 'steps': 0, 'minimum_energy': current,
        'temperature': {'floor': 0.04, 'amplitude': amplitude, 'period_steps': 20000},
        'best_sets': [S.tolist() for S in sets], 'pair_injective_models': 0,
        'repeated_pair_models': 0, 'exact_farkas_cuts': 0, 'exact_histogram_checks': 0,
        'status': 'running', 'witness': None, 'exponent_improvement': False,
        'scope': 'Bounded floating-guided discovery; actual witnesses and Farkas circuits use exact integers.'}
    if use_trades:
        report['objective'] = {'pair_collision_weight': 20, 'commuting_trade_weight': 1,
                               'actual_group_templates': len(trades),
                               'owner_edge_multiplicities': trade_multiplicity}
    if warm_path is not None:
        report['warm_start'] = {'path': str(warm_path),
            'sha256': hashlib.sha256(warm_path.read_bytes()).hexdigest(),
            'source_group': warm['group'],
            'transport': 'Copied point indices; recomputed all pair histograms in the current group.'}
    output.parent.mkdir(parents=True, exist_ok=True)
    cuts = output.with_suffix('.cuts.jsonl')
    cuts.write_text('')
    seen = set()
    started = time.monotonic()

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        report['current_energy'] = current
        # Check the incremental discovery objective by independent full counting.
        actual = histogram()
        expected = int((actual*(actual-1)).sum()//2)
        if use_trades:
            if not np.array_equal(owners, owner_histogram()):
                raise ArithmeticError('incremental owner histogram drift')
            report['pair_collision_energy'] = expected
            report['commuting_trade_energy'] = trade_energy(owners)
            expected = 20*expected+report['commuting_trade_energy']
        if not np.array_equal(counts, actual) or expected != current:
            raise ArithmeticError('incremental pair histogram drift')
        report['exact_histogram_checks'] += 1
        temporary = output.with_suffix('.tmp')
        temporary.write_text(json.dumps(report, indent=2)+'\n')
        temporary.replace(output)

    checkpoint()
    while time.monotonic()-started < seconds:
        report['steps'] += 1
        f = int(rng.integers(3))
        i = int(rng.integers(1, shape[f]))
        h, k = (f+1) % 3, (f-1) % 3
        old = int(sets[f][i])
        outgoing = table[inverse[old], sets[h]]
        incoming = table[inverse[sets[k]], old]
        removal = int(counts[f, outgoing].sum()+counts[k, incoming].sum()-len(outgoing)-len(incoming))
        counts[f, outgoing] -= 1
        counts[k, incoming] -= 1
        labels_out = table[inverse[:, None], sets[h][None, :]]
        labels_in = table[inverse[sets[k]][None, :], candidates[:, None]]
        scores = counts[f, labels_out].sum(axis=1)+counts[k, labels_in].sum(axis=1)
        if use_trades:
            if trade_multiplicity:
                products = owners[h, trades[:, h]]*owners[k, trades[:, k]]
                penalties = np.bincount(trades[:, f], weights=products, minlength=480).astype(np.int64)
            else:
                other_active = np.ones(len(trades), dtype=bool)
                for family in (h, k):
                    other_active &= owners[family, trades[:, family]] > 0
                penalties = np.bincount(trades[other_active, f], minlength=480)
            neighbors = np.delete(sets[f], i)
            old_labels = table[old, inverse[neighbors]]
            removed = np.bincount(np.minimum(old_labels, inverse[old_labels]), minlength=480)
            trade_removal = (int(penalties @ removed) if trade_multiplicity else
                            int(penalties[(owners[f] > 0) & (owners[f] == removed)].sum()))
            owners[f] -= removed
            labels = table[candidates[:, None], inverse[neighbors][None, :]]
            labels = np.minimum(labels, inverse[labels])
            if trade_multiplicity:
                additions = penalties[labels].sum(axis=1)
            else:
                labels = np.sort(labels, axis=1)
                unique = np.c_[np.ones(480, dtype=bool), labels[:, 1:] != labels[:, :-1]]
                additions = (penalties[labels]*unique*(owners[f, labels] == 0)).sum(axis=1)
            scores = 20*scores+additions
            removal = 20*removal+trade_removal
        occupied = set((sets[f]//4).tolist())-{old//4}
        allowed = np.array([q//4 not in occupied for q in candidates])
        minimum = scores[allowed].min()
        temperature = 0.04+amplitude*(1-(report['steps'] % 20000)/20000)
        probabilities = np.zeros(480)
        probabilities[allowed] = np.exp(-(scores[allowed]-minimum)/temperature)
        probabilities /= probabilities.sum()
        new = int(rng.choice(480, p=probabilities))
        current += int(scores[new])-removal
        sets[f][i] = new
        counts[f, table[inverse[new], sets[h]]] += 1
        counts[k, table[inverse[sets[k]], new]] += 1
        if use_trades:
            labels = table[new, inverse[neighbors]]
            owners[f] += np.bincount(np.minimum(labels, inverse[labels]), minlength=480)
        if current < report['minimum_energy']:
            report['minimum_energy'] = current
            report['best_sets'] = [S.tolist() for S in sets]
        if not current:
            lifted = [S.tolist() for S in sets]
            signature = tuple(tuple(sorted(S)) for S in lifted)
            if signature in seen:
                report['repeated_pair_models'] += 1
            else:
                seen.add(signature)
                for j in range(3):
                    pair_map(G, lifted[j], lifted[(j+1) % 3])
                report['pair_injective_models'] += 1
                relations, _ = extra_relations(G, lifted)
                answer = potential_or_circuit(relations, sum(shape))
                if 'potentials' in answer:
                    report['witness'] = {'sets': lifted, 'potentials': answer['potentials'],
                        'verification': verify_witness(G, lifted, answer['potentials'])}
                    report['status'] = 'exact-target-witness'
                    break
                if not verify_farkas(relations, answer['indices'], answer['weights']):
                    raise ArithmeticError('invalid exact Farkas result')
                support = set()
                for j in answer['indices']:
                    s, t, tt, u, uu, ss = relations[j]['vertices']
                    support.update(((0, lifted[0][s]), (0, lifted[0][ss]),
                                    (1, lifted[1][t]), (1, lifted[1][tt]),
                                    (2, lifted[2][u]), (2, lifted[2][uu])))
                item = {'type': 'exact-farkas', 'sets': lifted,
                    'relation_vertices': [relations[j]['vertices'] for j in answer['indices']],
                    'weights': answer['weights'], 'blocked_lift_points': sorted(support)}
                verify_farkas_record(G, item)
                with cuts.open('a') as stream:
                    stream.write(json.dumps(item, separators=(',', ':'))+'\n')
                report['exact_farkas_cuts'] += 1
                checkpoint()
            # Discovery-only kick. No unproved exclusion is learned.
            f = int(rng.integers(3))
            for i in rng.choice(np.arange(1, shape[f]), min(3, shape[f]-1), replace=False):
                sets[f][i] ^= int(rng.integers(1, 4))
            counts = histogram()
            current = int((counts*(counts-1)).sum()//2)
            if use_trades:
                owners = owner_histogram()
                current = 20*current+trade_energy(owners)
        if report['steps'] % 1000 == 0:
            checkpoint()
    if report['status'] == 'running':
        report['status'] = 'time-limit'
    checkpoint()
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--seed', type=int, default=2026102135)
    parser.add_argument('--shape', type=int, nargs=3, default=(18, 18, 20))
    parser.add_argument('--cyclic-center', action='store_true')
    parser.add_argument('--warm', type=Path)
    parser.add_argument('--temperature-amplitude', type=float, default=0.6)
    parser.add_argument('--commuting-trades', action='store_true')
    parser.add_argument('--trade-multiplicity', action='store_true')
    args = parser.parse_args()
    if args.cyclic_center:
        from cyclic_four import data as provider
    else:
        provider = data
    result = run(args.output, args.seconds, args.seed, args.shape, provider,
                 args.warm, args.temperature_amplitude, args.commuting_trades,
                 args.trade_multiplicity)
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_and_normalization', 'witness')}))
