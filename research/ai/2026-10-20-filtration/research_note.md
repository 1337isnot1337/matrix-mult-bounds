# All-size compatibility of the fixed-label determinant filtrations

Date: 2026-10-20. AI-derived research by this Codex session, directed by the
repository owner. Base: `e0d7ed5`. Written proof; no independent review or Lean
formalization. No smaller matrix multiplication exponent is established.

## Question and dependencies

R2 asks whether the three families (11)--(12) in the immutable
[first-pass note](../2026-10-20/research_note.md) exclude its matching profile
at some untested size. The answer is **no, at every positive integer size**.
The proof below uses only elementary discrete concavity. Its tensor-theoretic
interpretation is conditional on the first-pass construction; the scalar
inequalities themselves are proved without a tensor premise.

The determinant filtration and shared-leg argument are external constructions
from OpenAI's *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
October 2, 2026, Sections 3--4, repository commit
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
The general product-filtration family and the matching profile were already
recorded in the local first pass. This note supplies an all-size compatibility
proof, not a new derivation of OpenAI's exponent or recurrence.

## 1. A general scalar theorem

Let F be a positive function on positive integer pairs with these properties:

1. F is symmetric, nondecreasing, and discretely concave in each argument.
2. F(1,b)=b.
3. F(a,2) <= 2 F(a,1) for every a.

For any a,b,c,d >= 1 put

    A_i = a+c-1-2i,  0 <= i < min(a,c),
    B_j = b+d-1-2j,  0 <= j < min(b,d).

Then each of the following is at most F(a,b)F(c,d):

    sum_j F(A_i,B_j)                 (each fixed i),
    sum_i F(A_i,B_j)                 (each fixed j),
    sum_{i+j=k} F(A_i,B_j)           (each fixed k).

### Two elementary consequences of concavity

For a fixed first argument, write f(n)=F(a,n). Its increments are
nonincreasing. The third hypothesis gives f(2)-f(1) <= f(1). Therefore

    n (f(n+1)-f(n))
       <= (f(2)-f(1)) + sum_{r=1}^{n-1}(f(r+1)-f(r))
       <= f(n).

The first inequality compares each of n summands with the last increment;
for n=1 it is equality. Thus f(n)/n is nonincreasing. In particular,

    (b/d) F(a,d) <= F(a,b) whenever b <= d.                 (1)

For fixed d, concavity also gives

    F(a+c-1,d) <= F(a,d)+F(c,d)-d
               <= F(a,d)F(c,d)/d.                         (2)

The first inequality compares c-1 increments starting at a with those
starting at 1. For the second, use F(a,d),F(c,d) >= F(1,d)=d and expand
(F(a,d)-d)(F(c,d)-d) >= 0.

### The row bound

Exchange the two source pairs if necessary so that b <= d. The b arguments
B_j have arithmetic mean d. Jensen's inequality for the piecewise-linear
concave extension of F(A_0,.) gives

    sum_j F(A_0,B_j) <= b F(A_0,d)
       <= (b/d) F(a,d)F(c,d)
       <= F(a,b)F(c,d),                                   (3)

using (2) and then (1). All arguments B_j are positive integers. This
Jensen step also follows by pairing equal distances from d and summing
discrete concavity. Since A_i <= A_0, monotonicity proves every row bound.
Symmetry, with (a,b,c,d) replaced by (b,a,d,c), proves the column bounds.

Finally each fixed-k sum is dominated term by term by a subset of the top
row: F(A_i,B_{k-i}) <= F(A_0,B_{k-i}). Each j=k-i occurs only once.
Positivity allows adding the missing top-row terms. This proves the theorem.

## 2. Application to the matching profile

Use exactly the first-pass profile

    h_1=1, h_{m+1}/h_m=(3m+1)/(3m),
    P_*(a,b)=h_min(a,b) (max(a,b)+(min(a,b)-1)/2).

Symmetry, normalization and separate concavity were proved in the first pass.
Monotonicity follows either from its positive affine tails and decreasing
increments, or from positivity and concavity: a negative increment would
force eventually negative values. The remaining hypothesis holds because

    P_*(1,2)=2,
    P_*(a,2)=(4a+2)/3 <= 2a=2P_*(a,1) for a>=2.

Consequently every fixed-label inequality (11)--(12), including fixed output
labels, preserves P_* at t=3/4 for **all** a,b,c,d. The 353,664 archived checks
are now examples of a general theorem rather than the extent of the result.

The same conclusion holds for any finite derivation built solely by
substituting these numerical inequalities and the previously verified scalar
constraints: P_* remains a feasible scalar model. This statement does not
extend the model to an actual tensor character or to arbitrary tensor
isomorphisms and decompositions.

## 3. What this leaves open

The proof exploits fixing one label. It does not bound extracting sectors
that are independent on all three legs. Their direct-sum score at t=3/4 is
the 4/3 power of a sum of 3/4 powers, rather than the plain sum in (3).
Retaining multiple labels and using full direct sums, oriented character
information, or additional basis changes are different research questions.

This closes R2 for the displayed family. It gives no lower bound on omega
and no improvement of the external upper bound 9/4.

## Reproduction

Run `python research/ai/2026-10-20-filtration/verify_filtration.py` from the
repository root. Its exact rational certificates check each step of (3),
top-row/top-column domination, and the displayed profile hypotheses on a
finite regression domain. The written argument proves the universal claim;
finite certificates do not replace it. The verifier uses only the standard
library and never writes into the first-pass archive.
