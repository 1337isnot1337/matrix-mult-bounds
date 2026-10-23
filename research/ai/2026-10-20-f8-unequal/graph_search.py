"""Optional native-parity discovery for the unequal F8 target (16,20,21).

Four-point fibers may be nonlinear graphs; three-point fibers vary their
planes. Empty fibers, offsets and all allowed graph values are explicit.
Exact full-support integer verification is mandatory for acceptance.
"""
import argparse
from itertools import combinations,product
import json
from pathlib import Path
import sys
import time

PACKAGE = Path(__file__).resolve().parent
sys.path.insert(0,str(PACKAGE.parent/'2026-10-20-group-potentials'))
from octal_group import group,fm,inverse
from octal_variable_planes import NativeLinearCNF,CryptoAdapter
from octal_offset_search import scalar_vector
from quaternary_linear_search import plus
from stream_potentials import discover
from group_exact import verify_farkas
from graph_certificate import check,scalar_order

COUNTS = [[4,4,4,4,0,0,0],[4,4,0,4,4,4,0],[3,3,3,3,3,3,3]]


def base_columns(kind):
    if kind=='generic':
        return [1,8,2,16,4,32]
    def trace(x):
        x2 = fm(x,x)
        return x ^ x2 ^ fm(x2,x2)
    dual = [1,2,8,32,18,36]
    mapping = {}
    for v in range(64):
        key = sum(trace(fm(d & 7,v & 7)^fm(d >> 3,v >> 3)) << j
                  for j,d in enumerate(dual))
        mapping[key] = v
    if len(mapping)!=64:
        raise ArithmeticError('dependent dual normalization')
    return [mapping[1 << j] for j in range(6)]


def build(base,counts):
    cnf = NativeLinearCNF()
    H = scalar_order()
    offsets = [{},{},{}]
    abstract = [{},{},{}]
    points = [{},{},{}]
    members = [{},{},{}]
    for f in range(3):
        for i,a in enumerate(H):
            n = counts[f][i]
            if n not in (0,3,4):
                raise ValueError('this pilot uses only empty, three-point and four-point fibers')
            offsets[f][a] = [(0,0) if a==1 or n==0 else cnf.input(('offset',f,a,k))
                             for k in range(6)]
            abstract[f][a] = []
            for j in range(n):
                vector = []
                for k in range(6):
                    if k//2==f:
                        value = (0,(j >> (k%2)) & 1)
                    elif j==0 or a==1:
                        value = (0,0)
                    else:
                        value = cnf.input(('graph',f,a,j,k))
                    vector.append(plus(offsets[f][a][k],value))
                abstract[f][a].append(vector)
            points[f][a] = [[plus(*(v[j] for j in range(6) if base[j] & (1 << k)))
                              for k in range(6)] for v in abstract[f][a]]
    selected = next((a for i,a in enumerate(H) if a!=1 and counts[0][i]),None)
    if selected is not None:
        for form in offsets[0][selected]:
            cnf.clauses.append([-cnf.literal(form)])
    normal_start = len(cnf.clauses)
    differences = [{},{},{}]
    for f in range(3):
        for a in H:
            cell = abstract[f][a]
            differences[f][a] = ([[(0,0)]*6] +
                [[plus(x,y) for x,y in zip(left,right)] for left,right in combinations(cell,2)]) if cell else []
    for a,b,c in product(H,repeat=3):
        rows = differences[0][a],differences[1][b],differences[2][c]
        if not all(rows):
            continue
        for i,j,k in product(*(range(len(row)) for row in rows)):
            if i==j==k==0:
                continue
            cnf.nonzero([plus(x,y,z) for x,y,z in zip(rows[0][i],rows[1][j],rows[2][k])])
    normal_end = len(cnf.clauses)
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in H:
            edges = []
            for a in H:
                b = fm(a,q)
                edges.extend(scalar_vector(inverse(a),[plus(x,y) for x,y in zip(left,right)])
                             for left,right in product(points[f][a],points[g][b]))
            for left,right in combinations(edges,2):
                cnf.nonzero([plus(x,y) for x,y in zip(left,right)])
    pair_end = len(cnf.clauses)
    for f in range(3):
        for a in H:
            equality = []
            for j,vector in enumerate(points[f][a]):
                row = []
                for v in range(64):
                    eq = cnf.pool.id(('point_eq',f,a,j,v))
                    row.append(eq)
                    conditions = [cnf.literal(form) if v & (1 << k) else -cnf.literal(form)
                                  for k,form in enumerate(vector)]
                    cnf.clauses.extend([[-eq,lit] for lit in conditions])
                    cnf.clauses.append([eq,*[-lit for lit in conditions]])
                equality.append(row)
            members[f][a] = []
            for v in range(64):
                member = cnf.pool.id(('member',f,a,v))
                members[f][a].append(member)
                causes = [row[v] for row in equality]
                cnf.clauses.extend([[-eq,member] for eq in causes])
                cnf.clauses.append([-member,*causes])
    ranges = {'normal_start':normal_start,'normal_end':normal_end,'pair_end':pair_end}
    return cnf,points,members,ranges


