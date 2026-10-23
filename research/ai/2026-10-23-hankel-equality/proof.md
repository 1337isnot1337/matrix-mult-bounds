# A sharp constant-scheme strip above deficient-symbol equality

October 23, 2026. Owner-directed Codex work; written and unreviewed.
This generalizes the maintained rank-two equality containment. It does
not assert an ordinary matrix restriction, exclude a singular limit,
or improve the matrix multiplication exponent.

Work over C. Let a,b>=2, d=a+b-2, and use the literal cyclic source A(a,b).
For a source slice F set

    f_k(x,z) = sum_(i<a,s<b) F_(i,k,s) x^i z^s,
    H_F(x,z) = (f_(p+q)(x,z))_(p<a,q<b).

Let r be the rank of H_F over K=C(x,z), with

    1 <= r < min(a,b).

**Theorem.** If the full source slice matrix has rank strictly less than

    ab r + min(a,b),

there is a
degree-r nonzero homogeneous binary form q with constant coefficients
such that every coefficient sequence (F_(i,0,s),...,F_(i,d,s)) annihilates
q S_(d-r). Equivalently all these sequences belong to the same
length-r scheme span on the degree-d rational normal curve. The scheme
may be nonreduced and may contain infinity.

The supporting form q is unique up to a nonzero constant. In particular
the conclusion holds at equality rank M_F=ab r. It does not say that an
arbitrary slice with such a common q has rank ab r.

## 1. The two equalities

Adopt the polynomial coefficient maps and the full-output rank injections
from the credited maintained proofs `polynomial_rank_locus.md` and
`parity_structure_equality.md`. Their two orders give

    rank M_F >= b rho >= ab r,
    rank M_F >= a sigma >= ab r.

Here rho is the rank over C(x) of multiplication by H_F on b input
polynomials in z of degree below a. Likewise sigma is the rank over C(z)
of multiplication by H_F^T on a input polynomials in x of degree below b.
All output coefficients are retained. Since rho and sigma are integers,
rank M_F<ab r+min(a,b) forces rho=ar and sigma=br: otherwise the first
chain adds at least b or the second adds at least a.

The maintained coefficient-map equality lemma is valid at every rank:
if a polynomial matrix C(t) has rational-function rank r and its full
degree-below-T coefficient map has rank Tr, every column of C is a
constant linear combination of any r rationally independent columns.
Indeed those r columns and their T shifts form a basis of the image.
For another column c write c=sum p_j c_j with deg p_j<T; writing
t^(T-1)c in the same basis forces t^(T-1)p_j to have degree below T.
Independence over the rational function field makes each p_j constant.
This also covers T=1.

Apply this lemma to both inner maps, whose ranks are exactly ar and br.
The right kernel of H_F is the
scalar extension of a subspace defined over C(x). Its left kernel is
the scalar extension of a subspace defined over C(z). Neither statement
alone makes the supporting scheme constant in both variables.

## 2. Recover the same form from either kernel

The elementary scalar Hankel kernel description in the maintained
`hankel_symbol_dimension.md`, section 1, applies because r<min(a,b).
In homogeneous binary-form notation the kernels are

    ker_left H_F  = q_K S_(a-1-r),
    ker_right H_F = q_K S_(b-1-r),

for one degree-r form q_K over K, unique up to K*. The functional f
annihilates q_K S_(d-r).

For clarity, the kernel description is valid over the rational function
fields used here: take the gcd q of a kernel basis. The elementary
binary-form multiplication lemma in the cited proof shows that the
functional annihilates q S_(d-deg q). The resulting pairing factors
through the deg-q-dimensional quotient, so rank H_F<=deg q. The kernel
dimension gives deg q<=r, and both inequalities force deg q=r. The
kernel has the same dimension as q S_(a-1-r), giving equality. The same
argument applies to the right kernel. The common functional then makes
the two supporting forms proportional; alternatively their scheme spans
have intersection equal to the span of the scheme intersection, since
their union has length at most 2r<=d. Thus no algebraic closure or choice
of distinct roots is required for the kernel calculation.

