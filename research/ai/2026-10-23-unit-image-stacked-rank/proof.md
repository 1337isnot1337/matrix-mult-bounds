# A sharper Laurent bound from a stacked product

October23,2026. Owner-directed Codex continuation of the written,
unreviewed rank107 package. No independent review or exponent gain.

## 1. Statement and scope

For the balanced cyclic source A_a, a>=2, put N=a^2(2a-1). Let
E=Mat_m(C), Xi(X)=X tensor I_n, R=mn<=N and m>=2. Suppose Laurent
maps satisfy the complete identity

    B(t) M(F(t)(X)) C(t)=Xi(X)+O(t), for every X in E.

Assume C is regular with rank C(0)=R and u=F(I_m) is regular. Write
S=M(u). Suppose rank(S(0)C(0))>=r, and put

    e=R-r,        q=N-r,        k=N-R.

The following four strict inequalities force B and F to be regular:

    a^2>2q,       q+e<2n,       n+2q<2a^2,       m^2-m>a^2.  (1)

The limit is an ordinary restriction. If also n<a^2-2k, the degeneration
is impossible. All finite Laurent pole orders and all higher regular
coefficients are allowed.

For A4 to M(10,10,11), take r=105. Then e=5,q=7,k=2 and the strict
margins in(1) are

    16-14=2,       22-12=10,       32-25=7,       90-16=74.

The ordinary contradiction is12>11. Thus the exclusion reaches regular
unit images of rank at least105, including every regular source unit of
corank at most five, with one regular rank110 long-leg limit. It is
symmetric in the long legs. Retained rank104, singular long-leg limits
and polar unit lifts remain outside the result.

## 2. Normalization and the stacked rank fact

Use the [rank107 package](../2026-10-23-unit-image-rank-gap/proof.md),
Section2, with its exact source frames and all its stated hypotheses.
After normalizing BSC=I_R, fix a retained inclusion H:C^r -> C^R and
independent regular source frames completing CH and SCH. For every
constant left inverse P H=I_r, the same limiting source M_0 is
row/column equivalent to the original cyclic source, and

    X11(t)+L_P(t)X21(t)=P Xi(X)H+O(t).                 (2)

The source blocks have row/column sizes(r,q). If B has a pole, at least
one L_P has a pole, by the credited varying-left-inverse recovery.

For any matrices L,Y over C((t)), with Y having q rows, the single matrix

    Z(t)=[-L(t); I_q]Y(t)                             (3)

has rank at most q. Whenever t^h Z(t) is regular, its constant term has
rank at most q, by vanishing(q+1)-minors. It is unnecessary to add the
ranks of the top and bottom blocks separately. Regularity of both
blocks is required before this specialization; a raw coefficient of a
nonregular product need not obey the rank bound.

## 3. Eliminate first-map poles with2q rather than3q

Assume B has a pole, fix a compressed equation(2), and suppose F has
pole order h>0 with nonzero leading value f=F_-h(X). All source blocks
have poles of order at most h. Equation(2) makes t^h L_P X21 regular;
t^h X21 is also regular. Thus(3) with Y=X21 is regular after multiplying
by t^h, and its constant term is

    [X11,-h; X21,-h].

Indeed, multiplying(2) by t^h kills the regular target term, so
X11,-h=-(t^h L_P X21)(0). This is the entire first r columns of
M_0(f), and it has rank at most q. The last q columns add at most q.
Consequently rank M_0(f)<=2q<a^2, contradicting the credited minimum
source slice rank. Hence F is regular.

## 4. Control the kernel without assuming first-map injectivity

If X belongs to ker F_0, all source constant blocks vanish. Equation(2)
makes L_P X21 regular and gives rank(P Xi(X)H)<=q for every P. The
[rank-preserving retraction lemma](../2026-10-23-unit-image-rank-gap/proof.md),
Section4, therefore gives

    n rank X-e <= rank(Xi(X)H) <= q.                  (4)

The inequality q+e<2n implies every matrix in ker F_0 has rank at most
one. A linear subspace of m-by-m matrices of rank at most one has
dimension at most m; here is an elementary proof of the needed case.

Choose a nonzero uv^T in the subspace. For any other nonzero xy^T,
rank(uv^T+xy^T)<=1 forces x proportional to u or y proportional to v.
If an x not proportional to u occurs, its y is proportional to v.
An element with row factor not proportional to v would then have column
factor proportional to u, and its sum with that chosen element would
have rank two. Thus every element has row factor v in this case;
otherwise every element has column factor u. Either space has dimension
at most m. The zero subspace also satisfies the bound.

It follows from(4) that

    rank F_0 >= m^2-m > a^2.                         (5)

When q+e<n the same argument even gives ker F_0=0, but that stronger
condition is not needed at r105.

## 5. Propagate coherent factors even when a ruling meets the kernel

Since F is regular, both X21 and L_P X21 are regular. By(3) their stacked
constant correction has rank at most q. For rank-one X, (2) gives

    [X11,0;X21,0]=[P Xi(X)H;0]+Z(0),

so the first r columns have rank at most n+q, and

    rank M_0(F_0(X))<=n+2q<2a^2.                     (6)

Invoke the existing complete source slice classification below2a^2,
with its original credit. Every nonzero image of a linear target ruling
has one coherent factor h. Zero images cause no difficulty: the image
of a ruling is a linear space, so its nonzero members still have that
fixed factor.

For completeness, let uv^T and u'v'^T have nonzero images under F_0.
The two maps w |-> F_0(wv^T) and w |-> F_0(wv'^T) are nonzero.
Over C choose w outside the union of their two proper kernels. The
three rulings joining

    uv^T,       wv^T,       wv'^T,       u'v'^T

have nonzero shared images, so all these images have the same h.
Thus all nonzero rank-one images have one h. Rank-one matrices span E,
and the zero images are harmless, giving rank F_0<=a^2. This contradicts
(5), and excludes the assumed pole of B.

## 6. Specialization, strict boundary and evidence

With B,C regular, the unit identity at zero gives both long maps full
rank. A first-map pole would be a nonzero source slice killed by two
defect-k maps, forcing rank at most2k<a^2. Hence F is regular, and the
existing ordinary rank argument excludes the target when n<a^2-2k.
At A4 the source minimum16 loses at most four and contradicts target
rank11. A source unit of corank at most five has image rank at least
110-5=105, giving the corollary.

At r104, q=8 and the required16>2q becomes equality. The finite controls
include arbitrary block families attaining leading rank2q, so this rank
estimate alone has no strict contradiction there. These controls are
not cyclic-source degenerations and do not show that the boundary is
attainable for A4. Its status remains unresolved by this proof.

The source, rank minimum, below-twice-minimum classification, independent
frames and retraction lemma retain their prior repository credits and
are pinned in sources.json. This continuation contributes the combined
stacked-product rank count, bounded rank-one kernel step and propagation
without injectivity. The rank-one matrix-space lemma is proved above;
no new external theorem is imported. Finite exact controls support this
written unreviewed proof without formalizing arbitrary series or changing
the exponent. No historical priority or independent review is claimed.
