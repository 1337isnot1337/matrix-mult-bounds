# Proper linear sections of crossed-Hankel rank cones

October21,2026. AI-assisted written proof, unreviewed. This refines the
application of the concurrent crossed-Hankel dimension theorem. It gives
an ordinary-map obstruction, not a matrix tensor construction or exponent
gain. No historical priority, independent review, or formalization is claimed.

Work over C. Let V=Mat_(p,q) tensor S_(p+q-2)^*, with dimension
N=pq(p+q-1). For F=(F_0,...,F_(p+q-2)), form its crossed Hankel matrix,
with q block rows, p block columns and block entry F_(i+j). It is a
pq-by-pq matrix. Let X_R be its rank-at-most-R cone, with R>=1.

## 1. Every irreducible component spans the ambient coefficient space

The connected irreducible group

    GL_p times GL_q times GL2

acts on V. The two general linear groups multiply each F_k on its short
row and column factors; the GL2 factor changes the two binary variables
in the long moment coordinate. Every action preserves crossed-Hankel rank:
the short actions give invertible block row/column changes, and binary
multiplication covariance gives invertible long row/column changes.

The ambient representation V is irreducible. One elementary verification
is to use the diagonal tori to extract a nonzero individual short-matrix
unit times a long monomial from any nonzero invariant subspace. These
weights are distinct. Short elementary transformations generate every
matrix unit, and the two binary unipotent directions generate every long
monomial; their coefficients are nonzero in characteristic zero. Hence
that invariant subspace is all of V.

Let C be an irreducible component of X_R. The closure of the action image
of G times C is irreducible, lies in X_R and contains C. Maximality of C
as an irreducible closed subset therefore forces that closure to be C.
Thus C is stable under G, and its linear span is a G-invariant subspace.
Each component is nonzero: X_R is a nonzero cone, every nonzero component
contains zero by scalar closure, and {0} cannot be a maximal component.
Irreducibility of V now gives

    span C=V.                                               (1)

The group here acts on the auxiliary coefficient rank cone. It need not
preserve the original cyclic source tensor or the target parameter image;
no such symmetry reduction for tensor maps is assumed.

## 2. Every proper linear section loses at least one dimension

Let L be any proper vector subspace of V. By(1), no component C is
contained in L. Therefore C intersect L is a proper closed subset of the
irreducible variety C and has dimension at most dim C-1. Taking the finite
union over components proves

    dim(X_R intersect L) <= dim X_R-1.                       (2)

A loss equal to codim L is not asserted. The one-dimensional loss can be
sharp: for p=1,q=2 the crossed matrix is a general2-by2 matrix. Its rank-one
cone has dimension3, and its intersection with the two-dimensional subspace
having only the first row nonzero has dimension2.

The concurrent `bundle_hankel_dimension.md` proves, using its stated
classical bundle-splitting input and explicit extension count,

    dim X_R <= min(N,(p+q)R+floor((p-q)^2/4)).                (3)

Combining(2)--(3) gives the uniform bound

    dim(X_R intersect L)
      <= min(N,(p+q)R+floor((p-q)^2/4))-1.                   (4)

This is the new proper-section refinement. The imported all-rank bound,
its proof and its external sources retain their original credits.

## 3. Ordinary cyclic-source consequence

For A(a,b), identify its coefficient space with V using p=b,q=a, up to
transpose. Let G=ab and N=G(a+b-1). A concise ordinary matrix block gives
an injective first-leg map from Mat_(x,y) to V. If xy<N, its linear image
L is proper. The rank-at-most-k parameter variety has dimension

    k(x+y-k),    1<=k<=min(x,y).

Assume the maintained lower-symbol prerequisite proves generic scalar
symbol rank min(a,b) on that parameter variety. The concurrent quantitative
crossed-rank inequality then places its crossed rank at most

    R=L_source-(G-1)min(a,b).

Here L_source is the ordinary lifted source-slice upper bound. Closedness
extends the crossed-rank containment from the generic stratum to the
whole irreducible rank-k variety. Injectivity preserves its dimension.
Consequently the necessary dimension inequality strengthens to

    k(x+y-k)
      <= min(N,(a+b)R+floor((a-b)^2/4))-1,                 (5)

provided R>=1 and xy<N. With xy=N, retain the original bound without
subtracting one. The lower-symbol prerequisite is still mandatory.

For example, at A12 with an M50 block and total target dimension2546,
the rank-four lift bound is4*50+2*(3312-2546)=1732. The lower rank-eleven
alternative would, by projection saturation and the uniform linear-space
cap, inject2500 parameters into11*144=1584, so generic symbol rank is12.
The quantitative crossed bound gives R=1732-143*12=16. The prior dimension
upper bound is24*16=384, exactly the rank-four parameter dimension
4*(100-4)=384. Since2500<3312, (5) instead gives at most383, a contradiction.
This excludes that ordinary block configuration at the equality boundary.
It is not an exclusion of arbitrary singular degenerations.

## Attribution and verification limits

The finite application adopts `quantitative_crossed_rank.md` and
`bundle_hankel_dimension.md` from the concurrent rectangular integration,
pinned in sources.json. Its use of projection saturation and k-ruling
bounds is credited there as well. The component-span argument and the
resulting one-dimensional section refinement are the local continuation.
The structural proof is not inferred from finite examples. Exact small
controls protect the proper-subspace and nonzero-rank hypotheses, and the
finite screen retains every accepted inequality. No exponent improvement.