def assignment_audit(cnf,points,base,counts,ranges):
    """Audit a triangular nonlinear normal control, expected to fail pairs."""
    H = scalar_order()
    selected = {f:next((a for i,a in enumerate(H) if a!=1 and counts[f][i]==4),None)
                for f in [0,1]}
    word = 0
    for j,var in enumerate(cnf.inputs):
        key = cnf.pool.obj(var)
        if key[0]=='graph':
            _,f,a,label,k = key
            if f in selected and a==selected[f] and label==3 and k==2*(f+1):
                word |= 1 << j
    values = {var:bool((mask & word).bit_count()%2) for mask,var in cnf.forms.items()}
    sets = []
    actual = [{},{},{}]
    for f in range(3):
        row = []
        for a in H:
            actual[f][a] = [sum((((m & word).bit_count()%2)^c) << k
                                for k,(m,c) in enumerate(vector)) for vector in points[f][a]]
            row.extend((a-1)*64+v for v in actual[f][a])
        sets.append(sorted(row))
    for var in range(1,cnf.pool.top+1):
        if var in values:
            continue
        key = cnf.pool.obj(var)
        if key[0]=='point_eq':
            _,f,a,j,v = key
            values[var] = actual[f][a][j]==v
        elif key[0]=='member':
            _,f,a,v = key
            values[var] = v in actual[f][a]
        else:
            raise ArithmeticError('unrecognized audit variable')
    failures = {'normal':0,'pair':0,'definitions':0,'normalization':0}
    for i,clause in enumerate(cnf.clauses):
        if any(values[abs(lit)]==(lit>0) for lit in clause):
            continue
        category = ('normalization' if i<ranges['normal_start'] else
                    'normal' if i<ranges['normal_end'] else
                    'pair' if i<ranges['pair_end'] else 'definitions')
        failures[category] += 1
    xor_failures = sum(bool(sum(values[v] for v in variables)%2)!=rhs
                       for variables,rhs in cnf.xors)
    receipt = check(base,counts,sets,require_pairs=False)
    if failures['normal'] or failures['definitions'] or failures['normalization'] or xor_failures:
        raise ArithmeticError('triangular normal control falsifies a defining constraint')
    pair_valid = all(value is not None for value in receipt['pair_map_sizes'])
    if bool(failures['pair'])==pair_valid:
        raise ArithmeticError('pair encoding disagrees with the independent negative/positive control')
    return {'input_word':str(word),'clause_failures':failures,'xor_failures':xor_failures,
            'variables_checked':len(values),'clauses_checked':len(cnf.clauses),
            'native_xors_checked':len(cnf.xors),'graph_receipt':receipt,
            'scope':'Complete Boolean audit of one triangular normal assignment. '
                    'Pair validity is reported by the independent graph receipt. '
                    'This audit alone is not a strict-potential witness.'}


