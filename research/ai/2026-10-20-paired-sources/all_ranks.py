"""Exact all-power Koszul formulas and a finite paired matrix-target frontier."""
from functools import lru_cache
from itertools import combinations
from collections import defaultdict
from math import comb, prod


def choose(n,k): return comb(n,k) if 0<=k<=n else 0


def source_rank(a,p):
    if a<2: raise ValueError('the formula here requires a>=2')
    return a*(2*a-1)*choose(a*a-1,p)+2*(a-1)**2*choose(a*a-3,p-1)


def rows(length, cap):
    if not length:
        yield ()
        return
    for value in range(cap,-1,-1):
        for tail in rows(length-1,value): yield (value,)+tail


def weyl_dimension(shape,n):
    if len(shape)>n: return 0
    shape = tuple(shape)+(0,)*(n-len(shape))
    numerator = prod(shape[i]-shape[j]+j-i for i in range(n) for j in range(i+1,n))
    denominator = prod(j-i for i in range(n) for j in range(i+1,n))
    answer,remainder = divmod(numerator,denominator)
    if remainder: raise ArithmeticError('Weyl dimension is not integral')
    return answer


@lru_cache(None)
def matrix_basic_ranks(l,r):
    kernel = [0]*(l*r+1)
    for tail in rows(l-1,r):
        partition = (r,)+tail
        transpose = tuple(sum(value>=j for value in partition) for j in range(1,r+1))
        extended = (r+1,)+tail
        kernel[sum(partition)] += weyl_dimension(extended,l)*weyl_dimension(transpose,r)
    return tuple(l*choose(l*r,p)-kernel[p] for p in range(l*r+1))


