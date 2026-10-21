# Exact finite frontier for ordinary square direct sums

October 21, 2026. Written reduction and exact finite enumeration. No
external independent review, formalization, target construction, or
smaller exponent is claimed.

## Result

Within every cyclic source A(a,b) with 2<=a<=b and common leg dimension
N=ab(a+b-1)<960, no ordinary restriction to a direct sum of square
matrix multiplication tensors can pass this package's finite 9/4 score
test. The enumeration covers all 60 such integer source formats and
all square partitions of their available target leg dimensions.

The necessary conditions give the following exact upper bounds. They
are maxima of a relaxation; the listed partitions are not constructions.

| Source | Source leg dimension | Relaxed maximizing partition | Target leg dimension | Certified score upper bound | Critical threshold |
| --- | ---: | --- | ---: | ---: | ---: |
| A(5,5) | 225 | (13,3,1,1,1) | 181 | 18916.994428 | 21952 |
| A(5,6) | 300 | (15,4,2,1,1) | 247 | 26604.167197 | 29791 |
| A(7,8) | 784 | (25,1,1,1) | 628 | 78910.828146 | 79507 |
| A(7,9) | 945 | (27,6,2) | 769 | 97071.207486 | 97336 |
| A(8,8) | 960 | (27,7,1,1,1) | 781 | 98288.351249 | 97336 |

Each score is the sum of (6n)^(9/4) over the square block sizes n.
The displayed upper bounds have exact denominator 10^6. For example,

\[
\sum_j(6n_j)^{9/4}
\le\frac{18916994428}{10^6}
<21952=28^3
\]

for every ordinary square direct-sum target of A(5,5).

The first surviving source format is A(8,8). A simpler two-block target
that passes these necessary tests is

\[
A(8,8)\longrightarrow M_{27}\oplus M_7,             \tag{1}
\]

with total leg dimension 778. The maps in (1) are missing. If constructed,
they would imply omega<4497/2000=2.2485 through the existing character
comparison. This number is conditional, not an attained exponent.

The negative result concerns ordinary restrictions and the stated square
direct-sum score. It does not exclude singular degenerations from these
full sources, rectangular direct sums, tensor powers, alternative source
inequalities, or other tensors.

## Necessary conditions used in the enumeration

Fix a source and a target leg dimension D<=N. Put k=N-D. A rank-one
matrix parameter of a block of size n has target slice rank n. Lifting
it through ordinary maps can increase the slice rank by at most 2k.
The minimum source slice rank is ab. Thus a scalar block requires

\[
1+2k\ge ab.                                        \tag{2}
\]

The [polynomial rank-locus theorem](polynomial_rank_locus.md) classifies
all source slices below 2ab. Connected Segre rulings and three-leg
factorization give, for every nonscalar block,

\[
n\ge2\quad\Longrightarrow\quad n+2k\ge2ab.           \tag{3}
\]

Two scalar summands together have a two-dimensional common leg space
and tensor rank two. The corresponding whole-subspace argument gives

\[
\text{at least two scalars}\quad\Longrightarrow\quad2+2k\ge2ab.
                                                               \tag{4}
\]

The [general Hankel symbol dimension bound](hankel_symbol_dimension.md)
adds, for every integer r in its stated range,

\[
1\le r<\min(a,b),\quad3r\le a+b-1,\quad n^2>rab
\quad\Longrightarrow\quad n+2k\ge(r+1)ab.             \tag{5}
\]

Its proof applies the symbol map over C(x,z). Bounded Hankel rank on
rank-one matrix parameters forces a common symbol space of dimension
at most r. Selecting r long coordinates then injects the entire lifted
block into r copies of the ab-dimensional polynomial coefficient space.
The supporting scheme may depend on x,z; constancy is not assumed.

The separately proved
[first-boundary theorem](hankel_boundary_dimension.md) adds exactly
the next sequence length, with a different dimension cap when r<4:

\[
2\le r<\min(a,b),\quad a+b-1=3r-1,\quad n^2>\max(r,4)ab
\quad\Longrightarrow\quad n+2k\ge(r+1)ab.             \tag{6}
\]

