# Structural reductions for the asymmetric twelve-by-eight boundary

Written, unreviewed, owner-directed Codex work, October 23, 2026.
All statements use the credited canonical A4 source and predecessor
normal conventions. No independent review, formalization, full target
construction, all-order exclusion of the asymmetric case, or improvement
below the external exponent 9/4 is claimed.

## 1. Statement and inherited model

Let delta range over the complete 228-dimensional normal parameter space
of the moving-boundary package. Its boundary obstruction maps are

    Psi_B, Psi_C: C^228 -> Mat_(200 by 12)(C).

Their twelve columns use the predecessor's ordered boundary quotient
basis, consisting of six consecutive auxiliary pairs. Assume that the
first boundary span on B is the full twelve-dimensional quotient and
the span F_C on C has dimension eight. The necessary off-diagonal
equations are

    Psi_B(delta)=0,      Psi_C(delta) F_C=0.                 (1)

The complete ker(Psi_B) has dimension 100. Its subspace on which both
maps vanish is the prior complete 28-dimensional boundary-compatible
normal family. The conditioned minimum-rank-four theorem is imported
from the biform third-core package, with its exact certificate and
original credit: a nonzero Psi_C on ker(Psi_B) has rank at least four.

This package proves two reductions.

* If Psi_C(delta) is nonzero and (1) holds, it has rank four and
  F_C=H tensor C^2 for a uniquely determined four-plane H in C^6.
* If both obstruction maps vanish and the predecessor's required
  projected third first-rank is at most two, delta is a common-plane
  direction. Every non-plane delta in this 28-dimensional family has
  projected third first-rank at least four under every C-side quotient
  losing at most four dimensions and no B-side quotient.

The second assertion is a normal-system statement using the inherited
third-rank condition. The first assertion is necessary off-diagonal
compatibility only. In particular the nonzero rank-four branch is not
excluded, and its example below is not a target or a third-compatible jet.
The exchanged statements follow by swapping the two source legs and
using the column-support certificate.

## 2. A universal auxiliary splitting of the conditioned obstruction

Let K be the exported 228-by100 basis of ker(Psi_B), and write delta=Kp.
The exact source coefficients give a constant matrix J of size 200-by84
and a matrix M(p) of size 42-by6, linear in p, such that

    Psi_C(Kp) = J (M(p) tensor I_2).                       (2)

The report exports K, J and all 252-by100 coefficients of M in column
order. J has full column rank 84. The verifier reconstructs the original
normal system and checks every coefficient of (2); the focused test also
checks (2) on each of the 100 parameter basis vectors. Since both sides
are linear in p, these are identities on all C^100. No parameter value
is inverted or omitted. Only constant rational matrices are inverted.

Consequently

    rank Psi_C(Kp) = 2 rank M(p),
    ker Psi_C(Kp) = ker M(p) tensor C^2.                   (3)

The coefficient map of M has rank 72, so its zero kernel has dimension
28, in agreement with the complete preceding joint-zero family.

If (1) holds, rank Psi_C<=4. In the nonzero case the credited minimum
four forces equality; M then has rank two. Its kernel H has dimension
four, so ker Psi_C has dimension eight. Containment of F_C in that
kernel is therefore equality, proving the first reduction. This replaces
an arbitrary point of Gr(8,12) by a point of Gr(4,6) in this branch.

The sharp control p=e0 has rank M=2 and rank Psi_C=4. The report exports
the eight-dimensional product kernel and checks (1). Its nonzero
obstruction keeps it outside the prior 28-dimensional family. This
control shows that off-diagonal compatibility alone does not close the
remaining branch. No claim about its third coefficient is made.

## 3. The actual core has joint row and column support at least three

For delta in the complete 28-dimensional joint-zero family, adopt the
predecessor's core K_delta of dimensions 4-by6-by6. Its first-slice span
is Z_delta, and the full third first-slice space is

    Mat_2 tensor Z_delta.                                (4)

The credited biform proof shows that a non-plane delta has
dim Z_delta>=2 and no nonzero rank-one matrix in Z_delta. This package
adds the stronger support fact

    dim Row(Z_delta)>=3,      dim Col(Z_delta)>=3          (5)

for every non-plane delta. Both bounds are sharp.

Here is a complete polynomial certificate for the row assertion. Stack
the four core slices to a 24-by6 matrix L(delta); its rank is the joint
row-support dimension. Rank at most two forces all cubic minors to vanish.
Eight selected triangular minors equal nonzero rational multiples of
eight independent cubes of linear forms. Their vanishing reduces the
28 parameters to 20. Four further such identities impose four independent
linear equations and reduce to 16 parameters. The full kernel bases and
all twelve determinant identities are exported and independently replayed.

