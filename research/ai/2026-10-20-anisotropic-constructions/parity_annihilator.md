# Pairwise annihilators exclude the proposed parity target

October 21, 2026. AI-derived written proof, checked by two other agents in
the same generating session. No external independent review or
formalization is claimed. This is a degeneration obstruction, not an
improvement of the matrix multiplication exponent.

## Result

Let S be the `parity110` source defined in [singular_support.md](singular_support.md).
On every retained term exactly one coordinate has shifted parity zero.
The shifted odd coordinate dimensions are

\[
(o_X,o_Y,o_Z)=(113,113,112).
\]

If S degenerates to a direct sum of square matrix multiplication tensors,
with total leg dimension D, then

\[
\boxed{\sum_{i=X,Y,Z}\max(0,D-o_i)\le D.}                 \tag{1}
\]

In particular D is at most 169. This excludes both M14 and the previously
proposed M14 direct sum M4. The latter has D=212. It excludes all
degenerations to those targets, including arbitrary linear mixing and
singular parameter-dependent maps. The sharp asymptotic slice-rank
capacity in [parity_balancing.md](parity_balancing.md) remains correct;
passing that different necessary condition did not establish existence.

The boundary single target M13 is excluded as well, by the strict
refinement below. This note does not exclude a general asymptotic
conversion between powers, or the analogous targets from the full A(5,5)
source before taking the parity degeneration.

## 1. A closed condition inherited from the source

Write V_i=V_i^0 direct sum V_i^1 for the two shifted parity spaces.
The source has no term with two even coordinates. Hence its trilinear
form vanishes whenever any two dual inputs belong to (V_i^0)^*.

Consider any restriction into target spaces W_i of dimensions D_i.
Let L_i:W_i^* -> V_i^* be the pullback maps, and let pi_i be projection
onto (V_i^1)^*. Define

\[
E_i=\ker(\pi_i L_i).
\]

Then dim E_i is at least max(0,D_i-o_i). Every pair E_i,E_j annihilates
the restricted tensor, regardless of the input in the third space.
This dimension argument does not require the L_i to be injective.

This property is closed under degeneration. To see this, put
k_i=max(0,D_i-o_i) and choose a k_i-dimensional subspace of each E_i.
In the product of the three Grassmannians and the target tensor space,
the conditions

\[
T(E_X,E_Y,W_Z^*)=T(E_X,W_Y^*,E_Z)=T(W_X^*,E_Y,E_Z)=0        \tag{2}
\]

define a closed incidence variety: they are vanishing conditions for
the corresponding universal multilinear maps. The Grassmannians are
projective. Projection to the tensor space is therefore closed. Every
restriction lies in this image, so its Zariski closure does too. In
particular an algebraic degeneration also has subspaces of dimensions
k_i satisfying (2). This is the same projective-incidence mechanism as
the standard proof of closedness of bounded slice rank; see Tao--Sawin,
Corollary 2, cited below.

## 2. Pairwise-annihilating matrix spaces

First take one target M(a,b,c), with matrix spaces

\[
X=\operatorname{Hom}(\mathbb C^b,\mathbb C^a),\quad
Y=\operatorname{Hom}(\mathbb C^c,\mathbb C^b),\quad
Z=\operatorname{Hom}(\mathbb C^a,\mathbb C^c),
\]

and trilinear form tr(XYZ). The relevant trace pairings are nondegenerate.
Thus (2) says

\[
E_X E_Y=E_Y E_Z=E_Z E_X=0.                               \tag{3}
\]

Let I_X be the span of all images of matrices in E_X, and define I_Y,I_Z
likewise. Put r_X=dim I_X, r_Y=dim I_Y, r_Z=dim I_Z. Every matrix in E_X
annihilates I_Y and has image in I_X. Consequently

\[
\begin{aligned}
\dim E_X&\le r_X(b-r_Y),\\
\dim E_Y&\le r_Y(c-r_Z),\\
\dim E_Z&\le r_Z(a-r_X).
\end{aligned}                                           \tag{4}
\]

