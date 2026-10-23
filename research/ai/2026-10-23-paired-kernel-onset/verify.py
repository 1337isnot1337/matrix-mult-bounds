"""Fixed-short-direction integer kernels and exact long-leg rank bounds."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT/relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bundle = load('kernel_onset_bundle', 'research/ai/2026-10-23-paired-bundle-injectivity/verify.py')
matrix = load('kernel_onset_matrix', 'research/ai/2026-10-20-paired-sources/all_ranks.py')
choose = bundle.choose


def fixed_kernel(a, r):
    if a < 2 or not 0 <= r <= a*a:
        raise ValueError('a>=2 and valid restricted exterior degree required')
    m = a*(a-1)
    return choose(m, r-a)*max(r-m, 0)


@lru_cache(None)
def kernel_lower(a, p):
    N, m = a*(2*a-1), a*(a-1)
    if a < 2 or not 0 <= p <= N:
        raise ValueError('a>=2 and valid exterior degree required')
    return a*sum(choose(m, p-r)*fixed_kernel(a, r) for r in range(a*a+1))


@lru_cache(None)
def rank_bounds(a, p):
    N = a*(2*a-1)
    lower = bundle.source_rank_lower(a, p)
    upper = min(a*a*choose(N, p)-kernel_lower(a, p), N*choose(N, p+1))
    if not 0 <= lower <= upper:
        raise ValueError('the proved source bounds are inconsistent')
    return lower, upper


def restricted_columns(a, r):
    terms = [(y*a+v, u, (u+y)*a+v)
             for u, y, v in product(range(a), repeat=3)]
    return bundle.generic_koszul_columns((a*a, a, a*(2*a-1)), terms, r)


def mapped_column_labels(a, r, q):
    h = 2*a-1
    labels = []
    for subset in combinations(range(a*a), r):
        mask = sum(1 << ((b//a)*h+q+b % a) for b in subset)
        labels.extend((mask, u, q) for u in range(a))
    return labels


def replay_full_source_embeddings(a, r, free, vectors):
    """Check every integer output and the inherited independent coordinates."""
    all_free = set()
    count = 0
    for q in range(a):
        labels = mapped_column_labels(a, r, q)
        own_free = {labels[f] for f in free}
        if len(own_free) != len(free) or own_free & all_free:
            raise ValueError('embedded free coordinates are not independent')
        all_free |= own_free
        for f, vector in zip(free, vectors):
            coefficients = {labels[j]: value for j, value in vector}
            if not coefficients.get(labels[f]) or any(coefficients.get(labels[g], 0)
                                                    for g in free if g != f):
                raise ValueError('embedded diagonal kernel minor is missing')
            image = defaultdict(int)
            for (mask, u, fixed_q), value in coefficients.items():
                for row, coefficient in bundle.source_column(a, mask, u, fixed_q):
                    image[row] += value*coefficient
            if any(image.values()):
                raise ValueError('embedded integer vector is not in the literal source kernel')
            count += 1
    return count


def build_certificate():
    controls = []
    for a in [2, 3]:
        for r in range(a*a+1):
            columns = restricted_columns(a, r)
            rank = bundle.generic_rank_mod2(columns)
            free, vectors = bundle.integer_kernel(columns)
            nullity = bundle.verify_integer_kernel(columns, free, vectors)
            if nullity != fixed_kernel(a, r) or rank != len(columns)-nullity:
                raise ValueError('restricted rational and modular bounds do not match')
            record = {'a': a, 'degree': r, 'columns': len(columns), 'mod2_rank': rank,
                      'exact_complex_nullity': nullity, 'free_columns': free,
                      'integer_kernel_vectors': vectors}
            if r == a*(a-1)+1:
                record['independent_full_source_kernels'] = replay_full_source_embeddings(
                    a, r, free, vectors)
                if record['independent_full_source_kernels'] != a*choose(a*(a-1), a-1):
                    raise ValueError('critical global kernel count is wrong')
            controls.append(record)
    return {'schema': 'paired-fixed-short-kernels-v1',
            'proof_status': 'proof-written-unreviewed',
            'restricted_kernel_formula': 'binom(a*(a-1),r-a)*max(r-a*(a-1),0)',
            'full_column_range_is_sharp_over_every_field': True,
            'all_degree_source_upper_bound': 'short-domain dimension minus padded fixed-input kernels, capped by row dimension',
            'finite_exact_controls': controls,
            'complete_source_kernel_formula': False,
            'independent_review': False, 'lean_formalized': False, 'improves_omega': False}


def check_sources():
    for pin in json.loads((PACKAGE/'sources.json').read_text())['local_sources']:
        if hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest() != pin['sha256']:
            raise ValueError('adopted source no longer matches the inspected pin')


def verify_certificate(certificate):
    check_sources()
    for key in ['complete_source_kernel_formula', 'independent_review',
                'lean_formalized', 'improves_omega']:
        if certificate.get(key) is not False:
            raise ValueError('unsupported proof scope or evidence status')
    for record in certificate['finite_exact_controls']:
        columns = restricted_columns(record['a'], record['degree'])
        bundle.verify_integer_kernel(columns, record['free_columns'], record['integer_kernel_vectors'])
    if certificate != build_certificate():
        raise ValueError('certificate differs from exact source regeneration')
    return {'verified': True, 'restricted_exact_complex_ranks': 15,
            'critical_full_source_integer_kernels': [4, 45],
            'all_size_proof_formalized': False, 'improves_omega': False}


def runs(powers):
    result = []
    for p in powers:
        if result and p == result[-1][1]+1:
            result[-1][1] = p
        else:
            result.append([p, p])
    return result


def target_screen():
    frontier = json.loads((ROOT/'results/paired-sources-2026-10-20/all-power-frontier.json').read_text())
    records, additional, exclusions, comparisons = [], 0, 0, 0
    for source in frontier['records']:
        a, N = source['a'], source['a']*(2*source['a']-1)
        for target in source['remaining_after_this_screen']:
            l, b, r = target['shape']
            orientations = []
            for leg, shape in [('B', (l, r, b)), ('C', (r, l, b))]:
                cannot, excluded, unknown = [], [], []
                digest = hashlib.sha256()
                for p in range(N):
                    lower, upper = rank_bounds(a, p)
                    target_rank = matrix.padded_matrix_rank(shape, N, p)
                    digest.update((json.dumps([p, lower, target_rank, upper])+'\n').encode())
                    if target_rank > upper:
                        excluded.append(p)
                    elif target_rank <= lower:
                        cannot.append(p)
                    else:
                        unknown.append(p)
                    comparisons += 1
                new = sum(a*(a-1) < p < N-a for p in cannot)
                additional += new
                exclusions += len(excluded)
                orientations.append({'leg': leg, 'matrix_shape_with_short_input': list(shape),
                                     'cannot_exclude': runs(cannot), 'excludes': runs(excluded),
                                     'undecided': runs(unknown),
                                     'additional_intermediate_degrees_settled': new,
                                     'exact_comparisons_sha256': digest.hexdigest()})
            records.append({'a': a, 'original_matrix_shape': target['shape'],
                            'long_leg_orientations': orientations})
    return {'schema': 'paired-long-leg-bound-screen-v1',
            'scope': 'All28 maintained short-leg survivors through a16, both long legs with short input, all nonzero exterior maps',
            'records': records, 'exact_comparisons': comparisons,
            'additional_intermediate_noncuts': additional,
            'rank_exclusion_witnesses': exclusions,
            'undecided_is_not_a_pass': True, 'targets_constructed': False,
            'improves_omega': False}


def verify_screen(report):
    check_sources()
    if report.get('undecided_is_not_a_pass') is not True:
        raise ValueError('undecided comparisons were promoted to passes')
    if report.get('targets_constructed') is not False or report.get('improves_omega') is not False:
        raise ValueError('screen does not construct a target or improve the exponent')
    if report != target_screen():
        raise ValueError('target comparison ranges or exact-arithmetic digest changed')
    return {'verified': True, 'exact_comparisons': report['exact_comparisons'],
            'additional_intermediate_noncuts': report['additional_intermediate_noncuts'],
            'rank_exclusion_witnesses': report['rank_exclusion_witnesses'],
            'target_count': len(report['records']), 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify', type=Path)
    parser.add_argument('--screen', action='store_true')
    args = parser.parse_args()
    report = ((verify_screen(json.loads(args.verify.read_text())) if args.verify else target_screen()) if args.screen else
              verify_certificate(json.loads(args.verify.read_text())) if args.verify else
              build_certificate())
    text = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')
