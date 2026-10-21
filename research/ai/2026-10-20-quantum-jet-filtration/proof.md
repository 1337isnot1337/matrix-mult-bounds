# First-jet slice bounds without a grading assumption

Written local proof, unreviewed, October 20, 2026. No historical priority
or exponent improvement is claimed. This extends the saturated-rowspace
argument from the leading-flags package.

## 1. A partial saturated space

Let T be in A tensor B tensor C over a field, with dim A=a. Write
P(t)=P0+tP1+... and Q(t)=Q0+tQ1+... for two regular local maps. Let
S(t)=S0+tS1+... be the first-leg flattening of
(1 tensor P(t) tensor Q(t))T. Its rows are indexed by A. Put

    W1 = rowspan(S0)+{x S1 : x S0=0},
    r1 = dim W1.

The saturated limiting row space L0 contains W1. Indeed every constant
row combination xS(t) with xS0=0 is divisible by t, and xS(t)/t has
constant term xS1. These are regular rows in the generic row space, so
their constants lie in its saturated residue.

If E_B=im(P0), E_C=im(Q0), of dimensions b0,c0, then

    S1 corresponds to (P1 tensor Q0+P0 tensor Q1)T.

Both S0 and S1 are supported in
E_B tensor C' + B' tensor E_C. Consequently the tensor representing any
basis of W1 has slice rank at most b0+c0, by expanding along the two
small spaces. Extend such a basis to the at-most-a-dimensional space L0.
Each additional basis vector costs one first-leg slice. Every regular
limit made with an arbitrary Laurent first-leg map is a restriction of
that basis tensor. Therefore

    slice_rank U(0) <= a-r1+b0+c0.                         (1)

This holds with arbitrary higher jets in P,Q and arbitrary Laurent orders
on the first leg. As before, it does not assert submultiplicativity of
slice rank or give a tensor-power barrier.

## 2. A lower-rank witness that ignores the other first jet

Choose a projection pi_B killing E_B. Define the map

    x -> (xS0, (pi_B tensor 1)(xS1)).

Its rank k equals
rank(S0)+rank{(pi_B tensor 1)(xS1):xS0=0}. Since the projection kills
rowspan(S0), this rank is at most dim W1. Moreover the projected S1 is
just (pi_B P1 tensor Q0)T: the entire P0 tensor Q1 term vanishes there.
Thus this lower bound for r1 permits an arbitrary first jet Q1.
The other direction is symmetric.

For the root maps below, E_B,E_C are supported on four coordinate rows.
The witness is the ordinary projected-source flattening made with

    Btilde=P0+(the rows of P1 outside the four leading rows), Ctilde=Q0.

Its core and new-row columns are disjoint, so it represents the direct
sum map above, up to dropping zero coordinates.

## 3. Root derivatives and exact certificates

Use the same four phases as the leading-flags package: the two primitive
roots of order three and the two of order six. Let Phi be the relevant
cyclotomic polynomial, and nu the minimum entry valuation of the quantum
local matrix M(q). Set R(q)=Phi(q)^(-nu) M(q). Its value at the root is
G, supported on rows 70,71,73,74, of grades 4,5,7,8.

The first-jet code differentiates this regular matrix exactly. For an
entry f=Phi^v N/D, where N,D are coprime to Phi, the derivative at zeta is

    (N'D-ND')/D^2 at zeta,             if v=nu;
    Phi'(zeta) N/D at zeta,            if v=nu+1;
    0,                                if v>=nu+2.

All numerator and denominator operations are exact. Reduction modulo the
prime 786433 is made only after checking that the residue denominators
are nonzero. A nonzero minor after this reduction is nonzero over the
cyclotomic number field and in every complex embedding.

For each of sixteen ordered phase pairs and either varying leg, a
64-by-64 minor is nonzero. Hence r1>=64. With a=112 and b0,c0<=4, (1)
gives

    slice_rank U(0)<=112-64+4+4=56.                       (2)

The other first jet and every higher matrix jet are unrestricted in this
statement. Only the outside-leading-row part of the specified first jet
is fixed, up to a nonzero scalar.

## 4. Every nonzero approach rate

If the specified first derivative is multiplied by lambda, every new-row
column of the selected minor is multiplied by lambda, while every core
column is unchanged. Its determinant is therefore

    lambda^e times the nonzero certified determinant,

