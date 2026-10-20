"""Exact symmetries of the 56-point cubic parent and orbit hitting discovery."""
from itertools import product
import argparse
import json
from pathlib import Path
import threading
import time

from octal_group import fm


def position_map(f,j,lam,translations,rotation):
    a,x=divmod(j,8);a+=1
    y=fm(fm(lam,lam),x^fm(a,translations[f]))
    return (f+rotation)%3,(fm(lam,a)-1)*8+y


def core_orbit(core):
    return sorted({tuple(sorted(position_map(f,j,lam,t,rotation) for f,j in core))
       for lam in range(1,8) for t in product(range(8),repeat=3) for rotation in range(3)})


def verify_actions(source):
    from octal_group import cubic_group,cubic_parent
    from stream_potentials import relation
    from verify_stream_reports import verify_cut
    data=json.loads(source.read_text());G=cubic_group();parent=cubic_parent(G)
    seed=min(data['cuts'],key=lambda c:len(c['members']));count=0
    for lam in range(1,8):
        for translations in product(range(8),repeat=3):
            for rotation in range(3):
                sets=[None]*3
                for f,row in enumerate(seed['sets']):
                    mapped=[]
                    for g in row:
                        ff,j=position_map(f,parent[f].index(g),lam,translations,rotation)
                        mapped.append(parent[ff][j])
                    sets[(f+rotation)%3]=mapped
                vertices=[]
                for row in seed['vertices']:
                    step=2*rotation
                    vertices.append(row[-step:]+row[:-step] if step else row[:])
                rows=[relation(v,[48,48,48])['row'] for v in vertices];members=set()
                for s,t,tt,u,uu,ss in vertices:
                    members.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                                    (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
                cut={'sets':sets,'vertices':vertices,'rows':rows,'weights':seed['weights'],
                     'members':sorted(members)}
                verify_cut(G,cut,[48,48,48],parent);count+=1
    return {'group':G['name'],'transformed_integer_circuits_checked':count,
            'group_support_relations_checked':count*len(seed['vertices']),
            'seed_core_size':len(seed['members']),
            'orbit_hitting_clauses_validated':len(core_orbit([(f,parent[f].index(g)) for f,g in seed['members']])),
            'scope':'Every orbit clause is a necessary deletion constraint. No SAT '
                    'UNSAT proof or full-parent nonexistence is checked here.',
            'improves_omega':False}


def run(source,seconds,output):
    from pysat.card import CardEnc,EncType
    from pysat.formula import IDPool
    from pysat.solvers import Glucose4
    started=time.monotonic();data=json.loads(source.read_text())
    seed=min(data['cuts'],key=lambda c:len(c['members']))
    parent=data['parent_sets'];core=[(f,parent[f].index(g)) for f,g in seed['members']]
    orbit=core_orbit(core);pool=IDPool()
    holes=[[pool.id(('hole',f,j)) for j in range(56)] for f in range(3)]
    clauses=[]
    for row in holes:clauses.extend(CardEnc.equals(row,8,vpool=pool,encoding=EncType.seqcounter).clauses)
    clauses.extend([[holes[f][j] for f,j in edge] for edge in orbit])
    solver=Glucose4(bootstrap_with=clauses,with_proof=True)
    timer=threading.Timer(seconds,solver.interrupt);timer.start()
    try:solved=solver.solve_limited(expect_interrupt=True)
    finally:timer.cancel()
    result={'group':data['group'],'shape':[48,48,48],'seed_circuit':seed,
        'core_parent_positions':core,'symmetry_orbit_clauses':len(orbit),
        'encoding_variables':pool.top,'encoding_clauses':len(clauses),
        'solver_result':solved,'sat_statistics':solver.accum_stats(),
        'seconds_requested':seconds,'elapsed_seconds':time.monotonic()-started,
        'scope':'Necessary hitting constraints from one exact circuit and parent '
                'symmetries. SAT is not a potential witness; UNSAT requires '
                'independent proof replay before use as a certified exclusion.',
        'improves_omega':False,'unsat_proof_checked':False}
    if solved:
        model={v for v in solver.get_model() if v>0}
        selected=[[(f,j) for j in range(56) if holes[f][j] in model] for f in range(3)]
        chosen={pair for row in selected for pair in row}
        if any(not chosen.intersection(edge) for edge in orbit):
            raise ArithmeticError('invalid hitting assignment')
        result['hole_positions']=[[j for f,j in row] for row in selected]
    elif solved is False:
        proof=solver.get_proof();proof_path=output.with_suffix('.drup')
        proof_path.write_text('\n'.join(proof)+'\n')
        result['unverified_proof_file']=proof_path.name;result['proof_lines']=len(proof)
    solver.delete();output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='seed_circuit'},indent=2))
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True)
    parser.add_argument('--seconds',type=float,default=120)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();run(args.source,args.seconds,args.output)
