"""Optional bounded SAT/LP discovery for one SL(2,F8) full-subgroup frame.

The full (18,18,25) frame first replays its exact subgroup-ideal exclusion,
before any SAT dependency is imported. The positive control still searches.
Only exact full-support verification accepts a potential. Timeout and
solver-reported UNSAT without a proof trace establish no nonexistence.
"""
import argparse
from itertools import combinations
import json
from pathlib import Path
import threading
import time

from sl2_f8_source import group
from sl2_f8_frames import subgroup,right_cosets
from group_exact import pair_map,verify_farkas
from stream_potentials import discover


def run(seconds,output,control=False,max_models=50):
    G,H = group(),subgroup()
    bounds = [1,1] if control else [18,25]
    from subgroup_preflight import exclusion_for
    exclusion = exclusion_for([18,*bounds],H)
    if exclusion is not None:
        report = {'group':G['name'],'shape':[18,*bounds],'fixed_subgroup':H,
                  'subgroup_order':18,'right_coset_count':28,
                  'normalization':'T and U both contain the identity; S is the fixed D18 subgroup.',
                  'scope':__doc__,'positive_control_only':control,
                  'models':0,'cuts':[],'witness':None,
                  'status':'excluded-by-subgroup-ideal','exclusion':exclusion,
                  'analytic_exclusion_verified':True,'unsat_proof_checked':False,
                  'seconds_requested':seconds,'model_limit':max_models,
                  'improves_omega':False}
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','witness','fixed_subgroup']},indent=2))
        return report
    from pysat.card import CardEnc
    from pysat.formula import IDPool
    from pysat.solvers import Glucose4
    started = time.monotonic()
    pool = IDPool()
    members = [[pool.id(('member',f,g)) for g in range(504)] for f in range(2)]
    clauses = []
    for f,bound in enumerate(bounds):
        clauses.extend(CardEnc.equals(members[f],bound=bound,vpool=pool).clauses)
        clauses.append([members[f][0]])
        for coset in right_cosets():
            clauses.extend([[-members[f][a],-members[f][b]] for a,b in combinations(coset,2)])
    representatives = sorted({min(g,G['inv'][g]) for g in range(1,504) if g not in H})
    for g in representatives:
        D = [pool.id(('difference',f,g)) for f in range(2)]
        clauses.append([-D[0],-D[1]])
        for f in range(2):
            for t in range(504):
                u = G['mul'][g][t]
                if g==G['inv'][g] and u<t:
                    continue
                clauses.append([-members[f][t],-members[f][u],D[f]])
    solver = Glucose4(bootstrap_with=clauses)
    report = {'group':G['name'],'shape':[18,*bounds],'fixed_subgroup':H,
              'subgroup_order':18,'right_coset_count':28,
              'normalization':'T and U both contain the identity; S is the fixed D18 subgroup.',
              'scope':__doc__,'positive_control_only':control,'variables':pool.top,
              'clauses':len(clauses),'models':0,'cuts':[],'witness':None,
              'status':'running','improves_omega':False,'unsat_proof_checked':False,
              'seconds_requested':seconds,'model_limit':max_models}
    output.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds'] = time.monotonic()-started
        temporary = output.with_suffix('.tmp')
        temporary.write_text(json.dumps(report,indent=2)+'\n')
        temporary.replace(output)
    save()
    while report['models']<max_models:
        remaining = seconds-(time.monotonic()-started)
        if remaining<=0:
            report['status'] = 'time-limit'
            break
        timer = threading.Timer(remaining,solver.interrupt)
        timer.start()
        try:
            solved = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        if solved is None:
            report['status'] = 'time-limit'
            break
        if not solved:
            report['status'] = 'solver-reported UNSAT; no proof trace'
            break
        model = {v for v in solver.get_model() if v>0}
        sets = [H]+[[g for g,lit in enumerate(row) if lit in model] for row in members]
        for f,g in [(0,1),(1,2),(2,0)]:
            pair_map(G,sets[f],sets[g])
        report['models'] += 1
        lazy = discover(G,sets,max_rounds=60,violation_batch=500)
        decision,relations = lazy['decision'],lazy['relations']
        if decision is None:
            report['status'] = 'lazy LP unresolved'
            report['unresolved_candidate'] = sets
            break
        if 'potentials' in decision:
            report['witness'] = {'sets':sets,'potentials':decision['potentials'],
                                 'verification':lazy['verification']}
            report['status'] = 'exact-degeneration-witness'
            break
        if not verify_farkas(relations,decision['indices'],decision['weights']):
            raise ArithmeticError('incorrect integer rejection circuit')
        used = set()
        for i in decision['indices']:
            s,t,tt,u,uu,ss = relations[i]['vertices']
            used.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                         (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
        solver.add_clause([-members[f-1][g] for f,g in sorted(used) if f])
        report['cuts'].append({'sets':sets,'members':sorted(used),
                              'vertices':[relations[i]['vertices'] for i in decision['indices']],
                              'rows':[relations[i]['row'] for i in decision['indices']],
                              'weights':decision['weights']})
        save()
    else:
        report['status'] = 'model-limit'
    save()
    solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','witness','fixed_subgroup']},indent=2))
    return report


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds',type=float,default=180)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--control',action='store_true')
    parser.add_argument('--max-models',type=int,default=50)
    args = parser.parse_args()
    run(args.seconds,args.output,args.control,args.max_models)
