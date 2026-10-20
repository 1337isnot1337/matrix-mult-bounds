"""Replay sparse exact group circuits without enumerating the full support."""
import argparse
import json
from pathlib import Path

from group_exact import pair_map,verify_farkas
from octal_group import group,cubic_group,cubic_parent
from stream_potentials import relation,verify_stream_witness


def verify_cut(G,cut,shape,parent=None):
    sets=cut['sets']
    if list(map(len,sets))!=shape:raise ValueError('wrong cut shape')
    for f,row in enumerate(sets):
        if len(row)!=len(set(row)) or any(not isinstance(g,int) or not 0<=g<len(G['matrices']) for g in row):
            raise ValueError('invalid source set')
        if parent is not None and not set(row).issubset(parent[f]):raise ValueError('not a parent subset')
    if parent is None:
        for f,g in [(0,1),(1,2),(2,0)]:pair_map(G,sets[f],sets[g])
    if len(cut['vertices'])!=len(cut['rows']):raise ValueError('row count mismatch')
    relations=[];members=set()
    for vertices,row in zip(cut['vertices'],cut['rows']):
        if len(vertices)!=6:raise ValueError('six vertex indices required')
        s,t,tt,u,uu,ss=vertices
        if any(not isinstance(j,int) or not 0<=j<shape[f] for f,j in
               [(0,s),(1,t),(1,tt),(2,u),(2,uu),(0,ss)]):raise ValueError('invalid vertex index')
        if (s,t,u)==(ss,tt,uu):raise ValueError('intended term used as a strict constraint')
        x=G['mul'][G['inv'][sets[0][s]]][sets[1][t]]
        y=G['mul'][G['inv'][sets[1][tt]]][sets[2][u]]
        z=G['mul'][G['inv'][sets[2][uu]]][sets[0][ss]]
        if G['mul'][G['mul'][x][y]][z]!=0:raise ValueError('not a group support term')
        item=relation(vertices,shape)
        if tuple(row)!=item['row']:raise ValueError('wrong potential row')
        relations.append(item)
        members.update([(0,sets[0][s]),(0,sets[0][ss]),(1,sets[1][t]),
                        (1,sets[1][tt]),(2,sets[2][u]),(2,sets[2][uu])])
    if sorted(members)!=[tuple(x) for x in cut['members']]:raise ValueError('wrong circuit members')
    if not verify_farkas(relations,list(range(len(relations))),cut['weights']):
        raise ValueError('not a positive integer zero dependence')
    return True


def verify_report(report):
    if report['group']=='F8^3:C7':
        G=cubic_group();parent=cubic_parent(G)
        if report['parent_sets']!=parent:raise ValueError('wrong parent construction')
        for f,g in [(0,1),(1,2),(2,0)]:
            if len(pair_map(G,parent[f],parent[g]))!=3136:raise ValueError('bad parent pair map')
    elif report['group']=='F8^2:C7':G=group();parent=None
    else:raise ValueError('unsupported source group')
    for cut in report['cuts']:verify_cut(G,cut,report['shape'],parent)
    witness=report.get('witness')
    if witness:
        if list(map(len,witness['sets']))!=report['shape']:raise ValueError('wrong witness shape')
        if verify_stream_witness(G,witness['sets'],witness['potentials'])!=witness['verification']:
            raise ValueError('wrong full-support receipt')
    unresolved=bool(report.get('unresolved_candidate'))
    if report['models']!=len(report['cuts'])+int(bool(witness))+int(unresolved):
        raise ValueError('model count mismatch')
    return {'group':G['name'],'shape':report['shape'],'exact_cuts_replayed':len(report['cuts']),
            'exact_witness_replayed':bool(witness),'unresolved_candidate':unresolved,
            'reported_status':report['status'],'unsat_proof_checked':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reports',type=Path,nargs='+')
    args=parser.parse_args()
    for path in args.reports:print(json.dumps({'path':str(path),**verify_report(json.loads(path.read_text()))}),flush=True)
