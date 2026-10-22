"""Discovery: radical powers for the alternating source and its double cover."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
import json
import sys
from scipy.optimize import minimize_scalar

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'2026-10-21-s5-split'))
import radical
import s5_source
from peirce import indices,xor


def powers(G, images):
    n=len(G['mul'])
    constraints=[sum(1<<g for g in range(n) if images[g]>>i & 1) for i in range(33)]
    J=radical.kernel(constraints,n)
    translates=[[xor(1<<G['mul'][g][h] for h in indices(j)) for j in J] for g in range(n)]
    previous=J
    dims=[n,len(J)]
    bases=[J]
    for k in range(2,30):
        span={}
        for a in previous:
            support=list(indices(a))
            for j in range(len(J)):
                radical.insert(xor(translates[g][j] for g in support),span)
        previous=list(span.values())
        bases.append(previous)
        dims.append(len(previous))
        if len(previous)==dims[-2] or not previous:
            break
    print(G['name'],dims,flush=True)
    layers=[a-b for a,b in zip(dims,dims[1:])]
    f=lambda t:sum(v*t**i for i,v in enumerate(layers))/t**((len(layers)-1)/3)
    r=minimize_scalar(f,bounds=(.05,.99999),method='bounded')
    print('layers',layers,'cap',r.fun,'t',r.x,flush=True)
    (HERE/(G['name'].replace('/','-')+'-radical.json')).write_text(json.dumps({'group':G['name'],'dimensions':dims,'layers':layers,'bases':[[hex(x) for x in b] for b in bases]},indent=2)+'\n')


G=s5_source.group()
r1,r2,_=radical.representations(G)
image=[1|(r1[g]<<1)|(r2[g]<<17) for g in range(120)]
even=[g for g,p in enumerate(G['matrices']) if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0]
lookup={g:i for i,g in enumerate(even)}
A={'name':'A5','mul':[[lookup[G['mul'][g][h]] for h in even] for g in even]}
powers(A,[image[g] for g in even])
from data import data
S,Q,_=data()
embedding=s5_source.control()['quotient_action_image']
powers(S,[image[embedding[Q['projection'][g]]] for g in range(120)])
