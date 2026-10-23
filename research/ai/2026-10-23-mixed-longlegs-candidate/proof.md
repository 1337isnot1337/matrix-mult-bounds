# A frozen mixed-orientation candidate and its completed screens

Date: 2026-10-23. Owner-directed AI research. Exact finite experiments
and written deductions, with same-session cross-agent audits; no
external independent mathematical review.

Every ordinary Koszul degree on all three legs passes for the frozen
canonical endpoints. The separate [global RNC proof](global_rnc_obstruction.md)
now excludes the proposed degeneration, including singular leading first
maps and independent target first identifications. Earlier rank reports
remain preserved as checkpoints. The geometric obstruction uses a smooth
curve limit, source symmetry and the catalecticant comparison120<130.

## 1. Literal endpoints

Work over C. The common first space A has basis x_0,...,x_4.
Every displayed block has separate B and C coordinate intervals.

\[
\mathrm{Full}_{5,b}=\sum_{i=0}^4\sum_{j=0}^{b-1}
 x_i\otimes y_j\otimes z_{i+j}
\quad\text{has dimensions }(5,b,b+4).
\tag{1}
\]

\[
\mathrm{Mid}_{5,b}=\sum_{i=0}^4\sum_{k=0}^{b-1}
 x_i\otimes y_{i+k}\otimes z_k
\quad\text{has dimensions }(5,b+4,b).
\tag{2}
\]

For d+e=6, write

\[
O_{d,e}=\sum_{j=0}^{d-1}\sum_{k=0}^{e-1}
 x_{j+k}\otimes y_j\otimes z_k.
\tag{3}
\]

This is polynomial multiplication of input lengths d,e with its output
used as the shared first space. Define

\[
S=10\,\mathrm{Full}_{5,10},\qquad
T=7\,\mathrm{Full}_{5,2}+10\,\mathrm{Full}_{5,3}
 +4\,O_{3,3}+2\,O_{4,2}+6\,\mathrm{Mid}_{5,2}.
\tag{4}
\]

The source format is (5,100,140). The target's B dimension is
7*2+10*3+4*3+2*4+6*6=100, and its C dimension is
7*6+10*7+4*3+2*2+6*2=140. Concatenating the block intervals gives
literal tensors in the same three spaces.

The source has tensor rank and border rank exactly 140: its C
flattening has rank 140, and ten length-14 polynomial interpolation
decompositions give the matching rank upper bound. Summing the target
blocks' rank bounds gives 178. The separate [cactus-rank proof](cactus_rank.md)
now proves that ordinary, smoothable and cactus rank all equal178 for
the canonical target. Its low-rank-curve argument supplies the lower
bound directly; no rank-additivity assertion is assumed. Border rank
remains a separate question.

## 2. A strictly larger formal score

Use the symmetric specialization of the AVZ26 formal operational
potential, as attributed and developed in the preceding
[common-input package](../2026-10-23-common-input-rank-barrier/proof.md):

\[
G(a,b)=
 \left(\frac{3\min(a,b)-1}{2}\right)^{1/3}
 \left(\max(a,b)+\frac{\min(a,b)-1}{2}\right).
\tag{5}
\]

Each block is scored using its two polynomial input lengths, and block
scores are added. Thus

\[
G(S)=120\sqrt[3]7,\qquad
G(T)=76\sqrt[3]4+\frac{161}{2}\sqrt[3]{5/2}.
\tag{6}
\]

Multiplication by the positive number 2^(4/3) changes (6) to

\[
240\sqrt[3]{14}
\quad\text{and}\quad 304+161\sqrt[3]5.
\]

The following entirely rational inequalities certify strict increase:

\[
5-(29/17)^3=\frac{176}{4913}>0,
\]

\[
304+161(29/17)=\frac{9837}{17},
\]

\[
(9837/17)^3-240^3\,14
 =\frac{1050371253}{4913}>0.
\tag{7}
\]

The approximate ratio 1.00150749 is discovery context. Acceptance uses
only (7). The formal score in (5) is not asserted to be a character on
all tensors. Neither score improvement nor any of the screens below
establishes an improved exponent.

## 3. Shared-A Koszul ranks and ordinary slices

For

\[
K_{A,p}:B^*\otimes\Lambda^p A\longrightarrow
 C\otimes\Lambda^{p+1}A,
\]

the shared-A partial sum makes the map block diagonal. The verifier
builds all thirty literal block matrices, for six block types and all
p=0,...,4, and performs exact rational elimination.

