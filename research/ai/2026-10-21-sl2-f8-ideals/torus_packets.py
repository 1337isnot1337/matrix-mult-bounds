"""Exact cyclic-nine incidence, doubled-coset screens and punctured packets."""
from collections import Counter
from functools import lru_cache
from itertools import combinations,product
import json
from pathlib import Path

from sl2_f8_ideal_certificate import group,selected_subgroups
from stream_potentials import relation,verify_stream_witness
from verify_stream_reports import verify_cut


def powers(g):
    G = group()
    row = [0]
    x = g
    while x:
        row.append(x)
        x = G['mul'][x][g]
    return row


@lru_cache(None)
def tori():
    G = group()
    rows = sorted({tuple(sorted(powers(g))) for g in range(1,504) if len(powers(g))==9})
    H = selected_subgroups()['cyclic9']
    conjugates = {tuple(sorted(G['mul'][G['mul'][g][h]][G['inv'][g]] for h in H))
                  for g in range(504)}
    if len(rows)!=28 or set(rows)!=conjugates:
        raise ArithmeticError('incomplete order-nine subgroup coverage')
    if any(set(a)&set(b)!={0} for a,b in combinations(rows,2)):
        raise ArithmeticError('distinct tori have a nontrivial intersection')
    return rows


def packet_relation(indices):
    G = group()
    A,B,C = [tori()[i] for i in indices]
    solutions = [(a,b,G['inv'][G['mul'][a][b]]) for a,b in product(A,B)
                 if G['inv'][G['mul'][a][b]] in C]
    if solutions[0]!=(0,0,0) or len(solutions) not in [1,2]:
        raise ArithmeticError('unexpected local product relation')
    return None if len(solutions)==1 else solutions[1]


def cycles(g,H):
    G = group()
    unseen = set(H)
    result = []
    while unseen:
        start = min(unseen)
        row = [start]
        x = G['mul'][g][start]
        while x!=start:
            row.append(x)
            x = G['mul'][g][x]
        if not set(row).issubset(unseen):
            raise ArithmeticError('translation cycles overlap')
        unseen.difference_update(row)
        result.append(row)
    return result


def punctured_packet(indices,selected=None):
    rel = packet_relation(indices)
    if rel is None:
        raise ValueError('choose a non-TPP parent')
    sets = [list(tori()[i]) for i in indices]
    orders = list(map(lambda g:len(powers(g)),rel))
    if selected is None:
        selected = next((i for i,n in enumerate(orders) if n==9),0)
    elif type(selected) is not int or selected not in range(3):
        raise ValueError('punctured family must be zero, one or two')
    potential = {}
    for cycle in cycles(rel[selected],sets[selected]):
        sets[selected].remove(cycle[0])
        potential.update({g:-j for j,g in enumerate(cycle) if j})
    potentials = [potential[g] if f==selected else 0 for f,row in enumerate(sets) for g in row]
    receipt = verify_stream_witness(group(),sets,potentials)
    return {'parent_torus_indices':list(indices),'extra_relation':list(rel),
            'translation_orders':orders,'punctured_family':selected,
            'sets':sets,'potentials':potentials,'verification':receipt,
            'improves_omega':False}


def parent_cycle_cut(indices):
    G = group()
    rel = packet_relation(indices)
    if rel is None:
        raise ValueError('a TPP parent has no extra cycle')
    sets = [list(tori()[i]) for i in indices]
    chosen = [cycles(g,H)[0] for g,H in zip(rel,sets)]
    positions = [{g:i for i,g in enumerate(H)} for H in sets]
    vertices = []
    members = set()
    for s,tt,uu in product(*chosen):
        ss,t,u = [G['mul'][g][x] for g,x in zip(rel,[s,tt,uu])]
        row = [positions[f][g] for f,g in [(0,s),(1,t),(1,tt),(2,u),(2,uu),(0,ss)]]
        vertices.append(row)
        members.update([(0,s),(0,ss),(1,t),(1,tt),(2,u),(2,uu)])
    cut = {'sets':sets,'vertices':vertices,
           'rows':[list(relation(v,[9,9,9])['row']) for v in vertices],
           'weights':[1]*len(vertices),'members':sorted(map(list,members))}
    verify_cut(G,cut,[9,9,9])
    return cut


