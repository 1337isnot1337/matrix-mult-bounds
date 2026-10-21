"""Exact elimination-first finite-field discovery for nonmonic flags.

The predecessor's unit integer pivots remove 68 variables. This encoding
keeps 57 monic free coefficients and 18 nonzero target row scalars.
"""
from __future__ import annotations

import argparse
from functools import reduce
import gzip
import hashlib
import json
from pathlib import Path
import time

from torus_exact import ExactModel, Field


class ConcreteOps:
    def __init__(self, order):
        self.field = Field(order)
        self.zero, self.one = 0, 1
        self.add, self.mul, self.neg = self.field.add, self.field.mul, self.field.neg

    def integer(self, value):
        return int(value) % (3 if self.field.order == 3 else 2)


def eliminate(model, free, scales, ops):
    system = model.system
    if len(free) != len(system.free) or len(scales) != len(model.columns):
        raise ValueError('incorrect elimination parameter count')
    values = [ops.zero]*len(system.keys)
    for index, value in system.constant_values.items():
        values[index] = ops.integer(value)
    for index, value in zip(system.free, free):
        values[index] = value
    scalar_lookup = dict(zip(model.columns, scales))
    def product(items):
        return reduce(ops.mul, items, ops.one)
    def sum_values(items):
        return reduce(ops.add, items, ops.zero)
    residuals = []
    for level in system.levels:
        lower = [sum_values(product(values[j] for j in term) for term in terms)
                 for terms in level['terms']]
        targets = [product(scalar_lookup.get(j, ops.one) for j in (p,4+y,14+z))
                   if wanted else ops.zero for p,y,z,wanted in level['constraints']]
        rhs = [ops.add(target, ops.neg(value)) for target,value in zip(targets,lower)]
        matrix = level['matrix']
        for row in range(len(rhs)):
            free_terms = [ops.mul(ops.integer(matrix[row,column]), values[level['variables'][column]])
                          for column in level['free_columns'] if matrix[row,column]]
            rhs[row] = ops.add(rhs[row], ops.neg(sum_values(free_terms)))
        for j,column in enumerate(level['pivots']):
            terms = [ops.mul(ops.integer(level['inverse'][j,k]), rhs[row])
                     for k,row in enumerate(level['rows']) if level['inverse'][j,k]]
            values[level['variables'][column]] = sum_values(terms)
        for row in level['remaining_rows']:
            total = sum_values(ops.mul(ops.integer(matrix[row,j]), values[index])
                               for j,index in enumerate(level['variables']) if matrix[row,j])
            residuals.append(ops.add(ops.add(total,lower[row]),ops.neg(targets[row])))
    return values, residuals


def discover(order, seed, timeout_ms):
    import z3
    model = ExactModel()
    solver = z3.SolverFor('QF_BV')
    solver.set(random_seed=seed, timeout=timeout_ms)
    class SymbolicOps:
        zero, one = z3.BitVecVal(0,2), z3.BitVecVal(1,2)
        def integer(self, value):
            return z3.BitVecVal(int(value) % (3 if order == 3 else 2), 2)
        def add(self,a,b):
            if order == 4:
                return a ^ b
            return z3.If(a==0,b,z3.If(b==0,a,z3.If(a==b,z3.BitVecVal(3,2)-a,self.zero)))
        def mul(self,a,b):
            if order == 3:
                return z3.If(z3.Or(a==0,b==0),self.zero,z3.If(a==b,self.one,z3.BitVecVal(2,2)))
            a0,a1,b0,b1 = a&1,z3.LShR(a,1),b&1,z3.LShR(b,1)
            return ((a0&b0)^(a1&b1)) | (((a0&b1)^(a1&b0)^(a1&b1))<<1)
        def neg(self,a):
            return a if order == 4 else z3.If(a==0,self.zero,z3.BitVecVal(3,2)-a)
    ops = SymbolicOps()
    free = [z3.BitVec(f'free{j}',2) for j in range(len(model.system.free))]
    scales = [z3.BitVec(f'scale{j}',2) for j in range(len(model.columns))]
    if order == 3:
        solver.add(*(v != 3 for v in free+scales))
    solver.add(*(v != 0 for v in scales))
    values, residuals = eliminate(model,free,scales,ops)
    solver.add(*(residual == 0 for residual in residuals))
    solver.add(z3.Or(*(values[index] != 0 for index in model.variables[:5])))
    query = solver.to_smt2()
    started = time.monotonic()
    answer = solver.check()
    report = {'field_order':order,'seed':seed,'timeout_ms':timeout_ms,
              'free_monic_coefficients':len(free),'nonzero_target_scalars':len(scales),
              'remaining_equations':len(residuals),'eliminated_coefficients':68,
              'status':str(answer),'elapsed_seconds':time.monotonic()-started,
              'solver_version':z3.get_version_string(),
              'query_sha256':hashlib.sha256(query.encode()).hexdigest(),
              'characteristic_zero_certificate':False,'improves_omega':False}
    if answer == z3.unknown:
        report['reason_unknown'] = solver.reason_unknown()
    elif answer == z3.sat:
        solution = solver.model()
        f = [solution.eval(v,model_completion=True).as_long() for v in free]
        s = [solution.eval(v,model_completion=True).as_long() for v in scales]
        checked_values, errors = eliminate(model,f,s,ConcreteOps(order))
        if any(errors):
            raise ArithmeticError('eliminated field solution failed replay')
        coefficients = [checked_values[j] for j in model.variables]
        check = model.replay(coefficients,order)
        report.update({'free_coefficients':f,'target_scalars':s,'coefficients':coefficients,
                       'verification':check,'characteristic_zero_certificate':check['nonsingular_hensel_premise']})
    return report,query


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order',type=int,choices=(3,4),default=4)
    parser.add_argument('--seed',type=int,default=20261021)
    parser.add_argument('--timeout-ms',type=int,default=120000)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    report,query = discover(args.order,args.seed,args.timeout_ms)
    with gzip.GzipFile(filename=str(args.output.with_suffix('.smt2.gz')),mode='wb',mtime=0) as stream:
        stream.write(query.encode())
    report['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k not in ('free_coefficients','target_scalars','coefficients')},flush=True)


if __name__ == '__main__':
    main()
