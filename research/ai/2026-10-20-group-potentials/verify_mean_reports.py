"""Standard-library replay of crossed-mean and point Farkas certificates."""
from itertools import product
import argparse
import json
from pathlib import Path

from quaternary_group import fm,scale,group
from quaternary_directions import sumspace
from group_exact import verify_farkas,extra_relations,verify_witness


def verify_mean_circuit(planes,rows,weights):
    P=[{int(a):set(v) for a,v in row.items()} for row in planes]
    if len(P)!=3 or any(set(row)!={1,2,3} for row in P):
        raise ValueError('nine plane directions required')
    for row in P:
        for V in row.values():
            if len(V)!=4 or 0 not in V or any(not isinstance(v,int) or not 0<=v<64 for v in V):
                raise ValueError('invalid four-point direction plane')
            if any(x^y not in V for x,y in product(V,repeat=2)):
                raise ValueError('direction set is not F2-linear')
    for entry in rows:
        a,b,bb,c,cc,aa=entry['scalar_indices']
        if any(v not in [1,2,3] for v in [a,b,bb,c,cc,aa]):raise ValueError('invalid scalar')
        if (a,b,c)==(aa,bb,cc):raise ValueError('intended scalar triple is not strict')
        if fm(fm(aa,b),c)!=fm(fm(a,bb),cc):raise ValueError('wrong scalar product')
        q=fm(b,fm(bb,bb));r=fm(a,fm(aa,aa))
        left=sumspace(P[0][a],{scale(q,x) for x in P[1][bb]},
                      {scale(r,x) for x in P[2][cc]})
        right=sumspace({scale(r,x) for x in P[0][aa]},P[1][b],
                       {scale(q,x) for x in P[2][c]})
        if len(left)!=64 or len(right)!=64:raise ValueError('crossed sum is not bijective')
        expected=[0]*9
        for p,s in [(a-1,1),(aa-1,-1),(3+bb-1,1),(3+b-1,-1),
                    (6+cc-1,1),(6+c-1,-1)]:expected[p]+=s
        if entry['row']!=expected:raise ValueError('wrong fiber-mean row')
    if not verify_farkas(rows,list(range(len(rows))),weights):
        raise ValueError('mean circuit is not a positive integer zero sum')
    return True


def verify_report(report):
    G=group();mean_count=0;point_count=0
    for cut in report['mean_cuts']:
        verify_mean_circuit(cut['actual_planes'],cut['rows'],cut['weights']);mean_count+=1
    for cut in report['point_cuts']:
        if list(map(len,cut['sets']))!=[12,12,12]:raise ValueError('wrong point shape')
        relations,intended=extra_relations(G,cut['sets'])
        by_vertices={tuple(row['vertices']):i for i,row in enumerate(relations)}
        if len(cut['rows'])!=len(cut['vertices']):raise ValueError('point row count mismatch')
        indices=[]
        for vertices,row in zip(cut['vertices'],cut['rows']):
            index=by_vertices[tuple(vertices)];indices.append(index)
            if tuple(row)!=relations[index]['row']:raise ValueError('point row mismatch')
        if not verify_farkas(relations,indices,cut['weights']):raise ValueError('invalid point circuit')
        point_count+=1
    witness=report.get('witness')
    if witness:
        if list(map(len,witness['sets']))!=[12,12,12]:raise ValueError('wrong witness shape')
        verified=verify_witness(G,witness['sets'],witness['potentials'])
        if verified!=witness['verification']:raise ValueError('wrong witness receipt')
    if report['pair_models']!=mean_count+point_count+int(bool(witness)):
        raise ValueError('model count mismatch')
    return {'mean_cuts_replayed':mean_count,'point_cuts_replayed':point_count,
            'exact_witness_replayed':bool(witness),'reported_status':report['status'],
            'unsat_proof_checked':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reports',type=Path,nargs='+')
    args=parser.parse_args()
    for path in args.reports:print(json.dumps({'path':str(path),**verify_report(json.loads(path.read_text()))}),flush=True)
