"""Exact finite controls for the written slice-rank-gap argument.

The small binary enumerations and explicit rational ranks check finite
instances. The general theorem rests on the proof in slice_rank_gap.md.
"""
from collections import Counter
from itertools import product
import json
from pathlib import Path

from central_minrank import rank_mod_two
from verify import slice_entry, source_frontier


def biform_entry(f, a, b, row, column):
    j, long_row = row
    long_column, r = column
    i, s = long_column-j, long_row-r
    return f[i*b+s] if 0 <= i < a and 0 <= s < b else 0


def biform_matrix(f, a, b):
    m = a+b-1
    return [[biform_entry(f,a,b,row,column)
             for column in product(range(m),range(a))]
            for row in product(range(b),range(m))]


def full_matrix(f, a, b):
    m = a+b-1
    return [[slice_entry(f,a,b,row,column)
             for column in product(range(m),range(b),range(a))]
            for row in product(range(b),range(a),range(m))]


def binary_biform_controls():
    reports = []
    for a,b in ((2,2),(2,3),(3,3),(3,4)):
        histogram = Counter()
        minimum = 0
        for bits in range(1,1 << (a*b)):
            f = [(bits >> j)&1 for j in range(a*b)]
            rank = rank_mod_two(biform_matrix(f,a,b))
            coefficient_rank = rank_mod_two([f[i*b:(i+1)*b] for i in range(a)])
            if (rank == a*b) != (coefficient_rank == 1):
                raise ArithmeticError("The biform minimum-rank classification failed")
            if rank != a*b and rank < a*b+a:
                raise ArithmeticError("A binary biform violates the proposed rank gap")
            histogram[rank] += 1
            minimum += rank == a*b
        reports.append({"a":a,"b":b,"nonzero_slices":(1 << (a*b))-1,
                        "minimum_rank_slices":minimum,
                        "rank_histogram":dict(sorted(histogram.items()))})
    return reports


def binary_full_control():
    a = b = 2
    m = a+b-1
    histogram = Counter()
    actual_minimum = set()
    for bits in range(1,1 << (a*b*m)):
        f = [(bits >> j)&1 for j in range(a*b*m)]
        rank = rank_mod_two(full_matrix(f,a,b))
        if rank != a*b and rank < a*b+a:
            raise ArithmeticError("A binary full-source slice violates the proposed gap")
        histogram[rank] += 1
        if rank == a*b:
            actual_minimum.add(bits)
    expected_minimum = set()
    hankel_profiles = ((1,0,0),(1,1,1),(0,0,1))
    nonzero_pairs = ((1,0),(0,1),(1,1))
    for u,h,v in product(nonzero_pairs,hankel_profiles,nonzero_pairs):
        f = [u[i]*h[k]*v[s] for i,k,s in product(range(a),range(m),range(b))]
        expected_minimum.add(sum(c << j for j,c in enumerate(f)))
    if actual_minimum != expected_minimum:
        raise ArithmeticError("The full-source minimum-rank locus classification failed")
    return {"a":a,"b":b,"nonzero_slices":4095,
            "minimum_rank_slices":len(actual_minimum),
            "minimum_locus_matches_product_hankel_classification":True,
            "rank_histogram":dict(sorted(histogram.items()))}


def rational_gap_examples():
    import sympy as sp
    records = []
    for a,b in ((2,2),(2,3),(3,3),(3,4),(4,5),(5,5)):
        f = [0]*(a*b)
        f[0] = f[b+1] = 1
        # A full source slice supported at middle index zero has exactly
        # one nonzero block, so its rank equals this rational block rank.
        rank = sp.Matrix(biform_matrix(f,a,b)).rank()
        if rank != a*b+a:
            raise ArithmeticError("The stated sharpness example has the wrong rank")
        records.append({"a":a,"b":b,"biform":"1+x*z",
                        "middle_profile":"h_0=1; all other h_k=0",
                        "exact_rational_full_slice_rank":rank})
    return records


def enhanced_frontier(maximum_leg_dimension=300):
    survivors = []
    new_exclusions = []
    for source in source_frontier(maximum_leg_dimension):
        a,b = source["a"],source["b"]
        if a < 2:
            continue
        n = source["source_leg_dimension"]
        for shape in source["improving_shapes"]:
            if not shape["passes_minimum_rank_screen"]:
                continue
            l,h,r = shape["shape"]
            conditions = [x+y-2 > a+b-1 for x,y,z in ((l,h,r),(h,r,l),(r,l,h))]
            slacks = [2*n-a*b-a-z*(x+y-1) if use else old
                      for (x,y,z),use,old in zip(((l,h,r),(h,r,l),(r,l,h)),
                                                 conditions,shape["minimum_rank_slacks"])]
            item = {"a":a,"b":b,"source_leg_dimension":n,
                    "shape":shape["shape"],"volume":shape["volume"],
                    "rank_gap_dimension_conditions":conditions,
                    "rank_gap_slacks":slacks}
            if min(slacks) < 0:
                new_exclusions.append(item)
            else:
                survivors.append(item)
    return {"maximum_leg_dimension":maximum_leg_dimension,
            "excluded_after_minimum_rank_screen":new_exclusions,
            "remaining_finite_screen_survivors":survivors,
            "screen_survival_is_not_a_construction":True}


def report():
    return {"status":"written proof with exact finite controls; independent AI review completed",
            "independent_ai_review":True,"human_review":False,"formal_verification":False,
            "new_exponent_established":False,"target_constructed":False,
            "ordinary_restriction_only":True,
            "selected_target":{"source_lengths":[4,5],"target_shape":[12,12,13],
                 "lifted_rank_upper_bound":21,"source_minimum_rank":20,
                 "source_next_rank_lower_bound":24,
                 "source_minimum_locus_projective_dimension":8,
                 "target_rank_one_locus_projective_dimension":22},
            "binary_biform_controls":binary_biform_controls(),
            "binary_full_source_control":binary_full_control(),
            "rational_gap_examples":rational_gap_examples(),
            "enhanced_frontier":enhanced_frontier()}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    payload = json.dumps(report(),indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload,end="")
