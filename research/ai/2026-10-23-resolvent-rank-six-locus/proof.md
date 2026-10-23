# The complete rank-six locus and sharp compression loss

Claim `AI-RESOLVENT-RANK-SIX-LOCUS-001` is written and unreviewed.
All ranks here are ordinary matrix ranks. Sections 1-3 hold over every
field. Section 4 assumes an algebraically closed field, including C.
No matrix-multiplication exponent improvement follows.

## 1. Source and outer coordinates

Use the source and fixed limiting space of
[the predecessor proof](../2026-10-23-resolvent-minrank/proof.md).
Its exact revision and bytes are recorded in `sources.json`.
For indices i,s,j,r in {0,1,2,3} and H,L in {0,...,6}, put

\[
 S(f)_{(j,L),(H,r)}=f_{H-j,L-r},\qquad
 K=S(f_*),\qquad f_*[i,s]=\mathbf1_{i+s=3}.
\]

Unavailable short indices mean zero. Rows and columns have lexicographic
order. The integer matrix K has an integer inverse. Define

\[
 G(f)=K^{-1}S(f),\quad Q(f)=G(e_{00})G(f),\quad
 T(f)=KQ(f)=S(e_{00})K^{-1}S(f).
\]

The mixed outer space after multiplication by K is

\[
 \mathcal Y=\{S(g)+T(f):f,g\in\mathbb F^{16}\}.
\]

Since T(f_*)=S(e00), fix the gauge f03=0. The ordered 31 generators
are the 16 matrices S(eis), then the 15 matrices T(eis) with (i,s) != (0,3).
The predecessor proves their independence and minimum nonzero rank six.
The certificates below also re-establish both facts for this mixed space.

Define

\[
 D=-S(e_{10})+T(e_{13})+T(e_{22})+T(e_{31}),
 \qquad
 V=\operatorname{span}\{T(e_{00}),T(e_{10}),T(e_{20}),T(e_{30}),D\}.
\]

Let E0 be the coordinate six-space in the outer output with zero-based
row indices {0,7,14,21,22,23}, and let E=K^{-1}E0.

**Theorem 1.** The rank-at-most-six locus in Y is exactly V.
It has dimension five. Every nonzero member has rank six and image E0.
Equivalently, the rank-at-most-six locus in {G(g)+Q(f)} is K^{-1}V,
and every nonzero member has image E.

## 2. Complete integer certificate

The certificate contains 26 successive seven-by-seven minors in the
31-parameter gauge-fixed space. At each stage, the indicated submatrix
is lower triangular, with diagonal entries equal to a linear form ell
or its negative. Thus its determinant is plus or minus ell^7.
One coefficient of ell is a unit, 1 or -1.

For a rank-at-most-six matrix every such determinant vanishes. Over a
field this forces ell=0. The specified unit substitution eliminates one
parameter. The next minor is an identity on the entire resulting space,
not a specialization at sampled parameters. After all 26 substitutions,
the five remaining coefficient matrices are exactly the displayed basis
of V, in that order. This proves necessity.

Every entry of these five matrices outside E0 is zero. Therefore all
their linear combinations have rank at most six, proving sufficiency.
Five further triangular six-by-six minors eliminate all five remaining
parameters under the assumption of rank at most five. Consequently the
five generators are independent and every nonzero combination has rank
six. Its image, being contained in and of the same dimension as E0,
equals E0. The same argument, preceded by the 26 eliminations, proves
independence of the full 31-generator mixed space.

The acceptance program reconstructs S, K and T from the formula, verifies
both integer inverse identities, and checks every diagonal, upper-zero
entry, unit substitution and final basis coefficient. It verifies the
six-row support and all five terminal minors. It imports neither the
discovery program nor the predecessor verifier. Since only unit pivots
and polynomial identities over Z are used, the conclusion holds over
every field, including characteristics two and three.

The certificate is
[`certificate.json`](../../../results/resolvent-rank-six-locus-2026-10-23/certificate.json).
Its accompanying hash and exact report are in `manifest.json`.

One useful consequence is

\[
 \{Q(f):\operatorname{rank}Q(f)\le6\}
 =\operatorname{span}\{Q(e_{i0}):0\le i\le3\}.
 \tag{1}
\]

To see this without a dimension guess, put Q(f) into the gauge above.
Its g-coordinate is f03 e00, and its f-coordinate is f-f03 f_*.
In the five-dimensional terminal space the only possible nonzero
g-coordinate is -d e10, from the coefficient d of D.
Uniqueness of the gauge-fixed coordinates forces f03=d=0.
The remaining f-coordinates are precisely those with s=0. Conversely
these four matrices already lie in the rank-six space.

## 3. The entire 112-dimensional limit space

Order the middle coordinate first, giving four outer blocks of size 28.
The predecessor's space W consists of the matrices

