"""Optional full-source SL2 F8 SAT/lazy-LP discovery with every subgroup cut.

No solver-reported UNSAT or timeout is accepted as a target exclusion.
Only full integer support replay accepts a degeneration witness.
"""
import argparse
import gzip
import importlib.util
import json
from pathlib import Path
import sys
import threading
import time

PACKAGE=Path(__file__).resolve().parent
ROOT=PACKAGE.parents[2]
sys.path.insert(0,str(PACKAGE.parent/'2026-10-21-semisimple-koszul'))
from sl2_f8_source import group
from group_exact import pair_map
from stream_potentials import discover,verify_stream_witness
from verify_stream_reports import verify_cut
spec=importlib.util.spec_from_file_location('native_f8_subgroup_catalog',PACKAGE.parent/'2026-10-23-sl2-f8-subgroup-catalog/verify.py')
catalog=importlib.util.module_from_spec(spec);spec.loader.exec_module(catalog)
CERTIFICATE=ROOT/'results/sl2-f8-subgroup-catalog-2026-10-23/certificate.json.gz'


def all_cuts(shape):
    with gzip.open(CERTIFICATE,'rt') as handle:report=json.load(handle)
    receipt=catalog.verify(report)
    G=group();summaries=catalog.helper.minimal_summary(G,report['ideal_classes'],shape)
    cuts=[]
    for summary in summaries:
        orders={r['subgroup_order'] for r in summary};points=set()
        for record in report['ideal_classes']:
            if len(record['subgroup']) in orders:
                points.update(catalog.helper.conjugates_and_cosets(G,record['subgroup'])[1])
        cuts.append(sorted(points))
    return cuts,receipt


