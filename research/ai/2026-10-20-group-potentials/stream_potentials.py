"""Exact streaming support checks and optional cutting-plane discovery.

The support iterator stores only three injective pair maps. Integer
potentials are accepted only after every supported group triple was checked.
An incomplete prefix never verifies a witness.
"""
import random

from group_exact import pair_map,verify_farkas


def support(G,sets,seed=None):
    S,T,U=sets
    X=pair_map(G,S,T);Y=pair_map(G,T,U);Z=pair_map(G,U,S)
    left=list(X.items());right=list(Y.items())
    if seed is not None:
        rng=random.Random(seed);rng.shuffle(left);rng.shuffle(right)
    for x,(s,t) in left:
        row=G['mul'][x]
        for y,(tt,u) in right:
            z=G['inv'][row[y]]
            if z in Z:
                uu,ss=Z[z]
                yield (s,t,tt,u,uu,ss)


def relation(vertices,shape):
    n,m,p=shape;s,t,tt,u,uu,ss=vertices;row=[0]*(n+m+p)
    for j,sign in [(s,1),(ss,-1),(n+tt,1),(n+t,-1),
                   (n+m+uu,1),(n+m+u,-1)]:row[j]+=sign
    return {'vertices':list(vertices),'row':tuple(row)}


def weight(vertices,potentials,shape):
    n,m,p=shape;s,t,tt,u,uu,ss=vertices
    return (potentials[s]-potentials[ss]+potentials[n+tt]-potentials[n+t]
             +potentials[n+m+uu]-potentials[n+m+u])


def verify_stream_witness(G,sets,potentials):
    shape=list(map(len,sets))
    if len(shape)!=3 or any(len(set(row))!=len(row) or not row for row in sets):
        raise ValueError('three nonempty distinct-element sets required')
    if any(not isinstance(g,int) or not 0<=g<len(G['matrices']) for row in sets for g in row):
        raise ValueError('invalid group element')
    if len(potentials)!=sum(shape) or any(not isinstance(v,int) for v in potentials):
        raise ValueError('integer potentials required')
    intended=0;extra=0;minimum=None
    for vertices in support(G,sets):
        s,t,tt,u,uu,ss=vertices
        if (s,t,u)==(ss,tt,uu):intended+=1;continue
        value=weight(vertices,potentials,shape)
        if value<=0:raise ValueError('nonpositive extra term in full support')
        extra+=1;minimum=value if minimum is None else min(minimum,value)
    if intended!=shape[0]*shape[1]*shape[2]:raise ValueError('intended support count mismatch')
    return {'shape':shape,'intended_terms':intended,'extra_supported_terms':extra,
            'minimum_extra_weight':minimum,'verified':True,
            'verification':'Every supported group triple checked with integers; all three pair maps injective.'}


def discover(G,sets,max_rounds=60,violation_batch=1000,seed=20261020,progress=None):
    """Floating discovery, exact active-row checks, complete final acceptance."""
    from search import potential_or_circuit
    shape=list(map(len,sets));active={};rounds=[]
    for iteration in range(max_rounds):
        rows=list(active.values());decision=potential_or_circuit(rows,sum(shape))
        if 'potentials' not in decision:
            if not verify_farkas(rows,decision['indices'],decision['weights']):
                raise ArithmeticError('invalid lazy Farkas circuit')
            return {'relations':rows,'decision':decision,'rounds':rounds,'complete':False}
        potentials=decision['potentials'];bad={};scanned=0;intended=0;minimum=None
        for vertices in support(G,sets,seed+iteration):
            scanned+=1;s,t,tt,u,uu,ss=vertices
            if (s,t,u)==(ss,tt,uu):intended+=1;continue
            value=weight(vertices,potentials,shape)
            minimum=value if minimum is None else min(minimum,value)
            if value<=0:
                item=relation(vertices,shape);bad[item['row']]=item
                if len(bad)>=violation_batch:break
        rounds.append({'iteration':iteration,'active_relations':len(active),
                       'supported_terms_scanned':scanned,'new_violations':len(bad)})
        if progress:progress(rounds[-1])
        if not bad:
            # A second independent, deterministic traversal is the acceptance
            # receipt, distinct from randomized discovery/separation order.
            receipt=verify_stream_witness(G,sets,potentials)
            return {'relations':rows,'decision':decision,'rounds':rounds,
                    'complete':True,'verification':receipt}
        active.update(bad)
    return {'relations':list(active.values()),'decision':None,'rounds':rounds,
            'complete':False,'status':'lazy LP round limit, unresolved'}
