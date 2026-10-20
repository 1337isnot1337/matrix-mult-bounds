"""Global affine-offset discovery for the exact F8^2:C7 direction frontier."""
from itertools import combinations
import argparse
import json
from pathlib import Path
import threading
import time

from pysat.solvers import Glucose4
from octal_group import group,fm,inverse
from quaternary_linear_search import LinearCNF,plus
from stream_potentials import discover
from group_exact import verify_farkas


def scalar_vector(a,vec):
    return [plus(*(vec[3*i+j] for j in range(3) if fm(a,1<<j)&(1<<k)))
            for i in range(2) for k in range(3)]


def build(base):
    cnf=LinearCNF();offsets=[{},{},{}];points=[{},{},{}];membership=[{},{},{}]
    for f in range(3):
        for a in range(1,8):
            offsets[f][a]=[(0,0) if a==1 else cnf.input(('offset',f,a,k)) for k in range(6)]
            P=[0,*base[2*f:2*f+2]] if a<6 else [0,base[2*f]]
            points[f][a]=[[plus(offsets[f][a][k],(0,(v>>k)&1)) for k in range(6)] for v in P]
    # Common translation conjugation fixes the identity fibers and can set
    # S's multiplier-two offset to zero. A short two-point fiber is unchanged
    # by translating its offset by its nonzero direction; fix that redundancy.
    for form in offsets[0][2]:cnf.clauses.append([-cnf.literal(form)])
    for f in range(3):
        bit=(base[2*f]&-base[2*f]).bit_length()-1
        for a in [6,7]:cnf.clauses.append([-cnf.literal(offsets[f][a][bit])])
    for f in range(3):
        for a in range(1,8):
            P=[0,*base[2*f:2*f+2]] if a<6 else [0,base[2*f]]
            choices=[]
            for v in range(64):
                choice=cnf.pool.id(('offset-equality',f,a,v));choices.append(choice)
                conditions=[cnf.literal(form) if v&(1<<k) else -cnf.literal(form)
                            for k,form in enumerate(offsets[f][a])]
                cnf.clauses.extend([[-choice,lit] for lit in conditions])
                cnf.clauses.append([choice,*[-lit for lit in conditions]])
            membership[f][a]=[]
            for v in range(64):
                member=cnf.pool.id(('membership',f,a,v));membership[f][a].append(member)
                causes=[choices[v^p] for p in P]
                cnf.clauses.extend([[-choice,member] for choice in causes])
                cnf.clauses.append([-member,*causes])
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in range(1,8):
            edges=[]
            for a in range(1,8):
                b=fm(a,q)
                for x in points[f][a]:
                    for y in points[g][b]:
                        edges.append(scalar_vector(inverse(a),[plus(u,v) for u,v in zip(x,y)]))
            for left,right in combinations(edges,2):
                cnf.nonzero([plus(u,v) for u,v in zip(left,right)])
    return cnf,offsets,points,membership


def run(base,seconds,max_models,output):
    started=time.monotonic();G=group();cnf,offsets,points,membership=build(base)
    solver=Glucose4(bootstrap_with=cnf.clauses,use_timer=True)
    report={'group':G['name'],'shape':[19,19,19],'base_columns':base,
       'encoding':{'input_bits':len(cnf.inputs),'variables':cnf.pool.top,'clauses':len(cnf.clauses)},
       'normalization':'Identity-fiber offsets zero; common conjugation fixes S multiplier-two offset; short-fiber translation redundancy fixed.',
       'learned_cut_encoding':'Exact point-membership clauses, covering every offset assignment that retains the circuit.',
       'seconds_requested':seconds,'models_limit':max_models,'models':0,'cuts':[],
       'witness':None,'status':'running','improves_omega':False,
       'scope':'Fixed constant-direction and short-fiber pattern, all affine offsets. '
               'SAT UNSAT without proof is an experiment only. Full support checks '
               'and integer potentials are required for acceptance.'}
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
        model={v for v in solver.get_model() if v>0};report['models']+=1;sets=[]
        for f in range(3):
            row=[]
            for a in range(1,8):
                for vec in points[f][a]:
                    v=sum(cnf.value(form,model)<<k for k,form in enumerate(vec))
                    row.append((a-1)*64+v)
            sets.append(sorted(row))
        for f in range(3):
            encoded={(a-1)*64+v for a in range(1,8) for v,lit in enumerate(membership[f][a]) if lit in model}
            if encoded!=set(sets[f]):raise ArithmeticError('membership encoding differs from actual point set')
        lazy=discover(G,sets,max_rounds=40,violation_batch=300)
        decision=lazy['decision'];relations=lazy['relations']
        if decision is None:
            report['status']='lazy LP unresolved';report['unresolved_candidate']=sets;save();break
        if 'potentials' in decision:
            report['witness']={'sets':sets,'potentials':decision['potentials'],
                               'verification':lazy['verification']}
            report['status']='exact-degeneration-witness';save();break
        if not verify_farkas(relations,decision['indices'],decision['weights']):
            raise ArithmeticError('invalid offset Farkas circuit')
        members=set()
        for i in decision['indices']:
            s,t,tt,u,uu,ss=relations[i]['vertices']
            members.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                            (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
        solver.add_clause([-membership[f][g//64+1][g%64] for f,g in sorted(members)])
        report['cuts'].append({'sets':sets,'members':sorted(members),
            'vertices':[relations[i]['vertices'] for i in decision['indices']],
            'rows':[relations[i]['row'] for i in decision['indices']],
            'weights':decision['weights'],'lazy_rounds':lazy['rounds']})
        if report['models']%10==0:save()
    else:report['status']='model-limit'
    save();solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','witness']},indent=2))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frontier',type=Path,required=True)
    parser.add_argument('--index',type=int,default=0)
    parser.add_argument('--seconds',type=float,default=120)
    parser.add_argument('--max-models',type=int,default=1000)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();data=json.loads(args.frontier.read_text())
    base=data['surviving_direction_triples'][args.index]['base_columns']
    run(base,args.seconds,args.max_models,args.output)
