"""Bounded nonlocal operator-basis probes for Q(n,4) to M(n-1,4,n-1)."""
from itertools import product
from pathlib import Path
import argparse
import json
import sys
import time

import numpy as np

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO/'research/ai/2026-10-20-paired-direct-sums'))
from q64_complete_flag_search import bounded_step
from narrow_rectangle_balanced import balance_pair


def problem(n):
    r, m = n-1, n+3
    source = np.zeros((n*n, 4*m, 4*m))
    target = np.zeros((r*r, 4*r, 4*r))
    for p, q, y, v in product(range(n), range(n), range(4), range(4)):
        source[n*p+q, m*y+q+v, 4*(p+y)+v] = 1
    for i, j, k in product(range(r), range(4), range(r)):
        target[r*i+k, 4*i+j, r*j+k] = 1
    return source, target


def operators(n):
    r, m = n-1, n+3
    u = np.zeros((r, n))
    for i in range(r-1):
        u[i, i+1] = 1
    u[-1, 0], u[-1, n-1] = 1, -1
    products = np.zeros((2*r, m))
    for i, v, p in product(range(r), range(2), range(n)):
        products[2*i+v, p+3*v] += u[i, p]
    dual = np.linalg.pinv(products.T, rcond=1e-13)
    index = np.arange(m)
    fourier = np.exp(2j*np.pi*np.outer(index, index)/m)/np.sqrt(m)
    chirp = np.diag(np.exp(1j*np.pi*index*index/m))
    reflection = np.eye(m)[(-index) % m]
    named = [('product_dual_even', dual[::2]), ('product_dual_odd', dual[1::2]),
             ('identity', np.eye(m)[:r]), ('reflection', reflection[:r]),
             ('fourier', fourier[:r]), ('inverse_fourier', fourier.conj().T[:r]),
             ('chirp', chirp[:r]), ('inverse_chirp', chirp.conj().T[:r]),
             ('fourier_chirp', (fourier@chirp)[:r]),
             ('fourier_inverse_chirp', (fourier@chirp.conj().T)[:r]),
             ('chirp_fourier', (chirp@fourier)[:r]),
             ('inverse_chirp_fourier', (chirp.conj().T@fourier)[:r])]
    basis, names = [], []
    for name, operator in named:
        row = operator.astype(complex).ravel()
        for _ in range(2):
            for old in basis:
                row -= np.vdot(old, row)*old
        length = np.linalg.norm(row)
        if length <= 1e-12:
            continue
        basis.append(row/length)
        names.append(name)
    basis = np.array(basis).reshape(-1, r, m)
    if np.linalg.norm(basis.reshape(len(basis), -1)@basis.reshape(len(basis), -1).conj().T-np.eye(len(basis))) > 1e-12:
        raise ArithmeticError('The operator basis is not orthonormal.')
    return basis, names, u, dual


def expand(first, x, z, basis):
    # x[alpha,y,l], z[beta,v,l]; alpha,beta are the physical middle indices.
    b = np.einsum('ayl,lis->iays', x, basis).reshape(4*basis.shape[1], -1)
    c = np.einsum('avl,lks->aksv', z, basis).reshape(4*basis.shape[1], -1)
    return [first, b, c]


def initialize(n, seed, perturbation):
    basis, names, u, dual = operators(n)
    r = n-1
    x = np.zeros((4, 4, len(basis)), complex)
    z = x.copy()
    for y, v in product(range(2), repeat=2):
        x[2*y+v, 3*y] = np.einsum('is,lis->l', dual[v::2], basis.conj())
        z[2*y+v, 3*v] = np.einsum('is,lis->l', dual[y::2], basis.conj())
    first = np.array([np.outer(u[k], u[i]).ravel() for i, k in product(range(r), repeat=2)], complex)
    rng = np.random.default_rng(seed)
    for coefficients in [x, z]:
        noise = rng.normal(size=coefficients[:, :, 2:].shape)+1j*rng.normal(size=coefficients[:, :, 2:].shape)
        coefficients[:, :, 2:] += perturbation*noise/np.sqrt(noise.size*2)
    return first, x, z, basis, names