\[
 \lambda I_{112}+J_2\otimes G(g_2)+J_1\otimes G(g_1)
 +E_{30}\otimes(G(g_0)+Q(f_3))
 +\sum_{j=1}^3E_{3j}\otimes Q(f_{j+3}),
\]

where J2 has ones at (1,0),(2,1),(3,2), and J1 has ones at (2,0),(3,1).
The mixed block uses the gauge already fixed.

**Theorem 2.** The rank-at-most-six locus of W is the 17-dimensional
linear subspace

\[
 Z=E_{30}\otimes K^{-1}V
   +\sum_{j=1}^3 E_{3j}\otimes
       \operatorname{span}\{Q(e_{i0}):0\le i\le3\}.
\]

Every nonzero X in Z has rank six and the same image
Ehat={e3} tensor E, a fixed six-space in the 112-dimensional output.
Here {e3} tensor E denotes the final middle-coordinate layer with outer
coordinate in E.

Indeed, a nonzero lambda gives an invertible 28-by-28 block at (0,0).
With lambda=0, a nonzero g2 or g1 gives a block with rank at least 16,
by the predecessor's outer-source minimum-rank lemma. Thus all three
vanish for rank at most six. Theorem 1 and (1) classify the remaining
four blocks separately. Their images all lie in E; concatenating them
therefore has rank at most six. Any nonzero block has rank six, so every
nonzero concatenation has exactly that rank and image. The independent
blocks give dimension 5+4+4+4=17.

## 4. Sharp corank-three compression theorem

Let P and C be linear maps on the output and input sides of W,
respectively, both of rank 109. Their ambient source output and input
spaces have dimension 112. The external dimensions of P and C do not
matter; they can in particular be 110-by-112 and 112-by-110 as in the
previous application. Write L=ker P and U=im C, so dim L=3 and dim U=109.

**Theorem 3.** Over an algebraically closed field,

\[
 \dim\{X\in W:PXC=0\}\le1,\qquad \dim PWC\ge111.
\]

If this kernel is nonzero, L is contained in the specific six-space Ehat.
For any nonzero kernel element X, one has
U=X^{-1}(L), ker X contained in U, and X(U)=L.
These alignment conditions and the bound are sharp.

The rank-loss inequality gives rank X <=3+3=6 for every kernel element.
Theorem 2 identifies all nonzero such X as rank-six maps onto Ehat.
Also rank X|U >=6-3=3, while X(U) is contained in L. Hence X(U)=L,
L is contained in Ehat, and the kernel dimension calculation gives the
stated alignment.

Let H be the compression kernel. Quotienting input by U and output by L
defines a linear map

\[
 H\longrightarrow\operatorname{Hom}(\mathbb F^{112}/U,\widehat E/L).
\]

Both spaces on the right have dimension three. Every nonzero X induces
an invertible map: its image before quotienting is Ehat, and its induced
rank is 6-3=3. In particular this linear map on H is injective.
If dim H were at least two, two linearly independent induced matrices A,B
would yield a root of the degree-three polynomial det(A+tB) over the
algebraically closed field. The corresponding nonzero member of H would
induce a singular map, a contradiction. This proves the bound.

The rank-locus classification over every field is stronger in field
scope than this last determinant-pencil argument. No one-dimensional
compression-kernel bound over arbitrary fields is claimed. The same
evaluation-at-a-nonzero-vector argument gives dim H <=3 over any field,
but that observation is not needed for the complex application.

For an explicit sharp example, change output coordinates by I4 tensor K.
Delete output rows 105,106,107, and input columns 31,35,39, all zero-based.
These define rank109 maps on both sides. The nonzero X with sole block
(3,1)=Q(e00) is killed. In transformed coordinates, its six nonzero
rows are 84+{0,7,14,21,22,23}. Its first three rows are supported only
at columns 28+{3,7,11}, while its last three rows are deleted.
Thus the kernel is nonzero, and Theorem 3 makes it one-dimensional.
Padding P and C with a zero row and column gives the 110-dimensional
external shapes if desired. The verifier also reconstructs all 112
source-space generators and computes the compressed dimension 111
directly over Q, without using the determinant-pencil theorem.

## 5. Consequence and remaining limits

The prior alignment condition placed L in a 28-dimensional layer.
It now places L in a fixed six-space, and even an aligned compression
can lose at most one source-space dimension over C. The exact loss
example shows that universal injectivity at ranks109/109 would be false.

This closes the fixed W rank-six classification question. It does not
classify different nilpotents, higher resolvent corrections, or general
singular Laurent trajectories. A matrix-target conclusion for a larger
trajectory class still requires the full limiting-space argument for
that class. These written proofs and finite certificates supply no
smaller exponent, independent mathematical review, or formalization.
