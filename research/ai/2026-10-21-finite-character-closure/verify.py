#!/usr/bin/env python3
"""Exact finite-profile comparisons; no floating acceptance decisions."""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path

CASES = [
    (4, 5, 10, "accepted"),
    (5, 6, 16, "accepted"),
    (6, 7, 24, "accepted"),
    (7, 8, 34, "accepted"),
    (5, 7, 15, "accepted-independent-sectors"),
    (8, 9, 46, "hypothetical-unrecovered-certificate"),
]
EXPECTED_RATIOS = [F(27,35), F(10287,13468), F(135,182),
                   F(19521,27170), F(10287,13832), F(729,1045)]
EXPECTED_THIN = [F(162,175), F(10287,11648), F(1215,1456),
                 F(292815,369512), F(30861,34580), F(3645,4807)]
EXPECTED_FORMAT = [F(6561,8281), F(597871125,725548096), F(1594323,1952288),
                   F(14765025303,18455222500), F(597871125,765296896),
                   F(2259436291848,2883628515625)]
H = [F(0), F(1)]
for j in range(1, 1300):
    H.append(H[-1] * F(3*j+1, 3*j))

def linear(a, b):
    a, b = sorted((a,b))
    return b + F(a-1, 2)

def profile(a, b, c=F(1)):
    if min(a,b) == 0:
        return F(0)
    return (c*H[min(a,b)]-(c-1))*linear(a,b)

def target_sum(m):
    if m % 2 == 0:
        n = m//2
        return F((6*n+1)*(3*n+1),7)*H[n]
    n = (m+1)//2
    return F(18*n*n-12*n+1,7)*H[n]

def verify():
    rows = []
    for index, (m,a,b,status) in enumerate(CASES):
        total = sum((profile(r,m+1-r) for r in range(1,m+1)), F(0))
        assert total == target_sum(m)
        source = profile(a,b)
        target_linear = sum((linear(r,m+1-r) for r in range(1,m+1)), F(0))
        assert total/source == EXPECTED_RATIOS[index] < 1
        assert total/(b*H[a]) == EXPECTED_THIN[index] < 1
        n = m*(m+1)//2
        format_ratio = F(m*n*n)/(source*source)
        assert format_ratio == EXPECTED_FORMAT[index] < 1
        assert linear(a,b) < target_linear and b < target_linear
        for c in (F(1), F(21,20)):
            pc_target = sum((profile(r,m+1-r,c) for r in range(1,m+1)),F(0))
            hc = c*H[a]-(c-1)
            assert profile(a,b,c) > pc_target
            assert b*hc > pc_target
            for copies in (1,2,53,1000):
                assert profile(a,copies*b,c) >= copies*pc_target
        lower_cube = total**3/(a*(F(b)+F(a,2))**3)
        old_cube = H[a]**3/a
        assert lower_cube < old_cube
        rows.append({"m":m, "a":a, "B":b, "status":status,
                     "target_sum":str(total), "source_model":str(source),
                     "slack":str(source-total), "score_ratio":str(total/source),
                     "copy_limit_ratio":str(total/(b*H[a])),
                     "matrix_extraction_format_ratio":str(format_ratio),
                     "direct_amplitude_lower_cubed":str(lower_cube),
                     "existing_width_lower_cubed":str(old_cube)})
    assert F(27,32)*F(21,20)**3 == F(250047,256000) < 1
    assert F(5,3)**4/8 == F(625,648) < 1
    sum_checks = 0
    for m in range(1, 201):
        total = sum((profile(r,m+1-r) for r in range(1,m+1)),F(0))
        assert total == target_sum(m)
        sum_checks += 1
    crossings = []
    expected = [(4,53),(22,71),(38,88),(54,104)]
    for excess, (thin_expected,single_expected) in enumerate(expected):
        thin = next(m for m in range(1,201)
                    if target_sum(m) > (m*(m+1)//2)*H[m+excess])
        single = next(m for m in range(1,201)
                      if target_sum(m) > profile(m+excess,m*(m+1)//2))
        assert (thin,single) == (thin_expected,single_expected)
        crossings.append({"shared_excess":excess, "first_copy_limit":thin,
                          "first_single":single})
    controls = 0
    for c in (F(1), F(41,40), F(21,20)):
        for a in range(1,25):
            for b in range(1,25):
                p = profile(a,b,c)
                assert p > 0 and p == profile(b,a,c)
                assert profile(1,b,c) == b
                assert 2*p >= profile(a,b-1,c)+profile(a,b+1,c)
                assert profile(a,3*b+a-1,c) >= 3*p
                assert p**3 <= (a+b-1)**4
                assert (2*p)**3 <= (a+2*b-1)**4
                assert (2*p)**3 <= (2*a+b-1)**4
                for q in (2,3,7):
                    assert profile(q*a,q*b,c)**3 >= q**4*p**3
                controls += 1
    return {"cases":rows, "all_accepted_maps_compatible":True,
            "hypothetical_cost_free_copies_compatible":True,
            "feasible_c_interval":["1","21/20"], "sum_formula_checks":sum_checks,
            "first_crossings":crossings, "profile_grid_controls":controls,
            "scope":"Exact compatibility and closure for the stated scalar rules; no endpoint character or exponent improvement."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    report = json.dumps(verify(), indent=2) + "\n"
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report)
    print(report, end="")
