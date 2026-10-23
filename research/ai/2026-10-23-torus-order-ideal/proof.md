# A sharp dimension bound below source rank 64

October 23, 2026. Owner-directed AI-derived research over C. This is a
written, computer-assisted proof with exact finite certificates. It is
not formally verified and has no independent external mathematical
review. No target degeneration or exponent improvement is claimed.

## 1. Statements, source, and prior inputs

For the canonical cyclic source A4, write

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),                 (1)

where the short indices i,j,p,q,r,s are in {0,1,2,3}, and H,L are in
{0,...,6}. An out-of-range source coefficient is zero. Thus M is a
112-by-112 matrix, linear in the 112 coordinates F_(i,k,s), with
0<=i,s<=3 and 0<=k<=6. Formula (1) comes from the literal product

    X_i Y_j Z_(i+j), Y_p Z_q X_(p+q), Z_r X_s Y_(r+s).

The new conclusions are:

**Theorem 1.** If V is a complex linear source-parameter space and
rank M(F)<64 for every F in V, then dim V<=32. This dimension bound is
sharp: the full coordinate space with k in {0,1} has dimension 32 and
every one of its slices has rank at most 56.

**Theorem 2.** Suppose a complete Laurent degeneration has the form

    B(t) M(F(t)(X)) C(t) = X tensor I_11 + O(t),
    X in Mat_10(C),                                         (2)

where B has shape 110-by-112, C has shape 112-by-110, and F(t) is linear
in X. Independently multiply B,C by scalar powers of t to make each
regular with nonzero constant coefficient, compensating in F. If
b=rank B(0) and c=rank C(0) after this balancing, then b+c<=160.

Theorem 2 is a necessary condition at every Laurent pole order. Its
bound is not asserted to be sharp. In particular, Theorem 1's example
is a source space, not a pair of long maps realizing (2).

The literal source and ordinary restriction obstruction are credited
to the pinned [cyclic finite-target note](../2026-10-20-koszul/cyclic_finite_target.md).
The source torus and earlier dimension bounds are in the
[rank-48 frontier proof](../2026-10-23-torus-rank-frontier/proof.md),
which proves b+c<=176. The target-support argument is credited to the
[saturated-lattice note](../2026-10-20-graded-quantum-flags/saturation.md).
PR122 first combined that argument with bounded-rank cancellation
kernels to obtain b+c<=192. This package adds an order-ideal reduction,
an exhaustive rank-64 certificate, sharp dimension 32, and sum 160.
Exact source versions are in sources.json. No external theorem is
imported to justify the new order-ideal reduction.

## 2. Literal rank-preserving lowering operators

Let e_(i,k,s) denote the coordinate basis of the source space. Define
three nilpotent linear operators, with a zero value at a lower boundary:

    D_i e_(i,k,s) = i e_(i-1,k,s)                  if i>0;
    D_k e_(i,k,s) = (7-k) e_(i,k-1,s)             if k>0;
    D_s e_(i,k,s) = s e_(i,k,s-1)                 if s>0.     (3)

The coefficient 7-k in the middle direction is essential. It is not
the coefficient k from the other two directions. Directly from (1),
for every row (j,p,L) and column (H,q,r),

    M(D_i F)_((j,p,L),(H,q,r))
      = (H+1) M(F)_((j,p,L),(H+1,q,r))
        - j M(F)_((j-1,p,L),(H,q,r));

    M(D_k F)_((j,p,L),(H,q,r))
      = (3-p) M(F)_((j,p+1,L),(H,q,r))
        + (3-q) M(F)_((j,p,L),(H,q+1,r));

    M(D_s F)_((j,p,L),(H,q,r))
      = (L+1) M(F)_((j,p,L+1),(H,q,r))
        - r M(F)_((j,p,L),(H,q,r-1)).                    (4)

Matrix entries outside the row or column ranges are zero. For example,
the first right side has the same coefficient F_(H-j+1,p+q,L-r) in
both terms, with total scalar H-j+1. When H-j=-1 these terms cancel;
when the coefficient is outside its upper range they both vanish.
The same check handles the other boundaries. In the middle identity
the scalar is 6-p-q, exactly the coefficient induced by D_k in (3).

