# The channel-rank deficit also raises the auxiliary border-rank bound

October 23, 2026. Follow-up to the Laurent channel-separation proof.
Written and unreviewed; no exponent improvement or independent review.

The first flattening bound in `proof.md` is unchanged. If a nonzero good
contraction subspace has dimension d and its generic channel rank is at
most rho<h, its auxiliary **border rank** satisfies the stronger bound

\[
\boxed{\underline R(R)\ge d+h-\rho-1.}                 \tag{1}
\]

This statement explicitly assumes d>=1. For d=0 the argument supplies
no bound. The bound on the auxiliary first flattening remains d; (1)
does not assert the stronger number for an ordinary matrix flattening.

## 1. Rank-one terms retain rank-one channel matrices

The rank-one-term substitution pattern is standard; see Landsberg and
Michałek, *On the geometry of border rank algorithms*,
[arXiv:1601.08229v1, Section 5](https://arxiv.org/pdf/1601.08229v1).
The local addition here combines it with the preceding primitive-vector
regularity argument and the target's channel-polynomial determinant.

Retain the fields O=K[[t]], L=K((t)) and channel-polynomial encoding Psi
from the preceding proof. A long-leg rank-one term b tensor c maps to

\[
\left(\sum_j b_{j,\alpha}X^j\right)_\alpha
\left(\sum_i c_{\beta,i}Y^i\right)_\beta^{\mathsf T}.
                                                               \tag{2}
\]

Its channel matrix has rank at most one over L(X,Y), including when
the coefficients have poles. The first coefficient of such a tensor
term is an L-linear functional on first covectors.

Assume that the complete regular total is

\[
S(t)+\sum_{k=1}^c a_k(t)\otimes b_k(t)\otimes c_k(t)
       =M(l,h,r)+O(t),                                      \tag{3}
\]

and that V subset A* over L has dimension d>=1, with
rank(Psi(S(t)(w)))<=rho for every w in V. Put q=h-rho-1>=0.
If c<=d+q-1, impose the vanishing of any max(c-q,0) of the first
functionals a_k on V. Fewer than d linear equations have been imposed,
so there is a nonzero w(t) in their common kernel. At most q summands
of (3) survive its contraction.

Multiply w by the smallest power of t that makes all its coordinates
regular. Its nonzero constant term is w0. The contracted total is
regular and has constant term M(w0), whereas its generic channel rank
is at most rho+q=h-1. Its determinant therefore vanishes over L(X,Y).
After regularity is established, specialize the determinant at t=0.
This gives

\[
0=\det\Psi(M(w_0))=L_{w_0}(X,Y)^h,
\]

contradicting injectivity of w0 -> L_w0. Hence c>=d+q, which is (1)
for an auxiliary tensor with an actual c-term decomposition after its
local maps. The proof permits moving V and arbitrary pole cancellation
among all the surviving terms.

## 2. Applying the argument to auxiliary border rank

Over the complex numbers, use the standard rank-one-curve description
of border rank; see Conner, Harper and Landsberg, *New lower bounds for
matrix multiplication and det3*, [arXiv:1911.07981v1, Section 2.2](https://arxiv.org/pdf/1911.07981v1).
Choosing an algebraic curve in the closure of the rank-one addition
parameterization and normalizing its parameter gives Laurent factors
with finite pole orders. Thus a border-rank-c auxiliary admits an
approximation, possibly after ramification of its parameter:

\[
R(u)=\sum_{k=1}^c a_k(u)\otimes b_k(u)\otimes c_k(u)
     =R+O(u),                                              \tag{4}
\]

where the individual factors have finite pole orders. Equivalently,
the following argument applies over any field for which a formal
rank-c approximation (4) is supplied. It does not infer a rational
decomposition over a field merely from a geometric statement over its
algebraic closure.

Let A_R(t),B_R(t),C_R(t) be the three auxiliary local maps in the
original degeneration. Choose nonnegative integers p_A,p_B,p_C such
that t^p_A A_R, t^p_B B_R and t^p_C C_R all have regular entries, and
write P=p_A+p_B+p_C. Set u=t^N for any integer N>P. The error in (4)
then maps to O(t^(N-P)), hence to O(t). Therefore replacing the
auxiliary contribution by the c rank-one terms obtained from (4)
preserves the complete target identity modulo t. The local maps and
rank-one factors still have finite Laurent pole orders. Apply Section
1 to that replacement to obtain (1).

If a Puiseux parameter was used to obtain (4), choose its ramified
uniformizer first; (4) and the integer substitution are in that
uniformizer. No uniform N across source sizes is required.

## 3. Paired-source consequence

For the paired application in `proof.md`, one may take rho=ab, where a
is the common B-window span dimension and b is the C-profile count.
Whenever

\[
d_0=(lr-n^2+g_Bg_C)_+\ge1,\qquad ab<h,
\]

the same hypotheses imply

\[
\underline R(R)\ge d_0+h-ab-1.                         \tag{5}
\]

For d0=0 only the trivial bound zero is asserted. Replacing d0 by the
larger exact good-subspace dimension is valid. At fixed h the added
term is constant, so this sharpens finite repair bounds without changing
the preceding n-squared-minus-lower-order asymptotic conclusion.

## 4. Exact controls and a sharp one-dimensional example

Take d=1, 1<=rho<h, and standard channel vectors e0,...,e_(h-1).
Define

\[
S(t)=\sum_{j<\rho}e_je_j^{\mathsf T}
        +t^{-1}e_\rho e_0^{\mathsf T},\qquad E(t)=I_h-S(t).
                                                               \tag{6}
\]

S is an idempotent of rank rho, and E is an idempotent of rank h-rho.
Their actual poles cancel in S+E=I_h. The fixed auxiliary can be taken
to be a tensor a tensor I_(h-rho), with a one-dimensional first factor.
It has first flattening rank one and tensor border rank exactly h-rho,
which equals (1). Its images under the local maps are the terms

\[
e_\rho(e_\rho-t^{-1}e_0)^{\mathsf T}
  +\sum_{j>\rho}e_je_j^{\mathsf T}.
\]

Constant identity minors and these displayed decompositions certify
both channel ranks in every characteristic. Dropping one auxiliary
term leaves a total of rank at most h-1, so the complete target fails.

The verifier also supplies a rank-three approximation R(u) whose
mapped error is exactly u*t^-5 times one nonzero coefficient. It checks
u=t^4 (a pole survives), u=t^5 (the constant target changes), and u=t^6
(the error has positive order). These controls test the strict
inequality N>P in the proof rather than discarding a divergent raw
constant coefficient. A separate paired-source control has d0=16,
h=4 and ab=1, so (5) gives border rank at least 18 while the preceding
first-flattening conclusion is only 16.

These finite identities support the written argument. They are not an
independent mathematical review, formalization, or a matrix multiplication
construction. The earlier ordinary channel factorizations retain their
attribution in `sources.json`.
