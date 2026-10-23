"""Exact controls for a formal-operation repair barrier, not tensor obstructions.

The imported monotone is from Amanov--van den Berg--Zuiddam,
arXiv:2610.30054v1, Definition 5.5 and Proposition 5.9.  See README.md for
the precise formal preorder, tensor-leg convention, and all-size proof.
Acceptance decisions use integers and fractions only.
"""

import argparse
from fractions import Fraction
import json
from math import factorial
from pathlib import Path


def parameter(value):
    """Accept an exact parameter strictly between one and two."""
    if not isinstance(value, (int, str, Fraction)) or isinstance(value, bool):
        raise ValueError("Use an integer, fraction, or exact rational string.")
    value = Fraction(value)
    if not 1 < value < 2:
        raise ValueError("The parameter must satisfy 1 < p < 2.")
    return value


def positive_integer(value, name):
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise ValueError(f"{name} must be a positive integer.")
    return value


def dot_exponents(value):
    """Return theta and the three exponents in the paper's leg convention."""
    p = parameter(value)
    theta = ((2 - p) / p, (p - 1) / p, (p - 1) / p)
    exponents = (p * (2 - p), p / 2, p / 2)
    return theta, exponents


def source_branch(n, b, value):
    """The exact branch condition; n >= 2*b-1 is only sufficient."""
    positive_integer(n, "n")
    positive_integer(b, "b")
    p = parameter(value)
    return n - 1 >= 2 * (p - 1) * (b - 1)


def formal_powers(n, b, l, h, r, value):
    """Return target^D and source^D as fractions, for D=2*q^2.

    The target is M(l,h,r) in repository order (lr,lh,hr).  Its value is
    (l*r)^(p/2)*h^(p*(2-p)).  The source is Q(n,b).  These are values on
    the specified formal expressions, not invariants of arbitrary tensors.
    """
    for name, dimension in zip(("n", "b", "l", "h", "r"), (n, b, l, h, r)):
        positive_integer(dimension, name)
    p = parameter(value)
    if not source_branch(n, b, p):
        raise ValueError("This formula requires n-1 >= 2*(p-1)*(b-1).")
    a, q = p.numerator, p.denominator
    u = 2 * q - a
    degree = 2 * q * q
    target = Fraction((l * r) ** (a * q) * h ** (2 * a * u))
    source = (
        Fraction(q + a * (b - 1), q) ** (2 * q * u)
        * Fraction(q * n + u * (b - 1), q) ** (2 * a * q)
    )
    return degree, target, source


