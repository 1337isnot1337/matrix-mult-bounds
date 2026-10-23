# Exact boundary for two equal staircase legs

October 23, 2026. This is a finite experiment with a written completeness
argument for its specified class. No claim of arbitrary cover optimality,
independent mathematical review, target construction or exponent gain.

The source and degree hypotheses are those of the pinned
[S5 finite cube proof](../2026-10-23-s5-finite-covers/proof.md).
In a cube block word with j principal factors and k=3(r+1)-j central
degrees, use the bidegree support majorant

    p1+p2+p3<=D=6j,       e1+e2+e3<=k.

The coordinate counts are the coefficients of
16^(3-j) P(u)^j (1+v)^k. All coefficients in each of the two degree
intervals are positive, including j=0, where D=0. This investigation
optimizes covers of this support majorant; it does not assert that every
one of its triples occurs in the actual tensor.

## Exactly the enumerated family

A staircase f maps {0,...,k} to {-1,...,D}. It covers a coordinate (p,e)
when p<=f(e). Require f to be nonincreasing. Use this same f on two legs;
allow an independent threshold g on the third. Permuting the tensor legs
does not change the minimum cost, since their multiplicities agree.

For fixed f the cheapest third threshold is

    g(c)=max({-1} union
        {D-2-f(a)-f(b): a+b+c<=k, f(a)<D, f(b)<D}).

Indeed if either f value is D, that leg covers every principal degree.
Otherwise the least uncovered degrees on the first two legs are
f(a)+1 and f(b)+1. A triple avoiding all three legs exists exactly when

    f(a)+f(b)+g(c)+3 <= D.

If g(c)=D the third leg covers everything; the displayed formula never
exceeds D because f(a),f(b)>=-1. Thus the formula is both necessary and
sufficient. All coordinate costs are positive, so choosing a larger
third threshold cannot lower cost. The resulting g is itself
nonincreasing, since the set in its maximum shrinks as c increases.

For one leg, the cost of a threshold h is

    sum_(e=0..k) 16^(3-j) binomial(k,e) sum_(p<=h(e)) [u^p] P(u)^j.

The total is twice the cost of f plus the cost of g. Enumerate every
nonincreasing f as a reversed multiset of k+1 elements from D+2 values.
There are binomial(D+k+2,k+1) such f. A candidate whose two first legs
already cost at least the current best can be skipped: every third-leg
cost is nonnegative. This pruning changes no minimum or enumerated count.
The whole-leg cover is in the family, with f=-1 and g=D everywhere.

## Completed census

| Central rank r | Principal factors j | First staircases | Minimum word cost |
|---:|---:|---:|---:|
| 1 | 0 | 8 | 147456 |
| 1 | 1 | 1716 | 397568 |
| 1 | 2 | 8568 | 997536 |
| 1 | 3 | 8855 | 2534774 |
| 2 | 0 | 11 | 909312 |
| 2 | 1 | 11440 | 2440192 |
| 2 | 2 | 203490 | 6165024 |
| 2 | 3 | 657800 | 15768612 |

All 891888 staircases are accounted for. Each minimum agrees with the
previous weighted cover. Consequently nonlinear thresholds in this
two-equal-leg monotone family give no smaller cube bound, and cannot
exclude the remaining M(13,14,14) target in the first source.

Three unequal legs, nonmonotone coordinate covers, finer source support,
different bases and other source powers are outside this census.
No asymptotic extrapolation or global slice-rank lower bound follows.

The finite reduction and enumeration are owner-directed Codex work.
The prior S5 source certificates and external finite target theorem
retain their attribution in the pinned cube package; no additional
external theorem is imported here. Independent mathematical review and
formalization remain absent.