def designs(maps, source, target, basis, axis=None):
    a, b, c = maps
    n2, source_long, _ = source.shape
    r, m, count = basis.shape[1], basis.shape[2], len(basis)
    result = [None]*3
    if axis in [None, 0]:
        ea = np.einsum('bt,cu,stu->sbc', b, c, source, optimize=True).reshape(n2, -1)
        result[0] = ea, target.reshape(r*r, -1)
    if axis in [None, 1]:
        eb = np.einsum('as,cu,stu->tac', a, c, source, optimize=True).reshape(4, m, r*r, 4*r)
        eb = np.einsum('lis,ysac->ylaic', basis, eb, optimize=True).reshape(4*count, -1)
        wb = target.reshape(r*r, r, 4, 4*r).transpose(2, 0, 1, 3).reshape(4, -1)
        result[1] = eb, wb
    if axis in [None, 2]:
        ec = np.einsum('as,bt,stu->uab', a, b, source, optimize=True).reshape(m, 4, r*r, 4*r)
        ec = np.einsum('lks,svab->vlabk', basis, ec, optimize=True).reshape(4*count, -1)
        wc = target.reshape(r*r, 4*r, 4, r).transpose(2, 0, 1, 3).reshape(4, -1)
        result[2] = ec, wc
    return result if axis is None else result[axis]


def control():
    n = 5
    source, target = problem(n)
    first, x, z, basis, names = initialize(n, 0, 0)
    maps = expand(first, x, z, basis)
    actual = np.einsum('as,bt,cu,stu->abc', *maps, source, optimize=True)
    residual = float(np.linalg.norm(actual-target))
    environments = designs(maps, source, target, basis)
    coefficient_rows = [first, x.reshape(4, -1), z.reshape(4, -1)]
    errors = [float(np.linalg.norm(coeff@environment-wanted))
              for coeff, (environment, wanted) in zip(coefficient_rows, environments)]
    if residual > 1e-12 or max(errors) > 1e-12:
        raise ArithmeticError('The exact Q54 product maps did not calibrate the block designs.')
    rng = np.random.default_rng(202610460)
    random_coefficients = [rng.normal(size=c.shape)+1j*rng.normal(size=c.shape) for c in [first, x, z]]
    random_maps = expand(*random_coefficients, basis)
    random_actual = np.einsum('as,bt,cu,stu->abc', *random_maps, source, optimize=True)
    random_designs = designs(random_maps, source, random_actual, basis)
    random_errors = [float(np.linalg.norm(c.reshape(wanted.shape[0], -1)@environment-wanted)/np.linalg.norm(wanted))
                     for c, (environment, wanted) in zip(random_coefficients, random_designs)]
    if max(random_errors) > 1e-12:
        raise ArithmeticError('A complete random block-design contraction failed.')
    return {'source': 'Q(5,4)', 'target': 'M(4,4,4)', 'all_positions_checked': 4096,
            'source_terms_reconstructed': 400, 'floating_image_of_known_integer_control_error': residual,
            'three_block_design_control_errors': errors, 'operator_basis_dimension': len(basis),
            'random_all_operator_block_design_relative_errors': random_errors,
            'new_exact_certificate': False, 'improves_omega': False}


