# Explicit staircase source spaces and a rank-96 counterexample

October 23, 2026. Owner-directed AI-derived work. Written proof,
unreviewed externally, with exact finite controls. This constructs
bounded-rank source spaces, not a matrix multiplication degeneration.

## 1. Construction at every source size

For the canonical cyclic source A_a, put N=a^2(2a-1). Its source slice
matrix has entries

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),              (1)

where 0<=i,j,p,q,r,s<a and 0<=H,L<=2a-2. Coefficients outside these
ranges are zero. The source coordinates are (i,k,s), with k=p+q.
The formula and source attribution are pinned in sources.json.

Choose integers 1<=d<=a-1 and 0<=m<=2a-1. Let V_(a,d,m) be the
coordinate parameter space supported on

    i<d, with arbitrary k,s;
    or i=d, 0<=k<m, with arbitrary s.                    (2)

This is a downward order ideal. Its coordinate vectors are independent,
so

    dim V_(a,d,m) = a[d(2a-1)+m].                        (3)

Every matrix from this space has its nonzero columns in exactly the
following joint column support:

    0<=H<=a+d-2, with arbitrary q,r;
    or H=a+d-1, 0<=q<min(m,a), with arbitrary r.          (4)

To prove containment, coordinates i<d have H=i+j<=a+d-2. The added
coordinates i=d can introduce only one larger H, namely a+d-1. Their
middle coordinate obeys p+q<m, which implies q<m.

Conversely, each column in the first group occurs in a literal term:
write H=i+j with 0<=i<d, 0<=j<a, choose p=0 and s=0, and keep the
specified q,r. Such a decomposition exists throughout the stated H
interval. Each column in the second group occurs with i=d, j=a-1,
p=0, s=0. Thus (4) is the exact union of the column supports of the
basis slices, not only an overestimate.

It follows that every F in V_(a,d,m) satisfies

    rank M(F) <= a^2(a+d-1)+a min(m,a).                  (5)

This is a uniform rank upper bound from common column support. It
does not claim that any particular slice attains that upper bound.
The proof uses only the literal source and is valid over C (indeed
over any field). The finite checker below does not supply the all-size
quantifier; equations (2)-(5) do.

## 2. The proposed rank-96 cap is false

At a=4 and d=2, equations (3)-(5) give:

| m | Source-space dimension | Supported columns / uniform rank upper bound |
| --- | ---: | ---: |
| 0 | 56 | 80 |
| 1 | 60 | 84 |
| 2 | 64 | 88 |
| 3 | 68 | 92 |

In the final row, the 68 coordinates are all i=0,1 with arbitrary
k=0,...,6 and s=0,...,3, together with i=2, k=0,1,2 and arbitrary s.
Its supported columns are H=0,...,4 with all q,r (80 columns), plus
H=5, q=0,1,2 with all r (12 columns). Every slice therefore has rank
at most 92, strictly below 96.

Consequently the assertion that every complex A4 source space of
rank below 96 has dimension at most 57 is false. In fact any universal
dimension cap at that threshold must be at least 68. The same family
gives the four lower controls in the table at their stated weak rank
ceilings.

At m=4 the common support has 96 columns. Column counting alone no
longer proves rank below 96. The checker retains this boundary control
and does not turn it into an assertion of attained rank 96.

## 3. Which proposed research route this rules out

The preceding [rank-80 package](../2026-10-23-torus-rank80/proof.md)
proves the necessary balanced long-rank sum b+c<=144 for the A4 to
Mat_10 tensor I_11 Laurent problem. Its constant cancellation kernel K
obeys the two credited necessary conditions

    rank M(K) <= delta=224-b-c;
    dim K >= 100-floor(b/11)*floor(c/11).                 (6)

For sums 129 through 144, delta<=95 and the product of the two floors
is at most 6*7=42, so (6) requires dim K>=58. A proposed continuation
was to show that every source space of rank below 96 has dimension
at most 57, then apply that cap to K. The explicit 68-space disproves
that proposed premise.

This does not block every source-cap refinement. Smaller rank intervals,
more information about the actual two-sided compression kernel, or a
stronger compatible target-support inequality can still give additional
necessary conditions. The displayed spaces are not asserted to be
cancellation kernels of long maps satisfying the target equations.
They neither construct such maps nor disprove their existence.

## 4. Exact controls and scope

The standalone checker reconstructs the literal six-index source for
a=2,...,6. It checks all 140 permitted (a,d,m) triples in that range,
their parameter dimensions, and their exact joint column supports.
It separately replays the saved 68-coordinate A4 mask and the four
table rows, with the m=4 boundary kept distinct. Tests corrupt the
mask, support budget, scope, and source pins.

The all-size supported-column construction is the new result. The
rank-96 counterexample is its immediate specialization. No source-space
maximum, complete target construction, improved rank frontier, independent
external review, formalization, or exponent improvement is claimed.
