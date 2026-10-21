"""Variable affine-plane discovery for (19,19,19) in F8^2:C7.

The fifteen three-point fibers may choose separate planes; each of the six
two-point fibers chooses its own direction. A fixed complementary base
triple is the only direction data prescribed. All offsets vary.
"""
from itertools import combinations,product
import argparse
import json
from pathlib import Path
import random
import threading
import time

from pysat.solvers import Glucose4
from quaternary_linear_search import LinearCNF,plus
from quaternary_directions import sumspace
from octal_group import group,fm,inverse
from octal_offset_search import scalar_vector
from group_exact import verify_farkas
from stream_potentials import discover


class NativeLinearCNF(LinearCNF):
    def __init__(self):
        super().__init__();self.xors=[]

    def literal(self,form):
        mask,constant=form
        if mask not in self.forms:
            v=self.pool.id(('linear',mask));self.forms[mask]=v
            remaining=mask;inputs=[]
            while remaining:
                bit=remaining&-remaining;remaining^=bit
                inputs.append(self.inputs[bit.bit_length()-1])
            self.xors.append(([v,*inputs],False))
        return -self.forms[mask] if constant else self.forms[mask]


class CryptoAdapter:
    def __init__(self,cnf):
        from pycryptosat import Solver
        self.solver=Solver(threads=1);self.input_set=set(cnf.inputs)
        for clause in cnf.clauses:self.solver.add_clause(clause)
        for variables,rhs in cnf.xors:self.solver.add_xor_clause(variables,rhs)
        self.control_assumptions=[];self.solution=None;self.calls=0

    def set_phases(self,phases):
        # The native API has no phase-setting method. Use the exact known
        # input assignment as one explicit control, then solve freely.
        self.control_assumptions=[v for v in phases if abs(v) in self.input_set]

    def solve_for(self,seconds):
        control=bool(self.control_assumptions);self.calls+=1
        result,self.solution=self.solver.solve(assumptions=self.control_assumptions,time_limit=seconds)
        if control and result is False:raise ArithmeticError('native solver rejects the audited control')
        if result is not None:self.control_assumptions=[]
        return result

    def get_model(self):
        return [i if v else -i for i,v in enumerate(self.solution) if i]

    def add_clause(self,clause):self.solver.add_clause(clause)
    def accum_stats(self):return {'native_calls':self.calls,'variables':self.solver.nb_vars()}
    def delete(self):self.solver=None


def basis(seed):
    if seed==0:return [1,8,2,16,4,32]
    rng=random.Random(seed)
    while True:
        cols=rng.sample(range(1,64),6)
        if len(sumspace(*[{0,x} for x in cols]))==64:return cols


def build(base,native=False):
    cnf=NativeLinearCNF() if native else LinearCNF()
    offsets=[{},{},{}];columns=[{},{},{}];points=[{},{},{}];membership=[{},{},{}]
    for f in range(3):
        for a in range(1,8):
            offsets[f][a]=[(0,0) if a==1 else cnf.input(('offset',f,a,k)) for k in range(6)]
            columns[f][a]=[]
            for j in range(2 if a<6 else 1):
                col=[]
                for k in range(6):
                    if a==1:col.append((0,int(k==2*f+j)))
                    elif a<6 and k//2==f:col.append((0,int(k%2==j)))
                    else:col.append(cnf.input(('direction',f,a,j,k)))
                columns[f][a].append(col)
            abstract=[offsets[f][a],*[ [plus(u,v) for u,v in zip(offsets[f][a],col)]
                                       for col in columns[f][a]]]
            points[f][a]=[[plus(*(vec[j] for j in range(6) if base[j]&(1<<k)))
                            for k in range(6)] for vec in abstract]
    for form in offsets[0][2]:cnf.clauses.append([-cnf.literal(form)])
    # In an abelian normal subgroup, each three-point difference set is its
    # full plane. Thus every mixed fiber triple must have independent columns.
    for a,b,c in product(range(1,8),repeat=3):
        cols=columns[0][a]+columns[1][b]+columns[2][c]
        for mask in range(1,1<<len(cols)):
            cnf.nonzero([plus(*(cols[j][k] for j in range(len(cols)) if mask&(1<<j)))
                         for k in range(6)])
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in range(1,8):
            edges=[]
            for a in range(1,8):
                b=fm(a,q)
                for x,y in product(points[f][a],points[g][b]):
                    edges.append(scalar_vector(inverse(a),[plus(u,v) for u,v in zip(x,y)]))
            for left,right in combinations(edges,2):cnf.nonzero([plus(u,v) for u,v in zip(left,right)])
    for f in range(3):
        for a in range(1,8):
            equalities=[]
            for j,vec in enumerate(points[f][a]):
                eqs=[]
                for v in range(64):
                    eq=cnf.pool.id(('point-equality',f,a,j,v));eqs.append(eq)
                    conditions=[cnf.literal(form) if v&(1<<k) else -cnf.literal(form)
                                for k,form in enumerate(vec)]
                    cnf.clauses.extend([[-eq,lit] for lit in conditions])
                    cnf.clauses.append([eq,*[-lit for lit in conditions]])
                equalities.append(eqs)
            membership[f][a]=[]
            for v in range(64):
                member=cnf.pool.id(('member',f,a,v));membership[f][a].append(member)
                causes=[row[v] for row in equalities]
                cnf.clauses.extend([[-eq,member] for eq in causes])
                cnf.clauses.append([-member,*causes])
    return cnf,points,membership