def integer_root_floor(value, degree):
    """Floor of a nonnegative integer's positive integer root."""
    if not isinstance(value, int) or value < 0:
        raise ValueError("The radicand must be a nonnegative integer.")
    positive_integer(degree, "degree")
    if value < 2 or degree == 1:
        return value
    low = 0
    high = 1 << ((value.bit_length() + degree - 1) // degree)
    while high - low > 1:
        middle = (low + high) // 2
        if middle ** degree <= value:
            low = middle
        else:
            high = middle
    return low


def root_interval(value, degree, bits=48):
    """A certified dyadic enclosure; exact dyadic roots get zero width."""
    value = Fraction(value)
    if value < 0:
        raise ValueError("The radicand must be nonnegative.")
    positive_integer(degree, "degree")
    positive_integer(bits, "bits")
    scale = 1 << bits
    scaled_numerator = value.numerator * scale ** degree
    floor = integer_root_floor(scaled_numerator // value.denominator, degree)
    lower = Fraction(floor, scale)
    if floor ** degree * value.denominator == scaled_numerator:
        return lower, lower
    return lower, Fraction(floor + 1, scale)


def finite_certificate(n, b, l, h, r, value, scalar_repair=0, bits=48):
    """Export exact comparisons and a rigorous lower bound on scalar repair.

    A false exclusion flag means only that this one parameter did not
    exclude the relation.  It does not certify a formal derivation or maps.
    """
    if not isinstance(scalar_repair, int) or scalar_repair < 0:
        raise ValueError("Scalar repair must be a nonnegative integer.")
    p = parameter(value)
    degree, target, source = formal_powers(n, b, l, h, r, p)
    target_interval = root_interval(target, degree, bits)
    source_interval = root_interval(source, degree, bits)
    gap_lower = target_interval[0] - source_interval[1]
    gap_upper = target_interval[1] - source_interval[0]
    if target == source:
        gap_lower = gap_upper = Fraction(0)
    integer_lower = max(0, -((-gap_lower.numerator) // gap_lower.denominator))
    # Cross multiplication is an independent exact no-repair decision.
    left = target.numerator * source.denominator
    right = source.numerator * target.denominator
    if left > right:
        integer_lower = max(1, integer_lower)
    return {
        "source": {"n": n, "b": b},
        "target": {"l": l, "h": h, "r": r},
        "p": str(p),
        "branch_condition_holds": True,
        "power_degree": degree,
        "target_power": str(target),
        "source_power": str(source),
        "cleared_target_power": str(left),
        "cleared_source_power": str(right),
        "no_scalar_repair_ruled_out": left > right,
        "gap_interval": [str(gap_lower), str(gap_upper)],
        "certified_integer_scalar_repair_lower_bound": integer_lower,
        "tested_scalar_repair": scalar_repair,
        "tested_formal_relation_ruled_out": (
            left > right if scalar_repair == 0 else gap_lower > scalar_repair
        ),
        "scope": "Specified formal preorder only; not an actual tensor obstruction.",
    }


def coefficient_positive(b, value):
    """Exact check of b^p > 1+p*(b-1), equivalent to D_b(p)>0."""
    positive_integer(b, "b")
    p = parameter(value)
    a, q = p.numerator, p.denominator
    return q ** q * b ** a > (q + a * (b - 1)) ** q


def log_interval(value, terms=32):
    """Certified natural logarithm by the atanh series and a geometric tail."""
    value = Fraction(value)
    if value <= 0:
        raise ValueError("The logarithm argument must be positive.")
    positive_integer(terms, "terms")
    if value < 1:
        lower, upper = log_interval(1 / value, terms)
        return -upper, -lower
    z = (value - 1) / (value + 1)
    total = sum((2 * z ** (2 * k + 1) / (2 * k + 1) for k in range(terms)),
                Fraction(0))
    remainder = 2 * z ** (2 * terms + 1) / ((2 * terms + 1) * (1 - z * z))
    return total, total + remainder


def e_interval(terms=32):
    """Certified e from its positive series with a geometric tail bound."""
    positive_integer(terms, "terms")
    total = sum((Fraction(1, factorial(k)) for k in range(terms + 1)), Fraction(0))
    remainder = Fraction(terms + 2, (terms + 1) * factorial(terms + 1))
    return total, total + remainder


def logarithmic_constant_interval(b, terms=32):
    """Enclose ln(b^2/(2*b-1))/e, using natural logarithms."""
    positive_integer(b, "b")
    log_lower, log_upper = log_interval(Fraction(b * b, 2 * b - 1), terms)
    e_lower, e_upper = e_interval(terms)
    return log_lower / e_upper, log_upper / e_lower


def decimal_enclosure(interval, digits=12):
    """Outward rounding to rational decimal endpoints, without float math."""
    positive_integer(digits, "digits")
    scale = 10 ** digits
    lower, upper = interval
    lo = (lower.numerator * scale) // lower.denominator
    hi = -((-upper.numerator * scale) // upper.denominator)
    return Fraction(lo, scale), Fraction(hi, scale)


def certificate():
    examples = [
        finite_certificate(8, 4, 8, 4, 8, Fraction(15, 8)),
        finite_certificate(20, 4, 19, 4, 19, Fraction(8, 5)),
        finite_certificate(29, 4, 27, 4, 27, Fraction(3, 2)),
        # The exact branch holds here even though n < 2*b-1.
        finite_certificate(6, 4, 5, 4, 5, Fraction(7, 4)),
        # Width one is an equality control, outside the strict theorem.
        finite_certificate(8, 1, 8, 1, 8, Fraction(15, 8)),
    ]
    parameters = sorted({Fraction(a, q) for q in range(2, 13)
                         for a in range(q + 1, 2 * q)})
    positivity_checks = 0
    for b in range(2, 33):
        for p in parameters:
            if not coefficient_positive(b, p):
                raise ArithmeticError("A positive coefficient control failed.")
            positivity_checks += 1
    interval = logarithmic_constant_interval(4)
    rounded = decimal_enclosure(interval)
    if rounded != (Fraction(304118051531, 10 ** 12),
                   Fraction(304118051532, 10 ** 12)):
        raise ArithmeticError("The width-four natural-logarithm bracket changed.")
    return {
        "claim_id": "AI-OPERATIONAL-REPAIR-BARRIER-001",
        "date": "2026-10-23",
        "status": "written proof with exact finite controls; unreviewed",
        "external_input": "arXiv:2610.30054v1, Definitions 5.3/5.5 and Proposition 5.9",
        "formal_preorder_only": True,
        "actual_tensor_degeneration_excluded": False,
        "improves_omega": False,
        "source_branch": "n-1 >= 2*(p-1)*(b-1)",
        "source_value": "(1+p*(b-1))^(2-p)*(n+(2-p)*(b-1))^p",
        "target_value": "(l*r)^(p/2)*h^(p*(2-p))",
        "all_size_coefficient_proof": "strict convexity of x^p for 1<p<2, b>1",
        "finite_positivity_controls": positivity_checks,
        "parameter_count": len(parameters),
        "examples": examples,
        "logarithm_convention": "natural logarithm",
        "fixed_defect_constant": "ln(b^2/(2*b-1))/e",
        "width_four_constant_rational_bracket": [str(x) for x in rounded],
        "logarithmic_defect_constant": "A*exp(-1-alpha/A), A=ln(b^2/(2*b-1))",
        "defect_hypothesis": "limsup (ln n)*ln(n^2/(l_n*r_n)) <= alpha, 0<l_n,r_n<=n",
        "sharpness_scope": "Fixed nonnegative outer defects; this one-parameter family only.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = certificate()
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
    print(serialized, end="")
