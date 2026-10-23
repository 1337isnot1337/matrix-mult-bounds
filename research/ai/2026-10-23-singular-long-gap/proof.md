# Singular leading long maps with a minimum-rank gap

October23,2026. Owner-directed Codex work, written and unreviewed.
No independent mathematical review, formalization or exponent gain.

## 1. Statement

Let A_a be the balanced cyclic source over C, a>=2, with N=a^2(2a-1),
minimum nonzero slice rank a^2, and no slice rank strictly between a^2
and a^2+a. Its minimum-rank slices are exactly u tensor h tensor v,
where u,v belong to C^a and [h] is on the degree-(2a-2) rational normal
curve. These are prior source results, not new classifications here.

Consider the target M(m,m,n), Xi(X)=X tensor I_n, R=mn<=N and k=N-R.
Suppose Laurent maps satisfy the complete identity

    B(t) M(F(t)(X)) C(t)=Xi(X)+O(t), for every X in Mat_m(C). (1)

Assume C is regular with rank C(0)=R-s, where s>=0. If

    m>=2a,       n+2k+s<a^2+a,       a^2>2k+s,             (2)

then no such degeneration exists. There is no assumption on the original
first-map or unit-lift valuations; both other maps may have arbitrary
finite poles. The same statement holds with the two long legs exchanged.

For A4 to M(10,10,11), N=112,R=110,k=2 and m=10>=8. For every0<=s<=4,

    15+s<20,        16>4+s.

Thus a regular long map of limiting rank at least106 is excluded.
After scalar balancing, every remaining candidate must have limiting
rank at most105 on each long leg. Rank105, both more singular long maps
and the full matrix target remain unresolved by this proof.

## 2. The regular unit-kernel correction with singular C(0)

Use the [one-regular-leg argument](../2026-10-23-one-regular-leg/proof.md),
Sections2-3, retaining its predecessor credit. Scalar balancing F against
B makes F regular with F_0 nonzero and leaves C unchanged. Choose an
invertible matrix U with F_0(U) nonzero; such U exists because invertible
matrices form a dense open set and F_0 is a nonzero linear map.

Write Y_X=M(F(X)) C and D=Y_U. Both are regular. G=B D has invertible
constant term Xi(U). Replacing B by G^(-1)B makes BD=I_R exactly, and
the target limit becomes

    Xi_U(X)=Xi(U)^(-1)Xi(X).

This has rank n for rank-one X and is invertible for invertible X.
The regular correction

    W_X=Y_X-D(BY_X)=(I_N-DB)Y_X

has rank at most k over C((t)), since I_N-DB projects onto ker B.
Its regularity follows from the difference of regular products, not
from the possibly polar projector. Specialization gives

    M(F_0(X)) C(0)=D(0) Xi_U(X)+W_X(0),
    rank W_X(0)<=k.                                      (3)

Nothing through(3) required C(0) to have full rank. Its kernel dimension
is now k+s. Hence every rank-one X satisfies

    rank M(F_0(X)) <= n+k+(k+s)=n+2k+s<a^2+a.             (4)

Each nonzero such source lift has minimum rank a^2. Also,

    rank D(0)>=a^2-(k+s)>k,                              (5)

because F_0(U) is nonzero. If ker F_0 contains an invertible X, (3)
would give rank D(0)<=k, contradicting(5). It remains to prove that
invertible-kernel assertion.

## 3. One coherent factor, including zero images

The prior complete source locus below2a^2 implies that every nonzero
linear space of source slices in that locus has a fixed coherent h.
The bound(4) is below2a^2, since a>=2 and a^2+a<=2a^2. Every target
linear ruling therefore has a fixed h on its nonzero images.

