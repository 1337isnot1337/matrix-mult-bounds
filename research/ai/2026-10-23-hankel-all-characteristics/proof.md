# The Hankel Segre bound in every characteristic

October 23, 2026. Owner-directed Codex research. This is a written,
unreviewed extension of the existing characteristic-zero proof, with
same-session checking only. It is not an independent mathematical review,
a formalization, a tensor construction, or an improved exponent.

The prior [linear-annihilator proof](../2026-10-21-hankel-pencil-degree/proof.md)
proves the same numerical bound in characteristic zero. Its use of a
symmetric-square map with a diagonal coefficient two prevents that proof
from being used unchanged in characteristic two. Here a divided-square
map retains the diagonal equations and removes that restriction. The
annihilator, pencil, and dimension arguments retain their prior credit.
The source versions and exact hashes are recorded in [sources.json](sources.json).

## 1. Statement and geometric hypothesis

Let K be any field, let U,V be finite-dimensional K-vector spaces, and set

    1 <= r < min(a,b),       5r < 2(a+b),
    d=a+b-2,                t=3r-(a+b-1),
    k=max(1,floor((t+3)/2)), B=max(r,k^2).

Write S_j=K[x,y]_j. Regard a sequence h=(h_0,...,h_d) as the
functional on S_d taking x^(d-j)y^j to h_j. Its Hankel matrix is

    H(h)=(h_(p+q))_(0<=p<a, 0<=q<b).

**Theorem.** Let Phi:U tensor V -> S_d^* be K-linear. Assume every
(r+1)-minor of H(Phi(u tensor v)) is the zero polynomial in the
coordinates of u and v. Then

    dim_K im Phi <= B.                                      (1)

Equivalently, the rank is at most r for every decomposable input after
extension to an algebraic closure of K. Over an infinite K it suffices
to check all K-rational decomposable inputs, by polynomial identity.
Over a finite K that implication is not assumed: a finite pointwise
rank check alone is not the hypothesis of this theorem without a field-size
condition. If K=F_q with q>=r+1, checking every K-rational decomposable
input does suffice, by the elementary interpolation argument below.

Matrix rank, and hence dim im Phi, is unchanged by extending the field.
The polynomial-minor hypothesis also survives extension. We therefore
prove the result over an algebraically closed field F, of arbitrary
characteristic. In particular F is infinite.

**Finite-field interpolation.** A homogeneous polynomial of degree e<=q
over F_q is determined by its values on all rational vectors. For e<q,
every individual variable degree is below q, and successive univariate
interpolation proves the assertion. For e=q, a polynomial vanishing at
all vectors has zero coefficient on each pure power x_i^q, by evaluation
at the coordinate unit vectors. All remaining individual degrees are
below q, so the same interpolation applies. The degree-zero case is
immediate. Each Hankel minor is bihomogeneous of degree r+1 in each of
the two inputs. Fixing one input and applying the lemma to the other,
then applying it to the resulting coefficient polynomials, proves the
claimed implication when q>=r+1. All rational decomposable inputs must
be checked; sampling is not sufficient. The polynomial x^q*y-x*y^q
shows that degree q+1 is too large for this general interpolation lemma.
It is not claimed to be a counterexample to the Hankel rank bound or
to prove that the field-size threshold for that bound is sharp.

## 2. Scalar annihilators and pencil degree

We record the characteristic-free ingredients of the prior proof.
Suppose a nonzero sequence h has Hankel rank s<min(a,b). Its left
kernel L_h lies in S_(a-1), has dimension a-s, and satisfies

    h(L_h S_(b-1))=0.

Let q be the homogeneous gcd of L_h, of degree c. Since
L_h is contained in q S_(a-1-c), one has c<=s. The polynomial
multiplication fact proved in
[the earlier scalar argument, Section 1](../2026-10-20-anisotropic-constructions/hankel_symbol_dimension.md)
gives

    L_h S_(b-1)=q S_(d-c).

