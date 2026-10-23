# Every balanced A4 leading-rank pair has sum at most 144

October 23, 2026. Claim `AI-A4-ALL-PAIR-RANK144-001` is written and
unreviewed externally. This is owner-directed AI-derived research over
C, with exact finite certificates and no formalization.

## 1. Statement, conventions, and credit

Consider any complete Laurent presentation of a degeneration from the
canonical cyclic A4 source to M(10,10,11). Its outgoing target-leg maps
have row dimensions 100,110,110. For each map, divide by the smallest
power of t occurring in its entries; its first nonzero coefficient is
then a nonzero constant matrix. Let a,b,c be those constant ranks,
where a belongs to the 100-dimensional target leg.

**Theorem.** Every such presentation satisfies

    a+b<=144,       a+c<=144,       b+c<=144.              (1)

Consequently a+b+c<=216. If a=100, then b<=44 and c<=44.
The third map may have an arbitrary finite Laurent pole order when
either selected pair is made regular. Higher coefficients and complex
mixing on the selected pair are unrestricted.

These are necessary conditions. The rank bounds are not claimed sharp,
and no remaining rank triple is asserted to occur. This theorem does
not construct the target or improve the matrix multiplication exponent.

The source formula and cyclic symmetry retain their prior credit.
The [saturation theorem](../2026-10-20-graded-quantum-flags/saturation.md)
supplies the all-order support inequality. We use the registered source
caps and individual long-rank bound listed in Section 2, at the exact
local versions in `sources.json`.

[PR151 at f509561d](https://github.com/1337isnot1337/matrix-mult-bounds/blob/f509561d346635c097d3867a5c41741915d95491/research/ai/2026-10-23-coordinate-kernel-cap/torus_reduction.md)
already proves a universal pair bound 192 and a compression-kernel cap
nine when both defects are below 24 and their sum is at most 24. Its
matching and forced-cover method retains that credit. Sections 3-5
give a smaller, self-contained proof of the one case needed here,
defects (12,12), using seven ideals. The package does not import the
8,008-subset certificate or require PR151 files in the working tree.
The new application combines this special case with the stronger
source caps to obtain (1).

## 2. Source formula and available bounds

The source has 112 parameters F_(i,k,s), where 0<=i,s<=3 and 0<=k<=6.
Its slice matrix is

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),              (2)

where 0<=j,p,q,r<=3, 0<=H,L<=6, and out-of-range parameters are zero.
Both matrix dimensions are 112. Its literal terms are indexed by
six independent short indices i,j,p,q,r,s, with H=i+j and L=r+s.
The same source model applies after cyclically permuting the tensor
legs and reordering their coordinates.

For arbitrary complex linear parameter spaces V, the following
registered bounds apply to every slice M(F), F in V:

| Strict slice-rank threshold | Dimension upper bound | Prior proof |
| --- | ---: | --- |
| rank<24 | 8 | [torus low-rank](../2026-10-23-torus-low-rank/proof.md) |
| rank<37 | 16 | [rank37 source spaces](../2026-10-23-rank37-source-spaces/proof.md) |
| rank<48 | 24 | [rank48 frontier](../2026-10-23-torus-rank-frontier/proof.md) |
| rank<64 | 32 | [order-ideal theorem](../2026-10-23-torus-order-ideal/proof.md) |
| rank<80 | 44 | [sharp rank80 spaces](../2026-10-23-rank80-sharp-spaces/proof.md) |

The torus low-rank proof also shows that every individually balanced
long-map leading rank is at most 101, even with arbitrary finite poles
on the other maps. Thus

    0<=a<=100,       0<=b,c<=101.                         (3)

Allowing rank zero in the finite checks only enlarges the tested range.
The real balanced first coefficients are nonzero. The bound 101 is
an essential input: retaining long rank 110 would leave additional
mixed exceptional pairs in the source-cap screen.

## 3. A closed incidence locus for the special compression problem

**Compression lemma.** If U is a 12-dimensional subspace of C^112
and T is a 100-dimensional subspace of C^112, then

    dim {F : M(F)T is contained in U} <=9.                (4)

Suppose instead that this kernel contains a ten-dimensional parameter
space W. Consider the incidence

    I={(W,U,T): dim W=10, dim U=12, dim T=100,
                 M(W)T contained in U}                 (5)

in the product of the three complex Grassmannians. Let Z be its
projection to Gr(10,C^112 parameters). We need a closed invariant
locus of compressible spaces, not just a bound on each individual
matrix rank.

Here is an elementary proof of closedness. Fix Hermitian inner products
and represent each Grassmannian by the orthogonal projection onto its
plane. Fixed-rank orthogonal projections form a compact set: they are
Hermitian idempotents of fixed trace. If P_W,P_U,P_T are the respective
projections, the incidence is equivalent to the finitely many identities

    (I-P_U) M(P_W e_f) P_T=0                              (6)

