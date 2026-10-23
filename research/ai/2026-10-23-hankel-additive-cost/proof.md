# Exact source-rank minima in the binomial supporting chart

October 23, 2026. Owner-directed Codex work, written and unreviewed.
This is a source-slice theorem. It does not construct a matrix target,
exclude general degree-one supporting forms, or improve the exponent.

Work over any field K. Let a,b be positive integers and

    2<=r<min(a,b),     m=a+b-1,     d=m-1.

Use the literal cyclic source slice with coefficient polynomials

    f_k(x,z)=sum_(i<a,s<b) F_(i,k,s) x^i z^s,  0<=k<=d,

and matrix

    M_F[(j0,p,L),(H,q,t0)] = F_(H-j0,p+q,L-t0),

where j0<b,p<a,L<m,H<m,q<b,t0<a and out-of-range coefficients are zero.
Restrict attention to the **binomial chart**

    f_(k+r)=xz f_k,   0<=k<=d-r.                         (1)

This fixes the homogeneous supporting form V^r-xz U^r. It is a proper
subclass of the preceding primitive-degree-(1,1) question.

## 1. Feasible seeds and the rank formula

Put

    u_s = #{p<a: p is congruent to s modulo r},
    v_s = #{q<b: q is congruent to s modulo r},
    D_s=u_s-1,   E_s=v_s-1,       0<=s<r.

For a seed index 0<=j<r, write

    ell_j=floor((d-j)/r).

Call j feasible when ell_j<=min(a,b)-1. Let J be the feasible indices.
If J is empty, the only source slice satisfying (1) is zero. Otherwise
the minimum rank among its nonzero source slices is

    min_(j in J) R_j,
    R_j=ab*r+a(a-r)+b(b-r)+sum_(s=0)^(r-1) D_s E_((j-s) mod r).   (2)

Every nonzero slice in this chart has scalar Hankel rank exactly r and
primitive supporting degrees (1,1). In particular, the additive lower
bound from the preceding question holds throughout this entire chart,
including arbitrary polynomial initial moments, over every field.

## 2. Exact rank of one constant initial moment

Let F^j have f_k=(xz)^ell when k=j+r*ell, and f_k=0 otherwise. It is a
valid source slice exactly when j is feasible. Decompose the row moment
index as p=s+rP and the column moment index as q=t+rQ. A nonzero block
requires t=(j-s) mod r. Write s+t=j+r h; then h is zero or one. Thus the
matrix is the direct sum of r disjoint row/column components. Fix one.
Its P range is 0,...,u_s-1 and its Q range is 0,...,v_t-1. A nonzero
entry equals one and satisfies

    H-j_short = L-t_short = P+Q+h.

Give its row the key

    (A,B)=(j_short+P, L-P)

and its column the key

    (A,B)=(H-Q-h, t_short+Q+h).

The coefficient formula says that an entry is one exactly when its keys
agree. Feasibility ensures P+Q+h<=min(a,b)-1 throughout the component.
After grouping keys, each shared key gives a nonempty all-ones block,
and distinct keys have disjoint row and column supports. The component
rank is therefore its number of shared keys over every field.

For a fixed P, row keys fill

    [P,P+b-1] times [-P,m-1-P].

For a fixed Q, column keys fill

    [-Q-h,m-1-Q-h] times [Q+h,Q+h+a-1].

Their intersection is exactly the integer rectangle

    [0,b+u_s-2] times [h,h+a+v_t-2].                     (3)

Here are the boundary details. Put u=u_s,v=v_t. The maximum P+Q+h is
u+v+h-2, so feasibility gives u+v+h<=min(a,b)+1. Any point in (3)
belongs to a row rectangle by choosing P=max(0,A-b+1): P<=u-1, and
B+P<=h+a+v-2+u-1<=m-1. It belongs to a column rectangle by choosing
Q=max(0,B-h-a+1): Q<=v-1, and A+Q+h<=b+u-2+v-1+h<=m-1.
The opposite inclusion follows from the row lower/upper bounds on A and
the column lower/upper bounds on B. Thus the component
rank is (b+u_s-1)(a+v_t-1).

Sum over s and use sum D_s=a-r, sum E_s=b-r. Expanding these products
gives exactly R_j in (2). This is an all-parameter factorization and
identity-minor argument, not an inference from modular experiments.

