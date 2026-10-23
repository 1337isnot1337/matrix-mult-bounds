# Exact ranks of binomial biform coefficient matrices

October23,2026. Owner-directed Codex rederivation, written and unreviewed.
No historical priority, independent review, formalization or exponent gain.

## 1. Statement over every field

Let K be any field, a>=2 and1<=u,v<a. Let alpha,beta be nonzero elements
of K. For a biform g with coefficients g_(i,s), define the matrix

    R_a(g)_((j,L),(H,r))=g_(H-j,L-r),

with0<=j,r<a and0<=H,L<2a-1; out-of-range coefficients are zero.
This is the maintained cyclic source's biform block, with its original
source credit. Consider either

    g=alpha+beta*x^u*z^v,       or       g=alpha*x^u+beta*z^v.  (1)

Set

    n_i=1+floor((a-1-i)/u),    0<=i<u,
    m_j=1+floor((a-1-j)/v),    0<=j<v.

Then, without any restriction on the characteristic or field size,

    rank R_a(g)=a^2+sum_(i=0)^(u-1) sum_(j=0)^(v-1) min(n_i,m_j). (2)

All sizes and offsets are quantified. The finitely exported matrices
are controls, not the proof of those quantifiers.

For equal offsets u=v=d, write a=q*d+r with0<=r<d. Formula(2) gives

    rank R_a(g)=a^2+q*d^2+r^2
               =a^2+a*d-r*(d-r).                         (3)

The divisor threshold a(a+d) is attained exactly when d divides a.
For example(a,d)=(5,2),(5,3),(7,2),(7,3) give ranks34,38,62,68,
respectively, with deficits1,2,1,2 from that threshold. These are
binomial matrix ranks, not source-space dimension bounds.

## 2. Rectangular coefficient maps are path matrices

Fix positive integers b,c. Consider alpha+beta*XZ with input indices
0<=j<b and0<=r<c and full output ranges0<=H<=b,0<=L<=c. Its matrix
B_(b,c) has format b(c+1) by(b+1)c and entries

    alpha if(H,L)=(j,r),
    beta  if(H,L)=(j+1,r+1),
    zero otherwise.                                      (4)

We claim

    rank B_(b,c)=bc+min(b,c).                             (5)

Assume b>=c. Regard the support as a bipartite graph with row and column
vertices. Every vertex has degree at most two. A column(H,r) connects
to row(H,r) when H<b and to row(H-1,r+1) when H>=1. Two consecutive
columns along a path therefore differ by(H,r) -> (H+1,r-1).
The strict increase of H excludes cycles.

A path ending in columns at both ends would have to start at H=0 and
finish at H=b. It would require at least b decreases of r. This is
impossible because0<=r<c and b>=c. Thus every component has a row
endpoint. In a vector in the column kernel, the equation at that endpoint
forces its adjacent column coefficient to vanish, since the edge weight
is nonzero. Continue along the path; every column coefficient vanishes.
There are no isolated columns. Hence B_(b,c) has full column rank
(b+1)c=bc+c, proving(5) for b>=c.

For b<c, transposition and interchange of the two variables identify
the matrix with B_(c,b) up to row/column permutations. It has full row
rank b(c+1)=bc+b. This completes(5). The argument uses no cancellation
or division by a field characteristic. Reversing the L output indices
and r input indices identifies alpha+beta*XZ with beta*X+alpha*Z.
Thus the same rank formula holds for either orientation in(1).

Equivalently, each support component is a path with a unique perfect
matching in any nonsingular square minor. At unit coefficients every
nonzero minor has determinant plus or minus one. At arbitrary nonzero
coefficients that determinant is a nonzero monomial in alpha,beta.
This also explains the field-independent lower certificates.

## 3. Unequal residue blocks give the exact general formula

For the first biform in(1), a nonzero entry requires H=j modulo u and
L=r modulo v. Partition the matrix by those two residue classes.
The input j values in residue i have exactly n_i members, and the input
r values in residue j have exactly m_j members. After subtracting the
residues and dividing the indices by u or v, the corresponding block
is precisely B_(n_i,m_j), with possible additional zero output rows or
columns. The nonzero output indices stop at n_i and m_j respectively.
They fit in the original full ranges because u,v<=a-1.

For the crossed biform in(1), the same residue partition instead gives
the reversed version of B_(n_i,m_j), with the same rank. Every row and
column belongs to only one residue block, so ranks add. By(5),

    rank R_a(g)=sum_(i,j) (n_i*m_j+min(n_i,m_j)).

Since sum_i n_i=sum_j m_j=a, the products sum to a^2. This proves(2),
including all the unequal-residue and crossed-orientation cases.

For an explicit upper certificate, choose all active rows of a block
when n_i<=m_j, and all active columns otherwise. Their total count is
the right side of(2), and they cover every nonzero entry. Splitting any
covered matrix into its selected rows and remaining selected columns
bounds its rank by that count. Together with a nonsingular minor of
that size, this gives a direct exact certificate over every field.

## 4. The equal-offset deficit and the elementary binomial gap

If a=q*d+r, then r of the d residue lengths equal q+1 and the others
equal q. The sum of the pairwise minima is q*d^2+r^2, proving(3).
Its difference from a*d is r(d-r), positive exactly at nondivisors.

There is also the uniform bound

    rank R_a(g)>=a^2+a.                                  (6)

If u<=v, the largest n_i=ceil(a/u) is at least every m_j, whose maximum
is ceil(a/v). The contribution of that one i to the sum of minima is
sum_j m_j=a. All other contributions are nonnegative. The case u>v
is symmetric. This proves(6) by elementary integer arithmetic.

Bound(6) recovers the binomial instances of the prior nonseparable
biform block gap. It does not reprove that more general theorem, whose
bundle-splitting argument and original credit remain intact. For the
divisor-cycle application in [PR148 at 673710d](https://github.com/1337isnot1337/matrix-mult-bounds/blob/673710d3a4284d88e4d24350681b26912831bf7a/research/ai/2026-10-23-divisor-source-caps/proof.md),
only these two-monomial instances are needed. Replacing that specific
invocation by(6) supplies an elementary alternative input; the torus,
cycle partition and strip witness retain their credited proofs. A change
to that package's dependency ledger must be recorded explicitly.

## 5. Evidence, scope and attribution

The maintained source note and earlier biform note fix the coefficient
convention and retain their original credit and exact byte pins. PR148's
divisor and nondivisor examples motivated this rederivation. The path
proof, unequal-residue expression and exact two-monomial certificates
are supplied here without importing a classification or splitting theorem.
No claim of historical priority or independent review is made.

Finite acceptance checks exported full-rank unimodular minors and row/
column covers for both orientations at every offset for a=2,...,6,
plus the a7 equal-offset boundary cases d=2,3. Separate arithmetic checks
cover the quotient/remainder identity and lower gap through a30. Tests
also inspect weighted rational and small-characteristic matrices with
an independent rank implementation. These controls support the all-size
written proof and do not formalize it.

The formula classifies two-monomial slices. It does not classify arbitrary
biforms, bounded-rank linear subspaces at nondivisor widths, complete
matrix targets or the exponent below9/4. No such improvement is claimed.