For completeness, that fact uses only the following algebra. For a
basepoint-free p-dimensional subspace W of binary degree-j forms,
development modulo a degree-j member gives a (p-1)-dimensional
subspace of F[z]/(f). Multiplying successively by z increases its
span until the full quotient is reached; otherwise it would be a
proper z-stable ideal containing generators with gcd one. Hence
W S_e=S_(j+e) for e>=j-p+1. No differentiation or characteristic
assumption occurs.

The functional h consequently factors through a length-c subscheme
of P^1, and its Hankel pairing has rank at most c. Thus c=s.
The left and right kernels are exactly

    q S_(a-1-s),             q S_(b-1-s),                    (2)

because these subspaces lie in the kernels and have the required
dimensions. In particular q is the unique minimal homogeneous
annihilator, up to a scalar. These statements include support at
infinity and nonreduced support. When local coordinates are used,
"jets" mean coefficients in F[z]/((z-z_0)^e), equivalently Hasse
coefficients, not ordinary derivatives divided by factorials.

Now take a Hankel pencil H_0+tau H_1 of generic rank s. Formula (2)
holds over F(tau): one may take the gcd of a kernel basis over this
field, or descend the unique annihilator from its algebraic closure.
Clear denominators and choose q(tau;x,y) primitive over F[tau]. Set
D=deg_tau q. Gauss's lemma shows that its monomial multiples form
the entire polynomial right kernel module. Multiplication by the
nonzero leading tau coefficient of q is injective, so every nonzero
multiple q f has tau degree D+deg_tau f. The b-s right minimal
indices and the a-s left minimal indices are therefore all D.

The arbitrary-field index sum lemma of De Teran--Dopico--Mackey,
Lemma 6.3, gives

    (a+b-2s) D <= s.                                        (3)

Its omitted finite and infinite structural indices are nonnegative.
Since s<=r and 5r<2(a+b), the quotient s/(a+b-2s) is less than two.
Consequently D<=1. The external lemma's field hypothesis was checked
in the pinned primary source; it is not a characteristic-zero result.

## 3. Linear spaces and the correct quadratic assignment equations

Let L be a linear subspace of the Hankel rank-at-most-r cone, with
generic rank s>0. Its minimal annihilator defines a rational map
P(L) -> P(S_s). After removing the gcd from homogeneous coordinates,
the base locus has codimension at least two. A general projective
line avoids it, and the coordinate degree on that line is the degree
of the rational map's homogeneous representation. Section 2 bounds
that degree by one. If dim L=1 the map is constant directly.

A constant annihilator puts L in one fixed length-s scheme span.
In the moving case it is represented by a linear map Q:L -> S_s.
Write

    im Q=g W,    deg g=c,    dim W=p>=2,

where W is a basepoint-free subspace of S_(s-c). Let S_g denote the
c-dimensional subspace of S_d^* annihilating g S_(d-c), with S_g=0
when c=0. A generic pair of forms in im Q has gcd g. Their degree-d
ideals sum to g S_(d-c), since d>=2s; this is also immediate from
the principal syzygy of the two coprime residual binary forms.
Their scheme spans therefore intersect in S_g.

For l_0 in ker Q, the generic line l+tau l_0 has constant annihilator
Q(l). It follows that l_0 lies in every generic scheme span and hence
in S_g. Thus

    dim L <= p+c.                                          (4)

After choosing a section of Q, the family modulo S_g gives a linear
assignment A:W -> S_d^*/S_g satisfying

    A(w)(g w f)=0   for all w in W and f in S_(d-s).          (5)

Restriction to g S_(d-c) identifies S_d^*/S_g with S_(d-c)^*.
For a basis w_i of W, condition (5) is exactly the following set of
coefficient identities:

    A(w_i)(w_i f)=0                               for every i,
    A(w_i)(w_j f)+A(w_j)(w_i f)=0                 for i<j.   (6)