On the remaining 16-dimensional space the coefficient image of L has
dimension 12. An explicit surjective linear map R:C^16 -> C^12 and an
injective coefficient basis B give L(p)=L_B(Rp), checked coefficientwise.
Write x=Rp. There are exactly binomial(14,3)=364 degree-three monomials
in twelve variables. The report selects 364 cubic minors of L_B(x) whose
coefficient matrix in all those monomials has determinant nonzero modulo
32003 (the saved value is 32002). The coefficients are integers, so this
proves its determinant is nonzero over Q and over C. All cubic monomials
therefore lie in the Q-linear span of these actual minors. If the minors
vanish, each x_i^3=0 and hence x=0 over C. Thus L(p)=0.

The preceding source proof identifies the zero core with precisely the
four common-plane directions. It follows that a non-plane delta cannot
have joint row support at most two. Apply the same procedure to the four
transposed core slices for the column assertion. The two certificates
are generated and checked separately. Each has the same 28 ->20 ->16
reduction and a nonzero 364-by364 coefficient determinant. A saved original
parameter with support rank three witnesses sharpness on each side.

The coefficient determinant is a characteristic-zero lower-rank proof,
not an extrapolation from parameter samples. No Groebner-basis computation
or numerical rank decision is needed for acceptance. The verifier rebuilds
the entire core against the predecessor source coefficients before using it.

## 4. A sharp one-sided projection gap

**Lemma.** Let Z be a matrix space of dimension at least two with no
nonzero rank-one matrix. Quotient the column leg of Mat_2 tensor Z by
a kernel K of dimension at most four, leaving the row leg unchanged.
The projected first-slice-space dimension is either zero or at least four.

Write the two auxiliary spaces as E and F, both of dimension two, and
let q:V tensor F -> (V tensor F)/K be the column quotient. One auxiliary
row block has projected image

    W=(id_U tensor q)(Z tensor F).

The whole projected space is E tensor W and has dimension 2 dim W.
Suppose dim W=1 and choose a nonzero generator h. For a basis f0,f1 of F
there are linear forms alpha,beta on Z with

    q(z tensor f0)=alpha(z) h,
    q(z tensor f1)=beta(z) h,

where id_U is suppressed. For every nonzero f=a f0+b f1, the kernel of
a alpha+b beta contains a nonzero z, since dim Z>=2. Its row support
has dimension at least two. Therefore

    dim {v in V: v tensor f belongs to K} >=2             (6)

for every f. Applying (6) to f0 and f1 and using dim K<=4 gives
K=V0 tensor f0 direct_sum V1 tensor f1, with dim V0=dim V1=2.
Applying (6) to f0+f1 forces dim(V0 intersect V1)>=2, so V0=V1=V2.
Thus K=V2 tensor F. The quotient is now the product quotient of V by V2
with F. Its image W is the image of Z under that quotient, tensored
with F, and has even dimension. This contradicts dim W=1, proving the lemma.

Complete cancellation occurs exactly when

    Row(Z) tensor F is contained in K.                   (7)

In particular (7) is impossible when dim Row(Z)>=3 and dim K<=4.
Equations (4), (5) and the lemma therefore give projected first dimension
at least four for every non-plane core in the stated asymmetric case.
The required upper bound two then forces the common-plane kernel.

The positive lower bound four is sharp for the general lemma. Take
Z=span(E01-E10,E02-E20) in Mat3. Every nonzero member has rank two:
two minors of x(E01-E10)+y(E02-E20) are x^2 and y^2. Quotient the
amplified column leg by the four coordinates of base columns 0,1 and
both auxiliary positions. The projected first dimension is four.
With a five-dimensional kernel, keeping just one amplified column, the
dimension is two. Exact matrices and ranks are replayed; the allowed
loss budget four is essential. These are controls for the abstract lemma.

## 5. Remaining work and provenance

The full asymmetric problem is reduced to nonzero rank-four conditioned
normals with a forced product first span on the smaller side. Classifying
the rank-two locus of M, constructing its actual third tensor, and deciding
later compatibility remain open. The common-plane conclusion in the
joint-zero branch alone supplies no induction across the remaining branch.

The source, complete first-normal system, biform description, no-rank-one
property, minimum core first rank and target first-rank ceiling retain
their predecessor credits and hashes in sources.json. The local
continuation consists of the auxiliary splitting, joint-support certificates,
one-sided gap lemma and their stated application. No new external theorem
is imported. All proofs and code were prepared with OpenAI Codex under
owner direction; replay is not independent mathematical review.