For each D in (3), equation (4) has the form

    M(D F) = L_D M(F) + M(F) R_D,                         (5)

with fixed nilpotent row and column matrices L_D,R_D. The two actions
on the right commute. Exponentiating this intertwining identity gives

    M(exp(u D) F) = exp(u L_D) M(F) exp(u R_D).             (6)

All exponentials are finite polynomial sums over C and are invertible.
Thus exp(uD) preserves source slice rank for every complex u. This is
a literal matrix identity, not an assumed change of source model.
The verifier checks (4) on all 112 basis vectors in each of the three
directions, as sparse integer matrices, including all boundary terms.

We also use the previously credited torus

    T(z) e_(i,k,s) = z^(i+4k+28s) e_(i,k,s), z!=0.         (7)

It is rank-preserving: the row weight -j+4p+28L and column weight
H+4q-28r add to the parameter weight in (7). The 112 parameter weights
are the distinct integers 0,...,111. The three operators D_i,D_k,D_s
decrease this weight by 1,4,28 respectively.

## 3. A reusable order-ideal reduction

We prove a general elementary lemma before applying it to A4.

**Lowering lemma.** Let E have a coordinate basis with distinct integer
weights for a one-parameter torus T. Let M:E->Mat_(a,b)(C) be linear.
Suppose T preserves rank M, and suppose nilpotent operators D_alpha
have the following two properties:

1. Every exp(u D_alpha) preserves rank M.
2. Each D_alpha is homogeneous of weight -lambda_alpha with
   lambda_alpha>0.

If a d-dimensional linear space V satisfies rank M(v)<=R for every
v in V, then there is a coordinate d-plane W with the same rank bound
and D_alpha W contained in W for every alpha. If every nonzero
D_alpha e_x is a nonzero multiple of a designated lower neighbor of
e_x, the support of W is closed under all those lower neighbors.

**Proof.** Let G_(d,R) be the subset of the Grassmannian Gr(d,E) whose
planes satisfy the rank bound identically. It is closed. To see this
in a standard Grassmann chart, write the chart's basis matrix for a
plane and a general vector in that plane as a linear combination with
independent scalar variables x_1,...,x_d. Every (R+1)-minor of M of
that vector is a polynomial in the x variables. The plane lies in
G_(d,R) exactly when every coefficient of every such polynomial is
zero. These coefficients are polynomial in the chart parameters,
so they give closed conditions in every chart. The stated rank
invariances make G_(d,R) invariant under T and each exp(uD_alpha).

There is at least one coordinate plane in G_(d,R). Indeed, choose a
basis of V in echelon form for increasing source weight. Apply T(z)
and divide each basis vector by the power belonging to its leading
coordinate. As z tends to zero, the vectors tend to distinct coordinate
vectors. The limiting d-plane lies in G_(d,R), either by closedness
or by specializing the vanishing minors of each linear combination.

There are only finitely many coordinate d-planes. Choose one W in
G_(d,R) for which the sum w of its coordinate weights is minimal.
Let omega be the wedge of its coordinate basis vectors. It is a
nonzero Plucker vector of weight w.

Suppose D=D_alpha does not preserve W. Then exp(uD) omega is a finite
polynomial in u with a nonzero coefficient of positive degree. Here is
an explicit check in the lower-neighbor case used below. Choose a
coordinate in W whose lower neighbor is absent from W. In the first
derivative of the wedge, its replacement by that neighbor has a
nonzero coefficient. No other replacement gives the same wedge:
the missing original coordinate and the added coordinate determine
that replacement. Hence it cannot cancel. More generally the same
conclusion follows by taking the induced map W->E/W in a basis.

Write J>0 for the largest nonzero degree and omega_J for its coefficient.
As u tends to infinity, u^(-J) exp(uD) omega tends to omega_J. Its
projective point therefore belongs to G_(d,R). In particular omega_J
is decomposable and nonzero. Homogeneity of D makes omega_J a torus
eigenvector of weight w-J lambda_alpha, which is strictly smaller
than w.

