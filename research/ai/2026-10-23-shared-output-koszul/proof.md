# Canonical shared-output candidate: a second-leg rank obstruction

Date: 2026-10-23. Owner-directed Codex work. Written and unreviewed.

## 1. Literal endpoints and theorem

Work over the complex numbers. Let `A` have ordered basis
`a_0,...,a_4`. For `b=2,3,4`, define a block `E_b=Full(5,b)` by

\[
E_b=\sum_{i=0}^{4}\sum_{j=0}^{b-1}
a_i\otimes b_j\otimes c_{i+j}.
\tag{1}
\]

Its ordered dimensions are `(5,b,b+4)`. Define the shared-output block

\[
O=\sum_{j=0}^{3}\sum_{k=0}^{1}
a_{j+k}\otimes b_j\otimes c_k,
\tag{2}
\]

with dimensions `(5,4,2)`. This is the polynomial multiplication tensor
of input lengths `4,2` with its length-five output used as the common first
space. The notation `P_{5,4,2}` specifies the same ordered dimensions.

In a shared-first partial sum, each block has its own disjoint `B_i,C_i`,
and all occurrences of `a_i` in (1) and (2) refer to the same coefficient
basis of `A`. Set

\[
S=10E_4,\qquad T=10E_3+E_2+2O.
\tag{3}
\]

Both have format `(5,40,80)`.

**Theorem.** `T` is not in the complex general-linear orbit closure of `S`.
In particular, no complex tensor degeneration from `S` to `T` exists.

This statement concerns the canonical endpoints (1)--(3). It permits arbitrary
global changes of basis and arbitrary degeneration maps, with no regularity
assumption on the first map. Independent changes of first basis in the separate
target blocks are not part of this checkpoint's conclusion.

## 2. The degree-one flattening on the second leg

For a tensor `U` in `A tensor B tensor C`, define the linear map

\[
K_B(U):C^*\otimes B\longrightarrow A\otimes\Lambda^2B,
\quad
\gamma\otimes v\longmapsto
\sum_{i,j,k} U_{ijk}\gamma(c_k)a_i\otimes(b_j\wedge v).
\tag{4}
\]

For the endpoint dimensions this has 3200 columns and 3900 rows.
Its entries are integer linear combinations of tensor coefficients.
If `g_A,g_B,g_C` are invertible, then

\[
K_B((g_A\otimes g_B\otimes g_C)U)
=(g_A\otimes\Lambda^2g_B)K_B(U)
(g_C^*\otimes g_B^{-1}),
\tag{5}
\]

where `g_C^*` means pullback on linear forms. Thus the rank is invariant
under the full product of the three general linear groups. For any integer
`r`, the condition `rank K_B(U) <= r` is closed: all `(r+1)`-minors vanish.
Consequently, a degeneration from `S` to `T` would require

\[
\operatorname{rank}K_B(T)\le\operatorname{rank}K_B(S).
\tag{6}
\]

This argument applies directly to orbit closure, so singular first limits and
Laurent descriptions do not create an exception.

## 3. Exact block decomposition of the large map

Write `B=direct_sum B_i` and `C=direct_sum C_i`. Then

\[
\Lambda^2B=
\bigoplus_i\Lambda^2B_i\ \oplus\!
\bigoplus_{i<j}(B_i\otimes B_j).
\tag{7}
\]

Under (7), each intrinsic domain summand `C_i^* tensor B_i` maps only to
`A tensor wedge^2 B_i`. For each unordered pair `i<j`, the two domain
summands

\[
(C_i^*\otimes B_j)\oplus(C_j^*\otimes B_i)
\tag{8}
\]

map only to `A tensor B_i tensor B_j`. These domain groups are disjoint
and exhaust `C^* tensor B`. Therefore `K_B` is a direct sum of the intrinsic
and pair maps, and its rank is the sum of their ranks.

In the coefficient bases, the intrinsic map is exactly (4) for one block.
The pair map for blocks `U_i,U_j` is

\[
(\gamma\otimes v,\delta\otimes u)\longmapsto
U_i(\gamma)\otimes v-U_j(\delta)\otimes u,
\tag{9}
\]

where the second term is reordered into `A tensor B_i tensor B_j`.
The minus sign is the exterior sign for `B_j wedge B_i`.

Let `R_i` be the image of the concise coefficient map
`C_i^* -> A tensor B_i`. Equivalently, the pair rank is

\[
(\dim C_i)(\dim B_j)+(\dim C_j)(\dim B_i)
-\dim\big((R_i\otimes B_j)\cap(B_i\otimes R_j)\big),
\tag{10}
\]

