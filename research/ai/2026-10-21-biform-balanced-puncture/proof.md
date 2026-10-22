# Complete cancellation under balanced boundary punctures

October 21, 2026. Owner-directed Codex work; written and unreviewed.
No matrix multiplication construction, independent review, formalization,
historical priority, or exponent improvement is claimed.

## 1. The full auxiliary matrix action forces product kernels

Let U,V be finite-dimensional spaces over a field, let E,F have the same
positive dimension d, and let Z be a nonzero subspace of U tensor V with
no nonzero matrix of rank one. Suppose quotient maps on U tensor E and
V tensor F have kernels K_U,K_V, each of dimension d. Then

    the quotients kill Z tensor E tensor F

if and only if there are lines u in U and v in V such that

    K_U = u tensor E,   K_V = v tensor F,
    Z is contained in u tensor V + U tensor v.                 (1)

Here a matrix in U tensor V is a linear map V* to U. The statement is
about killing the entire matrix space, not bounding its surviving dimension
by one or two. The latter cases require a separate argument.

To prove necessity, choose any nonzero M in Z and identify F* with E.
The matrix M tensor I_d has rank d rank(M). Two quotient kernels of
dimensions d can lose at most 2d ranks. Complete cancellation therefore
forces rank(M)<=2, hence rank(M)=2. Write U_0=im M and V_0=row M.
Both are two-dimensional. Equality in the rank loss forces

    K_U subset U_0 tensor E,   K_V subset V_0 tensor F.

Indeed restricting M tensor I_d to the annihilator of K_V leaves rank
at least d; its image is contained in the d-dimensional K_U, so that
image equals K_U. Transposing gives the other containment.

Let W be the annihilator of K_V inside V_0* tensor F*. It has dimension d
and (M tensor I_d)W=K_U. Complete cancellation also says
(M tensor X)W is contained in K_U for every linear X:F*->E. Consequently
K_U is stable under I_(U_0) tensor End(E). Such invariant subspaces are
L tensor E: apply elementary matrix units to each auxiliary coordinate
to recover every coordinate vector in the subspace. Since dim K_U=d,
L is a line. The transposed argument gives K_V=v tensor F.
Applying the quotient maps to every M' tensor matrix unit now says
that M' vanishes after quotienting U by u and V by v. This is exactly
the last containment in (1). Sufficiency follows by direct substitution.

This proof uses the complete auxiliary matrix space. It makes no
inference from a finite collection of sampled quotient subspaces.

## 2. The biform multiplication kernel has an explicit cancellation space

Work over C. Put

    U=H^0(P1 x P1,O(1,2)),  V=H^0(P1 x P1,O(2,1)),
    S=ker(U tensor V -> H^0(O(3,3))).

Multiplication has no nonzero decomposable vector in its kernel because
the bihomogeneous polynomial ring is an integral domain. Thus S has no
nonzero rank-one matrix. For nonzero u in U,v in V put g=gcd(u,v), and
write u=g u', v=g v', with coprime u',v'. Let (i,j) be the bidegree of g.
The common bounds on the two degrees give 0<=i,j<=1.

The intersection

    S intersect (u tensor V + U tensor v)

consists exactly of the matrices

    M_h=(u' h) tensor v - u tensor (v' h),
    h in H^0(O(i,j)).                                      (2)

Indeed a representation a tensor v + u tensor b lies in S precisely
when a v+u b=0. Unique factorization and coprimality give a=u'h,
b=-v'h. The representation map has the one-dimensional kernel h=Cg,
so the intersection dimension is

    (i+1)(j+1)-1 <= 3.                                     (3)

If its dimension is at least two, necessarily (i,j)=(1,1). Conversely,
for any nonzero g of bidegree (1,1), any nonzero l_y of degree (0,1),
and any nonzero l_x of degree (1,0), set u=g l_y,v=g l_x. Formula (2)
then gives a three-dimensional matrix space, every nonzero member of
which has rank two. To see the rank assertion, a nonzero class of h
modulo Cg makes u'h,u and v,v'h independent on their respective sides;
(2) consequently has rank exactly two.

## 3. Consequence for the actual third normal tensor

