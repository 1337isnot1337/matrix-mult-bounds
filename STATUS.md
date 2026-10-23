# Research status

## General quadratic biform ranks from two kernel indices

The [quadratic-kernel theorem](research/ai/2026-10-23-quadratic-kernel-indices/proof.md)
makes the rank of every nonzero `u(x)+z*v(x)+z^2*w(x)` slice computable
over any field, with coefficient degrees below a, a>=2 and b>=3.
After common-factor normalization, let D be the largest coefficient degree.
The two polynomial-kernel indices sum to aD; the first is the first degree
at which the explicit recurrence coefficient matrix has a nonzero kernel,
which occurs by floor(aD/2). The full source rank is
`ab+min(b,mu1)+min(b,mu2)`. For positive D, a zero first index is equivalent
to a fixed ground-field linear factor in the homogeneous z-quadratic.
This specializes the prior kernel-bundle identity and adds an effective
two-index procedure. Exact finite controls compare 2010 complete source
matrices, including the earlier equal-resultant ranks14/15 and their
characteristic-two behavior. Claim `AI-QUADRATIC-KERNEL-INDICES-001` is
written and unreviewed. No source-space cap, compatible matrix target,
singular degeneration or exponent improvement is established.

## Full-channel paired maps: overlap and leading rank loss

The [column-overlap proof](research/ai/2026-10-23-column-overlap/proof.md)
allows arbitrary full channel matrices at each retained polynomial column.
For fixed injective routing, an overlap graph bounds the leading target
slice intersection. Saturation accounts for new directions from singular
leading blocks, even with arbitrary first-map and auxiliary Laurent poles.
At fixed width and near-full outer dimensions, all but o(n) invertible
leading blocks force auxiliary border rank n^2-o(n^2). Equal positive
fractions above 1/m of invertible leading blocks also force quadratic
cost by the stated quantitative bound. General column-mixing maps and
more extensively singular leading blocks remain open. Claim
`AI-PAIRED-COLUMN-OVERLAP-001` is written and unreviewed. Exact separated
window restrictions and a full-channel sharp flattening example test its
scope; no exponent improves.

## Independent coordinate compressions are excluded with sharp loss six

The [complete independent-coordinate census](research/ai/2026-10-23-a4-coordinate-compressions/proof.md)
covers all 142,884 independent two-row / two-column deletions of the
46-dimensional outer space. Every complex projected dimension is at
least 40. Two exact integer kernel witnesses attain 40, so the maximum
loss is six. The existing bottom-left kernel reduction transfers this
bound to every independent coordinate compression of the full fixed
112-dimensional conjugation family. Its target requires loss at least
nine, so the entire coordinate class is excluded. Claim
`AI-A4-INDEPENDENT-COORDINATE-004` is written and unreviewed, with finite
computer assistance. Arbitrary noncoordinate flags remain a separate
question; no target or exponent improvement is established.

## Sharp rank-two slice gap for the paired source (October 23)

The [rank-two source theorem](research/ai/2026-10-23-paired-rank-two-gap/proof.md) proves over every field that a rank-two first-leg coefficient matrix Y in Q(n,b) gives source contraction rank at least b(b+1), attained by Y=E00+E11. The proof uses classical Kronecker strict equivalence for full-projective-rank polynomial-multiplication pencils and an elementary all-characteristic block recurrence. It also gives the exact formula b^2+sum min(e_i,d_j) in terms of the two minimal-index partitions. At b=4 the minimum rank is 20 rather than the 17 obtained from the earlier general lower bound. Standalone direct-source finite controls include 128 block checks, 16 sharpness ranks and complete GF2 rank-two censuses in seven small formats. Claim AI-PAIRED-RANK-TWO-SLICE-GAP-001 is written and unreviewed. The theorem does not construct a tensor degeneration or improve the 9/4 exponent bound.

## Exact three-term biform ranks escape pairwise-resultant data

The [three-term coefficient-rank obstruction](research/ai/2026-10-23-three-term-resultant-obstruction/proof.md) proves over Z that the literal R_(3,3) determinant for u=x^2, v=1+x^2, w=1+t*x+c*x^2 is t(2c^3-2ct^2+t^4). Two specializations have primitive degree two and all three pairwise resultants equal to one, but ranks 14 and 15 over every field of characteristic other than two. The rank-14 case has an integral left-kernel vector and a -4 minor; the rank-15 case has unit determinant. A degree-bounded 256-point exact integer certificate and focused standard-library test pass. Claim AI-THREE-TERM-RESULTANT-OBSTRUCTION-001 is written, unreviewed and strictly one-slice. Next: identify the two polynomial-kernel minimal indices for general three-term coefficient recurrences, not another pairwise-resultant search. No tensor target or exponent gain is established.

## All-field ranks of single-top-polynomial biforms

The [top-coefficient biform theorem](research/ai/2026-10-23-top-coefficient-biforms/proof.md) computes the literal cyclic-source matrix R_(a,b) for every f(x,z)=c_0+...+c_(e-1)*z^(e-1)+w(x)*z^e with 1<=e<b, nonzero constant c_0, constant lower coefficients, and nonzero polynomial w of x-degree d<a. Over every field, its exact rank is ab + sum_(j=0)^(e-1) min(b,d*floor((a+j)/e)). The leading polynomial-kernel vectors form a triangular residue basis, giving a complete all-field proof. The new controls pass 3,372 full-matrix modular comparisons and 24 independent-implementation rational matrix ranks. Claim AI-TOP-COEFFICIENT-BIFORM-RANK-001 is proof-written-unreviewed. It does not classify arbitrary quadratic-in-z coefficients, build a three-leg tensor target, or improve omega below 9/4. The separate [continuation](research/ai/2026-10-23-top-coefficient-biforms/CONTINUATION.md) records exact scope and provenance.

## Exact all-field ranks for quadratic-z slices with constant endpoints

The [quadratic-z middle-polynomial theorem](research/ai/2026-10-23-quadratic-z-middle/proof.md)
classifies every literal cyclic-source slice
`f(x,z)=alpha+v(x)z+gamma z^2` for nonzero constant alpha,gamma, any
polynomial v of degree below a, any field, a>=2 and b>=3. Writing
d=deg(v), with d=0 for v=0, its exact rank is
`ab+min(b,ceil(a/2)*d)+min(b,floor(a/2)*d)`.
The proof identifies the entire left kernel with two central polynomial
seeds satisfying separate degree bounds, and exports an explicit basis.
A literal-matrix finite-field verifier passes 580 exhaustive and
960 seeded cases, 135 spectrum checks and 940 kernel vectors; an
independent term-placement rational verifier passes 36 cases and
105 exact rational kernel vectors. Claim `AI-QUADRATIC-Z-MIDDLE-RANK-001`
is proof-written-unreviewed. PR209's row-polynomial method and the
broader quadratic question remain credited; this constant-endpoint
subfamily is distinct from PR207's diagonal-polynomial family.
Nonconstant outer coefficients, three-leg target maps and any exponent
improvement remain open.

This consolidated register retains the scope of each package and its originating
checkpoint. Later continuations can supersede earlier open frontiers without
changing the earlier theorem or validation receipt. All written, unreviewed
claims retain that status; internal audits and CI do not supply independent
mathematical review. See `research/claims.json` for individual evidence records.

## Two-sided singular A4 maps require at least nine lost leading directions

The [full-source conjugation package](research/ai/2026-10-23-conjugation-limit/proof.md)
studies every normalized A4 slice under conjugation by `I+t^-1 N`, for
the specified square-zero source slice N of rank 16. Its complete
112-dimensional saturated limit acts by scalars on a fixed
12-dimensional space. After arbitrary constant compression to 110
coordinates on each long leg, a full `M(10,10,11)` target requires at
least nine lost leading slice directions: `dim(P L C)<=103`.
The proof allows every Laurent first map and accounts for directions
that reappear after compression; it does not replace re-saturation
with the projected leading space.

Exact replay rebuilds the literal source, its unimodular normalization,
all polynomial-combination coefficients, 112 independent leading
matrices and the 12 scalar-action columns. All 6,216 principal
coordinate compressions have projected rank at least 108 modulo 1009,
hence dimension at least 108 over C. They lose at most four leading
directions and are all excluded. Claims `AI-A4-TWOSIDED-RANKLOSS-001`
and `AI-A4-TWOSIDED-COORDINATE-002` are written and unreviewed.
The arbitrary constant-compression locus of dimension at most 103,
moving compressions and other singular paths remain open. This is a
scoped obstruction; it supplies no target or exponent improvement.

The [low-rank reduction](research/ai/2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md)
now confines every rank-at-most-four limiting matrix to one 28 by 28
block. That block is the explicit 46-dimensional space
`E=G+[G,G00]+G00 G G00`. A full target with arbitrary constant compression
therefore requires rank-26 maps with `dim(Phat E Chat)<=37`.
Exact replay checks 112 block-coordinate identities and 16
transpose-conjugation identities; the minimum-rank-six input retains
the prior resolvent package's credit. Claim
`AI-A4-TWOSIDED-LOWRANK-003` is written and unreviewed. The remaining
universal lower bound of 38 is not proved.

Two [finite two-sided follow-ups](research/ai/2026-10-23-conjugation-limit/EXPLORATION.md)
also screen all 6,216 principal coordinate pairs per family. A product
of two noncommuting square-zero factors has no surviving pair. For the
nonnilpotent moving-unit family, all 221 pairs surviving the first rank
screen were re-saturated over Q and excluded by exact invariant-subspace
identities. These completed experiments supply no full target and make
no statement about arbitrary noncoordinate compressions.

## October 23: exact independent-product aggregation

The [29-product construction](research/ai/2026-10-23-aggregation-families/proof.md)
gives, over every characteristic-zero field and every n>=1,
rank(M(n^3,n^3,n^3)^direct_sum29) <= x^9+9x^8+36x^7+3x^6, x=n+1.
This improves the attained 28-product comparison family in Solomonik and
Blaeser arXiv:2610.26563v2. Its cost bound per output is strictly smaller
for every n: 29*r28-28*r29=x^6*(x^3+9x^2+7x+32)>0.
All 24,389 ordered mixed triples and all 48 correction subsets are checked
exactly by a separate set-based verifier. A finite-field control also
evaluates all 159,651 rank-one terms at n=2 for one exact assignment
over F101; it is an implementation control.
The external aggregation mechanism retains credit. This is a positive
finite construction with a written unreviewed uniform rank proof; it
does not provide a polynomial-source restriction or an exponent below 9/4.
An exact weighted AM-GM certificate shows that this displayed cost
formula cannot reach 9/4 by direct asymptotic-sum substitution at any n.
This is not a lower bound on optimal tensor rank. No optimality,
historical priority, independent review or formalization is claimed.
Claim: AI-AGGREGATION-29-001.