for the 112 fixed coordinate vectors e_f. These are continuous conditions
on the projection matrices. Thus I is closed in a compact product,
and its projection Z is compact and closed in the ordinary topology.
This preserves all three plane dimensions, including both auxiliary
dimensions. Ordinary closedness is enough for the limits below.

For any source symmetry of the form

    M(gF)=L_g M(F) R_g,                                  (7)

with L_g,R_g invertible, the incidence transports as

    (W,U,T) -> (gW, L_g U, R_g^(-1) T).                   (8)

Therefore Z is invariant under each such parameter action.

## 4. Lower the parameter plane, then specialize the two auxiliaries

The credited order-ideal proof supplies a rank-preserving source torus
with parameter weights i+4k+28s, row weights -j+4p+28L, and column
weights H+4q-28r. Its parameter weights are distinct. It also gives
the nilpotent lowering operators

    D_i e_(i,k,s)=i e_(i-1,k,s)             when i>0,
    D_k e_(i,k,s)=(7-k)e_(i,k-1,s)         when k>0,
    D_s e_(i,k,s)=s e_(i,k,s-1)             when s>0,      (9)

with zero at a lower boundary. They have respective weight decreases
1,4,28 and literal identities M(D F)=L_D M(F)+M(F)R_D.
Their exponentials therefore have form (7). The acceptance program
replays all 336 sparse integer basis identities, with the stated edge
conventions. Exponentiation and the geometry are used over C.

The minimum Plucker-weight argument from the preceding proof applies
to any nonempty closed Grassmannian subset invariant under this torus
and these exponentials. For clarity, its application to Z is as follows.
Torus echelon degeneration gives a coordinate ten-plane in Z. Among
the finitely many such planes choose one of least total coordinate
weight. If a lowering operator does not preserve it, the wedge of
its basis, after applying exp(uD), has a nonzero highest positive
coefficient of degree J. Nonzero first variation is seen by replacing
a supported coordinate by an absent lower neighbor; that replacement
cannot cancel with any other wedge replacement.

After division by u^J, the limit at infinity is a nonzero decomposable
Plucker vector of smaller weight. It belongs to Z by closedness. Its
Plucker line is torus invariant, so its underlying plane is invariant
and hence coordinate, because the original parameter weights are
distinct. This contradicts minimality. The resulting ten-plane W
is thus a downward coordinate ideal, still belonging to Z.

Every F in such a compressible W has rank at most 24: its restriction
to T has image dimension at most 12, and the complementary domain has
dimension 12. A monomial in middle layer k has rank

    16*(1,2,3,4,3,2,1)_k.                                (10)

If the ideal contained any point with k>=1, it would contain a
middle-1 point of rank32. Hence W lies entirely in layer zero. Its
support is one of the seven short Ferrers ideals of size ten listed
in Section 5.

We must also make U and T coordinate while holding this W fixed.
The preceding torus is not sufficient: its matrix-column weights
can repeat. Use instead the second torus

    parameter weight: i-16k+256s,
    row weight:       -j-16p+256L,
    column weight:     H-16q-256r.                       (11)

The two matrix weights sum to the parameter weight in every one of
the 4096 source terms. All weights are distinct on each of the three
112-coordinate spaces, as also checked exactly. The coordinate W
is invariant under this torus. Move U,T by (8) for (11), then take
the limit as the torus parameter tends to zero. Echelon degeneration
on each auxiliary Grassmannian gives coordinate limits of dimensions
12 and100. The incidence remains valid by closedness.

Consequently any counterexample to (4) would give one of the seven
coordinate ten-planes whose entire matrix support is killed by deleting
at most12 rows and12 columns. Deleted rows are the coordinate U;
deleted columns are the12 coordinates outside T. The following finite
certificates exclude this possibility.

## 5. Seven literal support graphs

At middle layer zero the active matrix is the28-by28 coherent block

    R(g)_((j,L),(H,r))=g_(H-j,L-r).

Short coordinate (i,s) contributes sixteen graph edges

    row(j,r+s) -- column(i+j,r),       0<=j,r<=3.         (12)

Rows and columns outside this active block do not help delete these
edges. The certificate contains the following complete inventory.

| Short-ideal heights | Disjoint edges supplied | Additional certificate |
| --- | ---: | --- |
| (3,3,2,2) | 24 | Unique minimum cover uses24 rows |
| (3,3,3,1) | 24 | Unique minimum cover uses24 rows |
| (4,2,2,2) | 28 | None required |
| (4,3,2,1) | 28 | None required |
| (4,3,3,0) | 24 | Unique minimum cover uses24 columns |
| (4,4,1,1) | 28 | None required |
| (4,4,2,0) | 24 | Unique minimum cover uses24 columns |

Acceptance enumerates the seven height tuples independently. It builds
each graph from all four independent indices in (12) and checks its
embedding in the original six-index source. The three28-edge matchings
exclude any cover of total size at most24 immediately.

