# The invertible coefficient stratum of the quadratic rank-fourteen locus

October 25, 2026. Claim `AI-QUADRATIC-INVERTIBLE-STRATUM-001` is
**proof-written-unreviewed**. This is owner-directed Codex work, with a
separate same-session algebra audit, not independent mathematical review.
Exact checks corroborate the calculations; they do not replace this proof.

## Statement and scope

Let K have characteristic different from two and three. For a coefficient
matrix M in Mat_3(K), use the literal fifteen-by-fifteen source

    R(M)[(j,L),(H,r)] = M[H-j,L-r],
    0<=j,r<=2, 0<=L,H<=4,

with row pairs (j,L) and column pairs (H,r) in lexicographic order, and
out-of-range coefficients zero. Let W be a K-linear coefficient space such
that det R vanishes identically on W. If W contains an invertible coefficient
matrix after scalar extension to Kbar, then **dim W<=4**.

Equivalently, every geometric source-rank-at-most-fourteen family of dimension
at least five has identically singular coefficient matrices in these
characteristics. This does not imply a common kernel: singular coefficient
spaces also include the five-dimensional space of matrices supported in the
first row and first column. No sharpness example for the new cap four is
supplied. Characteristics two and three and the sharp maximum inside the
invertible coefficient stratum remain open here. No compatible three-leg
tensor map or exponent improvement is obtained.

Geometric vanishing means the source rank cap holds after algebraic closure.
Checking just the rational points over a finite field is insufficient. Over
an infinite K, a rank cap on every K-point implies this polynomial vanishing.

## 1. Pinned reduction and tangent ranks

All imported local formulas are pinned in [sources.json](sources.json).
The determinant proof, Section 8, makes the invertible linear coordinate
change M=P N P^t over k=Kbar, with P^t J P=-2I and J the binary-quadratic
discriminant matrix. It gives

    Delta(M)=4096 Delta0(N),
    Delta0(N)=det(2 adj(N^t N)-tr(adj(N^t N)) I),
    2048 det R(M)=det(M) Delta(M).

The coordinate change preserves dimension and coefficient invertibility.
Extend scalars and choose a five-space through an invertible member if a
larger counterexample exists. Continue to call this normalized five-space W.
Its coordinate ring k[W] is a polynomial ring and hence a domain. Since
det(N) is not the zero polynomial, Delta0 vanishes identically on W.

At an invertible N put Q=(N^t N)^(-1). A local defining function is

    Phi(N)=det(2Q-tr(Q) I),
    Delta0(N)=det(N^t N)^3 Phi(N).

The multiplier is a unit. The pinned equality proof establishes that Phi has
a nonzero differential at every invertible zero and that Q admits an
orthogonal block decomposition

    Q=diag(mu,B),  B=B^t in Mat_2(k),
    tr B=mu !=0,  d=det B !=0.

No diagonalization of B is assumed. The parent tangent calculation uses
(NN^t)^(-1); apply it to N^t. Transposition is an invertible linear map on
perturbations, while the two Gram inverses are similar. It therefore gives
the same rank statements for this right-Gram convention.

The tangent hyperplane has dimension eight. Its quadratic term splits into
a four-variable form and a four-variable form with the scalar direction in
its radical. In the parent's notation the first form has an invertible
two-by-two block and Schur complement K/d, where

    K=(3mu^2-d)B-2mu*d I,  det K=d*(d^2+3mu^4).

The second form, restricted to tracefree matrices, has a coefficient matrix
T_C after multiplication by mu, with

    det T_C=12mu^2*d*(mu^2-d).

Thus, in characteristic other than two and three, the full tangent rank is
seven whenever (d-mu^2)(d^2+3mu^4) is nonzero. This is a generic rank
statement; the parent characteristic-seven rank-five example is retained.

Every direction in W belongs to the tangent hyperplane, and the quadratic
term vanishes identically on W. Polarization makes W a totally isotropic
five-space. An eight-by-eight symmetric matrix vanishing on a five-by-five
principal block has rank at most six: its remaining three rows and columns
give two matrices of rank at most three. Therefore at each invertible point

    (d-mu^2)(d^2+3mu^4)=0.