The earlier biform package proves, coefficient by coefficient, that the
actual third normal matrix space is Mat2 tensor Z_D, where Z_D is the
span of its four six-by-six core slices. It proves that a non-plane D
has dim Z_D>=2 and Z_D subset S. These are adopted statements, with their
original proof status and source hashes retained in sources.json.

If deleting two dimensions on each twelve-dimensional boundary leg kills
this entire space, Section 1 forces both kernels to be the auxiliary
two-dimensional factors of two base lines u,v. Section 2 then forces

    u=g l_y,  v=g l_x,  deg g=(1,1),
    2 <= dim Z_D <= 3,

and every core slice is of the explicit form (2). In particular any actual
normal with dim Z_D=4 cannot be completely killed by balanced punctures.
No arbitrary-subspace search is needed for this implication.

This conclusion addresses complete cancellation only. The matrix-target
argument also permits projected first rank one or two; those possibilities
are not excluded here. Nor does a zero third block establish compatibility
of later coefficients, full row ranks, or the required matrix slice space.

## 4. Complete incidence classification on one affine chart

Use the actual monomial bases

    U=(1,x,y,xy,y^2,xy^2), V=(1,x,x^2,y,xy,x^2y).

Fix the open chart in which the constant coefficients of g,l_x,l_y
are nonzero. Scale them to one and write

    g=1+c x+d y+e xy, l_x=1+a x, l_y=1+b y.

Then a non-plane actual normal D with complete balanced cancellation
exists at these base lines **if and only if**

    c+d=0, e+d^2=0.                                      (4)

At every point of (4), the non-plane normal solution space has dimension
exactly two. Thus the common factor must be

    g=(1+c x)(1-c y),

whereas a,b,c are arbitrary complex numbers. This is an exact
three-parameter family of puncture choices, with a two-dimensional normal
fiber. It is not inferred from the coordinate discovery grid.

Here is a finite polynomial certificate for the complete assertion, with
no excluded denominator. The coefficient map of the four core slices
has rank 24. Its parameters split into two identical twelve-dimensional
copies, supported on source pairs (0,2) and (1,3). Let P be the 72-by-12
coefficient matrix of the first pair and T a full-rank 60-by-72
annihilator, so TP=0. Both matrices and their ranks are exported.

Since the constant coefficient of g is one, each h modulo Cg has a
unique representative in span(x,y,xy). Let G be the 36-by-3 map (2)
on this basis. The incidence condition for one source pair is

    H z=0, H=T diag(G,G), z in C^6.

The five-by-five minor of H at rows (1,2,25,27,28) and columns
(0,1,2,3,5), with zero-based indexing, is identically one. Consequently
every kernel vector is a scalar multiple of

    z=(0,0,-1,-1,1,2c+d).

Put R=Hz. Every entry of R belongs to the ideal generated by c+d and
d^2+e. Conversely two exported rows R_i,R_j satisfy

    R_i=-(c+d),
    R_j=-(d^2+e)-(a+2c-d)(c+d).

Thus R=0 is equivalent to (4), and the kernel is exactly one-dimensional
there and zero-dimensional elsewhere. The certificate checks these
polynomial identities directly. The second identical source pair gives
the asserted two-dimensional normal fiber. Adding the inherited four
plane parameters gives six in the original 28-dimensional normal space.

On (4), the two first-pair slices are M_(-xy) and M_(-x+y+cxy).
Their flattened two-by-two minor at positions 6 and 18 is -1. Thus their
span has dimension exactly two at every a,b,c. The complete four slices
are lambda*M_(-xy), mu*M_(-xy), lambda*M_(-x+y+cxy),
mu*M_(-x+y+cxy). Their first rank is exactly two whenever
(lambda,mu)!=(0,0). All their auxiliary products vanish under the
product kernels from Section 1.

The chart excludes zero constant coefficients in any of g,l_x,l_y.
No assertion about all other projective charts is made here. Complete
cancellation is still only a third-block necessary condition. Later
coefficients, singular leading flags and projected first ranks one and
two remain separate questions; this family is not an improving target.

## 5. Complete projective classification

The missing projective cases in Section 4 can be closed with constant
unit minors as well. Write a general shared factor as

    g=g00*x0*y0+g10*x1*y0+g01*x0*y1+g11*x1*y1.

