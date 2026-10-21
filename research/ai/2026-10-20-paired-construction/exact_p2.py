"""An exact P_2 -> M(2,2,2) restriction over the integers.

This positive construction calibrates searches on the paired source.  It
does not improve the matrix multiplication exponent.  Verification uses
only Python integers and checks every source monomial, including terms
which cancel outside the target support.
"""

from collections import Counter, defaultdict
from itertools import product
import argparse
import json
from pathlib import Path


def maps():
    """Source coordinate -> (integer coefficient, target coordinate)."""
    first = {(p, q): (1, (q, p)) for p, q in product(range(2), repeat=2)}
    second = {
        (0, 0): (1, (1, 1)), (0, 1): (1, (0, 0)), (0, 2): (1, (1, 0)),
        (1, 0): (1, (0, 1)), (1, 1): (1, (1, 1)), (1, 2): (1, (0, 0)),
    }
    third = {
        (0, 0): (-1, (0, 1)), (0, 1): (1, (0, 0)),
        (1, 0): (1, (1, 0)), (1, 1): (1, (0, 1)),
        (2, 0): (1, (1, 1)), (2, 1): (-1, (1, 0)),
    }
    return first, second, third


def expansion():
    """Return all 16 contributions before combining like monomials."""
    first, second, third = maps()
    answer = []
    for p, q, y, v in product(range(2), repeat=4):
        fa, a = first[p, q]
        fb, b = second[y, q+v]
        fc, c = third[p+y, v]
        answer.append({"source_indices": [p, q, y, v], "coefficient": fa*fb*fc,
                       "target_indices": [list(a), list(b), list(c)]})
    return answer


def certificate():
    contributions = expansion()
    by_monomial = defaultdict(list)
    for term in contributions:
        key = tuple(tuple(x) for x in term["target_indices"])
        by_monomial[key].append(term["coefficient"])
    coefficients = {key: sum(values) for key, values in by_monomial.items()}
    actual = {key: value for key, value in coefficients.items() if value}
    wanted = {((i, k), (i, j), (j, k)): 1
              for i, j, k in product(range(2), repeat=3)}
    if len(contributions) != 16 or actual != wanted:
        raise ArithmeticError("The full integer tensor identity failed")
    canceled = [{"target_indices": [list(x) for x in key],
                 "contributions": values, "coefficient": sum(values)}
                for key, values in sorted(by_monomial.items()) if not sum(values)]
    if len(canceled) != 4 or any(sorted(t["contributions"]) != [-1, 1] for t in canceled):
        raise ArithmeticError("The four off-support cancellations changed")
    return {
        "source": "P_2", "target": "M(2,2,2)",
        "source_dimensions": [4, 6, 6], "target_dimensions": [4, 4, 4],
        "target_convention": "sum_(i,j,k) a_(i,k) b_(i,j) c_(j,k)",
        "coefficient_ring": "Z", "valid_over_every_field": True,
        "source_terms_checked": 16, "monomials_touched": len(coefficients),
        "target_terms": len(actual), "off_support_cancellations": canceled,
        "all_source_contributions": contributions,
        "restriction_constructed": True, "singular_family_required": False,
        "improves_omega": False,
        "scope": "An exact small-source construction and positive search control; no exponent gain.",
    }


def multiply(left, right):
    """Evaluate the restriction in the conventional matrix-product order."""
    _, second, third = maps()
    b = {source: coefficient*left[i][j]
         for source, (coefficient, (i, j)) in second.items()}
    c = {source: coefficient*right[j][k]
         for source, (coefficient, (j, k)) in third.items()}
    # A_(p,q) maps to a_(q,p), so the output indices are i=q and k=p.
    return [[sum(b[y, i+v]*c[k+y, v] for y, v in product(range(2), repeat=2))
             for k in range(2)] for i in range(2)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = certificate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in {"all_source_contributions", "off_support_cancellations"}}, indent=2))