| Block | p=0 | p=1 | p=2 | p=3 | p=4 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Full(5,10) | 10 | 44 | 72 | 52 | 14 |
| Full(5,2) | 2 | 10 | 20 | 20 | 6 |
| Full(5,3) | 3 | 15 | 30 | 24 | 7 |
| O(3,3) | 3 | 15 | 30 | 15 | 3 |
| O(4,2) | 4 | 20 | 20 | 10 | 2 |
| Mid(5,2) | 6 | 20 | 20 | 10 | 2 |

After applying the multiplicities in (4), both profiles are exactly

\[
(100,440,720,520,140).
\tag{8}
\]

The source entries also equal 10*(10+p)*binom(4,p).
The first covector with coefficients (1,2,3,5,7) attains each block's
maximum possible B-by-C matrix rank. Therefore generic first slices
have rank 100 for S and 72 for T, and this necessary comparison passes.

## 4. Degree-one Koszul maps on both long legs

Use

\[
K_{B,1}:C^*\otimes B\longrightarrow A\otimes\Lambda^2B,
\qquad
K_{C,1}:B^*\otimes C\longrightarrow A\otimes\Lambda^2C.
\]

Decompose the exterior square into its individual-block and unordered
two-block components, exactly as in the preceding
[shared-output obstruction](../2026-10-23-shared-output-koszul/proof.md),
Sections 2--3. The resulting ranks are:

| Leg | Source rank | Target rank | Source minus target |
| --- | ---: | ---: | ---: |
| B | 12735 | 12587 | 148 |
| C | 14000 | 13572 | 428 |

Both endpoints use the full ambient B and C dimensions. No padding term
is being omitted in this comparison.

The verifier constructs all forty-four intrinsic and pair matrices
from (1)--(3). In these particular coefficient bases, every row is zero,
a single signed variable, or the difference of two variables. Attach
a grounded vertex for zero, and regard each nonzero equation as an
incidence edge. A spanning forest supplies independent matrix rows.
Every component not containing the grounded vertex supplies one
independent indicator vector in the kernel. These bounds agree, proving
each rank over Q and hence over C. The exported certificate records
the literal row hash, the forest row indices, and the component kernel
supports. This uses no floating-point or random rank calculation.

The controls concern canonical first identifications. Unlike the earlier
rejected candidate, this package does not assert a universal target
rank estimate for independent first-basis changes in every block.

The additive [higher-degree report](higher_note.md) computes the
remaining nonautomatic B degrees by exact graded occupancy matrices:

| B degree | Source rank | Target rank | Source minus target |
| --- | ---: | ---: | ---: |
| 0 | 140 | 140 | 0 |
| 1 | 12735 | 12587 | 148 |
| 2 | 573540 | 559238 | 14302 |
| 3 | 17050935 | 16315992 | 734943 |

The written [source B-leg theorem](source_b_koszul.md) gives

\[
\operatorname{rank}K_{B,p}(S)
=5\binom{100}{p+1}-\max(4-p,0)\binom{90}{p+1}.
\tag{8a}
\]

For p>=4 this is full row rank. Hence every B degree p=0,...,99
passes. The p=1 and p=2 source ranks also have literal matrix controls;
the p=3 source value and the all-degree tail use the written theorem.
The target values in the table are exact integer elimination results,
with independent small unsplit rational controls. Their target scope
remains the canonical identifications fixed in (4).

## 5. Both symmetric-power families pass in every degree

Let H_q=binom(q+4,4). For the two orientations

\[
\Phi_q:C^*\otimes\operatorname{Sym}^q A\longrightarrow
 B\otimes\operatorname{Sym}^{q+1}A,
\]

\[
\Psi_q:B^*\otimes\operatorname{Sym}^q A\longrightarrow
 C\otimes\operatorname{Sym}^{q+1}A,
\]

the source ranks, by Sections 1--2 of the
[common-input theorem](../2026-10-23-common-input-rank-barrier/proof.md), are

\[
\operatorname{rank}\Phi_q(S)=
 \min(140H_q,100H_{q+1}),\qquad
\operatorname{rank}\Psi_q(S)=100H_q.
\tag{9}
\]

Both are the maximum matrix ranks permitted by the format. Hence
every tensor of format (5,100,140), including T, satisfies both
necessary rank comparisons for every q>=0. This is an all-degree
consequence of the cited written theorem, not an extrapolation from a
finite numerical screen. That theorem imports the complex
boundary-format determinant result in DO01 with its stated hypotheses.

## 6. Quantum and upper support functionals

The known diagonal balancing construction is given in
[quantum_profiles.md](../2026-10-20-critical-character-extension/quantum_profiles.md),
Section 1, with attribution to the quantum-functional entropy definition
of Christandl, Vrana, and Zuiddam. Apply its identical A scaling to each
of the ten source blocks. The squared coefficient weights are

