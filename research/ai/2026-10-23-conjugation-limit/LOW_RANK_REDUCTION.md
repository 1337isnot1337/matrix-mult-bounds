# Reducing arbitrary constant compressions to a 46-dimensional outer space

October 23, 2026. Claim `AI-A4-TWOSIDED-LOWRANK-003`. Written and unreviewed. This is a necessary
reduction within the fixed two-sided conjugation family. The remaining
compression inequality is not proved, and no full target is constructed.

The source conventions, full saturated limit L, and rank-loss requirement
are those in [proof.md](proof.md), claim `AI-A4-TWOSIDED-RANKLOSS-001`.
Exact prior source versions are pinned in [sources.json](sources.json).
Write G for the 16-dimensional outer source space and F=G00.
All spaces and maps in this note are over the complex numbers.

## 1. Exact block form

The complete 112-dimensional saturated limit consists exactly of

\[
X=\begin{pmatrix}
D&0&0&0\\
B+TF&D&0&0\\
C+VF&B&D&0\\
A+QF-FQ+FRF&C-FV&B-FT&D
\end{pmatrix},\qquad D=\alpha I+\beta F,                 \tag{1}
\]

where A,B,C,T,V,Q,R belong to G. Blocks have size 28.
One can restrict Q to the 14 source generators other than G00 and G03.
Indeed, F commutes with itself and the source unit
I=G03+G12+G21+G30 commutes with F.

The exact certificate uses the two diagonal generators and the seven
groups of block generators in (1): 16 each for B,T,C,V,A,R and 14 for Q.
It expresses each of the already certified 112 independent leading
matrices as a rational linear combination of these 112 generators.
Acceptance reconstructs and compares every entry of all 112 identities.
Thus the displayed generators span L and are independent.

In particular the bottom-left block space is

\[
\mathcal E=G+[G,F]+FGF\subseteq\operatorname{Mat}_{28},
\qquad\dim\mathcal E=16+14+16=46.                       \tag{2}
\]

The [acceptance program](block_reduction.py) replays the
[block certificate](../../../results/conjugation-limit-2026-10-23/block-certificate.json).
The [accepted report](../../../results/conjugation-limit-2026-10-23/block-verification.json)
records the complete coverage. The certificate pins the parent
saturated-limit certificate by SHA-256.

## 2. Credited minimum-rank inputs and the right-sided counterpart

The ordinary minimum nonzero rank of G is 16. This is the maintained
source minimum-rank theorem, also replayed in Section 3 of
[resolvent minimum-rank proof](../2026-10-23-resolvent-minrank/proof.md).

Section 2 of that same proof, claim `AI-RESOLVENT-SHARP-MINRANK-001`,
proves that every nonzero matrix in G+FG has ordinary rank at least six.
Its 31 successive triangular 6-minor identities are retained in
[its certificate](../../../results/resolvent-minrank-2026-10-23/certificate.json)
and accepted by [its verifier](../2026-10-23-resolvent-minrank/verify.py).
The argument works over every field; only its complex-field consequence
is needed here. This note imports that theorem with its existing credit.

The space G+GF has the same minimum-rank bound. Here is the exact
transpose-conjugation that transfers it. Let R0 permute the outer row
coordinates (j,L) to (L,j), and set

\[
B(f)=R_0S(f),\qquad \Omega=R_0K=B(f_*).
\]

Both row and column indices of B(f) now have the form (H,r), with
H=0,...,6 and r=0,...,3. Its entries are

\[
B(f)_{(L,j),(H,r)}=f_{H-j,L-r}.
\]

If f^tau is the transposed coefficient array, then
B(f)^T=B(f^tau). The source unit f* is symmetric, so Omega is symmetric
and invertible. Since G(f)=Omega^-1 B(f),

\[
G(f)^T=\Omega G(f^\tau)\Omega^{-1},\qquad
F^T=\Omega F\Omega^{-1}.                                  \tag{3}
\]

Consequently

\[
(G(a)+G(b)F)^T
=\Omega\bigl(G(a^\tau)+FG(b^\tau)\bigr)\Omega^{-1}.         \tag{4}
\]

Transpose and conjugation preserve ordinary rank. Equations (3)-(4)
therefore transfer the minimum-rank-six theorem to G+GF. The block
acceptance program reconstructs Omega, checks its symmetry and exact
integer inverse, and checks (3) on all 16 literal source generators.
No modular inference about rank upper bounds or vanishing is used.

## 3. Rank at most four forces a single outer block

Suppose X in L has ordinary rank at most four. Each individual block
of X also has rank at most four.

The diagonal block D lies in G, so the rank-16 source bound forces D=0.
The block (2,1) is B in G, so B=0. With B zero, blocks (1,0) and (3,2)
are TF and -FT. They lie in G+GF and G+FG, respectively, so the
minimum-rank-six bounds force both blocks to vanish. Blocks (2,0) and
(3,1) are C+VF and C-FV, and the same two bounds force both to vanish.

Thus every rank-at-most-four element of L is supported in block (3,0):

\[
X=J_3 E Q_0,\qquad E\in\mathcal E,                        \tag{5}
\]

where J3 includes the last 28 output coordinates and Q0 projects onto
the first 28 input coordinates. Conversely every such bottom-left
matrix belongs to L, although its rank need not be at most four.

## 4. The remaining constant-compression problem

Let P have size 110 by 112 and C0 have size 112 by 110, both of rank
110. Their kernels/cokernels have dimension two. The elementary bound

\[
\operatorname{rank}(PXC_0)\ge\operatorname{rank}X-4
\]

shows that every element killed by this compression has rank at most
four. By (5), its support is in block (3,0). Set

\[
\bar P=PJ_3,\qquad \bar C=Q_0C_0.
\]

Both induced maps have rank at least 26: restriction of P to a
28-dimensional subspace can lose at most its two-dimensional kernel,
and the image of the codimension-two space im(C0) under the surjection
Q0 has codimension at most two.

The full compression kernel is therefore identified exactly with

\[
\ker(L\longrightarrow PLC_0)
\simeq\{E\in\mathcal E:\bar P E\bar C=0\}
=\{E\in\mathcal E:E(U)\subseteq W\},                      \tag{6}
\]

where U=im(bar C) has dimension at least 26 and W=ker(bar P) has
dimension at most two. This equality includes both directions, because
every embedded E from (2) belongs to L.

The previously proved rank-loss condition for a full M(10,10,11)
target is dim ker(L -> PLC0) >= 9. Thus a necessary condition is

\[
\exists U,W:\quad \dim U\ge26,\quad\dim W\le2,\quad
\dim\{E\in\mathcal E:E(U)\subseteq W\}\ge9.               \tag{7}
\]

One may reduce to dim U=26 and dim W=2: shrink U and enlarge W,
which can only enlarge the space in (7). Equivalently, there must be
full-rank matrices Phat of size 26 by 28 and Chat of size 28 by 26 with

\[
\boxed{\dim(\widehat P\mathcal E\widehat C)\le37.}          \tag{8}
\]

The number 37 is 46-9. A universal lower bound of 38 in (8) would exclude
every constant compression of this fixed conjugation family. That bound
has not been proved. A pair satisfying (8) would pass only this necessary
test; its true compressed saturated limit would still have to contain
all 100 target slices with a complete matrix-unit tensor certificate.

The finite acceptance checks the full block form, dimension 46, and the
transpose-conjugation identities. The minimum-rank-six result is a pinned
prior theorem, and Sections 3-4 are the mathematical deduction from those
inputs. This remains a written, unreviewed result with same-session
checking, not independent mathematical review or formalization.
