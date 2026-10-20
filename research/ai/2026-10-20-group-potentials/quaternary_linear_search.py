"""Search all six graph planes and offsets over fixed base F4 coordinate lines.

The 72 initial Boolean variables describe six 2x4 graph matrices and six
four-bit affine offsets. Pair-label injectivity and normal-fiber triple
tilings are bit-blasted exactly. SAT/LP are discovery tools only.
"""
from __future__ import annotations
import argparse
import json
from itertools import combinations,product
from pathlib import Path
import threading
import time
import random

from pysat.formula import IDPool
from pysat.solvers import Glucose4

from quaternary_group import group,scale
from quaternary_directions import crossed_mean_rows,cyclic_shears,sumspace
from group_exact import extra_relations,verify_farkas,verify_witness
from search import potential_or_circuit


class LinearCNF:
    def __init__(self):
        self.pool=IDPool();self.clauses=[];self.forms={};self.inputs=[]
        self.zero=self.pool.id(('false',));self.clauses.append([-self.zero])
        self.forms[0]=self.zero

    def input(self,key):
        v=self.pool.id(key);self.inputs.append(v)
        mask=1<<(len(self.inputs)-1);self.forms[mask]=v
        return (mask,0)

    def literal(self,form):
        mask,constant=form
        if mask not in self.forms:
            bit=mask&-mask
            a=self.literal((bit,0));b=self.literal((mask^bit,0))
            v=self.pool.id(('linear',mask));self.forms[mask]=v
            self.clauses.extend([[a,b,-v],[-a,-b,-v],[a,-b,v],[-a,b,v]])
        v=self.forms[mask]
        return -v if constant else v

    def nonzero(self,forms):
        if any(mask==0 and c for mask,c in forms):return
        self.clauses.append([self.literal(f) for f in forms if f[0]])

    def value(self,form,model):
        mask,c=form
        while mask:
            bit=mask&-mask;mask^=bit
            c^=self.inputs[bit.bit_length()-1] in model
        return int(c)


def plus(*forms):
    mask=0;c=0
    for m,d in forms:mask^=m;c^=d
    return mask,c


def scalar_vector(a,vec):
    result=[]
    for j in range(3):
        # F4 scalar multiplication is F2-linear.
        x,y=vec[2*j:2*j+2]
        for bit in [1,2]:
            parts=[]
            if scale(a,1)&bit:parts.append(x)
            if scale(a,2)&bit:parts.append(y)
            result.append(plus(*parts))
    return result


def base_columns(pattern='cyclic',seed=0):
    if pattern=='coordinate':return [1<<k for k in range(6)]
    if pattern=='cyclic':
        planes=cyclic_shears((7,7,7))
        return [planes[f][1][x] for f in range(3) for x in [1,2]]
    if pattern=='random':
        rng=random.Random(seed)
        while True:
            columns=rng.sample(range(1,64),6)
            if len(sumspace(*[{0,x} for x in columns]))==64:return columns
    raise ValueError('unknown base pattern')


def build(base_pattern='cyclic',base_seed=0):
    cnf=LinearCNF();directions=[{},{},{}];offsets=[{},{},{}]
    direction_inputs=[]
    for f in range(3):
        for a in [1,2,3]:
            columns=[];offset=[]
            for k in range(6):
                if k//2==f:
                    offset.append((0,0))
                elif a==1:
                    offset.append((0,0))
                else:offset.append(cnf.input(('offset',f,a,k)))
            for j in [0,1]:
                col=[]
                for k in range(6):
                    if k//2==f:col.append((0,int(k%2==j)))
                    elif a==1:col.append((0,0))
                    else:
                        value=cnf.input(('direction',f,a,j,k));col.append(value)
                        direction_inputs.append(cnf.literal(value))
                columns.append(col)
            directions[f][a]=columns;offsets[f][a]=offset
    points=[{},{},{}]
    for f in range(3):
        for a in [1,2,3]:
            points[f][a]=[[plus(offsets[f][a][k],
               *(directions[f][a][j][k] for j in [0,1] if x&(1<<j)))
               for k in range(6)] for x in range(4)]
    base=base_columns(base_pattern,base_seed)
    for row in points:
        for a,cell in row.items():
            row[a]=[[plus(*(vec[j] for j in range(6) if base[j]&(1<<k)))
                      for k in range(6)] for vec in cell]
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in [1,2,3]:
            edge=[]
            for a in [1,2,3]:
                from quaternary_group import fm
                b=fm(a,q)
                for x,y in product(range(4),repeat=2):
                    edge.append(scalar_vector(fm(a,a),
                        [plus(u,v) for u,v in zip(points[f][a][x],points[g][b][y])]))
            for left,right in combinations(edge,2):
                cnf.nonzero([plus(u,v) for u,v in zip(left,right)])
    for a,b,c in product([1,2,3],repeat=3):
        columns=directions[0][a]+directions[1][b]+directions[2][c]
        for mask in range(1,64):
            cnf.nonzero([plus(*(columns[j][k] for j in range(6) if mask&(1<<j)))
                         for k in range(6)])
    for row in points:
        for cell in row.values():
            for vec in cell:
                for form in vec:cnf.literal(form)
    return cnf,points,directions,direction_inputs