def known_phases(cnf,points,base,path):
    """Audit the full encoding on a previously verified pair-injective set."""
    source=json.loads(path.read_text())
    if source['base_columns']!=base:raise ValueError('phase-control base differs')
    sets=source['cuts'][0]['sets'];cells=[{} for _ in range(3)]
    inverse_base={}
    for abstract in range(64):
        actual=0
        for j in range(6):
            if abstract&(1<<j):actual^=base[j]
        inverse_base[actual]=abstract
    offsets=[{} for _ in range(3)]
    for f in range(3):
        for a in range(1,8):
            cells[f][a]={g%64 for g in sets[f] if g//64+1==a}
            P=[0,*base[2*f:2*f+2]] if a<6 else [0,base[2*f]]
            candidates=[v for v in range(64) if {p^v for p in P}==cells[f][a]]
            if not candidates:raise ValueError('control cell is not in this parameterization')
            offsets[f][a]=inverse_base[min(candidates)]
    values={};input_word=0;positive_inputs=set()
    for j,var in enumerate(cnf.inputs):
        key=cnf.pool.obj(var);kind,f,a=key[:3]
        if kind=='offset':value=bool(offsets[f][a]&(1<<key[3]))
        elif kind=='direction':value=(a>=6 and key[4]==2*f)
        else:raise ValueError('unknown input type')
        values[var]=value
        if value:input_word|=1<<j;positive_inputs.add(var)
    actual_points=[{a:[sum(cnf.value(form,positive_inputs)<<k for k,form in enumerate(vec))
                       for vec in cell] for a,cell in row.items()} for row in points]
    for var in range(1,cnf.pool.top+1):
        if var in values:continue
        key=cnf.pool.obj(var);kind=key[0]
        if kind=='false':value=False
        elif kind=='linear':value=bool((key[1]&input_word).bit_count()%2)
        elif kind=='point-equality':
            _,f,a,j,v=key;value=actual_points[f][a][j]==v
        elif kind=='member':
            _,f,a,v=key;value=v in actual_points[f][a]
        else:raise ValueError('unknown auxiliary type')
        values[var]=value
    for i,clause in enumerate(cnf.clauses):
        if not any(values[abs(lit)]==(lit>0) for lit in clause):
            raise ArithmeticError(f'known control falsifies encoding clause {i}')
    for i,(variables,rhs) in enumerate(getattr(cnf,'xors',[])):
        if bool(sum(values[v] for v in variables)%2)!=rhs:
            raise ArithmeticError(f'known control falsifies native XOR {i}')
    return ([var if value else -var for var,value in sorted(values.items())],
            {'source':path.name,'variables_checked':len(values),
             'clauses_checked':len(cnf.clauses),
             'native_xors_checked':len(getattr(cnf,'xors',[])),
             'status':'Exact complete CNF control; pair injection is not a degeneration witness'})


def run(seed,seconds,max_models,output,phase_report=None,engine='glucose4',vary_plane=False):
    started=time.monotonic()
    base=json.loads(phase_report.read_text())['base_columns'] if phase_report else basis(seed)
    G=group();cnf,points,membership=build(base,engine=='cryptominisat')
    solver=CryptoAdapter(cnf) if engine=='cryptominisat' else Glucose4(bootstrap_with=cnf.clauses,use_timer=True)
    report={'group':G['name'],'shape':[19]*3,'base_seed':seed,'base_columns':base,
      'ansatz':__doc__,'engine':engine,'encoding':{'input_bits':len(cnf.inputs),'variables':cnf.pool.top,
                                  'clauses':len(cnf.clauses),'native_xors':len(getattr(cnf,'xors',[]))},
      'seconds_requested':seconds,'model_limit':max_models,'models':0,'cuts':[],
      'witness':None,'status':'running','improves_omega':False}
    plane_variables=[v for v in cnf.inputs if cnf.pool.obj(v)[0]=='direction' and cnf.pool.obj(v)[2]<6]
    variation_active=False
    if phase_report:
        phases,audit=known_phases(cnf,points,base,phase_report)
        solver.set_phases(phases);report['known_pair_model_control']=audit
        report['base_source']=phase_report.name
    elif vary_plane:
        solver.add_clause(plane_variables);variation_active=True
    report['require_changed_plane']=vary_plane
    output.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds']=time.monotonic()-started;report['sat_statistics']=solver.accum_stats()
        tmp=output.with_suffix('.tmp');tmp.write_text(json.dumps(report,separators=(',',':'))+'\n');tmp.replace(output)
    save()
    while report['models']<max_models:
        remaining=seconds-(time.monotonic()-started)
        if remaining<=0:report['status']='time-limit';break
        if engine=='cryptominisat':solved=solver.solve_for(remaining)
        else:
            timer=threading.Timer(remaining,solver.interrupt);timer.start()
            try:solved=solver.solve_limited(expect_interrupt=True)
            finally:timer.cancel()
        if solved is None:report['status']='time-limit';break
        if not solved:report['status']='solver-reported UNSAT; no proof trace';break
        model={v for v in solver.get_model() if v>0};report['models']+=1;sets=[]
        if variation_active and not any(v in model for v in plane_variables):
            raise ArithmeticError('required plane change is absent')
        for f in range(3):
            selected=sorted((a-1)*64+sum(cnf.value(form,model)<<k for k,form in enumerate(vec))
                            for a,cell in points[f].items() for vec in cell)
            encoded={(a-1)*64+v for a in range(1,8) for v,lit in enumerate(membership[f][a]) if lit in model}
            if len(set(selected))!=19 or encoded!=set(selected):raise ArithmeticError('bad point encoding')
            sets.append(selected)
        lazy=discover(G,sets,max_rounds=40,violation_batch=300);decision=lazy['decision'];relations=lazy['relations']
        if decision is None:
            report['status']='lazy LP unresolved';report['unresolved_candidate']=sets;save();break
        if 'potentials' in decision:
            report['witness']={'sets':sets,'potentials':decision['potentials'],'verification':lazy['verification']}
            report['status']='exact-degeneration-witness';save();break
        if not verify_farkas(relations,decision['indices'],decision['weights']):raise ArithmeticError('bad circuit')
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
        if vary_plane and not variation_active:
            solver.add_clause(plane_variables);variation_active=True
        if report['models']<10 or report['models']%10==0:save()
    else:report['status']='model-limit'
    save();solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','witness']},indent=2))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-seed',type=int,default=0)
    parser.add_argument('--seconds',type=float,default=180)
    parser.add_argument('--max-models',type=int,default=1000)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--phase-report',type=Path)
    parser.add_argument('--engine',choices=['glucose4','cryptominisat'],default='glucose4')
    parser.add_argument('--vary-plane',action='store_true')
    args=parser.parse_args();run(args.base_seed,args.seconds,args.max_models,args.output,args.phase_report,args.engine,args.vary_plane)