def large_double_cosets(H):
    G = group()
    unseen = set(range(504))
    sizes = []
    records = []
    while unseen:
        r = min(unseen)
        D = {G['mul'][G['mul'][a][r]][b] for a,b in product(H,repeat=2)}
        if not D.issubset(unseen):
            raise ArithmeticError('double-coset classes overlap')
        unseen.difference_update(D)
        sizes.append(len(D))
        if len(D)==81:
            S = sorted(set(H)|{G['mul'][h][r] for h in H})
            difference = {G['mul'][a][G['inv'][b]] for a,b in product(S,repeat=2)}
            expected = set(H)|D|{G['inv'][g] for g in D}
            if difference!=expected or len(S)!=18:
                raise ArithmeticError('doubled right-coset difference formula failed')
            records.append({'representative':r,'difference_mask':sum(1 << g for g in difference),
                            'difference_size':len(difference)})
    if sorted(sizes)!=[9,9]+[81]*6:
        raise ArithmeticError('unexpected double-coset coverage')
    return records


def seven_packet():
    G = group()
    subgroups = sorted({tuple(sorted(powers(g))) for g in range(1,504) if len(powers(g))==7})
    for x in range(1,504):
        if G['mul'][x][x]!=0:
            continue
        inverted = [H for H in subgroups if all(
            G['mul'][G['mul'][x][h]][G['inv'][x]]==G['inv'][h] for h in H)]
        if len(inverted)>=3:
            sets = list(map(list,inverted[:3]))
            return {'sets':sets,'potentials':[0]*21,'common_involution':x,
                    'verification':verify_stream_witness(G,sets,[0]*21),
                    'improves_omega':False}
    raise ArithmeticError('no selected order-seven control')


def geometry_report():
    G,rows = group(),tori()
    involutions = [g for g in range(1,504) if G['mul'][g][g]==0]
    blocks = [[i for i,H in enumerate(rows) if all(
        G['mul'][G['mul'][x][h]][G['inv'][x]]==G['inv'][h] for h in H)]
        for x in involutions]
    if len(involutions)!=63 or any(len(B)!=4 for B in blocks) or len({tuple(B) for B in blocks})!=63:
        raise ArithmeticError('unexpected involution blocks')
    pairs = Counter(pair for B in blocks for pair in combinations(B,2))
    if len(pairs)!=378 or set(pairs.values())!={1}:
        raise ArithmeticError('not a two-(28,4,1) design')
    block_triples = {t for B in blocks for t in combinations(B,3)}
    actual_triples = set()
    orders = Counter()
    non_tpp = []
    for indices in combinations(range(28),3):
        rel = packet_relation(indices)
        if rel is None:
            actual_triples.add(indices)
        else:
            orders[tuple(sorted(len(powers(g)) for g in rel))] += 1
            non_tpp.append(indices)
    if actual_triples!=block_triples or len(actual_triples)!=252:
        raise ArithmeticError('TPP triples do not match the incidence blocks')
    first = punctured_packet(non_tpp[0])
    control_sets = [list(rows[i]) for i in sorted(actual_triples)[0]]
    control = {'sets':control_sets,'potentials':[0]*27,
               'verification':verify_stream_witness(G,control_sets,[0]*27)}
    base = large_double_cosets(rows[0])
    histogram = Counter()
    sizes = Counter()
    for K in rows[1:]:
        other = large_double_cosets(K)
        for a,b in product(base,other):
            histogram[(a['difference_mask']&b['difference_mask']).bit_count()] += 1
            sizes[a['difference_size']] += 1
    return {'group':'SL(2,F8)','cyclic_order_nine_subgroups':[list(H) for H in rows],
            'involutions':involutions,'involution_blocks':blocks,
            'TPP_torus_triples':[list(t) for t in sorted(actual_triples)],
            'all_unordered_torus_triples_checked':3276,
            'non_TPP_extra_relation_count':len(non_tpp),
            'non_TPP_translation_order_histogram':{str(k):v for k,v in sorted(orders.items())},
            'doubled_right_coset_pairs_checked':sum(histogram.values()),
            'doubled_right_coset_difference_intersection_histogram':{str(k):v for k,v in sorted(histogram.items())},
            'minimum_doubled_right_coset_difference_intersection':min(histogram),
            'full_TPP_control':control,'punctured_packet':first,
            'seven_packet_control':seven_packet(),
            'full_parent_positive_cycle':parent_cycle_cut(non_tpp[0]),
            'scope':'Finite torus geometry, doubled-coset obstructions and local punctured-packet constructions. No global improving target or exponent.',
            'improves_omega':False}


if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    data = geometry_report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'TPP_triples':len(data['TPP_torus_triples']),
                      'translation_orders':data['non_TPP_translation_order_histogram'],
                      'punctured_shape':data['punctured_packet']['verification']['shape'],
                      'punctured_receipt':data['punctured_packet']['verification']},indent=2))