## 2. A constant ratio forces a rank-one norm

The invariant rational function

    rho=d/mu^2=8 det(Q)/tr(Q)^3

on the nonempty invertible open subset of W satisfies
(rho-1)(rho^2+3)=0. In the function field k(W), this polynomial splits into
linear factors over k, and a product can be zero only if one factor is zero.
Hence rho is a constant. It is nonzero, and rho!=-1 because the critical
polynomial at -1 is -8, nonzero in odd characteristic.

Write p=det N and q=tr(N^t N). The characteristic coefficients of Q give

    tr Q=2mu,  s2(Q)=(1+rho)mu^2,  det Q=rho*mu^3,
    q=(1+rho)/(rho*mu),  p^2=1/(rho*mu^3).

Consequently the following is a polynomial identity on W:

    p^2 = [rho^2/(1+rho)^3] q^3.                     (1)

The constant and q are nonzero. Unique factorization in k[W] shows every
irreducible valuation of q is even, since 2 val(p)=3 val(q). As q is
homogeneous of degree two, it follows that

    q=c ell^2,  p=e ell^3,                          (2)

for a nonzero homogeneous linear form ell and nonzero constants c,e.

## 3. The determinant gradient yields a contradiction

Use the nondegenerate Frobenius pairing <A,B>=tr(A^t B) on Mat_3(k),
and let U=ker(ell|W). Polarizing (2) shows U is perpendicular to W.
Both U and W-perp have dimension four, so

    W-perp=U, in particular W-perp is contained in W. (3)

At an invertible N in W, q is nonzero. Differentiating (2) in every
direction in W shows that

    V=grad p-(3p/q)N=p N^(-t)-(3p/q)N

is perpendicular to W. Indeed <N,A>=c ell(N)ell(A) and
dp_N(A)=3e ell(N)^2 ell(A). By (3), V belongs to U. The line N+tV
therefore stays in W with unchanged ell-value, giving p(N+tV)=p(N).
After division by p(N), every positive coefficient of det(I+tC) must vanish,
where

    C=N^(-1)V=p*(Q-3/q I).

The first two coefficients are

    tr C = p*mu*(2-7rho)/(1+rho),                    (4)
    s2(C)=p^2*[s2(Q)-(6/q)tr(Q)+27/q^2].             (5)

In characteristic seven the numerator in (4) is 2p*mu, which is nonzero.
In all other allowed characteristics (4) forces rho=2/7, and then
q=9/(2mu). Substituting in (5) gives

    s2(C)=p^2*mu^2*(9/7-8/3+4/3)
         =-p^2*mu^2/21 !=0.

This is the required contradiction. Characteristic three was excluded before
the rank-seven step and before any division by three. Characteristic seven
was handled before any division by seven. Thus the theorem holds over every
field of characteristic different from two and three. The argument over
Kbar is enough because scalar extension preserves the dimension of W.

## 4. Verification boundaries and the next question

The two parent tangent determinants, the scalar identities after substituting
the normal-form invariants, the first two coefficients of det(I+tC), and the
gradient formula are checked exactly.
The verifier also checks characteristics five and 151: the trace condition
alone is compatible with the critical-ratio equation there, but (5) is
nonzero. These two finite controls prevent an incomplete trace-only argument
from being mistaken for exceptional families. They are not a census.

For a possible characteristic-three continuation there is a further necessary
condition in every odd characteristic. Let A=s2(N^tN). The invariant relation

    A^3-4q A p^2+8p^4=0

makes w=A/p integral over k[W], since w^3-4qw+8p=0 is monic. The UFD k[W]
is integrally closed: if a reduced fraction a/b satisfies a monic equation,
multiplication by b^n forces b to divide a^n, so b is a unit. Hence w is a
polynomial; homogeneity makes w linear. With h=w/2 this yields

    p=q h-h^3,  A=2p h.                             (6)

This observation uses p not identically zero. It neither bounds the dimension
in characteristic three nor constructs a family. Sharpness of the cap four,
characteristics two and three, and compatible tensor maps remain separate
questions. The normal-form and determinant packages retain their attribution;
no new external theorem or historical-priority claim is imported here.
