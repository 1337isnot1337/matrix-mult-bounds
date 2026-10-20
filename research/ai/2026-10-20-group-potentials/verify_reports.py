"""Replay exported degeneration witnesses and learned Farkas cuts exactly.

Standard library only. Reported SAT UNSAT outcomes are never promoted to proof.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from group_exact import group,affine_group,extra_relations,verify_witness,verify_farkas


def verify_run(report):
    affine=report.get('affine_parameters')
    quaternary=report.get('source_family')=='quaternary-affine'
    if quaternary:
        from quaternary_group import group as quaternary_group,plane_family,coset_representatives,scale
        G=quaternary_group()
        planes=plane_family(report.get('plane_pattern','covariant'))
        representatives=[{a:coset_representatives(P) for a,P in row.items()} for row in planes]
        if 'plane_pattern' in report:
            expected_planes=[{str(a):list(P) for a,P in row.items()} for row in planes]
            expected_reps=[{str(a):v for a,v in row.items()} for row in representatives]
        else:
            # First discovery run predates per-coset plane directions.
            expected_planes=[list(row[1]) for row in planes]
            expected_reps=[row[1] for row in representatives]
        if report['normal_planes']!=expected_planes or report['normal_offset_representatives']!=expected_reps:
            raise ValueError('quaternary ansatz data mismatch')
    else:
        G=affine_group(*affine) if affine else group(5)
    shape=report['shape']
    total=0
    for cut in report['cuts']:
        sets=cut['source_sets']
        if list(map(len,sets))!=shape: raise ValueError('source shape mismatch')
        relations,intended=extra_relations(G,sets)
        actual={tuple(r['vertices']):i for i,r in enumerate(relations)}
        indices=[];members=set()
        if len(cut['relation_vertices'])!=len(cut['relations']):
            raise ValueError('inconsistent circuit records')
        for vertices,row in zip(cut['relation_vertices'],cut['relations']):
            key=tuple(vertices)
            if key not in actual: raise ValueError('exported relation is not an extra term')
            i=actual[key];indices.append(i)
            if tuple(row)!=relations[i]['row']: raise ValueError('exported row differs')
            s,t,tt,u,uu,ss=vertices
            members.update([(0,sets[0][s]),(0,sets[0][ss]),
                            (1,sets[1][t]),(1,sets[1][tt]),
                            (2,sets[2][u]),(2,sets[2][uu])])
        if sorted(members)!=[tuple(x) for x in cut['members']]:
            raise ValueError('learned membership clause differs from exact circuit')
        if quaternary:
            cells={(f,G['matrices'][g][0]) for f,g in members}
            recorded=cut['offset_choice_cut']
            if len(recorded)!=len(cells) or {(f,a) for f,a,o in recorded}!=cells:
                raise ValueError('offset clause omits or repeats a circuit cell')
            for f,a,o in recorded:
                if not 0<=o<len(representatives[f][a]):raise ValueError('invalid offset')
                offset=representatives[f][a][o]
                points={(a,scale(a,v^offset)) for v in planes[f][a]}
                actual_points={G['matrices'][g] for g in sets[f] if G['matrices'][g][0]==a}
                if points!=actual_points:raise ValueError('offset clause does not preserve its circuit')
        if not verify_farkas(relations,indices,cut['weights']):
            raise ValueError('Farkas sum is not exactly zero with positive integer weights')
        if cut['extra_relations']!=len(relations) or cut['intended_terms']!=intended:
            raise ValueError('support counts mismatch')
        total+=1
    if total!=report['exact_farkas_cuts']: raise ValueError('cut count mismatch')
    witness=report.get('witness')
    if witness:
        if list(map(len,witness['sets']))!=shape: raise ValueError('witness shape mismatch')
        expected=[[list(G['matrices'][g]) for g in row] for row in witness['sets']]
        if expected!=witness['matrices']: raise ValueError('witness group elements mismatch')
        verified=verify_witness(G,witness['sets'],witness['potentials'])
        if verified!=witness['verification']: raise ValueError('witness receipt mismatch')
    if report['pair_injective_models']!=total+int(bool(witness)):
        raise ValueError('completed-model count mismatch')
    return {'group':G['name'],'shape':shape,'exact_cuts_replayed':total,
            'exact_witness_replayed':bool(witness),
            'reported_search_status':report['status'],
            'unsat_proof_checked':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reports',type=Path,nargs='+')
    args=parser.parse_args()
    for path in args.reports:
        report=json.loads(path.read_text())
        print(json.dumps({'path':str(path),**verify_run(report)}),flush=True)
