# Exact finite frontier for ordinary square direct sums

October 21, 2026. Written reduction and exact finite enumeration. No
independent mathematical review, formalization, target construction, or
smaller exponent is claimed.

## Result

Within every cyclic source A(a,b) with 2<=a<=b and common leg dimension
N=ab(a+b-1)<300, no ordinary restriction to a direct sum of square
matrix multiplication tensors can pass this package's finite 9/4 score
test. The enumeration covers all such integer sources and all square
partitions of their available target leg dimensions.

For A(5,5), N=225. Even after relaxing the restriction question to the
necessary conditions below, every target has certified score at most

\[
\sum_j(6n_j)^{9/4}
\le\frac{21685692380}{10^6}
=21685.692380<21952=28^3.                              \tag{1}
\]

The relaxed maximum occurs at the partition (14,2,1), with target leg
dimension 201. This is a maximizer of necessary conditions only; no
restriction to that partition is constructed.

At the next source A(5,6), N=300, the necessary conditions permit

\[
A(5,6)\ \unrhd\ M_{16}\oplus M_4,                    \tag{2}
\]

with total leg dimension 272. The maps in (2) are missing. If constructed,
they would imply omega<281/125=2.248 through the existing character
comparison. This number is conditional, not an attained exponent.

The negative result concerns ordinary restrictions and the stated square
direct-sum score. It does not exclude singular degenerations from the
smaller full sources, rectangular direct sums, tensor powers, alternative
source inequalities, or other tensors.

## Necessary conditions used in the enumeration

Fix a source and a target leg dimension D<=N. Put k=N-D. Let n be the
size of one square matrix block. The minimum slice rank of the source
is ab, so a rank-one parameter of that block requires

\[
n+2k\ge ab.                                          \tag{3}
\]

The [polynomial rank-locus theorem](polynomial_rank_locus.md) classifies
every source slice of rank below2ab. Its three-leg factorization gives,
for every selected target subsum of common leg dimension B>=2,

\[
B+2k\ge2ab.                                         \tag{4}
\]

We use (4) for every nonscalar block B=n^2 and for any pair of scalar
blocks B=2. Thus nonscalar blocks satisfy n^2+2k>=2ab, and repeated
scalars are allowed only when2+2k>=2ab. One scalar by itself is not
excluded by this particular condition.

The same theorem applied to the connected rulings of the rank-one
parameter variety gives the stronger condition for every nonscalar block:

\[
n\ge2\quad\Longrightarrow\quad n+2k\ge2ab.           \tag{5}
\]

Indeed, if the reverse strict inequality holds, every lifted rank-one
parameter belongs to the low-rank locus. Connected Segre rulings force a
single coherent factor on its entire block span on each leg. The source
then restricts to a rank-one tensor, contradicting the nonscalar matrix
block. This argument does not require n^2>ab. Condition (5) subsumes
(3) and the individual-block instances of (4) when n>=2. The scalar
conditions remain separate. These necessary tests may leave extra
impossible partitions, which is harmless for the upper bound.

## Exact arithmetic and exhaustive recurrence

Use a common denominator Q=10^6. For each block size n, compute integers
L_n,U_n with

\[
L_n^4\le Q^4(6n)^9<U_n^4,
\qquad U_n=L_n+1,
\]

unless the radicand is a perfect fourth power, in which case the interval
is exact with U_n=L_n. Thus (6n)^(9/4)<=U_n/Q. Both integer roots are
computed by two applications of integer square root, with the defining
inequalities explicitly checked. No floating-point sign decides an
acceptance comparison.

At each fixed D, let L be the block sizes allowed by (3)--(5). Starting
from F(0)=0 and unreachable negative values at other positions, use

\[
F(d)=\max_{n\in L,\ n^2\le d}\bigl(F(d-n^2)+U_n\bigr).
\]

Every square partition of d has a last block, so induction on d proves
that this recurrence covers every partition, including all repetitions.
When one scalar is allowed but two are not, run the recurrence without
scalars and compare F(D) with F(D-1)+U_1. This enforces the exact scalar
multiplicity condition. Unreachable dimensions are recorded explicitly.

The report contains23 source records up to N=300, the complete225-row
dimension frontier for A(5,5), and the first passing source. All22
smaller source formats have a maximum upper bound strictly below their
respective threshold [3(a+b)-2]^3. The exact denominator and maximizing
relaxed partition are included in each record.

## Conditional surviving target

For (2), both target orientations are square direct sums. The existing
two-orientation character argument gives the necessary inequality

\[
96^{\omega}+24^{\omega}\le31^3
\]

in the detecting-character implication described in the package README.
More precisely, a strict violation at an exponent c rules out detecting
characters with total dot-product parameter at least c. At c=281/125,
the following integer checks provide that strict violation:

\[
96^{281}>28585^{125},\qquad
24^{281}>1266^{125},\qquad
28585+1266=29851>29791=31^3.
\]

The corresponding scalar equation has a numerical root near 2.24754365.
That estimate is not the certificate. The integer comparisons prove the
conditional bound2.248, and no maps establishing its premise are given.

The earlier proposed partition (16,3,3), with D=274, is excluded by
the strengthened condition (5): 3+2(300-274)=55<60. The surviving
partition (16,4) meets that condition at equality for its smaller block:
4+2(300-272)=60. Neither statement supplies the missing maps.

## Reproduction

```
python research/ai/2026-10-20-anisotropic-constructions/square_sum_frontier.py --output results/anisotropic-constructions-2026-10-20/square-sum-frontier.json
python -m unittest discover -s tests -p test_square_sum_frontier.py -v
```

Tests also compare the dynamic program with separate recursive partition
enumeration on small source formats. The geometric exclusions depend on
the written rank-locus theorem, not on these finite implementation checks.

The root agent derived the finite partition reduction and implementation
after the anisotropic worker's stronger slice classification. All work
belongs to this generating session; no external review is implied.
