# Joint rank-locus profiles and the matrix-plus-scalars frontier

October 23, 2026. Written AI-derived arguments are unreviewed. The
candidate targets below are unconstructed; no exponent improvement is
established. Source records and inherited proof statuses are in SOURCES.json.

## A necessary profile inequality for joint targets

Let S be the complex trace tensor of a semisimple algebra with square
block degrees d_i and N=sum d_i^2. Write D_S(t) for the affine dimension
of its first-leg rank-at-most-t slice cone. The existing source calculation
in `2026-10-20-group-potentials/rank_locus_proof.md` gives

    D_S(t) = max sum_i k_i(2d_i-k_i),
             sum_i d_i*k_i <= t, 0 <= k_i <= d_i.

For a joint rectangular target U=direct_sum_j M(a_j,b_j,c_j), its
first-leg dimension L is sum_j a_j*b_j. Its corresponding profile is

    D_U(t) = max sum_j k_j(a_j+b_j-k_j),
             sum_j c_j*k_j <= t, 0 <= k_j <= min(a_j,b_j).

These dimension formulas use finite unions of products of determinantal
varieties. The slice rank as an ordinary matrix of a contracted matrix
product is c_j*rank(X_j), and ordinary block matrix ranks add.

A necessary condition for an arbitrary complex degeneration S -> U is

    D_U(t) >= D_S(t) + L - N                         (1)

for every nonnegative integer t, on each target leg. This extends the
existing empty-low-rank-locus test to the entire joint profile.

To prove (1), take any linear restriction and dualize its first-leg map
to F: C^L -> C^N. Put r=rank F and E=im F. Choose a source determinantal
component V of dimension D_S(t). Projective dimension intersection gives
an affine intersection dimension at least D_S(t)+r-N when that number is
positive; the zero vector is always present. Its preimage under F has
dimension at least L-r+max(0,D_S(t)+r-N), hence at least D_S(t)+L-N.
The other two restriction maps cannot raise matrix rank, so this
preimage lies in the restricted tensor's rank-at-most-t slice cone.

The lower bound on that cone's dimension persists in the limit. For a
positive required affine dimension m, projectivize the parameter cone;
its projective fibers have dimension at least m-1. The closed minors
incidence is projective over tensor space. Properness and upper
semicontinuity of fiber dimension make this condition closed. For m<=0
the inequality is automatic. Thus every degeneration satisfies (1).
This uses the same standard projective machinery as the adopted source
proof and claims no historical priority.

For M(a,b,c) plus r scalar tensors, the target profile specializes to

    D_U(t) = max_{0 <= k <= min(a,b), ck <= t}
             k(a+b-k) + min(r,t-ck).                 (2)

The scalar contribution is the dimension of a coordinate-support cone
of r scalar variables with at most t-ck nonzero entries. Finite unions
of its coordinate subspaces have dimension min(r,t-ck).

## Finite slice rank of the joint target

Over every field, SR(M(a,b,c)) = min(ab,bc,ca). For a<=b<=c, annihilate
the p first-leg forms of an alleged p+q+s<ab slice decomposition. The
resulting subspace of a-by-b matrices has dimension at least ab-p, while
every matrix X in it satisfies c*rank(X)<=q+s. The arbitrary-field
Flanders/Meshulam dimension bound, in de Seguins Pazzis
arXiv:1507.05375v2 Theorem 1.1, gives dimension at most
b*floor((q+s)/c)<=q+s, a contradiction. The matching upper bound expands
along a smallest leg. This is the rectangular version of the preceding
finite square-target argument; the imported matrix-space theorem is
external work.

Gowers, arXiv:2105.08394v2 Theorem 2, proves slice-rank additivity for
direct sums over an arbitrary field. Consequently

    SR(M(a,b,c) direct_sum r M1) = min(ab,bc,ca)+r.    (3)

The exact characteristic-two SL(2,F5) certificate gives source slice
rank at most 98. The same closedness and coefficient-one good-reduction
transfer as in the adopted nonsplit proof therefore requires

    min(ab,bc,ca)+r <= 98.                           (4)

Equation (4) is not asserted for arbitrary complex degenerations without
that good reduction. Equations (1) and the complex Koszul screens below
apply under their wider complex hypotheses.

## Full-space joint Koszul ranks

Adopt the maintained matrix Koszul rank formula and its padding convention
from `2026-10-21-semisimple-koszul/proof.md`, retaining its written,
unreviewed status and external Landsberg--Ottaviani credits. In ambient
first-leg dimension N, write F_(a,b,N)(p) for its padded basic rank. A
scalar tensor contributes binomial(N-1,p). The other two tensor legs of
a direct sum split into independent matrix blocks, so

    rank K_p(M(a,b,c) direct_sum r M1)
      = c F_(a,b,N)(p) + r binomial(N-1,p).          (5)

This is additivity of ordinary ranks of a block matrix, not an assumption
about tensor rank or border rank. The source rank is the adopted exact
sum over d_i. Hence every p and tensor-leg ordering supplies an integer
upper bound on r by division with remainder. Exterior duality reduces
the checks to 0<=p<=floor(N/2) with all leg permutations. Tests also build
small joint Koszul matrices directly, independently checking (5).

## A separately verified cube of the actual nonsplit source

Use the full nonsplit F4 basis checked against the actual SL(2,F5) group
trace, not the quotient or a split degeneration. Its principal block P
has dimension 88 and degree polynomial

    P(t)=9+8t+10t^2+8t^3+18t^4+8t^5+10t^6+8t^7+9t^8.

Every principal term has total degree at most eight. The other block B
has degree polynomial 16(1+t) and source total degree at most one. The
adopted dense verifier checks all 1728000 original coefficients, both
bounds and the absence of cross-block terms. These are exact finite
acceptance premises, with their original provenance retained.