Its proof classifies moving linear spaces at this boundary using a
Chinese remainder argument and the unique relation among 3r jets.
It does not justify any extension to a+b-1<3r-1.

There is also a narrow equality refinement. The
[rank-two equality theorem](parity_structure_equality.md) and
[three-leg argument](hankel_rank_two.md) show that, when a,b>=3 and
a+b-1>=6, an n>=3 block must satisfy

\[
n+2k>2ab.                                          \tag{7}
\]

At equality, the lifted rank-one parameters have constant length-two
long supports. Their connected rulings fix these supports on the block
spaces. The three-leg contraction then factors through at most eight
coordinates on each leg, contradicting the target flattening rank n^2>8.
For n=2 this last contradiction is unavailable, so the code retains
those equality cases.

These are necessary conditions. A partition that passes them may still
be impossible. That relaxation is harmless for an upper bound on the
best score of an actual restriction.

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

At each fixed D, let L be the block sizes allowed by (2)--(7). Starting
from F(0)=0 and marking other positions unreachable, use

\[
F(d)=\max_{n\in L,\ n^2\le d}\bigl(F(d-n^2)+U_n\bigr).
\]

Every square partition of d has a last block, so induction proves that
this recurrence covers every partition, including repetitions. When one
scalar is allowed but two are not, run the recurrence without scalars
and compare F(D) with F(D-1)+U_1. This enforces the exact multiplicity
condition. Unreachable dimensions are recorded explicitly.

The report contains 62 source records through N=960, the complete
225-row dimension frontier for A(5,5), and the first passing source.
All 60 smaller source formats have maximum upper bounds strictly below
[3(a+b)-2]^3. Each record includes the exact score denominator, permitted
Hankel rank levels, the separate first-boundary cap when applicable,
and a maximizing relaxed partition. The other format at N=960,
A(5,12), also remains below its critical score threshold.

## Conditional surviving target

For (1), the existing two-orientation character argument gives the
necessary comparison

\[
162^{\omega}+42^{\omega}\le46^3
\]

in the detecting-character implication described in the package README.
More precisely, a strict violation at an exponent c excludes detecting
characters with total dot-product parameter at least c. At c=4497/2000,
the following integer checks give the strict violation:

\[
162^{4497}>92916^{2000},\qquad
42^{4497}>4465^{2000},\qquad
92916+4465=97381>97336=46^3.
\]

The scalar equation has a numerical root near 2.248405133592566.
That estimate is not the certificate. The integer comparisons prove the
conditional bound 2.2485; no maps establishing its premise are given.

## Change from the preceding checkpoint

The preceding checkpoint left A(7,8) to M25 plus M5 as an ordinary
candidate with a conditional exponent below 2.247. Equation (6), with
r=5, closes that target: 25+2(784-650)=293<336, while 625>5*56.
The full partition screen also closes every square direct sum from
A(7,8), by the exact maximum 78910.828146<79507 above.

An older checkpoint used only the strict low-rank classification and
left A(5,6) to M16 plus M4 as a candidate. Equation (5), with r=3,
excludes even a single ordinary M16 block from that source:

\[
16+2(300-256)=104<120,\qquad16^2>3\cdot30.
\]

Adding other blocks decreases the loss and cannot repair the violation.
The earlier conditional number 2.248 is therefore not a live ordinary
construction target. A singular degeneration remains outside this proof.
The earlier M16 plus two M3 target was already excluded by (3).

## Reproduction and limits

```
python research/ai/2026-10-20-anisotropic-constructions/square_sum_frontier.py --output results/anisotropic-constructions-2026-10-20/square-sum-frontier.json
python -m unittest discover -s tests -p test_square_sum_frontier.py -v
```

Tests compare the dynamic program with separate recursive partition
enumeration on small source formats, including A(3,4), where the general
r=2 filter applies. The geometric exclusions depend on the written
proofs, not on these finite implementation checks.

The root agent derived the finite partition reduction and implementation,
with the general symbol dimension argument developed and checked by
coordinated agents in this session. No external review is implied.
