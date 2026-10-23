"""Check all induction seeds using separate truncated binary polynomial powers."""

import argparse
from functools import lru_cache
from hashlib import sha256
import importlib.util
import json
from math import factorial, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PRIOR = 'results/s5-finite-covers-2026-10-23/certificate.json'
PRIOR_VERIFY = 'research/ai/2026-10-23-s5-finite-covers/verify.py'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def multiply(left, right, limit):
    result = [0] * min(len(left) + len(right) - 1, limit + 1)
    for i, x in enumerate(left[:limit + 1]):
        for j, y in enumerate(right[:limit + 1 - i]):
            result[i+j] += x*y
    return result


def principal_count(layers, n):
    result, power, exponent = [1], list(layers), n
    while exponent:
        if exponent % 2:
            result = multiply(result, power, 2*n)
        exponent //= 2
        if exponent:
            power = multiply(power, power, 2*n)
    return sum(result)


def binary_count(k):
    coefficient = total = 1
    for d in range(1, k//3 + 1):
        coefficient = coefficient * (k-d+1) // d
        total += coefficient
    return total


def lower_bound(n, r, principal):
    total = 0
    for j in range(n+1):
        words = factorial(n) // (factorial(j) * factorial(n-j))
        total += words * 16**(n-j) * principal[j] * binary_count(n*(r+1)-j)
    return total


@lru_cache(None)
def replay_source(pins):
    # Every input digest is checked before this cached replay is called.
    spec = importlib.util.spec_from_file_location('s5_high_prior', ROOT / PRIOR_VERIFY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    prior = json.loads((ROOT / PRIOR).read_text())
    receipt = module.verify(prior)
    blocks = json.loads((ROOT / 'results/s5-block-filtration-2026-10-21/certificate.json').read_text())
    return prior, receipt, blocks['block_layers'][0]


def verify(report):
    require(report.get('schema') == 's5-majorant-higher-powers-v1', 'wrong schema')
    require(report.get('scope') == 'Coordinate covers of the full separately bounded S5 degree majorant; not actual-source slice-rank lower bounds.', 'wrong scope')
    require(report.get('proof_status') == 'written proof; unreviewed; not formalized'
            and report.get('improves_omega') is False
            and report.get('actual_source_lower_bound_claimed') is False, 'unsupported claim')
    require(report.get('source_commit') == '38e3c12553a7c499994b9ccb87946d749d718ad2', 'wrong source commit')
    prior = json.loads((ROOT / PRIOR).read_text())
    required = set(prior['source_pins']) | {PRIOR, PRIOR_VERIFY,
        'research/ai/2026-10-23-s5-finite-covers/proof.md'}
    require(set(report['source_pins']) == required, 'missing source pins')
    for path, digest in report['source_pins'].items():
        require(sha256((ROOT / path).read_bytes()).hexdigest() == digest, 'changed source ' + path)
    prior, source_receipt, layers = replay_source(tuple(sorted(report['source_pins'].items())))
    require((report['seed_start'], report['seed_end'], report['induction_step']) == (36, 71, 36), 'incomplete induction interval')
    require(len(report['sources']) == 2, 'wrong source count')
    principal = [principal_count(layers, j) for j in range(72)]
    receipts = []
    for r, source, previous in zip((1, 2), report['sources'], prior['sources']):
        require(source['central_rank'] == r and source['remaining_shapes'] == previous['remaining_shapes'], 'changed target inventory')
        volume = max(map(prod, source['remaining_shapes']))
        require(source['maximum_target_volume'] == volume, 'wrong target volume')
        require([row['power'] for row in source['seed_counts']] == list(range(36, 72)), 'missing or duplicated induction seed')
        for row in source['seed_counts'] + [source['previous_power']]:
            n = row['power']
            require(type(n) is int and 35 <= n <= 71, 'wrong power')
            count = lower_bound(n, r, principal)
            require(type(row['count']) is int and row['count'] == count, 'wrong diagonal count')
            if n >= 36:
                require(count**3 > volume**(2*n), 'failed induction seed')
        require(source['previous_power']['power'] == 35, 'wrong boundary control')
        receipts.append({'central_rank': r, 'maximum_target_volume': volume,
                         'induction_seeds_checked': 36,
                         'power35_passes': source['previous_power']['count']**3 > volume**70,
                         'power36_count': source['seed_counts'][0]['count']})
    return {'source_replay': source_receipt, 'sources': receipts,
            'independent_mathematical_review': False, 'improves_omega': False,
            'actual_source_lower_bound_claimed': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', required=True, type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipt = verify(json.loads(args.certificate.read_text()))
    if args.output:
        args.output.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))
