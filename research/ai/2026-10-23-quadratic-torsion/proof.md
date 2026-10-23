# Quadratic rank defects and a degree-zero line bundle

October 23, 2026. Owner-directed Codex research, written and unreviewed.
All checking described here belongs to the generating session. It is not
independent mathematical review or formalization. This note concerns one
crossed biform block and gives no tensor construction or improved
matrix-multiplication exponent.

The two-index formula and its structural dichotomy are credited prior
work in the merged [kernel-index package](../2026-10-23-quadratic-kernel-indices/README.md).
The present increment identifies its one-unit rank defect with torsion of
a specific line bundle, including the singular boundary, and determines
exactly when that defect can occur over F2. Standard cohomology,
degree, Riemann--Roch and normalization inputs are cited below and pinned
in [sources.json](sources.json). The arguments connecting those inputs
to this source matrix are given explicitly.

## 1. Statement and source convention

Let K be a field and a>=3. Start with a nonzero biform

    f(x,z)=u_original(x)+z v_original(x)+z^2 w_original(x),

whose three coefficient polynomials have degree below a. The balanced
crossed source matrix is exactly

    R_(a,a)(f)[(j,L),(H,r)] = [x^(H-j) z^(L-r)] f,

where 0<=j,r<a and 0<=L,H<2a-1. Thus all source rows, columns,
and x-coefficient endpoints are retained. Divide the three polynomials
by their monic common gcd and call the primitive triple u,v,w. Assume

    max(deg u,deg v,deg w)=2,
    u s^2+v s t+w t^2 is not identically zero
                         for every [s:t] in P1(K).        (1)

The second condition excludes a fixed K-rational homogeneous z-root.
Homogenize the triple to x-degree two and set

    U(X0,X1)=X0^2 u(X1/X0),   and similarly V,W,
    F(X,Z)=U Z0^2+V Z0 Z1+W Z1^2,
    Y=P1_X x P1_Z,          C=V(F) in Y,
    L=O_C(1,-1).                                          (2)

The letter L in the line-bundle notation is separate from the integer
row-group index in the literal source formula.

**Theorem A (all fields).** Under (1), L is nontrivial. For every n>=2,
let T_n be the coefficient matrix of the equations

    u lambda_r+v lambda_(r+1)+w lambda_(r+2)=0,
      0<=r<n-1,       deg lambda_j<=n-2,  0<=j<=n.         (3)

Every x coefficient through degree n is included. Then

    ker T_n = H0(C,L^n),                                  (4)
    dim ker T_n = 1 if L^n is trivial, and 0 otherwise.     (5)

The identification (4) is the explicit one in Section 2. In the notation
of the prior package, T_(a+1)=C_(a-1). Consequently

    rank R_(a,a)(f)=a^2+2a-1  iff  L^(a+1) is trivial,
    rank R_(a,a)(f)=a^2+2a    otherwise.                   (6)

Equivalently, if L has finite order d in Pic(C), the defect occurs
exactly when d divides a+1. If its order is infinite it never occurs.
No smoothness or K-rational point is required for this statement.
When C is smooth and geometrically integral it has genus one, and L
is the particular nonzero degree-zero class O_C(1,-1), rather than
an arbitrary chosen class.

**Theorem B (binary attainment).** For each a>=3, among nonzero
quadratic-in-z slices over F2 with coefficient degrees below a,

    a^2+2a-1 is attained  iff  gcd(a+1,30)>1.             (7)

The other three values in the balanced four-value containment are
always attained. Thus the exact nonzero rank set for this family is

    {a^2, a^2+a, a^2+2a}
       union {a^2+2a-1 : gcd(a+1,30)>1}.                  (8)

This is a statement about quadratic-in-z slices. For a>3 it is not a
classification of arbitrary biforms or of the full cyclic source.

## 2. Exact coefficient map from an ambient sequence

