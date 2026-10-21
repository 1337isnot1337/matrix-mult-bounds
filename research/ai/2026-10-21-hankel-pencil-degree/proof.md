# Hankel Segre images in the linear-annihilator range

October 21, 2026. AI-assisted written proof, unreviewed. This is an ordinary
restriction obstruction, not a tensor construction or an exponent improvement.
No historical priority, external independent review, or formalization is claimed.

Work over an algebraically closed field F of characteristic zero. Write S_j
for binary forms of degree j. Let a,b,r be positive integers with

    1 <= r < min(a,b),       5r < 2(a+b).

Put m=a+b-1, d=m-1, and

    t=3r-m,   k=max(1,floor((t+3)/2)),   B=max(r,k^2).

A sequence h of length m is a functional on S_d. Its a-by-b Hankel matrix
pairs the monomial bases of S_(a-1) and S_(b-1). Let X_r be the cone where
this matrix has rank at most r.

**Theorem.** Every linear map Phi:U tensor V -> S_d^* that sends every
decomposable input into X_r satisfies

    dim im Phi <= B.                                         (T)

For t<=0 this recovers the existing cap r. For t=1 it recovers the existing
first-boundary cap max(r,4). The new applications used in this package are

    t=2, r>=3:  B=max(r,4),
    t=3, r>=5:  B=max(r,9),
    t=4, r>=7:  B=max(r,9).

The displayed r conditions are exactly 5r<2(a+b) in these three cases.
In particular (a,b,r)=(8,8,6) and (9,9,7) have B=9.

The external inputs are the classical scalar Hankel annihilator description,
the index sum theorem for matrix pencils, and splitting of bundles on P^1.
The deductions below are supplied in full. The earlier repository proofs
of the t<=0 and t=1 cases are credited prior work, not new claims here.

## 1. Degree of the annihilator on a pencil

For an a-by-b Hankel pencil H(tau)=H_0+tau H_1 of generic rank s<min(a,b),
the classical scalar Hankel description gives a unique minimal binary
annihilator q(tau;x,y) of degree s in x,y, up to a rational function of tau.
This description includes nonreduced schemes and support at infinity; it
identifies the right kernel over F(tau) with q S_(b-1-s), and the left
kernel with q S_(a-1-s). One can use the elementary scalar proof in
`../2026-10-20-anisotropic-constructions/hankel_symbol_dimension.md`.

Choose q with polynomial coefficients in tau and coefficient gcd one.
Put epsilon=deg_tau q. Its monomial multiples are a basis over F[tau]
of the polynomial right kernel module. Indeed, a polynomial kernel
element is divisible by q over F(tau), and Gauss's lemma for primitive
polynomials over the UFD F[tau] makes its quotient polynomial over F[tau].
The highest tau coefficients of these monomial multiples are independent:
multiplication by the nonzero highest coefficient binary form of q is
injective. In fact every nonzero polynomial multiple q f has tau degree
epsilon+deg_tau f. Thus every polynomial right kernel vector has degree
at least epsilon, and a basis of b-s vectors attains it. All right minimal
indices equal epsilon. All a-s left minimal indices also equal epsilon.

Lemma 6.3, or Theorem 6.5 with grade one, of De Teran--Dopico--Mackey,
*Spectral equivalence of matrix polynomials and the index sum theorem*,
MIMS EPrint 2013.47, August 22, 2013, states that the sum of finite and
infinite structural indices and all left and right minimal indices is
the rank of a matrix pencil. The other indices are nonnegative. Hence

    (a+b-2s) epsilon <= s.                                   (1)

For every s<=r the hypothesis 5r<2(a+b) implies
s/(a+b-2s)<2. Therefore epsilon<=1. This conclusion is false without the
hypothesis: the exact controls include an 8-by-8 rank-seven pencil whose
primitive annihilator has tau degree two.

## 2. The annihilator map of a linear space

