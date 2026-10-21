"""Complete cyclic count-pattern Koszul screen for seven fibers of size >=2.

Each family has nineteen points and fiber sizes at most four. Directions,
offsets and strict potentials are not constructed by this finite screen.
"""
from itertools import combinations_with_replacement,product
import argparse
import json
from pathlib import Path


def rotate(row,shift):
    return row[shift:]+row[:shift]


def classes():
    return sorted({min(rotate(row,shift) for shift in range(7))
                   for row in product(range(2,5),repeat=7) if sum(row)==19})


def run():
    patterns = classes()
    masks = [[(sum(1<<i for i,v in enumerate(rotate(row,shift)) if v>=3),
               sum(1<<i for i,v in enumerate(rotate(row,shift)) if v>=4))
              for shift in range(7)] for row in patterns]
    histogram = {}
    survivors = []
    family_histogram = {}
    for triple in combinations_with_replacement(range(len(patterns)),3):
        a,b,c = triple
        a3,a4 = masks[a][0]
        best = max(84+15*(a3 & b3 & c3).bit_count()+21*(a4 & b4 & c4).bit_count()
                   for b3,b4 in masks[b] for c3,c4 in masks[c])
        histogram[best] = histogram.get(best,0)+1
        if best <= 128:
            survivors.append({'indices':list(triple),'maximum_Koszul_rank':best})
            number = sum(4 in patterns[i] for i in triple)
            family_histogram[number] = family_histogram.get(number,0)+1
    return {'claim':'EXP-GROUP-NORMAL-COUNTS-012','target_shape':[19]*3,
            'normal_subgroup':'C2^6','quotient':'C7','fiber_sizes':[2,3,4],
            'cyclic_pattern_classes':[list(row) for row in patterns],
            'triples_mod_family_permutation_checked':sum(histogram.values()),
            'maximum_rank_histogram':{str(k):v for k,v in sorted(histogram.items())},
            'unexcluded_pattern_triples':survivors,
            'unexcluded_by_number_of_families_with_four_point_fibers':
                {str(k):v for k,v in sorted(family_histogram.items())},
            'scope':__doc__,'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                     ['cyclic_pattern_classes','unexcluded_pattern_triples']},indent=2))
