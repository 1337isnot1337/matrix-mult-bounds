"""Find exact torus multiplicity budgets via low-deficit polynomial products."""
from collections import defaultdict
from itertools import combinations_with_replacement, product
from pathlib import Path
import json
import time

import sympy as sp


SOURCE=[1,3,6,10,14,17,19,20,19,17,14,10,6,3,1]


def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def compatible(a,b):
    return all(x<=y for x,y in zip(convolution(a,tuple(reversed(b))),SOURCE))


def central_screen(a,b,c):
    vectors=(a,b,c)
    target_dims=[sum(x*y for x,y in zip(vectors[i],vectors[j]))
                 for i,j in ((0,1),(1,2),(2,0))]
    defects=[20-x for x in target_dims]
    minima=[min(vectors[k][w] for w in range(8) if vectors[i][w]*vectors[j][w])
            for i,j,k in ((0,1,2),(1,2,0),(2,0,1))]
    slacks=[minima[i]-4+sum(defects[j] for j in range(3) if j!=i) for i in range(3)]
    return {'target_dimensions':target_dims,'source_kernel_dimensions':defects,
            'target_minimum_slice_ranks':minima,'minimum_rank_slacks':slacks,
            'passes':min(slacks)>=0}


def bounded_coefficients(poly):
    if poly.degree()>7 or poly.degree()<0:
        return None
    values=tuple(int(poly.nth(i)) for i in range(8))
    return values if min(values)>=0 else None


def search():
    x=sp.Symbol('x');base=sp.Poly.from_list(list(reversed(SOURCE)),x)
    by_c=defaultdict(set);counts=defaultdict(int);started=time.monotonic()
    for case,positions in enumerate(combinations_with_replacement(range(15),4)):
        deficits=[0]*15
        for p in positions: deficits[p]+=1
        if any(d>s for d,s in zip(deficits,SOURCE)):
            continue
        counts['valid_deficit_polynomials']+=1
        poly=base-sp.Poly(sum(d*x**i for i,d in enumerate(deficits)),x)
        content,factors=sp.factor_list(poly)
        forced=sp.Poly(1,x);optional=[];possible=True
        for factor,mult in factors:
            value=int(factor.eval(1))
            if value<0:
                factor=-factor;value=-value
            if value==1:
                optional.append((factor,mult))
            elif 12%(value**mult)==0:
                forced*=factor**mult
            elif 13%(value**mult)==0:
                pass
            else:
                possible=False;break
        if not possible:
            continue
        for choices in product(*[range(mult+1) for factor,mult in optional]):
            selected=forced
            for (factor,mult),power in zip(optional,choices):
                selected*=factor**power
            value=int(selected.eval(1))
            if value==0 or 12%value:
                continue
            selected*=12//value
            quotient,remainder=sp.div(poly,selected)
            if remainder or quotient.domain!=sp.ZZ:
                # Poly division may leave QQ even when every coefficient is integral.
                if remainder or any(v.q!=1 for v in quotient.all_coeffs()):
                    continue
                quotient=quotient.set_domain(sp.ZZ)
            a=bounded_coefficients(selected);g=bounded_coefficients(quotient)
            if a is None or g is None or sum(a)!=12 or sum(g)!=13:
                continue
            c=tuple(reversed(g))
            if not compatible(a,c):
                raise ArithmeticError('Polynomial budget reconstruction failed')
            by_c[c].add(a)
        if case%250==0:
            print('case',case,'pairs',sum(map(len,by_c.values())),'seconds',time.monotonic()-started,flush=True)
    triples=[]
    for c,neighbors in by_c.items():
        ordered=sorted(neighbors)
        for i,a in enumerate(ordered):
            for b in ordered[i:]:
                if compatible(a,b):
                    triples.append({'vertex_counts':[list(a),list(b),list(c)],'central_screen':central_screen(a,b,c)})
    return {'weight_interval':[0,7],'source_weight_multiplicities':SOURCE,
            'target_shape':[12,12,13], 'valid_deficit_polynomials':counts['valid_deficit_polynomials'],
            'compatible_12_13_pairs':sum(map(len,by_c.values())),
            'distinct_13_vertex_profiles':len(by_c),'compatible_triples':triples,
            'triples_passing_central_rank_screen':sum(t['central_screen']['passes'] for t in triples),
            'constructed':False,'new_exponent_established':False}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=search();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k!='compatible_triples'})