## 3. Arbitrary polynomial initial moments

Write g_j=f_j for 0<=j<r. Equation (1) determines all other moments:

    f_(j+r*ell)=(xz)^ell g_j.

If g_j is nonzero, the source degree bounds require

    deg_x g_j<=a-1-ell_j,  deg_z g_j<=b-1-ell_j.          (4)

Therefore j is feasible, proving the zero assertion when J is empty.
Every monomial x^i z^s in such a g_j individually obeys (4).

Scaling the three coefficient coordinates by integer weights
(alpha,gamma,beta) multiplies F_(i,k,s) by
lambda^(i alpha+k gamma+s beta). This scales matrix rows and columns
by, respectively,

    lambda^(-j_short alpha+p gamma+L beta),
    lambda^(H alpha+q gamma-t_short beta).

Consequently source matrix rank is unchanged over K(lambda). Choose

    alpha+beta+r gamma=0.

Every monomial descended from x^i z^s in g_j then has the same weight
i alpha+s beta+j gamma, independently of ell. Distinct triples
(i,s,j), with 0<=j<r, give distinct pairs (i-s,j-rs): equality would
force j-j'=r(s-s'), hence s=s',j=j',i=i'. Taking gamma=1,
alpha sufficiently large positive, and beta=-alpha-r separates this
finite set of weights. After division by the lowest power of lambda,
the coefficientwise limit is one nonzero scalar multiple of x^i z^s F^j.

The monomial shifts do not change the rank of F^j. Multiplication by
x^i shifts its nonzero columns H to H+i; multiplication by z^s shifts
its nonzero rows L to L+s. No nonzero entry is truncated, since (4)
gives H+i<=m-1 and L+s<=m-1 on their supports. Each shift extends to
a permutation of the nonzero rows or columns and unused zero positions.

Rank cannot increase in the limit: all minors of size one above the
original rank vanish over K(lambda), hence also at lambda=0 after this
polynomial coefficient normalization. Thus rank M_F>=R_j for the selected
seed, and in particular rank M_F>=min_(j in J) R_j. The basis slice
at a minimizing feasible seed attains this minimum, proving (2).

For completeness, its scalar Hankel rank is r. The leading r-by-r
Hankel minor of F^j is a permutation matrix with nonzero entries one
or xz, so its determinant is a signed monomial. The same weight-limit
argument applies to scalar symbol rank: the x,z substitution is a field
automorphism over K(lambda), and lambda^k is a row/column scaling on the
Hankel matrix. Hence every nonzero F has symbol rank at least r. Its
recurrence gives a nonzero kernel with the usual r-step shifts and
rank at most r; equivalently all columns after the first r are xz times
the column r positions earlier. Thus rank is exactly r. The supporting
form is consequently minimal. Its two primitive degrees are one.

## 4. Closed balanced minimum

For a=b=n and 2<=r<n every seed is feasible. Write n=qr+t, 0<=t<r.
Then D_s=E_s=q-1+1_(s<t). The final convolution in (2) has minimum

    r(q-1)^2+2(q-1)t+max(0,2t-r).                       (5)

Indeed the remaining term counts the intersection of a length-t cyclic
interval with a translate of its reflection. Two such intervals have
minimum intersection max(0,2t-r), attained by separating their starts.
The exact minimum source rank in the entire balanced binomial chart is
therefore

    r*n^2+2n(n-r)+r(q-1)^2+2(q-1)t+max(0,2t-r).         (6)

For r=n-1 the correction is zero. This recovers the preceding exact
two-variable boundary family and retains its prior credit. For n=4,r=2
the correction is two, giving the sharp chart minimum 50 rather than
the weaker additive threshold 48. These are source-slice minima, not
tensor-target constructions or exponent results.

## Attribution and limits

The literal source and supporting-degree question are prior repository
work. The r=n-1 two-variable boundary family is from PR134. This
continuation supplies the residue/key factorization, complete binomial-
chart minimum, monomial weight limit and balanced closed formula.
It does not prove the additive conjecture for an arbitrary primitive
degree-(1,1) supporting form. No historical priority, independent
mathematical review, formalization or smaller exponent is claimed.