def fixed_sum_rows(total,length,cap):
    if not length:
        if not total: yield ()
        return
    if total<0 or total>length*cap: return
    for value in range(min(cap,total),(total+length-1)//length-1,-1):
        for tail in fixed_sum_rows(total-value,length-1,value): yield (value,)+tail


@lru_cache(None)
def matrix_partition_rank(l,r,p):
    if p<0 or p>=l*r: return 0
    if p>(l*r-1)//2: return matrix_partition_rank(r,l,l*r-p-1)
    kernel = 0
    for tail in fixed_sum_rows(p-r,l-1,r):
        partition = (r,)+tail
        transpose = tuple(sum(value>=j for value in partition) for j in range(1,r+1))
        kernel += weyl_dimension((r+1,)+tail,l)*weyl_dimension(transpose,r)
    return l*choose(l*r,p)-kernel


@lru_cache(None)
def matrix_basic_rank(l,r,p):
    """Exact cohomological Euler sum, including the elementary outer-size-one cases."""
    if p<0 or p>=l*r: return 0
    if l==1: return choose(r,p)
    if r==1: return choose(l,p+1)
    if p>(l*r-1)//2: return matrix_basic_rank(r,l,l*r-p-1)
    kernel = sum((-1)**(j-r)*comb(l*r,p-j)*comb(j+l,l-1)*comb(j-1,r-1)
                 for j in range(r,p+1))
    return l*comb(l*r,p)-kernel


def padded_matrix_rank(shape, ambient, p):
    l,b,r = shape
    padding = ambient-l*r
    if padding<0: raise ValueError('matrix first leg exceeds the source ambient dimension')
    return b*sum(choose(padding,p-q)*matrix_basic_rank(l,r,q)
                 for q in range(max(0,p-padding),min(l*r,p)+1))


def frontier(maximum=8,minimum=2):
    records = []
    for a in range(minimum,maximum+1):
        ambient,N = a*a,a*(2*a-1)
        sources = [source_rank(a,p) for p in range(ambient)]
        considered = 0; rejected = []; remaining = []
        for l in range(1,ambient+1):
            for r in range(l,ambient//l+1):
                for b in range(1,N//r+1):
                    considered += 1
                    volume = l*b*r
                    if (36*volume)**3 <= (6*a-2)**8: continue
                    shape = (l,b,r)
                    witness = next(({'power':p,'source_rank':rank,
                                     'target_rank':padded_matrix_rank(shape,ambient,p)}
                                    for p,rank in enumerate(sources)
                                    if min(l*b*choose(ambient,p),b*r*choose(ambient,p+1))>rank
                                    and padded_matrix_rank(shape,ambient,p)>rank),None)
                    record = {'shape':list(shape),'volume':volume}
                    if witness: rejected.append({**record,**witness})
                    else:
                        record['ordinary_restriction_screen_passes'] = b*(l+r-1)<=3*a*a-2*a
                        remaining.append(record)
        records.append({'a':a,'format':[ambient,N,N],
                        'positive_shapes_mod_BC_exchange':considered,
                        'improving_shapes':len(rejected)+len(remaining),
                        'excluded_by_first_leg_Koszul':rejected,
                        'remaining_after_this_screen':remaining})
    return {'scope':'All positive matrix shapes in the stated finite formats, modulo B/C exchange.',
            'minimum_a':minimum,'maximum_a':maximum,'records':records,'improves_omega':False,
            'proof_status':'Source and matrix rank formulas written and unreviewed.'}


def source_rank_mod2(a,p):
    """Independent sparse coefficient lower-rank control, not formula evaluation."""
    width = 2*a-1; blocks = defaultdict(list)
    for subset in combinations(range(a*a),p):
        mask = sum(1<<i for i in subset)
        x,y = sum(i//a for i in subset),sum(i%a for i in subset)
        for i in range(a):
            for j in range(width): blocks[x-i,y+j].append((mask,i,j))
    total = 0
    for columns in blocks.values():
        row_ids,pivots = {},{}
        for mask,i,j in columns:
            vector = 0
            for q in range(a):
                t = j-q
                if not 0<=t<a: continue
                for s in range(a):
                    index = s*a+q
                    if mask>>index&1: continue
                    row = (mask|(1<<index),s+i,t)
                    if row not in row_ids: row_ids[row] = len(row_ids)
                    vector ^= 1<<row_ids[row]
            while vector:
                pivot = vector.bit_length()-1
                if pivot in pivots: vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    total += 1
                    break
    return total


@lru_cache(None)
def matrix_basic_rank_mod2(l,r,p):
    if p<0 or p>=l*r: return 0
    if p>(l*r-1)//2: return matrix_basic_rank_mod2(r,l,l*r-p-1)
    blocks = defaultdict(list)
    for subset in combinations(range(l*r),p):
        mask = sum(1<<i for i in subset)
        left,right = [0]*l,[0]*r
        for index in subset:
            left[index//r] += 1; right[index%r] += 1
        for i in range(l):
            key = (tuple(value+int(j==i) for j,value in enumerate(left)),tuple(right))
            blocks[key].append((mask,i))
    total = 0
    for columns in blocks.values():
        row_ids,pivots = {},{}
        for mask,i in columns:
            vector = 0
            for j in range(r):
                index = i*r+j
                if mask>>index&1: continue
                row = (mask|(1<<index),j)
                if row not in row_ids: row_ids[row] = len(row_ids)
                vector ^= 1<<row_ids[row]
            while vector:
                pivot = vector.bit_length()-1
                if pivot in pivots: vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    total += 1
                    break
    return total


def controls():
    """Rebuild the retained independent sparse coefficient checks."""
    sources = []
    for a, powers in [(2,range(4)),(3,range(5)),(4,range(5)),(5,[2,3])]:
        for p in powers:
            rank = source_rank_mod2(a,p)
            expected = source_rank(a,p)
            if rank != expected: raise ArithmeticError('source control disagrees')
            sources.append({'a':a,'power':p,'mod2_rank':rank,'formula_rank':expected})
    matrices = []
    for l,r in [(2,2),(2,3),(3,3),(4,4)]:
        for p in range(l*r):
            rank = matrix_basic_rank_mod2(l,r,p)
            expected = matrix_basic_rank(l,r,p)
            if rank != expected: raise ArithmeticError('matrix control disagrees')
            matrices.append({'l':l,'r':r,'power':p,'mod2_rank':rank,'formula_rank':expected})
    source,target = source_rank(6,7),10*matrix_basic_rank(6,6,7)
    return {'source_controls':sources,'matrix_controls':matrices,
            'excluded_size_six':{'power':7,'source_rank':source,'target_rank':target,
                                 'strict_gap':target-source},
            'proof_status':'Written, unreviewed; finite controls do not prove the all-size formulas.',
            'improves_omega':False}


if __name__ == '__main__':
    import argparse,json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--maximum-a',type=int,default=8)
    parser.add_argument('--minimum-a',type=int,default=2)
    parser.add_argument('--controls',action='store_true')
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    report = controls() if args.controls else frontier(args.maximum_a,args.minimum_a)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    if args.controls:
        print('Independent source and matrix coefficient controls passed.')
        raise SystemExit(0)
    print(json.dumps({'maximum_a':args.maximum_a,'counts':[
        {'a':r['a'],'improving':r['improving_shapes'],
         'remaining':len(r['remaining_after_this_screen'])} for r in report['records']]},indent=2))
