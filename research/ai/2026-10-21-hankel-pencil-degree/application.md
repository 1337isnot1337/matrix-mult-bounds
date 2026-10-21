# Consequences for the ordinary cyclic-source frontier

October 21, 2026. These are applications of the written, unreviewed
[Hankel Segre-image theorem](proof.md), not constructions or exponent gains.

## Source-to-symbol injection

For A(a,b), put N=ab(a+b-1). Adopt the existing polynomial slice inequality

    rank M_F >= ab rank_(C(x,z)) H_F,

with its original credit in `polynomial_rank_locus.md`. The symbol H_F is
the a-by-b Hankel matrix of the a+b-1 long-coordinate biforms of F. Each
biform belongs to an ab-dimensional polynomial space.

Suppose an ordinary restriction has a rectangular block M(l,h,n), with
first parameter space Mat_(l,h), and target B,C leg dimensions D_B,D_C.
For a rank-one parameter its lifted source slice has rank at most

    R=n+(N-D_B)+(N-D_C).

If R<(r+1)ab, its Hankel symbol has rank at most r. Those identities hold
for every complex rank-one parameter; their polynomial coefficients in
x,z and the rank-one variables vanish identically. They therefore remain
valid for arbitrary rank-one parameters over an algebraic closure of
C(x,z). The new theorem bounds the symbol-image dimension there by B.

Choose B long coordinates that inject this image over C(x,z), using fewer
if its dimension is smaller. They also inject the constant-coefficient
lifted block into B copies of the ab-dimensional biform space. Conciseness
of the target makes its source first-leg map injective, so

    l*h <= B*ab.                                             (1)

Thus an ordinary block with l*h>B*ab needs R>=(r+1)ab. The strictness in
both the pencil hypothesis 5r<2(a+b) and the source-rank antecedent is
retained in the code. The argument requires ordinary maps and does not
apply this rank-lift estimate through singular changes of basis.

## Balanced single rectangular targets

The existing complete enumeration considers a=2,...,12, sorted l<=h<=n,
h*n<=a^2(2a-1), and the exact improving-score condition

    216*l*h*n > (6a-2)^4.

It contains5139 formats. The prior polynomial and Hankel gates exclude4192.
The new theorem excludes453 more, with a full witness for each:

| a | Prior survivors | Additional exclusions | Remaining necessary-test survivors |
| --- | ---: | ---: | ---: |
| 8 | 1 | 1 | 0 |
| 9 | 11 | 11 | 0 |
| 10 | 123 | 70 | 53 |
| 11 | 269 | 140 | 129 |
| 12 | 543 | 231 | 312 |

All improving ordinary single rectangular formats through a9 are therefore
excluded by the accumulated written proofs. Exactly494 survive through a12,
first at a10. None of these surviving necessary-test formats is constructed.
The result does not cover general rectangular direct sums or unbalanced
source formats in this finite rectangular enumeration.

For the former A8 candidate M(27,28,28), choose the756-dimensional first
parameter space. Then R=408<448=7*64, while756>9*64=576. Equation(1)
excludes its ordinary maps. Its previously recorded conditional exponent
191/85 remains an implication with an unproved singular-degeneration
premise; the ordinary premise is now excluded by this written theorem.
The old report and its integer certificate are preserved unchanged.

## Square direct sums

For a direct sum of square blocks with common target leg dimension D,
a block M_n has R=n+2(N-D), first parameter dimension n^2. Add(1) to the
existing exact allowed-block filter and retain its integer dynamic program
and certified fourth-root score intervals unchanged.

For A8, the maximum relaxed score has exact upper bound

    95171566351/10^6 < 97336=46^3,

at the relaxed partition(27,4,2), of target leg dimension749. All960 target
leg dimensions and every square partition are covered by the recurrence.
This excludes every ordinary A8 square direct sum that would improve the
stated9/4 cyclic-source score. In particular the earlier M27 plus M7
candidate fails: D=778, R=391<448, and27^2=729>576.

For A9 the screen still has a necessary-test survivor. Its relaxed maximum
is(32,6,3), with D=1069 and score upper bound141065173366/10^6, above the
critical140608=52^3. The saved partition also has exact lower score numerator141065173363
over10^6, above the critical score. It passes this score comparison but
is unconstructed and remains unresolved by the necessary conditions. The M32 block has R=648 exactly, so the strict
r=7 antecedent R<8*81 does not apply. No equality exclusion is assumed.

The earlier all-source square screen through N=960 remains valid and is
strengthened at its one surviving source A8. The present calculation does
not enumerate all unbalanced sources between960 and the A9 dimension1377.

## Reproduction and evidence status

`verify.py` checks96760 splitting cases for the declared finite range
r=2,...,20, together with exact global-identity controls. No acceptance
uses an empirical threshold. The general
mathematical result rests on the written proof, including its external
lemmas. The tests also independently solve polynomial kernel and assignment
coefficient systems and test the strict boundary conditions.

`application.py` reuses the credited earlier candidate enumeration and
square-score recurrence from separately loaded modules. Their source
files and historical reports remain unchanged. The new reports retain
all formats, every square dimension, and exact accepted inequalities.
No independent mathematical review, formalization, target construction,
or exponent below9/4 is claimed.