with the natural reordering of factors. Formula (10) explains the pair kernels;
the accepted certificate uses the literal matrix (9).

## 4. Small exact matrices and the rank gap

The following table gives all ten matrices needed for (3). Every reported rank
has a nonzero integer minor and enough independent exact kernel vectors to prove
the matching upper bound. `certificate.json` contains the witnesses, and
`verify.py` reconstructs every matrix from (1), (2), (4), and (9).

| Matrix | Rows | Columns | Rank | Kernel dimension | Witness determinant |
| --- | ---: | ---: | ---: | ---: | ---: |
| Intrinsic `E4` | 30 | 32 | 21 | 11 | 1 |
| Intrinsic `E3` | 15 | 21 | 12 | 9 | -1 |
| Intrinsic `E2` | 5 | 12 | 5 | 7 | 1 |
| Intrinsic `O` | 30 | 8 | 8 | 0 | 1 |
| Pair `E4/E4` | 80 | 64 | 53 | 11 | 1 |
| Pair `E3/E3` | 45 | 42 | 33 | 9 | -1 |
| Pair `E3/E2` | 30 | 32 | 24 | 8 | -1 |
| Pair `E3/O` | 60 | 34 | 34 | 0 | -1 |
| Pair `E2/O` | 40 | 28 | 27 | 1 | 1 |
| Pair `O/O` | 80 | 16 | 16 | 0 | 1 |

The source has ten intrinsic `E4` maps and 45 unordered `E4/E4` pairs:

\[
\operatorname{rank}K_B(S)=10(21)+45(53)=2595.
\tag{11}
\]

The target's intrinsic rank is `10(12)+5+2(8)=141`. It has 45 `E3/E3`
pairs, ten `E3/E2` pairs, twenty `E3/O` pairs, two `E2/O` pairs, and one
`O/O` pair. Hence

\[
\begin{aligned}
\operatorname{rank}K_B(T)
&=141+45(33)+10(24)+20(34)+2(27)+16\\
&=2616>2595.
\end{aligned}
\tag{12}
\]

Equations (6), (11), and (12) prove the theorem.

The certificates are exact finite linear-algebra proofs of these particular
ranks. Their acceptance does not use the prior closed convolution Koszul
formulas or any randomized or floating-point rank test. Four separate controls
build unsplit two-block Koszul matrices and compare their ranks with the
decomposition, checking the literal exterior signs and block accounting.

## 5. Why the candidate was worth testing

The preserved discovery record uses the symmetric formal operational score

\[
G(a,b)=\left(\frac{3\min(a,b)-1}{2}\right)^{1/3}
\left(\max(a,b)+\frac{\min(a,b)-1}{2}\right)
\tag{13}
\]

on each polynomial block, then adds block scores. This is the symmetric
specialization of the formal potential described in AVZ26 and the preceding
common-input package; it is not an asserted character on all tensors.
For an `O` block the polynomial input lengths are `4,2`.

For (3), the two sums are

\[
G(S)=65\sqrt[3]{11/2},\qquad
G(T)=60\sqrt[3]{4}+\frac{29}{2}\sqrt[3]{5/2}.
\tag{14}
\]

The increase is strict by a short rational certificate. Multiply both sides
of (14) by the positive number `2^(4/3)`. The source becomes
`130*cuberoot(11)`, while the target becomes `240+29*cuberoot(5)`.
Since

\[
5-(17/10)^3=87/1000>0,
\]

the scaled target is greater than `2893/10`. Moreover,

\[
(2893/10)^3-130^3\,11=45815957/1000>0.
\tag{15}
\]

Thus the score increases even though the actual degeneration is impossible.
The candidate also passed shared-first-leg Koszul screening, all symmetric-power
degrees, and ambient quantum-functional bounds; those prior screens and their
scope are recorded as discovery context, not premises of the obstruction.

The mixed shared-output orientation lies outside the Full/Mid common-input
theorem. The present rejection supplies a separate concrete obstruction. It
does not prove an exclusion for every mixed-orientation packing, and it does
not establish an improved exponent.

## 6. Provenance and evidence status

The research-frontier agent discovered the candidate by optimization and
independently computed the same ten rank values in the same session. The
audit agent developed the second-leg decomposition and the exported literal
minor/kernel certificate. Both worked under the repository owner's direction.
Koszul flattenings and closed determinantal rank conditions are classical;
their earlier repository use and AVZ26's formal score retain their attribution.
No historical priority, independent mathematical review, or formalization is
claimed. The repository's complete regression and replay remain integration
gates handled separately from the focused controls here.
