# Exact slice covers for intermediate shared weights

October 20, 2026. AI-derived written proof, unreviewed. No smaller matrix
multiplication exponent is established. This extends Section 7 of
`arbitrary_shared_basis.md` and retains its constant-matrix grading scope.

Write D=m-1 and N=m(m+1)/2. Apply arbitrary constant matrices P,Q,G to
C(m,B), followed by the weights

    w(X_i)=beta*i,
    w(Y_(a,b))=alpha*(a+b)-beta*a,
    w(Z_(c,d))=alpha*(c+d)-beta*c-alpha*D.

There are k copies of each triangular Y/Z coordinate set. Suppose the
resulting limit is the canonical T_(m,k). The target is concise, so P,Q
have rank kN and G is invertible. For every nonzero shared source slice,
polynomial multiplication is injective on its B-dimensional input. Thus
the X_0 slice M_0 of the constant transformed tensor satisfies

    rank(M_0) >= 2*k*N-B-D.                              (1)

This is the same ordinary rank-loss inequality used in the earlier notes;
it is applied before the diagonal degeneration, not to its limiting slice.

## 1. A family of exact covers

Assume alpha>0 and put w(a,b)=(alpha-beta)*a+alpha*b. Define

    n(t)=#{(a,b): a,b>=0, a+b<=D, w(a,b)>t}.

For any real threshold t, a valid row/column cover of M_0 has size

    k*R(t), where
    R(t)=n(t)+n(alpha*D-t)+1_{t/alpha is an integer in [0,D]}.   (2)

Consequently every certificate in this grading class requires

    B >= k*(2*N-R(t))-D.                                (3)

To prove the cover, select all Y rows of weight greater than t and all Z
columns of weight greater than alpha*D-t. Every strictly positive-weight
entry is covered. An uncovered zero-weight target entry must have a=c=0,
b+d=D, alpha*b=t, and alpha*d=alpha*D-t. If such an integer b exists, add
the k rows indexed by (0,b), one per copy. These cover every remaining
allowed entry. All negative-weight entries and all other zero-weight entries
must be zero. This proves (2); a matrix covered by R rows and columns has
rank at most R, proving (3) from (1).

The program minimizes this explicit family of covers over all breakpoints
and intervening intervals. It does not claim to optimize all conceivable
rank obstructions. For integer weights the calculation is exact.

## 2. A continuous asymptotic obstruction

Suppose beta<=alpha<=2*beta and beta>0, and put r=alpha/beta. At the
symmetric threshold t=alpha*D/2, the triangular region counted by n(t)
has area r*D^2/8. More explicitly, its vertical height at coordinate a is

    max(0,D/2-a/r),   0<=a<=D.

The number of integer b in each column is at most that height plus one.
For this decreasing height function, its sum over integer a is at most
its integral plus D/2. There are at most r*D/2+1 nonempty columns. Hence

    n(alpha*D/2) <= r*D^2/8 + (1+r)*D/2 + 1.

Equations (2)-(3) give the uniform finite estimate

    B >= k*(2*N-r*D^2/4-(1+r)*D-3)-D.                (4)

In particular, along any unbounded sequence with limsup(alpha/beta)<=r_0
in [1,2], including arbitrary positive copy counts,

    liminf B/(k*N) >= 2-r_0/2.                       (5)

Thus this class cannot meet the conditional growth threshold
rho_c=9/(7*cuberoot(2)) if

    limsup(alpha/beta) < 4-2*rho_c = 1.9590557904... .

This closes most of the interval between the earlier small-slope region
and the balanced direction. It does not exclude slopes tending to 2 or
larger intermediate slopes. The formula is a source-cost obstruction;
it is not a new value of the matrix multiplication exponent.

## 3. The balanced direction and the replicated four-block target

For (alpha,beta)=(2,1), the cover has the particularly useful exact value

    R(t)=N-floor(m/2)                                (6)

at t=D when D is odd, and t=D-1 when D is even and positive. Both choices
are odd integers, so the extra boundary row in (2) is absent.

Indeed the involution (a,b)->(a,D-a-b) takes weight a+2*b to 2*D-(a+2*b).
If D=2h-1, the central level D has h points, so the two strict tails have
total N-h. If D=2h, the levels D-1,D,D+1 have respectively h,h+1,h points.
The tails beyond D-1 and D+1 have total N-h. This proves (6), including
m=2. Therefore

    B >= k*(N+floor(m/2))-D.                         (7)

At m=4 this becomes B>=12*k-3. In particular C(4,10*k) cannot give the
canonical T_(4,k) by this ansatz for any k>=2. This closes the previously
selected k>=53 finite-profile target in the balanced direction. The
single-copy case k=1 is not excluded by (7). The normalized overhead in
(7) tends to one as m grows, so it does not close the all-dimension premise.

Reversing each degree sector's binary coefficients sends
(alpha,beta) to (alpha-beta,-beta). Thus the concurrent (1,-1) direction
is equivalent to (2,1) and has the same limitation. No arbitrary shared
Laurent family is excluded here.

## Verification boundary

`weight_slice_covers.py` uses rational thresholds and integer counts.
Independent tests assemble the allowed support, check every covered edge,
and compare with a separately implemented bipartite maximum matching on
small cases. Exact lattice counts check the balanced formula and the
uniform estimate above. The retained report includes the finite m=4,k=53
cost calculation. These checks validate the code and stated finite cases;
the all-size conclusions depend on the written proof and remain unreviewed.
