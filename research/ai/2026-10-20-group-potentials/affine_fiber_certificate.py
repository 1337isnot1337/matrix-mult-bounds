"""Independent exact checks of the variable-plane search parameterization."""
from itertools import product

from octal_group import group
from group_exact import pair_map


def sumsets(*sets):
    values={0}
    for row in sets:values={x^y for x in values for y in row}
    return values


def check(base,sets):
    if len(base)!=6 or any(not isinstance(v,int) or not 0<v<64 for v in base):
        raise ValueError('six nonzero base columns required')
    inverse={}
    for abstract in range(64):
        actual=0
        for j in range(6):
            if abstract&(1<<j):actual^=base[j]
        if actual in inverse:raise ValueError('dependent base columns')
        inverse[actual]=abstract
    if list(map(len,sets))!=[19,19,19]:raise ValueError('wrong target shape')
    fibers=[{},{},{}];directions=[{},{},{}];varying_planes=0;varying_short=0
    for f,row in enumerate(sets):
        if len(set(row))!=19 or any(not isinstance(g,int) or not 0<=g<448 for g in row):
            raise ValueError('invalid group subset')
        for a in range(1,8):
            P={g%64 for g in row if g//64+1==a};fibers[f][a]=P
            if len(P)!=(3 if a<6 else 2):raise ValueError('wrong fiber size')
            D={x^y for x,y in product(P,repeat=2)};directions[f][a]=D
            if len(D)!=(4 if a<6 else 2):raise ValueError('wrong affine span')
            projected={(inverse[v]>>(2*f))&3 for v in D}
            if len(projected)!=len(D):raise ValueError('fiber direction is not transverse to the base complement')
            expected={0,base[2*f],base[2*f+1],base[2*f]^base[2*f+1]}
            if a<6 and D!=expected:varying_planes+=1
            if a>=6 and D!={0,base[2*f]}:varying_short+=1
        if fibers[f][1]!={0,*base[2*f:2*f+2]}:raise ValueError('base fiber is not normalized')
    if {inverse[v]&3 for v in fibers[0][2]}!={0,1,2} or 0 not in fibers[0][2]:
        raise ValueError('S multiplier-two offset is not normalized')
    triples=0
    for a,b,c in product(range(1,8),repeat=3):
        P=[fibers[0][a],fibers[1][b],fibers[2][c]]
        D=[directions[0][a],directions[1][b],directions[2][c]]
        unique_sums=len(sumsets(*P))==len(P[0])*len(P[1])*len(P[2])
        independent_directions=len(sumsets(*D))==len(D[0])*len(D[1])*len(D[2])
        if unique_sums!=independent_directions:raise ArithmeticError('three-point difference equivalence fails')
        if not unique_sums:raise ValueError('normal fibers have a triple-sum collision')
        triples+=1
    G=group();pair_sizes=[len(pair_map(G,sets[f],sets[g])) for f,g in [(0,1),(1,2),(2,0)]]
    return {'normal_fiber_triples_checked':triples,'pair_map_sizes':pair_sizes,
            'varying_three_point_planes':varying_planes,
            'changed_short_directions':varying_short,
            'scope':'Exact affine-fiber and pair-injection receipt only; no positive potential or exponent claim.'}