\[
w_{i,j}=\frac{\binom4i\binom9j}{\binom{13}{i+j}}.
\tag{10}
\]

The verifier checks all 500 weights across the ten blocks. Their total
mass is 140, each A marginal is 28, each individual B marginal is 7/5,
and each C marginal is 1. The normalized marginals are therefore
uniform in dimensions 5,100,140. Distinct support terms cannot share
both coordinates complementary to one leg, so the reduced matrices
are diagonal and these marginal computations suffice.

Consequently the canonical source attains the dimension upper bound
5^(theta_A)*100^(theta_B)*140^(theta_C) for every complex quantum
functional. Every tensor of this format is at most that value.
Thus this family of necessary inequalities cannot reject T.
The equality of upper support functionals with quantum functionals
is the imported SDW26 Theorem 1.1, not a local theorem.

The source uses one common canonical A basis. Simultaneous balancing
after arbitrary independent changes of A basis in the source blocks is
not asserted. The ambient target bound itself permits arbitrary target
basis changes.

## 7. Every C-leg degree passes

The [source C-leg theorem](source_c_koszul.md) treats any complex tensor
of format (a,N,M), with a>=2 and M>=N+a-1, whose bilinear contraction
A* times B* -> C has no nonzero zero-product pair. A quotient-bundle
resolution computes every C-leg Koszul rank from the dimensions alone.
The zero-free locus is nonempty and open, so these common ranks are
the maximum possible values among all tensors of that format.

Our source satisfies the hypothesis because multiplying two nonzero
polynomials gives a nonzero polynomial, independently in every output
block. The theorem even permits independent invertible first-space
identifications in the source blocks. For the present dimensions its
cancellation-free formula is

\[
\operatorname{rank}K_{C,p}(S)
=\sum_{j=0}^{103}
\min\!\left(100\binom{104}{j},5\binom{104}{j+1}\right)
\binom{36}{p-j}.
\tag{11}
\]

Every target of format (5,100,140), including targets with independent
first-basis changes or arbitrary coefficients, has C-leg rank at most
(11) in every degree p=0,...,139. No target C matrix is needed to prove
these comparisons. The theorem is a local written result, with
same-session cross-agent audits, not an imported external theorem.

The earlier, elementary proof
[source_koszul_tails.md](source_koszul_tails.md) establishes, for every
c Full(a,b) and N=c(a+b-1), that K_(C,p) is injective for p<=a-1 and
surjective for p>=c(a-1). It also constructs kernels showing that
these windows cannot be enlarged.

For (4), every C-leg comparison in degrees 0--4 and 40--139 therefore
passes automatically. The literal small controls cover 32 matrices
across six formats, including a=1, b=1, c=1, both window boundaries,
and an intermediate nonmaximal rank. These finite controls supplement
the all-parameter interpolation proof.

The independent [exterior-kernel and slice-cokernel controls](shadow_note.md)
also certify degrees 5,6 and 11,...,39 using the target's 428 explicit
degree-one kernel vectors and five evaluation first slices of rank 62.
Those bounds alone did not decide degrees 7,...,10. The general source
theorem now closes them, and every other C degree, as passing.

## 8. Construction excluded and evidence status

The separate [global RNC theorem](global_rnc_obstruction.md) proves that
T is outside the product-general-linear orbit closure of S, including
every independent target first identification. It first uses third
conciseness and proper rank-one incidence to constrain the flat limit
of the source's rational normal quartic. Degree and Hilbert polynomial
force a smooth quartic, so smooth orbit lifting and binary substitution
covariance replace any proposed first map by a regular invertible one.
The [catalecticant chart theorem](catalecticant_chart.md), with source
rank120 and universal target lower bound130, then gives a contradiction.

The earlier [copywise dimension lemma](copywise_dimensions.md) and the
completed rank tests retain their stated narrower scopes. The B-leg and
Schur target calculations use canonical first identifications; the global
exclusion permits independent target identifications. Source copies with
independent first identifications remain outside that global theorem.

The source has border rank140. The [cactus proof](cactus_rank.md) gives
canonical ordinary, smoothable and cactus rank178 for T. Neither that
finite-scheme result nor the single-orbit exclusion determines T's border
rank. In particular, no lower bound greater than140 for border rank is
asserted here.

The next construction must escape the finite-quartic projection hypothesis,
for example through enough width-one Full blocks or a different target
structure; see [the current question](QUESTION.md). Discovery used
floating-point optimization, while retained acceptance comparisons use
integer or rational certificates. The arbitrary-arc argument is a written
geometric proof with attributed external ingredients and same-session
audits, not a numerical verification. No external independent review,
formalization, improving degeneration or smaller exponent is claimed.
