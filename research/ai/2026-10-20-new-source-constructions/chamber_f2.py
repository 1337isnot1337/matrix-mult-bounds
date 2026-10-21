"""Boolean search for F2 points in a specified nonmonic flag chamber.

All nonzero target coefficients equal one over F2, so the toric relations
hold automatically. A candidate is independently replayed in F4, which
contains F2 and preserves its matrix ranks.
"""
import argparse
from functools import reduce
import gzip
import hashlib
import json
from pathlib import Path
import time

from chamber_system import ChamberModel


def main():
    import z3
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--eta',default='0,301,628,844')
    parser.add_argument('--beta',type=int,default=100)
    parser.add_argument('--seed',type=int,default=20261021)
    parser.add_argument('--timeout-ms',type=int,default=120000)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    model = ChamberModel(list(map(int,args.eta.split(','))),args.beta)
    variables = [z3.Bool(f'c{j}') for j in range(len(model.variables))]
    solver = z3.Solver()
    solver.set(random_seed=args.seed,timeout=args.timeout_ms)
    for terms,wanted in model.equations:
        coefficient = reduce(z3.Xor,(z3.And(*[variables[j] for j in term]) for term in terms),z3.BoolVal(False))
        solver.add(coefficient == bool(wanted))
    query = solver.to_smt2().encode()
    with gzip.GzipFile(filename=str(args.output.with_suffix('.smt2.gz')),mode='wb',mtime=0) as stream:
        stream.write(query)
    started = time.monotonic()
    answer = solver.check()
    report = {'structure':model.structure(),'field_order':2,'seed':args.seed,
              'timeout_ms':args.timeout_ms,'status':str(answer),
              'elapsed_seconds':time.monotonic()-started,'solver_version':z3.get_version_string(),
              'query_sha256':hashlib.sha256(query).hexdigest(),
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'characteristic_zero_certificate':False,'improves_omega':False}
    if answer == z3.unknown:
        report['reason_unknown'] = solver.reason_unknown()
    elif answer == z3.sat:
        solution = solver.model()
        values = [int(z3.is_true(solution.eval(v,model_completion=True))) for v in variables]
        check = model.replay(values,4)
        if check['nonzero_zero_equations'] or any(check['toric_errors']) or check['zero_target_coefficients']:
            raise ArithmeticError('Boolean model failed independent coefficient replay')
        report.update({'coefficients':values,'verification_over_f4':check,
                       'characteristic_zero_certificate':check['nonsingular_hensel_premise']})
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k not in ('structure','coefficients')},flush=True)


if __name__ == '__main__':
    main()
