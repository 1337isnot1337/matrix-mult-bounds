"""Discover cyclic shear plane directions before solving for offsets.

All filters are finite necessary conditions; surviving directions are not
degeneration witnesses. Averages of bijective crossed sums yield necessary
inequalities on the nine fiber means, without making an offset choice.
"""
from itertools import product
import argparse
import json
from pathlib import Path

from quaternary_group import fm,scale,coset_representatives


def sumspace(*spaces):
    result={0}
    for P in spaces:result={x^y for x in result for y in P}
    return result


def cyclic_shears(bits):
    """Actual (unnormalized) planes: two Frobenius shears, one scalar shear."""
    out=[{}, {}, {}]
    for a in [1,2,3]:
        f=(bits[0]>>(a-1))&1;g=(bits[1]>>(a-1))&1;h=(bits[2]>>(a-1))&1
        out[0][a]=tuple(x|((fm(x,x) if f else 0)<<2) for x in range(4))
        out[1][a]=tuple((y<<2)|((fm(y,y) if g else 0)<<4) for y in range(4))
        out[2][a]=tuple((fm(2,z) if h else 0)|(z<<4) for z in range(4))
    return out


def local_pair_packing(actual):
    for f,g in [(0,1),(1,2),(2,0)]:
        for q in [1,2,3]:
            masks=[]
            for a in [1,2,3]:
                b=fm(a,q)
                W={scale(fm(a,a),x^y) for x in actual[f][a] for y in actual[g][b]}
                if len(W)!=16:return False
                masks.append([sum(1<<(v^w) for w in W) for v in coset_representatives(W)])
            if not any(not (u&v or u&w or v&w) for u in masks[0] for v in masks[1] for w in masks[2]):
                return False
    return True


def crossed_mean_rows(actual):
    rows={}
    for a,b,c,aa,bb in product([1,2,3],repeat=5):
        denominator=fm(a,bb)
        cc=fm(fm(fm(aa,b),c),fm(denominator,denominator))
        if (a,b,c)==(aa,bb,cc):continue
        r=fm(a,fm(aa,aa));q=fm(b,fm(bb,bb))
        left=sumspace(actual[0][a],{scale(q,x) for x in actual[1][bb]},
                      {scale(r,x) for x in actual[2][cc]})
        right=sumspace({scale(r,x) for x in actual[0][aa]},actual[1][b],
                       {scale(q,x) for x in actual[2][c]})
        if len(left)!=64 or len(right)!=64:continue
        row=[0]*9
        for p,s in [(a-1,1),(aa-1,-1),(3+bb-1,1),(3+b-1,-1),
                    (6+cc-1,1),(6+c-1,-1)]:row[p]+=s
        rows[tuple(row)]={'row':row,'scalar_indices':[a,b,bb,c,cc,aa]}
    return list(rows.values())


def discover():
    from search import potential_or_circuit
    counts={'patterns':0,'pair_packing_pass':0,'mean_pass':0}
    survivors=[]
    for bits in product(range(8),repeat=3):
        counts['patterns']+=1;actual=cyclic_shears(bits)
        if not all(len(sumspace(actual[0][a],actual[1][b],actual[2][c]))==64
                   for a,b,c in product([1,2,3],repeat=3)):
            raise ArithmeticError('normal-fiber triple tiling failed')
        if not local_pair_packing(actual):continue
        counts['pair_packing_pass']+=1
        rows=crossed_mean_rows(actual)
        decision=potential_or_circuit(rows,9)
        if 'potentials' not in decision:continue
        counts['mean_pass']+=1
        normalized=[{a:sorted(scale(fm(a,a),x) for x in P) for a,P in row.items()} for row in actual]
        survivors.append({'bits':bits,'normal_planes':normalized,
                          'mean_constraints':len(rows),'mean_potentials':decision['potentials']})
    return {'counts':counts,'survivors':survivors,'improves_omega':False,
            'scope':'Restricted binary on/off cyclic shear directions. Pair packing '
                    'and necessary fiber-mean constraints only; no offsets or target.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=discover()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