def run(seconds,max_models,output,base_pattern='cyclic',base_seed=0):
    started=time.monotonic();G=group();cnf,points,directions,direction_inputs=build(base_pattern,base_seed)
    solver=Glucose4(bootstrap_with=cnf.clauses,use_timer=True)
    report={'group':G['name'],'shape':[12,12,12],
        'ansatz':'One affine F2-plane per scalar coset; six other planes and offsets vary over a fixed complementary base triple.',
        'base_pattern':base_pattern,'base_seed':base_seed,'base_columns':base_columns(base_pattern,base_seed),
        'encoding':{'input_bits':len(cnf.inputs),'variables':cnf.pool.top,'clauses':len(cnf.clauses)},
        'pair_models':0,'mean_cuts':[],'point_cuts':[],'witness':None,
        'seconds_requested':seconds,'model_limit':max_models,'status':'running','improves_omega':False}
    output.parent.mkdir(parents=True,exist_ok=True)
    index={g:i for i,g in enumerate(G['matrices'])}
    def save():
        report['elapsed_seconds']=time.monotonic()-started
        report['sat_statistics']=solver.accum_stats()
        tmp=output.with_suffix('.tmp');tmp.write_text(json.dumps(report,separators=(',',':'))+'\n');tmp.replace(output)
    save()
    while report['pair_models']<max_models:
        remaining=seconds-(time.monotonic()-started)
        if remaining<=0:report['status']='time-limit';break
        timer=threading.Timer(remaining,solver.interrupt);timer.start()
        try:solved=solver.solve_limited(expect_interrupt=True)
        finally:timer.cancel()
        if solved is None:report['status']='time-limit';break
        if not solved:report['status']='solver-reported UNSAT; no proof trace';break
        model={v for v in solver.get_model() if v>0};report['pair_models']+=1
        actual=[{},{},{}];sets=[];forms_by_point={}
        for f in range(3):
            selected=[]
            for a in [1,2,3]:
                actual[f][a]=[]
                for x in range(4):
                    vec=points[f][a][x]
                    v=sum(cnf.value(form,model)<<k for k,form in enumerate(vec))
                    g=index[(a,v)];selected.append(g);forms_by_point[f,g]=vec
                    actual[f][a].append(sum(cnf.value(plus(form,points[f][a][0][k]),model)<<k
                                                   for k,form in enumerate(vec)))
            sets.append(sorted(selected))
        mean_rows=crossed_mean_rows(actual);mean=potential_or_circuit(mean_rows,9)
        if 'potentials' not in mean:
            if not verify_farkas(mean_rows,mean['indices'],mean['weights']):
                raise ArithmeticError('invalid crossed-mean circuit')
            solver.add_clause([-v if v in model else v for v in direction_inputs])
            report['mean_cuts'].append({'actual_planes':actual,
               'rows':[mean_rows[i] for i in mean['indices']], 'weights':mean['weights']})
        else:
            relations,intended=extra_relations(G,sets)
            decision=potential_or_circuit(relations,36)
            if 'potentials' in decision:
                report['witness']={'sets':sets,'potentials':decision['potentials'],
                   'verification':verify_witness(G,sets,decision['potentials'])}
                report['status']='exact-degeneration-witness';save();break
            if not verify_farkas(relations,decision['indices'],decision['weights']):
                raise ArithmeticError('invalid point circuit')
            members=set()
            for i in decision['indices']:
                s,t,tt,u,uu,ss=relations[i]['vertices']
                members.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                                (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
            clause=set()
            for member in members:
                for form in forms_by_point[member]:
                    if not form[0]:continue
                    lit=cnf.literal(form);value=(abs(lit) in model)==(lit>0)
                    clause.add(-lit if value else lit)
            # Point coordinate forms were materialized by the pair constraints.
            # Check that no new XOR auxiliaries were introduced after solving.
            if cnf.pool.top>solver.nof_vars():raise ArithmeticError('unmaterialized point form')
            solver.add_clause(sorted(clause,key=lambda v:(abs(v),v)))
            report['point_cuts'].append({'sets':sets,
                'vertices':[relations[i]['vertices'] for i in decision['indices']],
                'rows':[relations[i]['row'] for i in decision['indices']],
                'weights':decision['weights']})
        if report['pair_models']%10==0:save()
    else:report['status']='model-limit'
    save();solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['mean_cuts','point_cuts','witness']},indent=2))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds',type=float,default=180)
    parser.add_argument('--max-models',type=int,default=2000)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--base-pattern',choices=['cyclic','coordinate','random'],default='cyclic')
    parser.add_argument('--base-seed',type=int,default=0)
    args=parser.parse_args();run(args.seconds,args.max_models,args.output,args.base_pattern,args.base_seed)
