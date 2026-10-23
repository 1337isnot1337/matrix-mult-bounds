# Laurent regularity from the low-rank source locus

October 23, 2026. Owner-directed Codex work over C. Written and
unreviewed; no independent review, formalization or exponent improvement.

## 1. Statement

Let A_a be the balanced cyclic source, a>=2, with slice map
M:A -> Mat_N(C), where dim A=N=a^2(2a-1). Consider the matrix target
M(m,m,n), with E=Mat_m(C), R=mn and target slices

    Xi(X)=X tensor I_n.

Suppose Laurent maps F:E -> A, B of size R by N, and C of size N by R
satisfy the complete degeneration identity

    B(t) M(F(t)(X)) C(t)=Xi(X)+O(t), for all X in E.       (1)

Assume C is regular with rank C(0)=R, and u=F(I_m) is regular. Write
S=M(u). Choose 1<=r<=R such that rank(S(0)C(0))>=r. Put

    e=R-r,        q=N-r,        k=N-R.

If

    a^2>3q,       n-e>q,       n+3q<2a^2,       m^2>a^2,  (2)

then B and F are regular, and (1) specializes to an ordinary restriction.
If also n<a^2-2k, no such degeneration exists.

For a=4,m=10,n=11,N=112,R=110, take r=107. Then e=3,q=5,k=2, and

    16>15,       11-3=8>5,       11+15=26<32,       100>16.

The ordinary rank floor is16-4=12>11. Consequently no A4 degeneration
to M(10,10,11) has a regular full-rank long map and a regular unit lift
with rank(S(0)C(0))>=107. This includes regular source unit slices of
corank at most three, without an alignment assumption. The statement
holds with the long legs exchanged and allows every finite Laurent
pole order. Rank106, singular long-leg limits and polar unit lifts are
not excluded here.

## 2. Dependencies and independent source frames

The existing [minimum slice-rank proof](../2026-10-20-koszul/cyclic_finite_target.md)
gives rank M(f)>=a^2 for every nonzero f. The existing
[polynomial rank-locus theorem](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md)
classifies every nonzero f with rank M(f)<2a^2 as

    f=g tensor h,    g in C^(a^2),

where [h] lies on the degree-(2a-2) rational normal curve. Every nonzero
linear space in that locus has a fixed h, hence dimension at most a^2.
We use this classification of source slices, not its ordinary-target
consequence as if it already applied to singular limits.

Use the independent frame construction from the prior
[partial-unit-image proof](../2026-10-23-regular-unit-image/proof.md),
Sections2-4. In detail, G=BSC=I_R+O(t) is regular invertible. Replacing
B by G^(-1)B preserves the target limit and makes BSC=I_R exactly.
Choose a constant R-by-r matrix H such that S(0)C(0)H has rank r.
Complete CH and SCH independently to regular invertible source frames
Q_C and Q_B. Set

    M_t(f)=Q_B^(-1) M(f) Q_C.

The limiting source is row/column equivalent to M and retains both its
rank minimum and the rank-locus classification on the same space A.
The frames are fixed independently of all subsequent choices of P.

For every constant left inverse P of H, the compressed equation is

    [I_r,L_P(t)] M_t(F(t)(X)) [I_r;0]
        = P Xi(X) H+O(t),                              (3)

because PBQ_B has first r columns P BSC H=P H=I_r. Block the source
matrix by (r,q), with entries X11,X12,X21,X22. Thus (3) says

    X11+L_P X21=P Xi(X)H+O(t).                         (4)

If B has a pole, some constant P has a pole in L_P. To see this, choose
target coordinates H=[I_r;0]. The left inverses are [I_r,Z]; their
differences recover every bottom row of B, while Z=0 recovers its top
rows. The regular source frame does not change regularity. This is the
prior finite left-inverse recovery argument.

## 3. First-map poles are impossible

Suppose B has a pole and select such a P. If F has pole order h>0,
choose X with nonzero highest coefficient f=F_-h(X). All source blocks
have pole order at most h. Equation(4) makes t^h L_P X21 regular, with
constant coefficient -X11,-h.

A regularized product of inner dimension q has limiting rank at most q:
its (q+1)-minors vanish over C((t)) and therefore after specialization.
Adding the bottom q rows and the last q columns yields

    rank M_0(f)<=3q<a^2,

