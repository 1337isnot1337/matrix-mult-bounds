"""A Laurent mixed-input local packet, checked by complete coefficient sums."""
import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sys

PARENT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PARENT/'2026-10-21-sl2-f8-ideals'))
from torus_packets import tori,packet_relation,powers,punctured_packet
from sl2_f8_ideal_certificate import group
from stream_potentials import support


def descriptor():
    indices = next(row for row in combinations(range(28),3)
                   if packet_relation(row) is not None and len(powers(packet_relation(row)[0]))==9)
    G = group()
    parent = [list(tori()[i]) for i in indices]
    packet = punctured_packet(indices,0)
    selected = packet['sets'][0]
    a = packet_relation(indices)[0]
    forward = [[int(s==i)+int(s==G['mul'][a][i]) for i in selected] for s in parent[0]]
    inverse = {}
    for ss in parent[0]:
        x = ss
        for power in range(9):
            inverse[x,ss] = (-1)**power
            x = G['mul'][a][x]
    backward = [[inverse[j,ss] for ss in parent[0]] for j in selected]
    return {'parent_torus_indices':list(indices),'selected_first_family':selected,
            'first_family_potentials':packet['potentials'][:8],
            'forward_integer_matrix':forward,'backward_integer_numerator_matrix':backward,
            'backward_denominator':2}


def verify(data):
    G = group()
    indices = data['parent_torus_indices']
    if len(indices)!=3 or len(set(indices))!=3 or any(type(i) is not int or not 0<=i<28 for i in indices):
        raise ValueError('three distinct torus indices required')
    parent = [list(tori()[i]) for i in indices]
    selected = data['selected_first_family']
    potential = data['first_family_potentials']
    F = data['forward_integer_matrix']
    K = data['backward_integer_numerator_matrix']
    denominator = data['backward_denominator']
    if len(selected)!=8 or len(set(selected))!=8 or not set(selected).issubset(parent[0]):
        raise ValueError('eight distinct first-family labels required')
    if len(potential)!=8 or any(type(x) is not int for x in potential):
        raise ValueError('eight integer Laurent exponents required')
    if len(F)!=9 or any(len(row)!=8 or any(type(x) is not int for x in row) for row in F):
        raise ValueError('integer9-by8 forward matrix required')
    if len(K)!=8 or any(len(row)!=9 or any(type(x) is not int for x in row) for row in K):
        raise ValueError('integer8-by9 backward numerator required')
    if type(denominator) is not int or denominator<1:
        raise ValueError('positive integer denominator required')
    accumulated = Counter()
    raw = negative = 0
    for s,t,tt,u,uu,ss in support(G,parent):
        for i in range(8):
            if F[s][i]==0:
                continue
            for j in range(8):
                coefficient = F[s][i]*K[j][ss]
                if coefficient==0:
                    continue
                exponent = potential[i]-potential[j]
                accumulated[i,t,tt,u,uu,j,exponent] += coefficient
                raw += 1
                negative += int(exponent<0)
    actual = {key:value for key,value in accumulated.items() if value}
    expected = {}
    intended = extras = 0
    for i,t,tt,u,uu,j in support(G,[selected,parent[1],parent[2]]):
        exponent = potential[i]-potential[j]
        is_intended = i==j and t==tt and u==uu
        if is_intended:
            if exponent!=0:
                raise ValueError('intended exponent must be zero')
            intended += 1
        else:
            if exponent!=1:
                raise ValueError('local extra term must have exponent one')
            extras += 1
        expected[i,t,tt,u,uu,j,exponent] = denominator
    if actual!=expected or intended!=648 or extras!=567:
        raise ValueError('complete mixed Laurent coefficient identity failed')
    return {'raw_integer_contributions':raw,
            'negative_exponent_contributions_before_cancellation':negative,
            'surviving_coefficient_numerators':sorted(set(actual.values())),
            'surviving_exponent_counts':{str(p):sum(key[-1]==p for key in actual) for p in [0,1]},
            'intended_terms':intended,'extra_terms_at_exponent_one':extras,
            'identity':'T_mixed(epsilon)=T_matrix+epsilon*T_extra',
            'verified':True}


def report():
    data = descriptor()
    return {'map':data,'coefficient_replay':verify(data),
            'proof_status':'explicit mixed local Laurent degeneration; written, unreviewed',
            'scope':'One local M(8,9,9) packet. The gauge preserves the parent tensor; no simultaneous target is constructed.',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['coefficient_replay'],indent=2))