The [106-product continuation](research/ai/2026-10-23-aggregation-families/proof.md#7-exact-106-product-continuation)
adds an exact characteristic-zero construction of 106 independent
M(n^4,n^4,n^4) products for every n>=1, with budget
x^12+12*x^11+66*x^10+139*x^9+5*x^8, x=n+1.
All 1,191,016 ordered mixed triples and 222 correction subsets pass the
set-based verifier. Its cost bound per output improves the credited
external 105-product bound for every integer n>=7, certified by an exact
positive-coefficient polynomial after the shift x=8+u. A separate seeded
F2 evaluation of 106 independent 16-by-16 products checks all 9,323,181
rank-one positions; it is an implementation control, not the uniform proof.
Claim: AI-AGGREGATION-106-002.

The [size gate for these displayed budgets](research/ai/2026-10-23-aggregation-families/cost_floor.md)
also shows that every balanced conflict-free family with N<=10 fails the
direct 9/4 cost comparison when the whole (n+1)^(3N) aggregate is charged.
The induced-edge count gives p<=floor(2CD/(3D-1)), where
C=binom(3N,N) and D=binom(2N,N). N>=11 is necessary for this budget
model, not sufficient. This is not a lower bound on tensor rank;
cheaper aggregate decompositions and other
constructions remain outside its scope. Claim: AI-AGGREGATION-COST-FLOOR-003.
Both new proofs are written and unreviewed, with no exponent improvement.

## Exact diagonal biform block reduction and quadratic ranks

The [diagonal-polynomial source calculation](research/ai/2026-10-23-diagonal-biform-ranks/proof.md)
permutes each R_a(f(xz)) into independent conserved-index blocks. For
nonzero polynomial endpoints and degree d<a, its exact rank over every
field is a^2 plus the ranks of d explicit a-by-a Toeplitz matrices.
For a>=3 and a quadratic c0+c1*xz+c2*x^2*z^2 with c0*c2 nonzero, the
rank is a^2+2a or a^2+2a-1 according to a determinant recurrence.
The coefficient-one polynomial drops one rank exactly at a=2 mod 3 in
every characteristic. Claim IDs AI-DIAGONAL-BIFORM-BLOCKS-001 and
AI-DIAGONAL-QUADRATIC-RANK-002 are written and unreviewed. Independent
finite replay passes 312 block identities and 112 full literal source
matrices over five prime fields, plus 144 quadratic, 5,016 triangular
and 290 recurrence cases. No new full tensor target or exponent follows.
The next scoped question is simultaneous Toeplitz defects at degree>=3.

## Exact three-leg contraction strata of the one-dependency oblique residual

The [slice-strata proof](research/ai/2026-10-23-oblique-slice-strata/proof.md)
classifies ordinary one-leg matrix ranks of the fixed adapted residual
over every field. Every nonzero first slice has rank two or four; its
projective rank-two locus is two disjoint projective `(r-2)`-spaces.
Exact two-column rank formulas determine the entire second- and
third-leg strata. Exhaustive binary checks cover all three legs at
`r=2,3,4,5` (6120 contractions); 2160 seeded odd-prime checks are
separate finite evidence. Claim `AI-OBLIQUE-SLICE-STRATA-001` is a
written, unreviewed proof, using PR147's pinned native residual
identification. It changes neither the 12..18 border-rank interval at
`r=5` nor the verified 9/4 exponent baseline.

## Exact rank spectrum of affine-in-z cyclic-source biforms

The [affine-z coefficient-rank theorem](research/ai/2026-10-23-affine-z-biform-ranks/proof.md) computes the literal R_(a,b)(u(x)+z*v(x)) over every field for all a,b>=2: its rank is ab+min(b,a*d), where d is the largest degree of the coprime pair after removing gcd(u,v), and d=0 if one coefficient vanishes. Every rank in the resulting finite spectrum is attained by 1+x^d*z. An explicit polynomial left-kernel parametrization proves the formula without the previous general biform gap. Finite exact controls cover 3265 exhaustive pairs, 2992 deterministic seeded pairs, 570 prescribed spectrum points and 300 a>b cases over F2,F3,F5,F7,F101. Claim AI-AFFINE-Z-BIFORM-RANK-001 is proof-written-unreviewed. This is a one-slice statement, not a source-space cap, tensor target or smaller exponent. Next: the three-coefficient u+z*v+z^2*w syzygy recurrence, separate from the diagonal Toeplitz problem in PR207.

## Laurent cancellation cannot remove a common channel-rank deficit

The [formal channel-separation proof](research/ai/2026-10-23-laurent-channel-barrier/proof.md)
extends the ordinary factorizations in pending PR157, PR173 and PR179
to arbitrary Laurent poles and arbitrary auxiliary maps. A common kernel
over K((t)) makes one source contraction regular before its rank equations
are specialized. The argument permits moving channel bases and genuine
cancellation between source and auxiliary poles.

For the stated maps to a near-full target M(l,h,r), the auxiliary
first-flattening rank is at least `(l*r-n^2+g_B*g_C)_+`, with the exact
bandwidth/exception counts in the note. At fixed widths, outer ratios
tending to one and sublinear bandwidth/exception counts, this is
`n^2-o(n^2)`. Thus increasing pole orders cannot supply subquadratic repair
while the generic common channel rank remains below h. Full generic
channel rank and general nonlocal maps remain open.

The [border-rank refinement](research/ai/2026-10-23-laurent-channel-barrier/rank_margin.md)
adds the channel-rank deficit to the auxiliary cost: if the good subspace
has dimension d>=1 and generic channel rank at most rho<h, then
`border_rank(R) >= d+h-rho-1`. Its first-flattening bound remains d.
The proof uses rank-one-term substitution and a finite-pole parameter
substitution for auxiliary border approximations. At fixed h this is a
constant improvement to the finite bound, with the same asymptotic scope.

All three claims are written and unreviewed. Seven original focused tests
and six refinement tests pass, including genuine pole cancellation,
moving subspaces, complete Laurent coefficient identities, sharp d=1
examples and strict parameter-order controls. The preceding source-branch proof tree
recorded all 904 regression tests and five archive replays, with exact
coverage and the interrupted-prefix procedure recorded in its
[validation receipt](results/laurent-channel-barrier-2026-10-23/VALIDATION.md).
The refinement has its own
[focused validation receipt](results/laurent-channel-barrier-2026-10-23/rank-margin-validation.json).
No target construction or smaller exponent is supplied.

## Alternating matched-sector separations

The [all-size alternating construction](research/ai/2026-10-23-alternating-sector-separation/README.md)
extracts any positive number `k` of matched convolution sectors from one
`C(a,B)`, with `B=sum_i b_i+floor(k/2)(a-1)`. A termwise interval proof
identifies the exact weight-zero support; an exact finite verifier checks the
recorded small grid. The shared-leg entropy inequality gives the corresponding
character-profile bound. The matching scalar profile `P_*` satisfies every
such bound, so this does not improve the exponent. Claim
`AI-ALTERNATING-K-SECTORS-001` is written and unreviewed; no character
realization, independent review, or formalization is claimed.
The padding is also minimal among exact copies that retain the common first
leg and either preserve or exchange the other two legs. This does not bound
decompositions with different sector tensors or auxiliary summands.

## A shared-output candidate fails for every target first identification

The [exact second-leg Koszul certificate](research/ai/2026-10-23-shared-output-koszul/proof.md)
rejects the canonical format-preserving candidate from ten Full(5,4)
blocks to ten Full(5,3), one Full(5,2), and two shared-output P(5,4,2)
blocks. It has a strictly larger symmetric operational score and passes
the previously used common-leg screens, but the second-leg degree-one
Koszul rank increases from2595 to2616. Ten integer minors with determinant
plus or minus one and56 exact kernel vectors certify the ranks.

The separate [all-identifications proof](research/ai/2026-10-23-shared-output-koszul/universal_identifications.md)
extends the exclusion to every independent invertible first-leg
identification of the thirteen target blocks. The target rank is always
at least2616. A squarefree contraction bounds Full/Full pair kernels;
constant-rank coefficient pencils bound the shared-output pair kernels.
All degeneration maps, including singular or polar first-map charts, are
covered. The source still has one common canonical first coefficient
basis. Claims `AI-SHARED-OUTPUT-KOSZUL-001` and
`AI-SHARED-OUTPUT-ALL-IDENTIFICATIONS-002` are written and unreviewed.
The frozen canonical checkpoint retains its original scope; this separate
extension removes its target-identification limitation. No general
mixed-orientation barrier, tensor construction or smaller exponent follows.
Future mixed-output candidates must be screened on both nonshared legs.

## Arbitrary common-input Full/Mid mixtures preserve the operational barrier

The [symmetric-power rank argument](research/ai/2026-10-23-common-input-rank-barrier/proof.md)
extends the result to every actual complex degeneration between finite
shared-first-leg sums of Full and Mid blocks with the same full first
dimension. Widths, multiplicities, orientations and independent invertible
first-leg identifications may all vary. For every rectangular parameter, the partial-sum score
`F_theta^star(T)^(1/p_1)` is a finite nonnegative combination of two
families of symmetric-power flattening ranks on this block class. For identical
source blocks, the two long-leg dimensions alone give the same potential
comparison for heterogeneous targets. Claims
`AI-COMMON-INPUT-RANK-BARRIER-001` and
`AI-HETEROGENEOUS-PACKING-DIMENSIONS-002` are written and unreviewed.
The critical determinant theorem retains its GKZ and Dionisi–Ottaviani
credit; the potential and concavity retain their AVZ26 credit. Shared-output
blocks and smaller first subspaces remain outside this theorem. No actual
improving tensor map or smaller exponent has been found.

## Pass packings preserve the complete polynomial operational barrier

The [operational extension](research/ai/2026-10-23-pass-operational-barrier/proof.md)
shows that every primal and dual packing in Pass's October20 preprint
preserves the full rectangular family of operational potentials in
Amanov, van den Berg and Zuiddam's October21 preprint. Adjoining those
packings and their compatible compositions therefore leaves the published
square9/4 and rectangular method barriers unchanged. A separate exact
ratio argument shows that both long-leg dimensions already enforce the
symmetric barrier for every stated homogeneous Full/Mid target mixture.
Claims `AI-PASS-OPERATIONAL-EXTENSION-001` and
`AI-HOMOGENEOUS-PACKING-DIMENSIONS-002` are written and unreviewed.
The authors retain credit for the imported constructions and barrier.
The local contribution is their stated extension and dimension comparison.
No unrestricted lower bound, new tensor map or smaller exponent is claimed.

## Elementary arbitrary-biform rank gap

The [elementary biform proof](research/ai/2026-10-23-elementary-biform-gap/README.md)
reproves the existing crossed block gap over every characteristic-zero
field without the earlier vector-bundle splitting input. For2<=a<=b,
separable nonzero f has rank ab, and every other f has rank at least ab+a.
A mixed irreducible factor of multiplicity e gives the stronger bound
ab+ae. If its mixed part is a power of one irreducible factor linear in x,
univariate factors preserve crossed rank and the exact rank is a(b+e);
see [the corollary](research/ai/2026-10-23-elementary-biform-gap/linear_factor_powers.md).
The proof uses exact affine covariance, a lowest-term limit at a
suitable factor zero, and the formula rank R((alpha*x+beta*z)^e)=a(b+e)
for1<=e<a. Classical path determinants retain their original attribution;
the required cancellation argument is reproduced. Claims
`AI-ELEMENTARY-BIFORM-GAP-001` and `AI-MIXED-POWER-BIFORM-RANK-001` are
written and unreviewed. Exact acceptance checks45 power cases,525 integer
minors and20 affine/scaling controls. Prior files and dependency ledgers
are unchanged; no target degeneration or exponent improvement follows.

## A uniform high-power boundary for the S5 degree-cover method

The [higher-power argument](research/ai/2026-10-23-s5-higher-powers/proof.md)
proves that every coordinate cover of the full separately bounded S5
degree majorant costs too much to exclude any of PR111's eleven remaining
single targets at every source power n>=36. It permits nonmonotone covers
and unequal leg choices within that majorant. A coordinate matching gives
an explicit cover-cost lower bound; a concatenation injection and 72
exact integer seed inequalities prove the all-power statement. Claim
`AI-S5-MAJORANT-HIGH-POWER-001` is written and unreviewed. This is not an
actual-source slice-rank lower bound, target construction or exponent
improvement. Finer support, other bases, non-coordinate decompositions
and powers below 36 remain separate questions.

## Geometric diagonal-source ranks are exact in every characteristic

The [geometric diagonal-rank proof](research/ai/2026-10-23-geometric-diagonal-ranks/proof.md) treats individual cyclic-source slices with coefficients in a nonzero geometric progression: for all fields, a>=2, 1<=d<a and c,lambda nonzero, rank R_a(c*sum_(k=0)^d(lambda*x*z)^k) = a^2+a*d-E, where q=a mod(d+1), E=0 at q=0 and E=(q-1)(d+1-q) otherwise. The theorem gives an explicit kernel basis and each of the d simultaneous Toeplitz defects; the maximum total defect is floor(d^2/4). This extends concurrent PR207's all-degree block reduction and quadratic example, with full credit retained. Claim AI-GEOMETRIC-DIAGONAL-RANKS-001 is **proof-written-unreviewed**. Exact finite-field and separate rational verifiers pass. It addresses individual source slice ranks only: no compatible three-leg maps, matrix target or exponent improvement.

## Exact convolution graph row barrier

The [R5 route map](docs/route-synthesis.md) identifies pinned Filmus neighbor,
square-tripling, and general-tripling shared-leg identities, a replication
degeneration packaged as a shared-leg row, componentwise restrictions,
input-swap symmetry, and border rank `u+v-1` for each rectangular source
`C(u,v)`. A direct coordinate check extends the terminal `C(2,1)` to `C(q,1)`
for every `q>=2`; that extension is written but not locally formalized.
The replication and componentwise-restriction wrappers are not locally
formalized. For source `C(u,v)` and terminal `C(q,1)`, the `P_*` potential
gives `qL<=P_*(u,v)` and `P_*(u,v)^3<=(u+v-1)^4`; equality can occur only for
source `C(1,1)`. The strict improvement criterion therefore never holds.
Claim `AI-R5-CONVOLUTION-GRAPH-BARRIER-001` is written and unreviewed. It
excludes only this restriction/neighbor/general-tripling/replication/input-swap
row family from rectangular convolution sources to thin terminals.
The pinned full oriented profile laws also admit the critical common profile
at weights `(3/4,3/4,3/4)`; this feasible-relaxation witness is tracked as
`AI-R5-ORIENTED-PROFILE-SCREEN-001` and does not provide a character.
Additional identities, other endpoints and stronger tensor-level constraints
remain open. No smaller exponent is established.

## Exact extension criterion for the prescribed full conic third jet

The [fixed-third obstruction](research/ai/2026-10-23-conic-fixed-third-obstruction/proof.md)
settles the next prescribed-jet question on d nonzero. PR107's complete
B/C coefficients through order three and all three kernel corrections
extend to order four exactly when Delta=(a+d^3)(b-d^3)=0. That condition
is also equivalent to formal and polynomial extension. A 28-entry exact
functional kills every fourth-map and fourth-kernel unknown but has
residual -d(a+d^3)^4(b-d^3)^3/3. On both exceptional components, exact
linear maps preserve the entire specified jet and give sufficiency.
Seven focused tests and complete standard-library acceptance pass.
Claim `AI-CONIC-FIXED-THIRD-OBSTRUCTION-001` is written and unreviewed.
The preceding two-jet curve remains valid everywhere on d nonzero: it
chooses a different third coefficient. No general matrix-target
obstruction or improved exponent follows from this local classification.

## The prescribed full conic two-jet extends to all orders

The [fixed-two-jet curve](research/ai/2026-10-23-conic-fixed-two-curve/proof.md)
preserves every entry of PR107's B0,B1,B2,C0,C1,C2 and the two supplied
kernel corrections Y1=Y2=0. For every complex a,b,d with d nonzero and
c=-d^3, it gives exact polynomial maps of degrees eight and nine over
Q[a,b,d,d^-1], with actual d-pole bounds five and six. There are no
additional a,b or Delta guards. The complete product stays on the same
twelve first-source coordinates; constant minors1,1,-1 give formal
ranks14,14,12. Exact replay checks all18 product orders and all352800
kernel coefficient positions. Six focused tests and a separate sparse
Laurent reconstruction pass. Claim `AI-CONIC-FIXED-TWO-CURVE-001` is
written and unreviewed. This closes the prescribed two-jet question on
the stated chart. PR107's full third jet, which has a nonzero kernel
correction, remains a separate question. No full matrix target or
improved exponent is established.

## The prescribed full conic first jet extends to all orders

The [fixed-first-jet curve](research/ai/2026-10-23-conic-fixed-first-curve/proof.md)
strengthens the earlier cubic-component construction: for every complex
a,b,d with c=-d^3, both full constant and first coefficient maps of
PR107 extend to exact cubic maps B(t),C(t) over Q[a,b,d]. The supplied
first source-kernel correction is also preserved. Complete source
replay checks all seven possible product coefficients; the fixed kernel
and unit minors give formal ranks14,14,12. The construction includes
d=0 and the linear-component intersections without parameter inverses.
Claim `AI-CONIC-FIXED-FIRST-CURVE-001` is written and unreviewed.
Its second coefficients differ by boundary terms, so preservation of
PR107's full two-jet is not asserted here. The full matrix target and
an improved exponent remain unconstructed.

## Polynomial all-order curves on the cubic conic component

The [all-order criterion](research/ai/2026-10-23-conic-polynomial-curve/all_order_criterion.md)
completes normal-class existence on the full affine conic base chart:
for every complex a,b,c and nonzero[lambda:mu], a suitable first tangent
extends to a formal (indeed polynomial) incidence curve exactly when
`(a-c)*(b+c)*(c*lambda^3+mu^3)=0`. Necessity is PR101's complete
second-order obstruction; sufficiency combines its linear-component
curves with the polynomial cubic-component curve below. Claim
`AI-CONIC-ALL-ORDER-CRITERION-002` is written and unreviewed. It is the
correct affine-chart prerequisite for the projective result above.
All projective normal directions are included in its stated affine base;
the new theorem supplies the other base charts. Extension of every
prescribed full tangent remains a distinct question.

The [polynomial-curve proof](research/ai/2026-10-23-conic-polynomial-curve/proof.md)
constructs an exact curve for every complex a,b,d with c=-d^3, including
d=0. The two fourteen-row maps have polynomial t-degrees one and three,
with coefficients in Q[a,b,d] and no parameter denominators. Their
complete contraction stays on the same twelve first-source coordinates;
constant unit minors certify formal ranks14,14,12. Literal replay checks
all five possible product coefficients against the original4096-term
source. The first normal class is exactly[1:d] and never vanishes.
The curve changes the boundary part of the first tangent, so it does not
settle extension of a prescribed full first or second jet. Claim
`AI-CONIC-POLYNOMIAL-CURVE-001` is written and unreviewed. The full
M(10,10,11) target and a smaller exponent remain unconstructed.

## Mixed conic lifts through order four and rational order-ten, fourteen and fifteen witnesses

The [higher-jet proof](research/ai/2026-10-23-conic-higher-jets/proof.md)
extends PR107's mixed family through order four for every complex a,b,d
with d nonzero and c=-d^3. The explicit coefficients lie in
Q[a,b,d,d^-1], with d-pole order at most three. A separate rational
witness extends the point a=1,b=2,d=1 through order ten. A separate
fourteenth-order witness at that point preserves its coefficients through
map order nine and source corrections Y1 through Y9, then varies later
coefficients. A fifteenth-order continuation preserves that witness through
map order thirteen and source corrections Y1 through Y13. All rational
witnesses preserve PR107's constant, first and second coefficients. The symbolic and
rational acceptance programs contract the literal 4096-term source
and check every moving-kernel coefficient, with leading ranks14,14,12.
Claims `AI-CONIC-MIXED-FOURTH-JET-001` and
`AI-CONIC-RATIONAL-TENTH-JET-002` and
`AI-CONIC-RATIONAL-FOURTEENTH-JET-003` and
`AI-CONIC-RATIONAL-FIFTEENTH-JET-004` are written and unreviewed. These are
rank-twelve incidence jets with specified lower coefficients. The separate
polynomial curve above gives all-order existence after allowing boundary
velocity to change; it does not preserve these specified lower jets.

## Third-order lifts on the mixed cubic conic component

The [third-jet witness](research/ai/2026-10-23-conic-third-jets/proof.md)
extends PR101's first jet through order three for every complex a,b,d
with d nonzero and c=-d^3, after changing its second coefficient. The
coefficient ring is Q[a,b,d,d^-1], with poles of order at most two in d.
Independent symbolic replay rebuilds the 4096-term integer source and
checks all 19600 moving-kernel coefficients at each positive order;
leading minor determinants1,1,-1 give map row ranks14 and first-source
rank12 throughout this chart. An earlier explicit rational point also
has a separate standard-library replay. Claims
`AI-CONIC-RATIONAL-THIRD-JET-001` and `AI-CONIC-MIXED-THIRD-JET-002`
are written and unreviewed. The later packages above supply fourth-order
lifts and all-order existence for the normal class, with their distinct
lower-coefficient conditions. The full matrix target remains open.
No smaller exponent is established.

## Fixed oblique-repair Koszul boundary

The [complete full-space Koszul atlas](research/ai/2026-10-23-oblique-koszul-atlas-extended/README.md)
checks all 112 maps for four fixed residuals, r=3,4,5,6. Integer unit
pivots certify every matrix rank over every field; a separate binary
elimination checks the ranks again. The best border lower bounds are
8,9,11,13, respectively, never above the earlier equalizer bounds in
[PR147](https://github.com/1337isnot1337/matrix-mult-bounds/pull/147).
All 576 native Q(6,4) terms are re-contracted locally. This finite
method boundary leaves the inherited r=5 border interval 12 through 18
unchanged. Projected flattenings, stronger secant conditions and improved
maps remain open. Claim `EXP-OBLIQUE-KOSZUL-ATLAS-EXTENDED-001` has no independent
review or formalization and supplies no exponent improvement.

## Ordered input roles in the monomial score

The [ordered-input census](research/ai/2026-10-23-ordered-monomial-search/README.md)
adds the missing `a > b` dimensions to the historical binary and ternary
searches: 24,708 and 370,252 ordered candidates respectively, with maximum
ratio one and no violation. The added orientation scores strictly better
than its swapped historical counterpart in 810 binary and 10,975 ternary
cases. An all-size alternating family proves why the shared first input
cannot be discarded by exchange or pointwise dominance: its swapped score
advantage tends to a factor of two, while its source ratio remains 9/14.
Claims `AI-ORDERED-SCORE-ASYMMETRY-001` and
`EXP-ORDERED-MONOMIAL-SEARCH-CENSUS-001` distinguish the written unreviewed
calculation from finite search coverage. A separate verifier checks retained
supports and exact scores; global maxima require the completed census replay.
The historical archives and PR118's scope remain unchanged. No smaller
exponent is established.

## Complete fixed-resolvent rank-six locus and sharp compression

The [rank-six classification](research/ai/2026-10-23-resolvent-rank-six-finite/proof.md)
resolves the open locus question from PR139. The rank-at-most-six matrices
form a 17-dimensional linear space, and every nonzero member has the same
six-dimensional image, over every field. Over an algebraically closed field,
two rank-109 compressions lose at most one direction, so their image has
dimension at least 111. An explicit integer pair attains 111 in every field.
The exact certificate checks 26 seven-minor eliminations, five six-minor
eliminations and 111 unit compression pivots. Claim
`AI-RESOLVENT-RANK-SIX-FINITE-001` is written and unreviewed. This is structural
information about the fixed space; it constructs no matrix target and
establishes no smaller exponent or arbitrary singular-trajectory exclusion.

## Complete width-two monomial score barrier

The [width-two proof](research/ai/2026-10-23-width-two-monomial/proof.md)
shows that the archived monomial sector score never exceeds P_* on
C(2,b) or C(b,2), for every b>=2 and all integer weights. A path-component
identity gives the exact deficit, sharp gap and every equality support
for C(2,b); the transposed orientation has equality only at full support.
All 59,046 orientation/support cases through b=10 replay against the
unchanged original scorer. Claim `AI-WIDTH-TWO-MONOMIAL-001` is written
and unreviewed. This closes that score at minimum input size two, not
arbitrary degenerations or stronger sector scores. No improved exponent.

## Conditional paired long-leg target screen

The [filtered-bundle target screen](research/ai/2026-10-23-paired-long-leg-target-screen/README.md)
uses the all-degree source-rank lower bound in unmerged PR #169, whose
written proof remains unreviewed. Exact target-rank comparisons show that,
conditional on that bound, both long-leg target ranks are no larger than
the source lower bound for all 28 saved formats in degrees 183–209 at
`a=14`, 211–241 at `a=15`, and 241–274 at `a=16`. This closes those finite
windows to an additional long-leg rank exclusion. Other intermediate
degrees remain undecided; the comparison is not an exact source-rank
formula or an exponent improvement.

## Rank-three inputs exclude the two nonsquare A(8,9) formats

The [rank-three argument](research/ai/2026-10-23-rank-three-hankel/proof.md)
excludes ordinary complex A(8,9) restrictions to M(28,31,31) and
M(29,30,31). Every rank-three parameter must map to Hankel rank at most
seven. Coefficient injection requires a symbol image of dimension13
through16; its rank-three image then has codimension at least two,
which the new projection budget permits only from dimension20 onward.
The proof uses the classical Borel fixed-point theorem and retains all
prior source/Hankel credit. Six focused tests check22014 Ferrers cases,
all697 coordinate sections omitting at most three coordinates, exact
projection differentials, conormals and target rank budgets. Claims
`AI-DETERMINANTAL-PROJECTION-BUDGET-001`, `AI-HANKEL-LARGE-SECTIONS-001`
and `AI-A89-NONSQUARE-EXCLUSION-001` are written and unreviewed.
The ordinary M30 format has only the weaker rank-two input constraint
and remains open. No singular exclusion or smaller exponent is established.

## Locally Toeplitz two-long-leg obstruction: quadratic repair cost

The [October 23 proof](research/ai/2026-10-23-toeplitz-long-legs/proof.md)
shows that ordinary restrictions of Q(n,m), m>=2, with both long-leg maps
Toeplitz in the bulk of half-bandwidth D and e_B,e_C arbitrary exceptional
source columns require correction border rank at least
(n-2(m-1+D)-m*e_B)_+*(n-2(m-1+D)-m*e_C)_+.
The first-leg map is completely unrestricted; exceptional maps may be
nonlocal. Fixed m and sublinear D,e_B,e_C force n^2-o(n^2) repair,
excluding this map class from the existing O(n^alpha), alpha<3/2,
paired-source conditional route. Five exact finite tensor/symbol controls
pass, including arbitrary first-leg mixing and nonlocal exceptions.
Written and unreviewed; no general degeneration exclusion and no
improved exponent. Next: variable-coefficient bulk maps and singular
Laurent cancellations.

## Exact binomial biform ranks in every characteristic

The [binomial-rank proof](research/ai/2026-10-23-binomial-biform-ranks/proof.md)
gives an exact all-size formula for either orientation of a two-monomial
biform with nonzero coefficients over any field. Its rank is
`a^2+sum min(n_i,m_j)` for input residue lengths modulo the two offsets.
At equal offset d and a=q*d+r, this is `a^2+ad-r(d-r)`; unequal residues
give the selected nondivisor ranks34,38,62,68, with deficits1,2,1,2
from a(a+d).
An elementary path-matrix proof imports no splitting or classification
theorem. Claims `AI-BINOMIAL-BIFORM-RANK-001` and
`AI-BINOMIAL-ELEMENTARY-GAP-002` are written and unreviewed. Exact controls
verify114 full minors and entry covers,8555 lower-gap cases and435
quotient/remainder identities. Weighted rational, symbolic and prime-field
tests pass. The binomial gap can replace the corresponding PR148 input
through an explicit dependency amendment; the broader biform theorem
retains its original credit. No nondivisor dimension cap, target or
exponent improvement is established.

## Complete ordered monomial scopes and recognition audit

The [independent monomial audit](research/ai/2026-10-23-ordered-monomial-audit/README.md)
replays all 60 retained exact PR118 certificates at its pinned head and
completes both input orientations of the finite exhaustive searches.
It checks 24,708 binary and 370,252 ternary weight pairs, adding 172,292
previously omitted a>b cases. Neither scope has a scored violation; both
exact maxima are 1. Input exchange can change this lower-bound score, so
the original a<=b restriction must remain explicit. Claim
`EXP-ORDERED-MONOMIAL-AUDIT-001` is a finite experiment.

The accompanying [recognition proof](research/ai/2026-10-23-ordered-monomial-audit/recognition.md)
shows that order and reversal tests already detect every complete convolution
support obtainable by arbitrary coordinate relabeling inside i+j=k, at all
sizes. Claim `AI-ADDITION-SUPPORT-RECOGNITION-001` is written and unreviewed.
Brute-force bijections agree on all 511 nonempty subsets of C(3,3).
Stronger sector bounds, arbitrary weights and general basis changes remain
open. No tensor character or smaller exponent follows.

## All-size width-two support score obstruction

The [width-two support proof](research/ai/2026-10-23-width-two-support/proof.md)
bounds the historical matched-component score by `P*(2,b)=(4b+2)/3`
for every b>=2 and every support subset of C(2,b) or C(b,2). This covers
arbitrary diagonal weights and support deletions. An exact path deficit
identity classifies equality in the first orientation; in the reversed
orientation equality requires full support. The theorem concerns the
existing convolution-recognition and single-slice fallback score. Stronger
estimates on unrecognized sectors remain open. Claim
`AI-WIDTH-TWO-SUPPORT-SCORE-001` is written and unreviewed. No spectral
realization or smaller exponent is established. Validation is recorded
in the package and its result directory.

## Complete rank-six locus and sharp compression loss

The [rank-six classification](research/ai/2026-10-23-resolvent-rank-six-locus/proof.md)
identifies the entire rank-at-most-six locus of the fixed resolvent space W
as a 17-dimensional linear space. Every nonzero member has rank six and
the same six-dimensional image. The mixed outer block has a five-dimensional
locus, certified over every field by 26 triangular seven-minors and five
terminal six-minors. The [boundary continuation](research/ai/2026-10-23-resolvent-rank-six-locus/boundary.md)
excludes rank seven using 26 eight-minors and proves the next rank eight
is attained. Over every field, two rank109 compressions can lose at most
one dimension of W; a displayed compression attains dimension111. Every
six-loss allocation with positive input loss has the same sharp bound;
deleting the entire common output image instead kills 17 dimensions.
Claims `AI-RESOLVENT-RANK-SIX-LOCUS-001` and `AI-RESOLVENT-RANK-GAP-001`
are written and unreviewed. This closes the
fixed-space rank-six classification and sharpens the prior alignment from
a 28-space to a specific six-space. General singular trajectories and the
exponent question remain open.

## Pinned internal audit of the divisor source-space cap

The [internal proof audit](research/reviews/2026-10-23-divisor-source-caps/PROOF_REVIEW.md)
checks PR148 at `673710d3a4284d88e4d24350681b26912831bf7a` without
incorporating that unmerged package. No gap was found in its stated
complex divisor-cap and regular-long-leg arguments. The review checks
the arbitrary-subspace specialization, wrapped residue blocks, sharp
strip, and regular correction despite a polar projection. A separate
implementation checks 237 literal weighted pair ranks and 67,170 coefficient
weight identities, plus Laurent and boundary controls. Its exact scope
and inherited bundle-splitting input are explicit. This is internal Codex
review; both cited claim IDs retain their original written-unreviewed
status. No nondivisor cap, new A4 cutoff, or exponent improvement follows.

## Two variable paired-source long maps with a strict channel gap

The [two-variable argument](research/ai/2026-10-23-two-variable-long-legs/proof.md)
allows both finite-band long maps to vary by source column. A common
B window span of dimension r and s fixed C coefficient profiles force
quadratic auxiliary repair whenever r*s<m. The first map and sparse
exceptional columns are arbitrary. At fixed width and sublinear bandwidth
and exceptions the lower bound is n^2-o(n^2). This includes two linear
polynomial maps at width at least five. The Laurent-symbol method retains
PR173/172 credit and is reconstructed without an unmerged dependency.
Claim `AI-TWO-VARIABLE-PAIRED-REPAIR-001` is written and unreviewed.
Full-profile maps and Laurent cancellation remain open; no improved
matrix exponent is claimed.

## The geometric Hankel bound in every characteristic

The [divided-square extension](research/ai/2026-10-23-hankel-all-characteristics/proof.md)
extends the linear-annihilator Hankel Segre bound to every field, including
characteristic two, with the same numerical cap. It retains the diagonal
assignment equations that would disappear under ordinary polarization.
Over finite fields the hypothesis is a polynomial identity on decomposable
inputs, equivalently a rank bound over an algebraic closure; rational-point
testing is justified by a supplied interpolation lemma when q>=r+1 over F_q.
No such implication is assumed for smaller fields. The ordinary cyclic-source
consequence likewise extends to every field. Exact controls check 911
evaluation fibers and 882 monomial assignment systems over F2, F3 and F5;
a negative control detects the lost diagonals. Claim
`AI-HANKEL-ALL-CHARACTERISTICS-001` is written and unreviewed. No stronger
characteristic-zero cap, singular-degeneration exclusion, constructed
target or smaller exponent follows.

## Sharp compression bound through total rank loss seven

The [loss-seven continuation](research/ai/2026-10-23-resolvent-loss-seven/proof.md)
proves that compression factors with total rank loss at most seven kill at
most max(0,p+q-5) directions of the fixed-resolvent W, over every field.
At total loss seven, integer factors of ranks109 and108 attain two lost
directions and compressed dimension110. The proof uses the complete
rank-six locus, the absent rank-seven stratum, classical projective
intersection and scalar extension/descent. Claim
`AI-RESOLVENT-LOSS-SEVEN-001` remains written and unreviewed. The finite
full-space controls have dimensions112 and110 over F2 and F3. Total loss
eight and arbitrary singular target constructions remain open; no smaller
exponent is established.

## Complete fixed-resolvent rank-six locus and sharp critical compression

The [rank-six continuation](research/ai/2026-10-23-resolvent-rank-six/proof.md)
classifies the complete rank-at-most-seven locus of the fixed-resolvent W.
It is a 17-dimensional linear space whose every nonzero matrix has rank six
and the same six-dimensional image. In particular there is no rank-seven
matrix. Twenty-six triangular eight-minor identities give an all-field
certificate. Over algebraically closed fields, two rank109 compression
factors kill at most one direction, so dim PWC>=111 sharply. The exact
image condition refines the predecessor's final-layer alignment.
Claims `AI-RESOLVENT-RANK-SEVEN-GAP-001` and
`AI-RESOLVENT-CRITICAL-COMPRESSION-002` remain written and unreviewed.
This classifies the predecessor's open locus; arbitrary singular trajectories,
larger compression losses and a smaller exponent remain unresolved.

## Variable-coefficient shift-window obstruction for paired sources

The [October 23 shift-window proof](research/ai/2026-10-23-shift-window-long-legs/proof.md)
extends the independently open two-Toeplitz argument (PR #157) to ordinary
paired-source maps with one genuinely variable-coefficient long leg and
one Toeplitz long leg. If all interior m-shift coefficient windows of the
variable leg span one common proper subspace of K^m, of rank r<m, and both
legs have half-bandwidth D outside e_B,e_C arbitrary exceptional columns,
the correction border rank is at least
`(n-2(m-1+D)-m e_B)_+ (n-2(m-1+D)-m e_C)_+`, even with arbitrary
first-leg mixing. For fixed m, D=o(n), e_B+e_C=o(n), this is n^2-o(n^2).
This excludes polynomial B bulk degrees <=m-2 and shared-recurrence
sequences of order <m in the stated ordinary construction class; mirrored
C-side statements also hold. Five finite exact cases and four focused tests
pass. Claim `THM-PAIRED-SHIFT-WINDOW-001` is written and unreviewed.
Moving or full-rank window spaces, two variable long legs, and singular
Laurent cancellations remain open. No improved exponent.

## Quadratic pencils inside the A10 moment four-space

The [four-space pencil calculation](research/ai/2026-10-23-hankel-fourspace-pencils/proof.md)
extends the prescribed-seed study to arbitrary lines in moments 3,7,11,15,
under an explicit nonzero determinant guard chi. The exact polynomial
identity `det N=-4*Delta*chi^3` gives common tangent dimension four when
Delta is nonzero and seven when Delta vanishes. In the first case the
four-space is the unique maximal linear rank-eight Hankel extension.
For the full exceptional family `A=v,B=beta*u,C=u,D=v`, with beta cubed
different from one, a constant-unit pivot, quadratic Schur coefficients
and a higher determinant also force the unique maximal extension to have
dimension four. Other exceptional lines, quadratic pencils outside this
four-space and the general Segre-image problem remain open. These are
written unreviewed results, with no changed matrix target frontier or
exponent below 9/4.

## Complete rank-six locus and sharp rank109 compression

The [rank-six classification](research/ai/2026-10-23-resolvent-rank-six-frontier/proof.md)
identifies the complete rank-at-most-six locus of the fixed-resolvent space
as a 17-dimensional linear space with a common six-dimensional image.
Twenty-six integer seven-minor identities expose a five-dimensional mixed
block, including an extra cancellation direction, and a four-dimensional
pure Q block. An elementary polynomial product-dimension argument proves
that two rank109 compression maps lose at most one dimension: the compressed
space has dimension at least111, sharply. Every nontrivial compression
kernel/image pair is parameterized in the proof. Exact controls attain
dimensions111 and112 over Q, F2, F3 and F1009. Claims
`AI-RESOLVENT-RANK-SIX-FRONTIER-001` and
`AI-RESOLVENT-RANK109-COMPRESSION-002` are written and unreviewed over every
field. Varying singular compressions and new Laurent leading coefficients
remain outside this result; no new matrix-target exclusion or exponent
improvement is established.

## Complete unbalanced ordinary square-sum frontier

The [unbalanced frontier](research/ai/2026-10-23-unbalanced-square-frontier/README.md)
applies the existing written rank gates to all82 cyclic source formats
2<=a<=b with N=ab(a+b-1)<=1377, all52310 target leg dimensions and
every square partition. All70 formats with N<1152 are excluded for an
improving ordinary square direct sum. The first necessary-test survivor
is A(8,9), N=1152; only it and A(9,9) survive the adopted gates
through1377. The later
[Wronskian application](research/ai/2026-10-21-hankel-wronskian-cap/application.md)
already excludes all improving ordinary A9 square direct sums; this
package preserves the earlier gate screen. The unbalanced
A(8,9) -> M30 target passes every adopted square-block gate. Its exact integer
score certificate would imply omega<=5621/2500=2.2484 if the missing maps
were constructed. An independent item-first recurrence checks every
saved dimension score. Claims `AI-UNBALANCED-SQUARE-FRONTIER-001` and
`COND-UNBALANCED-M30-001` retain written-unreviewed and conditional
status. Singular degenerations and rectangular direct sums are outside
the exclusion. No target or smaller exponent is established.

## Sharp Hankel pencil budgets at the nonlinear boundary

The [all-degree pencil family](research/ai/2026-10-23-hankel-index-sharpness/proof.md)
attains `(a+b-2r)*epsilon=r` for every positive integer annihilator degree
epsilon and every positive left and right nullity. Both polynomial kernels
are explicit over every field, and every projective member has the same
rank. In particular a 10-by-10 rank-eight pencil has minimal indices
`(2,2)` on both sides and annihilator `z^8-t*z^4+t^2`. Thus even constant
projective rank does not permit weakening the previous pencil-linearity
condition `5r<2(a+b)` to equality. This written unreviewed sharpness result
does not decide the Segre-image bound at equality, change the ordinary
matrix-target frontier or improve the exponent below 9/4.

The same package [classifies all linear extensions of this seed](research/ai/2026-10-23-hankel-index-sharpness/extensions.md)
in characteristic zero. The unique maximal space has dimension 2epsilon,
and every common tangent direction integrates inside that exact linear
space. At A10 it is the four-space supported at moments 3,7,11,15, with
ranks zero, four or eight. A linear Segre ruling containing the prescribed
pencil therefore has dimension at most four. Arbitrary quadratic pencils
and the general boundary Segre-image problem remain unclassified; these
are written unreviewed results.

## One-slice speedups of the exact paired seed

The [one-slice audit](research/ai/2026-10-23-one-slice-seed-audit/README.md)
applies Alman--Li's attributed speedup theorem to the previous integer
Q(5,4) seed. An explicit corner functional has raw rank 32 and compressed
rank 8. For every k>=1 it gives an actual complex degeneration from
`Q(5,4)^k plus J_(8^k)` to
`M(4^k,4^k,4^k) plus J_(8^k*(2^k-1)^2)`, with `J_s=M(1,s,1)`.
The square case has added J64 and extracted J576.

One appended one-slice tensor to a seed power and one-slice extraction
cannot exclude the existing feasible endpoint scalar profile. Every
resulting per-orientation scalar lower bound is below 37, while that
profile prescribes cyclic geometric mean `(910/81)^(3/2)>37`.
This comparison does not identify individual actual character values.
Multiple slices, successive extractions and other seeds remain outside
this ceiling. Claim `AI-ONE-SLICE-SEED-AUDIT-001` is written and unreviewed.
Six exact tests replay the complete seed, slice, cancellation, initial
kernels, formula controls, integer separation and source pins. The actual
degeneration follows from the imported theorem; no complete Laurent map,
actual endpoint character, or smaller exponent is supplied.
The [retained checkpoint receipt](results/one-slice-seed-audit-2026-10-23/validation.json)
records all 864 local tests and five archive replays at `42360e9`.
Three incomplete attempts are retained and excluded from that coverage.

## Ordinary repair from the diagonal of the first map

The [diagonal first-support proof](research/ai/2026-10-23-diagonal-first-support/README.md)
requires only the polynomial identity
`L(u u^T)=H(x,y)F(u)(x)G(u)(y)`, with fixed nonzero H and compatible
linear factors. Arbitrary long maps and arbitrary off-diagonal changes
that vanish on the diagonal are allowed. For Q(n,4) to M(n-c,4,n-c)
with residual first rank e, it gives
`e+max(tau(e)-6,q(e))>=max(0,n-5c-7)`, where tau is the largest
nonnegative integer d with d(d+1)/2<=e and q is the largest with
d(d+1)<=e. At n=200,c=1, first rank is at least 176, or 188 when both
diagonal factor maps are injective. The proof works over every field
by algebraic-closure descent. Claim `AI-DIAGONAL-FIRST-SUPPORT-001`
is written and unreviewed. The [follow-up receipt](results/first-support-capacity-2026-10-23/diagonal-followup.json)
records 37 passing checks at `26f4fb8`, including all eight new tests,
eight prior support-capacity tests, eighteen repository checks and three
archive-integrity checks. All 721 prior Python files are unchanged.
The combined 879-test inventory is discovery coverage; the complete
871-test run below remains attributed to its earlier checkpoint.
The injective shift-transpose control is a
first-map example, not a source-to-target construction. General first
maps, Laurent degenerations and linear repair costs remain open; no
smaller exponent is established.

## Repair support capacity and polynomial first maps

The [support-capacity proof](research/ai/2026-10-23-first-support-capacity/README.md)
gives a necessary first-support cost for repairing an actual tensor image
to M(l,h,r). It holds for arbitrary formal Laurent maps, including poles
that cancel between the source and the auxiliary image. The two long-map
annihilators force a union of row and column supports. Consequently an
auxiliary first rank below min(l,r) forces both source long maps to be
generically surjective. Fixed source widths below four require quadratic
first-support repair for M(n-c,4,n-c).

A separate ordinary theorem permits arbitrary long maps but assumes the
dual first map is H(x,y)F(u)(x)G(v)(y), with a fixed nonzero polynomial H.
Its residual first rank is at least both
`min(n-c,max(0,2n-10c-14))` and `max(0,2n-10c-19)`.
For c=1 it is at least n-1 once n>=23, and at least 371 when n=200.
Claims `AI-FIRST-SUPPORT-CAPACITY-001` and
`AI-POLYNOMIAL-FIRST-MAP-OBSTRUCTION-002` are written and unreviewed.
Eight exact-control tests pass. The [full regression receipt](results/first-support-capacity-2026-10-23/README.md)
records 871 passing tests across 204 modules at `66c4636`, with no skips,
and all five exact archive replays. The ordinary theorem does not cover
arbitrary first maps or Laurent degenerations, and it leaves linear
repair costs open. No smaller exponent is established.

## Complete SL(2,F8) subgroup cuts

The [complete F8 catalog](research/ai/2026-10-23-sl2-f8-subgroup-catalog/README.md)
certifies every averaging-ideal dimension for all386 subgroups in12
conjugacy classes. Order14 dihedral normalizers have dimension308 and
add1296 minimal forbidden cosets on every leg of all sixteen saved
coordinate/potential targets. Order6 subgroups have dimension455 and
add7056 cosets on ten of those48 legs. For M(18,18,25), the complete
minimal counts are3431,3431,2647. A control vertex set passes the prior
8,9,18 filters and fails the new14 filter. Independent extension closure,
integer projection identities, actual modular minors, and minimality/
coverage checks support claim `AI-SL2-F8-SUBGROUP-CUTS-001`, written and
unreviewed. These are necessary conditions; surviving constructions,
general complex maps and the exponent question remain open.

## Exact rational ranking for the monomial support search

The [maintained search](research/ai/2026-10-23-exact-monomial-search/README.md)
uses exact rational ordering and exports replayable zero-support, sector,
and block-recognition certificates. It preserves the first input leg as the
shared sector axis. The binary scope checks 12,976 candidates, the ternary
scope 209,692, and the seeded random scope 20,000; none has an exact score
above the source profile. The exact best ratio is 1 in all three scopes;
the random nontrivial best is 21/22. The historical search files remain
unchanged. Claim EXP-MONOMIAL-SEARCH-EXACT-001 is a finite experiment;
this relaxation does not establish an exponent improvement.
## Sharp rank six in the fixed-resolvent matrix space

The [fixed-resolvent certificate](research/ai/2026-10-23-resolvent-minrank/README.md)
proves that its 112-dimensional limiting matrix space has minimum nonzero
ordinary matrix rank exactly six over every field. Thirty-one triangular
six-by-six minor identities eliminate every parameter of the difficult
outer block, and an explicit rank-six witness proves sharpness. Thus every
two-sided compression with total rank loss at most five is injective.
At rank109 on both long maps, a lost direction must have rank six and obey
the stated kernel/image alignment. Claim `AI-RESOLVENT-SHARP-MINRANK-001`
is written and unreviewed; a first-party Codex audit found no gap in Sections
1--4, without changing its review status. See the
[scope-pinned audit](research/reviews/resolvent-minrank-proof-review-2026-10-23.md).
This refines the fixed-resolvent space from PR103; its narrow target application
is superseded by the regular-long-map
argument. The independently retained rank-six classifications now settle that
fixed-space locus, with their respective field and compression scopes.
General singular trajectories and an improved exponent remain unsettled.

## Three unbalanced single-rectangular survivors through dimension1377

The [complete unbalanced rectangular screen](research/ai/2026-10-23-unbalanced-rectangular-frontier/README.md)
applies the existing written source-rank and Hankel gates to all82
cyclic source formats2<=a<=b with N=ab(a+b-1)<=1377. It excludes2110
of2113 improving sorted single matrix shapes. Exactly three necessary-test
survivors remain, all from A(8,9), N=1152: M(28,31,31), M(29,30,31)
and M30. Their maps remain missing. Every exclusion has an exact
orientation and rank/dimension witness; independent interval enumeration
and certificate replay pass. Claim `AI-UNBALANCED-RECTANGULAR-FRONTIER-001`
is a written, unreviewed finite application of the credited prior proofs.
Rectangular direct sums and singular degenerations remain outside the
screen. The nonsquare survivors additionally require all rank-three
first parameters in selected orientations to have Hankel rank at most7;
M30 has the analogous rank-two constraint. A global symbol-dimension
consequence remains open. No target or smaller exponent is established.

## The adopted rank23 source cap gives normalized long-rank sum at most200

The [new rank-sum deduction](research/ai/2026-10-23-long-leg-rank-obstruction/torus_rank_sum.md)
adopts concurrent PR129's sharp source-space theorem: every linear A4
slice space with all matrix ranks at most23 has dimension at most eight.
If the two scalar-normalized long-map leading ranks summed to at least201,
the entire leading polar first-map image would lie in such a space.
Its target kernel would contain an invertible matrix, contradicting the
regular rank-two residual. Thus r_B+r_C<=200. With PR129's individual
bound, each rank is at most101. The additional excluded pairs are
(101,101), (101,100) and (100,101). Claim
`AI-A4-TORUS-LONG-RANK-SUM-005` is written and unreviewed.
The adopted proof is preserved byte-for-byte with its original attribution;
all finite matching-minor ingredients are reconstructed locally. Earlier
rank106 continuations and the separate rank20 classification are credited
in the concurrent-work note. Sum200 remains open, including (100,100).
No complete A4 exclusion or improved matrix multiplication exponent follows.

## The source rank gap lowers both A4 long-map rank budgets

The [rank-gap continuation](research/ai/2026-10-23-long-leg-rank-obstruction/README_gap.md)
excludes every complete A4 to M(10,10,11) Laurent degeneration with a
regular long map of limiting rank at least106. After independent scalar
normalization of both long maps, each leading rank is at most105 and
their sum is at most204. The proof permits arbitrary finite poles in the
other maps. It imports the prior 16-or-at-least-20 source slice-rank gap,
including its complex projective-line bundle-splitting dependency.
A direct rank-one-preserver argument supplies an invertible matrix in
the leading first-map kernel, contradicting the rank-two residual.
Claims `AI-A4-GAP-LONG-106-003` and `AI-A4-GAP-LONG-RANK-SUM-004` remain
written and unreviewed. Rank105 and sum204 are boundaries of these
arguments, not constructed degenerations. The simpler rank109 and
sum208 proofs are retained below with fewer structural dependencies.
No matrix target or smaller exponent is established.

## A4 long-map rank109 is also impossible

The [corank-one argument](research/ai/2026-10-23-long-leg-rank-obstruction/corank_one.md)
excludes every A4 to M(10,10,11) Laurent degeneration with either long
map regular and of rank at least109 at zero. It allows arbitrary finite
poles in both other maps. The rank110 regular-kernel argument is credited
to concurrent PR113. At rank109 its equality conditions force a fixed
four-dimensional source ruling; an invertible target matrix in the leading
first-map kernel contradicts the regular residual. Claims
`AI-A4-CORANK-ONE-LONG-001` and `AI-A4-NORMALIZED-LONG-RANK-SUM-002`
are written and unreviewed. A separate leading-pole argument requires
r_B+r_C<=208 after independent scalar normalization of both long maps;
each rank is at most108. Lower-rank pairs remain open. Exact controls do
not formalize the arbitrary-series proof, and no exponent is improved.

## Singular leading long-leg ranks106--109 are excluded by the source gap

The [singular-long-gap proof](research/ai/2026-10-23-singular-long-gap/proof.md)
extends the regular unit-kernel correction to long maps whose regular
limiting rank is at least106. The other two maps may have arbitrary
finite poles, with no original unit-lift hypothesis. A target rank-one
parameter lifts to source rank at most19; the existing16-or-at-least20
source gap forces minimum-rank leading images. Coherent-factor
propagation and a polynomial rank-one-preserver factorization, including
degenerate images, force an invertible matrix in the first-map kernel,
contradicting the unit-image rank budget. Claims
`AI-SINGULAR-LONG-GAP-001` and `AI-A4-LONG-RANK106-002` are written and
unreviewed. Exact controls export53 compression-kernel units and three
degenerate-kernel units, and check literal source ranks16 and20.
Flanders's complex matrix-space dimension bound is external and cited
with its exact version. Both scalar-balanced leading long-leg ranks
must be at most105 in any remaining candidate. No target, independent
review, formalization or exponent improvement is established.

## Highest-pole flags narrow the remaining regular unit images

The [highest-pole proof](research/ai/2026-10-23-unit-image-pole-flags/proof.md)
shows that at unit-image rank106 an A4 to M(10,10,11) degeneration in
the regular-full-long-map and regular-identity-lift chart must have a
first-map pole. Its highest coefficient has rank one to four and lies
in one minimum-rank source ruling, with fixed Hankel and one fixed short
factor; it annihilates the identity. Its complete principal part has rank
at least six and its pole order is at least two; every simple first-map
pole is excluded. Small principal parts give at most four polar long-map
terms, and the regular unit forces a source slice rank at least eight,
contradicting a rank-four correction. Complete principal rank6 remains
outside this method.
At image ranks102 through105, any
first-map pole has leading image dimension at most16 and a fixed Hankel
factor. Claim `AI-UNIT-IMAGE-LEADING-POLE-FLAGS-001` is written and unreviewed,
using the credited source rank-gap and below-twice-minimum classifications.
Exact controls also retain a rank106 block-budget survivor; no compatible
unit trajectory or full target is claimed. Lower poles, these remaining
image ranks and the exponent goal remain open.

## One-sided unit compression excludes image ranks107 and108

The [one-sided unit-image proof](research/ai/2026-10-23-one-sided-unit-image/proof.md)
strengthens the preceding partial-unit regularity theorem. Keeping every
target row gives the rank margin `nu-e>q`; using the original full long
map gives the dimension margin `D>dim(A)-mu_B+k`, where `k=N-R` and
`q=N-r=k+e`. Together with `mu_A>3q`, these force both Laurent maps to
be regular at every finite pole order. For A4 to M(10,10,11), unit-image
rank at least107 gives strict margins1,3,2 and reduces to the existing
ordinary rank contradiction12>11. A regular unit slice of corank at most
three is included. Claims `AI-ONE-SIDED-UNIT-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-107-002` are written and unreviewed; exact controls check
the rank losses and the failed sufficient test at rank106. Unit-image
rank at most106, singular long-leg limits and polar identity lifts remain
open. No target construction or exponent improvement is established.

## A projective fifteen-space inside the rank-six locus

The [rank-six family continuation](research/ai/2026-10-23-resolvent-rank6-family/README.md)
exhibits a sixteen-dimensional subspace of the fixed-resolvent space whose
every nonzero element has rank six over every field. This gives a `P^15`
inside the rank-six locus, not its full classification. For each family member, the
rank-loss-six compression alignment is realizable by constant rank-109 maps;
their product is necessarily singular, and this is not a tensor degeneration
or target. Claim `AI-RESOLVENT-RANK6-FAMILY-001` is written and unreviewed.

## Coordinate projections strengthen existing monomial scores

The [projection recurrence](research/ai/2026-10-23-monomial-projections/proof.md)
computes the exact optimum of the existing component score over y/z
coordinate deletions, retaining the shared x axis. Complete ordered binary
censuses through a+b=8 and 9 improve 581 of 1,623 and 1,817 of 4,197 scores;
the ternary census through a+b=8 improves 6,486 of 24,699. Every maximum
ratio remains one. Literal masks raise one old support's score from 3 to 5,
below the source 56/9. The acceptance checker replays the support without
calling the optimizer, and all 64 supports of a 2-by-3 grid agree with
direct enumeration of every pair of masks. Claims
`AI-MONOMIAL-PROJECTION-OPT-001` and `EXP-MONOMIAL-PROJECTION-CENSUS-001`
separate the written, unreviewed finite proof and the finite census.
This strengthens estimates on existing degenerations; general linear
restrictions and the exponent goal remain open.

## Whole-convolution recognition is complete under coordinate permutations

The [additive-support proof](research/ai/2026-10-23-monomial-recognition/proof.md)
shows that the archived monomial recognizer misses no whole convolution
sector that independent coordinate permutations could recover. A monotone
lattice path proves that the output cardinality and term count force the
sorted-index sum rule. Claim `AI-ADDITIVE-SUPPORT-RECOGNITION-001` is written
and unreviewed. Stronger proper restrictions, additional degenerations and
general linear bases remain separate questions. The score shares its first
input: already at dimensions (2,3), swapping inputs changes 13/14 to 9/14.
The [complete ordered census](research/ai/2026-10-23-monomial-recognition/README.md)
checks 24,708 binary and 370,252 ternary candidates at the archived dimension
cutoffs, including a>b. Both maximum ratios are exactly one, with no exact
violation; 8,742 and 118,604 unequal-dimension pairs have different orientation
scores. Claim `EXP-ORDERED-MONOMIAL-CENSUS-001` is a finite experiment with
the archived whole-convolution/slice-fallback score. No all-weight obstruction
or exponent improvement follows.

## A4 long-map limits must lose at least five ranks

The [singular-long-rank proof](research/ai/2026-10-23-singular-long-rank/proof.md)
excludes A4 to M(10,10,11) whenever either scalar-balanced long map has
limiting rank at least 106. Both other maps can have arbitrary finite
Laurent poles; no hypothesis on the target-unit lift is needed. The
regular kernel correction credited to PR113 combines with the existing
source rank gap: an active target ruling would inject ten dimensions
into the source's minimum-rank cone, which cannot contain that linear
space. Claim `AI-A4-SINGULAR-LONG-RANK-001` is written and unreviewed.
Exact controls check eight literal source slices, including a rank-20
boundary witness, and the strict singular-column and ruling budgets.
This first checkpoint gave the rank105 boundary; the later rank102
and sum176 results above further restrict the surviving candidates.
This supersedes the regular-unit hypotheses in the earlier scoped
exclusions below. No matrix target or smaller exponent is established.

## Finite and quantified repair criteria from residual ranks

The [residual-rank proof](research/ai/2026-10-23-residual-rank-repair/proof.md)
gives a finite paired-source criterion and a larger quantified repair class.
One genuine degeneration from Q(n,b) plus residual E to M(l,h,r) would suffice
when `(lhr)^(3/4)>D(E)^(3/4)+sqrt(2b(2n+b-1)^3)/3`, where D is the smallest
product of two residual flattening ranks. The minimum largest source leg
among full targets passing this paired criterion is 441, at Q(21,8) and
Q(21,9). Width four first passes without error at n=38 for full outer
dimensions, and at n=64 for outer deficit one.

An unbounded near-full family with first residual rank O(n^gamma), long
ranks O(n), and gamma<1 implies
`omega<=max(B_b,9/4-(1-gamma)^2/4)`. At gamma=7/10 and b=4 this retains
the previous conditional bound below 2.2334, despite a crude scalar-rank
cost O(n^1.7). All needed maps remain missing. Claims
`AI-RESIDUAL-RANK-FINITE-GATE-001` and
`AI-RESIDUAL-RANK-ASYMPTOTIC-GATE-002` are conditional and unreviewed.
Exact arithmetic certifies these search criteria, not tensor constructions.

## A repair-cost barrier for the existing formal calculus

The [operational-repair proof](research/ai/2026-10-23-operational-repair-barrier/README.md)
applies the new external monotones of Amanov, van den Berg and Zuiddam.
Within their specified formal calculus, a near-full fixed-width target
requires more than `O(n^alpha)` scalar repairs for every fixed `alpha<2`.
For fixed outer defects, the necessary lower bound is
`liminf s_n ln(n)/n^2 >= ln(b^2/(2b-1))/e`.
The proof also permits quantified outer defects of order `n/ln n`.
At width four, its coefficient lies between
`0.304118051531` and `0.304118051532`.
The coefficient is optimal over the entire external F_theta family,
including parameters approaching simplex boundaries and corners. A uniform
finite upper envelope also proves sharpness with convergent logarithmic
outer loss. This concerns certificate strength, not repair attainability.

Claim `AI-OPERATIONAL-REPAIR-BARRIER-001` is written and unreviewed.
Integer and rational calculations verify finite inequalities and control cases.
They do not verify tensor maps. The imported functions need not be actual
tensor invariants, so this result does not exclude arbitrary degenerations.
The actual construction target remains open, and no smaller exponent is established.

The [validation receipt](results/paired-repair-2026-10-23/validation.json)
records all 875 tests passing with no skips at commit `121be1c`, plus all
five exact archive replays. One incomplete test-process attempt was
excluded from coverage and replaced by a complete successful rerun.
Both research archives remain unchanged. Current-head hosted checks are
still required before merging PR130; these checks do not change the
mathematical review status. Main `3008d70` is integrated with the prior
Python implementation unchanged. Its five new tests and eighteen metadata,
profile and support checks pass; the integration receipt preserves the
distinction between this check and the earlier full regression.

## Every pair of balanced A4 leading ranks has total at most192

The [simple-source-torus argument](research/ai/2026-10-23-coordinate-kernel-cap/torus_reduction.md)
transfers the complete coordinate matching cap to arbitrary complex
compression kernels. Simultaneous kernel limits retain their dimensions
and can only lower the projected first rank. The literal source torus has
112 distinct weights on every leg and preserves all4096 source terms.
Together with the prior dense regular-leg screen, this closes all sixteen
mixed high-rank pairs: every two regular target-leg maps have rank sum at
most192, allowing arbitrary later jets and a Laurent third map. Individual
scalar balancing gives the same bound on every pair of leading ranks in
any Laurent presentation. Their total is at most288; short leading rank100
forces both long leading ranks at most92. Claim
`AI-A4-DENSE-REGULAR-PAIR-003` is written and unreviewed. Finite source-weight,
matching and noncoordinate rank-drop controls support the proof without
formalizing it. Lower rank triples and the target remain unconstructed;
no exponent improvement is established.

## Coordinate leading kernels close the mixed high-rank regular pairs

The [coordinate-kernel certificate](research/ai/2026-10-23-coordinate-kernel-cap/proof.md)
closes all sixteen high-rank mixed pairs of the standalone regular-leg
screen when both regular constant maps have coordinate kernels. Any such
regular pair has limiting ranks summing to at most192. The matching
census covers all8008 ten-cell biform subsets:7744 have25 disjoint source
edges, and264 have a uniquely forced24-vertex cover entirely on one side.
These exceed the candidate deletion budgets and force projected source
rank at least103, above target ceilings102 and101. Higher jets and the
remaining Laurent map are unrestricted. Claims
`EXP-COORDINATE-COVER-CENSUS-001` and `AI-A4-COORDINATE-REGULAR-PAIR-002`
are respectively finite evidence and a written unreviewed deduction.
Noncoordinate leading kernels and smaller rank pairs remain outside this
argument. No target or exponent improvement is established.

## A rank budget for two regular A4 target legs

The [regular-leg frontier](research/ai/2026-10-23-regular-leg-frontier/proof.md)
shows that any A4 to M(10,10,11) degeneration with both long maps regular
must have limiting long-map ranks summing to at most192, a total rank loss
of at least28. The third map may have arbitrary Laurent poles and both
regular maps may have arbitrary higher jets and complex mixing. The proof
combines the prior low-rank source locus with the saturated target-support
condition, without selecting a unit lift. With one short and one long
regular map, the same tests leave sixteen explicit rank pairs of total
rank at least193. Ten coordinate compressions, five strict-threshold
controls and23532 integer rank pairs replay exactly. Claims
`AI-REGULAR-COMPRESSION-KERNEL-001` and `AI-A4-REGULAR-LEG-FRONTIER-002`
are written and unreviewed. Scalar balancing extends the long-pair budget
to every Laurent presentation, forcing at least one balanced long leading
rank to be at most96. Lower-rank pairs remain open. No target or smaller exponent is established.

## Exact rank minimum in the binomial supporting chart

The [binomial-chart proof](research/ai/2026-10-23-hankel-additive-cost/proof.md)
determines the exact nonzero source-slice minimum for f_(k+r)=xz*f_k,
over every field and all polynomial initial moments with the source
bidegree bounds. Residue components give exact basis ranks and identity
minors; a diagonal monomial limit supplies the general minimum. The
balanced closed formula sharpens the additive cost by an explicit
nonnegative cyclic-convolution term. Claim
`AI-BINOMIAL-SUPPORT-CHART-MINIMUM-001` is written and unreviewed.
Controls include 426 feasible seeds, 19 full literal certificates and
1711 balanced formula cases. Arbitrary other degree-one supporting
forms, matrix-target constructions and the exponent goal remain open.

## Primitive annihilator degrees widen the pointwise strip

The [degree-count proof](research/ai/2026-10-23-hankel-annihilator-degree/proof.md)
gives the exact two inner polynomial coefficient-map ranks from the
primitive x and z degrees of the supporting form. For scalar symbol rank
r<min(a,b), source rank below ab*r+min(a(a-r),b(b-r)) forces one constant
length-r scheme. A balanced family attains the boundary for every
2<=r<a. Twenty-four exact controls cover wider deficiencies, unbalanced
formats, higher degrees and both-variable motion. Claim
`AI-HANKEL-ANNIHILATOR-DEGREE-001` is written and unreviewed. This does
not strengthen the width at A9 rank eight, make schemes constant over
matrix parameters, or establish a target or smaller exponent. A separate
[additive-cost question](research/ai/2026-10-23-hankel-annihilator-degree/additive_question.md)
retains an unproved sum bound, an exact two-variable boundary family
at r=n-1, and a forty-case finite recurrence pilot with zero violations.
Claims `AI-HANKEL-ADDITIVE-BOUNDARY-001` and
`EXP-HANKEL-ADDITIVE-PILOT-001` retain those distinct evidence tiers.

## A sharp constant-scheme strip at deficient Hankel rank

The [kernel-descent proof](research/ai/2026-10-23-hankel-equality/proof.md)
extends the earlier rank-two equality containment: for scalar Hankel rank
r<min(a,b), source slice rank below ab*r+min(a,b) forces one constant
length-r supporting scheme for every coefficient sequence of that slice.
A moving-scheme family reaches the strict boundary for every r>=2.
Exact controls include saturated ranks one through eight, excess-one
examples, reduced and nonreduced schemes, and endpoint and full-rank
warnings. Claim `AI-HANKEL-CONSTANT-SCHEME-STRIP-001` is written and
unreviewed. Constancy over a whole matrix-parameter family remains
unproved; no new matrix-target exclusion or smaller exponent follows. The
historical ordinary A9 square sums are already excluded by the credited
Wronskian application.

## The mixed candidate is excluded by rational-normal-curve rigidity

The [global geometric proof](research/ai/2026-10-23-mixed-longlegs-candidate/global_rnc_obstruction.md)
excludes every complex degeneration from the canonical ten Full(5,10)
source to the frozen mixed target, even with arbitrary independent first
identifications of its blocks. All three maps may initially have poles
or singular leading terms, and the long maps may mix source copies.

Third conciseness gives a regular family of third-slice spaces. Proper
rank-one incidence forces the moving source rational normal quartic to
limit inside the target's finite union of smooth quartics. Its degree and
Hilbert polynomial force one reduced smooth quartic. Smooth orbit lifting
and the source's binary substitution symmetry then produce an equivalent
degeneration with an invertible regular first map. The already proved
catalecticant comparison120<130 contradicts that normalized degeneration.

The earlier Koszul and Schur screens still pass; the new proof uses
additional geometry. It excludes this source orbit closure, not every
border-rank140 realization of the target. The next construction must
escape the finite-quartic projection hypothesis, for example through
width-one Full blocks or a different target structure. This is a written
proof with same-session audits and exact convention checks, without
external independent review, formalization or an improved exponent.

## Mixed target: exact rank178 and a first-map chart obstruction

The [canonical mixed target](research/ai/2026-10-23-mixed-longlegs-candidate/cactus_rank.md)
has ordinary, smoothable and cactus rank exactly178. A low-rank evaluation
curve gives the lower bound and rational interpolation gives the upper
bound. Independent first identifications still give cactus rank at
least168. These are finite-scheme ranks; target border rank140 remains
possible from this argument alone. A small canonical (2,3,3) control has
border rank3 but cactus rank4 and prevents that distinction being lost.

The [middle catalecticant](research/ai/2026-10-23-mixed-longlegs-candidate/catalecticant_chart.md)
has source rank120 and target rank at least130 after every independent
invertible first identification. Its covariance on the two long factors
excludes every degeneration with an invertible scalar-normalized first
limit, even when the long maps have poles and mix source copies. The
singular first limits are now settled for the frozen target by the global
rational-normal-curve proof above. These written proofs and exact controls have same-session audits, without
external independent review or any matrix multiplication exponent gain.

## A mixed-output candidate survives every ordinary Koszul degree

The [frozen candidate](research/ai/2026-10-23-mixed-longlegs-candidate/README.md)
compares ten Full(5,10) source blocks with seven Full(5,2), ten Full(5,3),
four shared-output O(3,3), two O(4,2), and six Mid(5,2) blocks. Both
canonical tensors have format (5,100,140). An exact rational certificate
proves a strictly larger symmetric formal operational score for the target.
Every ordinary Koszul degree on all three legs passes. Both symmetric-power
families and all quantum and upper support bounds also pass.

The [source B-leg proof](research/ai/2026-10-23-mixed-longlegs-candidate/source_b_koszul.md)
computes every exterior and simultaneous tensor-power contraction rank
of a canonical shared-first sum of Full blocks. Exact target computations
settle the nonautomatic degrees. The
[Schur-component check](research/ai/2026-10-23-mixed-longlegs-candidate/schur_screen.md)
also passes every component of that contraction family.
The [source C-leg theorem](research/ai/2026-10-23-mixed-longlegs-candidate/source_c_koszul.md)
proves that every zero-free bilinear tensor in the stated format has the
same output-leg Koszul ranks, which are the largest attainable ranks in
that format. Thus no target of this format can fail a C-leg comparison
against this source, even after arbitrary target basis changes.

These results settle the stated necessary tests. The computed B-leg and
Schur target ranks use the canonical target first bases. The global RNC
proof above now excludes the proposed source-target degeneration under
all independent target first identifications. It does not determine
target border rank. No improving tensor degeneration or smaller exponent
has been established. The written
proofs and finite experiments remain without external independent review.

## Sharp onset of paired long-leg kernels

The [fixed-short-direction proof](research/ai/2026-10-23-paired-kernel-onset/proof.md)
makes the paired long-leg full-column interval sharp over every field.
Fixing one short input coordinate gives a complete restricted kernel
formula. Padding and summing its independent coordinate input spaces
gives a full-source kernel lower bound and therefore a rank upper bound
in every degree. At p=a(a-1)+1 the kernel has dimension at least
a binom(a(a-1),a-1)>0; the restricted construction remains nonzero in
every later degree. Claim `AI-PAIRED-KERNEL-ONSET-002` is written and
unreviewed. The full coupled source kernel remains unresolved.

The [cokernel Euler calculation](research/ai/2026-10-23-paired-kernel-onset/cokernel.md)
gives a second all-degree source rank upper bound. Throughout the remaining
intermediate interval, the exact missing term is h^1 of the filtered
kernel bundle, with every other term explicit. Three matching literal
modular ranks certify exact complex ranks 70,18819,6660 at
(a,p)=(2,3),(3,10),(3,11). Claim `AI-PAIRED-COKERNEL-EULER-004` is
written and unreviewed; the extension maps remain unresolved.

An [exact bound screen](results/paired-kernel-onset-2026-10-23/target-screen.json)
makes 25,254 rank comparisons on the pinned 28-target frontier through
a=16. It settles 2,970 intermediate-degree comparisons beyond the two
full-rank intervals as incapable of excluding a target. No target is
excluded; remaining comparisons are undecided. Claim
`EXP-PAIRED-LONG-BOUND-SCREEN-003` is a finite experiment. No target
construction or smaller exponent follows.

## A quadratic full-rank interval on paired long legs

The [paired-long-leg proof](research/ai/2026-10-23-paired-bundle-injectivity/proof.md)
shows that both long-leg Koszul maps of P_a, with the short leg as input,
are injective over every field for every a>=2 and 0<=p<=a(a-1).
Their rank is a^2 binom(a(2a-1),p). A full-rank Hankel calculation and an
explicit filtered bundle on the projective line prove the all-size
statement; finite coefficient controls are retained separately.
Claim `AI-PAIRED-LONG-LEG-INJECTIVITY-001` is written and unreviewed.
The same bundle argument gives full row rank for N-a<=p<=N, N=a(2a-1),
and an explicit all-degree upper bound on the kernel dimension.

These degrees cannot exclude any dimension-compatible padded target.
For the 28 short-leg survivors through a16, a new long-leg exclusion
requires p in [183,363], [211,419], [241,479] at a14,15,16.
Those intermediate degrees remain open; the kernel bound gives a source
rank lower bound and cannot itself exclude a degeneration.
An integer kernel and modular rank70 witness certify the exact complex
rank70 at a2,p3, beyond the proved interval. No target is constructed and
no exponent is improved.

## Sharp rank20 linear spaces and singular long-map rank105

The [all-size extension](research/ai/2026-10-23-rank20-ruling/all_sizes.md)
proves the analogous classification for every square source A_a, a>=2:
rank at most a^2+a means a coherent middle factor and an outer biform
with a divisor of degree a-2 in x or z. The sharp vector linear-space
bound is2a. This gives a uniform Laurent ruling obstruction; selected A5
target long-rank thresholds are216,212,210 for M(13,13,17), M(14,14,16),
M(15,15,15), respectively. Claim `AI-FIRST-GAP-LINEAR-SPACES-003` is
written and unreviewed. Selected-size exact controls cover331 possible
splitting triples/tuples, sharp source spaces at a2,3,5 and four target
margin examples. They do not prove the all-size quantifiers.

The [rank20 classification](research/ai/2026-10-23-rank20-ruling/proof.md)
gives a sharp vector linear-space dimension bound eight for A4 source
slices of rank at most20. After fixing the coherent middle factor, the
biform has a quadratic divisor in x or in z. A generic-pencil common-factor
argument controls linear spaces whose divisor may vary; a fixed quadratic
times the full bidegree(1,3) or(3,1) space attains dimension eight.
The shared-correction ruling criterion below therefore excludes either
balanced long-map leading rank at least105 in A4 to M(10,10,11), allowing
arbitrary finite poles in both other maps and in the original unit lift.
At c105 the source cap is20 and8<10, with nonzero-lift margin7. Claims
`AI-A4-RANK20-LINEAR-SPACES-001` and `AI-A4-SINGULAR-LONG105-002` are
written and unreviewed. The source splitting formula, its Grothendieck
dependency and the prior correction criterion retain their original credit.
Exact controls check eight dimension-eight source spaces,24 actual source
ranks,22 possible splitting-degree triples and generic-pencil hypotheses.
At c104 the cap is21 and the new dimension bound is not asserted.
Remaining candidates have both balanced long-map leading ranks at most104.
No constructed target, independent review or smaller exponent is established.

## Singular long-leg limits and a shared correction ruling test

The [shared-correction ruling argument](research/ai/2026-10-23-singular-long-ruling/proof.md)
excludes the canonical A4 to M(10,10,11) degeneration if either
scalar-balanced long map has leading rank at least106. Both other maps,
including the original identity lift, may have arbitrary finite poles.
This extends concurrent PR113's regular full-rank long-leg premise to
singular limits. Its rank-two regular kernel corrections share one
constant column space. After quotienting by that space, a nonzero unit
image would make a ten-dimensional target ruling inject into a source
minimum-cone linear space of dimension at most four. The prior source
rank gap16 to20 applies because the c106 source cap is19. Claims
`AI-SHARED-KERNEL-RULING-001` and `AI-A4-SINGULAR-LONG106-002` are written
and unreviewed. The gap's Grothendieck splitting dependency and all prior
source credits are retained. Exact finite controls check shared corrections,
target rulings and actual source ranks16/20. At c105 the cap reaches20,
so the adopted minimum-cone argument stops. Both balanced long limits
must have rank at most105 in any remaining candidate; existence and the
full target remain open. No smaller exponent is established.

## Sharp divisor-strip source caps at every balanced size

The [divisor-source proof](research/ai/2026-10-23-divisor-source-caps/proof.md)
extends the A4 torus method to every proper positive divisor d of every
balanced size a. For each integer rank ceiling q with
`a(a+d-1)<=q<a(a+d)`, the largest dimension of an arbitrary complex
linear source space whose slices have rank at most q is exactly ad.
Divisor cycles bound a coordinate specialization; a literal d^2-block
decomposition imports the prior biform rank gap. A d-row strip attains
the cap. Claims `AI-DIVISOR-SOURCE-CAP-001` and
`AI-DIVISOR-LONG-EXCLUSION-002` are written and unreviewed. Exact controls
check110 minors,330 residue identities and60 divisor/strip cases.
The all-size long-leg corollary recovers the prior A4 rank102 exclusion;
no new A4 frontier or exponent improvement is claimed. The earlier
block lemma retains its P1 bundle-splitting dependency and original credit.

## Single-copy mixed-sector termwise incidence screen

The [twisted-cubic subset screen](research/ai/2026-10-23-mixed-family-twisted-cubic-screen/RESULT.md)
computes all 120 seven-point subsets of the ten displayed `T4` interpolation
factors over the rationals. Their quadratic evaluation matrices all have
rank 7; 68 subsets have fewer than two linear syzygies among their three
common quadrics. Every eight-point set contains such a subset. A projective
limit of the source evaluation curves retains at least two linear syzygies,
so at most seven displayed target factors can be limits of distinct source
evaluation factors under one common shared-space change of basis. Claim
`AI-MIXED-SINGLE-COPY-002` is written and unreviewed. This does not exclude a
general degeneration, cancellations, collisions or other target
decompositions, and does not improve the exponent. A specified seven-point
subset lies on a Hilbert-Burch flat-limit curve, so point-set curve
containment alone cannot strengthen this count; its evaluation-node
parameters are not aligned by that example. Every seven-set passing the
syzygy screen contains a collinear triple, so no such set lies on a smooth
twisted cubic; seven-point candidates require a singular special fiber.

## Fixed long-leg coordinates force a quadratic Q(n,4) correction

The [all-size flattening proof](research/ai/2026-10-23-q64-diagonal-shift/proof.md)
shows that one explicit set of maps from `Q(n,4)` leaves a correction
whose first-leg flattening rank is `n^2`. The proof projects the
`(0,0)` and `(1,1)` inner-coordinate blocks; every resulting diagonal
block is nonsingular modulo two. The standard-library replay reconstructs
the literal tensors and checks the block formula and rank for `n=1,...,12`.
Claim `AI-Q64-DIAGONAL-SHIFT-CORRECTION-001` is written and unreviewed.
This excludes only the displayed maps from an `O(n)` correction route;
general `Q(n,4)` maps remain open. The exponent remains unchanged.

The [fixed-long-leg extension](research/ai/2026-10-23-q64-coordinate-long-legs/proof.md)
allows an arbitrary linear map on the first leg. With the two coordinate
long-leg maps fixed, the correction's first-leg flattening rank is exactly
`n^2` for every such map. Two projected inner-coordinate blocks force
kernel vectors to be constant along diagonals, and the boundary rows force
them to vanish. This proof remains unreviewed and does not cover changes to
either long-leg map.

The [inner-index shift family](research/ai/2026-10-23-q64-inner-shifted-coordinates/proof.md)
covers all size-dependent multipliers `0<=k_B,k_C<n` on the two long
legs. For every first-leg map the correction flattening rank is at least
`n^2/2` for `n>=4`: high multipliers leave the matched `j=2` target block
unsupported by the source, and low multipliers satisfy the off-diagonal
support bound. This closes the full inner-index proportional shift family.

The [arbitrary inner-shift continuation](research/ai/2026-10-23-q64-arbitrary-inner-shifts/proof.md)
allows independent integer coordinate translations on every inner index
of both long legs. For every first-leg map its correction flattening rank
is at least `n(n-1)/2` for every n. The proof splits on adjacent C-shift
differences and remains unreviewed; general linear long-leg maps remain open.

The [matched-window permutation result](research/ai/2026-10-23-q64-window-permutations/proof.md)
allows an independent permutation of every length-n matched coordinate
window on both long legs. Every first-leg map leaves correction flattening
rank at least `(n-1)^2`. Its written proof and exact finite replay remain
unreviewed.

## Asymmetric boundary support and auxiliary product reductions

The [asymmetric reduction](research/ai/2026-10-23-asymmetric-boundary/proof.md)
proves a universal auxiliary split on the complete100-dimensional
full-side normal kernel. A nonzero rank-four obstruction forces the
smaller eight-dimensional first span to be H tensor C2 for a four-plane H.
Separately, both joint supports of every non-plane core in the preceding
28-dimensional joint-zero family have dimension at least three, certified
by two complete cubic coefficient determinants. A sharp one-sided
zero-or-four projection gap then excludes this joint-zero branch from
the12-by8 target third-rank ceiling. The nonzero rank-four branch and the
full asymmetric problem remain open. Claims are written and unreviewed;
no exponent improvement or full target construction is established.

## Border rank at least twelve for the fixed oblique residual

The [long-leg equalizer proof](research/ai/2026-10-23-oblique-border-equalizer/proof.md)
raises the full n=6,b=4 residual's border-rank lower bound from eleven
to twelve. The current complex interval is `12 <= border_rank(E) <= 18`,
alongside exact ordinary rank nineteen. For the one-dependency family
`b>=2,n=b+2,r=b+1`, the same coefficient argument gives lower bound
`2r+2` over every characteristic. The established pairwise symmetry
condition requires at least `m` equalizing endomorphism pairs at border
rank at most `m=2r+1`; this residual has exactly two. A unit minor of
order 240 certifies the n=6 calculation for the actual exported tensor.

Claim `AI-OBLIQUE-BORDER-EQUALIZER-001` is written and unreviewed.
Seven focused standard-library tests check eight family controls, four
source hashes, the full native identity and deliberate false certificates.
The previous maps, implementations, tests and source pins are unchanged.
The lower bound concerns the fixed residual; optimal border rank,
improvements from other maps and a smaller exponent remain open.
The [follow-up receipt](results/oblique-repair-2026-10-23/equalizer-followup.json)
records 35 completed incremental checks at `2c1e026`, including all seven
added tests, plus a standalone certificate replay. All 734 prior Python
files remain unchanged. The combined 910-test inventory is discovery
coverage; the complete 884-test regression remains attributed below.

## Exact ordinary rank nineteen and an eighteen-scalar degeneration

The [full-residual rank proof](research/ai/2026-10-23-oblique-border-repair/full_residual_rank.md)
shows that the existing product-oblique residual has ordinary rank exactly
`4r-1` whenever `b>=2,n=b+2,r=b+1`. Two support projections remove
`2(r-2)` terms each from every proposed decomposition, leaving the core
of rank seven. The inherited ordinary construction attains this bound
over every field. Thus the full n=6,b=4 residual has ordinary rank
exactly nineteen; the separate equalizer follow-up above places its
complex border rank between twelve and eighteen. This ordinary optimality
concerns the fixed residual, not arbitrary
source maps. Claim `AI-OBLIQUE-FULL-ORDINARY-RANK-004` is written and
unreviewed. Seven focused tests check eight family controls, unit support
minors, the complete exported source contraction and false certificates.
The middle first-leg Koszul rank has structural ceiling 504, so that
test cannot certify optimal border rank eighteen.

The [validation receipts](results/oblique-repair-2026-10-23/README.md)
record complete 871-test and 884-test regressions at the ordinary and border
checkpoints, each with all five archive replays and no skips. After integrating
the full-rank proof, long-map frontier and main `3008d70`, all nineteen added
tests and forty-four related or repository checks pass. All 728 prior Python
files are unchanged. The combined 903-test inventory is not a fresh full run;
current-head hosted CI remains required.

## A surjective benchmark and the fixed-good-row frontier

The [long-map frontier](research/ai/2026-10-23-oblique-longmap-frontier/README.md)
gives integer Q(6,4) maps with both long maps surjective and minimum first
residual rank nine. Its displayed residual has rational ranks `(9,18,18)`;
this is a search benchmark, not a lower scalar repair cost. A determinant-one
projected source minor proves that arbitrary fillers in the four added
output rows cannot reduce first residual below nine when the sixteen good
rows on each long leg remain fixed. This lower bound holds over every
field and for every first map. Equality is asserted for the benchmark,
not for arbitrary fillers. Claim `AI-OBLIQUE-FILLER-SCOPE-001` is written
and unreviewed.

The separate finite screen checks 384 specified inner-dependent shift
pairs and 61 nonsingular mixed-middle corners from an 81-point grid.
All 384 quotient-rank minors give rational first residual lower bound nine.
Every valid corner retains an injective thirty-six-dimensional source
first-slice projection; 20 singular modular decoders are skipped.
Claim `EXP-OBLIQUE-LONGMAP-FRONTIER-002` is a finite experiment.
Seven standard-library tests replay the complete compact certificate,
five source hashes and deliberate changes or omissions. These scoped
results leave unrestricted long maps and general degenerations open.
The ordinary nineteen-term and border eighteen-term repairs below remain
unchanged; no smaller exponent follows.

## An eighteen-scalar degeneration from a six-term core

The [polynomial border repair](research/ai/2026-10-23-oblique-border-repair/proof.md)
keeps the ordinary oblique maps and constructs
`Q(6,4) + D_18` degenerating to `M(5,4,5)` over every field.
All three polynomial local maps replay the complete identity
`t^2(1-t)(M+tH)`. The complex residual has border rank at most eighteen,
alongside the exact ordinary rank nineteen above. Its small
three-by-five-by-five core has border rank exactly six: six polynomial
terms supply the upper bound, and an eleven-by-eleven Koszul minor with
determinant one supplies the lower bound.

The separate [ordinary-rank proof](research/ai/2026-10-23-oblique-border-repair/ordinary_rank.md)
shows that this isolated core has ordinary rank exactly seven over every
field. Its quadratic left and right polynomial kernels reduce every
hypothetical six-term decomposition to two support patterns. A mixed-block
functional and a unit slice minor exclude those patterns. Six focused
tests replay the proof's explicit integer inputs, check agreement with the
border core, and reject changed products and false certificate entries.
Claim `AI-OBLIQUE-CORE-RANK-SEVEN-003` is written and unreviewed.
The full-residual result above additionally uses two support projections.

Disjoint cores give ordinary correction bound `4rd-m^2` and border
correction bound `4rd-2m^2`, where `r=n-1`, `d=r-b` and
`m=min(d,b-1)`. Width-four border costs are eighteen, forty, sixty-six
and one hundred ten at n=6,7,8,9. Seven focused tests replay the core,
complete source maps, all seventy-two saved family records, four source
hashes and deliberate false certificates. Claims
`AI-OBLIQUE-CORE-BORDER-SIX-001` and `AI-OBLIQUE-BORDER-REPAIR-FAMILY-002`
are written and unreviewed. No optimal border rank for the whole residual
or eighteen-term ordinary decomposition is asserted. The fixed-width
repair remains quadratic and no smaller exponent follows.

## Explicit oblique maps with a nineteen-scalar repair

The [integer oblique construction](research/ai/2026-10-23-oblique-paired-repair/proof.md)
gives `Q(6,4) -> M(5,4,5)-E` with exact residual ranks `(9,11,11)`
and nineteen replayed rank-one correction terms. The previous embedded
M4 comparison has ranks `(9,20,20)` and thirty-six naive scalar terms.
The product witness's three pieces have ranks `(4,2,8)`, `(4,8,2)`,
and `(1,4,4)`. A separate nonproduct-middle integer witness has the
same global ranks and a verified twenty-four-term correction.

The all-size product family has residual ranks `(r^2-b^2,2r+d,2r+d)`
for `r=n-1`, `d=r-b>0`, with `4rd` scalar terms and a `4r-1` refinement
when `d=1`. All formulas and scalar identities hold over every field.
These changed long maps attain their own exact minimum first residual
rank; at n=6 that minimum is nine, compared with sixteen for the old
long maps below. Claims `AI-OBLIQUE-PAIRED-REPAIR-001` and
`AI-OBLIQUE-NONPRODUCT-CONTROL-002` are written and unreviewed.
Seven focused tests replay the complete identities, saved certificates,
support factorizations, scalar terms, and distinct variant costs.
The fixed-width family has quadratic first support and does not supply
the small asymptotic repair required for an exponent improvement.
The [pending PR130](https://github.com/1337isnot1337/matrix-mult-bounds/pull/130)
endpoint criterion is used only for a pinned cost comparison; even its
zero-residual finite gate fails at this source and target.

## The first map cannot repair the fixed product long maps

The [product-longmap residual proof](research/ai/2026-10-23-product-longmap-residual/README.md)
computes the exact minimum first residual rank when both existing product
long maps are fixed and the first map is arbitrary. For every `n>=5` in
characteristic different from two, the minimum is
`(n-1)^2-max(9-n,1)^2`, attained by the old first map. For `n>=8` this
equals `(n-1)^2-1`. Thus a new first map alone cannot concentrate this
construction's error on a small first-leg support.

Claim `AI-PRODUCT-LONGMAP-RESIDUAL-001` is written and unreviewed. Direct
rational paired ranks replay every `n=5,...,12` and `n=16`. Larger
one-factor controls and characteristic-three/five checks also pass.
Other long maps and general tensor degenerations remain open. No matrix
target or improved exponent is established.

## Paired-source long-leg ranks through the first support threshold

The [low-degree proof](research/ai/2026-10-23-paired-long-legs/long_leg_low_degrees.md)
uses exact interpolation and full-spark evaluation vectors to prove
`rank K_p(P_a; B)=rank K_p(P_a; C)=a^2*binom(a(2a-1),p)` for every
`a>=2` and `0<=p<=a`. The maps are injective in this range. All 28 saved
single-matrix survivors through `a=16` have the short leg uniquely aligned;
the result shows that their long-leg tests cannot exclude them in these
degrees. For all `p`, the proof also gives `rank K_p >= a^2 L_(a,p)`, where
`L_(a,p)` counts wedges using at most `a-1` interpolation blocks. At
`p=a+1`, this floor dominates both long-leg target ranks for four of eleven
`a=15` survivors and six of twelve `a=16` survivors. It dominates neither
long-leg rank for the `a=14` survivors or for the other `a=15,16` survivors.
Higher-degree ranks and comparisons remain open. Claim
`AI-PAIRED-LONG-KOSZUL-005` is written and unreviewed. Exact interpolation,
frontier, support-count, and coefficient-matrix controls are recorded in
`results/paired-long-legs-2026-10-23/verification.json`. No exponent
improvement is established. A separate exact bidegree atlas gives full
column rank through `p=6` at `a=3` and rank `57185/57915` at `p=7`, with
kernel dimension `730`; it is a finite pilot, not an all-size formula. See
`results/paired-long-legs-2026-10-23/graded-rank-atlas-a3.json`. A further
finite control gives full rank modulo two, hence over `Q`, at `(a,p)=(4,5)`:
`1,572,480` columns in 524 bidegree blocks. This single point adds no
all-size conclusion; see
`results/paired-long-legs-2026-10-23/graded-rank-atlas-a4-p5.json`.
The first finite kernel defects at `(2,3)` and `(3,7)` have also been
decomposed into `SL2 x SL2` types; the `(3,8)` kernel has dimension 3,780.
The exact `a=3` atlas is now complete through `p=14`, with ranks
`37464,18819,6660,1575,225,15` at `p=9,...,14` respectively.
The first-defect degrees fit the conjecture `p=a(a-1)+1`, still untested at
`a=4`; see
`research/ai/2026-10-23-paired-long-legs/kernel_module_types.md`.

## Sharp source caps84/88 force balanced long leading sum136

The [finer source-cap proof](research/ai/2026-10-23-rank84-88-source-caps/proof.md)
proves sharp complex A4 source dimensions56 below matrix rank84 and60
below rank88. Complete independent acceptance checks1404 size57 ideals
and118 size61 ideals, each with an odd84/88 minor, after the credited
characteristic-zero order-ideal reduction. The prior staircase examples
attain both dimension caps. With the prior saturated support condition,
the finite comparison covers644 rank pairs and improves the necessary
sum from144 to136, at every Laurent order. Claims
`AI-A4-RANK84-SOURCE-CAP-001`, `AI-A4-RANK88-SOURCE-CAP-002` and
`AI-A4-BALANCED-LONG-SUM136-003` are written and unreviewed. At68,68 the
prior64-dimensional rank-at-most88 staircase meets the two numerical
kernel conditions; it is not shown to be a compression kernel. Lower
rank pairs and a matrix target remain open. No smaller exponent follows.

## A sharp source cap below rank 37 and a counterexample below rank 96

The [rank-37 source theorem](research/ai/2026-10-23-rank37-source-spaces/proof.md)
proves a sharp dimension-16 cap for complex A4 source spaces whose slices
all have rank strictly below 37. The order-ideal reduction leaves exactly
13 size-17 ideals; each has an exported odd integer 37-minor. The full
middle-zero plane attains dimension 16 with only 28 supported rows.

The [staircase source construction](research/ai/2026-10-23-source-staircase-spaces/proof.md)
gives an explicit 68-dimensional A4 space whose matrices use only 92
columns. It disproves the proposed dimension-57 cap below rank 96, which
would have been sufficient for a further target obstruction. The general
all-size family has a proved dimension and exact joint column support.
This closes that proposed premise, while more specific compression-kernel
constraints and smaller threshold refinements remain available. Claims
`AI-A4-RANK37-LINEAR-SPACE-001` and
`AI-CYCLIC-SOURCE-STAIRCASE-SPACES-001` are written and unreviewed.
Twelve focused tests pass. These results leave the necessary balanced
long-rank sum 144 unchanged and do not construct a target or improve omega.

## Balanced A4 long-rank sum is at most 144

The [rank-80 source-space proof](research/ai/2026-10-23-torus-rank80/proof.md)
shows that every complex A4 source space whose slices have rank strictly
below 80 has dimension at most 50. The earlier order-ideal reduction,
small coherent minors and disjoint middle blocks leave exactly 24
size-51 ideals; each has an exported integer 80-minor with odd determinant.
Together with the credited saturated target-support inequality and the
preceding sum-160 exclusion, this forces balanced leading long ranks
b+c<=144 in every complete Laurent A4 to M(10,10,11) candidate. Thus
the two target long maps must lose at least 76 leading ranks in total;
each rank is also at most 101. Arbitrary first-map poles and all higher
coefficients remain allowed. Claims `AI-A4-RANK80-LINEAR-SPACE-001` and
`AI-A4-BALANCED-LONG-SUM144-002` are written and unreviewed. Exact replay
verifies all 35 minors and all 24 remaining ideals; eight focused tests
pass. The source cap 50 is sharpened to 44 above. The target sum 144
is not asserted sharp, and no full matrix target or improved exponent
is constructed.

## Sharp source dimension32 below rank64; balanced long-rank sum at most160

The [order-ideal proof](research/ai/2026-10-23-torus-order-ideal/proof.md)
uses three literal rank-preserving lowering actions and the source torus
to reduce arbitrary complex bounded-rank spaces to downward coordinate
ideals. All611 size33 ideals in the relevant4-by3-by4 box have exported
integer64-minors that are odd. Thus every source space whose slices have
rank below64 has dimension at most32. A full32-plane supported at middle
coordinates0,1 attains this dimension with only56 supported matrix rows.
The credited target-support inequality then forces balanced long-rank
sum at most160 in every complete Laurent A4 to M(10,10,11) candidate,
allowing arbitrary first-map poles and higher coefficients. This is a
leading rank loss of at least60; each individual rank is also at most101.
Claims `AI-A4-RANK64-LINEAR-SPACE-001` and
`AI-A4-BALANCED-LONG-SUM160-002` are written and unreviewed. The source
dimension bound is sharp; sharpness of the target rank-sum bound is not
asserted. No full target or exponent improvement is constructed.

## Balanced A4 long-map rank sum is at most176

The [rank-48 source-space proof](research/ai/2026-10-23-torus-rank-frontier/proof.md)
shows that every complex linear A4 source space whose slices all have
rank below48 has dimension at most24. Torus specialization, disjoint
middle blocks and the earlier rank23 cap prove this for arbitrary
complex subspaces. Combined with the credited saturated target-support
inequality, it forces `rank(B0)+rank(C0)<=176` in every complete A4 to
M(10,10,11) Laurent degeneration after scalar-balancing the two long
maps. The first map may have arbitrary finite poles, and higher
coefficients are unrestricted. This strengthens concurrent PR122's
sum192 bound; the total leading long-rank loss is at least44.
Claims `AI-A4-RANK48-LINEAR-SPACE-001` and
`AI-A4-BALANCED-LONG-SUM176-002` are written and unreviewed. The separate
rank102 exclusion below also applies: both ranks are at most101.
Neither24 nor176 is asserted sharp; no surviving target or exponent
gain is constructed.

## Sharp rank-23 source-space cap and long-map rank 102 exclusion

The [torus specialization proof](research/ai/2026-10-23-torus-low-rank/proof.md)
shows that every complex linear space of A4 slices of rank at most23
has dimension at most8, with an explicit8-dimensional example. The
rank-preserving diagonal source action reduces arbitrary subspaces to
coordinate subspaces; sixteen determinant-one minors give the finite
coordinate obstruction. Combined with the active-ruling argument, this
excludes every A4 to M(10,10,11) degeneration with either scalar-balanced
long-map limit of rank at least102. Both other maps may have arbitrary
finite poles. Claims `AI-A4-LOW-RANK-SPACE-CAP-001` and
`AI-A4-SINGULAR-LONG-102-002` are written and unreviewed. All remaining
candidates have both balanced long ranks at most101. A12-dimensional
space of rank-at-most24 slices shows why the source-cap argument stops
there. No full matrix target or improved exponent is established.

## Four double-leg split seeds and an exact W35 cover obstruction

The [two-stage mixed-leg package](research/ai/2026-10-23-double-leg-anchor/README.md)
gives four exact rank-76 Laurent border families from the externally
credited M(4,5,5) seed. Two extra W splits after the eleven-U/two-W
mixed seed yield 65/76/54 projective factor directions and fifteen
strictly vanishing discarded rank-one tensors under one physical
stabilizer. Every constant and positive Laurent coefficient replays.
The stronger W-weight total falls from152 to144, meeting nine times
the rank-four cap16. Yet W35 is in no saturated flat: each of four
complete 23426-triple modulo101 anchor enumerations has maximum
weight15. Thus none of these *displayed* W configurations has the
nine-four-space cover required by the specified termwise Q(6,4)
alignment. The written implication is unreviewed and does not exclude
further factor changes or general source maps. No rank or exponent
improvement is claimed.

## Mixed-leg splits pass both old screens, then meet a stronger W bound

The [mixed U/W witness](research/ai/2026-10-23-mixed-leg-splits/README.md)
uses eleven U replacements and two W replacements in the credited
external algorithm. Its 89-term exact expansion leaves a 76-term Laurent
border seed with 65 U, 76 V and 56 W directions. Exact replay checks
all 10000 constant positions, no negative-degree coefficients, all 506
positive coefficients, and the full identity with the 13 discarded terms.
Each discarded tensor has positive valuation under one physical family;
product-one gauges after epsilon=z^3 make all discarded factors positive.

The new seed retains old U weight 214 against capacity 216 and old W
weight 141 against capacity 144. Passing both necessary inequalities
does not supply a cover. A new integer weighting has total 152 and
rank-four cap 16, verified over all 367290 four-subsets. Thus its displayed
W directions still require at least ten groups in the specified termwise
grid alignment. This bound permits common invertible physical changes
and scalar gauges; it does not close later flips or refactorizations.
Claim `AI-EXTERNAL-MIXED-LEG-SPLIT-SEED-011` is written and unreviewed.
No new rank bound, complete source map, or smaller exponent follows.

## Complete-error invariants exclude further one-term deletions

The [quadratic-error certificate](research/ai/2026-10-23-quadratic-error/README.md)
reshapes the matrix-format tensor into a 100-by-100 matrix. The physical
action becomes conjugation, and the multiplication target reshapes to
the identity. Its power traces are therefore exact tests on the complete
discarded error, allowing cancellation between old and newly removed terms.

For the ten-split block `{36,56,61,62,75}`, every exact minimum five-term
refactorization obeys `q(D+A)=2-2*tau+tau^2` for any selected term A,
where D is the full original discarded error and tau is the term trace.
Contraction would force tau to zero while q tends to two. Thus no such
one-term deletion works, even with Laurent-dependent refactorizations
and physical matrices. Two specified shared-V families from the six-split
seed also have complete-error invariant two, despite trace-zero selected
terms with square-zero cyclic products. Claim
`AI-EXTERNAL-QUADRATIC-ERROR-010` is written and unreviewed. Full replay
checks 10000 source coordinates and 90000 family coefficient positions.
Arbitrary block mixing, simultaneous deletions and general border-rank
reductions remain outside these obstructions. No smaller exponent follows.

## Larger split batches pass a new screen and change component geometry

The [larger gauged witnesses](research/ai/2026-10-23-large-gauged-batches/README.md)
give exact ten- and eleven-split Laurent families, each with 76 surviving
terms and limit M(4,5,5). They have 66 and 65 distinct U directions and
283 and 414 positive-degree remainder coefficients, respectively. Full
replay checks all 10000 constant positions, every nonzero coefficient,
the exact surviving-plus-discarded identity, and positive valuations of
all discarded tensors. Product-one factor gauges after epsilon=t^3
make every discarded factor positive.

The eleven-split witness retains original-U weight 214, below the
earlier nine-group capacity of 216. Passing this necessary inequality
does not construct a cover. The ten-split witness has four exact
one-dimensional intersections between factor spans of distinct initial
sharing components, so the earlier pairwise separation hypothesis does
not apply. A span intersection does not establish an available flip or
refactorization. Claim `AI-EXTERNAL-LARGE-GAUGED-SPLIT-SEEDS-008` is
written and unreviewed. Both seeds still retain the original W directions
and fail immediate termwise grid reuse. No maximum batch size, rank
improvement, complete source map, or smaller exponent is established.

## Six split deletions escape the unscaled-arrow condition

The [gauged split witness](research/ai/2026-10-23-gauged-splits/README.md)
uses six replacements and one physical Laurent family to give a 76-term
border seed with 70 distinct U directions. Two discarded factors have
poles, but each discarded tensor has positive valuation. Separate factor
gauges after epsilon=t^3 give every discarded factor positive valuation
without changing any tensor term. Complete contraction checks all 10000 constant
positions, no negative-degree coefficients, and 73 positive-degree remainder coefficients.
A mixed trace equal to one proves that simultaneous contraction of all
unscaled arrows is impossible for this batch. Claim
`AI-EXTERNAL-GAUGED-SPLIT-SEED-006` is written and unreviewed.

The [six-split geometry certificate](research/ai/2026-10-23-six-split-grid/README.md)
shows that only 47 W directions remain fixed throughout this new
standard-flip component. An explicit rational cover uses nine rank-four
groups. Integer weights of total 144 and flat cap 16 prove that nine is
the exact minimum; full replay checks all 178365 four-subsets. Claim
`AI-EXTERNAL-SIX-SPLIT-FIXED-COVER-007` is written and unreviewed.

The later [mobile-factor obstruction](research/ai/2026-10-23-six-split-mobile-obstruction/README.md)
closes the full nine-space cover in this component. The fixed weight
144 forces each of nine spaces to saturate the weight-16 bound and to
be a rational four-space spanned by fixed directions. Complete replay
finds 21649 such spaces. Each meets either of two specified mobile
planes in at most one fixed line, whereas each mobile block retains a
two-dimensional W flattening image. Thus no finite standard-flip
continuation, or separate minimum-term refactorization of its initial
blocks, fits the specified termwise grid. The argument also permits
Laurent coefficients, product-one gauges, and common invertible physical
changes. Claim `AI-EXTERNAL-SIX-SPLIT-MOBILE-009` is written and unreviewed.
The fixed-subset cover remains valid. New splits, arbitrary singular
limits and general source maps remain outside this obstruction.

## Fixed post-split components close two further searches

The [post-split component proof](research/ai/2026-10-23-fixed-flip-components/README.md)
shows that every finite standard-flip continuation of either explicit
split seed retains 50 fixed W directions. Exact rank certificates keep
the components isolated on all three legs. Their weighted rank-four
cover bounds are 148>9*16 and 74>9*8, excluding the specified termwise
Q(6,4) grid assignment throughout both components, including over
characteristic-zero Laurent fields. Each bound replays all 230300
four-subsets. Claim `AI-EXTERNAL-FIXED-FLIP-GRID-004` is written and
unreviewed; singular limits that change incidences remain outside it.

For the five-split seed, a [scalar trace pairing](research/ai/2026-10-23-fixed-flip-components/TRACE_PROOF.md)
also excludes further nonempty-subset deletion by the physical stabilizer
after finite standard flips. Minimum V-flattening ranks force every term
to retain trace one or two; the original discarded error has trace zero.
Thus the total error from any additional deletion cannot tend to zero.
Claim `AI-EXTERNAL-FIVE-SPLIT-TRACE-005` is written and unreviewed. This
argument does not exclude all border-rank reductions or the four-split
seed's nonscalar trace blocks. Separate factor gauges give the new
six-split witness above; further changes outside the two closed components
remain open.
No smaller exponent is established.

## Weighted grid covers require changes on both long legs

The [weighted-flat certificate](research/ai/2026-10-23-grid-escape/README.md)
assigns integer weight 149 to the 58 original W directions, with at most 16
in every rank-four span. Nine groups have capacity 144, so a termwise
Q(6,4) assignment preserving those directions on a long leg in the specified
alignment is excluded. U-only splits
cannot repair it. On the original76 U directions a second weighting gives
total 251 and flat cap 24, requiring 3r+e>=35 for a subset replacement; the
four-split seed still has weight 238>216. Exact replay enumerates all
1282975 U and 424270 W four-subsets over F101, with integer-minor transfer
to characteristic zero. Claim `AI-EXTERNAL-WEIGHTED-GRID-003` is written
and unreviewed. The later fixed-component proof above closes standard
flips of the two explicit seeds; different seeds and general source maps
remain open. The positive border seeds and exponent status are unchanged.

## Exact obstruction for the external seed's standard-flip component

The [component proof](research/ai/2026-10-23-flip-escape/component_proof.md)
closes finite standard shared-factor flips and term gauges of the pinned
external rank-76 M(4,5,5) algorithm. Its 58 proportional-W classes have
pairwise disjoint U spans and V spans, certified by 3306 integer unit
minors. Scalar trace pairings force every term to retain trace one or two.
No usual rank reduction or physical-stabilizer deletion of a nonempty
subset is possible within this move component. Claim
`AI-EXTERNAL-FLIP-COMPONENT-001` is written and unreviewed. Rank-increasing
splits and different decompositions remain outside the result. Three
focused exact tests pass; this is not a global rank or exponent bound.

The [four-split construction](research/ai/2026-10-23-flip-escape/split_proof.md)
escapes that move component by increasing the exact term count to 80,
then deleting four terms with a common physical stabilizer degeneration.
Unimodular bases and a nine-step joint image flag give an explicit rank-76
border seed with 72 distinct first-leg directions. Complete rational
Laurent contraction checks all 10000 constant positions, no negative-degree
coefficients, and 51 positive-degree remainder coefficients. Claim
`AI-EXTERNAL-SPLIT-BORDER-SEED-002` is written and unreviewed. A
[second exact witness](research/ai/2026-10-23-flip-escape/five_split.md)
instead splits and deletes five terms. Its seed has 71 distinct U
directions, an eight-step common image flag,
and 172 positive-degree remainder coefficients. Seven split tests pass for both
variants, including schema/scope and coefficient mutations. Both seeds
still fail the stronger termwise grid incidence test. Their new shared-U
pairs permit changes to some W directions, but the fixed-component proof
above shows those changes cannot repair the specified termwise grid.
No Q(6,4) map, rank record, or smaller exponent is supplied.

## Total balanced A4 leading rank is at most 198

The [rank91 core continuation](research/ai/2026-10-23-rank91-core/proof.md)
proves that every complex A4 source space whose slices have rank strictly
below 91 has dimension at most 67. This source cap is not claimed sharp.
The four dimension-68 equality profiles from the preceding theorem
reduce to eight strip ideals. Each contains one fixed 56-coordinate
core with an odd 91-minor, or its transpose.

For every complete complex Laurent A4 to M(10,10,11) presentation, the
individually scalar-balanced leading ranks now satisfy a+b,a+c<=133,
b+c<=136, and a+b+c<=198, where a is the short rank. All earlier
screens remain in force. At a=100, the high-threshold result below
restricts each positive long leading rank to 1 through 12 or 20. Arbitrary
complex leading kernels, higher coefficients and finite Laurent poles
remain allowed. The necessary total leading-rank loss is at least 122.

The exact census retains every frozen202 exclusion and removes 60
additional pairs and 5,250 additional triples. Its only total-198
endpoints are (62,66,70) and (62,70,66). These numerical survivors do
not construct target-compatible maps or establish target sharpness.
Four exact minors, all eight ideals, 112 source-transposition identities,
20,706 integer pairs and 1,050,804 triples are replayed. Eight focused
tests cover corrupt witnesses, strict thresholds, complete retained
censuses, source pins and scope.

Claims AI-A4-RANK91-LINEAR-SPACE-001 and AI-A4-LEADING-RANK-SUM198-001
remain written and unreviewed. Internal mathematical audits and exact
replays are not independent external review or formalization. No
matrix target or improved exponent is established.

## Sharp source caps through rank 112 and the full-short long-rank gap

The [high-threshold source proof](research/ai/2026-10-23-high-rank-source-caps/proof.md)
determines maximum complex source-space dimensions 84, 88, 92 and 96
when every A4 slice has rank strictly below 100, 104, 108 and 112,
respectively. Complete layer-size cases prove the upper bounds after
the credited order-ideal reduction. The credited d=3 staircase spaces
attain all four dimensions; exact new minors show maximum slice ranks
96, 100, 104 and 108. These strict thresholds cannot be replaced by
weak inequalities at the same dimension caps.

For every complete complex Laurent A4-to-M(10,10,11) presentation
with individually balanced short leading rank 100, each long leading
rank is at most 20. More precisely, each positive long rank belongs
to {1,...,12,20}. The proof retains arbitrary complex leading kernels,
higher coefficients and finite poles. The arithmetic endpoint
(100,20,20) is not a target construction or a sharp-target assertion.

Exact acceptance checks 245,157 nested layer-size profiles at all four
thresholds, eleven credited coherent minors and four new source minors,
all 112 literal-source factorizations, all 102 one-leg target decisions,
and 10,404 full-short pairs. It retains 196 of the preceding 841 full-short
triples, excluding 645 additional numerical possibilities. Eight focused
tests cover source and target boundaries, support and minor corruption,
source pins, retained prerequisites, and claim scope.

Claims AI-A4-RANK100-SHARP-LINEAR-SPACE-001,
AI-A4-RANK104-SHARP-LINEAR-SPACE-001,
AI-A4-RANK108-SHARP-LINEAR-SPACE-001,
AI-A4-RANK112-SHARP-LINEAR-SPACE-001, and
AI-A4-FULL-SHORT-LONG20-001 remain written and unreviewed. No external
independent review, formalization, matrix target or improved exponent
is established. This source package has separate frozen prerequisites;
the rank91 result above supplies the current global bound.

## Complete projective conic normal-class lifting

The [projective criterion](research/ai/2026-10-23-conic-projective-criterion/proof.md)
covers every complex base point `[r:s]`, `[a0:a1]`, `[b0:b1]` in the
product of three projective lines. The leading ranks remain 14, 14 and 12,
and the complete tangent has 68 boundary directions and two normal
directions at every point, including infinity. For a nonzero normal class
`[lambda:mu]`, some second jet, some formal curve and some exact polynomial
curve exist precisely when
`(a1*r-a0*s)*(b1*r+b0*s)*(s*lambda^3+r*mu^3)=0`.
The first boundary velocity may be chosen; this does not assert that
every prescribed full first or higher jet extends.

The set of liftable classes has exactly three irreducible components:
the graphs `[a0:a1]=[r:s]`, `[b0:b1]=[r:-s]` and
`[r:s]=[lambda^3:-mu^3]`. This is a set-theoretic classification, without
an assertion about the full incidence scheme. A literal source reversal
swaps the conic coordinates and the normal class `[lambda:mu]` to
`[mu:lambda]`; unit row transitions prove that no extra component appears
through rank loss at infinity. Three complete missing-stratum curvature
certificates, eight polynomial families and seven linear-component
identities replay exactly. Seven focused tests pass. The finite mixed
curves have degrees one and two. Claim
`AI-CONIC-PROJECTIVE-CRITERION-001` is written and unreviewed. The earlier
affine criterion remains a correct scoped prerequisite. No full matrix
target, independent mathematical review, Lean formalization or exponent
improvement is claimed.

## Retained total202 prerequisite

The [new target refinement](research/ai/2026-10-23-leading-rank202/proof.md)
proves a+b+c<=202 for every complete complex Laurent A4 to M(10,10,11)
presentation, with a on the short target leg and all three leading ranks
individually scalar balanced. Its earlier conclusion b,c<=28 at a=100
is refined above. This historical checkpoint gave total leading-rank
loss at least 118; the current rank91 result strengthens it to 122.
Arbitrary complex leading kernels,
higher coefficients and finite Laurent poles remain allowed.

Two [sharp source theorems](research/ai/2026-10-23-rank92-rank96-spaces/proof.md)
give maximum dimensions 68 below slice rank 92 and 72 below slice rank
96. The explicit spaces attain ranks 91 and 95. Their unchanged proofs
use complete layer-volume cases, the credited order-ideal reduction,
and exact coherent minors and support covers. Combined with the retained
every-pair bound of 136 and its all-order support inequalities, these
caps give the historical total-202 and full-short-28 refinements.

Exact additional floor constraints exclude 817 further integer pairs
and 62,478 further triples. Complete exported censuses cover all 20,706
pairs and 1,050,804 triples in the established rank ranges. The unique
endpoint of that historical total-202 screen was (70,66,66), now excluded
by the rank91 refinement. It was not a target construction or a proof
that the necessary target bound was sharp. Seven target tests
and six source tests cover the censuses, strict thresholds, source pins,
source minors, and scope controls.

Claims AI-A4-RANK92-SHARP-LINEAR-SPACE-001,
AI-A4-RANK96-SHARP-LINEAR-SPACE-001, and
AI-A4-LEADING-RANK-SUM202-001 remain written and unreviewed. Internal
exact replays do not establish independent external review or
formalization. No matrix target or improved exponent is established.

## Retained every-pair 136 prerequisite

The [all-pair theorem](research/ai/2026-10-23-all-pair-rank136/proof.md)
forces a+b, a+c, and b+c to be at most 136 in every complete complex
Laurent A4 to M(10,10,11) presentation, where a is the short-leg leading
rank and each map is individually scalar balanced. Its earlier numerical
consequences were a+b+c<=204 and, if a=100, b,c<=36. The credited202
checkpoint first strengthened these to 202 and 28. The current bounds
are total198 and, at short rank100, positive long ranks1 through12 or20.
The unselected map may have
arbitrary finite Laurent poles; arbitrary leading kernels and higher
coefficients remain allowed.

Two [sharp source theorems](research/ai/2026-10-23-rank84-rank88-spaces/proof.md)
give maximum dimensions 56 below slice rank 84 and 60 below slice rank
88. The sharp examples attain ranks 80 and 84. Three disjoint middle
block pairs and exhaustive layer-size cases prove the upper bounds.
The [preceding all-pair 144 theorem](research/ai/2026-10-23-all-pair-rank144/proof.md)
closes the exceptional mixed rank pair (100,100) with a seven-ideal
compression certificate, using incidence-preserving lowering and a
second torus with distinct matrix-leg weights. It credits PR151's
earlier universal compression result and matching method.

Claims AI-A4-RANK84-SHARP-LINEAR-SPACE-001,
AI-A4-RANK88-SHARP-LINEAR-SPACE-001, AI-A4-ALL-PAIR-RANK144-001,
and AI-A4-ALL-PAIR-RANK136-001 remain written and unreviewed.
Exact acceptance checks the 245,157 layer profiles, all thirteen small
and sharpness minors, seven matching/forced-cover certificates, and
20,706 integer target-rank pairs. Source sharpness does not imply
sharpness or attainability of the necessary target bounds. No full
matrix target or improved exponent is established.

## Sharp source dimension 44 below slice rank 80

The [sharp rank-80 source theorem](research/ai/2026-10-23-rank80-sharp-spaces/proof.md)
determines the maximum dimension of a complex A4 source space whose
slices all have rank strictly below 80: it is exactly 44. The complete
inventory of 1,709 remaining size-45 ideals has an exported odd integer
80-minor for every ideal. An explicit 44-dimensional space has its matrix
support covered by 35 rows and 44 columns, so all ranks are at most 79;
a saved 79-minor attains that rank. This sharpens the earlier cap 50.
Claim `AI-A4-RANK80-SHARP-LINEAR-SPACE-001` is written and unreviewed.
Six focused tests replay all 1,721 minors, the source pins, exhaustive
coverage and the sharpness construction. Its strict threshold matters:
a 56-dimensional source space has rank at most 80. No new target rank
sum is asserted in this package, and no matrix target or exponent gain
is constructed.

## Nonsplit vector-degree continuation: no finite bound gain

The [vector-degree experiment](research/ai/2026-10-23-nonsplit-vector-covers/README.md)
checks every original nonsplit coefficient, finding the 95 principal
degree triples of even total at most eight. Seven bounded class-cover
runs replay exactly, and a complete 3372-vector integer weight census
combining degree and the saved principal cover retains the cube bound
6155844. Claim `EXP-NONSPLIT-VECTOR-COVERS-001` is a finite experiment.
Numerical optimality reports are not accepted as class-wide exclusion
certificates. No improved bound or exponent follows. A new attempt needs
additional basis structure or a changed source/basis/power.

## A joint cube closes the matrix-plus-scalars coordinate family

The [full nonsplit joint-target certificate](research/ai/2026-10-23-central-cover-joint-frontier/README.md)
gives SR_F4(T_SL2F5^3)<=1012332. Cyclic tensoring of M(a,b,c) plus r
scalars has exact finite slice rank V^2+3r V min(a,b,c)+3r^2 min(ab,bc,ca)+r^3,
where V=abc. The complete stated frontier covers 866 positive shapes and
41132 dimension-compatible family members. The only three improving
targets left by the earlier screens, M(9,9,11) plus 11,12,13 scalars,
exceed the source cube bound by 76910,106953,137554. Thus the improving
one-matrix-plus-scalars family is closed in the maintained one-copy
complex coefficient-one coordinate/potential class. General complex
mixing, other joint sums and higher source powers remain open.

Claims `AI-NONSPLIT-MATRIX-SCALAR-CUBE-002` and
`AI-SEMISIMPLE-JOINT-RANK-PROFILE-001` are written and unreviewed. The
latter gives a full profile necessary condition for general complex
semisimple-source degenerations. No exponent improvement is established.

## General full-right-inverse Laurent criterion

Concurrent [PR113](https://github.com/1337isnot1337/matrix-mult-bounds/pull/113)
at08ac3e9 gives a stronger A4 exclusion with one regular full-rank long map,
using low-rank target generators and allowing a polar original unit lift.
It subsumes the A4 rank102 corollary below. This package retains a general
regularity theorem without the low-rank-spanning target hypothesis; its
rank101 equality is a boundary of this sufficient criterion, not the
updated A4 frontier. Both results are written and unreviewed. The separate
[PR125](https://github.com/1337isnot1337/matrix-mult-bounds/pull/125) and
[PR142](https://github.com/1337isnot1337/matrix-mult-bounds/pull/142) continue
to singular balanced long-map limits using source ruling geometry.

The [regular-right-inverse argument](research/ai/2026-10-23-regular-unit-projector/proof.md)
extends the preceding rank109 A4 chart to unit-image rank at least102.
One long map must still be regular with rank110 limit, and the source
identity lift must be regular. Its product T with the long map is a
regular right inverse of the normalized other long map B. The projector
I-T B has rank two over C((t)); regularizing its product with a source
slice first excludes every pole in F, independently of unit-image rank.
At image rank102, F(0) is injective and a source-row dimension bound forces
B to be regular, reducing to the prior ordinary rank contradiction12>11.
Source units of corank at most eight are included. Every finite pole order
is covered. Claims `AI-REGULAR-RIGHT-INVERSE-001` and
`AI-A4-RANK102-UNIT-IMAGE-002` are written and unreviewed. Exact controls
include polar projectors and the attained rank101 injectivity boundary.
Image ranks at most101, singular long-leg limits and polar unit lifts
remain outside this exclusion. No matrix target or smaller exponent is
established.

## Stacked Laurent ranks extend the unit-image exclusion to105

The [stacked-product continuation](research/ai/2026-10-23-unit-image-stacked-rank/proof.md)
combines two regularized source blocks into one rank-q product. The
first-pole bound improves from3q to2q and the rank-one source bound
from n+3q to n+2q. A rank-one matrix-kernel argument and propagation
across rulings with zero images now exclude A4 to M(10,10,11) when one
long map is regular with rank110 limit, the source identity lift is
regular, and its unit image has rank at least105. Regular source units
of corank at most five are included. Claims
`AI-CYCLIC-STACKED-REGULARITY-001` and `AI-A4-UNIT-IMAGE-RANK105-002` are
written and unreviewed. Exact controls replay48 Laurent block families,
three symbolic rank-one spaces and seven strict boundary cases. Retained
rank104, singular long-leg limits and polar units remain open to this
method. No tensor target or smaller exponent is established.

## A4 unit-image exclusion down to rank107

The [source rank-locus continuation](research/ai/2026-10-23-unit-image-rank-gap/proof.md)
extends the previous all-order partial-unit-image exclusion from rank109
to rank107. It retains one regular long map of limiting rank110 and a
regular source lift of the target identity. Varying target retractions
preserve first-map injectivity; the existing classification of source
slices below rank32 then forces any polar long-map chart's100-dimensional
first image into16 dimensions. Regular source units of corank at most
three are included. Claims `AI-CYCLIC-RANK-LOCUS-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-RANK107-002` are written and unreviewed. Exact controls
check56 rational retractions, nine literal source matrices and strict
boundary margins. This earlier proof stops at rank106; the stacked
continuation above reaches105. Singular long-leg limits and polar unit
lifts remain open. No target or smaller exponent is established.

## Singular A4 leading flags need total defect at least20

The [leading-defect proof](research/ai/2026-10-23-leading-defect/proof.md)
excludes r_B+r_C>204 for the two scalar-balanced A4 long-map leading
ranks, at every finite Laurent pole order. An invertible target matrix
in the leading first-map kernel activates the rank-two unit correction;
Flanders's dimension bound and the prior source gap above16 finish the
exclusion. For total defects20..27, the leading first-map rank is10..16
with one coherent middle factor. The same coherent upper bound16 holds
at defects28..31. Exact defect16 leading controls do not extend to a
target. Claims `AI-A4-LEADING-DEFECT-001` and
`AI-A4-INVERTIBLE-LEADING-KERNEL-002` are written and unreviewed.
Larger-defect constructions and the full target remain open; the certified
upper bound remains9/4.

The numerical204 corollary is weaker than the separate written,
unreviewed176 bound in [PR129](https://github.com/1337isnot1337/matrix-mult-bounds/pull/129).
This package retains a general invertible leading-kernel method for square
matrix targets;204 is not the strongest current proposed A4 frontier.

## One regular long leg is impossible for the full A4 target

The [unit-kernel argument](research/ai/2026-10-23-one-regular-leg/proof.md)
excludes A4 to M(10,10,11) whenever either long map is regular with rank110
limit, allowing arbitrary finite poles in both other maps. No hypothesis
on the original target-identity lift remains. Scalar balancing and an
exact regular right inverse produce a regular kernel correction of rank
at most two. The100 rank11 target generators would force the leading
first map to vanish, since the source minimum16 exceeds11+4. Claims
`AI-UNIT-KERNEL-LOW-RANK-001` and `AI-A4-ONE-REGULAR-LEG-002` are written
and unreviewed. Finite exact controls support the proof without
formalizing it. Every remaining candidate must have singular leading
coefficients on both long legs after scalar balancing. Those candidates,
the full target and the exponent below9/4 remain open.

## Exact curve on the d=0 cubic-conic fiber

The [d=0 curve](research/ai/2026-10-23-conic-d0-cubic/proof.md)
specializes PR101's polynomial two-jet at `c=d=0` and extends it to an
exact polynomial curve for every complex `a,b`, without changing its
second coefficient. The maps are `B0+t*B1+t^2*B2` and `C0+t*C1`; `B2`
has eight nonzero entries, `C2=0`, and the source-row correction vanishes.
Independent replay checks all 4096 source terms, 78,400 kernel
coefficients, and constant leading minors `1,1,-1`. Claim
`AI-CONIC-D0-EXACT-CURVE-001` is written and unreviewed. This closes only
the `d=0` fiber for the specified first jet; it does not construct the full
matrix target or improve the exponent.

## Three unequal monotone legs also retain the S5 cube bound

The [three-leg census](research/ai/2026-10-23-s5-staircase-covers/three_leg_boundary.md)
accounts for all 77392758 unordered first/second threshold pairs in the
four S5 x C2 cube block words. Exact pruning leaves 5207743 third-leg
evaluations. Separate Python and C++ implementations agree on all costs
and witnesses, retaining the bound6867542 above the M(13,14,14) threshold
6492304. Claim `EXP-S5-THREE-LEG-COVERS-002` is a finite experiment. This
closes monotone thresholds on these bidegree majorants as an improvement
route, without claiming optimal covers of the actual source. Finer support,
nonmonotone covers, other bases/powers and the exponent question remain open.

## Finite boundary for two-equal-leg S5 staircase covers

The [complete staircase census](research/ai/2026-10-23-s5-staircase-covers/proof.md)
checks 891888 monotone first-leg thresholds with two equal legs and an
independently minimized third. All eight cube block-word minima agree
with the preceding weighted S5 covers. Nonlinear thresholds in this
family therefore cannot strengthen those bounds. Claim
`EXP-S5-STAIRCASE-COVERS-001` is a finite experiment; three unequal legs,
nonmonotone covers and other source data remain outside it. No exponent
improvement or arbitrary cover optimality is claimed.

## Finite weighted S5 cubes close the selected M19 coordinate target

The [weighted cube proof](research/ai/2026-10-23-s5-finite-covers/proof.md)
gives characteristic-two slice covers of 6867542 and 42493572 for the cubes
of S5 x C2 and S5 x C2^2. Every one-copy single rectangular target then
has abc<=2620 or abc<=6518 respectively. This excludes 38 additional shapes
from the maintained coordinate/potential frontier, including M19 in the
second source, leaving two and nine general-test survivors at that checkpoint.
The later Peirce full-source covers exclude five of those nine
two-central-factor shapes. M(13,14,14) in the first source remains open. The exact verifier replays the prior radical
and block certificates and all 227713 allowed bidegree triples. Claim
`AI-S5-FINITE-COVERS-001` is written and unreviewed. General complex mixing,
arbitrary higher-source constructions, and the exponent question remain open.

## Fifth- through seventh-power screens for a pinned two-matrix candidate list

The [nonsplit two-matrix continuation](research/ai/2026-10-23-nonsplit-two-matrix-targets/README.md)
verifies fifth-, sixth- and seventh-power source slice-rank upper bounds of
9874344844, 991166716704 and 100070673945707 for the actual SL(2,F5)
source. Exact target direct-sum ranks over all orientation multisets replay
the earlier power-three values and exclude eight of 144 candidates at
power five, ten more at power six and one more at power seven. The other
125 are not excluded by these comparisons.
The prior pair census and its rank-profile/Koszul screens are not
regenerated here, so this does not close the two-matrix family. Claims
`AI-NONSPLIT-TWOMATRIX-POWER5-001` and
`AI-NONSPLIT-TWOMATRIX-POWER6-001` and
`AI-NONSPLIT-TWOMATRIX-POWER7-001` are written and unreviewed; the
established one-copy coefficient-one good-reduction limitation remains,
and no exponent improvement is claimed.

## All-order A4 exclusion with a partial regular unit image

The [partial-unit-image argument](research/ai/2026-10-23-regular-unit-image/proof.md)
extends the previous invertible-unit Laurent chart. A4 cannot degenerate
to M(10,10,11) if one long map C is regular with full-rank limit, the
source lift of the target identity is regular, and its limiting image
`S(0) C(0)` has rank at least109. In particular, singular source units
of corank one are included. Independent source frames and varying
left inverses first force both other maps to be regular; the existing
ordinary-map obstruction finishes the argument. Every finite pole order
is covered. Claims `AI-PARTIAL-UNIT-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-EXCLUSION-002` are written and unreviewed. Exact finite
controls verify the rank budgets and projection recovery, without
formalizing the proof. The newer one-regular-leg theorem above removes
these unit-image and unit-lift hypotheses. The rank107 and rank105 unit-image results and asymmetric-frame
arguments remain scoped predecessor methods. The
[singular-long-rank continuation](research/ai/2026-10-23-singular-long-rank/proof.md)
and subsequent source-space caps further restrict singular leading maps
on both long legs; the general degeneration problem remains open. No matrix target or smaller exponent is established.

## Exact pure-fiber curves and the complete third-order criterion

The [pure-fiber proof](research/ai/2026-10-23-conic-pure-criterion/proof.md)
certifies PR101's d=0, c=0 specialization as an exact polynomial
rank-twelve incidence curve for every complex a,b, with map degrees at
most two and one. All coefficients on the fixed 100-dimensional source
kernel vanish; the leading minors are1,1,-1. Together with the mixed
three-jets and earlier exact linear components, this makes the complete
order-three projective normal-class existence criterion identical to
the order-two criterion: `(a-c)*(b+c)*(c*lambda^3+mu^3)=0`.
Claims `AI-CONIC-PURE-CURVE-003` and `AI-CONIC-THIRD-CRITERION-004` are
written and unreviewed. Mixed fourth-order/all-order lifting and the
full matrix target remain open. No smaller exponent is established.

## Finite covers close the selected nonsplit coordinate targets

The [actual nonsplit source certificate](research/ai/2026-10-21-sl2-finite-slices/proof.md)
gives a 98-slice cover for SL(2,F5), excluding M10 in characteristic two
and in the maintained one-copy coefficient-one coordinate/potential
class over C. For SL(2,F5) x C2 its cube has a 6155844-slice cover, below
2535^2=6426225. Cyclic symmetry gives abc<=2481 for any single rectangular
target, excluding the selected M(13,13,15). Independent replay checks
rank120, all1728000 original nonsplit coefficients, full block degrees,
and grouped cube coordinate counts with multiplicity13824000. Claim
`AI-NONSPLIT-FINITE-COVERS-001` is written and unreviewed. Together with
the split-cover result, this closes the three selected one-copy
central-cover coordinate/potential targets. General complex input mixing,
other targets and arbitrary higher source powers remain open. No smaller
exponent is established.

## Disjoint unimodular units and the all-size singular-space cap

The [all-size packing proof](research/ai/2026-10-23-all-size-unit-packing/proof.md)
constructs a^2 disjoint unimodular source slices for every balanced size
a>=1. A short polynomial recurrence proves their invertibility over
every field, including characteristics dividing a. Consequently every
complex linear source subspace consisting entirely of singular matrices
has dimension at most a^2(2a-2), attained by a zero-row kernel. The proof
uses the earlier elementary distinct-weight limit for arbitrary dense
subspaces. Claims `AI-ALL-SIZE-RESIDUE-UNITS-001` and
`AI-ALL-SIZE-SINGULAR-CAP-002` are written and unreviewed. Finite exact
controls check21 integer determinants,63 independent modular determinants
and70 recurrence identities, without supplying the universal quantifiers.
The theorem does not establish regular target maps or the needed partial
frames. No matrix construction or exponent improvement follows.

## Sharp singular-source-space cap and first leading rank

The [source packing proof](research/ai/2026-10-23-source-singular-space-cap/proof.md)
shows that every complex linear subspace of A4 consisting entirely of
singular matrix slices has dimension at most96, attained by a zero-row
kernel. Sixteen disjoint unimodular unit supports and a diagonal action
with112 distinct source weights prove the all-subspace bound. Exact
replay checks all200704 entries of a second Kronecker factorization,
four28-square integer determinants and all4096 source weight identities.
Consequently, in any A4 to M(10,10,11) Laurent degeneration with a regular
first lift and109 regular independent selected long-map columns, the
leading first image must be entirely singular and have rank at most96.
Claims `AI-SOURCE-SINGULAR-CAP-001` and
`AI-A4-FIRST-LEADING-RANK-002` are written and unreviewed. No injective
leading first map is assumed. Polar first maps and cases without the
partial long frame remain outside the result; no exponent improvement.

## Unequal partial frames and the rank106 regular unit-image chart

The [asymmetric-frame proof](research/ai/2026-10-23-asymmetric-regular-frames/proof.md)
weakens the full regular unit-image threshold from109 to106. It excludes
A4 to M(10,10,11) with one regular full-rank long map and regular unit
lift whenever `rank(S(0) C(0))>=106`, including every source unit of
corank at most four. More generally,107/109 and106/110 partial frames
suffice, allowing poles in unselected coefficients. The target identity
upgrades the limiting opposite long-map rank after first-map regularity.
The complete12100-pair strict-budget scan has nine sufficient pairs and
two minimal pairs. Claims `AI-ASYMMETRIC-FRAME-REGULARITY-001` and
`AI-A4-UNIT-IMAGE-106-002` are written and unreviewed. Finite controls
pass; frame existence is a hypothesis, rank105 is outside this argument,
and no matrix construction or exponent improvement follows.

## Partial regular frames with polar map coefficients

The [partial-frame proof](research/ai/2026-10-23-partial-regular-frames/proof.md)
extends the regular-unit-image argument. For A4 to M(10,10,11), it is
enough that 109 selected columns of C and of their source-unit image
are regular with rank109 limits. All other C and unit coefficients may
have poles. A unit-free version uses independent partial right and left
frames for the long maps. The argument forces B, then F, then C regular
using all three source contraction minima, and applies the existing
ordinary rank contradiction. Claims `AI-PARTIAL-FRAME-REGULARITY-001`
and `AI-A4-PARTIAL-FRAME-EXCLUSION-002` are written and unreviewed.
Exact finite matrix controls pass. Such frames are hypotheses; their
existence in arbitrary degenerations is unproved, and rank108 remains
outside the strict dimension argument. No exponent improvement.

## Complete affine conic tangents and second jets

The [conic second-jet proof](research/ai/2026-10-21-conic-second-jets/proof.md)
computes the complete seventy-dimensional tangent module of the rank-twelve
incidence of two fourteen-row maps of the canonical source. Its boundary
family has dimension68 and uses three independent polynomial planes.
For every affine a,b,c and every nonzero normal class[lambda:mu], some
representative extends through order two exactly when
`(a-c)*(b+c)*(c*lambda^3+mu^3)=0`. All68 boundary motions are included;
pure fibers are checked separately from the mixed Laurent chart.
An exported polynomial two-jet on c=-d^3 passes direct all-source replay,
including d=0, while its uncorrected third coefficient has184 nonzero
entries. The other two factors admit exact linear incidence curves.
Claims `AI-CONIC-TANGENT-001`, `AI-CONIC-SECOND-JET-002` and
`AI-CONIC-POLYNOMIAL-JET-003` are written and unreviewed. The later
polynomial-curve package completes affine all-order existence for a suitable
first representative, and the projective criterion above covers every
base chart. On d=0, `AI-CONIC-D0-EXACT-CURVE-001` separately preserves
PR101's fixed polynomial two-jet. Prescribed-jet questions, the separate 12-by-8 problem and the
full matrix target retain their separate scopes. The exponent remains 9/4.

## A singular-unit resolvent chart

The [resolvent proof](research/ai/2026-10-21-singular-unit-resolvent/proof.md)
excludes A4 to M(10,10,11) with constant PC=I110 and
B(t)=P(tI112+N)^(-1), where N is the specified normalized square-zero
coordinate slice, whenever the displayed limiting candidate space has
dimension 112. It allows every finite Laurent pole order in the first
map and arbitrary constant target bases. An exact integer/modular
certificate proves the rank hypothesis on a nonempty open dense set of
compression pairs. A source grading supplies a proper invariant space
whose dimension is indivisible by 10, contradicting a normalized Mat10
action. Claim `AI-CYCLIC-SINGULAR-RESOLVENT-001` is written and unreviewed.

This singular unit lift is outside the earlier regular-invertible-unit
chart. Rank-drop compression pairs, moving compressions and other unit
trajectories remain open. No general A4 exclusion or exponent gain follows.

## Finite cube bounds split-cover coordinate target volume

The [full-source cube certificate](research/ai/2026-10-21-central-cover-finite-slices/proof.md)
gives a characteristic-two slice cover of 973422 for `(A5 x C2)^3`, below
the exact finite slice rank 1000000 of M1000. Cyclic symmetry gives the
single-target volume bound abc<=986. It excludes the maintained one-copy
coefficient-one coordinate/potential M10 and M(9,10,11) constructions in
the split cover. The verifier checks all 216000 A5 coefficients and enumerates
all 1728000 one-leg cube coordinates. A direct argument from the external
arbitrary-field bounded-rank matrix-space theorem supplies the target
lower bound. Claim `AI-SPLIT-COVER-CUBE-EXCLUSION-001` is written and
unreviewed. The separate nonsplit note above addresses its selected
coordinate targets. General complex degenerations and constructions
from arbitrary higher powers remain open. No smaller
exponent is established.

## Regular unit charts and full-source calibrations

The [unit-chart proof](research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md)
excludes A4 to M(10,10,11) at every Laurent order when one long map is
regular with full-rank limit and a target identity has a regular source
lift with invertible limiting slice. The other long map and remaining
first-map coefficients may have arbitrary finite poles. Regularized
correction products have rank at most two; the source minimum rank 16
eliminates first-map poles and then forces 100 dimensions into at most 98.
Claim `AI-CYCLIC-REGULAR-UNIT-003` is written and unreviewed. Singular
long-leg limits and singular or polar unit lifts remain outside it.

The [integer slice proof](research/ai/2026-10-21-cyclic-slice-determinants/proof.md)
gives a literal unimodular full-rank slice of A_a for every a>=1 and every
field. At a=2,3,4, exact Krylov/Bezout certificates prove the full source
determinant is reduced over C; its submaximal minors have no nonconstant
common divisor. Normalized slice commutators also attain full rank in
those sizes. These calibration facts reject two proposed full-source invariant
premises. They do not exclude matrix targets or factor arguments after
compression or leading-flag restriction. Claims `AI-CYCLIC-UNIMODULAR-001`
and `AI-CYCLIC-REDUCED-DETERMINANTS-002` are written and unreviewed.
The general singular A4 target and exponent question remain open.

## Characteristic-two source-cost barrier for the central covers

The [A5 tight-limit certificate](research/ai/2026-10-21-a5-peirce/README.md)
checks an explicit basis and all 216,000 source coefficients, giving a
tight 277-term limit. A rational distribution and integer entropy
comparison prove a written lower barrier for asymptotic slice-rank costs
in characteristic two: above 517/5 for A5 x C2 and SL(2,F5), and above
976613/5000 for SL(2,F5) x C2. An explicit central-cover limit transfers
the certificate to both covers. These values exceed the selected M10
and cyclic M(13,13,15) comparison thresholds, so eventual global source
slice-rank bounds of this kind cannot close those targets. This barrier
alone leaves finite-power tests and constructions undecided; the separate
cube result above now closes the one-copy split-cover coordinate class.
Claim `AI-CENTRAL-COVER-SLICE-BARRIER-001` is written and
unreviewed; no smaller exponent is established.

## Modular SL(2,F8) bound across source powers

The [modular source proof](research/ai/2026-10-21-sl2-f8-modular/proof.md)
constructs an exact 125-dimensional semisimple quotient over F2 and F8,
certifies a 379-dimensional nilpotent kernel, and separates the 64-dimensional
central summand. The resulting all-power coordinate/potential slice bound
is 1035637/2304, below 450. It excludes the joint six M(8,9,9) packets plus
M7 across source powers, extending the prior one-copy coordinate assembly
obstruction. All 16 general-test single-matrix survivors remain unexcluded,
including M(18,18,25). Claim `AI-SL2-F8-MODULAR-001` is written and
unreviewed; arbitrary complex maps and the exponent goal remain open.

## Complete subgroup-ideal catalog

The [complete finite catalog](research/ai/2026-10-21-subgroup-ideal-catalog/README.md)
certifies all 455 subgroups in 65 conjugacy classes of the three active
central-cover sources. Integer annihilators and matching modular ranks
give every averaging-ideal dimension. In PSL(2,5) x C2, noncyclic
order-four and order-six subgroups add 550 minimal forbidden cosets per
leg of M10 beyond central pairs and the earlier five-cycle cuts.
The other two specified targets have no additional minimal subgroup
coset cuts. This is completeness for a finite necessary-condition method,
not exclusion of the targets. The weighted 3-by-3 control passes. A new
600-second search reached 34 model events and 32 replayed parity
contradictions with no pair-injective lift; it ended at its time limit.
Claims `EXP-SUBGROUP-IDEAL-CATALOG-001`
and `AI-SPLIT-NONCYCLIC-COSETS-001` remain finite or written and unreviewed.
Arbitrary complex maps and the exponent below 9/4 remain open.

## Complete coupled boundary rank-two reduction

The [coupled cubic proof](research/ai/2026-10-21-coupled-boundary-rank-two/proof.md)
shows that both canonical boundary obstruction matrices have rank at most
two precisely when both are zero. Its 232 universal determinant identities
reduce the normal dimensions 228 to 96, 56, 32 and 28. An invertible
coefficient transformation identifies the final space with the complete
biform normal family. Combined with the sharp balanced gap and prior
projective classification, this gives the necessary conic classification
for non-plane balanced boundary normals under the credited third-gap
conditions. Four focused tests pass. Later compatibility, an all-order
10-by-10 conclusion, the separate 12-by-8 case and a matrix target remain
open. These proofs are written and unreviewed; the exponent remains 9/4.

## A gap for balanced two-dimensional boundary quotients

The [gap proof](research/ai/2026-10-21-balanced-puncture-gap/proof.md)
shows that a complex rank-one-free matrix space of dimension at least
two, amplified by Mat2 and quotiented by kernels of size at most two
on each leg, leaves first dimension zero or at least three. The bound
is sharp. Its constant-rank-two reduction imports the classical complex
Kronecker form, with the rank cases and quotient arguments supplied.
Within the actual 28-dimensional boundary normal family, low first rank
at most two therefore forces complete cancellation, whose projective
survivors were already classified. The coupled cubic proof now supplies
entry into that family from the two rank bounds. Six focused tests and
the registered 423801-pair finite pilot retain separate scopes. The proofs
are written and unreviewed; no matrix target or smaller exponent.

## Finer full-source S5 covers exclude five further coordinate targets

The [full-source refinement](research/ai/2026-10-23-s5-peirce-covers/proof.md)
lowers the two cube bounds to 6638912 and 41159136, giving one-copy
single-target volume caps 2576 and 6415. It excludes five more shapes
for S5 x C2^2, leaving four in the pinned frontier; the two S5 x C2
shapes, including M(13,14,14), remain open. The verifier checks an
invertible 120-vector binary basis, all 1728000 original group-trace
coefficients, and eight explicit covers using finer principal-block
degrees. Claim `AI-S5-PEIRCE-COVERS-003` is written and unreviewed.
The complex implication is restricted to the maintained coefficient-one
coordinate/potential model; no exponent improvement is established.

## Blockwise modular bounds for S5 central sources

The [central-block proof](research/ai/2026-10-21-s5-block-filtration/proof.md)
splits F2[S5] into exact 88- and 32-dimensional blocks and counts their
radical flags separately. It gives an all-power, joint-rectangular bound
for coordinate/potential constructions in S5 x C2^r. In particular the
source with two central factors has asymptotic slice rank below 389.
This excludes M(20,20,20) and M(19,20,21), two formats which pass the
existing complex rank-locus and every full Koszul test. The M19 and
one-factor M(13,14,14) targets remain unconstructed and unexcluded by this
bound. Claim `AI-S5-BLOCK-FILTRATION-001` is written and unreviewed;
arbitrary complex maps remain open and no smaller exponent is established.

## Balanced punctures of the third biform core

The [balanced-puncture proof](research/ai/2026-10-21-biform-balanced-puncture/proof.md)
classifies complete cancellation at the 10-by-10 boundary threshold. The
full auxiliary matrix action forces product quotient kernels; the biform
syzygy space has dimension at most three. The actual core is now
classified on every projective chart: non-plane cancellations occur
exactly for `g=(r*x0+s*x1)*(r*y0-s*y1)`, with arbitrary residual linear
forms and a two-dimensional normal fiber. Sixteen disjoint cases with
constant unit minors and exact residual identities cover every complex
parameter value. Nine focused tests pass. These are written, unreviewed
structural results. Projected first ranks one/two and later coefficients
remain open. No matrix target or exponent improvement is established.

## Stronger ordinary slice spans from reflexive closures

The [reflexivity application](research/ai/2026-10-21-semisimple-reflexive/proof.md)
uses Ambrozie--Kuzma--Muller's2010 theorem and its finite-domain proof to
strengthen the ordinary slice-span lower bound. It excludes ordinary
restrictions3*M7 ->M11+M4 by18>16 and(M1+4*M7+M8) ->(3*M9+M3) by40>9.
Both pass the other recorded rank tests and remain open for singular maps.
Exact Jordan and Hankel controls attain the required rank-one span bounds.
The larger packet target's ordinary exclusion strengthens to136>49.
Claim027 is a written, unreviewed application of the credited external
theorem. Conditional numerical gates do not supply the missing maps or
an exponent improvement.

## Closed determinant factors for square semisimple targets

The [low-rank span proof](research/ai/2026-10-21-semisimple-low-slices/proof.md)
excludes arbitrary ordinary restrictions to the conditional499-dimensional
rectangular packet target. A separate determinant-factor proof persists
under singular limits for square-block targets. It excludes
4*M7 ->2*M9+M4+M3+M2, although every full Koszul and rank-locus dimension
test passes. The rectangular packet target has zero generic slice
determinant and remains outside that border obstruction. An exact
[mixed local map](research/ai/2026-10-21-semisimple-low-slices/mixed_packet.md)
has complete Laurent coefficient cancellation; it is equivalent to one
earlier punctured packet and supplies no joint assembly. Claims024-026
are written and unreviewed. No smaller exponent is established.

## SL(2,F8) local packets and a conditional joint target

The [torus packet proof](research/ai/2026-10-21-sl2-f8-ideals/torus_note.md)
constructs local M(8,9,9) degenerations and gives full-coset exclusions
using the classical smallest Ree-unital incidence. The proposed joint
target of six balanced punctured packets plus M7 would imply omega<=2.24,
with exact interval and necessary rank certificates. Its joint source map
is missing. The [positive-marginal proof](research/ai/2026-10-21-sl2-f8-ideals/assembly_note.md)
excludes an injective group-basis/diagonal assembly of that target.
Claims021-023 are written and unreviewed or explicitly conditional.
Arbitrary complex input maps remain open; omega remains9/4.

## Uniform Hankel caps and dimension refinements

The [Wronskian proof](research/ai/2026-10-21-hankel-wronskian-cap/proof.md)
gives dim L<=r for every characteristic-zero linear space of a-by-b Hankel
matrices of rank at most r<min(a,b), with an exact rational witness generator.
The package also proves [scalar-Hankel saturation at its dimension equality](research/ai/2026-10-21-hankel-wronskian-cap/boundary_saturation.md)
and [a dimension loss for proper crossed-rank parameter images](research/ai/2026-10-21-hankel-wronskian-cap/proper_sections.md).
The [exact application](research/ai/2026-10-21-hankel-wronskian-cap/application.md)
adopts the concurrent rectangular worker's higher-input-rank and bundle
bounds with source credit. It closes every improving ordinary A9 square
sum, and a proper-section equality case at A12. Its240 balanced rectangular
survivors are a pinned comparison, not the full concurrent all-source frontier.
All proofs remain written and unreviewed. No target maps or exponent gain.

## S5 split-source continuation

The [S5 x C2 package](research/ai/2026-10-21-s5-split/README.md) derives
an exact conditional2.247 comparison for M(13,14,14), with margin verified
using integer root intervals. Its actual weighted3-by3 control passes.
Two SAT runs reached their600-second limits without a projected model;
the local runs exported32 exact parity contradictions and no lift, all
replayed. A finite F2 ideal certificate checks the radical
powers and leaves the target unexcluded by that filtration. Claims
`AI-S5-SPLIT-028` and `EXP-S5-RADICAL-029` are conditional/finite. The target
and any smaller exponent remain unconstructed.

The same source investigation now checks S5 x C2 squared and its
conditional M19 gate at2.247. A600-second native run found no pair model.
A [central four-point matching lemma](research/ai/2026-10-21-s5-split/central_slice_proof.md)
adds a written unreviewed necessary cut beyond pair injectivity and the
existing commuting trades. Its finite control has an exact five-row
Farkas circuit. The smaller M(18,18,20) projected run exported one such
cut and no lift; direct colored search reached two collisions. The
alternative S5 x C4 basis has the same conditional degree cost, with its
four-matching obstruction following from pair injectivity alone.
The warm colored continuations reached1,218 and1,427 pair-injective
models respectively; all have exactly replayed Farkas contradictions.
The sampler now incorporates the existing commuting-trade condition.
The trade-guided continuation adds27 exactly refuted pair models;25
also survive the central matching cut. Claims031/032/033 supply no
improving target or smaller bound.

## Subgroup-ideal cuts on the central-cover targets

The [subgroup-ideal proof](research/ai/2026-10-21-subgroup-ideal/proof.md)
shows that a full subgroup coset in one coordinate vertex set bounds the
other-pair product by dim C[G]e_HC[G]. Exact five-cycle dimensions80,88,160
exclude such cosets in all legs of the two M10 targets and the order240
M(13,13,15) target. Integer annihilator and modular lower-rank certificates
replay, including a real positive equality control. The revised split-cover
search uses these necessary cuts. Claim `AI-SUBGROUP-IDEAL-027` is written
and unreviewed; the targets outside this coset condition remain open and
the exponent remains9/4.

## Scalar repairs and a rank obstruction

The [scalar repair continuation](research/ai/2026-10-21-s5-scalar-repair/proof.md)
gives a conditional2.2499 route from the S5 source plus eight scalar
tensors; its improving witness is missing. A new diagonal matrix argument
shows that bad extras on q output coordinates need auxiliary rank at
least q, even with arbitrary Laurent correction maps. Nine exactly
verified Farkas circuits on disjoint coordinate sets exclude rank-eight
corrections for the first trade-free pair model, for every integer vertex
potential. The general group input maps and other vertex sets remain open.
Claims034/035 are conditional/written-unreviewed, without an exponent gain.

## Joint central-sign search in SL(2,5)

The [joint sign investigation](research/ai/2026-10-20-sl2-five-native-parity/README.md)
adds a native encoding and conditional parity learning for the open
M(10,10,10) target. Two 600-second searches found no pair-injective lift.
All 506 exported parity contradictions replay exactly, with positive and
negative encoding controls. This is a finite discovery result
(`EXP-SL2-NATIVE-024`), not a source exclusion. The source and its conditional
2.247 comparison retain their existing attribution; no bound was improved.

The same package now derives an exact source certificate for the split
cover PSL(2,5) x C2, with degrees two copies of1,3,3,4,5. Its M10 target
passes the conditional2.247 gate and the rank-locus screen, and a genuine
weighted3-by3 control passes. This is the new conditional lead
`AI-SPLIT-COVER-SOURCE-026`; the improving target remains unconstructed.
Complete projected triple-translation classes encode the necessary pair
capacity without relying on an SL(2,5) cocycle.

## Ferrers ruling caps and low-rank dominance

The [sharp ruling proof](research/ai/2026-10-21-ferrers-ruling-cap/proof.md)
reduces a bilinear quotient's bilateral k-input dimension bounds to exact
Ferrers budgets by the classical Borel fixed-point theorem. Its
[dominance continuation](research/ai/2026-10-21-ferrers-ruling-cap/dominance.md)
strengthens closed-target saturation using the dimension of contained
linear spaces. The [finite application](research/ai/2026-10-21-ferrers-ruling-cap/application.md)
adds67 exclusions to PR83's balanced rectangular comparison, leaving173
necessary-test survivors through a12, and tightens three square-score
ceilings. It is not the full concurrent all-source frontier. The proofs
remain written and unreviewed; no tensor construction or smaller exponent.

## Modular obstruction for small Heisenberg sources

The [modular application](research/ai/2026-10-20-heisenberg-seven/modular_proof.md)
of Petrov's external filtration excludes coordinate/potential constructions
passing the ordinary degree gate for every tensor power of H_p, for each
odd prime p<=47. It covers finite rectangular direct sums through cyclic
symmetrization and the credited tight-support entropy theorem. Exact rational
certificates and 1,485 finite group-algebra generator controls accompany
written, unreviewed claim `AI-HEIS-MODULAR-025`. Arbitrary complex maps remain
open; no smaller exponent was established. This retires the earlier bounded
H_7 coordinate searches for this gate.

## Hankel pencils and the ordinary frontier

The [linear-annihilator proof](research/ai/2026-10-21-hankel-pencil-degree/proof.md)
bounds Hankel Segre images when1<=r<min(a,b) and5r<2(a+b), using the classical
index sum theorem and a kernel-bundle calculation. It extends the earlier
fixed-scheme and first-boundary ranges; all claims remain written and
unreviewed. The [exact application](research/ai/2026-10-21-hankel-pencil-degree/application.md)
adds453 exclusions to the5139-format balanced rectangular scan through a12.
Every improving ordinary single rectangular target through a9 is excluded;
494 necessary-test survivors remain, first at a10. All improving ordinary
A8 square direct sums are also excluded. The later
[Wronskian application](research/ai/2026-10-21-hankel-wronskian-cap/application.md)
already excludes every improving ordinary A9 square sum, including
(32,6,3); the older pencil-degree report is preserved as historical data.
Singular degenerations remain open; no smaller exponent is established.

## Expanded ordinary search

The size2000 scan covers110 formats and5741 score-eligible single targets, with427076 exact Hankel minor checks. After the separately written critical-state obstruction,74 ordinary candidates remain. The first is A(7,12) to M(35,35,35). All74 candidates fail the fixed-diagonal SL2 matrix-vertex capacity test, including both permitted parity sectors, but remain open without that symmetry restriction. See [the expanded frontier](research/ai/2026-10-21-rectangular-direct-sums/single_frontier.md). No smaller exponent is certified.

## Written obstruction for the last ordinary single target

The [critical-state argument](research/ai/2026-10-21-rectangular-direct-sums/critical_finite_states.md) excludes the remaining A(8,10) to M(32,33,33) ordinary restriction, subject to its written, unreviewed lemmas. A new graded-module argument handles generic finite realization outside low-outer-rank compressions. Uniform finite-state fibers and support velocities then obstruct the target leg. Exact controls cover all22 partitions of8 and the exceptional Jordan pairings. This is not independent certification, and singular degenerations and multiple-block candidates remain open. The associated finite filter removes62 of752 prior two-block survivors, leaving690. No smaller exponent has been established.

## Ordinary two-block ruling refinement

The [ruling refinement](research/ai/2026-10-21-rectangular-direct-sums/ruling_two_sums.md)
excludes3717 of4469 hash-verified predecessor targets, retaining664 at
A(8,10) and88 at A99. All50 at A89 are excluded. Together with the
single-target scan, this closes improving ordinary one- and two-block
targets through source leg dimension1152. General lemmas remain written
and unreviewed; singular degenerations and three or more blocks remain
open. The exponent remains9/4.

## Uniform mixed-axis closure

The [auxiliary-projection proof](research/ai/2026-10-21-mixed-axis-incidence/proof.md)
closes the ten-dimensional family left by claim091, for every complex a
and nonzero t at b=1. A polynomial rank13 minor remains nonzero over
C(ell) at every parameter pair. Its two-dimensional relation space has
only one rank-one direction; applying this to two identical blocks and
then two cubic minors leaves only the four common-plane normals.
Claim `AI-MIXED-AXIS-CLOSURE-092` is written and unreviewed. It excludes
this axis under the prior shifted induction; general mixed-row graphs
remain open. The exponent remains9/4.

## Every projective rank-one partner in the seven-by-five class

The [projective closure](research/ai/2026-10-21-all-rankone-seven-five/proof.md)
reconstructs the remaining coordinate endpoint and eliminates all84
non-plane normal coordinates with28 actual source slices. Physical source
reversal is checked on all4096 terms, leading lines and mixed bases.
Together with the adopted finite affine chart, this covers every nonzero
projective rank-one partner for canonical full-B seven versus arbitrary
mixed C five first spaces, including every graph and boundary four-space.
Claim `AI-ALL-RANKONE-SEVEN-FIVE-101` is written and unreviewed. Smaller
first spaces and other leading flags remain open; the exponent remains9/4.

## Complete finite affine rank-one partner chart

The [affine-chart proof](research/ai/2026-10-21-affine-partner-chart/proof.md)
closes the punctured b=0 boundary by a fresh rational calculation at(1,0)
and a checked source torus. Both complete necessary normal families close:
stable54->14->6->4->0 and rank-one projection48->10->4->0. The existing
corner verifier is replayed. Adopting099 for b nonzero now covers every
finite complex pair(a,b), with every mixed graph and boundary four-space.
Claim `AI-AFFINE-PARTNER-CHART-100` is written and unreviewed. The two
projective endpoints, smaller first spaces and other leading flags remain
outside this result. The exponent remains9/4.

## Every graph on the full normalized partner line

The [full-line proof](research/ai/2026-10-21-full-partner-line/proof.md)
closes every complex a on b=1 for the canonical full-B seven-frame against
an arbitrary mixed C five-space. Seventy-nine verified maximal minors
leave only a=0 and a^3=1 as candidates. A checked original-source phase
automorphism covers the cube roots of one, and a complete rational source
replay closes0. Only the four common planes remain, for every graph and
boundary four-space. The adopted induction excludes M(10,10,11) with
arbitrary later maps; the torus extends to every b nonzero. Claim
`AI-FULL-PARTNER-LINE-099` is written and unreviewed. The b=0 boundary and
other first-space/flag classes remain open; the exponent remains9/4.

## Every graph outside finitely many partner values

The [generic-partner proof](research/ai/2026-10-21-generic-partner-all-graphs/proof.md)
excludes every mixed graph and boundary four-space at each a in a nonempty
open subset U of the partner line b=1, containing2. Uniform54/48 enclosures,
exact source/cubic identities over Q(a), and79 rank guards leave only the
four common planes. The adopted induction excludes M(10,10,11) there for
arbitrary later maps; the torus extends to b nonzero with a/b in U.
Claim `AI-GENERIC-PARTNER-ALL-GRAPHS-098` is written and unreviewed. The
finite candidates are subsequently covered by claim099 on all of b=1.
This excludes every graph at a good partner, rather than only generic
graphs. Other flags and sources remain open; the exponent remains9/4.

## Every mixed graph at the equal nonzero partner

The [all-graph proof](research/ai/2026-10-21-all-mixed-graphs-a1/proof.md)
closes the canonical full-B seven-frame against every mixed C five-space
at a=b=1, including all six graph coefficients and arbitrary boundary
four-spaces. Uniform source equations, exact cubic identities and an
exhaustive four-branch split leave only the four common planes. The
adopted shifted induction excludes M(10,10,11) for arbitrary later maps;
the source torus extends this to a=b nonzero. Claim
`AI-ALL-MIXED-GRAPHS-A1-097` is written and unreviewed. Claim098 now covers all but finitely many partner values on b=1;
claim099 closes the whole normalized partner line. Other boundaries and
flags remain open. The exponent remains9/4.

## A uniform mixed-normal dichotomy

The [all-graph reduction](research/ai/2026-10-21-global-mixed-normal-dichotomy/proof.md)
at a=b=1 encloses every necessary normal, modulo the four common planes,
in two fixed linear families of dimensions54 and36. Eight rational square
identities and four polynomial mixed-row identities force the rank-one
projection alternative to projection zero for all six graph coefficients,
including exceptional fibers. Claim `AI-GLOBAL-MIXED-NORMAL-DICHOTOMY-096`
is written and unreviewed. Claim097 subsequently eliminates both families
at this partner. The dichotomy itself does not assert an exponent gain.

## An affine family of larger mixed normal spaces

The [exceptional affine-family proof](research/ai/2026-10-21-mixed-exceptional-affine/proof.md)
gives h=(x-y,1-x-z,1-x,x,y,z), at a=b=1, with necessary normal dimension
at least38 everywhere and exactly38 generically. Two degree-two polynomial
left-relation certificates prove the all-parameter rank upper bound.
At h=(0,1,1,0,0,0), a complete38-dimensional kernel, square minors and
additional source equations eliminate all34 non-plane directions; the
adopted induction excludes M(10,10,11) there for arbitrary later maps.
Claim `AI-MIXED-EXCEPTIONAL-AFFINE-095` is written and unreviewed. Its entire
affine family is now included in claim097 at the same partner.

## An open set of arbitrary mixed graphs

The [generic graph proof](research/ai/2026-10-21-generic-mixed-graphs/proof.md)
excludes the canonical seven-by-five target case on an explicitly defined
nonempty Zariski-open set of all six graph coefficients and a at b=1.
A rational point certificate uses two fourteen-variable normal blocks:
559 cubic minors in each generate all2380 quartic forms. Exact rank
modulo32003 proves the relevant rational minors are nonzero. Symbolic
source blocks and a fixed normal chart make this an open-set theorem,
not an extrapolation to all parameters from a finite test. The checked
torus extends it to an open set for b nonzero. Claim
`AI-GENERIC-MIXED-GRAPHS-094` is written and unreviewed. A remaining target
would require its entire affine four-plane of graph representatives to
lie in the exceptional fiber. Claim097 closes all graphs at a=b nonzero;
claim098 reduces the remaining partner chart to finitely many values.
The exponent remains9/4.

## Two-coordinate rank strata and exceptional graph closure

The [two-coordinate chart proof](research/ai/2026-10-21-mixed-two-coordinate-chart/proof.md)
classifies every complex parameter pair in m+t*d0+h*d1 at a=b=1:
normal dimensions32 off two points,36 at the origin and34 at (1,1).
A polynomial frame is complete away from those points, certified by
matched minors and all complex exceptional-root controls. The full
exceptional normal system at (1,1) reduces to the four plane directions
and excludes that graph under the prior shifted induction. Claim
`AI-MIXED-TWO-COORDINATE-STRATA-093` is written and unreviewed. The subsequent
claim097 excludes this whole target chart; the exponent remains9/4.

## Uniform mixed-axis reduction

The [axis reduction](research/ai/2026-10-21-mixed-axis-family/proof.md) covers every complex a
and nonzero t for the mixed row m+t*d0 at b=1. A rank minor t^18 and
Laurent-unit certificates reduce the initial32 normals to four plane
directions plus a necessary10-dimensional quotient family. Projection
minors work uniformly through all exceptional a values. Claim
`AI-MIXED-AXIS-REDUCTION-091` is written and unreviewed; its reduction
alone is not an axis exclusion. The subsequent claim092 above closes
its remaining family. The exponent remains9/4.

## Four mixed five-space graph families

The [graph-family proof](research/ai/2026-10-21-mixed-five-space-graphs/proof.md) excludes four specified
nontrivial mixed rows at partner a=b=1, with arbitrary four-dimensional
boundary parts. Exact quadratic-minor spans over Q force a stable-row
kernel, and target-slice equations reduce its dimensions10->2->0. The
modular calculation certifies rational rank and applies over C. Claim
`AI-MIXED-FIVE-GRAPH-CONTROLS-090` is written and unreviewed. Fifteen
parameterized graph charts still need analysis; the exponent remains9/4.

## Pure mixed five-spaces on the nonzero partner chart

The [pure-row five-space proof](research/ai/2026-10-21-pure-mixed-five-spaces/proof.md)
forces only plane normals when the B first space is the full seven-frame
and the C five-space contains its pure mixed partner, for every chart
parameter with b nonzero. A stable row subspace and a minimum-rank-two
projection split32 quotient parameters into families of dimensions6 and14;
both vanish under the remaining target conditions. All complex a are
covered polynomially after b=1 normalization, including coalescing modes.
Claim `AI-PURE-MIXED-FIVE-SPACES-089` is written and unreviewed. General
mixed-row graphs remain open, and the exponent remains9/4.

## Uniform adapted mixed source slices

The [adapted-source proof](research/ai/2026-10-21-mixed-five-space-uniform/proof.md)
extends the first sixteen low-rank source slices across the entire
two-parameter rank-one partner chart. Their projected third slices have
only the mixed B row remaining and must vanish in a matrix-target lift.
Claim `AI-MIXED-FIVE-SPACE-LOW-SLICES-088` has exact polynomial certificates
and a written unreviewed proof. The full five-space closure remains open
away from the earlier coordinate partner; the exponent is still9/4.

## Mixed seven-by-five coordinate partner

The [five-space point proof](research/ai/2026-10-21-mixed-five-space-residues/proof.md)
forces the four common-plane normals for every complex mixed five-space
opposite the full seven-frame at u=v=e3. Exact source-slice covers, cubic
minors and mixed-column equations give dimensions88,68,54,30,18,12,4.
The shifted induction excludes the matrix target at this partner and its
reversal. Claim `AI-MIXED-FIVE-SPACE-POINT-087` is written and unreviewed.
Other partner lines remain open; the exponent remains9/4.

## Arbitrary mixed hyperplanes on either leg

The [mixed-hyperplane proof](research/ai/2026-10-21-rankone-mixed-hyperplanes/proof.md)
excludes every rank-one mixed first pair with both effective dimensions
at least six, including arbitrary complex subspaces, graphs and delayed
unequal orders. On all228 normal parameters, each leg's rank-one obstruction
has only its mixed column remaining; a mixed hyperplane kills that column
without assuming opposite-leg equations. Claim
`AI-RANKONE-MIXED-HYPERPLANES-086` is written and unreviewed. The necessary
ordinary both-mixed first-rank sum is at most twelve, with only seven-by-five
rank-one pairs remaining at that threshold. The exponent is still 9/4.

## Uniform maximal rank-one mixed frames

The [seven-frame proof](research/ai/2026-10-21-rankone-seven-frames/proof.md)
excludes every maximal seven-by-seven rank-one mixed first pair at these
flags, with arbitrary graphs and delayed unequal orders. A fixed normal
minor stays nonzero polynomially over the entire parameter chart; only
four plane directions remain. Claim `AI-RANKONE-SEVEN-FRAMES-085` is
written and unreviewed. The necessary ordinary first-rank sum when both
mixed projections are nonzero is now at most thirteen. Smaller mixed
spaces and other flags remain open; the exponent remains 9/4.

## Invertible mixed lines: all-order output-growth obstruction

The new [five-frame proof](research/ai/2026-10-21-invertible-five-frame/proof.md)
excludes every compatible invertible mixed-line first pair at the canonical
flags, including arbitrary boundary graphs and delayed unequal orders.
A rank-ten cross and exact five-dimensional annihilators force both output
maps to have generic rank at most five. Claim
`AI-INVERTIBLE-FIVE-FRAME-084` is written and unreviewed. Its separate cubic
control passes complete source replay through degree three; it supplies
no matrix target. The exponent remains 9/4. Rank-one mixed partners and
other first spaces remain construction questions.

Date: October 21, 2026.

**No improvement below $\omega\le9/4$ is established here.** The external baseline belongs to OpenAI. The initial local work analyzes a scalar relaxation and records finite searches.

## Nonlocal maps, exact projection cost, and source capacity

Three completed [nonlocal operator pilots](research/ai/2026-10-20-paired-direct-sums/q_metaplectic_history.md)
retain all saved maps, all 123 sampled records, and their actual
1,000-update stops. The Fourier/chirp/reflection basis depends on the
source size. Complete replays check 40,736 output positions; none gives
an exact matrix target. The first two error plateaus agree with a
separate rational projection construction. That literal projected
tensor has an error whose A-flattening contains
`(3/4) I_((n-5)^2)`, so its repair needs quadratic auxiliary border rank.
The floating-point maps are not exactified by this comparison, and
other joint maps remain open.

The [source-capacity proof](research/ai/2026-10-21-correction-budget/source_capacity.md)
gives a necessary condition even when auxiliary summands have singular
local maps. For fixed-width Q(n,b), a subquadratic border-rank correction
and positive limiting outer ratios imply
`rho*sigma<=1`, `rho*h<=b`, and `sigma*h<=b`. The target volume therefore
obeys `rho*sigma*h<=b`; changing the target shape cannot improve the
critical coefficient allowance beyond its equal-width, near-full value.
This is not a construction or a general exponent barrier.

A [source update](research/ai/2026-10-21-pass-packing/README.md)
records Rafael Pass's arXiv:2610.28627v1 constructive proof of the same
9/4 bound. Its generalized packing count suggests a scalar rule that
already follows exactly from the existing concavity and shifted-tripling
assumptions. This equivalence concerns that scalar rule, not the full
tensor maps or every possible use of the external construction.

Checkpoint `27d7a75`, integrating main `8a07bed`, completed 578 local
tests: 577 passed and one optional NumPy discovery control was skipped.
All five archive replays passed. The complete 638-line transcript and
machine-readable result are in its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint12-validation.json).
Five hosted static checks passed; no hosted test or archive job was
observed for that commit. This continuation incorporates main `b113866`,
including its sixteen-parameter mixed two-jet family and the fixed-space
third-coefficient obstruction. That obstruction retains its stated seed
scope and written, externally unreviewed status. The earlier test count
does not describe the enlarged tree.

## Critical correction allowance and new construction tests

The [critical-coefficient criterion](research/ai/2026-10-21-correction-budget/critical_coefficient.md)
allows a nonzero auxiliary border-rank coefficient at growth rate
`n^(3/2)`. For one unbounded, character-independent family
`Q(n,b) + R_n -> M(l_n,h,r_n)`, with limiting outer ratios rho and sigma,
the sufficient condition is
`limsup border-rank(R_n)/n^(3/2) < (rho*sigma*h)^(3/4) - (4/3)*sqrt(b)`.
At near-full width four, the coefficient `4/25` is admissible by an exact
rational comparison. This would imply a qualitative strict improvement
below 9/4. **The family is unconstructed, and no numerical exponent gap
is supplied by this conditional argument.**

For the fixed endpoint corner R, the [one-scalar proof](research/ai/2026-10-20-paired-construction/m1_corner_one_scalar.md)
excludes `R + D1 -> M4` even by degeneration, using a closed Grassmannian
incidence condition. The [two-scalar proof](research/ai/2026-10-20-paired-construction/m1_corner_two_scalar_ordinary.md)
excludes ordinary restrictions from `R + D2`; its projection argument
does not extend to arbitrary degenerations. A separate
[enriched leading-point gate](research/ai/2026-10-20-paired-direct-sums/r_enriched_lead_obstruction.md)
excludes every two-scalar placement in one specified Laurent chart.
The general border-D2 question remains open.

Two [completed additional pilots](research/ai/2026-10-20-paired-direct-sums/q64_m1_free_kernel_and_reduced_corner.md)
preserve the exact M1 lead while freeing its corner kernel, or seek the
diagonal-deleted M4 target from R. Both fail their full coefficient
conditions. Their saved maps, all 62 sampled history records, actual
1,500-update stops, and complete coefficient replays are retained.
Numerical small singular values are not exact rank certificates.

The [centered aggregation calculation](research/ai/2026-10-21-centered-orientations/README.md)
constructs four shared-input partial transposes with twelve corrections
of size `n^(4/3)`. Its leading source costs `n^2`; a separate six-factor
source has endpoint coefficient 64. Neither meets the paired-source
budget. A full-format closed-orbit argument prevents this fixed tensor
from degenerating to the same-orientation matrix target, and its literal
orientation repair has quadratic flattening rank. No map from Q is given.

Checkpoint `25600a7`, integrating main `e00622f`, completed 565 local tests:
564 passed and one optional NumPy discovery control was skipped. All five
archive replays passed. Its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint11-validation.json)
retains the complete transcript and final result. Five hosted static
checks passed; no hosted test or archive job was observed for that commit.
This continuation incorporates main `8a07bed` and the packages above.
The prior count does not describe the enlarged tree.

## Smaller leading maps and partial targets

The [endpoint corner calculation](research/ai/2026-10-20-paired-construction/m1_endpoint_corner.md)
constructs an exact `16 x 18 x 18` tensor R from Q(6,4). It then excludes
every degeneration of this R to M4: every restriction to the required
long-leg dimensions retains a nonzero slice of rank at most three,
whereas M4 has minimum nonzero slice rank four. The projective incidence
argument makes this obstruction closed under limits. The result concerns
the stated inherited corner kernel, not arbitrary Q(6,4) maps.

The [M1 leading-point package](research/ai/2026-10-20-paired-direct-sums/q64_m1_leading_history.md)
excludes one fixed sparse leading seed by a first-edge support deficit,
for all source outer sizes at least four. A different endpoint seed passes
that support test. Its three inherited outer rows leave exactly the
corner kernel used above. Two completed searches that let the leading
maps move retain all saved coefficients and sampled histories; neither
satisfies the Laurent equations or the necessary leading-rank condition.

The [partial-target proof](research/ai/2026-10-21-bulk-partial/README.md)
excludes another specified first-cross chart without assuming tight
saturation. A polynomial pencil over `C[u]/(u^4)` forces a required
rank-four edge to have rank at most two. Twelve bounded partial-target
probes also retain their maps and actual stops. No all-size bulk
construction has been found. Restoring the stated omitted diagonals
would have linear auxiliary rank if such a construction existed.

The [graded correction calculation](research/ai/2026-10-21-quantum-correction/README.md)
excludes up to four homogeneous scalar corrections for one fixed
root-of-unity quantum tensor and three specified assignments of six
corrections. Slice ranks and a nonzero normalized-slice commutator give
the exact obstructions. Ungraded maps and general Laurent families are
outside these results.

The [leading-M4 search archive](research/ai/2026-10-21-leading-m4-search/README.md)
preserves 39 terminal points from seven finite search families, their
available histories and discovery source snapshots. A standard-library
replay checks all 576 source terms and 4,096 output positions at every
point. No exact lead with the needed kernel dimension was found. The
archive documents a corrected norm-penalty derivative and preserves
the earlier runs as historical evidence. These points are not 39
independent restarts, and full intermediate maps were not retained.

A separate [history correction](research/ai/2026-10-20-paired-direct-sums/q64_ridge_metadata_correction.md)
restores 90 sampled ridge-parameter snapshots in three previously
published full-flag artifacts from their original emitted records.
The recorder now copies the mutable parameter list. Saved maps,
coefficient errors, actual stops, and mathematical statuses are unchanged.

Checkpoint `9d8b240`, integrating main `11aca0f`, completed all 485 local
tests successfully; all five archive replays and nine hosted checks also
passed. Its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint10-validation.json)
preserves the full machine-readable completion result. The separately
retained live text stream is incomplete and is identified as such.
This continuation incorporates main `e00622f` and the packages above;
the earlier test count does not describe that enlarged tree.

## Paired constructions with boundary and correction budgets

An [exact integer construction](research/ai/2026-10-20-paired-construction/outer_product_injection.md)
now gives `Q(5,4) -> M(4,4,4)`, and more generally
`Q(k+1,k) -> M(k,4,k)` for every k at least two. Two unimodular
polynomial-multiplication maps supply the local tensor maps. The small
witness has 25, 20, and 20 nonzero entries, all in `0,+1,-1`; all 400
source terms and 4,096 output coefficients are checked exactly. This
construction works over every field. It does not improve the exponent.
The same product-subspace method at fixed source width four requires
`2k<=n+3`, so it does not supply the needed near-full family at large n.

The [linear-correction criterion](research/ai/2026-10-21-correction-budget/README.md)
shows that an unbounded family `Q(n,4) + R_n -> M(n,4,n)`, with auxiliary
border rank at most `Cn` for a fixed C, would imply
`omega < 30000/13433 < 2.2334`. The same conclusion allows outer dimensions
`n-c` for any fixed c. The cyclic error terms vanish asymptotically, and
the strict rational comparison has an integer certificate. **These
construction premises remain unproved; this is not an achieved exponent.**

The [larger correction budget](research/ai/2026-10-21-correction-budget/superlinear_budget.md)
allows auxiliary border rank `O(n^alpha)` for any fixed `1<=alpha<3/2`.
Its conditional bound is `max(B_b,9/4-(3/2-alpha)^2)`, with B_b defined
by the existing source-profile equation. At width four, `alpha=4/3` or
`137/100` still gives `omega<30000/13433<2.2334`, if the unbounded
near-full construction exists. Even `o(n^(3/2))` would give a qualitative
strict improvement. This relaxes the missing construction premise; it
does not supply the required tensor maps.

The [ordinary narrow-source proof](research/ai/2026-10-20-paired-construction/narrow_ordinary_all_n.md)
excludes `Q(n,2) -> M(n,2,n)` for every n at least three. It uses a
classified two-dimensional kernel and the cited constant-rank matrix-space
bound. A [minimum-slice theorem](research/ai/2026-10-20-paired-construction/narrow_rank_locus.md)
gives `rank Q(n,m)(X) >= rank(X)+m^2-1`; the minimum locus consists exactly
of rank-one X. Full narrow long-leg quotients lose at most one first-leg
direction. The [regular-long-leg extension](research/ai/2026-10-20-paired-construction/narrow_regular_long_legs_obstruction.md)
excludes Laurent families of every first-leg pole order when both long
maps remain regular and surjective at zero. Singular leading long maps
remain outside that result. A [wider jet obstruction](research/ai/2026-10-20-paired-construction/wider_jet_obstruction.md)
excludes the specified regular-nilpotent quotient for every `m>=2` and
`n>=m+1`, while other wider kernels remain open.

The [finite-symmetry package](research/ai/2026-10-20-paired-direct-sums/scalar_and_symmetry.md)
excludes ordinary tetrahedral-equivariant `P3 + trivial scalars -> M3`
with the stated physical representations, for any number of scalars.
All three exact correction phases have nonsingular twelve-by-twelve
equation matrices. Sixteen complete numerical checkpoints replay to their
reported failed-search metrics; these failures alone are not exclusions.

These are written, externally unreviewed deductions and finite controls.
Current constructive work seeks `Q(6,4) -> M(5,4,5)` and scalable formulas
beyond the injection template's dimension limit. The exact small witness
does not meet the unbounded fixed-width family premise.

The [sixteen completed extension searches](research/ai/2026-10-20-paired-direct-sums/q64_search_history.md)
retain all map coefficients and iteration histories. Twelve ordinary fits
and four prescribed Laurent fits give no exact witness. A separate native
coefficient replay checks their reported objectives, including every pole
and every explicit scalar cost. The ordinary product component and the
Laurent runs' non-nilpotent operator errors explain particular failed
searches; they are not general obstructions.

The [boundary-column calculation](research/ai/2026-10-20-paired-construction/outer_product_boundary.md)
excludes an all-order extension that keeps the integer seed's old long-map
columns fixed. Arbitrary new boundary columns lose at most one first-leg
direction; a full next-size matrix extension needs at least `2k+1`.
For Q(6,4), these numbers are one and nine. Changes to the old columns
remain open and are being searched separately.

The [mixed-middle extension](research/ai/2026-10-20-paired-construction/mixed_middle_boundary.md)
proves the same leading rank lower bound of 35 when the seed's four middle
polynomials can mix across the two-dimensional factor. A polynomial syzygy
argument forces an injective projection, so changing only the new boundary
columns still cannot supply the required nine-dimensional kernel. Outer
polynomial spaces in P5 remain outside this argument.

The [balanced-support lemma](research/ai/2026-10-21-nearfull-quantum/README.md)
closes all diagonal Laurent weights for two specified regular quantum
families, even followed by arbitrary further degenerations to their full
matrix targets. Exact rational marginal certificates and Koszul deficits
supply its hypotheses. It does not exclude different leading families,
auxiliary corrections, or the separate recovered integer construction.

Checkpoint `cfa12ba`, integrating main `63eecee`, passes all 467 local
regression tests and all five archive replays on an isolated checkout.
Site packages are disabled for these runs; maintained verification uses
the declared dependencies. Its [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint8-validation.json)
records the exact tree and log hashes. All nine observed hosted checks,
including CI, also pass. The next integration includes main `fc8207e`;
this historical test count applies only to `cfa12ba`.

The [external rank-76 seed screen](research/ai/2026-10-21-external-grid-seed/README.md)
replays all 10,000 coefficients of a known AlphaTensor M(4,5,5) algorithm.
An exhaustive finite-field calculation excludes a termwise assignment of
that fixed decomposition to the Q(6,4) evaluation grid in one specified
leg alignment: nine rank-four groups can hold at most 72 of its 76 vectors.
Different decompositions and general maps remain open. This is a failed
reuse attempt, not a new multiplication algorithm or exponent.

The [complete-flag experiments](research/ai/2026-10-20-paired-direct-sums/q64_full_flag_history.md)
retain six further searches and every coefficient of their best maps.
None satisfies the exact Laurent equations. The complete grading has
5,050 required positions; exact shear controls and numerical derivative
checks verify the implemented gauge conventions. Small residuals and
three small trace moments still do not establish nilpotent error.

A [smaller leading-seed calculation](research/ai/2026-10-20-paired-construction/small_leading_jet.md)
excludes the stated first-jet extension of one fixed M(2,4,2) seed inside
Q(6,4) plus one scalar. Both complete rational first-edge systems have
rank 52 and zero aligned image. Other leading maps and higher valuation
patterns remain open.

Checkpoint `1e0e468`, integrating main `fc8207e`, completed 476 tests with
475 passing and one claim-ledger failure: the external-grid experiment
used an unsupported status label. The label is corrected to the existing
`finite-experiment` category in this continuation. Its five archive
replays passed. The [failed-checkpoint receipt](results/paired-checkpoints-2026-10-21/checkpoint9-validation.json)
retains the completion record and hosted failures; it does not describe
the corrected tree as fully verified.

## Audit of a separately claimed exponent improvement

The [bounded Sun audit](research/ai/2026-10-21-sun-audit/README.md) checks
parts of the external preprint arXiv:2610.13971v1. Its proposed
`D16 tensor (14 CW3 + 6 CW2 + 7 W + 5 D4) -> M32` degeneration would imply
`omega<=2.2`. The proposed complete
three-factor Laurent map has not been reconstructed or verified here.

Exact calculations find 50 normalization discrepancies among 354 literal
support occurrences; a stated local scaling repairs all of them. All 256
normalized Walsh equations and the checked five-empty-module identities
hold. A particular packetwise reading of the chart pullback would require
a border-rank-five source to contain `M2`; an explicit determinant-one
Koszul minor gives border rank at least six and excludes that reading.
The preprint's later assembly retains outer rows and additional records,
so this packetwise obstruction is not presented as a refutation of its
global claim. Standard full-space Koszul tests necessarily pass for the
proposed global source and cannot resolve this gap. No external smaller
exponent is adopted on the basis of this audit.

Checkpoint `89c0287`, integrating main `8722b36`, passes all 385 local
regression tests and all five archive replays. Every hosted check also
passes at that commit. The [validation receipt](results/paired-checkpoints-2026-10-21/checkpoint4-validation.json)
records the exact tree, commands, environment, and log hashes. These checks
do not change the mathematical review status of the research.

## Constructive continuation and source obstructions

The constructive continuation records seventy-four local claims
in [the claim ledger](research/claims.json). This checkpoint adds
claims 118 through 122 and 124 through 126 to the earlier sixty-six claims. All general arguments are
written and unreviewed. Same-session agent checks and exact finite replays
do not constitute independent mathematical review.

The [auxiliary corner](research/ai/2026-10-20-anisotropic-constructions/spin_scalar_corner.md)
now gives exact M(1,1,9) with full response ranks (15,9,9) and six
vanishing mixed responses against the reduced search's ambient spaces.
It would cancel nine copies of a shared-first-factor scalar defect;
the reduced maps with that defect remain missing. A second agent
independently reconstructed the source and all compatibility checks.

An [exact source-basis control](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_basis_escape.md)
escapes claim124's fixed compression hyperplane: its three selected
coefficients are (1,2,7), with alternating combination6. This enlarged
family still has no M9 witness. The failed finite numerical pilots and
their actual residuals are saved separately from exact acceptance.

The [25-test ordinary-frontier integration receipt](results/anisotropic-constructions-2026-10-20/spin-hankel-integration-validation.json)
passes the seven incoming Hankel-pencil controls and eighteen repository
checks after incorporating main4695298. It preserves that proof's
unreviewed status and its exclusion of ordinary A8 targets. Singular
matrix constructions remain the active positive question.

The [27-test integration receipt](results/anisotropic-constructions-2026-10-20/spin-scalar-basis-focused-validation.json)
passes all seven new mathematical tests, both tests from main's external
preprint audit, and all18 repository checks. Main bf3b7d8 is preserved.
Earlier complete regression and archive receipts remain linked below;
this receipt does not count a second complete-suite run.

The concurrent [ordinary Hankel–Segre application](https://github.com/1337isnot1337/matrix-mult-bounds/blob/1721a4e9d7ac3eb0762075c235be3afa99a3e8fa/research/ai/2026-10-21-hankel-pencil-degree/application.md),
pinned at1721a4e9 in PR75, supplies a written unreviewed exclusion of
the former ordinary A8 rectangle M(27,28,28), and all improving ordinary
A8 square sums. Its argument leaves singular degenerations outside its
scope. The current construction effort therefore targets singular maps;
the earlier response budgets remain exact necessary tests for their
fixed cores, without asserting that the larger ordinary target exists.

A [complete fourth vertex](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin22_fourth_vertex.md)
now gives exact rational A(8,8) restrictions to M(3,4,32) and its
common-channel section M(3,4,28). The section has response ranks
(192,252,252) and preimage dimensions (780,820,792), leaving allowances
(24,36,36) for the proposed M(27,28,28) rectangle. All 112,896
section coefficients are checked. The tiny target alone was already
known by cyclic rotation; the new evidence concerns the specified spin
chart, residue lift and response spaces. A singular larger rectangle remains
unconstructed; the ordinary case is excluded by the concurrent proof above.

An [exact two-endpoint repair](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin44_double_endpoint.md) changes both retained maps of the balanced module while preserving M(3,3,27). Its complete first response vanishes at two specified endpoint coordinates. The remaining response rank is exactly190, giving a first preimage of dimension779. The current rational coefficients were freshly reconstructed; they are explicitly distinguished from the lost original implementation. Every original-source and target coefficient passes, and a second agent separately replays both endpoint responses. The remaining matrix-unit extension equations are unsolved.

Its [22-test follow-up receipt](results/anisotropic-constructions-2026-10-20/spin-double-endpoint-focused-validation.json) passes with no skips, including all four substantive construction tests and repository checks. The four unchanged tests introduced by main20fa49b also pass in their [separate integration receipt](results/anisotropic-constructions-2026-10-20/spin-main20fa-incidence-validation.json).

The [three-leg budget calculation](research/ai/2026-10-20-anisotropic-constructions/spin_rectangle_budget.md)
also certifies ranks (192,236,216) for the original full 28 spin core.
It credits the concurrent ordinary frontier for the same rectangular
candidate. Its exact numerical comparison would imply omega<2.247
only after the missing full maps are constructed. The retained core
dimension must increase when a vertex is completed; a fixed old
dimension would give the wrong extension budget.

The [balanced-core freedom theorem](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin44_freedoms.md)
gives the complete low-coordinate kernels after five channels are
removed. Simultaneous individually neutral changes preserve the core
exactly when their deleted-channel graph spaces are orthogonal.
A full rational example changes all 81 retained rows on both legs and
passes every original-source coefficient check.

A separate [ordinary compression proof](research/ai/2026-10-20-anisotropic-constructions/spin_fiber_compression.md)
and its [Laurent-limit extension](research/ai/2026-10-20-anisotropic-constructions/spin_fiber_closure.md)
close the fixed local-spin/raw-column/radix family at every power k>=2.
Three actual output coefficients satisfy a linear identity that the
matrix tensor violates. The three-bit induction base has an independent
full source enumeration. Changed local maps and additional output
transformations remain open.

The [recovery checkpoint receipt](results/anisotropic-constructions-2026-10-20/spin-recovered-focused-validation.json) records all 34 focused tests passing. Its initial metadata-assertion error and correction are retained separately. The [complete regression](results/anisotropic-constructions-2026-10-20/spin-current-main-full-validation.json) through main 48bd72d completed 609 tests, with 606 passes and three optional skips; the later recovered packages have the separate focused coverage. All five [archive replays](results/anisotropic-constructions-2026-10-20/spin-current-archive-validation.json) also pass. Concurrent branch head f1ffc57, which integrates main 20fa49b, is preserved beneath this checkpoint.

A [balanced spin module](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin44.md)
now constructs M(3,3,8) from A(4,4), and M(3,3,32) from A(8,8).
Its four parity sectors use the same nine first images. The full-source
replay checks all 82,944 target coefficients of the larger tensor.
Retaining 27 of its 32 channels leaves five channels available for
coupled changes; compatible larger matrix maps remain unconstructed.

A separate [four-vertex extension](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_four_columns.md)
constructs the complete rectangular tensor M(3,7,27) from A(8,8),
with all 321,489 target coefficients checked. Its other-leg maps
have first response rank 576, leaving a first preimage of dimension
405. Therefore this specific pair cannot be retained in an ordinary
extension with first dimension greater than 405, even if the first
map changes. Other maps and singular degenerations remain open.

An [exact Laurent repair](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_w34_laurent.md)
preserves M(3,3,27) at every nonzero parameter while canceling one
endpoint response. It also constructs a two-channel M(3,4,2) attachment,
sharing six third-leg variables with the core. Complete Laurent
coefficient replays include unwanted terms and negative powers.
The [ordinary core-freedom certificate](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin_w34_freedoms.md)
separately describes an 891-parameter family preserving the same core
and proves that this specified family cannot cancel either stated
endpoint. Neither result completes an improving target.

A [new four-chain spin module](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_w34.md)
changes both retained maps and constructs M(3,3,28) exactly. Deleting
one channel leaves three explicit boundary directions that support
[eight simultaneous attachments](research/ai/2026-10-20-anisotropic-constructions/spin_channel_extension.md).
The resulting tensor has leg dimensions (33,89,81): it glues
M(3,3,27) and M(3,8,1) along three third-leg variables. All 237,897
target coefficients are checked exactly. Each new second vertex still
lacks 26 channels; this is not a complete M(3,11,27) tensor or a square
target. Its first response has rank 216 and first preimage dimension 777.

The [boundary-discovery record](research/ai/2026-10-20-anisotropic-constructions/spin_private_boundary_discovery.md)
also preserves 108 finite-field undoubled-module trials and a separate
private-boundary repair attempt. Neither supplies accepted rational maps.
Their rank calculations apply to the recorded charts over F65521 and
do not establish a characteristic-zero obstruction.

An [exact endpoint repair](research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin_endpoint.md)
changes the retained Y map and gives A(8,8) to M(3,3,27) with response
rank 191. Its first preimage has dimension 778, meeting the necessary
dimension allowance for M27 plus M7. A separate
[coefficient argument](research/ai/2026-10-20-anisotropic-constructions/spin_endpoint_extension.md)
nevertheless excludes an ordinary extension that keeps those repaired
Y and Z rows: a new matrix unit would have response rank at most one
where the target requires three. This proof permits arbitrary kernel
changes to the nine first images. Changed retained maps and the
dimension-774 target M27 plus M6 plus M3 remain open.

The [original spin-core preimages](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin_assembly.md)
are also determined exactly. All 28 single-coordinate middle deletions
keep response rank 192 and first preimage dimension 777. With the
actual first map fixed, explicit bases give dimensions 727 and 747
for adding second- and third-leg rows. The remaining coupled equations
are not implied by those linear spaces.

The [spin-one module construction](research/ai/2026-10-20-anisotropic-constructions/spin_module14.md)
now gives exact rational maps from A(4,8) to M(3,3,14) and from A(8,8)
to M(3,3,28). Its nonproduct first map absorbs the earlier scalar
correction into the larger source, with no extra scalar summand. All
source and target coefficients are checked exactly. The first response
is confined to 192 coordinates, leaving enough linear room for the
unconstructed target M27 plus M6 plus M3. That target would imply
omega below 2.24975; this is a conditional comparison, not a new bound.

A separate [changed corner construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner_shifted.md)
gives M(4,4,12) with exact response rank 164 and fixed-first-map
flattening rank 481. It passes two necessary tests for extending toward
M27 plus M7. Its other square-matrix entries remain unconstructed.
The original corner variant, with response rank 186, is also preserved.

The [exact crossed-module construction](research/ai/2026-10-20-anisotropic-constructions/crossed_module11.md)
gives a rational restriction from C(2,4) tensor C(2,8) to M(2,2,11).
Its [full-source lifts](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_cross_module_lifts.md)
give A(4,8) to M(4,4,11) and A(8,8) to M(4,4,22), with every desired
and unwanted coefficient checked from the original source tensors.
These improve the corresponding coordinate-module controls from eight
and sixteen channels to eleven and twenty-two. The first target leg
still has only sixteen directions; compatible square extensions are
missing. Neither rectangular restriction establishes a smaller exponent.

The [four-factor flattening proof](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_crossed_flattening.md)
proves that eleven and twenty-two are optimal within the corresponding
product first-map branch. It also excludes extending the old sixteen
first images to M27, even with arbitrary other-leg maps. The
[saved-seed response certificate](research/ai/2026-10-20-anisotropic-constructions/crossed_module_response.md)
separately excludes retaining the old other-leg maps. The newer spin
and corner constructions change the first core; these scoped
obstructions do not rule them out.

The [two-source capacity inequality](research/ai/2026-10-20-anisotropic-constructions/two_source_budget.md)
requires equal source leg dimensions N at least ceil(3 n^2 / 4) for a
direct sum of two sources to degenerate to M_n. Explicit complementary
block-zero trace tensors attain this dimension threshold. Combining this
necessary condition with the finite convolution budget first leaves
2 A(11,12) to M62, which is unconstructed. The recorded ordinary
majority-block factorization at that size is separately excluded.

An [exact carry contradiction](research/ai/2026-10-20-anisotropic-constructions/bitwise_hankel_projection.md)
closes one specified two-copy spin1 projection family. The completed
[moving physical-compression experiment](research/ai/2026-10-20-anisotropic-constructions/parity_structure_rectangular_compression.md)
retains all 1,210,000 target coefficients and explicit scale normalization.
Its final normalized residual is about 5.4627, so it supplies no target
identity or singular family. These records preserve exact controls and
the actual limitations of the searches.

The [new focused receipt](results/anisotropic-constructions-2026-10-20/crossed-module-focused-validation.json)
pins the artifact hashes and includes concurrent main through `8a07bed`.
It records 38 completed tests: 36 passed and two optional numerical
controls skipped in the maintained environment. All four compression
control tests pass separately with NumPy and SciPy available.
The [complete regression receipt](results/anisotropic-constructions-2026-10-20/crossed-module-full-validation.json)
pins checkpoint `1f813bb`: 496 tests completed, with 493 passed and
three optional skips. All five [original archive replays](results/anisotropic-constructions-2026-10-20/crossed-module-archive-validation.json)
passed unchanged. The later spin, corner, response and flattening
packages have separate focused validation; they are not included in
that 496-test count.
Their [35-test focused receipt](results/anisotropic-constructions-2026-10-20/changed-core-focused-validation.json)
checks all four new packages, main's mixed second-order family through
`21f54c3`, and the repository ledger, sources, archives and links with no
skips or failures.
The [full spin-and-corner regression receipt](results/anisotropic-constructions-2026-10-20/spin-corner-full-validation.json)
pins checkpoint `4ed2b52`: 513 tests completed, with 510 passed and
three optional skips. The later preimage, endpoint-repair and extension
packages are not included in that count.
The integration of main at `b113866` also has a separate
[27-test focused receipt](results/anisotropic-constructions-2026-10-20/spin-corner-main-integration-validation.json),
with no skips or failures.
The [assembly checkpoint receipt](results/anisotropic-constructions-2026-10-20/spin-assembly-focused-validation.json)
checks the exact preimages, endpoint repair, fixed-map extension proof,
four-chain module, simultaneous attachments and repository invariants:
31 tests pass with no skips. The finite-field discovery files are
preserved separately from the rational construction certificates.
All hosted checks pass for assembly head `1b94457`; Python 3.10
completes 530 tests with three optional skips. A subsequent
[36-test growth receipt](results/anisotropic-constructions-2026-10-20/spin-growth-focused-validation.json)
checks the four new packages above, the incoming third-boundary theorem
at `18a06b3`, and repository invariants. These new packages are not
included in the earlier 530-test count.

The [support-peeling proof](research/ai/2026-10-20-anisotropic-constructions/torus_support_peeling.md)
now excludes **every ordinary A88 to M27 plus M7 restriction whose matrix-unit
images are homogeneous for the fixed source grading**, including unrelated
vertex charge lists and profiles with holes. Exact rank budgets successively
force all three map images into coordinate spaces of dimensions
960, 922, 834, and finally 468, below the required 778. The primary verifier
checks 492 removals through integer separating lines, independently of the
discovery hull algorithm. A separately written full-source replay agrees
on every retained coordinate set. Ungraded maps and arbitrary singular
degenerations remain open, and the exponent is unchanged.

The [mixed-grading extension](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_mixed_grading.md)
shows that, on at least two legs of any ordinary target restriction,
at least 19 matrix-unit images must each use three or more source weights.
It uses separate coordinate masks and injectivity inherited from the full
maps. An exact M12 plus M3 change of basis provides a positive control
with balanced cross-weight cancellation; it does not enlarge that target.

Two [Laurent collision controls](research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_extension.md)
give explicit singular limits from the existing three matrix cores.
The larger limit retains all 134 intermediate directions per leg, including
24 off-diagonal directions, with complete negative-power cancellation.
The [scalar-power construction](research/ai/2026-10-20-anisotropic-constructions/scalar_power_recycling.md)
reuses corrections to realize A22 squared plus A22 plus M3 to M9 with
165 source coordinates per leg. Its all-power residual has exact flattening
rank 9^k-8^k, and its complete source cost does not cross the finite gate.
These are constructed identities and scoped cost bounds, not smaller
exponent claims.

- The [oriented endpoint analysis](research/ai/2026-10-20-critical-character-extension/README.md)
  gives a common critical amplitude and a quantitative stability bound.
  A certified fifth-difference stencil separates that hypothetical profile
  from quantum characters and the classified edge of the spectrum. The
  corresponding test for interior spectral points remains unproved.
- The [nonmonic target normalization](research/ai/2026-10-20-new-source-constructions/README.md)
  gives an all-size unimodular normalization. At size four, a sampled chamber
  reduces the coefficient system to 95 zero equations and two orbit
  relations. Exact elimination has 65 unit pivots. No exact solution or
  Hensel certificate has been found.
- The [full polynomial rank locus](research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
  classifies cyclic-source slices below twice their minimum rank. It gives
  an ordinary-map obstruction for every nonscalar square target block.
  The [Hankel-symbol dimension theorem](research/ai/2026-10-20-anisotropic-constructions/hankel_symbol_dimension.md)
  extends the obstruction to every rank r with r<min(a,b) and
  3r<=a+b-1. A separate [equality argument](research/ai/2026-10-20-anisotropic-constructions/parity_structure_equality.md)
  and [three-leg factorization](research/ai/2026-10-20-anisotropic-constructions/hankel_rank_two.md)
  close the rank-2ab boundary for square blocks of size at least three.
  The [first-boundary theorem](research/ai/2026-10-20-anisotropic-constructions/hankel_boundary_dimension.md)
  extends the Segre-image bound to a+b-1=3r-1, with dimension cap max(r,4).
  [Exact partition enumeration](research/ai/2026-10-20-anisotropic-constructions/square_sum_frontier.md)
  now excludes every improving ordinary square direct sum from all 60 source
  formats with leg dimension below 960, and from A(5,12) at dimension 960.
  The former A(7,8) target M25 plus M5 is excluded. The first surviving
  format is A(8,8): M27 plus M7 would imply omega<2.2485, but its maps are
  missing. Singular full-source degenerations remain open.
- An [explicit parity degeneration](research/ai/2026-10-20-anisotropic-constructions/parity_balancing.md)
  has positive rational marginal certificates and cyclic asymptotic
  slice-rank capacity about 212.716257. A stronger
  [pairwise-annihilator obstruction](research/ai/2026-10-20-anisotropic-constructions/parity_annihilator.md)
  bounds every square direct-sum target of that one-copy source by leg
  dimension 169, including arbitrary singular degenerations. A single M13
  is also excluded. The proposed M14 plus M4 target is therefore closed.
- The [integral direct-sum construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_direct_sum.md)
  gives actual restrictions A(a,a) to M(2a−2) plus M(a−2), for every a≥3.
  Complete coefficient controls cover a=3 through 6, including M8 plus M3
  from A(5,5). An additional proposed scalar block fails mixed-coefficient
  checks and is explicitly rejected.
- A new [rational matrix identity](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_spin1.md)
  gives an actual restriction from A(2,2) plus one scalar to M3. All 729
  target coefficients are checked exactly. The additional scalar is part
  of the source, so this does not assert a restriction from A(2,2) alone.
- The [residual construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_residual.md)
  gives A(5,6) to M8 plus the full A(2,3) tensor. Exact maps also give M10
  alone and M8 plus M4. These constructions retain useful smaller sources
  for composition. A [corner split](research/ai/2026-10-20-anisotropic-constructions/parity_structure_corner_extension.md)
  supplies A(2,2) plus one scalar from A(2,3). These maps do not improve
  the exponent.

- The [all-size retained-residual construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_full_residual.md)
  gives A(a,a+1) to M(2a-2) plus A(2,a-2), for every a>=5. The complete
  A(7,8) to M12 plus A(2,5) witness has an integer-only replay. A fixed-core
  extension bound limits that particular core to total leg dimension 256.
- The [triangular lift](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_triangular.md)
  gives A(a,b) plus M((a-1)(b-1)) to M(a+b-1). Its residual is retained.
  [Score limits](research/ai/2026-10-20-anisotropic-constructions/quotient_score_barrier.md)
  close the stated single full-correction comparison and independent corner
  supplier. A [cyclic determinant identity](research/ai/2026-10-20-anisotropic-constructions/parity_structure_three_quotients.md)
  prevents the scalar correction from vanishing in the exact A22 quotient
  family. The [cyclic quotient-volume theorem](research/ai/2026-10-20-anisotropic-constructions/cyclic_quotient_volume.md)
  further proves m0*m1*m2<=(a+b-1)^3 for three unrelated exact physical
  quotients over every field. Even free residual cancellation cannot pass
  the single-target finite comparison in that class. Unrestricted
  off-diagonal compression maps remain open.
- Exact integral controls include A(2,3) to M4 with zero quotient-kernel
  action and [A(8,8) to M15](research/ai/2026-10-20-anisotropic-constructions/parity_structure_a88_seed.md).
  The latter has 462 nonzero entries per map and a complete sparse replay.
  These controls do not construct the larger improving target.

- A new [torus-compatible exact seed](research/ai/2026-10-20-anisotropic-constructions/parity_structure_torus_seed.md)
  gives A(8,8) to M12 plus M3. The [monotone physical-vertex construction](research/ai/2026-10-20-anisotropic-constructions/monotone_endpoint_seeds.md)
  gives exact endpoint M4 and M8 controls. The latter construction's literal
  common coordinate code has a [size limit](research/ai/2026-10-20-anisotropic-constructions/coordinate_compression_limit.md):
  every A88 M27 construction must leave that code on each target leg.
- The [recorded endpoint maps](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_torus_anchors.md)
  have full row rank 778 on all three legs. They satisfy all six extreme
  slices of the M27 plus M7 target and the complete endpoint M4 tensor.
  Each rational map has denominator 64 and 782 nonzero entries. The other
  target coefficients cannot all be satisfied with that boundary fixed:
  a [direct affine-slice contradiction](research/ai/2026-10-20-anisotropic-constructions/torus_affine_slices.md)
  forces a coefficient to equal one where the target requires zero.
  A [four-map relation](research/ai/2026-10-20-anisotropic-constructions/fixed_anchor_obstruction.md)
  excludes completion of the preserved first Hadamard seed with its stated
  maps fixed. Both saved seeds remain valid controls for their partial
  identities, and both fixed boundary families are now nonextendable.
- The [degree-13 pencil proof](research/ai/2026-10-20-anisotropic-constructions/torus_degree13_pencils.md)
  excludes every ordinary grading-preserving restriction with the original
  symmetric 27-plus-7 charge profile, including arbitrary boundary maps.
  It combines the [two-leg rank chain](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_rankone_13_chain.md),
  exact source symmetries, universal product identities and all 256
  singular-projection patterns. This does not exclude the ungraded frontier.
- A [saturated-block rank inequality](research/ai/2026-10-20-anisotropic-constructions/torus_saturated_blocks.md)
  excludes the common width-13 profile: its target block has rank 9,
  while saturation of the two input spaces requires rank at least 12.
  A separate [cube determinant](research/ai/2026-10-20-anisotropic-constructions/torus_saturated_pencil.md)
  excludes specified saturated degree-13 pairs even with unequal vertex
  charge lists. Neither argument addresses arbitrary singular limits.
- The [graded fixed-core bound](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_fixed_core_weights.md)
  excludes keeping two complete copies of the displayed M4, M6 or M8 core
  while extending to the original profile. The [free-interior construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_free_interior.md)
  gives A(a,a) with both physical endpoints deleted to
  M(a-1) plus M(a-1) plus M(a-2), for every a>=3. Its fixed M7 channels
  also fail an exact extension-rank test; movable small-block maps remain open.
- The [complete common-vertex M7 screen](research/ai/2026-10-20-anisotropic-constructions/parity_structure_m7_vertex_screen.md)
  covers 1,290,240 choices. Sixteen pass the necessary weight-zero rank
  gate, but all retain 498 unwanted coefficients. Exact balanced cycles
  obstruct removing those extras by coefficientwise Laurent rescaling.
- The earlier [common-profile classification](research/ai/2026-10-20-anisotropic-constructions/parity_structure_common_profiles.md)
  also closes all common integer charge lists by exact enumeration and
  local proofs. Its [zero-grade lemma](research/ai/2026-10-20-anisotropic-constructions/parity_structure_zero_grade_rank.md)
  gives minimum slice rank a for the zero-grade A(a,a) tensor. The later
  peeling proof removes the need to enumerate profiles for the main exclusion.
  [Unequal-profile partial maps](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_unequal_profiles.md)
  retain exact M12 plus M3 controls; their full targets are explicitly
  excluded. Optional numerical objective code is preserved with separate
  small controls and introduces no maintained dependency.
- The [simple-pole argument](research/ai/2026-10-20-anisotropic-constructions/compression_simple_poles.md)
  excludes a nonzero simple pole in the fixed A22 compression chart when
  the trace tensor must have a finite limit. It does not cover arbitrary
  pole supports or moving physical bases. A separate [stabilizer invariant](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_stabilizer.md)
  excludes the saved dyadic A33 numerical seed from the stated target
  stabilizer orbit, with a complete integer-only modular replay. It does
  not exclude changing that seed or general A33 maps.

The [combined validation receipt](results/anisotropic-constructions-2026-10-20/residual-boundary-validation.json)
records 368 passing tests and five unchanged archive replays at `8b09235`.
This computational coverage does not change the proof-review status.

The [torus-anchor checkpoint receipt](results/anisotropic-constructions-2026-10-20/torus-anchors-validation.json)
records 391 passing tests and five unchanged archive replays for `fa74fee`
combined with main `f67467d`. That receipt predates the new fixed-boundary,
degree-13 and saturated-block packages; it is not their validation receipt.

The [support-peeling checkpoint receipt](results/anisotropic-constructions-2026-10-20/torus-peeling-validation.json)
records the complete 447-test suite at `bb64dae`: 446 passed and the optional
NumPy control skipped. All five original archive replays passed unchanged.
This pin includes main through `b0a54f2` and claims through 093; the newer
mixed-grading, Laurent, scalar-power and concurrent-main additions pass
the [separate 16-test focused suite](results/anisotropic-constructions-2026-10-20/torus-construction-controls-validation.json).
The claim ledger, source registry, archive manifest and relative links also
pass their repository checks. Current hosted validation is required before
merge.

These results identify constructions and obstructions within stated classes.
They establish no smaller matrix multiplication exponent.

The earlier checkpoint `e44aaff`, integrated against main `a44451d`, passed
323 regression tests and all five original archive replays. Its
[validation receipt](results/anisotropic-constructions-2026-10-20/integration-validation.json)
records the commands and log hashes. The historical archives are unchanged.
Checkpoint `eed3cbc` incorporated main `2a7c503` and passed 338 local regression
tests and all five archive replays. Its
[validation receipt](results/anisotropic-constructions-2026-10-20/integration-hankel-validation.json)
records the commands and exact log hashes. Hosted validation then found an
undeclared NumPy import in the rank-two checker. The checker now uses Python
integers only and reproduces the same 1,296,000 coefficient comparisons.
The repaired tree includes main `75bf6a3` and passes 344 tests plus all five
archive replays with site packages disabled and only the declared SymPy and
mpmath dependencies available. The
[repair receipt](results/anisotropic-constructions-2026-10-20/integration-maintained-validation.json)
records this environment and the original hosted failure. CI and finite
replays do not change the proofs' review status.

## Earlier integration checkpoints

The [main integration checkpoint](docs/integration_2026-10-20.md) combines the
four research lanes and passes 160 local tests plus the five original archive
replays. Written proofs remain unreviewed, and conditional constructions remain
unproved. Active worker branches continue to carry new experiments.

| ID | Local statement | Evidence status |
| --- | --- | --- |
| AI-SCALAR-001 | Exact pointwise-minimal profile for S1-S3 | Written proof; Codex audit found no gap; independent review open |
| AI-RANK-002 | Matching profile satisfies the rank upper bound at $t=3/4$ | Written proof; unreviewed |
| AI-REPLICATION-003 | Matching profile satisfies replication at $t=3/4$ | Written proof; unreviewed |
| AI-PACKING-004 | Flattening obstruction for shorter identical-sector packing | Written proof; unreviewed |
| AI-FILTRATION-005 | Additional product-filtration inequalities | Derivation; unreviewed |
| AI-CONDITIONAL-006 | Uniform positive tripling gain implies a smaller exponent | Conditional implication; premise unproved |
| EXP-PROFILE-001 | 73,856 grid assertions and four symbolic identities | Reproduced |
| EXP-FILTRATION-002 | 353,664 inequalities over 20,736 source quadruples | Reproduced; no finite violation |
| EXP-WEIGHTS-003 | 242,668 specified weight candidates | Reproduced; no scored violation |

[Claim ledger](research/claims.json) | [Full original note](research/ai/2026-10-20/research_note.md) | [Replay report](results/bootstrap-2026-10-20/summary.json)

The commit-pinned [Codex proof audit](research/reviews/2026-10-23-scalar-profile/PROOF_REVIEW.md)
found no gap in the all-integer argument. The claim remains unreviewed pending
independent human review; the audit does not change its theorem or exponent
status.

The all-integer statements rely on written proofs, not finite checks. The pointwise-minimality argument has no independent mathematical review or full Lean formalization; only its auxiliary finite slope estimate is checked in [the scalar-profile Lean project](formal/scalar-profile/README.md).

The matching-profile result rules out improving the exponent from only its listed scalar assumptions. It neither proves $\omega\ge9/4$ nor excludes the full tensor spectrum.

The [F8 variable-plane continuation](research/ai/2026-10-20-group-potentials/octal_research.md#variable-planes-after-the-first-main-integration)
now searches independently chosen normal-fiber planes. Its encodings pass
a complete known-model audit, and an independent integer checker validates
the affine fibers and pair maps. The first native-parity run checks four
candidates, including a reused control; all fail exact potential constraints.
This extends discovery coverage and supplies no improved exponent.

The current next steps are listed in [research directions](docs/research_directions.md). Repeating a completed finite search with the same parameters is reproduction, not new research progress.

The [fixed cubic F8 parent obstruction](research/ai/2026-10-20-octal-parent-barrier/research_note.md)
excludes every single strict-coordinate-potential target from vertex subsets
of that 56-point parent from passing the usual 9/4 degree-sum gate. An
explicit circuit orbit forces a seven-cycle hole inequality; exact integer
optimization bounds the target volume by 92,928, including rectangular
shapes. The checker verifies 10,752 circuits and independently enumerates
all 4,782,969 hole patterns. This written proof is unreviewed and concerns
only that parent and construction method. It gives no exponent improvement.

A complete local continuation checks all 3,060 single-plane changes in the
F8 base `[1,8,2,16,4,32]`, keeping all short directions fixed. Every change
fails a necessary pair-quotient packing. This finite scope is replayed by
`tests/test_octal_single_plane.py`; it does not exclude simultaneous changes
or other bases. Two native-parity pilots yield only reused controls and
untraced UNSAT answers. Neither gives an exponent improvement.

The [C29 near-capacity classification](research/ai/2026-10-20-c29-near-capacity/research_note.md)
proves that every three-point unique-sum triple in C29 consists of arithmetic
progressions. Two exact enumerations agree on its six ordered normalized
cases. A complete fiber-direction filter for C29:C4 leaves twelve size-ten
configurations, and the identity-quotient offset telescoping condition rejects
them all. Thus the stated injective-pair-map construction with strict vertex
potentials cannot have all three sizes at least ten. This written argument
is unreviewed; general tensor degenerations and smaller unequal targets
remain open. No smaller exponent follows.

The [C29 unequal-target followup](research/ai/2026-10-20-c29-near-capacity/rectangular_note.md)
closes the same coordinate-potential one-source degree-sum route for all
single matrix shapes. The full sorted rank-locus frontier leaves only
(9,9,11), (9,10,10), and (10,10,10). Complete finite filters and identity
gluing now exclude all three in the stated construction class. This is
an unreviewed obstruction, not a general degeneration exclusion or an
improvement of the arithmetic exponent.

## General semisimple Koszul continuation

The [full-space semisimple screen](research/ai/2026-10-21-semisimple-koszul/proof.md)
applies the existing exact matrix Koszul formulas to general complex
degenerations of group algebras. It excludes five of the26 remaining F8
formats, including(16,16,26), while21 still pass, including(19,19,19).
These exclusions have broader scope than the coordinate-construction
barriers below. The written derivation and imported rank proofs are unreviewed.

The same package exactly derives the504-element SL(2,F8) source degrees
1,7,7,7,7,8,9,9,9 by rational central algebra. Its degree/rank-locus/full-Koszul
frontier leaves16 formats. A genuine M(18,18,25) degeneration would imply
exponent at most2.245 by the certified conditional comparison; no such
degeneration is supplied. One fixed-full-D18 subgroup pilot timed out with
zero pair models in180 seconds. Only its small M(18,1,1) control is verified.

The [SL(2,F8) subgroup-ideal followup](research/ai/2026-10-21-sl2-f8-ideals/proof.md)
applies a concurrent worker's averaging lemma with new exact central
projection upper bounds308,440,244 for subgroup orders8,9,18. Complete
unipotent-eight and dihedral-eighteen cosets are forbidden on every leg of
all16 remaining coordinate formats. For M(18,18,25), nine-cycle cosets are
also forbidden in the two size-eighteen families. This now excludes the
first fixed-full-D18 frame by a written unreviewed proof; its historical
timeout is not used as proof. Remaining coordinate sets and general tensor
maps remain open. No exponent improvement follows.
The full-D18 search command now replays the exact244<450 projection
obstruction before importing optional SAT dependencies. Its analytic
exclusion report is checked separately from the historical timeout and
the positive control, which remain unchanged.

## Abelian-normal coset Koszul obstruction

The [normal-coset proof](research/ai/2026-10-20-normal-coset-koszul/research_note.md)
restricts a coordinate-potential group construction to its abelian normal
subgroup. The classical three-slice commutator bound then requires
`3 sum k_a^2 - number(k_a=1) <= 2|H|` for common-coset vertex minima.
An explicit rank-129 integer matrix versus source upper bound 128 closes
the entire F8 size-nineteen maximum-three-fiber ansatz, including every
variable plane and offset in the prior search. A separate difference-space
argument bounds all size-nineteen F2^6 normal fibers by four.

The same proof excludes the full stated F4^3:C3 size-twelve coordinate
class and every C31:C6 candidate with all normal fibers at least two. It
does not exclude general complex degenerations. The proof is unreviewed.
A complete seven-fiber count screen with sizes in {2,3,4} leaves 1,566
necessary patterns; they have no constructed directions, offsets or
potentials. The exponent remains 9/4.

The [rectangular coset followup](research/ai/2026-10-20-normal-coset-koszul/rectangular_note.md)
now excludes the full size-nineteen F8 construction class, including every
four-point, one-point and empty fiber pattern. A rank formula for rectangular
normal blocks, a pair-averaging argument and 466,859 independently replayed
alignment bytes cover all 505 cyclic count classes. Thus no balanced target
in this stated F8^2:C7 coordinate-potential source-cost route beats 9/4.
General tensor degenerations and unequal targets with a side below nineteen
remain open. This written proof is unreviewed and gives no exponent improvement.

The [higher-slice unequal followup](research/ai/2026-10-20-f8-unequal/research_note.md)
also excludes every target of side sizes at least (16,16,26), in any order,
in this construction frame. All32 small integer pencils and520710 count
pairs are replayed exactly; seven-slice averaging gives8970/7>1280.
The proof is written and unreviewed. A (16,20,21) count pattern survives
the stated three-, five- and seven-slice necessary tests. Two restricted
nonlinear graph searches found no target: one reported untraced UNSAT,
the other timed out. The separately verified (4,4,3) positive control
does not pass the exponent gate. The arithmetic exponent remains9/4.

The [complete F8 coordinate closure](research/ai/2026-10-21-f8-coordinate-closure/proof.md)
now closes every unequal format in this one-source route. New even-slice
rectangular pencils reject the former(16,20,21) count survivor. Exact replay
checks64 pencils,9539875 pair tags and90 residual alignments across all12
minimal formats. Thus no single F8^2:C7 target through injective pair maps
and strict vertex potentials passes its usual source-degree gate at any
positive exponent at most9/4. The written proof is unreviewed. Arbitrary
complex degenerations, joint extraction and tensor powers remain open;
no arithmetic exponent improvement is established.

## All-size product-filtration result

[Written proof](research/ai/2026-10-20-concavity-equivalence/research_note.md) |
[Exact proof-chain checks](results/concavity-equivalence-2026-10-20/verification.json)

AI-FILTRATION-007 settles R2 for the three fixed-label two-source families:
for every positive, symmetric profile with `F(1,b)=b`, those families are
equivalent to separate concavity including the zero boundary. The matching
profile satisfies that boundary, so it survives **all positive integer
quadruples**, beyond the previous finite grid. Actual character profiles have
the boundary from the elementary restriction `B_Y(a) tensor B_X(b) >= C(a,b)`.

The written proof is unreviewed and not formalized. New exact checks cover
11,808 inequalities and 5,184 intermediate bounds on 1,296 source quadruples,
plus 4,860 inequalities at six larger or unequal sources. This rules out an
improvement based only on adding these families to the matching-profile
relaxation; it does not exclude coupled-fiber or oriented tensor constructions.
The exponent remains unchanged.

## Scaling and critical-shape bridge

[Analytic argument](research/ai/2026-10-20-concavity-equivalence/homogeneous_rigidity.md)
completes the second-pass draft under the stated replication and rank
assumptions. AI-HOMOGENEOUS-008 gives the full homogeneous limit and forces
the displayed unique shape, up to amplitude, at `t=3/4`, without assuming
differentiability. The diagonal derivatives agree as a conclusion at equality.
Uznański's earlier oriented rescaling is explicitly attributed.

AI-CURVATURE-009 proves the conditional criterion
`omega <= 9/(4(1+delta_0))` if the normalized limiting curvature is at least
the same positive `delta_0` for every relevant character. The limit and
derivative bridge are supplied; **the positive curvature premise remains
unproved**. Compactness also explains why excluding every endpoint character
would suffice for some strict, potentially nonnumerical improvement. No such
exclusion or smaller exponent is established. These written arguments have
no independent review or Lean formalization.

Concurrent reports at `712c91a` (fixed-label compatibility) and `30219d0`
(actual-character rigidity/curvature) overlap these conclusions and are
explicitly credited in the notes. Additional content here includes the
filtration converse and boundary counterexample, direct scalar limit proof,
and compactness consequence. These overlapping conclusions are not counted
as independent new advances or independent review.

AI-FATPOINT-GROWTH-010 gives a concrete conditional target using the all-degree
extension of the Koszul worker's fat-point tensor. A source cost factor below
`9/(7*2^(1/3))`, about `1.020472`, would beat 9/4. The cost-one case would imply
the rational bound `125/56`. **The source degeneration is unconstructed**, so
neither number is a new exponent result. The proof, exact threshold certificate
and 528 finite rank-identity checks are in the
[construction route](research/ai/2026-10-20-concavity-equivalence/fatpoint_growth_route.md).

The same branch now proves an arbitrary exact-restriction cost of at least two
for the canonical fat-point targets, using their special rank-`ka` slice.
This strengthens the concurrent maximum-slice estimate. The construction
must be singular. Fixed-shared-coordinate attempts are closed by the other
worker's stronger catalecticant obstruction at `6bdab15`; the active graded
discovery therefore includes an unrestricted shared basis. The completed
Chebyshev search covers 18,440 candidates and gives no finite profile violation.
No floating fit is accepted as a certificate.

## Selected SL(2,7) finite target

The [SL(2,7) lane](research/ai/2026-10-20-sl2-seven/README.md) derives its
complex group algebra block sizes through exact rational class-algebra
idempotents, without importing a character table. Integer root intervals
certify that a degeneration to M(16,16,17) would imply omega < 2247/1000.
**No such degeneration is constructed.** The source cost comparison is
conditional evidence for selecting this finite target, not an exponent bound.
Its SAT adapter credits and pins the concurrent group worker's implementation.
The exact source and graded-verifier checkpoint passes all 59 local tests.
The first 600-second run ended at its time limit with zero pair-injective
models and no witness. It provides no impossibility proof.

The follow-up [central-involution argument](research/ai/2026-10-20-sl2-seven/central_involution_proof.md)
shows that a pair differing by a central involution in one set forces the
other pair map to inject into the central quotient. For shape (16,16,17),
all three sets must therefore avoid central pairs. This adds 504 sound binary
clauses to coordinate-potential discovery. Exact checks cover 334 cancelling
two-term trades and the strict counting threshold. The claim concerns this
construction class, not every complex tensor degeneration.

The subsequent exact projection/lift reduction found 1,394 projected
SL(2,7) candidates in its first 600-second run. All fail the lift equations;
all 1,394 saved parity circuits replay using integer group arithmetic.
No candidate has reached a full degeneration witness. Ten focused controls
check the source, subgroup normalization, lift equations against exhaustive
small sign choices, certificate tampering and the cyclic-eight fiber rule.
The fiber-strengthened run separately rejected 149 candidates by replayed
circuits. Verified small parity cores can now be reused across independent
right translations and set permutations, with source hashes and explicit
occurrence clauses. These finite rejections are not a complete exclusion.
The first run with those templates separately rejected 619 candidates by
replayed circuits and supplied no pair-injective lift or tensor witness.

## Heisenberg source and coordinate frontier

The [Heisenberg lane](research/ai/2026-10-20-heisenberg-five/README.md)
derives the order-125 source degrees from explicit shift/phase operators.
Its conditional M10 comparison passes at 2247/1000, but the
[normal-coset incidence proof](research/ai/2026-10-20-heisenberg-five/normal_coset_closure.md)
now excludes every single target passing the source's 9/4 gate in the
injective-pair-map, strict-vertex-potential class. It applies the concurrently
merged rectangular Koszul bound, exhausts 3003 balanced and 410333 unequal
count cases, and uses affine-line pair-count contradictions. It does not
exclude arbitrary complex degenerations or establish a smaller exponent.

Separately, [stabilizer averaging](research/ai/2026-10-20-heisenberg-five/coset_averaging.md)
bounds the volume of the stated full cyclic-coset class by p^4 for every
odd prime p. Exact finite controls cover subgroup triples at p=3,5,7,
all 400 two-coset circuits at p=5 and 38 progression circuits at p=11.
These are written, unreviewed construction obstructions. The original
untraced SAT reports are retained as discovery history and are not proof
premises.

## Selected direct-product group target

The [SL(2,5) x C2 lane](research/ai/2026-10-20-sl2-five-c2/README.md)
selects M(13,13,15). Exact rational central idempotents derive the first
factor's degrees; the standard direct-product theorem repeats them twice.
Integer root intervals give a conditional omega < 2247/1000 comparison, and
the concurrent rank-locus screen requires 217<=240, so it does not exclude
the target. **The target degeneration is unconstructed.**

The adapter checks an order-48 subgroup and 60 center orbits, applies the
central-pair exclusions and reuses the pinned integer acceptance verifier.
Six controls check the source, projection, an embedded positive weighted
control, the unchanged SL(2,7) certificate and exact finite rejection replay.
The two initial 600-second target searches, with and without projected
inverse-class capacities, ended without a pair-injective model. These
timeouts exclude nothing. A separate structured-parent enumeration rejects
all 1,000 explicitly generated ten-point section triples by independently
replayed positive integer Farkas circuits; its finite scope is documented in
the [parent note](research/ai/2026-10-20-sl2-five-c2/structured_note.md).
The larger target remains open.

The [projected continuation](research/ai/2026-10-20-sl2-five-c2/projected_note.md)
adds necessary four-pair fiber capacities and binary equations over the
projected involutions. The first binary-filter run has 2,765 replayed
capacity certificates and 2,474 replayed parity certificates, plus 3,794
untraced solver cores and one budget skip. It produces no lift or witness;
the exact circuits do not upgrade the untraced parts into a complete proof.
All 720 full-space Koszul comparisons pass for this target. A separate
(12,12,17) comparison is also conditional on an unconstructed degeneration.

The [central cocycle extension](research/ai/2026-10-20-sl2-five-c2/pair_saturation.md)
uses the zero sum of all four central colors in a saturated projected pair
fiber. It yields exact equations for both bits, including the twisted
SL(2,5) bit. The first run rejects 169 candidates by replayed circuits.
A separate learning run has 244 replayed circuits, 1,075 learned necessary
rows, and one untraced inner refutation. Neither constructs a lift or
establishes a complete exclusion. All 4,096 normalized small lifts were
checked; the 128 with injective pair maps satisfy the necessary equations.

## Second-pass checkpoint

[Research and recovery record](research/ai/2026-10-20-session2/README.md) | [Supplementary claims](research/ai/2026-10-20-session2/claims.json) | [Verification](results/session2-2026-10-20/verification.json)

The dimension-only search covers 189 cases and finds 85 candidate scores. None is certified by dimension accounting alone. Exact tensor calculations reject two specific candidates.

The checkpoint includes draft homogeneous-profile rigidity and curvature criteria. Their missing hypotheses and unproved gains remain explicit. The stronger scoring search is incomplete, with no completed run.

The temporary second-pass files were not retained in the current runtime. Reconstructed programs and regenerated reports are labeled accordingly. All eight new checkpoint tests passed. The first-pass archive remains unchanged.

The [external source review](docs/external_followups.md) covers the three repositories suggested by the owner. It includes Filmus's finite identities-to-exponent criterion with its hypotheses. No external Lean rebuild is claimed.

## Koszul research pass

[General proof and scope](research/ai/2026-10-20-koszul/research_note.md) |
[Exact candidate audit](results/koszul-2026-10-20/candidate_audit.json) |
[Supplementary claim ledger](research/ai/2026-10-20-koszul/claims.json)

Written, unreviewed formulas now give every Koszul-flattening rank of a
convolution in every leg orientation, including padding of the shared space.
They reject **all 85 specific packings** saved by the second-pass dimension
search. This does not exclude alternative packings for those sources.

In particular, the former best candidate needs border rank at least 30 while
its source has rank 21. The all-size proof permits arbitrary independent
identifications of the shared block spaces. Exact coefficient matrices check
180 oriented cases and 27 padded cases; those finite checks are not the proof.

The matrix-multiplication exponent remains unchanged. New constructions must
pass these tests and still provide actual tensor identities.

The [intermediate-weight slice covers](research/ai/2026-10-20-koszul/intermediate_weights.md)
(AI-INTERMEDIATE-WEIGHT-COVERS-033) give exact source-cost constraints for
constant matrices followed by the specified shared and monomial weights.
For slopes alpha/beta tending to r in [1,2], the asymptotic source ratio is
at least 2-r/2. At the balanced direction (2,1), the finite bound is
B>=k*(N+floor(m/2))-(m-1). Thus the m=4,B=10k target is excluded for k>=2
within this class, including the previous k>=53 finite-profile target.
Single-copy m=4 and the growing-m balanced route remain open. The proof is
written and unreviewed; exact covers and small independent matching checks
validate finite cases without establishing an exponent improvement.

The [finite amplitude criterion](research/ai/2026-10-20-koszul/finite_amplitude.md)
(AI-FINITE-AMPLITUDE-CRITERION-034) offers a separate target: a universal
13/12 improvement over P_*(4,4) for near-endpoint characters would imply
omega<=2.249. **That finite lower bound is unproved.** An exact integer
certificate checks the conditional implication only. The accompanying
dimension screen (AI-MATRIX-EXTRACTION-DIMENSION-035) closes the analogous
direct-sum matrix-product extraction method for symmetrized C(a,a) at
a=2,3; a=4 survives the screen. Eleven retained floating permutation fits
in a different construction class supplied no exact witness.
The concrete finite alternative is to degenerate the product of all six
leg permutations of C(4,4) to M(106,106,106). That unconstructed target
would also imply omega<=2.249. The source/target leg dimensions pass, but
the group worker's abelian opposite-relation argument excludes coordinate
maps with diagonal weights. A Holder bound also excludes all-power
coordinate extractions into independent matrix products at this diagonal
(AI-COORDINATE-MATRIX-EXTRACTION-037). General linear cancellation remains open.

The [finite-target screens](research/ai/2026-10-20-koszul/finite_target_screens.md)
sharpen that distinction. An explicit binomial scaling gives uniform quantum
marginals for every C(a,b), so all singleton quantum functionals permit H106
(AI-QUANTUM-CONVOLUTION-SCREEN-038). An elementary entropy deficit excludes
all-power coordinate-and-weight independent-matrix extraction also at a=5
(AI-COORDINATE-ENTROPY-LOSS-039). Allowing arbitrary Laurent output maps while
retaining coordinate inputs still bounds square targets from S_4 by n<=93
(AI-LAURENT-OUTPUT-MATRIX-SCREEN-040); thus H106 needs input mixing.
These are written, unreviewed proofs. Exact controls cover 256 marginal
normalizations, 4877 rational convolution pairs and 43681 four-type bipartite
component count pairs. No new degeneration or smaller exponent is established.

The [smaller cyclic target](research/ai/2026-10-20-koszul/cyclic_finite_target.md)
uses three convolution factors and leg dimension 112. Its unconstructed
M(10,10,11) target would imply omega<=2.248 (AI-CYCLIC-FINITE-TARGET-041).
Every nonzero source slice has matrix rank at least 16, which excludes
constant linear maps to this target (AI-CYCLIC-MINIMUM-SLICE-RANK-042).
The all-a minimum-rank locus is also classified; its dimension excludes
constant restriction A_5 to M(13,13,17) (AI-CYCLIC-MINIMUM-RANK-LOCUS-043).
All 4095 nonzero F2 slices at a=2 agree with the minimum-rank formula;
the 27 equality cases agree exactly with the stated factorization.
These written proofs are unreviewed and leave singular degenerations open.

The [cyclic recoupling experiment](research/ai/2026-10-20-cyclic-recoupling/README.md)
(EXP-CYCLIC-RECOUPLING-044) now computes exact coefficients after a basis
change mixing all three factors on each leg. At a=4 its 2539 scalar blocks
factor into 175 representation-degree blocks. Sampled searches using exact
scores find no matching-profile violation. The full a=4 grouped binary
weight run also finishes with no violation across 1797505 distinct supports;
its best score ratio is about 0.258426. A separate exact determinant
certificate excludes interpreting the central 4-by-4-by-4 multiplicity
tensor as M2 under constant maps (AI-CYCLIC-CENTRAL-MULTIPLICITY-045).
This finite experiment supplies reusable coefficient data, not a degeneration
achieving the required gain.

The [agent-board review](docs/agent_board_review.md) attributes four external
research reports and records a checked correction: the published
Massarenti-Raviolo exact-rank bound excludes the board's n=34 through 37 search
window. At n=38 only rank 3585 survives the two lower bounds used here. This
does not exclude or construct border-rank algorithms.

Two further results sharpen the next construction target:

- [Mixed-sector survivor](research/ai/2026-10-20-koszul/research_note.md#6-an-all-size-family-that-these-necessary-tests-do-not-exclude):
  an explicit all-k family passes every full-space Koszul test on all three legs. Its score exceeds
  P_* from k=53 onward (first source C(4,530), ratio 37206/37205). The degeneration
  is unconstructed. Its canonical target has an explicit border-rank-10k
  certificate, but coordinate selection plus diagonal weights cannot realize it
  from that source: this restricted ansatz requires source length at least
  12k-1. Arbitrary changes of basis remain outside the obstruction.
- [Actual-profile rigidity](research/ai/2026-10-20-koszul/scaling_rigidity.md):
  Uznański's rescaling theorem and a one-sided derivative proof remove the second
  pass's missing analytic bridge and global C1 assumption. Every critical
  character must have the stated homogeneous profile. The curvature criterion
  now applies to actual characters, but a uniform positive curvature gain remains
  unproved. No exponent improvement follows yet.

The [all-dimension extension](research/ai/2026-10-20-koszul/all_dimension_targets.md)
now provides explicit targets T_m of dimensions (m,N,N), N=m(m+1)/2,
with border rank N and an all-size full-space Koszul survival proof. A source
degeneration C(m,B_m) to repeated copies, at asymptotic overhead below
9/(7*cuberoot(2))-1, would imply a smaller exponent. At zero overhead the
proved **conditional** implication gives omega<=125/56. The source
degenerations are unconstructed. Coordinate selection and diagonal weights
require asymptotically 50 percent overhead, so that ansatz cannot meet the
criterion. Exact replay covers 20,153 interpolation coefficients, 3,276
shared-leg Koszul degrees, and 495 gap-formula cases; five dedicated tests pass.

[Broader source obstructions](research/ai/2026-10-20-koszul/source_obstructions.md)
now exclude ordinary linear restrictions at low overhead, even with arbitrary
bases. A catalecticant argument also excludes arbitrary polynomial Y/Z changes
when X keeps its binary-form coefficient structure. General shared-factor
changes remain open. Exact coefficient controls construct the m=2 all-k and
m=3,k=1 cases; these fixed dimensions do not meet the growth criterion.
Bounded real/complex orbit fits found no new certificate and are not exclusions.
The polynomial-matrix argument in that note also shows why every projected
shared Koszul test and every linear equivariant Young/Pieri test of its stated
form must pass against this border-rank-B target. It does not cover all
other-factor or nonlinear invariants.

The concurrent minimum-slice argument strengthens the ordinary-restriction
overhead to asymptotically 100 percent; it is adopted with attribution to
`d2d505c`. A new [polynomial-basis audit](research/ai/2026-10-20-koszul/orthogonal_bases.md)
excludes degree-ordered orthogonal coordinate degenerations at low overhead
for all dimensions. Its exact Chebyshev permutation reduction additionally
excludes nonidentity shared orders for m=4,...,38, for every k and admissible B.
The latter is a finite enumeration, not an all-size theorem. Independent
small enumerations and normalized small construction controls pass. General
shared-factor transformations remain open.

A further [biform proof](research/ai/2026-10-20-koszul/arbitrary_shared_basis.md)
shows that the same catalecticant lower bound survives **every constant
invertible shared basis**, including independent identifications of the target
blocks. It therefore closes the enlarged constant-G graded search as well.
The proof uses a standard projective-dimension argument and remains unreviewed;
360 exact transformed-block ranks and independent coefficient checks support
its implementation. A genuinely singular shared map is still outside it.
The same proof extends to all matched bilinear blocks with no zero divisors.
It excludes the dominant-degree weight region alpha>(m-1)*abs(beta).
A separate explicit slice support cover excludes 0<alpha<=beta, requiring
B>=k*(2N-floor(m^2/4)-1)-(m-1). These close the recorded dominant-degree
experiment and two concurrent mixed-weight directions. Intermediate slopes
and general singular shared maps remain open; no exponent is improved.

The [single-copy pilot](research/ai/2026-10-23-mixed-family-single-copy/RESULT.md)
computes an exact determinant `1` for the ten shared projective factors in the
displayed border-rank-10 interpolation of `T_4`. No quadric contains all ten,
so they cannot be pointwise limits of the ten source evaluation factors under
a common shared-basis change when all target points stay distinct. This only
closes that termwise route. It does not exclude `C(4,10) -> T_4`, any path with
cancellations, or the replicated `k>=53` family, and gives no exponent bound.

Concurrent results are indexed with pinned commits in
[the collaboration review](docs/concurrent_research.md). They close the old
fixed-label filtration question and supply additional constructions and
obstructions, with their stated review and verification limits. They do not
establish an exponent improvement.

## Concurrent product-filtration constructions

The [new concavity proof](research/ai/2026-10-20-affine-direct-sums/research_note.md)
settles R2 for every displayed fixed-label product-filtration inequality:
all positive integer parameters preserve the matching profile P_*.
This replaces the earlier finite-only knowledge for that family. The proof is
AI-derived, written and unreviewed; it does not construct a tensor character.

The exact regression certificates check 81,648 comparisons over 4,096 source
quadruples, plus six dedicated tests. The universal statement rests on the
written proof. Full direct sums involving multiple labels remain outside this
theorem. No exponent improvement is established.

The [affine-line construction](research/ai/2026-10-20-affine-direct-sums/direct_sums.md)
adds explicit integer-weight degenerations retaining full direct sums across
several labels. Four exact determinant-basis examples check all 4,770
coefficients. A finite assignment upper bound covers 9,600,473 maximal
relaxed matchings on 6,561 ordered source quadruples through dimension 9;
none violates P_* at t=3/4.

Other agents independently pushed a stronger fixed-label equivalence theorem
at `73b2d20` and broader entropy-score bounds at `e6d33e7`.
[The overlap record](research/ai/2026-10-20-affine-direct-sums/COORDINATION.md)
separates their work from the distinct coefficient construction here.

## Off-leading recoupling blocks and low-border-rank sources

[Full Clebsch--Gordan coefficients and coverage](research/ai/2026-10-20-clebsch-gordan/README.md)
now retain actual k>i+j blocks discarded by the old filtration. Exact axis
and diagonal-factor certificates recognize convolution blocks. One interior
five-dimensional transvectant contains C(3,3), improving its lower score from
5 to 56/9. Completed binary/ternary outer-weight screens found no matching
profile violation; their exact scopes and overlapping counts are recorded.

[Truncated-polynomial algebra sources](research/ai/2026-10-20-truncated-algebras/README.md)
have explicit border-rank certificates and permit a direct critical-parameter
test against r^(4/3). Completed binary runs through r=7, including a stronger
output-deletion score, found no violation. Work on algebra products and
nonseparable weights remains active. See [the live queue](research/ACTIVE.md).

The [two-sector source-rank inequality](research/ai/2026-10-20-truncated-algebras/two_sector_bound.md)
now gives `2P(a,b)<=(a+2b-1)^(1/t)` at all sizes. With the concurrent
critical-shape theorem, the remaining t=3/4 amplitude must satisfy
`1/Gamma(4/3)<=K<=(16/9)^(1/3)`. The interval is nonempty. A separate
all-size argument proves P_* survives this entire inequality family with
cubed score at most 27/32, so a larger grid cannot exclude it.

[Exact scalar tight-support certificates](research/ai/2026-10-20-clebsch-gordan/subrank_blocks.md)
strengthen all 101 recoupling blocks in six sources. This uses the external
scalar theorem, without assuming a weighted block-transfer theorem. Added
outer-coordinate restrictions improve a finite score but do not violate P_*.

## Exact mixed-target collision experiments

The [new mixed-target package](research/ai/2026-10-20-mixed-restrictions/README.md)
allows arbitrary shared-coordinate permutations and output-coordinate sums.
Independent integer coefficient replay verifies the saved m=2,3 controls and
a C(4,11) to T_4 degeneration. Z3 reports UNSAT for m=4,B=10 in this larger
finite ansatz; m=5,B=15 timed out. No unbounded construction or smaller
exponent is proved. The local restriction and equivariant-flattening notes
independently overlap concurrent results, which are explicitly credited.

The [capacity refinement](research/ai/2026-10-20-mixed-restrictions/collision_capacity.md)
now excludes the exact-length permutation/collision ansatz for all m>=10.
The proof is written and unreviewed; near-unit asymptotic overhead remains
open. Proved solver cuts preserve the m=2,3 SAT controls and resolve the
m=5 query as UNSAT. The m=6 run times out; it supplies no exclusion.

The [quantitative capacity theorem](research/ai/2026-10-20-mixed-restrictions/asymptotic_capacity.md)
strengthens the obstruction to asymptotic overhead at least
`3/2-sqrt(3)/4` (about 1.066987) for the coordinate-input and constant-output
ansatz, even with arbitrary canonical target-copy counts and shared source
length asymptotically at most 5m/4. This exceeds the needed approximately
1.020472. General input mixing and general Laurent shared maps remain open.
The result is written and unreviewed, with 1,599 explicit integer-matrix
controls and exact algebraic comparisons. It does not improve the exponent.

The [Laurent-output extension](research/ai/2026-10-20-mixed-restrictions/laurent_capacity.md)
retains the same overhead lower bound when the output matrix is an arbitrary
Laurent family and the two inputs remain coordinate injections with Laurent
scalars. A joint index-and-valuation word supplies one common arithmetic
interval for the rank argument. An exact size-three control verifies the
broader model. This written proof leaves actual input mixing open.

## Paired convolution source ranks

The [paired-source proof](research/ai/2026-10-20-paired-sources/research_note.md)
computes an exact first Koszul kernel of dimension 3a-2 for two oppositely
oriented convolutions. It excludes the full-capacity matrix target for all
sizes under arbitrary complex degeneration, and excludes a promising
size-five direct sum. A complete integer budget certificate also bounds
the one-copy size-four factorwise matrix-block method below the finite
profile-improvement threshold. These written and finite results do not
exclude joint extraction from the full source or its powers.

The [all-power formula](research/ai/2026-10-20-paired-sources/all_koszul.md)
now gives every first-leg source rank. A separately derived matrix formula,
crediting Landsberg--Ottaviani's kernel inclusion, supplies exact comparison
ranks over C, and a second cohomological argument gives the same ranks
over every field. These written, unreviewed arguments exclude the initially
selected P_6 to M(6,10,6) target at power seven. Its former conditional
2.235 implication therefore has an excluded premise. The complete finite
frontier through a=13 contains 239 improving dimension-compatible single
matrix targets, modulo B/C exchange; all are excluded by saved rank
witnesses. The frontier through a=16 has 28 survivors, first at a=14.
No surviving target is constructed; joint extraction remains open.

The [two-block frontier](research/ai/2026-10-20-paired-direct-sums/README.md)
now enumerates every one-block or two-block matrix target through `a=10`.
After exact score comparisons and every first-leg Koszul degree, none
survives through `a=9`; at `a=10`, 19 pairs survive modulo B/C exchange
(EXP-PAIRED-DIRECT-SUM-FRONTIER-001). The selected target is
`P10 -> M(4,11,10) direct_sum M(10,12,6)`, in formats
`(100,190,190) -> (100,164,182)`. Its existence would force
`15840^t+25920^t<=3364`, hence `omega<1121/500=2.242`
(COND-PAIRED-DIRECT-SUM-002). Exact integer powers certify this implication.
**The degeneration is unconstructed.** Ordinary constant restrictions are
excluded; passing 100 first-leg rank comparisons does not supply singular
maps. These results do not constitute an exponent improvement.

The [boundary-chain construction](research/ai/2026-10-20-paired-construction/README.md)
now gives explicit restrictions `P_a -> M(a,2,a)` for every integer `a>=2`,
with coefficients `0,1,-1` (AI-PAIRED-CHAIN-001). A telescoping identity
proves the family over the integers, and full coefficient and ordinary
matrix-product checks cover `a=2,...,8`. The first `P2 -> M2` witness
includes four exact off-support cancellations. This is a positive tensor
construction, but its finite character gate has strict slack at `t=3/4`
for every `a`, so it does not improve the exponent. Its specific quotient
does not extend to square `M(a,a,a)` at `a=3,4,5`.

The [Laurent pilots](research/ai/2026-10-20-paired-direct-sums/laurent_search.md)
record four first-order alternating fits and two bounded refinements for
`P3 -> M(1,3,3) direct_sum M(3,3,2)`. Every completed run retains nonzero
full coefficient error or uncancelled poles. Exact positive and negative
controls check the coefficient verifier, and six saved coefficient arrays
replay the reported residuals. These finite failures do not exclude the
target or establish a degeneration (EXP-PAIRED-LAURENT-003).

The [second-order continuation](research/ai/2026-10-20-paired-direct-sums/higher_jet_search.md)
retains two completed degree-two Laurent searches with all pole and target
equations. Both have nonzero pole coefficients (EXP-PAIRED-HIGHER-JET-004).
The [narrow-source searches](research/ai/2026-10-20-paired-direct-sums/narrow_source_search.md)
test `Q_(3,2) -> M(3,2,3)` using eight full coefficient fits and ten kernel
compression runs, including two complex runs. None produces a construction.
Closure-only fits approach nearly singular normalization matrices; condition,
commutant, and trace-form checks reject those false leads. An exact algebra
recognition criterion and positive and negative controls accompany the
searches (EXP-NARROW-SOURCE-005, LEM-NORMALIZED-SLICE-006). All 24 new saved
points recontract to their reported metrics. Two lagging intermediate
checkpoints were recovered by deterministic reruns matching the complete
original numerical histories. These finite experiments imply neither
existence nor nonexistence of the proposed target.

The [complete narrow-source Koszul screen](research/ai/2026-10-20-paired-construction/narrow_koszul_exact.md)
computes all 25 exterior-degree comparisons on all three legs for
`Q_(3,2) -> M(3,2,3)` (EXP-NARROW-KOSZUL-001). Signed coefficient matrices
give exact rational ranks, with independent modulo-two eliminations
matching every value. The long target legs are padded from six to eight
coordinates before comparison. All tests pass; this supplies neither
the desired maps nor an exponent improvement.

## Varying quantum recoupling

The [quantum family](research/ai/2026-10-20-quantum-recoupling/family.md)
uses rational Clebsch--Gordan changes of basis that vary with q. Explicit
local factors keep the generic source isomorphic to convolution. Exact
controls check 196 projection positions, 360 invariant equations and 30
small basis/root configurations. At q=i, the rowwise-regular cyclic maps
have ranks 8,32,64 at a=2,3,4 over Q(i). This calibration produces ordinary
restrictions and does not supply the size-four matrix target. Coupled
singular normalizations remain open; no exponent improvement is claimed.

The [paired quantum calibration](research/ai/2026-10-21-paired-quantum/README.md)
checks 64 prescribed local maps and 353 rational-function source identities
(AI-PAIRED-QUANTUM-001). At size ten and root order fourteen, the specified
rowwise regular first map has rank 91, below the selected target's 100.
Two small regular limits have matching matrix-tensor dimensions but fail
exact slice-algebra closure tests. These calculations concern the stated
normalization only.

Two [coupled Laurent families](research/ai/2026-10-21-paired-quantum/coupled_faces.md)
now give exact intermediate tensors `P3 -> F0,F1`, each of format `(9,15,15)`
(AI-PAIRED-QUANTUM-002). The verifier checks all 288 nonzero rational-function
coefficients, proves cancellation of every pole, and records 241 and 108
nonzero rational leading coefficients. Both tensors pass every first-leg
Koszul test for the small two-block target, but an invertible source slice
excludes an ordinary restriction. `F1` has a rank-two first slice, and a
closed projective incidence argument excludes every further degeneration
to that concise target, whose minimum first-slice rank is three. Further
singular extraction from `F0` remains a construction question. These are
actual intermediate degenerations, not matrix direct sums or smaller
matrix multiplication exponents.

The [unequal quantum extension](research/ai/2026-10-21-narrow-quantum/README.md)
gives explicit generic local maps for every `Q_(n,m)`, with an all-size
coefficient identity and 841 finite controls (AI-NARROW-QUANTUM-001).
Twenty-three specified root-eight Laurent families for `Q_(3,2)` have
complete exact coefficient and valuation certificates. Nine limits lose
first-leg concision, ten have rank-one slices that exclude all further
degenerations to the target, and four fail a Koszul comparison. Two of
those four pass every first-leg test but fail a long-leg test by one rank
(`62<63`). These are fixed-family exclusions; other bases, weights, and
singular maps remain open.

## Polynomial flags and numerical calibration

The [polynomial flag argument](research/ai/2026-10-20-singular-flags/normal_form.md)
reduces arbitrary constant matrices followed by strict target-compatible
weights to decreasing input-degree flags and increasing output-pivot flags.
An equal-degree coefficient is a product of nonzero pivots. This excludes
the earlier m=4,B=10 grading eta=(7,14,21,0), and forces B>=N+m-1 in the
stated separated cone. The proof is written and unreviewed. Balanced orders
and arbitrary Laurent input mixing remain open; the additive cost does not
close the asymptotic construction question.

An [exact source-family calibration](research/ai/2026-10-20-singular-flags/masked_residuals.md)
has partial squared error t^(-6) while full squared error is
t^(-6)+2t^2+t^8. The retained balanced complex pilot likewise has no valid
certificate: its smallest partial residual is about 5.25e-8, but the full
relative error is about 61501 at the best parameter in the recorded interval.
All discovery reports remain experiments. Exact controls preserve known
m=2,3,4 limits through the full normal-form reduction.

The [balanced coefficient system](research/ai/2026-10-20-balanced-coefficients/elimination.md)
now gives an exact algebraic construction problem in a restricted monic
flag ansatz: 53 integer polynomial conditions of degree at most 12 in 57
parameters, after 68 coefficients are eliminated by unimodular systems.
An exactly checked finite-field solution with full-row-rank Jacobian would
lift to characteristic zero by standard Hensel theory. No qualifying point
or complex degeneration has been found. Monic pivots are an additional
restriction; the written reduction does not settle general constant maps.

## Whole-filtration entropy investigation

Branch `research/full-filtration-entropy-20261020` studies the whole support
`i+j=k`, separately from the other workers' Koszul and matched-row audits.
[Written proof](research/ai/2026-10-20-full-filtration/research_note.md) |
[Exact certificates](results/full-filtration-2026-10-20/entropy_certificate.json).

- AI-FULL-ENTROPY-001: an analytic dual certificate bounds every probability
  distribution in the explicitly defined optimistic entropy score.
- AI-BALANCED-ENTROPY-002: for every integer `n>=2`, that score for the balanced
  source `C(n,n)^2` is at most `39/40` of its matching source profile. The proof
  uses 3,794 exact block tests for sizes 2--22 and a positive-coefficient
  polynomial for every size at least 23.
- EXP-FULL-ENTROPY-001: all 20,736 source tuples through size 12 admit exact
  upper certificates over their entire probability simplex.

These are unreviewed analytic results and exact finite certificates. The
optimistic score is not claimed as a proved weighted block-extraction theorem.
A first-party [Codex audit](research/reviews/full-filtration-entropy-proof-review-2026-10-23.md)
found no gap in the all-distribution certificate or its balanced all-size
bound. The claims remain unreviewed pending independent human review; the
audit does not change their scope or exponent status.
The all-size unequal-source inequality is now settled by the
[sharp unequal-source proof](research/ai/2026-10-20-unequal-entropy/research_note.md)
(AI-UNEQUAL-ENTROPY-001). For every four lengths at least two, the explicit
upper certificate has ratio at most
`B=(81/350)*(1+14*sqrt(14)/27)^(4/3)`, with
`0.974772906<B<0.974772907`, attained only at `(2,2,2,2)`.
Every other tuple has ratio at most `97/100`. Eight all-size polynomial
cones, 216 small-minimum tail certificates and 37 proved residual cases
support the analytic proof. It is written and unreviewed. The sharpness
statement concerns `U`, not the entropy optimum or the exponent.

A first-party [Codex audit](research/reviews/unequal-entropy-proof-review-2026-10-23.md)
found no gap in the all-size certificate proof. The claim remains unreviewed
pending independent human review; this audit does not change the theorem scope
or exponent status.

## Exact finite-group construction campaign

[Research note](research/ai/2026-10-20-group-potentials/research_note.md) |
[Reports](results/group-potentials-2026-10-20/) |
[Integer-only verifier](research/ai/2026-10-20-group-potentials/verify_reports.py).

The SL(2,5) source degrees are now checked from nine primitive central
idempotents, with all 81 products verified over Q(sqrt(5)). Exact integer-root
intervals show that a degeneration of one of the three reported target shapes
would imply `omega <= 2249/1000`. **That degeneration is unconstructed.**

A new written, unreviewed determinant-divisor argument excludes a target
`M(n,n,p)` whenever a source irrep degree `d>N-np` is not divisible by `n`.
It removes three small affine-group candidates under arbitrary basis changes,
beyond the coordinate-potential search class. It does not exclude the SL(2,5)
targets or establish a smaller exponent.

The exact search has a genuine (3,3,3) control degeneration and 479 verified
Farkas cuts across two control/candidate runs. The larger target runs timed out
or returned SAT-solver UNSAT without proof traces; these are not independently
checked nonexistence results. Construction research continues.

The [rank-locus dimension proof](research/ai/2026-10-20-group-potentials/rank_locus_proof.md)
now excludes the original SL(2,5) shapes **(9,9,12)** and **(9,10,11)** under
arbitrary complex tensor degeneration. The explicit source rank-eight variety
has dimension 14, forcing required source dimensions 122 and 124, respectively,
against the actual dimension 120. This is a written, unreviewed proof, not a
SAT-derived exclusion.

An exact finite enumeration of every sorted shape passing the degree-sum gate
at 9/4 leaves only **(10,10,10)** after this screen. That shape and selected
larger affine-group candidates remain unconstructed. The same rank-locus
screen removes several affine cases that had only untraced SAT negatives.
The abelian-coset ceiling lemma and exact normal-subgroup tables further
strengthen discovery constraints; these restrictions do not constitute an
exponent improvement.

The [normal-subgroup Fourier proof](research/ai/2026-10-20-group-potentials/ternary_fourier_proof.md)
excludes three four-point unique-sum sets in C3^4. Its elementary integer
bound is 1232 versus the Parseval requirement 1088. This excludes the
coordinate-potential (16,16,16) ansatz in index-four extensions of that group;
it does not exclude arbitrary complex degeneration. The proof is unreviewed.

An exact finite affine-source frontier leaves 58 conditional candidate shapes
among 45 groups of order at most 250 with normal prime subgroup at most 61.
New F4^3:C3 offset searches checked 426 pair-injective candidates, all rejected
by exactly replayed Farkas circuits. No qualifying degeneration was found.

A further [fiber-mean argument](research/ai/2026-10-20-group-potentials/crossed_means_proof.md)
excludes an entire affine-plane base family in F4^3:C3, including arbitrary
other plane directions and offsets. Its hypothesis is scalar invariance of
two complementary base-plane sums. Two opposite strict mean inequalities
give the contradiction. This written proof is unreviewed and has a narrower
scope than arbitrary group-algebra degeneration. Another 2000 discovered
direction assignments have exactly replayed mean certificates.

The [F8 source campaign](research/ai/2026-10-20-group-potentials/octal_research.md)
now has exact local packing frontiers and a streaming whole-support verifier.
The F8^2:C7 frontier reduces 3942 local direction triples to 342 classes;
global constructions remain unresolved. In F8^3:C7, 87 proposed deletions
from an explicit pair-injective parent fail exactly replayed potential
constraints. Another 10752 symmetry-transformed circuits verify exactly.
The resulting hole-hitting search timed out. No target degeneration or
exponent improvement follows from these source and obstruction certificates.

## Exact small cyclic mixed-map construction

[AI-CYCLIC-MIXED-RESTRICTION-046](research/ai/2026-10-20-cyclic-mixed-map/README.md)
supplies explicit integer maps for the ordinary restriction
A_2 -> M(2,3,4). All 576 coefficients agree exactly, including all 552
required zeros; the identity holds over every field. The three matrices
have 40 nonzero entries in total, all +/-1. This strengthens the earlier
rational M(2,3,3) witness, which is retained with its discovery history.
The certificate has no independent mathematical review or Lean
formalization. Its profile lower bound is weaker than the existing scalar
bound, so it does not improve the exponent. Larger mixed or singular
constructions remain open.

The [all-power full-capacity argument](research/ai/2026-10-20-cyclic-mixed-map/full_capacity.md)
(AI-CYCLIC-FULL-CAPACITY-047) excludes arbitrary complex degenerations
from A_a^r to direct sums of square matrix products that use every source
coordinate. It combines an all-power minimum-slice-rank formula with
external polystability theory. In particular A_5 -> M15 and S_4 -> M112
are excluded even with singular maps. The smaller H1100 and H106 targets
remain open; this gives no uniform asymptotic gap or exponent improvement.
The proof is written and unreviewed. Finite controls check 112 triangular
minors plus an independent tensor-square coefficient expansion.

[AI-CYCLIC-CENTRAL-POLYSTABILITY-048](research/ai/2026-10-20-cyclic-recoupling/central_polystability.md)
strengthens the earlier ordinary-map exclusion for the degree-(6,6,6)
central multiplicity block B: B cannot degenerate to M2 over C. Four exact
rational polynomial identities prove smoothness of its associated cubic;
external stability theorems and cyclic symmetry yield a closed special-linear
orbit. The earlier determinant obstruction then excludes the required
isomorphism. This concerns B itself, without cancelling its accompanying
scalar tensor. The proof remains unreviewed and gives no exponent gain.

## Graded cyclic construction pilots

[EXP-CYCLIC-GRADED-PILOTS-049](research/ai/2026-10-20-cyclic-singular-search/README.md)
records four exact kernel certificates blocking one-sided new-vertex
extensions of two fixed M(2,3,3) witnesses. Changing the old maps or using
more general Laurent maps remains open. Two 16-start weighted ALS searches
and two refinements supplied no exact M3 degeneration. Saved diagnostics
include large omitted coefficients; masked residuals are not certificates.
The exponent is unchanged.

## Equivariant cyclic construction obstruction

[AI-CYCLIC-EQUIVARIANT-050](research/ai/2026-10-20-cyclic-equivariant/README.md)
proves an all-size five-coefficient polynomial obstruction to diagonal-SL2
equivariant A_a to M_(2a-1) degeneration with irreducible vertex actions.
Exact representation counts also exclude all choices of matrix-vertex
representations for the specified H1100 equivariant ansatz; A2 to M3 is
closed by combining the count with the polynomial identity. General maps
that break this symmetry remain open. The proof is unreviewed; the exponent
is unchanged.

[EXP-CYCLIC-CARTAN-FRONTIER-051](research/ai/2026-10-20-cyclic-equivariant/torus.md)
relaxes the action to its torus. Exactly one necessary H1100 vertex-character
triple survives an exhaustive 89-case integer coefficient search. This
selects 3854 allowed map entries, but supplies no construction. Completed
32-start A2 and six-start H1100 pilots found no exact witness; several of
the latter escaped to large norms.

## Changed first jets at the quantum root flags

[AI-QUANTUM-EXTENSION-SPACES-075](research/ai/2026-10-21-quantum-extension-spaces/proof.md)
uses the concurrent partial-saturation argument to force dim W1=12 for
M(10,10,11) with the prescribed rank-four leading images. Exact rational
constraints classify all changed first derivatives: 20 dimensions per new
output row and 532 coupled leading-row parameters, totaling 4772 for two
110-row maps. The bilinear next component has first flattening rank 25
and maximum matrix-slice rank at most eight. Other second-jet terms remain
free, and no complete degeneration or smaller exponent is established.
The proof is written and unreviewed.

[AI-QUANTUM-BOUNDARY-TRAP-076](research/ai/2026-10-21-quantum-extension-spaces/proof.md)
excludes all orders when the four leading output rows stay in explicit
56-dimensional boundary spaces; the other rows may vary arbitrarily.
A separate necessary bound caps the second partial saturated space at
37 dimensions for all compatible first derivatives. Moving leading rows
outside those spaces remains open, and compatible first-order directions
that do so exist. These written proofs are unreviewed.

## Maximal first jets with moving leading rows

[AI-QUANTUM-MAXIMAL-JET-077](research/ai/2026-10-21-moving-boundary-flags/proof.md)
extends the boundary obstruction to moving leading rows when both outside
first-jet quotient ranks are 16. Exact linear systems leave only four
normal directions. They move a common polynomial plane, and a formal
induction confines the full maps to spaces of dimension 56. Thus these
maximal first extensions cannot reach M(10,10,11) at any order. At least
one first extension must be rank-deficient for a possible construction
with the same leading maps. The written proof is unreviewed; delayed
growth and other flags remain open, and the exponent is unchanged.

[AI-QUANTUM-RANK-FOUR-078](research/ai/2026-10-21-moving-boundary-flags/rank_deficient.md)
strengthens the necessary first-extension threshold: at least one quotient
rank must be at most twelve. Every nonzero one-leg obstruction has rank
at least four, proved by three rounds of exact triangular minors and
linear restrictions. Thus arbitrary quotient spans of dimension at least
thirteen on both sides are excluded at every order. The lower-rank and
delayed cases remain open; this is a written unreviewed result, with no
exponent improvement. The concurrently inspected second-jet package at
d8de82f already gives the stronger conditions W2=W0 and rank sum at most
24 (at most20 with mixed directions); the rank-four certificate is retained
as auxiliary structure, with no claim to improve that target frontier.

## Exact mixed second-order family

[EXP-MIXED-TWOJET-FAMILY-079](research/ai/2026-10-21-mixed-first-jets/family.md)
constructs sixteen independent leading-row directions with first-extension
quotient ranks14 and6. Explicit maps and regular first-row corrections
solve every coefficient equation through order two for every combination
of the parameters. The separate constructor and full coefficient verifier
retain all136 quadratic monomials. The active output formats are18 and10;
later growth and a matrix target remain unconstructed. An exact nonzero
third coefficient is retained as an order-boundary check. This finite
polynomial certificate does not improve the exponent.

[AI-MIXED-THIRD-ORDER-080](research/ai/2026-10-21-mixed-first-jets/third_order.md)
now excludes the target for these fixed 14-by-6 first subspaces at every order.
The exact normal space has dimension 16. Successive universal matrix-rank
covers impose six plus six independent constraints, leaving only the four
common-plane tangents. Arbitrary correction-row freedoms vanish from the
projected obstruction, and formal induction bounds both map ranks by 56.
This is an unreviewed scoped proof; other mixed spaces and delayed growth
remain open, and the exponent is unchanged.

[AI-MIXED-PENCIL-FRONTIER-081](research/ai/2026-10-21-mixed-first-jets/pencil_frontier.md)
extends this exclusion to **every** maximal mixed pair of quotient ranks
14 and 6, in either order. Exact source symmetries reduce the pencils to
two representatives. Target slice-rank divisibility bounds the generic
projected third space by dimension two; twelve cubic minors force it to
vanish and leave only plane motion. The necessary mixed first-rank sum
therefore drops from 20 to **19**. If both mixed projections are nonzero,
the block argument already gives sum at most 16. These are scoped,
unreviewed obstruction results, with no change to the exponent. The
concurrent third-boundary proof at `1068ce9`, Section 5, independently
proves a broader target-side third-rank ceiling; that overlap is credited
in the pencil note.

## Simultaneous mixed first projections

[AI-BOTH-MIXED-FIRST-SPACES-082](research/ai/2026-10-21-both-mixed-first-spaces/proof.md)
shows that when both mixed projections are nonzero, each must be a line,
even with arbitrary boundary graph corrections. Rank-one lines have a
unique partner relation and quotient ranks at most 7 each. Invertible
mixed lines force quotient ranks exactly 1 each. The necessary sum in
this case drops from 16 to **14**. Exact compatible 7-by-7 and 1-by-1
first spaces are retained; their polynomial maps still have first rank 12.
The invertible-line example leaves 72 normal directions before further
lifting equations. This is a written, unreviewed local classification,
not a matrix target or exponent improvement.

## Invertible-line lifting equations

[EXP-INVERTIBLE-LINE-LIFTS-083](research/ai/2026-10-21-invertible-line-lifts/calculation.md)
reduces the selected invertible seed's normal dimension from 72 to 40
using the target's zero projected third block. A specified 36-direction
ansatz has sixteen exact quadratic conditions for second leading rows
and third new rows. A retained compatible control has uncorrected first
rank 13. Third leading rows and later coefficients remain to solve;
these equations do not classify arbitrary corrections or construct the
matrix target. The linear decomposition is not a nonlinear gauge reduction.

## Regular root flags and Laurent first-leg maps

The [saturated-rowspace argument](research/ai/2026-10-20-graded-quantum-flags/saturation.md)
proves a source-leading-map slice bound while allowing an arbitrary Laurent
first leg and arbitrary regular higher jets on the other two legs. Exact
root-map certificates give ceilings 62,44,64,68,86 at orders 4,8,12,16,24,
below the size-four target's required slice rank 100. A separate
[central-weight proof](research/ai/2026-10-20-graded-quantum-flags/graded_obstruction.md)
excludes sixteen order-three/six phase pairs under the stated grading
hypotheses, using explicit nonzero coefficients over Q(zeta_6).
The unique Cartan profile is adopted from claim 051; the second integer
recursion only checks that earlier result. All new proofs are written and
unreviewed. Different flags, ungraded constructions and powers remain open.

## Candidate quantum quotient and weight-block comparisons

[AI-CYCLIC-ROOT-MODULES-053](research/ai/2026-10-20-cyclic-weight-blocks/root_quotient.md)
realizes the formal negative-singlet vertex character as an actual quantum
quotient at a root of unity. The quotient keeps a divided-power connection
that would be lost by treating its ordinary-generator pieces independently.
This supplies target representation data, not the required tensor maps.

[EXP-CYCLIC-BLOCK-FLATTENINGS-054](research/ai/2026-10-20-cyclic-weight-blocks/README.md)
retains 14364 grading upper comparisons and 3924 modular source-rank
comparisons on the selected A3, A4, A5 blocks. None excludes its target.
The specified quantum leading flags closed by PR33 remain closed, and no
exponent improvement is established.

## Size-five Cartan frontier

[AI-CYCLIC-CARTAN-SCREENS-052](research/ai/2026-10-20-cyclic-equivariant/a5.md)
uses exhaustive character factorizations and a five-inequality dual certificate
to exclude three of the four size-five targets that passed the general
constant-map screens, within the specified Cartan-intertwining class.
M(14,14,15) still passes the displayed character and extreme-slice tests.
An actual degeneration to it would imply omega<2.245; it is unconstructed.
Completed 32-start size-three and six-start size-five pilots produced no exact witness.

## Quantum first jets with constant output projections

The [first-jet saturation proof](research/ai/2026-10-20-quantum-jet-filtration/proof.md)
removes the grading assumption for the prescribed order-three/six quantum
curves. Thirty-two nonzero 64-by-64 minors give a full-output slice ceiling
56, allowing arbitrary Laurent first-leg maps and all nonzero approach rates,
orders and higher terms. A separate uniform inactive-slice argument gives
ceiling 94 after arbitrary constant codimension-two output projections
before taking the limit. Both ceilings are below the target's required 100.
Claims AI-FIRST-JET-SATURATION-001 and AI-QUANTUM-CURVE-JETS-002 are written
and unreviewed. Six completed finite-field coefficient pilots are retained
as discovery data only. Parameter-dependent projections, different leading
flags and non-scalar block weights remain open; the exponent is unchanged.

The [higher-jet extension](research/ai/2026-10-20-higher-jet-quantum-flags/higher_jets.md)
also permits moving output maps that remain surjective at the limit, with
slice ceiling 98. Leading output ranks below 110 remain open. Separately,
[256 single-leading-block flags](research/ai/2026-10-20-higher-jet-quantum-flags/blocks.md)
in the specified two-layer family have saved minors giving ceiling 97 for
regular full-output limits; pre-limit projections are outside that finite
cover. The new proofs are written and unreviewed. None gives an exponent gain.

The [second-jet spanning certificate](research/ai/2026-10-21-second-jet-rank-one/rank_one.md)
sharpens PR45's bound37 to W2=W0 of dimension12 at its canonical leading
flags. Twenty-six exact rank-two slices span the entire25-dimensional
bilinear image. Including the complete second derivatives and row correction
leaves every potential second target residue below the minimum matrix rank11.
The actual bilinear first-jet product must therefore vanish. Its effective
first-row rank sum is at most24, or20 after a mixed component. These proofs
are written and unreviewed; higher-order lifting and the exponent goal remain
open. Canonical extension data and their earlier classification retain PR45's
credit.

## Local audit of an external tensor-degeneration preprint

The [exact local audit](research/ai/2026-10-21-sun-local-audit/README.md)
reconstructs selected maps from arXiv:2610.13971v1, with the inspected HTML
pinned by hash. It finds a repairable scalar normalization omission and
verifies four local Laurent leading tensors, four generic endpoint blocks,
and 256 crossed-group identities. The complete M32 maps remain unverified;
the preprint's claimed exponent improvements are not adopted.

A separate elementary centroid argument excludes a bridge that first
collapses to the fixed zero-fibre tensor D256 tensor M2 and then seeks M32.
This narrower obstruction does not exclude every enriched assembly.
The audit and written proof remain AI-derived and externally unreviewed.

The [packetwise follow-up](research/ai/2026-10-21-sun-local-audit/packet_lift.md)
shows that an individual printed generic packet contribution contains M2,
whose exact Koszul rank exceeds that packet's stated border-cost ceiling.
It excludes a lift preserving each such contribution, while allowing the
possibility of different global maps with interpacket cancellation.

## Two rectangular summands with asymmetric leg losses

[AI-RECTANGULAR-DIRECT-SUM-001](research/ai/2026-10-21-rectangular-direct-sums/README.md)
extends the ordinary slice/Hankel tests to unequal direct-sum leg dimensions.
An exact two-block search checks 62 source formats through dimension 960.
The first surviving necessary-test format is A(7,9), dimension 945, with
19 normalized candidates; A(8,8) has 552. All other formats in that finite
range are excluded for this two-block score. The candidate M(27,27,28) plus
M(6,6,2) would imply omega<2.2495 if constructed; its maps are missing.
The proof is written and unreviewed, and no exponent improvement is established.

## Rank-three saturation closes the rectangular survivors

[AI-RECTANGULAR-SATURATION-002](research/ai/2026-10-21-rectangular-direct-sums/saturation.md)
proves a low-rank linear-projection density lemma and combines it with 12,870
integer Hankel-space certificates. It excludes all 571 survivors of the earlier
two-block screen. In particular, A(8,8) to M27 plus M7 is now excluded for
ordinary maps, superseding its open-candidate status above. No two-positive-
rectangular-block ordinary target in the 62 tested source formats through
dimension 960 passes the stated 9/4 comparison. Singular degenerations and
larger sources remain open. The proof is written and unreviewed; no exponent
improvement is established.

## Extended rectangular screen and second boundary

The [second-boundary proof](research/ai/2026-10-21-rectangular-direct-sums/second_boundary.md)
and a strengthened low-rank projection argument extend the ordinary necessary
conditions. The completed additional 24-format search through source dimension
1500 leaves 50 normalized candidates for A(8,9), 3425 for A(8,10), and 994
for A(9,9); all other formats in this extension are excluded by these tests.
A(7,10)'s 1143 initial candidates are all excluded. The first remaining source
is now dimension 1152, after the later crossed-dimension exclusion of M30 plus M3.
The compact report stores deterministic hashes of complete retained/excluded
lists and the first 20 retained rows per format; the script regenerates them.

An [exact equality counterexample](research/ai/2026-10-21-rectangular-direct-sums/equality_next.md)
shows why the existing lower-rank fixed-scheme proof cannot simply be extended
to full-row-rank symbols. The general obstruction proofs remain unreviewed.
No target maps or smaller exponent have been established.

## Source-weight windows and full original-source Laurent fibers

Claims `AI-WEIGHT-WINDOWS-098` and `AI-ORIGINAL-JET-FIBERS-099` preserve
two completed local packages. No exponent below 9/4 is established.

Every ordinary A88 to M27 plus M7 restriction needs at least one
matrix-unit image whose source weights span at least four. The exact
width-three containing-space sequence is 960,948,906,844,622, contradicting
the required 778 dimensions. Width four is a proved fixed point of this
particular screen. An explicit slice over Q(phi), phi^2=phi+1, has rank 384
although its middle homogeneous component has rank 512. It supplies one
cancellation direction, not full target maps. See
[the proof and exact acceptance certificate](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_weight_windows.md).

The original-source Laurent construction has generically invertible
960-by960 maps on all three legs, exact cancellation of every negative
power, and 28,316 nonzero constant coefficients. A recorded coordinate
projection is concise in format 936 by 936 by 935. However, 42 selected rows
per leg cover the complete constant support, so its slice rank is at
most 126. The intended M27 plus M7 target has slice rank 778. Consequently
this limit cannot reach the target by restriction or further degeneration.
The full source and other Laurent families remain open. See
[the complete maps, fiber equations, and cover proof](research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_original_fibers.md).

The source-map, fiber-system, rank, coordinate-cover, and tamper checks
pass in the same generating session. The proof status remains written
and unreviewed externally. The next construction searches use moving
physical compression spaces and the exact weight-mixing module equations.

The [corrected prolongation family](research/ai/2026-10-21-corrected-prolongation/proof.md)
constructs complete second jets with fixed boundary first frames. Exact
off-diagonal constraints reduce532 leading parameters to172; all36 remaining
quadratic obstructions vanish identically. Twenty-eight independent leading
directions still leave the fixed boundary spaces. Two exported rational
witnesses verify the entire first and second coefficients, including both
source-row corrections. These are finite-order data, not a matrix limit.
The boundary-frame matrix-target lifting question is closed by the following
third-order argument; the exponent goal remains open and the proof is unreviewed.

The [third-order boundary trap](research/ai/2026-10-21-third-boundary-trap/proof.md)
excludes these full boundary first frames at every order, including delayed
and unequal first-growth orders. An exact normal calculation leaves28
parameters; the third block has coefficient image24 and sharp minimum
nonzero first rank8. The matrix target forces first rank at most2. Only
four common polynomial-plane motions remain, and formal induction traps
both regular leg maps in dimension56. Ordinary effective first rank sum24
is therefore excluded; the necessary sum is at most23. A separate general
consequence forces third first rank at most2 on K_inf for every admissible
ordinary first pair at these flags. The complete PR49 second jets remain
valid finite data. These proofs are written and unreviewed; different first
subspaces and leading flags remain open, and no exponent improvement follows.

The [arbitrary-hyperplane extension](research/ai/2026-10-21-boundary-hyperplanes/proof.md)
now excludes both first boundary dimensions at least11 at every order,
including delayed unequal growth. It covers every complex hyperplane.
Boundary obstruction matrices have minimum nonzero rank2. The full third
matrix span is S0 tensor Mat2, with dim S0=20 in Mat6x6 and no rank-one
matrix; exact polynomial identities certify this. A general compression
lemma loses at most5 slice dimensions under two arbitrary hyperplanes.
First rank at least8 therefore leaves at least3, above the target ceiling2.
At ordinary first order one effective rank is at most10 and the total is
at most22. Pairs12,10 remain open. The proofs are written and unreviewed;
no matrix-multiplication exponent improvement follows.

The [crossed-flattening equality lemma](research/ai/2026-10-21-rectangular-direct-sums/equality_crossed_flattening.md)
retains a valid consequence where the fixed-scheme extension fails. At full
slice equality rank(M_F)=ab rank(B_F), the crossed coefficient flattening
has the same rank as B_F. Thus an ordinary A89 to M30 plus M3 map must take
every rank-at-most-three large-block parameter to crossed rank at most eight.
This condition alone is not an exclusion. Exact finite controls include the
A89 counterexample family, which satisfies the new condition as required.
The written proof remains unreviewed and the exponent is unchanged.

The [block-Hankel dimension proof](research/ai/2026-10-21-rectangular-direct-sums/block_hankel_dimension.md)
now excludes ordinary A89 to M30 plus M3: its171-dimensional rank-three
parameter variety would inject into a crossed-Hankel variety of dimension136.
The proof includes both common-input and common-output exceptional components.
That checkpoint excluded11 further A89,217 A810, and78 A99 candidates,
leaving62,3687,1263 respectively. A source slice of exact rank577 also shows
why576 cannot be rounded upward. All these general proofs remain unreviewed;
no smaller exponent or actual improved target maps have been established.

The [biform third-core theorem](research/ai/2026-10-21-biform-third-core/proof.md)
identifies the entire third tensor as the4,2,2 outer-product tensor times
a4-by6-by6 core. Its matrices lie in the kernel of ordinary biform
multiplication of degrees(1,2) and(2,1), under determinant-one basis
changes. This gives a short rank-one exclusion and improves the actual
two-hyperplane loss bound from5 to the sharp value3. A general sharp
projection lemma for losses1,3 and conditioned obstruction minimum4 then
exclude every arbitrary boundary first pair of dimensions at least11,9,
in either order, including delayed unequal growth. The necessary ordinary
first-rank sum at these flags is now at most20. Pure boundary pairs12,8
and10,10 remain at that threshold; a retained general losses2,2 control
shows why the new projection lemma alone cannot close them. These are
written unreviewed proofs, not an exponent improvement.

The [bundle-extension dimension proof](research/ai/2026-10-21-rectangular-direct-sums/bundle_hankel_dimension.md)
supplies an all-rank crossed-Hankel bound, with classical P1 splitting credited.
It removes543 more ordinary candidates beyond the exact equality screen.
The current retained counts are50 A89,3425 A810,994 A99. Its geometric argument
is written and unreviewed; finite controls verify10544 splitting-type arithmetic
cases,23402 Cech entries, and495 generic-matrix comparisons. No exponent gain
or surviving target construction is established.

The asymmetric SL2 continuation supplies exact rational A33 to M(5,5,3)
maps, replayed on every original source term. Its pencil invariant excludes
the remaining dimension-five SL2 vertex pattern for full M5, including its
equivariant closure. A separate cubic cap excludes ordinary A33 to M6.
These are small constructions and restricted obstructions, with no exponent
improvement. See `research/ai/2026-10-21-asymmetric-sl2-seed/rectangular_exact.md`.

The [integrable boundary shear](research/ai/2026-10-21-integrable-boundary-shears/proof.md)
gives an exact two-parameter non-plane family at effective first ranks10,10.
Both source rowspaces move, while the full112-by14-by14 contraction stays
constant with first rank12. For every nonzero parameter pair the moving
14-dimensional spaces are complete mutual annihilators on the fixed
100-dimensional source kernel; exact polynomial chart minors prove this.
The resulting degree-two maps satisfy all-order coefficient equations
with zero source-row corrections. Their generic row ranks are14, so
this family cannot reach the110-dimensional target legs. It establishes
integrability of two additional normal directions, not an improving matrix
limit. Higher-rank completions and the exponent goal remain open; the
construction and completeness proof are written and unreviewed.

## Complete fixed-residual Koszul screening

The [all-leg, all-degree atlas](research/ai/2026-10-23-oblique-koszul-atlas/README.md)
computes 75 exact matrix ranks for the fixed product-oblique residuals at
`b=2,3,4`, using integer unit elimination over every field. At `Q(6,4)`,
the strongest full-space Koszul bound is eleven, below the inherited
equalizer lower bound twelve. Standard full-space Koszul maps therefore
do not narrow the border-rank interval `[12,18]` for these fixed maps.
Arbitrary projections, other flattenings and other maps remain open.
Claim `EXP-OBLIQUE-KOSZUL-ATLAS-001` is a finite exact experiment; no
independent review, optimal border rank or exponent improvement follows.
The construction and equalizer claims retain their original attribution
and pinned pending-PR147 dependency.

The [updated ordinary rectangular frontier](research/ai/2026-10-21-rectangular-ordinary-frontier/proof.md)
applies the already proved polynomial/Hankel gates to every improving
sorted single matrix format for balanced a=2,...,12. Of5139 formats,4192
are excluded and947 survive. All improving ordinary shapes through a7
are closed; its earlier gates retained M(27,28,28) at a8, with
legs756,784,756. Later arguments below close that ordinary candidate.
Its maps are unconstructed. The existing spectral implication would give
omega<=191/85 if that premise were supplied, certified by the recorded
integer comparison; no exponent improvement is established. The earlier
polynomial-rank-locus note already excluded all four A5 ordinary targets;
this scan updates the stale minimum-only research queue and retains that
prior credit. A separate corner-minor note rederives the existing rank
inequality, without claiming a new general theorem or independent review.

The later ordinary single-target saturation scan closes A88 to M(27,28,28).
Across71 source formats through leg dimension1152,1200 potentially improving
shapes first reduced to A89 to M30; the new two-ruling bound now closes
that final ordinary candidate too. The general lemmas remain written
and unreviewed;25740 integer minor witnesses and the finite enumeration were
replayed. This supplies no maps and no improved exponent. See
`research/ai/2026-10-21-rectangular-direct-sums/single_frontier.md`.

The self-contained two-ruling lemma proves that if all two-row and
two-column bilinear image spaces have dimension at most r>=6, the full
image has dimension at most floor(r^2/4). Its r=7 application excludes
ordinary A89 to M30 by900>12*72=864. The proof is written and unreviewed;
finite controls retain an r=5 counterexample and check all equality cases
through r=20. No smaller exponent or general singular exclusion follows.

With the two- and three-ruling gates included, the scan through source leg
dimension1500 leaves only A(8,10) to M(32,33,33), at source dimension1360.
Its required maps are missing. The conditional arithmetic would give about
2.245871, but no smaller exponent is established. The rank-two lift is641,
one above the640 full-symbol threshold; the existing one-step counterexample
prevents rounding away that gap. See `next_ordinary_target.md` in the
rectangular-direct-sums research folder.

## Paired-source variable-coefficient shift rank

The [shift-separation proof](research/ai/2026-10-23-paired-shift-separation/proof.md)
shows that an ordinary restriction of `Q(n,m)` to `M(n,m,n)` still has
residual flattening rank at least `g_B*g_C` when one finite-band long-leg
map has column dependence expressed by profiles with combined shift-matrix
rank below `m`, and the other long-leg map is finite-band Toeplitz. The
first-leg map is arbitrary. For fixed `m` and sublinear bandwidths and
exception counts, this is `n^2-o(n^2)`, so such maps cannot use a
subquadratic auxiliary repair. The claim is written and unreviewed; generic
full shift rank, Laurent cancellations, and the exponent goal remain open.
An exact `F_101` control at `n=9,m=4` has profile ranks `1,2`, residual
rank `81`, and the theorem's lower bound `9`. It is finite verification, not
the all-size proof.

## Continued finite-construction search

The [higher-Hankel proof](research/ai/2026-10-20-hankel-segre/README.md)
excludes ordinary A(5,6) restrictions to M16 plus M4, using higher secant
geometry. Its finite frontier screens all square-sum partitions in 52 source
formats through leg dimension 800. Singular degeneration remains open.

The [unequal paired-source extension](research/ai/2026-10-20-unequal-paired/README.md)
gives all first-leg Koszul ranks under its explicit hypotheses. Its selected
120-dimensional first-leg target would imply an exponent near 2.2495306348
if a degeneration were constructed. **No such construction is supplied.**
The written proofs remain AI-derived and externally unreviewed; no smaller
exponent is established. See the [sprint record](research/ai/2026-10-20-construction-sprint/README.md)
for current questions and verification status.

The unequal-source polynomial now has a universal upper-bound proof outside
its equality range. Applied on the other input leg, it excludes the proposed
`EPR2` tensor `C(25,29)` to `M(7,6,7)` degeneration by an exact positive
Koszul-rank gap. This closes a candidate; it does not lower the exponent.

The [singular shared-map family](research/ai/2026-10-20-singular-shared-normalization/README.md)
passes every transported shared catalecticant test for one copy of the
canonical fat-point target at source length `N=m(m+1)/2`. An explicit
[all-size construction of its projection](research/ai/2026-10-20-singular-shared-normalization/projected_construction.md)
uses polynomial residue levels and has a complete coefficient identity.
Exact replays at `m=4,6,8,10` check 26,694 coefficients. The projection loses
`m/2-1` shared directions; recovering those directions with Laurent maps
remains open. Neither result constructs the full target or improves omega.

The [first and second order lift obstruction](research/ai/2026-10-20-shared-tangent-lift/README.md)
closes the exact `B=N` problem for the displayed simple-pole shared map
and its quadratic ramification, even with arbitrary Laurent orders on the
other legs. A nonzero normal coefficient cannot be cancelled; the second
order correction vanishes by an image-intersection argument. Higher
ramification and additional source space are outside the claim. Current
construction work allows `B=N+O(m)`, which still meets the asymptotic
cost-one premise if full tensor maps can be found.

## Exact fixed-shared packing and broader construction targets

The [alternating-degree construction](research/ai/2026-10-20-alternating-degree-packing/README.md)
works for every size and replication count, at the exact prior fixed-shared
threshold `B=k ceil(3m^2/4)-floor((m-1)/2)`. The earlier finite C(4,11)
witness is credited. The all-size formula has asymptotic ratio 3/2 and
therefore does not improve the exponent. Exact replay covers 120 cases
and 2,995,050 source terms.

An [explicit rational algebra deformation](research/ai/2026-10-20-singular-shared-normalization/curvilinear_krylov.md)
produces the plane fat-point algebra from a curvilinear algebra. The extra
consecutive-moment condition needed for the convolution tensor remains
unconstructed; a small square-dimension obstruction proves that preserving
algebra multiplication is too restrictive to include the known size-three
tensor control. Current work permits two independent nonshared maps.

The [ordinary EPR-convolution frontier](research/ai/2026-10-20-unequal-paired/edge_ordinary.md)
now excludes all 10,418 improving shapes from the stated 2,867-source grid,
using Koszul ranks, minimum slices, polynomial gcds, and product spaces.
Twenty-seven actual restrictions pass exact positive controls. Singular
degenerations are outside the full frontier conclusion.

The [source-aspect extension](research/ai/2026-10-20-construction-sprint/shared_dimension_slack.md)
allows extra shared coordinates: an unbounded cost-one family with shared
ratio at most 21/20 would still imply omega at most 2247/1000. This is a
conditional criterion; no such family or smaller exponent is established.
The new finite question includes dense rectangular shared maps for C(5,10).

The earlier ordinary frontier in the higher-Hankel package is preserved
as a dated relaxation. Main's later boundary theorem excludes its A(7,8)
survivor; the current larger ordinary frontier is described above.

## Rectangular module equations and compressed maps

The [independent-map reformulation](research/ai/2026-10-20-rectangular-module/README.md)
gives an exact row/controllable-pair criterion and an explicit parity factorization
of the fat-point tensor. Its middle rank suggests the source C(m+1,N+m/2-2).
For C(5,10), the missing right-factor condition becomes eight vector syzygies.
No simultaneous solution is supplied. A separate coprime-product argument
excludes only the symmetric one-pole low/high degree split, leaving mixed
leading rows, asymmetric supports, and higher Laurent orders open.
The exact parity replay checks 43,664 coefficients at m=4,6,8,10.

The [compressed packing](research/ai/2026-10-21-compressed-packing/README.md)
fits in C(m,N), with an explicitly retained negative Laurent coefficient.
A singular shared rescaling gives an actual all-even-size degeneration to
a different tensor U_m consisting of the three central fat-point slices and
that error coefficient. Twenty exact cases cover 182,140 source terms per
map family. This does not construct the full fat-point target or prove a
smaller exponent; a useful character estimate for the alternative tensor
has not been established. The new claims remain written and unreviewed.

## Explicit singular matrix multiplication pilot

The [integer Laurent construction](research/ai/2026-10-21-singular-pilots/README.md)
proves C(4,5) degenerates to 2-by-2 matrix multiplication over every field.
All 64 coefficient positions are checked exactly: eight target coefficients
remain at degree zero, every negative-degree coefficient vanishes, and twenty-two
positive-degree remainder terms have degrees one through seven. Two further
same-session source-coefficient replays agree with the displayed witness.
This is a finite constructive result and a pilot for the larger fat-point
search. It does not establish a smaller exponent or an unbounded family.

## Certified rectangular fat-point degeneration

The [rational contraction certificate](research/ai/2026-10-21-rectangular-t4-certificate/README.md)
proves C(5,10) degenerates to the canonical T4 over the real and complex
numbers. Exact rational bounds prove a common zero of all 172 required
coefficient equations inside a radius-10^-8 cube. The fixed-point map
has contraction factor below 0.000553 and image radius below 1.37e-11.
A separate verifier expands all 400 source coefficients and obtains the
selected Jacobian by exact integer finite differences; its bounds agree.

This resolves the finite rectangular target named above and goes beyond
the symmetric degree split that was excluded earlier. The result does
not supply an unbounded family. Larger source-target constructions and
a uniform cost bound remain necessary for the conditional exponent
criterion. No exponent below 9/4 is established. The written proof has
same-session checks and no external mathematical review.

## Rational flags and a broader matched-sector target

The [explicit rational refinement](research/ai/2026-10-21-rectangular-t4-certificate/rational_flag_construction.md)
constructs the finite C(5,10) degeneration to T4 by polynomial flags,
a cofactor pencil, and rational linear solves. A second implementation
expands all 400 source coefficients exactly. This strengthens the earlier
real existence certificate to explicit maps over the rationals; both
certificates are retained. It does not improve the exponent.

An [all-size first-flag formula](research/ai/2026-10-20-rectangular-module/first_flag.md)
constructs all equations involving input degrees zero and one, with exact
controls on 89,739 coefficients. The higher input rows remain unsolved.
The [conditional growth target](research/ai/2026-10-20-construction-sprint/independent_sector_bases.md)
may also use independent invertible shared identifications in its matched
convolution sectors. This preserves the character lower bound and relaxes
the search, but supplies no missing unbounded family.

## Exact five- and six-sector moment constructions

The [self-adjoint moment package](research/ai/2026-10-21-selfadjoint-sectors/README.md)
constructs C(6,20) degenerating to the five matched convolution sectors and
C(7,28) degenerating to the six matched sectors, with a separate invertible
shared basis in each sector. Independent rational substitution checks all
1,125 and 2,646 coefficient positions, including every negative zero and
constant target coefficient. Both nonshared maps have full target rank.
These are finite results; no unbounded family or smaller exponent is proved.

A [scoped ideal bound](research/ai/2026-10-21-selfadjoint-sectors/common_ideal_bound.md)
forces asymptotic source cost at least 3/2 if every strictly lower sector is
placed in one principal isotropic polynomial ideal. The six-sector witness
already uses low monomials outside that ideal. Mixed recursive flags and
other moment mechanisms remain open. Both new claims have written proofs
and same-session exact checks; external mathematical review is outstanding.

## Integer canonical four-sector maps

The [integer moment-flag certificate](research/ai/2026-10-21-canonical-moment-flags/README.md)
gives C(5,10) degenerating to canonical T4 over every field, with all map
entries of absolute value at most six. Independent source expansion checks
all 400 coefficient positions: every negative power vanishes and exactly
twenty target monomials remain. A separate JavaScript expansion agrees.
This strengthens the earlier rational finite certificate; no unbounded
family or smaller exponent follows. Claim `AI-CANONICAL-INTEGER-FLAGS-001`
is written and externally unreviewed.

## Canonical integer flags through seven sectors

The [canonical moment-flag package](research/ai/2026-10-21-canonical-moment-flags/README.md)
now constructs C(6,16) to T5, C(7,24) to T6, and C(8,34) to T7 over every
field, using literal integer maps. The five- and six-sector long source
dimensions decrease from 20 to 16 and from 28 to 24. Independent full-source
expansion checks all 9,659 coefficient positions across T4 through T7;
all negative powers vanish and all constant coefficients match exactly.
The maximum absolute map entries are 6,1,5,2. A recovered m6 index error
was caught and corrected before acceptance. These are finite improvements;
no unbounded family or smaller exponent is established. Claim
`AI-CANONICAL-INTEGER-FLAGS-001` retains written, externally unreviewed status.

## Free five-sector flag at exact long-source cost

The [free isotropic flag](research/ai/2026-10-21-free-isotropic-flags/README.md)
proves a finite complex degeneration C(7,15) to all five matched convolution
sectors, each with its own invertible shared basis. An explicit solution
over F2 has an odd 45-by-45 Jacobian minor in the integral polynomial chart.
The written lifting and algebraic existence argument supplies a complex
point with all required rank and normalization conditions. A separate
verifier expands all 1,125 coefficients of the literal binary maps. Those
binary maps are not presented as characteristic-zero coefficients. The
source shared dimension is seven, so this finite exact long-source cost
does not establish an unbounded family or a smaller exponent. Claim
`AI-FREE-ISOTROPIC-FLAGS-001` is written and externally unreviewed.

## Canonical boundary pair in every size

The [boundary-pair construction](research/ai/2026-10-21-boundary-pair/README.md)
gives C(m+2,m+1) degenerating to C(2,m-1) and C(m-1,2), on disjoint
nonshared legs and one canonical shared m-space, for every m>=3.
All maps are integral and all basis determinants are units, so the result
holds over every field. Independent source expansion for m=3 through 20
checks 50,028 coefficient positions. The construction supplies two sectors;
adding the middle sectors with a useful total source cost remains open.
Claim `AI-BOUNDARY-PAIR-001` has a written all-size proof and same-session
exact controls. It has no external mathematical review or exponent claim.

## Scalar shifted-block cost obstruction

The [shifted moment relation bound](research/ai/2026-10-21-global-moment-flag/scalar_shifted_barrier.md)
forces B>=m(m+1)/2+floor((m-2)^2/4)-2 for scalar shifted input factors
with the specified full negative moment equations and invertible matched
shared Hankel matrices in C(m+1,B). The limiting source cost is therefore
at least 3/2. The proof uses coefficient-dual contraction over any field;
828 finite rank controls and 189 exact sum checks support its ingredients.
Free quotient flags and affine carry rows lie outside these hypotheses.
Claim `AI-SCALAR-SHIFTED-BARRIER-001` is a written, externally unreviewed
obstruction for that class. No exponent below 9/4 is established.

## Affine carry construction and finite-field continuation

The [affine carry flag](research/ai/2026-10-21-affine-carry-flags/README.md)
has an exact six-row first-stage formula in shared dimension m+3 for every
m>=4. Three independent families of polynomial relations bound the product
space by 3m+6. The integer controls check 142,653 relation coefficients for
m=4 through 24. This formula supplies a starting flag; it does not construct
all sectors for arbitrary m. Claim `AI-AFFINE-CARRY-FIRST-FLAG-001` is written
and externally unreviewed.

A complete continuation at m=6 gives C(9,23) to all six matched convolution
sectors over F2. Every shared sector map is invertible, and independent
source expansion checks all 2,646 coefficients. Claim
`AI-AFFINE-CARRY-M6-F2-002` is a finite-field result only. The stored lift
satisfying 540 congruences modulo 2^1025 is recorded separately as experiment
`AI-AFFINE-CARRY-LIFT-003`. No characteristic-zero existence certificate
or exponent consequence is inferred from that finite precision.

## Finite constructions leave explicit endpoint models feasible

The [finite-character closure audit](research/ai/2026-10-21-finite-character-closure/README.md)
shows that all five accepted characteristic-zero flag formats satisfy the
existing endpoint scalar model. An explicit interval of larger profiles
also satisfies every listed scalar rule, including hypothetical copies at
unchanged input cost per copy. The same package gives a
[format ceiling](research/ai/2026-10-21-finite-character-closure/correlated_matrix_ceiling.md)
for arbitrary powers and mixtures followed by direct sums of rectangular
matrix products, including correlated extractions and leg permutations.
Those matrix-extraction bounds cannot exceed the formal source values for
these finite formats. Other tensor comparisons and new constructions remain
outside both conclusions. Claims `AI-FINITE-FLAG-CLOSURE-001` and
`AI-FINITE-MATRIX-EXTRACTION-001` are written and externally unreviewed.
Neither is a lower bound for the matrix multiplication exponent.

## Character ceiling for the compressed alternative

The [compressed-tensor character audit](research/ai/2026-10-21-compressed-packing/character_ceiling.md)
bounds the actual endpoint character of the specific alternative tensor
U_m retained from the compressed Laurent identity. A simultaneous
companion-matrix deformation turns each nested error family into a limit
of a direct sum of dot products; the three central slice ranks supply the
remaining terms. The resulting asymptotic ratio to the source's
symmetrized character is at most 4/7. Exact rational comparisons and an
all-size polynomial bound place this upper estimate below the existing
source lower estimate for every even m>=120.

Thus that particular constant tensor does not provide the missing growth
inequality. Cancellation in the full Laurent identity and different
constant tensors remain open. Claim `AI-COMPRESSED-CHARACTER-002` is written,
externally unreviewed, and restricted to characteristic zero. No smaller
matrix multiplication exponent is established.
