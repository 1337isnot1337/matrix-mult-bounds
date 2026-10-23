# Can the costs of two moving variables be added?

October 23, 2026. Discovery question, with a separate written exact
family calculation. The general inequality below is **unproved**.
No matrix target or smaller exponent is claimed.

Retain the hypotheses and primitive degrees from proof.md. In the case
epsilon_x=epsilon_z=1, the proved source-rank lower bound is

    rank M_F >= ab*r+max(a(a-r),b(b-r)).

**Conjecture, degree-one case only.** If both primitive degrees equal
one, then

    rank M_F >= ab*r+a(a-r)+b(b-r).                       (C)

The current coefficient-map proof gives a maximum, not a sum. No step
in the maintained proof assumes (C). The finite pilot does not prove it,
nor does an exact family attaining its proposed boundary prove it.

## An exact balanced boundary family

For n>=3, set a=b=n and r=n-1. Take only

    f_(r-1)=1,     f_(2r-1)=xz,

with all other long-coordinate polynomials zero. The scalar Hankel
rank is r: its leading r-by-r moment matrix is an invertible
antidiagonal matrix, and f_(k+r)=xz*f_k for every available shift.
The supporting form is V^r-xz U^r, with both primitive degrees one.

The full source slice has rank

    rank M_F = n^2*r+2n.                                  (1)

This is exactly the proposed additive boundary in this subfamily. Here
is a direct coefficient-rank calculation. The constant term at moment
r-1 has r nonzero block positions p+q=r-1, 0<=p,q<n. Each block is R(1),
with entries H=j,L=t, and rank n^2. The xz term has only the two block
positions (p,q)=(r-1,r),(r,r-1), with entries H=j+1,L=t+1. Since r>=2,
the two components touched by xz are distinct in the bipartite graph of
block rows and block columns.

In the component with block row r-1 and block columns 0,r, the matrix
is [R(1) R(xz)]. Its row count gains exactly n independent rows beyond
rank R(1): the new rows are L=n, with n choices of j. All other
nonzero rows have L<n and their R(1) coordinates already form independent
pivots. Thus this component has rank n^2+n. In the transposed incidence
component, the stacked matrix [R(1);R(xz)] has rank n^2+n, with new
independent columns H=n. Each of the remaining r-2 components has rank
n^2. Their total is r*n^2+2n, proving (1).

This family calculation does not assert the corresponding equality for
r<n-1, nor establish the conjectured universal lower bound (C).

## Completed finite pilot

The pilot covers the forty ordered parameter choices

    n=3,...,6; r=2,...,n-1;
    kind in {separated,mixed}; seed in {0,r-1}.

Set f_seed=1, the other initial f_0,...,f_(r-1) to zero, and recursively
define f_(k+r)=sum_(j=0)^(r-2) c_j*f_(k+j). The coefficients are

    c_0=x+z                  for separated,
    c_0=1+xz                 for mixed,
    c_j=(j+1)x+(j-1)z        for 1<=j<=r-2.

All source degree bounds are checked, the actual scalar symbol rank is
r, and the reconstructed primitive degrees are (1,1). Exact rational
source ranks violate (C) in zero of these forty cases. The smallest
observed gap is zero. These are a declared recurrence class and two
initial conditions, not an exhaustive search over complex slices or
supporting forms. `additive_pilot.py` regenerates the compact saved
records and can replay the ranks. The all-rank theorem in proof.md does
not depend on this pilot.