Although distinct Plucker coordinates can have the same total weight,
that does not cause a gap here. The Plucker line of omega_J is torus
invariant, so its underlying d-plane W_J is torus invariant: it is
the space of vectors v for which v wedge omega_J=0. A torus-invariant
subspace of E is a sum of its weight spaces, and these weight spaces
are one-dimensional because the original coordinate weights are
distinct. Thus W_J is a coordinate d-plane. Its weight sum is
w-J lambda_alpha, contradicting the choice of W. Every D_alpha
therefore preserves W. The final support assertion follows from
the nonzero lower-neighbor coefficients. This proves the lemma.

For A4, (3), (6), and (7) meet the hypotheses. Every coefficient of a
permitted downward move is nonzero over C. Consequently every bounded-
rank source space has a coordinate limiting space of the same dimension
whose support is a downward order ideal in

    {0,1,2,3} x {0,1,2,3,4,5,6} x {0,1,2,3},            (8)

with the coordinatewise order on (i,k,s). This assertion is reusable
for every rank threshold; the next section specializes it to rank 63.

The geometric argument is over C. In particular the coefficients in
(3) and the factorials in the exponentials are not interpreted modulo
two. Only the separate integer minors below are checked modulo two.

## 4. Rank 64 witnesses for all size-33 order ideals

A single source coordinate e_(i,k,s) is a partial permutation matrix
of rank

    16 times (1,2,3,4,3,2,1)_k.                           (9)

This follows directly from the 4096 literal terms, or from the
Hankel-block factorization in the prior rank-48 proof. In particular,
middle coordinate k=3 already has rank 64. An order ideal with any
point at k>=3 contains a point at k=3. Thus an order ideal whose every
slice has rank below 64 must lie in the smaller box

    {0,1,2,3} x {0,1,2} x {0,1,2,3}.                    (10)

If this ideal has at least 33 points, it contains an order ideal of
exactly 33 points. To obtain one, repeatedly remove a maximal point.
Removing a maximal point preserves downward closure and decreases
the size by one. This reduces the desired exclusion to a finite,
complete list of size-33 ideals in (10).

Encode each ideal by three four-entry height rows h[k][i], where its
points above (i,k) are exactly s=0,...,h[k][i]-1. The conditions are

    0<=h[k][i]<=4;
    h[k][i]>=h[k][i+1];
    h[k][i]>=h[k+1][i];
    sum_(k,i) h[k][i]=33.                                (11)

There are exactly 611 such arrays. Discovery enumerates the 70
nonincreasing four-entry rows with entries in {0,...,4}, and then
all coordinatewise nested triples of total size 33. Acceptance uses
a separate recursive enumeration of the twelve heights in (k,i)
order. Each height ranges from zero to the minimum of four and its
already assigned neighbors. It retains exactly total size 33. Every
array in (11) has one branch in this recursion, and no array outside
(11) survives. Its only additional pruning uses the loose remaining
capacity bound of four per unfilled cell, so it cannot remove an
admissible array.

For each of these 611 arrays, the saved certificates.json gives:

- A subset of its source coordinates, all with coefficient one; all
  other source coefficients are zero.
- A set of 64 matrix rows and a set of 64 matrix columns.

Each selected minor has determinant 1 modulo two. All matrix entries
are the literal integers zero or one. Therefore its integer determinant
is odd and is nonzero over C. The chosen source point belongs to the
coordinate space of its ideal and has complex matrix rank at least 64.

The masks use index n of the lexicographic list of (i,k,s) in (10) for
source coordinates. Matrix indices are

    row(j,p,L)=(4j+p)*7+L;
    column(H,q,r)=(4H+q)*4+r.                             (12)

A set bit selects the corresponding index. The verifier rejects
noncanonical or oversized masks, supports outside the stated ideal,
minors of the wrong size, duplicate ideals, missing ideals, or singular
minors. It builds source slices from the original six-index product,
not from discovery's direct matrix-entry formula. It uses fixed
low-column elimination on each saved 64-by-64 minor, not discovery's
highest-bit pivot search on the full matrix. It does not call discovery
or regenerate random choices while accepting the certificate.

This proves the finite exclusion for every size-33 ideal. The lowering
lemma and the trimming argument prove dim V<=32 for every complex
linear space V with rank M(V)<64.