**Theorem.** For arbitrary nonzero g,l_x,l_y, a non-plane actual normal
with complete balanced cancellation at the associated two product kernels
exists if and only if

    g10+g01=0,  g00*g11+g10^2=0.                           (5)

At every incident point the non-plane normal fiber has dimension exactly
two, and every nonzero such normal has core first rank exactly two.
There is no exceptional fiber of dimension three or greater. The four
plane directions can be added independently in the original normal space.

Projectively, (5) is the conic

    g=(r*x0+s*x1)(r*y0-s*y1),  [r:s] in P1.                (6)

Indeed if g00 is nonzero, normalize it to one and use (4). If g00=0,
(5) forces g10=g01=0, so g is a nonzero multiple of x1*y1. This is the
r=0 point of (6). There are no other points. The residual linear forms
l_x,l_y are arbitrary nonzero forms of degrees (1,0),(0,1).

Here is the complete certificate cover. Normalize the first nonzero
coefficient of g, in the displayed order (00,10,01,11), to one. In affine
x,y notation this gives four disjoint cases:

    1+c*x+d*y+e*x*y;  x+d*y+e*x*y;  y+e*x*y;  x*y.

Independently, the pair l_x,l_y has four disjoint cases:

    (1+a*x,1+b*y); (x,1+b*y); (1+a*x,y); (x,y).

The sixteen products cover all nonzero projective triples. In each case
discard the h monomial whose coefficient in g has been normalized to one.
The other three h monomials give unique representatives modulo Cg.
Build the same 60-by-6 matrix H as in Section 4. The exported report
records a minor of determinant +1 or -1 for every case, never an inverse
of a variable coefficient.

| First nonzero g coefficient | Four residual-form cases |
| --- | --- |
| g00 | A five-by-five unit minor; the residual ideal is exactly (c+d,d^2+e) in each case. |
| g10 | Three five-by-five unit minors with a constant nonzero linear combination of residuals; one six-by-six unit minor. All four cases are empty. |
| g01 | A six-by-six unit minor in each case. All four cases are empty. |
| g11 | A five-by-five unit minor in each case, with identically zero residuals. |

For every g00 case the report exports two reverse ideal identities,
as in Section 4. For each empty five-minor case it exports two residual
rows whose sum or difference is +1 or -1. Thus the asserted zero loci
follow from explicit polynomial identities; no generic-rank inference,
uncertified ideal radical, numerical tolerance, or omitted root is used.
The six-minor cases are injective immediately.

In every incident case the one-dimensional source-pair kernel reconstructs
an actual twelve-parameter normal, using a fixed inverse of the constant
coefficient matrix P. Two identical copies give exactly two non-plane
normal parameters. The verifier checks all 144 core coefficients of both
reconstructed basis normals. To certify that the resulting two core
slices are independent at every parameter value, append their h vectors
to g in the four-dimensional biform space H^0(O(1,1)). The report's h
vectors give a three-by-three minor equal to +1 or -1 in every incident
case. Their classes modulo Cg are therefore independent. The injectivity
in (2) proves that their matrix images are independent as well.

For g00 cases, the classes are -xy and -x+y+cxy. For g11 cases, they
are -x+y and 1. This also proves the first-rank assertion throughout the
projective boundary, including the r=0 point of (6).

This theorem closes only **complete third-block cancellation**. It does
not decide projected first rank one or two, compatibility of fourth and
later coefficients, full long-leg ranks, or an actual matrix target.

## Attribution and proof boundary

The source tensor, canonical flags, normal parameter space, biform bases,
full auxiliary factorization, rank-one-free property and minimum core
rank are inherited from the earlier boundary and biform packages. The
known two-parameter integrable shear remains a positive control and does
not provide a matrix target. The product-kernel argument, its application
to complete balanced cancellation, and the explicit three-dimensional
syzygy classification are the present deductions. The uses of elementary
matrix units and unique factorization are standard algebra, supplied
above rather than imported as unpublished theorems.

The exponent remains 9/4. All local mathematical claims remain written
and unreviewed regardless of successful tests or repository integration.