For a24-edge matching, any cover with at most24 vertices must contain
exactly one endpoint of each matching edge and no unmatched vertex.
A saved forcing sequence determines all24 choices on one side. To
force a matched row, its forcing edge goes to an unmatched column,
or to a matched column whose matched row was already forced. That
column is unselected, so the new row must be selected. The symmetric
rule forces columns. Each step uses a literal graph edge and only
previously forced choices. The final selected24 vertices are also
checked to cover every edge, proving uniqueness of the minimum cover.

The28-edge cases cannot have a cover of total size at most24. In each
other case, such a cover must use24 vertices all on one side. Neither
possibility fits budgets(12,12). This proves (4). Acceptance checks only
the exported matchings and forcing sequences; it performs no matching
or cover search. This is the PR151 method in the smaller ideal family,
with a new incidence-preserving lowering reduction.

## 6. Cancellation kernels and the all-order support bound

Choose any pair of target-leg maps, make both regular by multiplying
them by scalar powers of t, and compensate on the third map. Their
leading ranks are unchanged from individual balancing. Write the
regular maps in slice convention as B(t),C(t), with constant ranks
p,q. Define the cancellation space

    K={F : B(0) M(F) C(0)=0},       h=dim K.

For F in K, M(F) sends the q-dimensional image of C(0) into the
(112-p)-dimensional kernel of B(0). Extending that image by a domain
complement gives

    rank M(F)<=224-p-q.                                  (13)

The saturated support theorem gives, for a long/long pair,

    h>=100-floor(p/11)*floor(q/11),                       (14)

and for a short/long pair,

    h>=110-floor(p/10)*floor(q/10).                       (15)

We repeat its relevant argument to make the Laurent quantifiers clear.
Let S(t) be the first-source flattening after applying only B(t),C(t).
Its112 rows are regular. Its generic row span has dimension d<=112,
and its saturated C[[t]] lattice has a d-dimensional residue L0.
The constant row span W0 of S(0), of dimension112-h, lies in L0.
Every row of the complete regular output also lies in the saturated
lattice, even though the remaining map may have Laurent entries.
Thus the target matrix space Z lies in L0, and

    dim(Z intersect W0)>=dim Z-h.

The target slices are X tensor I_m, where m=11 and dim Z=100 for the
long pair, or m=10 and dim Z=110 for a mixed pair. In the intersection,
their joint column and row spaces lie in the leading images of the two
selected maps. Before tensoring I_m, these spaces have dimensions at
most floor(p/m) and floor(q/m). The intersection therefore has dimension
at most their product. This proves (14)-(15). No bound on the other
map's finite pole order occurs in this argument.

At the mixed pair(p,q)=(100,100), equation(15) gives h>=10. But K has
exactly the form in (4), with U=ker B(0) of dimension12 and
T=im C(0) of dimension100. Hence h<=9, a contradiction.

## 7. Every remaining pair above144 is excluded

For other pairs use (13), the source caps in Section 2, and(14)-(15).
The integer intervals below exhaust every possible sum above144 under
(3). The exceptional mixed(100,100) is omitted from the ordinary row
of its interval, having been excluded separately.

| Rank sum | Source dimension cap for K | Mixed h minimum | Long/long h minimum |
| --- | ---: | ---: | ---: |
| 201 through202 | 8 | 10 | 19 |
| 188 through200, excluding mixed(100,100) | 16 | 20 | 19 |
| 177 through187 | 24 | 29 | 28 |
| 161 through176 | 32 | 38 | 36 |
| 145 through160 | 44 | 46 | 51 |

Mixed pairs have maximum sum201. Each listed lower bound is strictly
larger than its source dimension cap. These integer bounds follow
directly from the floor products; the acceptance program also checks
all10,302 mixed rank pairs and10,404 long rank pairs in(3), without
rounding. Before the special compression lemma, exactly mixed(100,100)
survives among the pairs above144. Afterwards all1,653 such mixed
pairs and all1,711 such long pairs are excluded.

This proves every inequality in(1). Adding them gives twice the total
rank at most432, hence total at most216. Setting a=100 in either mixed
inequality gives the stated long-rank bound44.

The strict source threshold80 is respected: at pair sum144, equation
(13) only gives rank at most80, so the cap44 does not apply. The saved
controls leave(72,72) and the mixed pair(100,44) open to this argument.
They are arithmetic boundary controls, not target constructions.

## 8. Evidence and scope

The standard-library verifier checks the seven complete graph
certificates, all112 monomial ranks,4096 cyclic symmetries,8192 torus
coefficient identities,336 integer lowering identities, and every
integer pair in the stated ranges. All imported local proof versions
are checked by hash. These finite controls support the written
compactness, lowering, and all-Laurent-order deductions; they do not
formalize those arguments or constitute external independent review.

The package establishes necessary leading-rank conditions only.
Lower-rank triples, different constructive maps and the complete target
remain open. It makes no exponent improvement claim.
