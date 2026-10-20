"""Exact SL(2,p) group and matrix-tensor degeneration witness verification.

Standard library only. No SAT solver or floating LP is trusted by this file.
"""
from __future__ import annotations

from itertools import product


def group(p: int = 5) -> dict:
    matrices = [x for x in product(range(p), repeat=4)
                if (x[0]*x[3]-x[1]*x[2]) % p == 1]
    identity = (1,0,0,1)
    matrices.remove(identity)
    matrices.insert(0, identity)
    index = {x:i for i,x in enumerate(matrices)}
    def multiply(x,y):
        a,b,c,d=x; e,f,g,h=y
        return ((a*e+b*g)%p,(a*f+b*h)%p,
                (c*e+d*g)%p,(c*f+d*h)%p)
    table = [[index[multiply(x,y)] for y in matrices] for x in matrices]
    inverses = [index[(d%p,-b%p,-c%p,a%p)] for a,b,c,d in matrices]
    return {'p':p, 'matrices':matrices, 'mul':table, 'inv':inverses, 'identity':0,
            'name':f'SL(2,{p})'}


def affine_group(p: int, r: int) -> dict:
    if p<2 or any(p%d==0 for d in range(2,int(p**0.5)+1)) or r<1 or (p-1)%r:
        raise ValueError('prime p and positive r dividing p-1 required')
    subgroup=None
    for a in range(1,p):
        powers={pow(a,k,p) for k in range(r)}
        if len(powers)==r and pow(a,r,p)==1:
            subgroup=sorted(powers);break
    if subgroup is None: raise ArithmeticError('multiplicative subgroup not found')
    matrices=[(a,b,0,1) for a in subgroup for b in range(p)]
    identity=(1,0,0,1);matrices.remove(identity);matrices.insert(0,identity)
    index={x:i for i,x in enumerate(matrices)}
    table=[[index[((a*c)%p,(a*d+b)%p,0,1)] for c,d,_,_ in matrices]
           for a,b,_,_ in matrices]
    inverses=[index[(pow(a,-1,p),(-pow(a,-1,p)*b)%p,0,1)] for a,b,_,_ in matrices]
    return {'p':p,'index':r,'matrices':matrices,'mul':table,'inv':inverses,
            'identity':0,'name':f'C{p}:C{r}'}


def borel_anchor_certificate(G: dict) -> dict:
    if G['name']!='SL(2,5)':raise ValueError('this certificate is specific to SL(2,5)')
    p=5;matrices=G['matrices'];index={x:i for i,x in enumerate(matrices)}
    H=[i for i,x in enumerate(matrices) if x[2]==0]
    anchors=[index[x] for x in [(4,0,0,4),(1,1,0,1),(4,1,0,4),(2,0,0,3)]]
    def mm(x,y):
        a,b,c,d=x;e,f,g,h=y
        return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
    conjugators=[(a,b,0,d) for a in range(1,p) for d in range(1,p) for b in range(p)]
    witnesses=[]
    for q in H:
        if q==0:continue
        witness=None
        for reverse in [False,True]:
            candidate=matrices[G['inv'][q] if reverse else q]
            for P in conjugators:
                a,b,c,d=P;iv=pow((a*d-b*c)%p,-1,p)
                Pinv=((d*iv)%p,(-b*iv)%p,(-c*iv)%p,(a*iv)%p)
                target=index[mm(mm(P,candidate),Pinv)]
                if target in anchors:
                    witness={'quotient':q,'reverse_pair':reverse,
                             'conjugator':list(P),'anchor':target}
                    break
            if witness:break
        if not witness:raise ArithmeticError('Borel quotient orbit not covered')
        witnesses.append(witness)
    if len(H)!=20 or len(witnesses)!=19:raise ArithmeticError('Borel size mismatch')
    return {'group':'SL(2,5)','subgroup':'upper triangular Borel','order':20,'index':6,
            'members':H,'anchors':anchors,'quotient_orbit_witnesses':witnesses,
            'justification':'Every nonidentity Borel quotient is conjugate under an '
                 'upper-triangular GL2(5) matrix, possibly after pair reversal, to '
                 'one of the four anchors. Conjugations preserve the Borel.',
            'verified':True}


def pair_map(G: dict, left: list[int], right: list[int]) -> dict:
    result = {}
    for i,x in enumerate(left):
        for j,y in enumerate(right):
            label = G['mul'][G['inv'][x]][y]
            if label in result:
                raise ValueError('pair map is not injective')
            result[label] = (i,j)
    return result


def extra_relations(G: dict, sets: list[list[int]]) -> tuple[list[dict],int]:
    S,T,U = sets
    n,m,p = map(len,sets)
    X,Y,Z = pair_map(G,S,T),pair_map(G,T,U),pair_map(G,U,S)
    rows = {}
    intended = 0
    for x,(s,t) in X.items():
        for y,(tt,u) in Y.items():
            z = G['inv'][G['mul'][x][y]]
            if z not in Z: continue
            uu,ss = Z[z]
            if (s,t,u) == (ss,tt,uu):
                intended += 1
                continue
            row = [0]*(n+m+p)
            for pos, sign in [(s,1),(ss,-1),(n+tt,1),(n+t,-1),
                              (n+m+uu,1),(n+m+u,-1)]:
                row[pos] += sign
            key = tuple(row)
            rows[key] = {'row':key, 'group_labels':[x,y,z],
                         'vertices':[s,t,tt,u,uu,ss]}
    if intended != n*m*p:
        raise ArithmeticError('intended matrix multiplication support corrupted')
    return list(rows.values()), intended


def verify_witness(G: dict, sets: list[list[int]], potentials: list[int]) -> dict:
    if len(sets) != 3 or any(not s or len(set(s)) != len(s) for s in sets):
        raise ValueError('three nonempty sets required')
    if any(not isinstance(x,int) or not 0 <= x < len(G['matrices'])
           for s in sets for x in s):
        raise ValueError('invalid group element')
    if len(potentials) != sum(map(len,sets)) or any(not isinstance(v,int) for v in potentials):
        raise ValueError('integer vertex potentials required')
    relations, intended = extra_relations(G,sets)
    weights = [sum(x*y for x,y in zip(r['row'],potentials)) for r in relations]
    if any(w <= 0 for w in weights):
        raise ValueError('extra tensor term has nonpositive weight')
    return {'shape':list(map(len,sets)), 'intended_terms':intended,
            'extra_relations':len(relations),
            'minimum_extra_weight':min(weights) if weights else None,
            'verified':True,
            'meaning':'Exact group products, three injective pair maps, zero '
                      'intended weights and strictly positive extra weights. '
                      'No exponent claim is part of this verifier.'}


def verify_farkas(relations: list[dict], indices: list[int], weights: list[int]) -> bool:
    if (len(indices) != len(weights) or not weights or any(w <= 0 for w in weights)
            or any(not isinstance(w,int) for w in weights)):
        return False
    if any(not 0 <= i < len(relations) for i in indices): return False
    width = len(relations[0]['row'])
    return all(sum(w*relations[i]['row'][j] for i,w in zip(indices,weights)) == 0
               for j in range(width))