def run(seconds,output,control=False,max_models=100):
    from pysat.card import CardEnc
    from pysat.formula import IDPool
    from pysat.solvers import Glucose4
    started=time.monotonic();G=group();shape=[18,1,1] if control else [18,18,25]
    cuts,receipt=all_cuts(shape)
    pool=IDPool();members=[[pool.id(('member',f,g)) for g in range(504)] for f in range(3)]
    clauses=[]
    for f,size in enumerate(shape):
        clauses.extend(CardEnc.equals(members[f],bound=size,vpool=pool).clauses)
        clauses.append([members[f][0]])
        clauses.extend([[-members[f][g] for g in C] for C in cuts[f]])
    # Simultaneous conjugation preserves the source, all coordinate support
    # equations and the complete cut family. Some nonidentity first-set
    # point can therefore be moved to a canonical conjugacy representative.
    classes,_,_=catalog.helper.projection.class_data()
    clauses.append([members[0][min(C)] for C in classes if 0 not in C])
    representatives=sorted({min(g,G['inv'][g]) for g in range(1,504)})
    for g in representatives:
        difference=[pool.id(('difference',f,g)) for f in range(3)]
        clauses.extend([[-difference[f],-difference[h]] for f,h in [(0,1),(1,2),(2,0)]])
        for f in range(3):
            for t in range(504):
                u=G['mul'][g][t]
                if g==G['inv'][g] and u<t:continue
                clauses.append([-members[f][t],-members[f][u],difference[f]])
    solver=Glucose4(bootstrap_with=clauses)
    search_started=time.monotonic()
    report={'group':G['name'],'shape':shape,'positive_control_only':control,
            'frame':'all three vertex sets free in the full group; identity in each; simultaneous conjugacy normalization',
            'minimal_subgroup_cuts_per_leg':list(map(len,cuts)),
            'catalog_subgroups_verified':receipt['subgroups'],'catalog_classes_verified':receipt['conjugacy_classes'],
            'variables':pool.top,'initial_clauses':len(clauses),
            'seconds_requested':seconds,'model_limit':max_models,'preflight_and_build_seconds':search_started-started,
            'models':0,'cuts':[],'witness':None,'status':'running',
            'unsat_proof_checked':False,'all_coordinate_targets_excluded':False,'improves_omega':False}
    output.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['search_elapsed_seconds']=time.monotonic()-search_started
        report['elapsed_seconds']=time.monotonic()-started
        temporary=output.with_suffix('.tmp');temporary.write_text(json.dumps(report,indent=2)+'\n');temporary.replace(output)
    save()
    try:
        while report['models']<max_models:
            remaining=seconds-(time.monotonic()-search_started)
            if remaining<=0:report['status']='time-limit';break
            timer=threading.Timer(remaining,solver.interrupt);timer.start()
            try:solved=solver.solve_limited(expect_interrupt=True)
            finally:timer.cancel()
            if solved is None:report['status']='time-limit';break
            if not solved:report['status']='solver-reported UNSAT; no proof trace';break
            model={x for x in solver.get_model() if x>0}
            sets=[[g for g,lit in enumerate(row) if lit in model] for row in members]
            for f,h in [(0,1),(1,2),(2,0)]:pair_map(G,sets[f],sets[h])
            report['models']+=1;report['pending_candidate']=sets;save()
            lazy=discover(G,sets,max_rounds=60,violation_batch=500,seed=20261023)
            decision,relations=lazy['decision'],lazy['relations'];report.pop('pending_candidate')
            if decision is None:
                report['status']='lazy LP unresolved';report['unresolved_candidate']=sets;break
            if 'potentials' in decision:
                report['witness']={'sets':sets,'potentials':decision['potentials'],
                                   'verification':lazy['verification']}
                report['status']='exact-degeneration-witness';break
            selected=[relations[i] for i in decision['indices']];used=set()
            for row in selected:
                s,t,tt,u,uu,ss=row['vertices']
                used.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                             (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
            cut={'sets':sets,'members':sorted(used),'vertices':[r['vertices'] for r in selected],
                 'rows':[r['row'] for r in selected],'weights':decision['weights']}
            verify_cut(G,cut,shape)
            solver.add_clause([-members[f][g] for f,g in sorted(used)])
            report['cuts'].append(cut);save()
        else:report['status']='model-limit'
        save()
    finally:solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','witness']},indent=2))
    return report


def verify_report(report):
    expected=[18,1,1] if report['positive_control_only'] else [18,18,25]
    if (report['group']!='SL(2,F8)' or report['shape']!=expected or report['unsat_proof_checked'] is not False
            or report['all_coordinate_targets_excluded'] is not False or report['improves_omega'] is not False):
        raise ValueError('incorrect source, format or claim scope')
    statuses={'time-limit','solver-reported UNSAT; no proof trace','model-limit',
              'lazy LP unresolved','exact-degeneration-witness'}
    if report['status'] not in statuses:raise ValueError('only terminal reports can be accepted')
    if bool(report['witness'])!=(report['status']=='exact-degeneration-witness'):
        raise ValueError('witness status does not match its evidence')
    if bool(report.get('unresolved_candidate'))!=(report['status']=='lazy LP unresolved'):
        raise ValueError('unresolved status does not match its candidate')
    if report['status']=='model-limit' and report['models']!=report['model_limit']:
        raise ValueError('model limit was not reached')
    G=group();shape=report['shape']
    for cut in report['cuts']:verify_cut(G,cut,shape)
    witness=report['witness']
    if witness:
        if list(map(len,witness['sets']))!=shape or any(0 not in row for row in witness['sets']):
            raise ValueError('witness left the selected normalized format')
        if verify_stream_witness(G,witness['sets'],witness['potentials'])!=witness['verification']:
            raise ValueError('wrong complete source witness receipt')
    unresolved=report.get('unresolved_candidate')
    if unresolved:
        if list(map(len,unresolved))!=shape:raise ValueError('wrong unresolved format')
        for f,h in [(0,1),(1,2),(2,0)]:pair_map(G,unresolved[f],unresolved[h])
    if report['models']!=len(report['cuts'])+int(bool(witness))+int(bool(unresolved)):
        raise ValueError('incomplete terminal model accounting')
    return {'group':G['name'],'shape':shape,'exact_cuts_replayed':len(report['cuts']),
            'exact_witness_replayed':bool(witness),'reported_status':report['status'],
            'unsat_proof_checked':False,'all_coordinate_targets_excluded':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds',type=float,default=600)
    parser.add_argument('--max-models',type=int,default=100)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--control',action='store_true')
    parser.add_argument('--verify',type=Path)
    args=parser.parse_args()
    if args.verify:print(json.dumps(verify_report(json.loads(args.verify.read_text())),indent=2))
    else:
        if args.output is None:parser.error('--output is required for discovery')
        run(args.seconds,args.output,args.control,args.max_models)