The diagonal conditions are retained explicitly. In characteristic
two they do not follow by substituting i=j into the mixed equation.
The equivalence with (5) follows by expanding the quadratic polynomial
in the coordinates of w over the infinite field F.

## 4. Divided squares and the assignment dimension

For a vector bundle T define its divided square here by the swap
invariants

    Gamma^2 T = (T tensor T)^(swap).

In a local basis e_i it has basis e_i tensor e_i and
 e_i tensor e_j+e_j tensor e_i (i<j). This is a locally free bundle
in every characteristic; it is not defined by quotienting out
antisymmetric tensors. Write gamma_2(e_i) for the diagonal basis
vector and e_i odot e_j for the mixed one.

Put e=d-s and let E be the evaluation kernel:

    0 -> E -> W tensor O -> O(s-c) -> 0.

Restrict id tensor ev to the swap-invariant tensors and twist by O(e).
This gives the exact sequence

    0 -> Gamma^2 E(e) -> Gamma^2 W tensor O(e)
      -> W tensor O(d-c) -> 0.                              (7)

The map sends gamma_2(w_i) to w_i tensor ev(w_i), and
w_i odot w_j to w_i tensor ev(w_j)+w_j tensor ev(w_i).
To check exactness, split the evaluation map locally as E direct sum
O(s-c). A local generator l of the quotient has
 gamma_2(l) mapping to l tensor ev(l), with coefficient one, and
u odot l maps to u tensor ev(l) for u in E. These vectors span the
codomain, and the remaining kernel is exactly Gamma^2 E. This works
in characteristic two as well as all other characteristics.

Pairing a linear assignment with the map on global sections of (7)
gives precisely the diagonal and mixed equations (6). Hence the
assignment space is the dual of its cokernel on global sections.
Since e>=0, H^1(O(e))=0. The splitting theorem for vector bundles on
P^1, valid over every field, writes

    E = direct sum_(i=1)^(p-1) O(-mu_i),
    mu_i>=1,                 sum mu_i=s-c.                 (8)

Indeed H^0(E)=0 because the forms of W are independent. The divided
square of this direct sum has one line-bundle summand of degree
-mu_i-mu_j for each i<=j. The Laurent-monomial calculation of
H^1(O(n)) gives the assignment-space dimension

    alpha = sum_(i<=j) max(mu_i+mu_j-e-1,0).                (9)

Thus the numerical formula is the same as in the prior
characteristic-zero proof, but (7) supplies its valid all-characteristic
justification. No division by two or polarization-only argument is used.

A moving generic-rank-s family needs alpha>0: otherwise its values
would all lie in S_g and have Hankel rank at most c<s. Therefore
2 mu_max>=e+2. Since mu_max<=s-c-p+2, equations (4) and (8) imply

    2(p+c)<=3s-d+2,
    dim L<=floor((3s-d+2)/2).                               (10)

For the original rank parameter r, this last bound is at most k.
Every linear subspace of the rank-at-most-r cone with dimension
at least k+1 therefore lies in one fixed scheme span.

## 5. The Segre image bound

Initially suppose the generic Hankel rank of Phi(u tensor v) is r.
Let u_0 and v_0 denote the maximum dimensions of the two families
of rulings, Phi(U tensor v) and Phi(u tensor V), respectively.
If both are at most k, choose u_0 vectors of U whose images span
one generic first ruling. They also span that ruling for generic v,
by the nonvanishing of a suitable minor. The complete image is then
contained in the sum of their u_0 second rulings, a space of dimension
at most u_0 v_0<=k^2. The containment extends by density.

Otherwise exchange U and V so the generic second ruling has dimension
at least k+1. Section 4 puts each such ruling in a fixed length-r
scheme span, with annihilator q(u). If q(u) is constant, the entire
image has dimension at most r.

