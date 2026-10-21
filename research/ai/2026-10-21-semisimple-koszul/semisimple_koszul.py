"""Exact full-space Koszul gates for direct sums of matrix tensors over C.

The matrix-rank formula is imported from the maintained paired-source
proofs. Surviving necessary tests supply no tensor degeneration.
"""
import argparse
from functools import lru_cache
from itertools import permutations
import json
from math import comb,isqrt
from pathlib import Path
import sys

PARENT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PARENT/'2026-10-20-paired-sources'))
sys.path.insert(0,str(PARENT/'2026-10-20-group-potentials'))
from all_ranks import matrix_basic_rank
from rank_locus_obstruction import profile,screen,gate_9_fourths


@lru_cache(None)
def padded_basic_ranks(a,b,ambient):
    if any(type(v) is not int or v<1 for v in [a,b,ambient]) or a*b>ambient:
        raise ValueError('positive integer sides with a*b<=ambient required')
    padding = ambient-a*b
    return tuple(sum(comb(padding,p-q)*matrix_basic_rank(b,a,q)
                     for q in range(max(0,p-padding),min(a*b-1,p)+1))
                 for p in range(ambient//2+1))


def source_ranks(degrees):
    if not degrees or any(type(d) is not int or d<1 for d in degrees):
        raise ValueError('positive integer degrees required')
    ambient = sum(d*d for d in degrees)
    ranks = [0]*(ambient//2+1)
    for d in sorted(set(degrees)):
        for p,rank in enumerate(padded_basic_ranks(d,d,ambient)):
            ranks[p] += degrees.count(d)*d*rank
    return ranks


def target_screen(degrees,shape,source=None):
    if len(shape)!=3 or any(type(v) is not int or v<1 for v in shape):
        raise ValueError('three positive integer target sides required')
    ambient = sum(d*d for d in degrees)
    source = source_ranks(degrees) if source is None else source
    for a,b,c in sorted(set(permutations(shape))):
        if a*b>ambient:
            return {'shape':list(shape),'excluded':True,'reason':'ordinary flattening'}
        target = padded_basic_ranks(a,b,ambient)
        for p,(s,r) in enumerate(zip(source,target)):
            if c*r>s:
                return {'shape':list(shape),'excluded':True,
                        'witness':{'ordered_shape':[a,b,c],'power':p,
                                   'source_rank':s,'target_rank':c*r,
                                   'rank_one_divisor':comb(ambient-1,p)}}
    return {'shape':list(shape),'excluded':False,
            'scope':'All first-leg Koszul powers and all tensor-leg orderings pass; no construction.'}


def frontier(name,degrees):
    ambient = sum(d*d for d in degrees)
    source = source_ranks(degrees)
    rank_locus = profile(degrees)
    checked = improving = 0
    records = []
    for b in range(2,isqrt(ambient)+1):
        for c in range(b,ambient//b+1):
            for a in range(2,b+1):
                checked += 1
                shape = [a,b,c]
                if not gate_9_fourths(degrees,shape):
                    continue
                improving += 1
                if not screen(degrees,shape,rank_locus)['excluded']:
                    records.append(target_screen(degrees,shape,source))
    survivors = sorted(r['shape'] for r in records if not r['excluded'])
    minimal = [s for s in survivors if not any(t!=s and all(x<=y for x,y in zip(t,s)) for t in survivors)]
    return {'source':name,'degrees':degrees,'source_dimension':ambient,
            'sorted_shapes_checked':checked,'strict_degree_gate_formats':improving,
            'rank_locus_survivor_count':len(records),'koszul_records':records,
            'koszul_surviving_shapes':survivors,'minimal_surviving_shapes':minimal,
            'proof_dependency':'2026-10-20-paired-sources/matrix_koszul.md and matrix_euler.md',
            'coverage':'All sorted integer formats with a>=2 and b*c<=source dimension. Every unexcluded format is tested at all powers via duality and all tensor-leg orderings. Excluded formats stop at a checked witness.',
            'scope':'General complex tensor degenerations of the stated direct-sum matrix source. Passing is only necessary.',
            'proof_status':'written proof; unreviewed; not formalized','improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = {'sources':[frontier('C[F8^2:C7]',[1]*7+[7]*9),
                         frontier('C[SL(2,F8)]',[1,7,7,7,7,8,9,9,9])],
              'improves_omega':False}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([{'source':r['source'],'survivors':r['koszul_surviving_shapes'],
                       'new_exclusions':sum(x['excluded'] for x in r['koszul_records'])}
                      for r in result['sources']],indent=2))
