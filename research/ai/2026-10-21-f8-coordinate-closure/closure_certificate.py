"""Exact replay of the complete F8 one-source coordinate-target count cover.

Discovery tags are untrusted. Each positive pair tag proves either a
pair-map capacity violation or a Koszul averaging violation. All triangles
left by zero tags receive an independently checked exact alignment.
"""
import argparse
from collections import Counter
import hashlib
from itertools import permutations,product
import json
from math import comb
from pathlib import Path
import sys
import zlib

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-10-20-f8-unequal'))
from koszul_tables import koszul_matrix,rank_mod,verify
from pair_averaging import classes,coverage,rotate
from f8_source_frontier import report as source_frontier


def tables(base_pencils,even_pencils):
    verify(base_pencils)
    keys = set()
    for row in even_pencils['records']:
        a,b,d,p = (row[k] for k in ['a','b','slice_dimension','p'])
        if any(type(v) is not int for v in [a,b,d,p,row['rank_lower_bound']]):
            raise ValueError('integer dimensions and ranks required')
        key = a,b,d,p
        if key in keys or key not in {(a,b,d,p) for a,b in product(range(1,5),repeat=2) for d,p in [(4,1),(6,2)]}:
            raise ValueError('duplicate or unsupported even pencil')
        keys.add(key)
        slices = row['integer_slices']
        if len(slices)!=d or any(len(X)!=a or any(len(line)!=b for line in X) for X in slices):
            raise ValueError('wrong even pencil shape')
        if row['rank_one_contribution']!=comb(d-1,p) or row['modulus']!=101:
            raise ValueError('wrong divisor or modulus')
        matrix = koszul_matrix(slices,p)
        if row['matrix_format']!=[len(matrix),len(matrix[0])] or rank_mod(matrix,101)!=row['rank_lower_bound']:
            raise ValueError('unverified even rank')
    if len(keys)!=32:
        raise ValueError('incomplete even pencil table')
    records = base_pencils['records']+even_pencils['records']
    result = [(3,1,2,[[3*min(a,b)-int(a==b==1) if a*b else 0
                       for b in range(5)] for a in range(5)])]
    for d,p in [(4,1),(5,2),(6,2),(7,3)]:
        table = [[0]*5 for _ in range(5)]
        for row in records:
            if (row['slice_dimension'],row['p'])==(d,p):
                table[row['a']][row['b']] = row['rank_lower_bound']
        result.append((d,p,comb(d-1,p),table))
    return result


def unpack(data):
    decoder = zlib.decompressobj()
    raw = decoder.decompress(data)
    raw += decoder.flush()
    if not decoder.eof or decoder.unused_data or decoder.unconsumed_tail:
        raise ValueError('incomplete or trailing compressed data')
    return raw


def replay(raw,base_pencils,even_pencils):
    levels = tables(base_pencils,even_pencils)
    frontier = source_frontier()
    shapes = frontier['minimal_surviving_shapes']
    all_totals = sorted({v for row in shapes for v in row})
    rows = {total:classes(total) for total in all_totals}
    covered = {str(total):coverage(rows[total],total) for total in all_totals}
    rotations = {total:[[rotate(row,s) for s in range(7)] for row in rows[total]] for total in all_totals}
    position = 0
    formats = []
    permutation_rows = list(permutations(range(3)))

    def pair_grid(first,second,third):
        nonlocal position
        A,B = rows[first],rows[second]
        size = len(A)*len(B)
        if position+size>len(raw):
            raise ValueError('truncated pair grid')
        masks = []
        bad = 0
        for a in A:
            mask = 0
            for j in range(len(B)):
                tag = raw[position]
                position += 1
                if tag==0:
                    mask |= 1 << j
                    bad += 1
                    continue
                if tag<=7:
                    b = rotations[second][j][tag-1]
                    if sum(x*y for x,y in zip(a,b))<=64:
                        raise ValueError('invalid capacity tag')
                elif tag<78:
                    level,rest = divmod(tag-8,14)
                    reverse,shift = divmod(rest,7)
                    d,p,divisor,table = levels[level]
                    b = rotations[second][j][shift]
                    weight = (sum(table[y][x] for x,y in zip(a,b)) if reverse else
                              sum(table[x][y] for x,y in zip(a,b)))
                    if third*weight<=7*64*divisor:
                        raise ValueError('invalid Koszul averaging tag')
                else:
                    raise ValueError('invalid pair tag')
            masks.append(mask)
        return masks,bad,size

    for shape in shapes:
        a,b,c = shape
        ab,nab,sab = pair_grid(a,b,c)
        ac,nac,sac = pair_grid(a,c,b)
        bc,nbc,sbc = pair_grid(b,c,a)
        explicit = 0
        histogram = Counter()
        start = position
        for i,neighbors in enumerate(ab):
            while neighbors:
                bit = neighbors & -neighbors
                neighbors ^= bit
                j = bit.bit_length()-1
                common = ac[i] & bc[j]
                while common:
                    bit = common & -common
                    common ^= bit
                    k = bit.bit_length()-1
                    if position+2>len(raw):
                        raise ValueError('truncated triangle tag')
                    tag = raw[position]+256*raw[position+1]
                    position += 2
                    if tag>=5*6*49:
                        raise ValueError('invalid triangle tag')
                    outer,shifts = divmod(tag,49)
                    level,permutation = divmod(outer,6)
                    left_shift,right_shift = divmod(shifts,7)
                    triple = [rows[a][i],rows[b][j],rows[c][k]]
                    order = permutation_rows[permutation]
                    X,Y,Z = [triple[v] for v in order]
                    d,p,divisor,table = levels[level]
                    rank = sum(z*table[x][y] for x,y,z in
                               zip(X,rotate(Y,left_shift),rotate(Z,right_shift)))
                    if rank<=64*divisor:
                        raise ValueError('invalid explicit Koszul alignment')
                    histogram[str((d,p,rank,64*divisor))] += 1
                    explicit += 1
        formats.append({'shape':shape,'cyclic_class_counts':[len(rows[v]) for v in shape],
                        'pair_tags_checked':sab+sac+sbc,'uncertified_pair_counts':[nab,nac,nbc],
                        'explicit_triangles_checked':explicit,'explicit_tag_offset':start,
                        'explicit_rank_histogram':dict(sorted(histogram.items()))})
    if position!=len(raw):
        raise ValueError('unused certificate bytes')
    return {'normal_subgroup_order':64,'quotient_order':7,'fiber_bound':4,
            'pencils_replayed':64,'bounded_composition_counts':covered,
            'sorted_shapes_screened':frontier['all_sorted_shapes_checked'],
            'rank_locus_survivors':len(frontier['rank_locus_surviving_shapes']),
            'minimal_formats_covered':len(shapes),'formats':formats,
            'pair_tags_checked':sum(row['pair_tags_checked'] for row in formats),
            'explicit_triangles_checked':sum(row['explicit_triangles_checked'] for row in formats),
            'uncompressed_certificate_bytes':len(raw),'uncompressed_sha256':hashlib.sha256(raw).hexdigest(),
            'scope':'Complete single-target source-degree-sum obstruction for F8^2:C7 via injective pair maps and strict vertex potentials. General complex degenerations and joint extraction are not excluded.',
            'status':'written proof with complete finite certificate; unreviewed',
            'improves_omega':False}


if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('base_pencils',type=Path)
    parser.add_argument('even_pencils',type=Path)
    parser.add_argument('cover',type=Path)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    receipt = replay(unpack(args.cover.read_bytes()),json.loads(args.base_pencils.read_text()),
                     json.loads(args.even_pencils.read_text()))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ['formats']},indent=2))