where e is the number of selected new-row columns, recorded separately
for each certificate. Thus the rank lower bound holds for every nonzero
complex lambda, not merely the finite-field rates in the discovery pilot.

Now consider independent nonconstant parameter arcs q_B(t),q_C(t) tending
to the selected roots. Clear each local matrix's scalar pole with its
Phi factor; this scalar can be absorbed into the arbitrary Laurent map
on the remaining leg. Let m be the earlier of the two finite positive
approach orders. Both regular matrices are constant through order m-1.
At order m at least one has a nonzero scalar multiple of R'(zeta).
The other contributes either zero or its own first derivative.

Replace t by t^m in the partial-saturation argument: divide constant
kernel rows by t^m. The same W1 and disjoint-column minor proof applies.
It yields (2), regardless of the two approach orders, leading rates or
higher parameter coefficients. Puiseux arcs are covered after a common
ramified base change.

The matrix target restricts to square M10, whose slice rank is 100 by
Blasiak et al., arXiv:1605.06702v4, Remark 4.9. Slice-rank upper bounds
persist under restrictions and further complex degenerations. Thus these
quantum-curve limits cannot supply the target even if subsequent maps
break the Cartan grading. If a regularized parameter is constant at its
root, that leg has rank at most four throughout and cannot give a
110-dimensional concise target leg either.

## 5. Constant output projections before the limit

The full-output statement alone does not justify moving a projection
through a possibly divergent expression. Here is a separate argument
that includes constant output maps before regularity is imposed.

Let L_B:B' -> B'' and L_C:C' -> C'' be constant surjections, each of
codimension at most two. Fold them into P and Q before constructing S.
There is no assumption that the tensor before these projections has a
regular limit. Suppose for definiteness that the specified earliest jet
is on B. Write E=im P0, F=im Q0; the saved leading-map minors show
dim E=dim F=4.

Consider the auxiliary tensor

    H=(1 tensor (P0+P1_out) tensor Q0)T,

with the specified jet's nonzero scalar rate included in P1_out. Its
F-coordinate slices at grades 4,5,7,8 each have a certified nonzero
28-by-28 minor. All local matrices preserve weight, so H is homogeneous
for the original three-leg grading. Every nonzero linear combination of
these four slices has rank at least 28: apply the grading torus on A and
B, rescale by the smallest occurring weight, and take the limit. The
limit is a nonzero multiple of one coordinate slice. Matrix rank cannot
increase in this limit, and all four weights are distinct. Each minor
remains nonzero at every nonzero rate by the same column-monomial test
as in Section 4. This is a statement over the number field, not an
inference from random linear combinations over a finite field.

Since L_C has kernel dimension at most two, it does not annihilate F.
Choose a functional on C'' whose pullback beta to F is nonzero. The
A-by-B matrix H_beta therefore has rank at least 28.

Use the filtration E subset B'. The associated graded map induced by
L_B is

    E direct_sum (B'/E) -> L_B E direct_sum (B''/L_B E).

It is surjective and has kernel dimension equal to dim ker L_B, at most
two. Consequently its application to H_beta has matrix rank at least
26. The two components of this resulting row map are precisely

    x -> (x S0'_beta, (pi tensor beta) x S1'),

where S' is formed after the output maps and pi kills L_B E. In the
second component pi kills the P0 tensor Q1 term and the E-valued part
of P1. In the first component S0'_beta lies in L_B E. Thus this map is
a contraction of the partial map from Section 2 for S', and its rank
is at most the new partial-saturation dimension r1'. We obtain

    r1' >= 26,
    slice_rank U(0) <= 112-26+4+4 = 94.                 (3)

The argument is symmetric for a specified C jet, and Section 4 supplies
that jet for either earliest approach order. It allows arbitrary constant
surjections to the two 110-dimensional target legs, including ungraded
ones whose kernels meet the leading images. Non-surjective maps into
those spaces cannot produce a concise 110-dimensional target leg.
Further restrictions and degenerations are covered by slice-rank
semicontinuity. The four leading-rank controls and 128 slice minors are
included in the frozen certificate file.

Parameter-dependent output projections, different leading flags,
non-scalar row weights, or changed first
derivatives outside the prescribed curve remain outside the conclusion.
The original source target and an exponent below 9/4 remain open.