Expand the source cube into its eight P/B block words. In a word with j
principal positions, weight the B degree by h and leave P's degree
unchanged. Its one-leg polynomial is P(t)^j [16(1+t^h)]^(3-j), and each
source term has total degree at most D=8j+h(3-j). Coordinates of degree
at most cutoffs (u,v,w) cover every term when u+v+w=D-2: avoiding all
three sets would require degree at least D+1.

| j | Words | h | D | Cutoffs | Slices per word |
| ---: | ---: | ---: | ---: | --- | ---: |
| 0 | 1 | 1 | 3 | 0,0,1 | 24576 |
| 1 | 3 | 2 | 12 | 3,3,4 | 65024 |
| 2 | 3 | 3 | 19 | 5,6,6 | 147680 |
| 3 | 1 | 0 (unused) | 24 | 7,7,8 | 349644 |

Adding these decompositions gives

    SR_F4(T_SL2F5^tensor(3)) <= 1012332.              (6)

The producer multiplies integer histograms. A separate verifier instead
counts all 11^3=1331 ordered triples of one-leg classes, with total
coordinate multiplicity 120^3=1728000. It checks each of the eight block
words, every claimed degree distribution and cutoff coverage. The full
source certificate is replayed first. No numerical optimizer bound is
used. No asymptotic source cost is inferred from this finite power.

For U=M(a,b,c) direct_sum r M1, tensor U with its two cyclic rotations.
The eight direct-sum choices consist of one all-matrix tensor M(V,V,V),
three types with two matrix factors and r scalar choices, three types
with one matrix factor and r^2 scalar choices, and r^3 scalar tensors,
where V=abc. Finite rectangular slice rank and Gowers's direct-sum
additivity therefore give the exact value

    C(a,b,c,r) = V^2 + 3r V min(a,b,c)
                    + 3r^2 min(ab,bc,ca) + r^3.     (7)

For example, two cyclic matrix factors multiply to M(ab,bc,ca), whose
smallest face is V min(a,b,c). Direct expansion tests independently check
this count. The cyclic group trace supplies the three source copies.
Thus any characteristic-two degeneration to U requires C(a,b,c,r)
<=1012332, by slice-rank closedness and monotonicity. The same inequality
holds for the maintained complex coordinate/potential constructions by
the stated good reduction. It is not an arbitrary-complex obstruction.

For M(9,9,11), r=8 gives C=1002401 and r=9 already gives C=1030806.
The polynomial is strictly increasing in nonnegative r. Therefore this
source cube permits at most eight scalar outputs beside that matrix in
the stated class, improving the earlier Koszul cap of thirteen.

## Complete stated family and exact numerical gates

For SL(2,F5), the certified complex degrees are
1,2,2,3,3,4,4,5,6 and N=120. Sort 1<=a<=b<=c. Ordinary dimensions require
bc+r<=120, so 1<=b<=floor(sqrt(120)), b<=c<=floor(120/b), 1<=a<=b,
and 0<=r<=120-bc cover the complete family, including sides equal to one.
There are 866 shapes and 41132 such dimension-compatible family members.

First apply the existing single-matrix rank-locus obstruction, which any
joint target must satisfy after projecting away its scalars. Next apply
(4), all bounds (5), and the exact strict cost comparison at exponent
9/4. Apply (1) at all 121 source rank budgets and all distinct leg
orderings for every improving survivor. Before using the joint cube,
the only surviving formats are

    M(9,9,11) direct_sum r M1, r = 11, 12, 13.        (8)

They have leg dimensions (81+r,99+r,99+r) and finite slice rank 81+r.
The sharpest scalar cap from the maintained Koszul tests is r<=13; the
saved report identifies the ordering and power 57 witness. All three
survivors satisfy the full profile (1). The report stores exact source
and target ranks and rational interval comparisons. The joint cube
then excludes all three: its target ranks are 1089242, 1119285 and
1149886, exceeding 1012332 by 76910, 106953 and 137554. Hence no member
of this matrix-plus-scalars family improves the 9/4 cost comparison in
the one-copy complex coefficient-one coordinate/potential class. This
is not an exclusion of arbitrary complex mixing, arbitrary joint
matrix sums or higher source powers.

Schönhage's externally credited asymptotic sum inequality and the usual
border-to-asymptotic conversion give the conditional necessary comparison

    891^(omega/3) + r <= sum_i d_i^omega.            (9)

The same conversion is already used by the maintained group-target
criterion; no new source-cost theorem is assumed. Exact integer-root
intervals show the reverse strict inequality at

| r | Conditional upper bound if the target is constructed |
| ---: | ---: |
| 11 | 1121/500 = 2.242 |
| 12 | 2233/1000 = 2.233 |
| 13 | 2223/1000 = 2.223 |

To justify inference from a strict comparison at x to omega<x, let
H(x)=(sum d_i^x)/(891^(x/3)+r). For x>=2 the logarithmic derivative of
the numerator is at most log 6. Since 891>9^3, the logarithmic derivative
of its denominator is greater than 81 log 9/(81+r), and for r<=13 this
is at least 81 log 9/94 > log 6. The last inequality is exactly the
integer comparison 9^81>6^94. Thus H is strictly decreasing on x>=2.
Together with the ordinary omega>=2 lower bound, (9) and the saved
strict comparisons prove these conditional implications.

The three conditional comparisons remain valid for a hypothetical
general complex degeneration, where good reduction is not presumed.
Their premises are excluded in the maintained one-copy coordinate/
potential class by (7), and remain unconstructed outside that class.
The exponent remains at the external 9/4 bound. No construction,
independent mathematical review or formalization is claimed.
