"""Discovery over F4 = F2[u]/(u^2+u+1), with independent integer replay."""
import argparse
from functools import reduce
import hashlib
import json
import os
from pathlib import Path
import time
from coefficient_system import System
from finite_field import equations


def multiply(a,b):
    a0,a1 = a&1,a>>1; b0,b1 = b&1,b>>1
    return ((a0&b0)^(a1&b1)) | (((a0&b1)^(a1&b0)^(a1&b1))<<1)


def rank(matrix):
    matrix = [list(row) for row in matrix]; r = 0; pivots = []
    for column in range(len(matrix[0]) if matrix else 0):
        pivot = next((i for i in range(r,len(matrix)) if matrix[i][column]),None)
        if pivot is None: continue
        matrix[r],matrix[pivot] = matrix[pivot],matrix[r]
        inverse = multiply(matrix[r][column],matrix[r][column])
        matrix[r] = [multiply(value,inverse) for value in matrix[r]]
        for row in range(r+1,len(matrix)):
            factor = matrix[row][column]
            if factor: matrix[row] = [a^multiply(factor,b) for a,b in zip(matrix[row],matrix[r])]
        pivots.append(column); r += 1
        if r == len(matrix): break
    return r,pivots


def replay(system, values):
    variables,eqs = equations(system)
    if len(values) != len(variables) or any(v not in range(4) for v in values):
        raise ValueError('invalid F4 coefficient list')
    errors,jac = [],[]
    for terms,wanted in eqs:
        value = wanted; row = [0]*len(variables)
        for term in terms:
            product = 1
            for j in term: product = multiply(product,values[j])
            value ^= product
            for differentiated,j in enumerate(term):
                derivative = 1
                for k,index in enumerate(term):
                    if k != differentiated: derivative = multiply(derivative,values[index])
                row[j] ^= derivative
        errors.append(value); jac.append(row)
    r,pivots = rank(jac)
    return {'equations_checked':len(eqs),'variables':len(variables),'jacobian_rank':r,
            'nonzero_equations':sum(bool(v) for v in errors),'jacobian_pivot_columns':pivots,
            'nonsingular_hensel_premise':not any(errors) and r==len(eqs)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout-ms',type=int,default=120000)
    parser.add_argument('--max-models',type=int,default=16)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    import z3
    seed = int.from_bytes(os.urandom(4),'big')&0x7fffffff
    system = System();variables,eqs = equations(system)
    x = [z3.BitVec(f'c{j}',2) for j in range(len(variables))]
    solver = z3.Solver();solver.set(random_seed=seed)
    def product(a,b):
        a0,a1 = a&1,z3.LShR(a,1); b0,b1 = b&1,z3.LShR(b,1)
        return ((a0&b0)^(a1&b1)) | (((a0&b1)^(a1&b0)^(a1&b1))<<1)
    for terms,wanted in eqs:
        monomials = [reduce(product,[x[j] for j in term],z3.BitVecVal(1,2)) for term in terms]
        solver.add(reduce(lambda a,b:a^b,monomials,z3.BitVecVal(0,2)) == wanted)
    query = solver.to_smt2();args.output.with_suffix('.smt2').write_text(query)
    started = time.monotonic();records = [];status = 'not-started';reason = None
    for index in range(args.max_models):
        remaining = args.timeout_ms-int(1000*(time.monotonic()-started))
        if remaining<=0:status='total-time-limit';break
        solver.set(timeout=remaining);answer=solver.check();status=str(answer)
        if answer != z3.sat:
            if answer == z3.unknown:reason=solver.reason_unknown()
            break
        model=solver.model();values=[model.eval(v,model_completion=True).as_long() for v in x]
        check=replay(system,values);records.append({'index':index,'coefficients':values,'verification':check})
        print('model',index,'rank',check['jacobian_rank'],flush=True)
        if check['nonsingular_hensel_premise']:status='nonsingular-certificate';break
        solver.add(z3.Or(*[v!=value for v,value in zip(x,values)]))
    report={'field':'F2[u]/(u^2+u+1)','order':4,'seed':seed,'seed_origin':'os.urandom(4)',
            'timeout_ms':args.timeout_ms,'max_models':args.max_models,'result':status,'reason_unknown':reason,
            'models':records,'elapsed_seconds':time.monotonic()-started,'solver_version':z3.get_version_string(),
            'query_sha256':hashlib.sha256(query.encode()).hexdigest(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'imported_source_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                      for name in ['finite_field.py','coefficient_system.py']},
            'improves_omega':False}
    args.output.write_text(json.dumps(report,indent=2)+'\n');print('result',status,flush=True)
