"""Solver-free checks for a selected full-D18 subgroup search frame."""
from functools import lru_cache
from sl2_f8_source import group
from group_exact import pair_map
from stream_potentials import verify_stream_witness
from verify_stream_reports import verify_cut


@lru_cache(None)
def subgroup():
    G = group()
    def powers(g):
        row = [0]
        x = g
        while x:
            row.append(x)
            x = G['mul'][x][g]
        return row
    C = next(powers(g) for g in range(1,504) if len(powers(g))==9)
    g = C[1]
    x = next(x for x in range(1,504) if G['mul'][x][x]==0 and
             G['mul'][G['mul'][x][g]][G['inv'][x]]==G['inv'][g])
    H = sorted(set(C+[G['mul'][c][x] for c in C]))
    if len(H)!=18 or any(G['mul'][a][b] not in H for a in H for b in H):
        raise ArithmeticError('not the selected order-eighteen subgroup')
    return H


def right_cosets():
    G,H = group(),subgroup()
    unseen = set(range(504))
    rows = []
    while unseen:
        coset = {G['mul'][h][min(unseen)] for h in H}
        if len(coset)!=18 or not coset.issubset(unseen):
            raise ArithmeticError('invalid right-coset partition')
        rows.append(sorted(coset))
        unseen.difference_update(coset)
    if len(rows)!=28:
        raise ArithmeticError('incorrect subgroup index')
    return rows


def verify_search(report):
    if report['group']!='SL(2,F8)' or report['fixed_subgroup']!=subgroup():
        raise ValueError('incorrect source or subgroup')
    G = group()
    shape = report['shape']
    if len(shape)!=3 or shape[0]!=18 or report['right_coset_count']!=28:
        raise ValueError('incorrect frame format')
    for cut in report['cuts']:
        if cut['sets'][0]!=subgroup() or any(0 not in row for row in cut['sets'][1:]):
            raise ValueError('candidate left the normalized frame')
        verify_cut(G,cut,shape)
    witness = report['witness']
    if witness:
        if list(map(len,witness['sets']))!=shape or witness['sets'][0]!=subgroup():
            raise ValueError('incorrect witness frame')
        if verify_stream_witness(G,witness['sets'],witness['potentials'])!=witness['verification']:
            raise ValueError('incorrect full-support witness receipt')
    unresolved = report.get('unresolved_candidate')
    if unresolved:
        if list(map(len,unresolved))!=shape or unresolved[0]!=subgroup():
            raise ValueError('incorrect unresolved frame')
        for f,g in [(0,1),(1,2),(2,0)]:
            pair_map(G,unresolved[f],unresolved[g])
    if report['models']!=len(report['cuts'])+int(bool(witness))+int(bool(unresolved)):
        raise ValueError('incorrect model count')
    return {'group':G['name'],'shape':shape,'exact_cuts_replayed':len(report['cuts']),
            'exact_witness_replayed':bool(witness),'unsat_proof_checked':False,
            'reported_status':report['status'],'improves_omega':False}
