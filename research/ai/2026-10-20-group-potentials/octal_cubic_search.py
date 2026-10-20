"""Delete eight vertices per family from an explicit pair-injective source.

The parent sets have 56 vertices in F8^3:C7. The search targets 48 per set.
Every learned clause is an exact integer Farkas obstruction; no bound follows
unless a full positive-potential witness is verified.
"""
from itertools import product
import argparse
import json
from pathlib import Path
import threading
import time

from pysat.card import CardEnc,EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose4

from octal_group import cubic_group,cubic_parent
from group_exact import pair_map,verify_farkas,verify_witness
from search import potential_or_circuit
from stream_potentials import discover


def find_relations(G,sets,prefix_limit=20000):
    """Return an exact opposite pair early, or a verified finite prefix.

    A prefix suffices to reject. Acceptance must check the entire support.
    """
    S,T,U=sets;n,m,p=map(len,sets)
    X,Y,Z=pair_map(G,S,T),pair_map(G,T,U),pair_map(G,U,S)
    rows={};intended=0;exhausted=True
    for x,(s,t) in X.items():
        for y,(tt,u) in Y.items():
            z=G['inv'][G['mul'][x][y]]
            if z not in Z:continue
            uu,ss=Z[z]
            if (s,t,u)==(ss,tt,uu):intended+=1;continue
            row=[0]*(n+m+p)
            for j,sgn in [(s,1),(ss,-1),(n+tt,1),(n+t,-1),(n+m+uu,1),(n+m+u,-1)]:row[j]+=sgn
            key=tuple(row);opposite=tuple(-v for v in key)
            item={'row':key,'vertices':[s,t,tt,u,uu,ss]}
            if opposite in rows:
                return [rows[opposite],item],False,{'indices':[0,1],'weights':[1,1]}
            rows[key]=item
            if len(rows)>=prefix_limit:return list(rows.values()),False,None
    if intended!=n*m*p:raise ArithmeticError('corrupted intended support')
    return list(rows.values()),True,None


def run(seconds,max_models,output):
    started=time.monotonic();G=cubic_group();parent=cubic_parent(G)
    for f,g in [(0,1),(1,2),(2,0)]:
        if len(pair_map(G,parent[f],parent[g]))!=56**2:raise ArithmeticError('bad parent pair map')
    pool=IDPool();holes=[[pool.id(('hole',f,j)) for j in range(56)] for f in range(3)]
    clauses=[]
    for row in holes:clauses.extend(CardEnc.equals(row,8,vpool=pool,encoding=EncType.seqcounter).clauses)
    solver=Glucose4(bootstrap_with=clauses,use_timer=True)
    report={'group':G['name'],'shape':[48,48,48],'parent_sets':parent,
        'parent_pair_maps_verified':[3136]*3,'parent_sizes':[56]*3,
        'holes_per_family':8,'seconds_requested':seconds,'models_limit':max_models,
        'models':0,'cuts':[],'witness':None,'status':'running','improves_omega':False,
        'scope':'Restricted deletion ansatz. A prefix can reject but cannot accept; '
                'any potential candidate must undergo complete support verification.'}
    output.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        report['sat_statistics']=solver.accum_stats()
        tmp=output.with_suffix('.tmp');tmp.write_text(json.dumps(report,separators=(',',':'))+'\n');tmp.replace(output)
    save()
    while report['models']<max_models:
        remaining=seconds-(time.monotonic()-started)
        if remaining<=0:report['status']='time-limit';break
        timer=threading.Timer(remaining,solver.interrupt);timer.start()
        try:solved=solver.solve_limited(expect_interrupt=True)
        finally:timer.cancel()
        if solved is None:report['status']='time-limit';break
        if not solved:report['status']='solver-reported UNSAT; no proof trace';break
        model={v for v in solver.get_model() if v>0}
        sets=[[g for j,g in enumerate(row) if holes[f][j] not in model] for f,row in enumerate(parent)]
        report['models']+=1
        relations,complete,decision=find_relations(G,sets)
        if decision is None:decision=potential_or_circuit(relations,144)
        if 'potentials' in decision:
            if not complete:
                lazy=discover(G,sets,progress=lambda row:print(json.dumps(row),flush=True))
                report.setdefault('lazy_lp_runs',[]).append(lazy['rounds'])
                relations,complete,decision=lazy['relations'],lazy['complete'],lazy['decision']
                if decision is None:
                    report['status']='lazy LP round limit, unresolved'
                    report['unresolved_candidate']={'sets':sets,'active_relations':len(relations)}
                    save();break
            if 'potentials' in decision:
                from stream_potentials import verify_stream_witness
                verified=verify_stream_witness(G,sets,decision['potentials'])
                report['witness']={'sets':sets,'potentials':decision['potentials'],'verification':verified}
                report['status']='exact-degeneration-witness';save();break
        if not verify_farkas(relations,decision['indices'],decision['weights']):
            raise ArithmeticError('refusing unverified cut')
        members=set()
        for i in decision['indices']:
            s,t,tt,u,uu,ss=relations[i]['vertices']
            members.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                            (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
        solver.add_clause([holes[f][parent[f].index(g)] for f,g in sorted(members)])
        report['cuts'].append({'sets':sets,'members':sorted(members),
            'vertices':[relations[i]['vertices'] for i in decision['indices']],
            'rows':[relations[i]['row'] for i in decision['indices']],
            'weights':decision['weights']})
        if report['models']%25==0:save()
    else:report['status']='model-limit'
    save();solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','parent_sets','witness']},indent=2))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds',type=float,default=180)
    parser.add_argument('--max-models',type=int,default=2000)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();run(args.seconds,args.max_models,args.output)
