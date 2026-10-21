"""Optional cubic finite-field formulation with explicit target row scalars."""
import argparse
from functools import reduce
import hashlib
import json
from pathlib import Path
import time

from torus_exact import ExactModel


def run(order, seed, timeout_ms, query_path):
    import z3
    model = ExactModel()
    solver = z3.SolverFor("QF_BV"); solver.set(random_seed=seed)
    coefficients = [z3.BitVec(f"c{j}",2) for j in range(len(model.variables))]
    scales = [z3.BitVec(f"s{j}",2) for j in range(len(model.columns))]
    zero,one = z3.BitVecVal(0,2),z3.BitVecVal(1,2)
    if order == 3:
        solver.add(*(v != 3 for v in coefficients+scales))
        def multiply(a,b):
            return z3.If(z3.Or(a==0,b==0),zero,z3.If(a==b,one,z3.BitVecVal(2,2)))
        def add(a,b):
            return z3.If(a==0,b,z3.If(b==0,a,z3.If(a==b,z3.BitVecVal(3,2)-a,zero)))
    elif order == 4:
        def multiply(a,b):
            a0,a1,b0,b1=a&1,z3.LShR(a,1),b&1,z3.LShR(b,1)
            return ((a0&b0)^(a1&b1)) | (((a0&b1)^(a1&b0)^(a1&b1))<<1)
        add=lambda a,b:a^b
    else:
        raise ValueError("field order must be three or four")
    solver.add(*(v != 0 for v in scales))
    scalar_lookup=dict(zip(model.columns,scales))
    for (terms,wanted),(p,y,z) in zip(model.equations,model.all_triples):
        value=reduce(add,(reduce(multiply,(coefficients[j] for j in term),one) for term in terms),zero)
        target=reduce(multiply,(scalar_lookup.get(j,one) for j in (p,4+y,14+z)),one) if wanted else zero
        solver.add(value==target)
    query=solver.to_smt2();query_path.write_text(query)
    started=time.monotonic();solver.set(timeout=timeout_ms)
    answer=solver.check();records=[]
    if answer==z3.sat:
        solution=solver.model()
        values=[solution.eval(v,model_completion=True).as_long() for v in coefficients]
        scalar_values=[solution.eval(v,model_completion=True).as_long() for v in scales]
        records.append({"coefficients":values,"target_scales":scalar_values,
                        "verification":model.replay(values,order)})
    return {"field_order":order,"seed":seed,"timeout_ms":timeout_ms,
            "status":str(answer),"reason_unknown":solver.reason_unknown() if answer==z3.unknown else None,
            "elapsed_seconds":time.monotonic()-started,"models":records,
            "encoding":"125 monic coefficients plus 18 nonzero target scalars; 121 cubic equations",
            "solver_version":z3.get_version_string(),"query_sha256":hashlib.sha256(query.encode()).hexdigest(),
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "exact_solution_found":bool(records) and records[0]["verification"]["nonsingular_hensel_premise"],
            "improves_omega":False}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order",type=int,choices=(3,4),default=4)
    parser.add_argument("--seed",type=int,default=20261021)
    parser.add_argument("--timeout-ms",type=int,default=180000)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    report=run(args.order,args.seed,args.timeout_ms,args.output.with_suffix('.smt2'))
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(report,flush=True)