Take a C(x)-basis of the right kernel supplied by section 1 and form its
homogeneous polynomial gcd over C(x). Scalar extension to K preserves
this gcd up to a unit: after removal of the gcd the residual homogeneous
forms have no common projective zero, a property preserved by field
extension (or checked by their univariate Bezout identity in each chart).
Because the gcd of all degree-(b-1-r) monomials is one, the resulting
degree-r form q_x is proportional to q_K. This remains true when
b-1-r=0, where the kernel is one dimensional.

The left kernel gives a degree-r form q_z over C(z) proportional to the
same q_K. Choose one nonzero coefficient of q_K and normalize that
coefficient of all three forms to one. Every other coefficient then lies
in both C(x) and C(z). Inside C(x,z) their intersection is C: a rational
function of x equal to a rational function of the independent variable z
must be constant, as follows by clearing denominators and comparing
coefficients. Hence the normalized form q has coefficients in C.

## 3. Descend the recurrence coefficient by coefficient

Write q(U,V)=sum_(j=0)^r q_j U^(r-j)V^j. The annihilation statement is

    sum_(j=0)^r q_j f_(k+j)(x,z)=0,   0<=k<=d-r.

Since q_j are constant, comparing coefficients of x^i z^s gives the same
identities for every coefficient sequence of F. These are exactly the
equations for the span of the length-r zero scheme of q on P1, including
jets at multiple roots and at infinity. Uniqueness of q_K gives uniqueness
over C up to scale. This proves the theorem.

## 4. Boundaries and the unresolved family problem

The strict inequality r<min(a,b) is essential. PR76 already provides
full-symbol-rank equality counterexamples, including the actual A(8,9)
frontier format. The small control f=(0,x,0,1) in A(2,3) has symbol rank
two and full slice rank twelve, but its coefficient sequences have no
common quadratic annihilator. That warning is retained with its credit.

The strict strip boundary is sharp in a family of balanced formats. For
every r>=2 take a=b=r+1, d=2r and

    f_0=1,   f_r=x,   f_(2r)=x^2,

with all other f_k zero. The degree bounds hold. The symbol has rank r:
its final column is x times its first, while the leading r-by-r minor
is a nonzero signed power x^(r-1). Its kernel is generated by
(-x,0,...,0,1), so its supporting form V^r-x U^r moves with x.

Because the coefficients are independent of z, the full source matrix
splits into a identical blocks, indexed by the original short z input
coordinate. The transpose of each block is the full polynomial
coefficient map for this scalar Hankel matrix, with input degrees below a.
Its polynomial kernel consists of (-x,0,...,0,1)g(x), with deg g<a-1.
Thus each block has rank a^2-(a-1)=ar+1, and

    rank M_F = a(ar+1) = ab r + min(a,b).

No constant degree-r annihilator exists: the coefficient of x is the
sequence supported only at the middle index r. Its shifted recurrence
equations, for shifts zero through r, force every coefficient of a
putative annihilator to vanish. This supplies a written all-rank sharpness
family, not just finite evidence. The exact controls replay its small
members independently.

As a historical arithmetic example, in the A9 square sum (32,6,3), a rank-one parameter of the M32
block lifts to source rank at most 648=8*81. If its symbol rank is eight,
the theorem gives a constant length-eight scheme **for that parameter**.
It does not make that scheme independent of the matrix parameter. A
family argument is still required to turn this pointwise statement into
a general family constraint. This historical ordinary candidate is
already excluded by the maintained Wronskian application: rank-three
M32 parameters lift to rank 712<729, and the credited three-ruling cap
would inject 1024 parameters into 11*81=891 dimensions. This existing
exclusion is not attributed to the present lemma. Its source and the
underlying unreviewed proof status are retained in sources.json.

## Attribution

The coefficient-map equality lemma, the two injection chains, the
rank-two theorem and the elementary Hankel kernel description are prior
repository work. Their unchanged files are pinned in sources.json. The
crossed-flattening equality theorem and full-rank counterexamples in the
unmerged rectangular PR76 retain their separate credit. The continuation
here is the all-deficient-rank kernel-gcd descent and its exact controls.
No external independent review, formalization or historical novelty is
claimed.