For two rank-one parameters uv^T and u'v'^T with nonzero images, choose
w outside the two proper kernels of the nonzero maps
w |-> F_0(wv^T) and w |-> F_0(wv'^T). The three rulings through
uv^T,wv^T,wv'^T,u'v'^T have nonzero shared images, forcing the same h.
Thus all nonzero rank-one images have one h, even if some rulings meet
ker F_0. Rank-one matrices span Mat_m, so the whole image has that h.

Identify that fixed-h space with Mat_a via the two outer source factors.
By the minimum-rank classification and(4), the resulting nonzero linear
map T:Mat_m -> Mat_a takes every rank-one matrix to rank at most one.
It has the same kernel as F_0.

## 4. A polynomial proof of the required rank-one-preserver cases

We prove the needed factorization instead of importing a preserver
classification with unstated nondegeneracy assumptions. Form

    A(u,v)=T(uv^T)

over the polynomial ring C[u_1,...,u_m,v_1,...,v_m]. Its entries have
bidegree(1,1), and its2-by2 minors vanish identically, since they vanish
at every complex u,v. Choose a nonzero column and divide it by the gcd
of its entries to obtain a primitive polynomial column p. Rank one over
the fraction field makes each other column a rational scalar multiple
of p. Its scalar is polynomial: any reduced denominator would divide
every entry of p in this UFD. Thus A=p q^T for polynomial columns p,q.

Factors of a bihomogeneous polynomial can be chosen bihomogeneous:
the minimum and maximum degrees in each variable group add under a
nonzero product, so their differences must both vanish. Consequently
the gcd is bihomogeneous, all nonzero p entries have one bidegree
(alpha,beta), and q has bidegree(1-alpha,1-beta), with alpha,beta in{0,1}.

If(alpha,beta)=(0,0), p is constant and the image of T has a fixed
column factor; its dimension is at most a. If(alpha,beta)=(1,1), q
is constant and the image has a fixed row factor, again of dimension
at most a. In the other two cases p and q are linear in opposite
variable groups. Since rank-one matrices span the domain, respectively

    T(X)=P X Q,       or       T(X)=P X^T Q,              (6)

with P of size a by m and Q of size m by a. This includes rank-deficient
P and Q. These four cases exhaust all nonzero T under consideration.

## 5. Each case has an invertible matrix in the kernel

In(6), let p=rank P and q=rank Q. Since p+q<=2a<=m, an invertible X
can map im Q into ker P: choose bases of those spaces, map a basis of
im Q to q independent vectors of ker P, and complete both to bases of
C^m. This gives PXQ=0. For the transpose case use the transpose of that
invertible witness.

In the fixed-row or fixed-column case, dim im T<=a, so

    dim ker T>=m^2-a>m(m-1),

where m>=2a>a. The external bounded-rank matrix-space theorem implies
that ker T contains a matrix of rank m. Precisely, use Flanders's bound
for complex linear spaces, with square size m and upper rank m-1:
dim V<=m(m-1) if every matrix of V is singular. It is stated in
[de Seguins Pazzis, arXiv:1507.05375v2, Theorem1.1](https://arxiv.org/pdf/1507.05375v2),
page3. Only the dimension inequality is imported, with its complex-field
hypotheses satisfied. The classification of equality cases is not used.
This theorem is external and retains Flanders's credit; the repository's
earlier finite-slice note already uses its arbitrary-field version.

All cases put an invertible X in ker T=ker F_0, contradicting(5) through
(3). This proves(2) and the A4 consequence.

## 6. Boundary, verification and credit

At s=5, the lifted rank-one bound is20, which meets the next permitted
source rank. An exact source control attains rank20; it is a source
slice, not a target degeneration. The minimum-rank preserver step above
therefore supplies no conclusion at long-leg rank105. No claim of
optimality or attainability for that degeneration is made.

The canonical source, minimum-rank gap and locus, coherent-factor locus
and regular unit-kernel correction retain their prior credits and exact
byte pins. Noninjective ruling propagation continues the preserved
PR119 checkpoint; the polynomial factorization and singular-column
application are written here with all degenerate cases included.
Flanders's dimension theorem is the sole imported external theorem,
with the exact version, field and application given above. There is
no historical-priority claim or independent review.

Finite exact controls verify invertible-kernel witnesses for rank-deficient
compression maps, degenerate maps, source ranks16 and20, strict long-leg
boundary budgets and source pins. They do not formalize arbitrary formal
series or constitute a matrix-multiplication construction. The exponent
below9/4 and the more singular A4 target remain unproved.
