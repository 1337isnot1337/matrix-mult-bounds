"""Exact paired-source coefficients and first Koszul certificates."""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb


def source(a):
    width = 2*a-1
    terms = [(p*a+q, y*width+q+v, (p+y)*a+v)
             for p in range(a) for q in range(a) for y in range(a) for v in range(a)]
    return (a*a, a*width, a*width), terms


def kernel_vector(a, label):
    width = 2*a-1
    return {(r*a+s, r*width+j):1 for r in range(a) for s in range(a)
            for j in range(width) if s+j == label}


def first_koszul_image(terms, vector):
    by_input = defaultdict(list)
    for x,y,z in terms: by_input[y].append((x,z))
    result = defaultdict(int)
    for (w,y),coefficient in vector.items():
        for x,z in by_input[y]:
            if x == w: continue
            result[min(x,w),max(x,w),z] += coefficient*(1 if x<w else -1)
    return {key:value for key,value in result.items() if value}


def first_rank_mod2(dimensions, terms, leg=0):
    other = [i for i in range(3) if i != leg]
    first,second = dimensions[leg],dimensions[other[0]]
    by_input = defaultdict(list)
    for term in terms: by_input[term[other[0]]].append((term[leg],term[other[1]]))
    row_ids, pivots = {}, {}
    for w in range(first):
        for y in range(second):
            vector = 0
            for x,z in by_input[y]:
                if x == w: continue
                row = (min(x,w), max(x,w), z)
                if row not in row_ids: row_ids[row] = len(row_ids)
                vector ^= 1<<row_ids[row]
            while vector:
                pivot = vector.bit_length()-1
                if pivot in pivots: vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    break
    return len(pivots)


def matrix_blocks(shapes):
    dimensions = [0,0,0]; terms = []
    for l,b,r in shapes:
        terms.extend((dimensions[0]+i*r+k, dimensions[1]+i*b+j, dimensions[2]+j*r+k)
                     for i in range(l) for j in range(b) for k in range(r))
        dimensions = [d+e for d,e in zip(dimensions,[l*r,l*b,b*r])]
    return tuple(dimensions), terms


def slice_matrix(a, coefficients):
    import sympy as sp
    width = 2*a-1
    return sp.Matrix(a*width, a*width,
        lambda row,col: coefficients[col//a-row//width, row%width-col%a]
        if 0<=col//a-row//width<a and 0<=row%width-col%a<a else 0)


def grade_upper(a, maximum):
    """Dimension upper bounds, without claiming the actual Koszul ranks."""
    counts = [Counter() for _ in range(maximum+2)]
    counts[0][0,0] = 1
    for x in range(a):
        for y in range(a):
            for p in range(maximum+1,0,-1):
                for (u,v),value in list(counts[p-1].items()): counts[p][u+x,v+y] += value
    report = []
    for p in range(maximum+1):
        columns,rows = Counter(),Counter()
        for (x,y),value in counts[p].items():
            for i in range(a):
                for j in range(2*a-1): columns[x-i,y+j] += value
        for (x,y),value in counts[p+1].items():
            for i in range(2*a-1):
                for j in range(a): rows[x-i,y+j] += value
        upper = min(sum(min(value,rows[key]) for key,value in columns.items()),
                    (2*a-1)**2*comb(a*a-1,p))
        report.append({'power':p,'source_grading_upper':upper})
    return report


def verification():
    ranks = []
    for a in range(2,7):
        dimensions,terms = source(a)
        for label in range(3*a-2):
            if first_koszul_image(terms,kernel_vector(a,label)):
                raise ArithmeticError('claimed kernel vector has nonzero exact image')
        actual = [first_rank_mod2(dimensions,terms,leg) for leg in range(3)]
        expected = a**3*(2*a-1)-(3*a-2)
        if actual[0] != expected: raise ArithmeticError('modular lower bound does not match proved upper')
        ranks.append({'a':a,'format':list(dimensions),'kernel_dimension':3*a-2,
                      'first_koszul_rank':expected,'three_mod2_ranks':actual})
    dimensions,terms = matrix_blocks([(4,9,4),(3,3,3)])
    target_rank = first_rank_mod2(dimensions,terms)
    if target_rank != 1125: raise ArithmeticError('size-five target rank control failed')
    if not (2441**10000 < 5184**7499*4**10000 and
            1391**10000 < 972**7499*8**10000 and Fraction(6273,8)>784):
        raise ArithmeticError('excluded conditional threshold failed')
    if not 12960**2235 > 34**6000: raise ArithmeticError('selected finite threshold failed')
    graded = grade_upper(6,5)
    for row in graded:
        row['target_injective_rank'] = 60*comb(36,row['power'])
        row['rejected_by_this_coarse_bound'] = row['target_injective_rank']>row['source_grading_upper']
    _,open_terms = matrix_blocks([(6,10,6)])
    open_ranks = [first_rank_mod2((36,66,66),open_terms,leg) for leg in range(3)]
    return {'source_kernel_controls':ranks,
            'excluded_size_five_target':{'shapes':[[4,9,4],[3,3,3]],'format':list(dimensions),
                                       'target_mod2_rank':target_rank,'source_exact_rank':1112},
            'conditional_threshold_integer_checks':{'excluded_size_five_2_2497':True,
                                                    'unconstructed_size_six_2_235':True},
            'historical_size_six_first_tests':{'a':6,'b':10,'source_format':[36,66,66],
                                    'target_format':[36,60,60],'constructed':False,
                                    'current_status':'Excluded at power seven; see all-power-controls.json.',
                                    'source_first_rank':2360,'target_first_rank':2160,
                                    'source_three_first_ranks':[2360,2376,2376],
                                    'target_three_padded_first_ranks':open_ranks,
                                    'ordinary_restriction_test':[110,96],
                                    'adopted_coordinate_input_screen':[288,121,360,121],
                                    'coarse_higher_tests':graded},
            'proof_status':'Written, unreviewed; finite controls do not prove the all-size formula.',
            'improves_omega':False}


if __name__ == '__main__':
    import argparse,json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args();text = json.dumps(verification(),indent=2)+'\n'
    if args.output: args.output.write_text(text)
    print(text,end='')
