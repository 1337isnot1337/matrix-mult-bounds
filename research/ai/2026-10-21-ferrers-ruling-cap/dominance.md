# A stronger consequence when the low-rank image lies in a closed target

October21,2026. AI-assisted written proof, unreviewed; characteristic zero.
No historical priority, independent review or exponent improvement claimed.

Let B:U tensor V -> W be surjective, and let X be any closed cone in W
whose contained linear spaces all have dimension at most r. Suppose

    B({matrices of rank at most k}) is contained in X.

Every k-input ruling is a linear space in X and therefore has dimension
at most r. The preceding Borel-fixed-kernel argument applies. In addition,
either the rank-k image of B is dense in W, or its Ferrers limit must
have Durfee number at least k+1.

Indeed, dominance of the polynomial map

    (A,C) -> B(A*C), A in Mat_(dim U,k), C in Mat_(k,dim V),

is open in B: in characteristic zero it is equivalent to a nonzero
full-dimensional Jacobian minor for at least one (A,C). To justify this
standard criterion, polynomial coordinate functions are algebraically
independent exactly when their differentials are independent over the
rational-function field. One direction differentiates a minimal relation;
the other extends the functions to a transcendence basis and uses
separability of the resulting algebraic field extension in characteristic
zero. Equivalently
at least one coefficient of such a minor is nonzero, an open condition
on B. Locally trivialize the Grassmannian quotient to formulate it for
kernels; it is independent of the chosen quotient basis. It is invariant
under input basis changes. Thus dominance at a point of the orbit closure
forces dominance on the original orbit. This openness step would not
follow merely by assuming an image variety had constant dimension.

For a Ferrers diagram with Durfee number h<=k, a generic assignment to
all its cells has a rank-h completion. Its leading h-by-h square is
generically invertible; every diagram cell is in the first h rows or
first h columns. Fill the remaining unspecified entries in these rows
and columns arbitrarily, and use the Schur-complement formula to fill
the bottom-right block. The result has rank h and realizes every specified
entry on that dense open set. Therefore the rank-k coordinate projection
is dominant. The zero diagram is immediate.

If B itself is dominant on rank-k matrices, closedness puts W inside X,
so dim W<=r. Otherwise the Ferrers diagram has h>=k+1. Then its first
k rows each have at least k+1 cells, forcing r>=k(k+1). The third case
of the Ferrers optimization gives, with r=kq+s,0<=s<k,

    dim W<=q^2+2s.

Consequently the general bound improves to

    dim W<=r                       if r<k(k+1),
    dim W<=floor(r/k)^2+2(r mod k)   if r>=k(k+1).

In the first case the argument actually proves the whole image W is in X.
This extends saturation using the maximal dimension of contained linear
spaces, rather than the dimension of X. No sharpness is claimed for every
case with a prescribed closed X.

The intermediate dichotomy is sharp for abstract bilinear quotients:
either their rank-k image is dominant, or r>=k(k+1) and d<=q^2+2s.
The square-extension diagram from the first proof attains this latter
bound whenever r>=k(k+1). Its Durfee number is at least k+1, so its full
leading(k+1)-square supplies a nonzero minor vanishing on the projected
rank-k image, which therefore is not dominant. This sharpness statement
assumes the bilateral ruling caps; it does not assert that the same
diagram's image cone has no larger contained linear spaces.

Closedness of X is essential to the dominance step. The three-coordinate
hook projection of rank-one2-by2 matrices has image
{(a,b,c):a!=0} union {(0,b,c):bc=0}, a dense proper cone in F3. Its missing
point(0,1,1) prevents replacing closedness by mere density.

For scalar Hankel rank<=r, the uniform Wronskian cap supplies the needed
linear-space hypothesis. This gives cap r at(r,k)=(5,2),(8,3),(9,3),
(10,3),(11,3). The currently used dimension-saturation threshold alone
does not give all those cases. The generic k-ruling formula remains
credited to the concurrent rectangular worker; the stronger fixed-point
and dominance argument is a separate continuation.