a contradiction. Hence F is regular. No pole-order bound has been used.

## 4. Varying retractions preserve the rank needed for injectivity

We need a stronger compression observation than deleting e rows and e
columns independently.

**Retraction lemma.** If H:C^r -> C^R is injective and Y is an R-by-r
matrix, then

    max_{P H=I_r} rank(PY)=rank Y.                     (5)

Choose constant coordinates with H=[I_r;0], and write Y=[U;V]. Put
s=rank Y<=r and a_0=rank U. Apply invertible row operations to U to
put a_0 independent rows first and zero rows last. Among the rows of V
select s-a_0 extending those independent rows to the row space of Y.
There are enough zero rows since s<=r. Add the selected V rows to
distinct zero rows of U. This constructs Z with rank(U+ZV)=s; reversing
the row operations gives P=[I_r,Z]. The opposite inequality is ordinary
rank monotonicity. The case s=0 is included.

Now F is regular. For any X in ker F_0, the constant coefficient of
X11 in(4) is zero. The product L_P X21 is regular for every P by(4),
and its constant coefficient is P Xi(X)H. The product-rank fact gives

    rank(P Xi(X)H)<=q for every P H=I_r.

By(5), rank(Xi(X)H)<=q. If X were nonzero, removing e columns from
Xi(X) would instead give

    rank(Xi(X)H)>=rank Xi(X)-e>=n-e>q.

Therefore F_0 is injective. P may depend on X in this argument; the
source frames and F do not. A single fixed compression need not preserve
this rank, and no simultaneous choice of P for all X is asserted.

## 5. Rank-one parameters force a fixed coherent factor

Fix any P. Since F is regular, (4) again makes L_P X21 regular. Its
constant coefficient has rank at most q. For rank-one X, rank Xi(X)=n,
so

    rank X11(0)<=n+q,
    rank M_0(F_0(X))<=n+3q<2a^2.                      (6)

The additional 2q accounts for the bottom q rows and last q columns.
This estimate concerns the limiting source lift after first-map
regularity was proved. It does not apply an ordinary-map rank estimate
to the original approximating tensor.

Injectivity makes F_0(X) nonzero for every nonzero rank-one X. Every
linear ruling of the rank-one Segre variety maps into the source locus
below rank2a^2, hence has one coherent factor h. Any two rank-one
parameters uv^T and u'v'^T are connected by the two rulings through
u'v^T. Their nonzero shared images force the same h. Thus the entire
rank-one variety has one h. Rank-one matrices span E, so

    F_0(E) is contained in C^(a^2) tensor h.

Its dimension is at most a^2. Injectivity and dim E=m^2>a^2 contradict
this. Consequently B cannot have a pole.

## 6. Ordinary specialization and the A4 boundary

Now B and C are regular. Taking BSC=I_R at zero shows B(0) has rank R.
If F had a pole with highest coefficient f, equation(1) would give
B(0)M(f)C(0)=0. Two source projections of defect k lose at most2k
rank, so rank M(f)<=2k<a^2, since a^2>3q>=3k. This is impossible.
Thus F is regular, proving the regularity assertion.

The specialization is an ordinary restriction. Its nonzero target
rank-one slices have rank n, whereas every nonzero source lift has
rank at least a^2 and loses at most2k. This proves the exclusion when
n<a^2-2k. For A4 the comparison is12>11.

If a regular source unit S(0) has corank at most three, then
rank(S(0)C(0))>=110-3=107, giving the stated corollary. Larger coranks
can also meet the image-rank hypothesis. At r106, q=6 and16>18 fails;
the present first-pole argument supplies no conclusion. This failure
does not construct a degeneration or assert that rank106 is attainable.

## 7. Evidence and attribution

The source, rank minimum, source rank-locus classification, independent
frame construction, Laurent product-rank fact and ordinary A4 exclusion
retain their existing repository credits and are pinned in sources.json.
The continuation replaces the row-contraction dimension step by the
varying-retraction injectivity lemma and propagation over target Segre
rulings. No new external theorem is imported, and no historical priority
or independent review is claimed.

The finite verifier constructs rank-preserving retractions over Q,
including cases where a fixed projection loses rank; reconstructs source
coefficient matrices and sharp rank32 controls; and replays every stated
integer margin and the strict rank106 failure. These are finite controls
for the written argument, not a formal proof of arbitrary Laurent series.
