"""Alternate local-search solver for a saved, exact chamber query.

Every returned model is checked by the original coefficient evaluator.
An unknown answer is not an exclusion.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

from chamber_system import ChamberModel


def main():
    import z3
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query',type=Path,required=True)
    parser.add_argument('--structure',type=Path,required=True)
    parser.add_argument('--order',type=int,choices=(3,4),required=True)
    parser.add_argument('--seed',type=int,default=20261021)
    parser.add_argument('--timeout-ms',type=int,default=120000)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    raw = args.query.read_bytes()
    if args.query.suffix == '.gz':
        raw = gzip.decompress(raw)
    structure = json.loads(args.structure.read_text())['structure']
    model = ChamberModel(structure['eta'],structure['beta'])
    solver = z3.Tactic('qfbv-sls').solver()
    solver.set(random_seed=args.seed,timeout=args.timeout_ms)
    solver.add(z3.parse_smt2_string(raw.decode()))
    started = time.monotonic()
    answer = solver.check()
    report = {'field_order':args.order,'seed':args.seed,'timeout_ms':args.timeout_ms,
              'method':'qfbv-sls','status':str(answer),'elapsed_seconds':time.monotonic()-started,
              'solver_version':z3.get_version_string(),'query_sha256':hashlib.sha256(raw).hexdigest(),
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'characteristic_zero_certificate':False,'improves_omega':False}
    if answer == z3.unknown:
        report['reason_unknown'] = solver.reason_unknown()
    elif answer == z3.sat:
        solution = solver.model()
        values = [solution.eval(z3.BitVec(f'c{j}',2),model_completion=True).as_long()
                  for j in range(len(model.variables))]
        check = model.replay(values,args.order)
        if check['nonzero_zero_equations'] or any(check['toric_errors']) or check['zero_target_coefficients']:
            raise ArithmeticError('local-search model failed exact coefficient verification')
        report.update({'coefficients':values,'verification':check,
                       'characteristic_zero_certificate':check['nonsingular_hensel_premise']})
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print({k:v for k,v in report.items() if k!='coefficients'},flush=True)


if __name__ == '__main__':
    main()
