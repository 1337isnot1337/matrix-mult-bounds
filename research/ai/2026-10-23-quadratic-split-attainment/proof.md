# Split and doubled quadratics: exact rectangular source ranks

October 23, 2026. Owner-directed Codex research, written and unreviewed.
Same-session checking is not independent mathematical review or
formalization. This note classifies an explicit one-parameter family of
individual source slices and proves balanced attainment over algebraically
closed fields. It gives no source-space dimension bound, compatible tensor
target, or improved matrix-multiplication exponent.

The source convention, two-index rank formula, and structural dichotomy
are credited to the merged
[quadratic kernel-index package](../2026-10-23-quadratic-kernel-indices/README.md).
The recurrence calculation below is elementary and needs no line-bundle
torsion theorem or geometric gluing convention. Exact prerequisite hashes
and the distinction between new and prior evidence are in
[sources.json](sources.json).

## 1. Statement with all source endpoints

Let K be any field, a>=3, b>=3, and m=a+b-1. For

    q_t(x,z)=(z-x)(z-tx)=t x^2-(1+t)xz+z^2,
                         t in K^*,                       (1)

use the full crossed source matrix

    R_(a,b)(q_t)[(j,L),(H,r)]
       = [x^(H-j) z^(L-r)] q_t,
    0<=j<b, 0<=r<a, 0<=L,H<m.                           (2)

Thus the matrix has bm rows and am columns. Its rows are ordered by
(j,L) and its columns by (H,r). Every output coefficient from the
literal source is retained. The degree-two coefficient polynomials in
(1) have degree below a because a>=3. The condition b>=3 retains
every potentially nonzero z-row group L=0,...,a+1.

Define the finite geometric sums by

    S_0(t)=0,       S_n(t)=1+t+...+t^(n-1) for n>=1,
    epsilon_a(t)=1 if S_(a+1)(t)=0, and 0 otherwise.      (3)

**Theorem A (all-field split/double formula).** The two polynomial
kernel indices of (1) are

    (mu1,mu2)=(a-epsilon_a(t), a+epsilon_a(t)).            (4)

The full rectangular source rank is exactly

    rank_K R_(a,b)(q_t)
      = ab+min(b,a-epsilon_a(t))+min(b,a+epsilon_a(t))
      = ab+2 min(a,b)-epsilon_a(t) [a=b].                 (5)

Here [a=b] is one when a=b and zero otherwise. More explicitly:

- If t!=1, then epsilon_a(t)=1 exactly when t^(a+1)=1.
- If t=1, the polynomial is the doubled model (z-x)^2 and
  epsilon_a(1)=1 exactly when char K=p>0 and p divides a+1.
  In characteristic zero epsilon_a(1)=0.

Thus the two possible index pairs are (a-1,a+1) and (a,a), but their
rank difference is visible only at the balanced integer width b=a.
At every b!=a both give ab+2 min(a,b).

**Theorem B (algebraically closed balanced attainment).** For every
algebraically closed field K and every a>=3, the nonzero ranks of
balanced quadratic-in-z slices with coefficient degrees below a are
exactly

    {a^2, a^2+a, a^2+2a-1, a^2+2a}.                    (6)

The prior structural theorem supplies containment. The present explicit
split and doubled models supply attainment of the one-unit defect in
every characteristic and at every size. For a>3, (6) concerns only
quadratic-in-z slices, not arbitrary biforms or the whole cyclic source.

## 2. An auxiliary recurrence valid for every n>=2

For n>=2 let T_n(t) be the exact coefficient map on tuples
lambda_0,...,lambda_n in K[x], with each coordinate of degree at most
n-2, given by

    t x^2 lambda_r-(1+t)x lambda_(r+1)+lambda_(r+2),
                            0<=r<n-1.                   (7)

Every x coefficient through degree n is included. This is a square
map with (n-1)(n+1)=n^2-1 coordinates on each side. These auxiliary
maps are defined even at n=2,3; that does not extend the source-rank
theorem to a=1,2, where its coefficient-degree hypothesis would fail.