If q(u) varies, choose a generic v. The linear family Phi(U tensor v)
has generic rank r and annihilator q(u). Section 3 represents this
annihilator by a linear map Q:U -> S_r; write im Q=g W, with deg g=c
and dim W=p. For l in ker Q, the constant-annihilator line argument
puts Phi(l tensor v) in S_g for generic v, hence for every v. A section
of Q now assigns to each v a permitted assignment from Section 4.
The span of all assignment values has dimension at most p alpha;
adding S_g gives

    dim im Phi <= c+p alpha.                               (11)

Here alpha is (9), with s=r. Set ell=p+c and retain
 t=3r-d-1 and k=max(1,floor((t+3)/2)). Since a,b>=r+1,
 t<=r-1. Every mixed term i<j in (9) vanishes: its two mu entries
sum to at most r-c, whereas e+1=2r-t>r. At most one diagonal term
can be positive, since two positive terms would also make the sum
of their two mu entries exceed 2r-t. Consequently

    alpha <= t-2ell+4.

In the moving case alpha>=1, so 2<=ell<=k and k>=2. Since
 t+4<=2k+2, equation (11) gives

    c+p alpha <= ell alpha <= 2ell(k+1-ell) <= k^2,

where the last inequality follows from

    k^2-2ell(k+1-ell)=(k-ell)^2+ell(ell-2)>=0.

If the generic rank is some s<r, apply the argument with s. Its
hypothesis follows from 5s<2(a+b), and both s and its corresponding
k are no larger than the original ones. The zero-rank case is
immediate. This proves (1), and field extension gives the assertion
over the original K.

## 6. Ordinary cyclic-source consequence

The existing polynomial source inequality is already proved over any
field. For A(a,b), with N=ab(a+b-1), write its slice as

    M_F[(j,p,L),(H,q,r')]=F_(H-j,p+q,L-r'),
    f_k(x,z)=sum_(i<a,s<b) F_(i,k,s) x^i z^s.

The two full polynomial-multiplication injections in
[polynomial_rank_locus.md](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
give

    rank M_F >= ab rank_(K(x,z)) (f_(p+q)).                 (12)

Suppose ordinary linear maps over any K take A(a,b) to a concise
target containing a rectangular matrix block M(l,h,n). Let k_Y,k_Z
be the kernel dimensions of the two maps opposite its lh-dimensional
parameter leg. Conciseness makes each dual leg map injective. A lifted
rank-one block parameter has source rank at most

    n+k_Y+k_Z.                                             (13)

This elementary compression inequality remains true after any field
extension, since the tensor restriction is an identity of coefficients.
If (13) is less than (r+1)ab, equation (12) bounds its polynomial
Hankel-symbol rank by r. Over an algebraic closure of K, all relevant
minors vanish on every decomposable parameter; thus their coefficients
are polynomial identities and remain zero over the algebraic closure
of K(x,z). The theorem bounds the K(x,z)-span of these symbols by B.

Choose at most B sequence coordinates whose projection is injective
on that rational-function span. Projection onto the corresponding
biform coefficients is then a K-linear injection of the whole
lh-dimensional lifted block parameter space into B copies of a space
of dimension ab. Therefore

    lh>Bab  implies  n+k_Y+k_Z >= (r+1)ab.                  (14)

The same statement holds on each cyclic leg. For a square direct-sum
target of total leg dimension D, every block M_n consequently satisfies

    n^2>Bab  implies  n+2(N-D) >= (r+1)ab.

This extends the field scope of an ordinary-map necessary condition.
It does not apply the source-lift rank estimate to arbitrary singular
Laurent approximations. It constructs no target, supplies no new
characteristic-zero numerical cap, makes no claim of historical
priority, and establishes no smaller matrix multiplication exponent.

## 7. Verification boundary

The all-size result rests on the written argument. Finite checks of
assignment equations, characteristic-two controls, and source identities
can detect implementation mistakes and exhibit why the diagonal
conditions matter; they do not prove the theorem or change its review
status. The historical characteristic-zero proof and reports remain
unchanged. The inherited proof steps and external statements are
identified individually in sources.json.
