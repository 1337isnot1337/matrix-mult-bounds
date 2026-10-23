# Sharp bilateral k-ruling cap by a Borel-fixed kernel

October21,2026. AI-assisted written proof, unreviewed. No historical
priority, independent review or exponent improvement is claimed.

Let F be algebraically closed and let B:U tensor V -> W be a surjective
linear map of finite dimensional spaces. Fix integers r>=1 and k>=1.
Suppose for every input subspace E of dimension at most k, on either side,
the image B(E tensor V), respectively B(U tensor E), has dimension at most r.
Then the largest possible dimension of W, allowing all finite input sizes, is

    F(r,k)=max(r, 2r-2k+1, floor(r/k)^2+2(r mod k) if r>=k^2).

The omitted third term is not used when r<k^2. The cap is attained by
explicit coordinate quotients. This is a different claim from a cap on
the nonlinear image of rank-one inputs: W means its full linear span.

## 1. Closed conditions and a projective fixed point

Put M=dim U dim V and d=dim W. The kernel K belongs to Gr(M-d,U tensor V).
For a fixed E, rank of E tensor V -> (U tensor V)/K at most r is a closed
determinantal condition on that Grassmannian. Intersect these closed sets
for every E on both sides. The resulting closed set Z is stable under
GL(U) times GL(V), and contains K. This step keeps the quotient dimension d
fixed; replacing the matrix B by an arbitrary matrix limit would not do so.

The orbit closure of K in Z is a nonempty projective variety, stable under
the product H of the two upper-triangular groups. H is smooth, connected
and solvable. The Borel fixed-point theorem gives an H-fixed kernel K0
in this closure. External input: J.S.Milne, Algebraic Groups, CUP2022,
corrected October5,2021 manuscript, Corollary17.3, printed353/PDF363
(zero-indexed), https://www.jmilne.org/math/Books/iAG2022.pdf.

The diagonal torus has distinct weights on the basis cells e_i tensor f_j,
so K0 is a coordinate span. The elementary upper-triangular transformations
imply: if (i,j) is in K0, so is every (i',j') with i'<=i and j'<=j.
Reverse both coordinate orders. The surviving quotient cells then form a
Ferrers diagram with nonincreasing row lengths lambda_1,lambda_2,... .
Its number of cells is exactly d. Zero rows/columns can be discarded.

## 2. Ruling dimensions of a Ferrers quotient

For a k-dimensional E on the row side, each surviving column receives
the coordinate projection of E onto its height-many row coordinates.
These columns have disjoint output coordinates. Hence the image dimension
is the sum over columns of these projection ranks, bounded by

    sum_columns min(k,column height) = sum_(i=1)^k lambda_i.

A generic E attains all these finitely many maxima simultaneously (a
Vandermonde generator with distinct row parameters also does). Therefore
this sum is the exact maximal row-side ruling dimension. Interchanging
rows and columns gives the other exact maximum

    sum_rows min(k,lambda_i).

If either input dimension is smaller than k, its entire image is tested
and d<=r. Otherwise pad the diagram by zero rows as needed. Our two
constraints are exactly that the first k rows and first k columns each
contain at most r cells.

## 3. Optimizing the diagram

If lambda_k=0, the total area is at most r. Suppose 1<=lambda_k<k.
Let h be the number of the first k rows whose lengths are at least k.
Every lower row has width less than k, so its entire area is counted by
the first-k-column budget. Thus

    d <= r + sum_(i=1)^h (lambda_i-k).

If h=0 this is r. Otherwise the remaining k-h top rows each have length
at least one. Their top-row budget yields

    sum_(i=1)^h(lambda_i-k) <= r-(k-h)-hk
      =r-k-h(k-1) <= r-2k+1.

Hence d<=max(r,2r-2k+1) in this case.

Finally suppose lambda_k>=k, which requires r>=k^2. Write r=kq+s,
0<=s<k, so q>=k. The top k rows have total area at most r and already
spend k^2 of the column budget. Each lower row has width at most
lambda_k<=q. Rows of width at least k spend k budget each, while all
shorter rows have area equal to their budget. The largest possible lower
area with remaining budget k(q-k)+s is at most

    (q-k)q+s.

Indeed at most q-k full-cost rows can occur; if fewer occur, replacing
one full-cost row by its k budget units at efficiency one cannot increase
area because q>=k. Adding the top budget gives d<=q^2+2s.

## 4. Exact attainment

The one-row diagram (r) attains r. When the hook value dominates r,
r>=2k-1 and the hook of width and height r-k+1 has area2r-2k+1;
its top k rows and columns each contain r cells. When r>=k^2, take
s rows of length q+1, followed by q-s rows of length q, and, if s>0,
one last row of length s. Its area is q^2+2s and both budgets are r.
If a displayed diagram has fewer than k input coordinates, the whole
image bound still holds directly; padding zeros is harmless.

This proves the formula and its sharpness. It gives11 rather than12 at
(r,k)=(7,2),18 rather than20 at(9,2),15 rather than16 at(10,3), and17
rather than19 at(11,3). The concurrent generic-ruling bound and its
special k=2 improvement remain credited; this draft uses a separate
Grassmannian compression argument. The application to scalar Hankel
symbols still requires the uniform linear-space cap and the other
ordinary source-lift hypotheses; none is silently removed.