**Recurrence lemma.** For every field K, every t!=0, and every n>=2,

    dim ker T_n(t)=1 if S_n(t)=0, and 0 otherwise.         (8)

When S_n(t)=0 an explicit basis is

    lambda_0=0,
    lambda_r=S_r(t) x^(r-1),       1<=r<=n.               (9)

In particular the last coordinate in (9) is zero, not an omitted
endpoint equation.

To prove the lemma, set P=lambda_0 and Q=lambda_1. Since the last
coefficient in (7) is one, every polynomial recurrence solution is
uniquely determined by P,Q. Induction gives

    lambda_r=x^(r-1)(S_r Q-t S_(r-1)xP),   1<=r<=n.      (10)

This follows from S_0=0, S_1=1 and

    S_(r+1)=(1+t)S_r-t S_(r-1).

We shall also use

    S_(r-1)^2-S_r S_(r-2)=t^(r-2),       r>=2.           (11)

For example, the expression on the left is one at r=2, and the
displayed recurrence multiplies it by t when r increases by one.
Thus (11) follows by induction without dividing by 1-t. Both (10)
and (11) are valid at t=1 and in every characteristic.

Suppose S_n!=0. Formula (10) expresses lambda_n as x^(n-1) times
a polynomial. The degree bound deg lambda_n<=n-2 therefore forces
that polynomial to be zero, giving

    Q=t S_(n-1) xP/S_n.

Using this in the preceding coordinate and applying (11) yields

    lambda_(n-1)=t^(n-1) x^(n-1) P/S_n.

The scalar is nonzero because t and S_n are nonzero. The same degree
bound forces P=0 and then Q=0. All coordinates vanish.

Suppose instead S_n=0. The identity S_n=1+t S_(n-1) gives
S_(n-1)=-t^-1, which is nonzero. Formula (10) now gives
lambda_n=x^n P, so its degree bound forces P=0. The preceding
coordinate is S_(n-1)x^(n-2)Q and forces Q to be constant. Conversely,
every constant Q gives Q times (9), satisfying the recurrence and
all degree bounds. Its lambda_1 coordinate is Q, so the solution
space is exactly one-dimensional. This proves (8).

The familiar split and doubled criteria follow only after this
characteristic-free calculation. For t!=1,

    (1-t)S_n=1-t^n,

so S_n=0 iff t^n=1. At t=1, S_n is the image of the integer n
in K. The doubled equation is explicitly

    x^2 lambda_r-2x lambda_(r+1)+lambda_(r+2)=0.

In characteristic two the middle coefficient is zero; no step of
the proof divides by two. There is also no binomial normalization,
differentiation, or characteristic-zero interpolation premise.

## 3. From the auxiliary kernel to the two source indices

The coefficient triple t x^2, -(1+t)x, 1 is primitive because its
last member is one, and has maximum degree two because t!=0.
It has no fixed homogeneous z-root over any extension field: for
constant [s:h], the identity

    t x^2 s^2-(1+t)x s h+h^2=0

would force s=0 from its x^2 coefficient and h=0 from its constant
coefficient, an impossibility for a projective point. This also
covers characteristic two and the doubled case.

The merged quadratic index theorem gives mu1+mu2=2a, with mu1<=mu2.
The full polynomial recurrence coefficient matrix C_(a-1) of that
theorem is exactly T_(a+1)(t): both have lambda_0,...,lambda_(a+1)
of degree at most a-1 and equations (7) for r=0,...,a-1, with all
x coefficients through degree a+1.

Because the indices sum to 2a, mu1<=a<=mu2. The prior bounded-kernel
formula therefore gives

    nullity C_(a-1)=(a-mu1)_+ +(a-mu2)_+=a-mu1.