The nonzero section F of O_Y(2,2) is a non-zero-divisor on the integral
smooth surface Y. Thus C is an effective Cartier divisor, even if C
itself is reducible or nonreduced. For every n>=2 its defining sequence,
twisted by O_Y(n,-n), is

    0 -> O_Y(n-2,-n-2) --F--> O_Y(n,-n)
      -> O_C(n,-n) -> 0.                                 (9)

Both ambient H0 groups vanish because their second twists are negative.
The projective-line cohomology computation and Kunneth formula give

    H1(O_Y(n-2,-n-2))
      = H0(P1_X,O(n-2)) tensor H1(P1_Z,O(-n-2)),
    H1(O_Y(n,-n))
      = H0(P1_X,O(n)) tensor H1(P1_Z,O(-n)).               (10)

Both dimensions are (n-1)(n+1). These formulas hold over every field;
see Stacks [30.8.1](https://stacks.math.columbia.edu/tag/01XS) and
[33.29.1](https://stacks.math.columbia.edu/tag/0BEC).

Here is the matrix of the induced H1 map, without a choice of divided
powers or a duality normalization. On the standard z-chart, represent
H1(O(-m)) by Laurent monomials z^-1,...,z^(-(m-1)). The source basis
in (10) is

    x^j z^(-(L+1)),     0<=j<=n-2,  0<=L<=n,

and the target basis is

    x^k z^(-(r+1)),     0<=k<=n,    0<=r<n-1.

Multiplication by u+vz+wz^2 sends a tuple of polynomials lambda_L
to the tuple

    u lambda_r+v lambda_(r+1)+w lambda_(r+2).

Indeed, multiplication by z^s contributes to target exponent -(r+1)
exactly when L=r+s. Laurent terms outside the target range represent
Cech coboundaries; the surviving x polynomials include all degrees
0,...,n. Therefore the matrix is exactly T_n, with entry

    T_n[(r,k),(L,j)] = [x^(k-j)] c_(L-r),
       c_0=u, c_1=v, c_2=w, c_s=0 otherwise.              (11)

The long exact sequence of (9) now identifies its kernel with H0(C,L^n).
There are no binomial coefficients, factorials, derivatives, or divisions
by two in this identification. In particular it applies unchanged in
characteristic two and when one of the three polynomials is zero.

The same defining sequence at n=1 is

    0 -> O_Y(-1,-3) -> O_Y(1,-1) -> L -> 0.

The middle H0 and the first H1 vanish, since both H0 and H1 of
O_P1(-1) vanish. Hence

    H0(C,L)=0.                                            (12)

Since the trivial bundle has the nonzero constant section, L is
nontrivial. This argument does not require any geometric restriction
on C beyond F being a nonzero (2,2) section.

Two more ambient consequences will be useful. The sequence

    0 -> O_Y(-2,-2) -> O_Y -> O_C -> 0

gives H0(C,O_C)=K and h1(C,O_C)=1. These statements persist under every
field extension by the same computation. Also

    chi(O_C(p,q))
      = (p+1)(q+1)-(p-1)(q-1)=2p+2q.                    (13)

The formula chi(O_Y(p,q))=(p+1)(q+1) for all integers p,q follows
directly from (10) and the line cohomology formula. In particular C has
arithmetic genus one and L has degree zero. Degree is understood as
chi(M)-chi(O_C), as in Stacks [33.44](https://stacks.math.columbia.edu/tag/0AYQ).

## 3. Why the singular boundary still has a section criterion

Work first over an algebraic closure k of K. The forms U,V,W have no
common geometric zero: finite common zeros are excluded by the Bezout
identity for gcd(u,v,w)=1; at X0=0 at least one coefficient of degree
two is nonzero. Therefore C_k has no vertical component.

It has no horizontal component either. A geometric constant z-root
has a minimal polynomial over K of degree at most two (using the
homogeneous version at infinity). Degree one contradicts (1). In degree
two that polynomial divides F in z and exhausts its z-degree, forcing
F=A(X)B(Z). Then all nonzero members of u,v,w have a common factor and
their primitive degree is zero, a contradiction. This argument also
allows inseparable degree-two extensions.

Every geometric irreducible component therefore has positive degree
in both directions. Since the total bidegree is (2,2), exactly one of
the following holds:

1. C_k is integral of bidegree (2,2).
2. C_k is the reduced union of two distinct (1,1) curves.
3. C_k=2D for one (1,1) curve D.

A (1,1) curve with no vertical or horizontal component is the graph
of an invertible linear fractional transformation, so is a smooth P1.
In the second case the two components meet: restricting one equation
to the other's P1 gives a nonzero section of O_P1(2), whose zero
scheme has length two. Thus the reduced curve is connected. The
restriction of L to each (1,1) component is O_P1(0). In the first
case L has degree zero by (13).

For any proper integral curve, a nonzero section of a degree-zero
invertible sheaf has no zeros and trivializes the sheaf: its zero
divisor is effective and has degree zero, hence is empty. This is
Stacks [33.44.12](https://stacks.math.columbia.edu/tag/0AYQ), and it
does not require a smooth curve. For a reduced union as in case 2,
a section restricts to either zero or a nowhere-vanishing section on
each component. A nonzero restriction on one component forces a
nonzero restriction on the other at their intersection. It therefore
generates at every point and trivializes the bundle. Since the curve
is reduced, a nonzero section has a nonzero restriction somewhere.

For case 3 put I=I_D/I_D^2, the ideal of D in 2D. Then

    I^2=0,        I=O_D(-D)=O_P1(-2),
    L|D=O_D.

For each integer n the restriction sequence is

    0 -> O_P1(-2) -> L^n -> O_D -> 0.                    (14)

As H0(O_P1(-2))=0, a nonzero global section of L^n has nonzero
constant restriction to D. It generates L^n at every point by
Nakayama's lemma for the nilpotent ideal I, and again trivializes it.

In all three cases H0(C_k,L_k^n) is therefore zero unless L_k^n is
trivial, and in the trivial case it has dimension one. Cohomology
commutes with field extension (Stacks [30.5.2](https://stacks.math.columbia.edu/tag/02KH)).
If L_k^n is trivial, this gives a nonzero K-section of L^n. Its base
extension trivializes L_k^n by the preceding argument, so the section
already trivializes L^n by faithful flatness. Conversely, a trivial
bundle stays trivial. Thus geometric and K-triviality agree for these
actual line bundles, and (5) holds over K. No assertion that all
Galois-invariant geometric Picard classes descend is needed.

To deduce (6), use the prior structural dichotomy at primitive degree
two. It gives mu1 in {0,a-1,a}; condition (1) excludes mu1=0.
Since mu1+mu2=2a, the alternatives are (a-1,a+1) and (a,a).
The prior full-endpoint rank formula then gives respectively
a^2+2a-1 and a^2+2a. Its nullity formula identifies these alternatives
with nullity C_(a-1)=1 and 0. This finishes Theorem A, including the
original common-gcd case, because the prior formula proves that
dividing the common gcd leaves the full source kernel unchanged.

## 4. Singular curves over F2

We next bound the possible order of L over F2. The preceding geometric
classification covers all cases allowed by (1).

First suppose C is geometrically reduced and geometrically singular. Over k, its
normalization is one P1 in the integral case, or two P1's in the
reducible case. In the integral singular case this follows from
arithmetic genus one: the normalization sequence subtracts a positive
singularity contribution from h1, so the normalized genus is zero.
A smooth projective genus-zero curve over an algebraically closed
field is P1 (Riemann--Roch at a point gives a degree-one parameter).

Here is a precise description sufficient to control the line bundle.
The normalization factors into gluings of two points and contractions
of a tangent direction, by Stacks [53.15.4](https://stacks.math.columbia.edu/tag/0C1L).
For such a factorization, a gluing between distinct connected
components changes h0 but neither h1 nor the Picard kernel. A gluing
within one connected component increases h1 by one and contributes
the group G_m; a contracted tangent direction increases h1 by one
and contributes G_a. The exact unit sequences are given in
[53.15.5](https://stacks.math.columbia.edu/tag/0C1M) and
[53.15.6](https://stacks.math.columbia.edu/tag/0C1N); the corresponding
cohomology changes are recorded in the proof of
[53.17.3](https://stacks.math.columbia.edu/tag/0C20).

The normalized components have h1=0 and C_k has h1=1. Hence exactly
one step contributes a positive-dimensional Picard kernel. The group
of geometric line bundles of degree zero on every component is
therefore G_m(k) or G_a(k). This is an algebraic-group identification:
the parameters are respectively the ratio of fiber identifications
in a point gluing, and the additive first-order gluing parameter in
the unit sequence. It is not merely an abstract group isomorphism.

The class L_k belongs to this group. In the additive case every
nonzero class has order two. In the multiplicative case the F2 descent
acts on a geometric parameter as t -> t^2 or t -> t^(-2). Indeed,
after removing coefficient Frobenius the action is an algebraic-group
automorphism of G_m, hence t -> t or t -> t^-1. These are the only
possibilities because the units of k[t,t^-1] are c t^m, and preserving
the identity and having an inverse force c=1 and m=+1 or -1.
A fixed nonidentity parameter consequently satisfies t^3=1; in the
untwisted case the only fixed parameter is 1. Since L is defined over
F2 and nontrivial, its order in every reduced singular case is two
or three. This includes conjugate components and non-split nodes.

For completeness, consider C_k=2D. The square-zero unit sequence

    1 -> 1+I -> O_(2D)^* -> O_D^* -> 1

identifies 1+I with the additive sheaf I. Since constants k^* on D
lift, it gives

    ker(Pic(2D) -> Pic(D)) = H1(P1,O(-2)) = (k,+).        (15)

This is the first-order thickening sequence of Stacks
[37.4.1](https://stacks.math.columbia.edu/tag/0C6Q).
L_k lies in this kernel and is nonzero by (12), so its order is two
in characteristic two. More generally the same argument gives order
p in characteristic p, and infinite order in characteristic zero;
tensor powers correspond to adding the gluing parameter, since
(1+eta)^n=1+n eta when eta^2=0. Triviality descends as in Section 3.

## 5. Smooth curves over F2: an elementary bound of five

Suppose C is smooth and geometrically integral. The ambient computation
already gives genus one. We first show that C has an F2 point, using
the special (2,2) embedding rather than a point-count theorem.

The only nonzero homogeneous quadratic in Z over F2 with no root in
P1(F2) is

    B(Z)=Z0^2+Z0 Z1+Z1^2.

Indeed, avoiding [1:0] and [0:1] forces both endpoint coefficients
to be 1; avoiding [1:1] then forces the middle coefficient to be 1.
If C had no F2 point, each of the three x fibers would equal B:
they are nonzero by primitivity, and F2 has no nontrivial scalar.
Write

    F=X0^2 A(Z)+X0 X1 B'(Z)+X1^2 E(Z).

Evaluation at [1:0], [0:1], and [1:1] gives A=E=B'=B. This forces

    F=(X0^2+X0 X1+X1^2) B(Z),

contradicting the primitive degree-two hypothesis. Choose O in C(F2).

Riemann--Roch and duality for this smooth genus-one curve imply that
every positive-degree line bundle M has h0(M)=deg M: the dual term
has negative degree and thus no nonzero section. These statements
hold in characteristic two; see Stacks
[53.5.2](https://stacks.math.columbia.edu/tag/0B5B) and
[33.44.12](https://stacks.math.columbia.edu/tag/0AYQ).
In particular, for each degree-zero line bundle N over F2, N(O)
has a unique effective divisor of degree one, necessarily one point
P in C(F2). This proves the bijection

    Pic^0(C) <-> C(F2),        N=O_C(P-O),                (16)

where Pic^0(C) here means actual degree-zero line bundles over F2.
Injectivity follows from the same uniqueness for degree-one divisors.
No Jacobian representability or Picard descent theorem is used.

Moreover h0(O_C(O))=1 and h0(O_C(2O))=2. A nonconstant function in
the latter space has exact pole divisor 2O, so defines a finite
degree-two morphism C -> P1 over F2. The fiber over infinity contains
only O. Each of the other two F2 fibers has at most two rational
points. Thus

    #Pic^0(C)=#C(F2)<=1+2+2=5.                            (17)

This count remains valid for an inseparable map, since the scheme
length of each fiber is two. The nontrivial class L therefore has
order in {2,3,4,5}. Together with Section 4, every curve allowed by
(1) over F2 has L of order 2, 3, 4, or 5. By Theorem A its defect
can occur only if a+1 has a prime factor in {2,3,5}.

## 6. Three exact witnesses and the rank set

The converse uses three polynomials over F2, with coefficient order
u+zv+z^2w:

| n | f_n(x,z) | A nonzero tuple in ker T_n |
| --- | --- | --- |
| 2 | x^2+z^2 | (0,1,0) |
| 3 | x^2+xz+z^2 | (0,1,x,0) |
| 5 | x^2+z+(x+x^2)z^2 | (1+x^2+x^3, x^2, x^3, x^2, x+x^2+x^3, 1+x^2) |

Each triple is primitive of degree two. None has a fixed F2 root:
u, w, and u+v+w are all nonzero polynomials, which checks the three
points of P1(F2). Every displayed coordinate has degree at most n-2.
Substitution in all n-1 equations of (3) gives zero coefficient by
coefficient; these are exact polynomial identities in F2[x]. For the
last row the four equations use u=x^2, v=1, w=x+x^2. Thus H0(C,L^n)
is nonzero for each displayed prime n. Since H0(C,L)=0, Theorem A
shows that L has exact order n. These small T_2 and T_3 calculations
use (9)--(11) directly; they do not invoke the older source theorem
outside its allowed parameter range a>=3.

All three polynomials satisfy the source degree restriction for every
a>=3. If gcd(a+1,30)>1, choose a prime n in {2,3,5} dividing a+1.
The corresponding f_n then has rank a^2+2a-1 by Theorem A. Conversely,
the earlier balanced containment says that such a defect can arise
only at primitive degree two without a fixed root, so Sections 4--5
apply to every potential witness. This proves (7).

Finally, rank a^2 is realized by f=1 and rank a^2+a by f=1+xz,
using the prior formula at primitive degree zero and one. For a=3,
f=x^2+xz+z^2 has full active rank 15: its order is three, which does
not divide a+1=4. For each a>=4 use f=x^3+z^2. It is primitive of
degree three and has no fixed F2 root; the prior balanced dichotomy
then forces full active rank a^2+2a. These witnesses prove (8).

## 7. Evidence boundary and remaining scope

The proof of the binary all-size statement uses the geometric criterion,
the order bounds, and the three explicitly displayed polynomial
identities. It does not extrapolate a period from sampled sizes or
require an exhaustive orbit census. The package's exact finite controls
provide a separate check of the coefficient convention, these identities,
and the correspondence with the literal crossed matrix.

The saved earlier F2 negatives at a=6 and a=10 are consistent with
(7), since 7 and 11 are coprime to 30. Their finite coverage and
provenance remain separate from this proof. The same formula also
predicts no defect at a=12. No universal attainment statement over
other fields is inferred from the F2 conclusion. The all-field object
is the specific line bundle in (2), and its order over another field
must be established there.

Review status remains written and unreviewed. Neither the standard
external geometry nor the previously merged kernel-index results are
claimed as new general theorems of this package.
