"""A uniform Laurent-monomial inverse for the diagonal orbit of T_m.

The output identities concern target coefficients only. They do not provide
source tensor maps or a matrix multiplication exponent bound.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


def triples(m):
    """Return (sector u, first degree a, second degree c)."""
    if m < 2:
        raise ValueError('the uniform normalization requires m >= 2')
    return [(u,a,c) for u in range(m) for a in range(u+1) for c in range(m-u)]


def rows(m):
    return [('x',p) for p in range(m)]+[('y',u,a) for u in range(m) for a in range(u+1)]+[('z',u,c) for u in range(m) for c in range(m-u)]


def selected_triples(m):
    return [(u,a,c) for u,a,c in triples(m) if a == 0 or c == 0 or u == 1]


def selected_rows(m):
    # Gauge alpha_0=alpha_1=1 and beta_(u,0)=1 for every u.
    return [row for row in rows(m) if row not in [('x',0),('x',1)] and not (row[0]=='y' and row[2]==0)]


def incidence(m):
    all_rows=rows(m)
    return sp.Matrix([[int(row in [('x',a+c),('y',u,a),('z',u,c)])
                       for row in all_rows] for u,a,c in triples(m)])


def normalize(m, values, field):
    """Reconstruct scalars using selected coefficients over a supplied field.

    field must expose mul and inv; its one element has integer encoding 1.
    Every supplied value must be nonzero. Unselected coefficients are not used.
    """
    if any(values[t] == 0 for t in selected_triples(m)):
        raise ValueError('selected target coefficients must be nonzero')
    mul,inv=field.mul,field.inv
    alpha=[1,1]
    for c in range(1,m-1):
        ratio=mul(mul(values[1,1,c],values[1,0,0]),
                  inv(mul(values[1,0,c],values[1,1,0])))
        alpha.append(mul(alpha[-1],ratio))
    scales={('x',p):alpha[p] for p in range(m)}
    for u in range(m):
        for a in range(u+1):
            scales['y',u,a]=mul(values[u,a,0],inv(mul(alpha[a],values[u,0,0])))
        for c in range(m-u):
            scales['z',u,c]=mul(values[u,0,c],inv(alpha[c]))
    reproduced={(u,a,c):mul(mul(alpha[a+c],scales['y',u,a]),scales['z',u,c])
                for u,a,c in triples(m)}
    return scales,reproduced


def relation_vectors(m):
    """Primitive exponent differences for each unselected coefficient.

    Each vector records target / predicted_target, so its target coefficient
    is +1. A zero exponent vector means the corresponding multiplicative
    equation holds. No root extraction is involved.
    """
    terms=triples(m);position={t:j for j,t in enumerate(terms)}
    units={t:sp.eye(len(terms))[:,j] for t,j in position.items()}
    alpha=[sp.zeros(len(terms),1),sp.zeros(len(terms),1)]
    for c in range(1,m-1):
        alpha.append(alpha[-1]+units[1,1,c]+units[1,0,0]-units[1,0,c]-units[1,1,0])
    selected=set(selected_triples(m))
    output={}
    for u,a,c in terms:
        if (u,a,c) in selected:continue
        vector=(units[u,a,c]-units[u,a,0]-units[u,0,c]+units[u,0,0]
                -alpha[a+c]+alpha[a]+alpha[c])
        output[u,a,c]=vector
    return output


def structure(m):
    terms=triples(m);all_rows=rows(m)
    selected=selected_triples(m);columns=selected_rows(m)
    E=incidence(m)
    D=E.extract([terms.index(t)for t in selected],[all_rows.index(row)for row in columns])
    relations=relation_vectors(m)
    return {'m':m,'target_terms':len(terms),'row_scalars':len(all_rows),
            'orbit_dimension':len(selected),'stabilizer_dimension':m+2,
            'selected_minor_determinant':int(D.det()),
            'selected_triples':[list(t)for t in selected],
            'selected_rows':[list(row)for row in columns],
            'relation_count':len(relations),'predicted_relation_count':(m-3)*(m-2)*(m+2)//6,
            'relations':{'/'.join(map(str,t)):[int(x)for x in vector]for t,vector in relations.items()},
            'binomial_degrees':{'/'.join(map(str,t)):sum(max(int(x),0)for x in vector)for t,vector in relations.items()},
            'all_relations_annihilate_incidence':all(E.T*vector==sp.zeros(len(all_rows),1)for vector in relations.values())}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--maximum-m',type=int,default=7)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    report={'purpose':'Exact finite controls for the written all-m target-orbit formula',
            'records':[structure(m)for m in range(2,args.maximum_m+1)],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'tensor_construction_supplied':False,'improves_omega':False}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print([{key:value for key,value in r.items()if key not in ('relations','selected_triples','selected_rows','binomial_degrees')}
            for r in report['records']])