def fit(n, seed, iterations, budget, perturbation, prefix):
    prefix = Path(prefix)
    source, target = problem(n)
    first, x, z, basis, names = initialize(n, seed, perturbation)
    r, m, count = n-1, n+3, len(basis)
    initial_maps = expand(first, x, z, basis)
    prefix.with_name(prefix.name+'-initial.json').write_text(json.dumps({
        'n': n, 'b': 4, 'target_outer': r, 'seed': seed, 'auxiliary_rank': 0,
        'operator_names_before_orthonormalization': names,
        'operator_basis_real': basis.real.tolist(), 'operator_basis_imag': basis.imag.tolist(),
        'maps_real': [a.real.tolist() for a in initial_maps], 'maps_imag': [a.imag.tolist() for a in initial_maps],
        'perturbation_norm_scale': perturbation}, separators=(',', ':'))+'\n')
    norm_target = np.linalg.norm(target)
    history, best, ridges = [], float('inf'), [None]*3
    started = time.monotonic()
    for step in range(iterations+1):
        maps = expand(first, x, z, basis)
        if step % 25 == 0 or step == iterations:
            actual = np.einsum('as,bt,cu,stu->abc', *maps, source, optimize=True)
            error = actual-target
            relative = float(np.linalg.norm(error)/norm_target)
            singular = [np.linalg.svd(a, compute_uv=False) for a in maps]
            rec = {'n': n, 'iteration': step, 'relative_full_coefficient_error': relative,
                   'maximum_coefficient_error': float(np.max(np.abs(error))),
                   'map_norms': [float(np.linalg.norm(a)) for a in maps],
                   'map_smallest_singular_values': [float(s[-1]) for s in singular],
                   'map_numerical_ranks_relative_1e_minus_8': [int(np.count_nonzero(s > 1e-8*s[0])) for s in singular],
                   'nonproduct_operator_coefficient_norms': [float(np.linalg.norm(coeff[:, :, 2:])) for coeff in [x, z]],
                   'ridge_parameters': ridges.copy(), 'elapsed_seconds': time.monotonic()-started}
            history.append(rec)
            print(json.dumps(rec), flush=True)
            if relative < best:
                best = relative
                prefix.with_name(prefix.name+'-checkpoint.json').write_text(json.dumps({
                    'n': n, 'b': 4, 'target_outer': r, 'auxiliary_rank': 0,
                    'source_dimensions': list(source.shape), 'target_dimensions': list(target.shape),
                    'seed': seed, 'iteration': step, 'norm_budget': budget,
                    'operator_basis_dimension': count, 'operator_names': names,
                    'operator_basis_real': basis.real.tolist(), 'operator_basis_imag': basis.imag.tolist(),
                    'B_operator_coefficients_real': x.real.tolist(), 'B_operator_coefficients_imag': x.imag.tolist(),
                    'C_operator_coefficients_real': z.real.tolist(), 'C_operator_coefficients_imag': z.imag.tolist(),
                    'maps_real': [a.real.tolist() for a in maps], 'maps_imag': [a.imag.tolist() for a in maps],
                    'relative_coefficient_error': relative, 'exact_coefficient_certificate': False,
                    'improves_omega': False}, separators=(',', ':'))+'\n')
            if not np.isfinite(relative) or relative < 1e-12:
                break
        if step == iterations:
            break
        # The three updates have respectively r^2,4,4 rows.  The latter
        # solve coefficients in the fixed orthonormal operator span.
        for axis in range(3):
            maps = expand(first, x, z, basis)
            env, wanted = designs(maps, source, target, basis, axis)
            gram = env@env.conj().T
            cross = wanted@env.conj().T
            solved, ridges[axis] = bounded_step(np.broadcast_to(gram, (wanted.shape[0], *gram.shape)), cross, budget)
            if axis == 0:
                first = solved
            elif axis == 1:
                x = solved.reshape(4, 4, count)
            else:
                z = solved.reshape(4, 4, count)
        if step % 10 == 0:
            x, z = balance_pair(x, 0, z, 0)
        norms = np.array([np.linalg.norm(first), np.linalg.norm(x), np.linalg.norm(z)])
        common = np.exp(np.mean(np.log(norms)))
        first, x, z = [a*(common/length) for a, length in zip([first, x, z], norms)]
        if common > budget*(1+1e-9):
            raise ArithmeticError('A target gauge exceeded the complete-map norm budget.')
    result = {'source': f'Q({n},4)', 'target': f'M({r},4,{r})', 'n': n, 'b': 4,
              'target_outer': r, 'auxiliary_rank': 0, 'seed': seed,
              'maximum_iterations': iterations, 'iterations_completed': step,
              'actual_stop_reason': 'iteration_budget' if step == iterations else
                    ('coefficient_tolerance' if np.isfinite(best) and best < 1e-12 else 'nonfinite'),
              'all_source_terms': 16*n*n, 'all_target_positions_checked': int(target.size),
              'nonzero_target_positions': 4*r*r, 'norm_budget': budget,
              'operator_basis_dimension': count, 'operator_names': names,
              'first_map_free_parameters': r*r*n*n, 'each_long_map_free_parameters': 16*count,
              'target_gauge': 'full physical middle factor plus global mode balancing; outer factors fixed',
              'history': history, 'best_relative_full_coefficient_error': best,
              'exact_coefficient_certificate': False, 'unbounded_family_constructed': False,
              'improves_omega': False}
    prefix.with_name(prefix.name+'-result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'history'}, indent=2), flush=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, default=6)
    parser.add_argument('--seed', type=int, default=202610461)
    parser.add_argument('--iterations', type=int, default=1000)
    parser.add_argument('--norm-budget', type=float, default=25)
    parser.add_argument('--perturbation', type=float, default=0.15)
    parser.add_argument('--prefix', type=Path)
    parser.add_argument('--control-only', action='store_true')
    args = parser.parse_args()
    print(json.dumps({'control': control()}), flush=True)
    if not args.control_only:
        if args.prefix is None:
            parser.error('--prefix is required for a fit')
        fit(args.n, args.seed, args.iterations, args.norm_budget, args.perturbation, args.prefix)