To attain dimension 32, take all coordinates (i,k,s) with k in {0,1}.
Every nonzero entry of its slices has p+q<=1, so p is zero or one.
There are only 4*2*7=56 possible nonzero rows. Every slice therefore has
rank at most 56, strictly below 64. The 32 parameters are independent,
which proves sharpness in Theorem 1.

## 5. Apply the bound to arbitrary Laurent long maps

Retain the notation of (2), after scalar balancing. Put

    K = {F : B(0) M(F) C(0)=0}, h=dim K,
    delta=224-b-c.                                       (13)

Two-sided compression loses at most (112-b)+(112-c) ranks. Therefore
every slice from K has rank at most delta. For delta<64, Theorem 1 gives

    h<=32.                                               (14)

We recall why the prior saturated-support inequality applies even
when F has arbitrary poles. Let S(t) be the 112-row first flattening
of the projected source, rho=rank S(0)=112-h, and L its row space over
C((t)). Its dimension d is at most 112. The saturated lattice

    Lambda = L intersect C[[t]]^(110*110)

has rank d, and its reduction L_0 embeds into the residue space with
dimension d. Indeed, a lattice vector divisible by t in the ambient
space remains in this lattice after division by t. The constant row
space W_0 of S(0) lies in L_0 and has dimension rho.

Every row of the regular product F(t)S(t) is also in Lambda. Thus the
100-dimensional target slice space Z={X tensor I_11} lies in L_0,
and dim(Z intersect W_0)>=100+rho-112=rho-12.

If a parameter space E of matrices X maps into that intersection,
let p,q be the dimensions of its joint column and row supports. The
joint supports of X tensor I_11 have dimensions 11p,11q. Those supports
fit in the leading long-map supports of dimensions b,c, so

    dim E<=p*q<=floor(b/11)*floor(c/11).

Combining these inequalities gives the credited necessary condition

    h >= 100-floor(b/11)*floor(c/11).                     (15)

The [preceding frontier proof](../2026-10-23-torus-rank-frontier/proof.md)
already excludes b+c>176, using (15), source-space caps 0,16,24 at
strict rank thresholds 16,32,48, and the ordinary restriction obstruction.
Those arguments are not new here and their exact proof is pinned.

It remains to exclude 161<=b+c<=176. In this interval 48<=delta<=63,
so (14) gives h<=32. On the other hand,

    floor(b/11)+floor(c/11)<=floor(176/11)=16.

The largest product of two nonnegative integers with sum at most 16
is 8*8=64. Equation (15) then gives h>=36, a contradiction. This proves
b+c<=160 and Theorem 2. The total deficiency relative to the two
110-dimensional target legs must therefore be at least 220-160=60.

Every Laurent pair can be scalar-balanced independently, with the
inverse scalar product absorbed in F. This does not require a pole
bound or a prescribed higher-order jet. At the boundary b+c=160,
delta=64; Theorem 1 has a strict rank threshold and supplies no cap
there. No candidate at that boundary is asserted to exist.

## 6. Exact coverage, status, and scope

The maintained verifier checks all 4096 literal terms, all 12544 matrix
positions, all 112 monomial slices, and all 336 lowering identities.
It independently enumerates the 611 size-33 ideals and replays all
611 integer minor certificates. It also checks the sharpness plane
and all 12321 pairs of integer ranks 0<=b,c<=110. The necessary
conditions exclude all 1830 pairs with sum above 160, including 840
new pairs with sums 161 through 176. The rank-64 boundary stays open.

The certificates prove a finite statement; the written geometric
argument supplies the universal quantifier over complex subspaces.
Neither component alone is the whole theorem. Tests include deliberate
corruption of the certificate inventory, source pins, supports, minors,
and scope, so acceptance is not just the discovery program rerun.

Internal agent audits checked the lowering formulas, geometric argument,
ideal inventory, and minors independently during development. They do
not constitute independent external mathematical review or formal proof
verification. The repository claim status remains written-unreviewed.
No historical source files are modified. No matrix multiplication
exponent bound is improved by these necessary obstructions alone.
