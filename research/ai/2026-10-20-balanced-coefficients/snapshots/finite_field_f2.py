"""Finite-field coefficient search and exact Jacobian-rank controls.

A full-row-rank solution would lift to characteristic zero by Hensel's
lemma. Discovery may use Z3; coefficient and Jacobian replay do not.
"""
from __future__ import annotations

import argparse
from functools import reduce
import hashlib
import json
import os
from pathlib import Path
import time
from coefficient_system import System


def equations(system):
    variables = [i for i in range(len(system.keys)) if i not in system.constant_values]
    position = {index:j for j,index in enumerate(variables)}
    result = []
    for level in system.levels:
        for p,y,z,wanted in level['constraints']:
            delta = level['level']; terms = []
            for i in range(min(delta, system.degrees[0][p])+1):
                for j in range(min(delta-i, system.degrees[1][y])+1):
                    k = delta-i-j
                    if k > system.degrees[2][z]: continue
                    monomial = []
                    for leg,row,drop in [(0,p,i),(1,y,j),(2,z,k)]:
                        index = system.index[(leg,row,drop)]
                        if index in position: monomial.append(position[index])
                        elif system.constant_values[index] == 0: break
                    else:
                        terms.append(tuple(monomial))
            result.append((terms, wanted))
    return variables, result


def rank_mod(matrix, prime):
    matrix = [[int(value)%prime for value in row] for row in matrix]
    rank = 0; columns = []
    for column in range(len(matrix[0]) if matrix else 0):
        pivot = next((r for r in range(rank,len(matrix)) if matrix[r][column]), None)
        if pivot is None: continue
        matrix[rank],matrix[pivot] = matrix[pivot],matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [(value*inverse)%prime for value in matrix[rank]]
        for row in range(rank+1,len(matrix)):
            factor = matrix[row][column]
            if factor:
                matrix[row] = [(a-factor*b)%prime for a,b in zip(matrix[row],matrix[rank])]
        columns.append(column); rank += 1
        if rank == len(matrix): break
    return rank, columns


def replay(system, values, prime):
    variables, eqs = equations(system)
    if len(values) != len(variables): raise ValueError('wrong coefficient count')
    errors, jac = [], []
    for terms,wanted in eqs:
        value = -wanted
        row = [0]*len(variables)
        for term in terms:
            product = 1
            for j in term: product = product*values[j]%prime
            value += product
            for differentiated,j in enumerate(term):
                derivative = 1
                for k,index in enumerate(term):
                    if k != differentiated: derivative = derivative*values[index]%prime
                row[j] = (row[j]+derivative)%prime
        errors.append(value%prime); jac.append(row)
    rank,pivots = rank_mod(jac, prime)
    return {'equations_checked':len(eqs), 'variables':len(variables),
            'nonzero_equations':sum(bool(v) for v in errors),
            'jacobian_rank':rank, 'jacobian_pivot_columns':pivots,
            'nonsingular_hensel_premise':not any(errors) and rank == len(eqs)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prime', type=int, choices=[2,3,5], default=2)
    parser.add_argument('--timeout-ms', type=int, default=120000)
    parser.add_argument('--max-models', type=int, default=16)
    parser.add_argument('--seed', type=int)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    import z3
    seed = args.seed if args.seed is not None else int.from_bytes(os.urandom(4),'big')&0x7fffffff
    system = System(); variables, eqs = equations(system)
    prime = args.prime
    solver = z3.Solver(); solver.set(random_seed=seed)
    if prime == 2:
        x = [z3.Bool(f'c{j}') for j in range(len(variables))]
        for terms,wanted in eqs:
            monomials = [z3.And(*[x[j] for j in term]) for term in terms]
            value = reduce(z3.Xor, monomials, z3.BoolVal(False))
            solver.add(value == bool(wanted))
    else:
        x = [z3.Int(f'c{j}') for j in range(len(variables))]
        solver.add(*[z3.And(v>=0,v<prime) for v in x])
        for terms,wanted in eqs:
            products = []
            for term in terms:
                product = 1
                for j in term: product *= x[j]
                products.append(product)
            solver.add(z3.Sum(products)%prime == wanted)
    query = solver.to_smt2()
    args.output.with_suffix('.smt2').write_text(query)
    records = []; started = time.monotonic(); status = 'not-started'
    for index in range(args.max_models):
        remaining = args.timeout_ms-int(1000*(time.monotonic()-started))
        if remaining <= 0: status = 'total-time-limit'; break
        solver.set(timeout=remaining)
        answer = solver.check(); status = str(answer)
        if answer != z3.sat: break
        model = solver.model()
        values = [int(z3.is_true(model.eval(v,model_completion=True))) if prime==2
                  else model.eval(v,model_completion=True).as_long() for v in x]
        check = replay(system, values, prime)
        records.append({'index':index, 'coefficients':values, 'verification':check})
        print('model',index,'rank',check['jacobian_rank'],'of',len(eqs),flush=True)
        if check['nonsingular_hensel_premise']: status='nonsingular-certificate'; break
        solver.add(z3.Or(*[v != bool(value) if prime==2 else v != value for v,value in zip(x,values)]))
    report = {'prime':prime,'seed':seed,'seed_origin':'provided' if args.seed is not None else 'os.urandom(4)',
              'timeout_ms':args.timeout_ms,'max_models':args.max_models,'result':status,
              'models':records,'elapsed_seconds':time.monotonic()-started,
              'query_sha256':hashlib.sha256(query.encode()).hexdigest(),'solver_version':z3.get_version_string(),
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'system_source_sha256':hashlib.sha256(Path(__file__).with_name('coefficient_system.py').read_bytes()).hexdigest(),
              'improves_omega':False}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print('result',status,'models',len(records),flush=True)
