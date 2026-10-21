"""Finite-field discovery in a symmetric polynomial-pairing subfamily.

The extra ansatz is Q_z(f)=[t^12] H(t) P_z(t) f(t), with H monic cubic.
The source remains C(4,10). This is not a lossless normal form.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

from torus_exact import ExactModel, Field


def convolution(a, b, add, mul, zero, bound=12):
    result = [zero] * min(len(a)+len(b)-1, bound+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j < len(result):
                result[i+j] = add(result[i+j], mul(x, y))
    return result


def coefficient_triples(model):
    return [(triple, wanted) for triple, (_, wanted) in zip(model.all_triples, model.equations)
            if triple[1] <= triple[2]]


def coefficient_vector(model, g, p, h, order):
    """Convert pairing parameters to the original 125-variable source model."""
    field = Field(order)
    q = [convolution(h, row, field.add, field.mul, 0) for row in p]
    polynomial_rows = [g, p, q]
    full = [0]*len(model.system.keys)
    for index, (leg, row, drop) in enumerate(model.system.keys):
        degree = model.system.degrees[leg][row]
        full[index] = polynomial_rows[leg][row][degree-drop]
    return [full[index] for index in model.variables]


def discover(order, seed, timeout_ms):
    import z3
    exact = ExactModel()
    solver = z3.Solver()
    solver.set(random_seed=seed, timeout=timeout_ms)
    zero, one = z3.BitVecVal(0, 2), z3.BitVecVal(1, 2)
    if order == 3:
        def add(a, b):
            return z3.If(a == 0, b, z3.If(b == 0, a,
                         z3.If(a == b, z3.BitVecVal(3, 2)-a, zero)))
        def mul(a, b):
            return z3.If(z3.Or(a == 0, b == 0), zero,
                         z3.If(a == b, one, z3.BitVecVal(2, 2)))
    else:
        add = lambda a, b: a ^ b
        def mul(a, b):
            a0, a1, b0, b1 = a & 1, z3.LShR(a, 1), b & 1, z3.LShR(b, 1)
            return ((a0 & b0) ^ (a1 & b1)) | (((a0 & b1) ^ (a1 & b0) ^ (a1 & b1)) << 1)
    variables = []
    def monic(prefix, degree):
        row = [z3.BitVec(f'{prefix}_{j}', 2) for j in range(degree)]+[one]
        variables.extend(row[:-1])
        return row
    g = [monic('g0', 3), monic('g1', 2), [zero, one], [one]]
    p = [monic(f'p{y}', degree) for y, degree in enumerate(exact.system.degrees[1])]
    h = monic('h', 3)
    if order == 3:
        solver.add(*(v != 3 for v in variables))
    # Exclude the already ruled-out exact pure-power shared stratum.
    solver.add(z3.Or(*(v != 0 for v in variables[:5])))
    hg = [convolution(h, row, add, mul, zero) for row in g]
    pairs = {}
    values = {}
    for (x, y, z), wanted in coefficient_triples(exact):
        if (y, z) not in pairs:
            pairs[y, z] = convolution(p[y], p[z], add, mul, zero)
        terms = [mul(v, pairs[y, z][12-i]) for i, v in enumerate(hg[x])
                 if 0 <= 12-i < len(pairs[y, z])]
        value = zero
        for term in terms:
            value = add(value, term)
        values[x, y, z] = value
        solver.add(value != 0 if wanted else value == 0)
    query = solver.to_smt2()
    start = time.monotonic()
    answer = solver.check()
    report = {'field_order': order, 'seed': seed, 'timeout_ms': timeout_ms,
              'variables': len(variables), 'zero_equations': 57, 'nonzero_conditions': 10,
              'status': str(answer), 'elapsed_seconds': time.monotonic()-start,
              'solver_version': z3.get_version_string(),
              'query_sha256': hashlib.sha256(query.encode()).hexdigest(),
              'tensor_construction_supplied': False, 'improves_omega': False}
    if answer == z3.unknown:
        report['reason_unknown'] = solver.reason_unknown()
    elif answer == z3.sat:
        solution = solver.model()
        conv = lambda rows: [[solution.eval(v, model_completion=True).as_long() for v in row] for row in rows]
        gv, pv, hv = conv(g), conv(p), conv([h])[0]
        coefficients = coefficient_vector(exact, gv, pv, hv, order)
        report.update({'shared_polynomials': gv, 'input_polynomials': pv, 'pairing_polynomial': hv,
                       'coefficients': coefficients, 'verification': exact.replay(coefficients, order)})
    return report, query


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order', type=int, choices=(3, 4), default=3)
    parser.add_argument('--seed', type=int, default=20261021)
    parser.add_argument('--timeout-ms', type=int, default=60000)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report, query = discover(args.order, args.seed, args.timeout_ms)
    query_path = args.output.with_suffix('.smt2.gz')
    with gzip.GzipFile(filename=str(query_path), mode='wb', mtime=0) as stream:
        stream.write(query.encode())
    report['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print({k:v for k,v in report.items() if k not in ('coefficients', 'input_polynomials')}, flush=True)


if __name__ == '__main__':
    main()