Let L be a linear subspace of X_r, of generic rank s. If s=0 then L=0.
Otherwise its unique minimal annihilator defines a rational map
P(L) -> P(S_s). Represent it by homogeneous coordinate polynomials of
one degree D with no common divisor. Its base locus has codimension at
least two. A generic projective line avoids that locus; restriction to
that line has degree D. Section 1 gives D<=1. For a one-dimensional L
the map is constant directly.

If D=0, all of L lies in the span of one fixed length-s scheme. If D=1,
there is a linear map Q:L -> S_s giving its minimal annihilator generically.
We call this the moving case. Its image has dimension p>=2. Let g be
the gcd of all forms in im Q, of degree c; write im Q=g W. The space
W is a p-dimensional basepoint-free subspace of S_(s-c).

For a generic pair q_0,q_1 in im Q, their gcd is g. Their scheme spans
intersect in the length-c span S_g. This follows from the jet intersection
formula, or directly from

    q_0 S_(d-s) + q_1 S_(d-s) = g S_(d-c).

The latter equality follows by taking the degree-d part of the ideal of
two coprime binary forms q_0/g,q_1/g; their principal syzygy also gives
it by dimension counting. Here d>=2s, since s<min(a,b), so the needed
degree threshold d>=2s-c-1 always holds.

If l_0 lies in ker Q, the generic line l+tau l_0 has the constant
annihilator Q(l). Thus l_0 belongs to every such scheme span, hence to
S_g. Consequently

    dim L <= p+c.                                            (2)

## 3. The space of linear assignments

For general s,d,c,p as above, fix a basepoint-free W subset S_(s-c).
A linear assignment A:W -> S_d^*/S_g is permitted when a lift h(w)
satisfies

    h(w)(g w f)=0  for every w in W and f in S_(d-s).          (3)

This does not depend on the lift, because S_g annihilates g S_(d-c).
Identify S_d^*/S_g with S_(d-c)^* by restriction to g S_(d-c).
Then (3), after polarization, becomes

    h_i(w_j f)+h_j(w_i f)=0.

Set e=d-s. Let E be the kernel bundle of evaluation on P^1:

    0 -> E -> W tensor O -> O(s-c) -> 0.

The forms in W are independent, so H^0(E)=0. The splitting theorem gives

    E = direct sum O(-mu_i),   mu_i>=1,   sum mu_i=s-c.        (4)

The evaluation map gives an exact sequence

    0 -> Sym^2 E(e) -> Sym^2 W tensor O(e)
      -> W tensor O(d-c) -> 0.                               (5)

On elementary tensors, w_i w_j maps to w_i tensor w_j+w_j tensor w_i,
with the second factor evaluated as a binary form. To check exactness
locally, split the evaluation surjection: the kernel of this symmetric
map is Sym^2 E; its coefficient on the square of the one-dimensional
quotient is two. Characteristic zero ensures surjectivity there.

The assignment space in (3) is dual to the cokernel on global sections
in (5). Since e>=0, H^1(O(e))=0. Its dimension is therefore

    alpha = h^1(Sym^2 E(e))
          = sum_(i<=j) max(mu_i+mu_j-e-1,0).                 (6)

The identity h^1(O(j))=max(-j-1,0) follows from Laurent monomials on
the two standard affine charts of P^1.

If alpha=0, every lift takes values in S_g, which cannot have generic
Hankel rank s>c. A moving rank-s family therefore requires alpha>0.
In particular 2 mu_max>=e+2. Since mu_max<=s-c-p+2, this gives

    2(p+c) <= 3s-d+2.                                       (7)

Combining (2) and (7) bounds every moving L by

    dim L <= floor((3s-d+2)/2) <= k.                         (8)

Thus **every L subset X_r with dimension at least k+1 lies in one fixed
scheme span**, even if its generic rank is smaller than r.

## 4. A Segre image