The recurrence lemma sets this nullity equal to epsilon_a(t), so
mu1=a-epsilon_a(t) and mu2=a+epsilon_a(t). This proves (4)
directly from the index sum and bounded-kernel formula.
Substituting the two indices into the prior full-source rank formula

    rank R_(a,b)=ab+min(b,mu1)+min(b,mu2)

proves the first equality of (5). If b<a, integrality gives b<=a-1
and both minima equal b. If b>a, then b>=a+1 and their sum is 2a.
If b=a, their sum is 2a-epsilon_a(t). These three cases prove the
second equality of (5).

The value ab+2 min(a,b) is also the largest rank permitted by the
active support of this particular degree-two family: only (a+2)b
rows and a(b+2) columns of (2) can be nonzero, whose smaller number
is ab+2 min(a,b). These zero groups are accounted for in the full
matrix calculation; no source truncation defines the theorem.

## 4. Every balanced rank over an algebraically closed field

Fix an algebraically closed K and a>=3, and write n=a+1>=4. To
attain the one-unit defect there are two cases.

If char K=p>0 divides n, choose t=1. The doubled model has S_n(1)=0
and therefore rank a^2+2a-1 by Theorem A.

Otherwise n is nonzero in K. The polynomial t^n-1 has n distinct
roots: its derivative is n t^(n-1), nonzero at every root. Since
n>=4 and K is algebraically closed, it has a nonzero root different
from one. Choose such a t. Then S_n(t)=0 and the distinct-factor
model has the same one-unit defect.

For full active rank choose a nonzero t with t^n!=1. An algebraically
closed field is infinite, while this polynomial has only finitely many
roots, so such a t exists. Formula (5) then gives a^2+2a. The
remaining two ranks are supplied by the prior universal witnesses
f=1 and f=1+xz, of ranks a^2 and a^2+a respectively. All these
coefficient polynomials have degree below a. Together with the prior
four-value containment this proves (6).

This argument uses the existence of roots in an algebraically closed
field, not a bounded field search. It makes no all-size attainment
claim over an arbitrary nonclosed ground field.

## 5. Boundaries, exact checks, and prior negative evidence

The parameter t=0 is excluded from Theorem A. It gives q_0=z(z-x),
whose primitive coefficient degree is one and which has a fixed
homogeneous root. The prior formula then gives indices (0,a) and
rank ab+min(a,b), instead of (5). The value t=1 is included, but
must use S_n(1)=n rather than division by 1-t. The source hypotheses
a>=3 and b>=3 are separate from the auxiliary range n>=2.

Over Q, the distinct-factor model has a defect exactly when t=-1
and a+1 is even: the only rational roots of unity are 1 and -1,
and t=1 is the doubled case with no defect in characteristic zero.
This restriction is only a classification of the explicit family
(1); it does not exclude rational attainment by other biforms.

As another field-sensitive example within this family, take a=8.
Over F2 the only nonzero parameter is t=1, with S_9(1)=1 and
balanced rank80. Over F4 an element alpha with alpha^2+alpha+1=0
has alpha^9=1 and alpha!=1, giving rank79. This comparison concerns
q_t only, not all binary quadratic slices.

The package's finite controls reconstruct both the auxiliary recurrence
and the complete literal source. They check split and doubled cases,
the rectangular transition at b=a, the displayed kernel vector, and
the excluded t=0 boundary using exact arithmetic. Finite fields and
rational examples corroborate the proof; they do not establish its
all-field or all-size quantifiers.

A prior separate experiment checked the sixteen rational sign choices
u=+/-x^2, v=+/-1, w=+/-x+/-x^2 supporting the binary order-five model.
Its saved T_5 matrices all had full rank24. Those sixteen cases were
not rerun here, are not counted as new acceptance checks, and exclude
only those sign lifts. Their preserved hashes and limited scope are
recorded separately in sources.json. They are not a premise of either
theorem and do not imply failure of rational order-five models generally.

Review status remains written and unreviewed. No independent review,
historical-priority claim, target construction, or exponent improvement
is inferred from these formulas or their finite checks.