def run(kind,seconds,max_models,output,control=False):
    started = time.monotonic()
    counts = [[4,0,0,0,0,0,0],[4,0,0,0,0,0,0],[3,0,0,0,0,0,0]] if control else COUNTS
    base = base_columns(kind)
    cnf,points,members,ranges = build(base,counts)
    audit = assignment_audit(cnf,points,base,counts,ranges)
    solver = CryptoAdapter(cnf)
    G = group()
    report = {'group':G['name'],'shape':list(map(sum,counts)),'base_kind':kind,
              'base_columns':base,'fiber_counts':counts,'ansatz':__doc__,
              'positive_control_only':control,'encoding_audit':audit,
              'encoding':{'input_bits':len(cnf.inputs),'variables':cnf.pool.top,
                          'clauses':len(cnf.clauses),'native_xors':len(cnf.xors)},
              'seconds_requested':seconds,'model_limit':max_models,'models':0,
              'cuts':[],'witness':None,'status':'running','improves_omega':False,
              'unsat_proof_checked':False}
    output.parent.mkdir(parents=True,exist_ok=True)
    def save():
        report['elapsed_seconds'] = time.monotonic()-started
        report['sat_statistics'] = solver.accum_stats()
        temporary = output.with_suffix('.tmp')
        temporary.write_text(json.dumps(report,separators=(',',':'))+'\n')
        temporary.replace(output)
    save()
    while report['models']<max_models:
        remaining = seconds-(time.monotonic()-started)
        if remaining<=0:
            report['status'] = 'time-limit'
            break
        solved = solver.solve_for(remaining)
        if solved is None:
            report['status'] = 'time-limit'
            break
        if not solved:
            report['status'] = 'solver-reported UNSAT; no proof trace'
            break
        model = {v for v in solver.get_model() if v>0}
        sets = [sorted((a-1)*64+sum(cnf.value(form,model) << k for k,form in enumerate(vector))
                       for a,cell in row.items() for vector in cell) for row in points]
        for f in range(3):
            encoded = {(a-1)*64+v for a in scalar_order() for v,lit in enumerate(members[f][a]) if lit in model}
            if encoded!=set(sets[f]):
                raise ArithmeticError('membership encoding disagrees with actual vertices')
        receipt = check(base,counts,sets)
        report['models'] += 1
        lazy = discover(G,sets,max_rounds=60,violation_batch=500)
        decision,relations = lazy['decision'],lazy['relations']
        if decision is None:
            report['unresolved_candidate'] = sets
            report['status'] = 'lazy LP unresolved'
            save()
            break
        if 'potentials' in decision:
            report['witness'] = {'sets':sets,'potentials':decision['potentials'],
                                 'verification':lazy['verification'],'graph_receipt':receipt}
            report['status'] = 'exact-degeneration-witness'
            save()
            break
        if not verify_farkas(relations,decision['indices'],decision['weights']):
            raise ArithmeticError('invalid integer rejection circuit')
        used = set()
        for i in decision['indices']:
            s,t,tt,u,uu,ss = relations[i]['vertices']
            used.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                         (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
        solver.add_clause([-members[f][g//64+1][g%64] for f,g in sorted(used)])
        report['cuts'].append({'sets':sets,'members':sorted(used),
                              'vertices':[relations[i]['vertices'] for i in decision['indices']],
                              'rows':[relations[i]['row'] for i in decision['indices']],
                              'weights':decision['weights'],'graph_receipt':receipt,
                              'lazy_rounds':lazy['rounds']})
        save()
    else:
        report['status'] = 'model-limit'
    save()
    solver.delete()
    print(json.dumps({k:v for k,v in report.items() if k not in ['cuts','witness']},indent=2))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base',choices=['generic','dual'],default='generic')
    parser.add_argument('--seconds',type=float,default=180)
    parser.add_argument('--max-models',type=int,default=50)
    parser.add_argument('--control',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    run(args.base,args.seconds,args.max_models,args.output,args.control)