First assume the generic Hankel rank on decomposable inputs is exactly r.
Let v and u be the maximum dimensions of the V and U rulings, respectively.
If u,v<=k, then dim im Phi<=uv<=k^2. To prove the elementary bound uv,
choose u vectors u_1,...,u_u whose images span Phi(U,v_0) for generic v_0.
For generic v the same images span Phi(U,v). Thus all images lie in the
fixed space sum_i Phi(u_i,V), of dimension at most uv. The containment
extends to all v because this is a closed linear space.

Otherwise, exchange U,V if necessary so that v>=k+1. Section 3 puts
each generic ruling Phi(u,V) in one fixed scheme span of length r;
write its annihilator as q(u). If q(u) is constant generically, the full
image lies in that r-dimensional span and the theorem follows.

Suppose q(u) varies. Choose generic v_0. The linear family
u -> Phi(u,v_0) has generic rank r and the same annihilator map q(u).
Section 2 represents q(u) by a linear map Q:U -> S_r. Write im Q=g W,
with dimensions p,c as above. For l_0 in ker Q and generic v, the
fixed-annihilator line argument puts Phi(l_0,v) in S_g. Density extends
this to every v. After choosing a linear section of Q, each v therefore
supplies a permitted assignment W -> S_d^*/S_g. The span of all such
values has dimension at most p alpha. Adding S_g gives

    dim im Phi <= c+p alpha.                                (9)

It remains to bound (9) by k^2. Write ell=p+c. Since a,b>=r+1, we have
t=3r-d-1<=r-1. In (6), every term with i<j is zero, because
mu_i+mu_j<=r-c and e+1=2r-t>r. At most one square term is nonzero:
two such terms would require two mu_i whose sum exceeds 2r-t>r-c.
Consequently

    alpha <= 2(r-c-p+2)-2r+t = t-2ell+4.

A moving family has alpha>=1, so (7) gives 2<=ell<=k and k>=2.
Also t+4<=2k+2. Hence

    c+p alpha <= ell alpha <= 2 ell(k+1-ell) <= k^2.          (10)

The first inequality uses alpha>=1. The last follows from the identity

    k^2 - 2 ell(k+1-ell) = (k-ell)^2+ell(ell-2) >= 0.

This proves (T) when the generic rank is r. If that generic rank is
s<r, repeat the argument with s as the rank parameter. The hypothesis
5s<2(a+b) still holds, and both s and
max(1,floor((3s-d+2)/2)) are at most their r analogues. Thus the resulting
bound is at most B. The zero-rank case is immediate. This completes the
proof for arbitrary finite-dimensional U,V, including maps with kernels.

## 5. Controls, attribution, and scope

The exact controls include split-index calculations, a moving rank-six
linear space of dimension three, an eight-dimensional Segre image of
rank-seven Hankel matrices, and the quadratic-annihilator pencil outside
the hypotheses. The rank-seven Segre control refutes an extension with
image cap r instead of nine. No sharpness of nine is asserted.

The t<=0 and t=1 conclusions agree with the repository's prior
`hankel_symbol_dimension.md` and `hankel_boundary_dimension.md`. Their
claims and authorship are preserved. The present proof uses another
route and the new applications have t>=2. It does not construct the
matrix tensor, cover arbitrary higher-degree annihilator maps, or extend
ordinary restriction arguments to singular degenerations.

External sources, read in their stated versions:

- Fernando De Teran, Froilan M. Dopico, D. Steven Mackey (August 22, 2013),
  *Spectral equivalence of matrix polynomials and the index sum theorem*,
  MIMS EPrint 2013.47, Lemma 6.3 and Theorem 6.5, printed pages37--38
  (PDF pages38--39 including the cover):
  https://eprints.maths.manchester.ac.uk/2017/01/covered/MIMS_ep2013_47.pdf
- Claudia Schoemann, Stefan Wiedmann, *Another proof of Grothendieck's
  theorem on the splitting of vector bundles on the projective line*,
  arXiv:1712.03056v1 (December 8, 2017), Theorem 2.1, PDF page3:
  https://arxiv.org/pdf/1712.03056v1
