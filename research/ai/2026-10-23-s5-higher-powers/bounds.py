"""Export a lower bound on coordinate covers of the S5 degree majorant."""

import argparse
from hashlib import sha256
import json
from math import comb, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PRIOR = ROOT / 'results/s5-finite-covers-2026-10-23/certificate.json'
LAYERS = [17, 9, 9, 18, 9, 9, 17]
SCOPE = 'Coordinate covers of the full separately bounded S5 degree majorant; not actual-source slice-rank lower bounds.'


def principal_prefixes(maximum):
    polynomial = [1]
    prefixes = []
    for j in range(maximum + 1):
        prefixes.append(sum(polynomial[:2*j + 1]))
        following = [0] * (len(polynomial) + 6)
        for degree, count in enumerate(polynomial):
            for d, layer in enumerate(LAYERS):
                following[degree + d] += count * layer
        polynomial = following
    return prefixes


def lower_bound(n, r, prefixes):
    return sum(comb(n, j) * 16**(n-j) * prefixes[j]
               * sum(comb(n*(r+1)-j, d)
                     for d in range((n*(r+1)-j)//3 + 1))
               for j in range(n+1))


def export():
    prior = json.loads(PRIOR.read_text())
    inputs = set(prior['source_pins']) | {
        str(PRIOR.relative_to(ROOT)),
        'research/ai/2026-10-23-s5-finite-covers/verify.py',
        'research/ai/2026-10-23-s5-finite-covers/proof.md',
    }
    prefixes = principal_prefixes(71)
    sources = []
    for r, source in zip((1, 2), prior['sources']):
        shapes = source['remaining_shapes']
        maximum = max(map(prod, shapes))
        sources.append({
            'central_rank': r, 'remaining_shapes': shapes,
            'maximum_target_volume': maximum,
            'seed_counts': [{'power': n, 'count': lower_bound(n, r, prefixes)}
                            for n in range(36, 72)],
            'previous_power': {'power': 35, 'count': lower_bound(35, r, prefixes)},
        })
    return {
        'schema': 's5-majorant-higher-powers-v1', 'scope': SCOPE,
        'source_commit': '38e3c12553a7c499994b9ccb87946d749d718ad2',
        'source_pins': {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in sorted(inputs)},
        'proof_status': 'written proof; unreviewed; not formalized',
        'seed_start': 36, 'seed_end': 71, 'induction_step': 36,
        'sources': sources, 'improves_omega': False,
        'actual_source_lower_bound_claimed': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(export(), indent=2) + '\n')