The sum on the right is a multiaffine function on
[0,a] times [0,b] times [0,c]. Its maximum occurs at a corner: optimizing
one variable at a time preserves a maximizer and moves it to an endpoint.
The eight corner values are zero or one of ab,bc,ca. Therefore

\[
\dim E_X+\dim E_Y+\dim E_Z\le\max(ab,bc,ca).             \tag{5}
\]

For a direct sum of matrix tensors, project each E_i to each block.
The projections still satisfy (3) block by block: any chosen element in
each projected space has a lift to its original E_i, so the original
pairwise vanishing applies to their product. The dimension of a space is
at most the sum of the dimensions of its coordinate projections. Summing
(5) over blocks consequently gives

\[
\sum_i\dim E_i\le\sum_j\max(a_jb_j,b_jc_j,c_ja_j).       \tag{6}
\]

When the blocks are square, the right side equals the common target leg
dimension D. Combining this with Section 1 proves (1).

## 3. Rectangular targets and exact numerical consequences

Let D_X=sum_j a_jb_j, D_Y=sum_j b_jc_j and D_Z=sum_j c_ja_j.
The general necessary condition is

\[
\sum_i\max(0,D_i-o_i)
\le\sum_j\max(a_jb_j,b_jc_j,c_ja_j).                     \tag{7}
\]

A convenient weaker consequence is that the sum, over target blocks,
of their two smaller leg dimensions is at most o_X+o_Y+o_Z=338.
Indeed max(0,D_i-o_i) is at least D_i-o_i. This rectangular extension
was supplied and checked by the structure worker in this same session.

For the proposed square target, the left side of (1) is

\[
(212-113)+(212-113)+(212-112)=298>212.
\]

For D>113, (1) is 3D-338<=D, giving D<=169. Values D<=113 already satisfy
that conclusion. The smaller parity controls in the source note remain
valid; the excluded large target is not inferred from those controls.

There is a useful strict refinement for a single square block. Put
a=b=c=n. The deficit in the multiaffine estimate factors as

\[
n\left[n^2-\sum_i r_i(n-r_{i+1})\right]
=(n-r_X)(n-r_Y)(n-r_Z)+r_Xr_Yr_Z.                       \tag{8}
\]

Equality requires at least one r_i=0 and at least one r_j=n. In
particular, if all three E_i are nonzero then every r_i>0 and (5) is
strict. For M13, D=169 forces dim E_X>=56, dim E_Y>=56, dim E_Z>=57.
Their sum is at least169, contradicting strictness. The same argument
excludes the previously searched parity A(2,2) to M3 target: each
o_i=6 and each annihilator has dimension at least3. This refinement was
identified by the balancing worker in the same session.

Strictness must not be transferred to every block of a direct sum:
a projected annihilator can be zero in a particular block. The proof
of (7) uses only the non-strict inequality and remains valid.

## 4. Reproduction and research consequence

`parity_annihilator.py` checks the multiaffine corner formula, the exact
deficit identity, the parity counts, absence of terms with two shifted
even coordinates, and the stated target inequalities. It records both
excluded targets and valid controls. These finite checks validate the
implementation; Sections 1--3 are the universal written argument.

The no-two-even hypothesis is essential. Full A(5,5) also has the
discarded all-even sector and does not satisfy it. The proposed full-source
M14 direct sum M3 target is therefore not excluded by this theorem.
Tensor products have a different multilevel grading and are not covered
by simply substituting powers into the one-copy bound.

The exact entropy certificates remain support information, while the
annihilator argument rules out the specific matrix-algebra targets.
Numerical searches for the excluded targets were stopped when the proof
was found. Their saved unsuccessful runs remain experiments and are
not evidence for the universal obstruction.

## Source and attribution

Terence Tao and Will Sawin, [Notes on the slice rank of tensors](https://terrytao.wordpress.com/2016/08/24/notes-on-the-slice-rank-of-tensors/),
August 24, 2016, Corollary 2: projective-incidence proof of closedness.
The present pairwise-annihilator property and matrix-space dimension
calculation are derived here. No historical priority claim is made.

The root agent supplied the square obstruction and closure argument.
The two parity workers checked it in this generating session, supplied
the rectangular and strict refinements above, and did not find a flaw.
This is not external independent mathematical review.
