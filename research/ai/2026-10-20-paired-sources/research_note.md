# An all-size paired-source kernel and finite construction targets

AI-derived written argument, October 20, 2026. Unreviewed; no new exponent
bound. Elementary tensor products, Koszul rank monotonicity and spectral
conversion are imported tools, not new results here. The finite profile
ceiling is the concurrent Koszul worker's existing finite-amplitude result.

## 1. Source and exact first Koszul kernel

The subsequent [all-power calculation](all_koszul.md) now gives every
first-leg Koszul rank and excludes the size-six target considered in
Section 4. Its matrix comparison is derived in [matrix_koszul.md](matrix_koszul.md).
The earlier first-rank and budget arguments remain valid.

Put D=a-1 and h=2a-1. Pair two copies of C(a,a) with their second and third
legs exchanged. Their tensor P_a has first coordinates A_(p,q), second
coordinates B_(y,j), and third coordinates C_(z,v), and coefficients

    P_a = sum_(p,q,y,v=0)^D A_(p,q) B_(y,q+v) C_(p+y,v).

Its format is (a^2,ah,ah), with border rank at most h^2. For its first
Koszul map use

    K: A tensor B* -> exterior^2(A) tensor C,
    K(w tensor beta)=sum_(p,q) A_(p,q) wedge w tensor P_(p,q)(beta).

Write an input vector as v_(r,s;y,j). The image vanishes exactly when

    v_(r,s;z-p,q+v) = v_(p,q;z-r,s+v)                 (1)

for every p,q,r,s,v in [0,D] and z in [0,2D], taking an entry with an
out-of-range y index as zero. This is direct antisymmetrization of the two
A indices; it is valid in every characteristic with the exterior relation.

If y<r, choose p=0 and z=y in (1). Split the arbitrary index j as q+v,
which is possible for every j in [0,2D]. The right side is zero, hence
v_(r,s;y,j)=0. If y>r, choose p=D and z=D+y for the same conclusion.
Only y=r can remain. Write F_r(s,j)=v_(r,s;r,j). Equation (1) becomes

    F_r(s,q+v)=F_p(q,s+v).                            (2)

Splitting j=q+v and fixing p proves independence from r. Denote the result
by F(s,j). Equation (2) preserves L=s+j. For a fixed L, choose
q=max(0,min(D,L-D)). For every admissible s, v=L-s-q lies in [0,D].
Thus (2) connects every entry of total L to the same F(q,L-q).

Consequently the entire kernel is

    v_(r,s;y,j) = 1_(y=r) u_(s+j),  0<=s+j<=3D.

Conversely each such vector satisfies (1). The 3D+1 parameters have
disjoint nonempty supports, so they are independent. This proves, over
any field,

    dim ker K = 3a-2,
    rank K = a^3(2a-1)-(3a-2).                        (3)

This is an exact all-size formula, not an inference from modular ranks.
Koszul rank cannot increase at a complex degeneration in the fixed ambient
first-leg format. Smaller other legs can be padded by zeros.

## 2. Matrix targets and the full-capacity obstruction

For M(l,b,r), place its lr-dimensional leg first, its lb-dimensional leg
second and its br-dimensional leg third. If r>=2, its first Koszul map is
injective. Indeed, for a proposed input coefficient at A_(i,k) tensor
B*_(i',j), choose k'!=k. In the output coordinate
A_(i,k) wedge A_(i',k') tensor C_(j,k'), that coefficient is the only
contribution. It must vanish in a kernel vector. This works for every
input coefficient. The rank is therefore (lr)(lb).

If r=1 the map is antisymmetrization on l-by-l matrices in each of b
copies; its kernel has dimension b*l*(l+1)/2. Exchanging the other two
legs gives the corresponding statement with l and r interchanged.

In particular, a degeneration P_a to M(a,b,a), for a>=2, requires

    a^3 b <= a^3(2a-1)-(3a-2).

For integer b this gives b<=2a-2. Thus full-capacity M(a,2a-1,a) is
excluded under arbitrary complex degeneration, including Laurent basis
changes. This settles a tempting full-format shortcut without assuming
a shared basis stays regular.

For a direct sum of matrix blocks with the entire first space still of
dimension a^2, different blocks give independent output components of K.
Cross-block A coordinates are independent as well. If every block has
r>=2, the resulting Koszul map is injective on A tensor B*. For a=5,
the full-format target

    M(4,9,4) direct_sum M(3,3,3)                     (4)

has format (25,45,45) and Koszul rank 1125, whereas P_5 has rank 1112.
Therefore (4) is impossible under arbitrary complex degeneration.

Had (4) been possible, three cyclic copies and the shared spectral profile
would give P(5,5)^(2t)>=144^t+27^t. The existing upper bound
6P(5,5)<=28^(1/t) would imply 5184^t+972^t<=784. At t=7499/10000,

    (2441/4)^10000 < 5184^7499,
    (1391/8)^10000 < 972^7499,
    2441/4+1391/8 = 6273/8 > 784.

These exact integer comparisons explain why the target would have implied
omega<=2.2497. The Koszul obstruction excludes its premise; this number is
not an achieved bound.

## 3. One-copy matrix-block scoring at size four

At a=4 every matrix block M(l,b,r) must satisfy

    lr<=16, lb<=28, br<=28.

There are 268 positive integer shapes in this format. Section 2 removes
(4,7,4), leaving 267 shapes. At a hypothetical endpoint character all
dot-product exponents are 3/4, so the character of a matrix block is
(lbr)^(3/4), and a direct sum scores the sum of these quantities.

The finite integer budget certificate in `budgets.py` bounds every such
direct sum, with total leg budgets (16,28,28), by

    L=132771862263/4294967296, approximately 30.91335815.

The certificate uses integer ceilings of fourth roots; no floating ordering
decides acceptance. A simple verifier checks all budget transitions. The
maximizing rounded partition consists of shapes (1,1,1), (1,3,3), (4,6,3).
It is a scoring partition, not a constructed degeneration.

If each of the three paired factors is first converted, in one copy, to a
direct sum of matrix products, their combined endpoint character lower
bound is at most L^3. This can force a lower bound for P(4,4) no larger
than L^(2/3). The exact comparisons

    L^4 < 106^3,
    6^3 L^2 < 22^4

put that ceiling below both sqrt(106) and the existing finite endpoint
ceiling 22^(4/3)/6. Thus this factorwise scoring method cannot supply the
needed finite profile gain. This is a limitation on the method, not an
upper bound on actual P(4,4), and not a proof that S_4 cannot degenerate
to M106. Joint extraction from paired factors or their powers remains open.

## 4. A finite target subsequently excluded by higher Koszul ranks

The initial next single-matrix paired target was

    P_6 -> M(6,10,6),                               (H)

in formats (36,66,66) to (36,60,60). It is now excluded by the all-power
formula: at power 7 the source rank is 499196720 and the target rank is
500652900. The conditional exponent calculation is retained to explain
the target selection; its premise is impossible under the written proof.
Three cyclic copies would give S_6 -> M(360,360,360). By the existing
spectral rules this implies P(6,6)>=sqrt(360). Combining it with the
existing finite upper bound 6P(6,6)<=34^(1/t) gives

    omega <= 6 log(34)/log(12960) < 2235/1000.

The final strict comparison has the exact certificate

    12960^2235 > 34^6000.

Thus (H) would have been sufficient for omega<=2.235 without a separate
unbounded family. It is not an active construction target after the
higher-rank exclusion. The first Koszul ranks are 2360 on the source and 2160 on the
target, so that necessary test does not exclude it. On the other two legs,
both source and padded target have injective first Koszul maps of rank
2376, as certified by modular full-column ranks. The recorded higher
grading upper bounds are coarse source bounds, not computed source ranks;
they do not establish that every Koszul test passes.

For the displayed target lower ranks at powers p=0,...,5, the matrix
Koszul map is injective whenever p<r. One can see this directly over C.
In an orthonormal exterior basis, write its creation operator as delta.
The creation-annihilation relations give delta* delta = r I-T, where T
is the restriction to the antisymmetric tensors of the sum of p operators
that exchange the auxiliary l-dimensional factor with the l-dimensional
part of one exterior factor. Each exchange has norm one. Hence
delta* delta >= (r-p)I, proving injectivity when p<r. The b middle-index
copies are independent. The source grading bounds use the two weights
A_(p,q)=(p,q), B_(y,j)=(y,-j), C_(z,v)=(-z,v): each Koszul map preserves
their induced weights, so its rank is at most the sum of the smaller
domain and codomain dimensions over all weights.

Ordinary restrictions are excluded. Every nonzero first slice of P_a has
rank at least a^2: choose its lexicographically first nonzero coefficient
X_(p0,q0), use rows (y,q0+v) and columns (p0+y,v), and order them by y
then v. The resulting a^2-square minor is block triangular with triangular
diagonal blocks and determinant X_(p0,q0)^(a^2). A monomial slice attains
rank a^2. Projection to the two ab-dimensional target legs can lose at
most 2a(2a-1-b) in slice rank. Since M(a,b,a) has minimum slice rank b,
an ordinary restriction requires

    (2a-1)b <= 3a^2-2a.

At (a,b)=(6,10), 110>96 violates this condition. The construction must be
singular. The source is also a coordinate restriction of the abelian group
tensor (Z/11)^2. The previously proved Laurent coordinate-input screen,
adopted from `../2026-10-20-koszul/finite_target_screens.md`, excludes any
two coordinate input maps even with arbitrary Laurent mixing on the third
leg: its left side is 288>121 for a large output leg, or 360>121 for the
small output leg. These weaker screens alone leave general mixed input
families open; the later power-seven comparison excludes this specific
target even with general complex Laurent maps.

The triangular-minor argument is the same elementary mechanism used in
the concurrent `cyclic_finite_target.md`, Section 2, for its three-factor
source. This paired specialization and its ordinary-restriction consequence
are not credited as an independent general minimum-rank method.

## Dependencies and claim boundary

The finite profile ceiling, the six-factor source, endpoint equality of
the dot-product exponents, and its spectral conversion are the concurrent
worker's `finite_amplitude.md` and the cited external OpenAI/Uznański
results. The local contribution is the exact paired-source kernel,
its consequences, the finite budget certificate and the selected smaller
construction question. The existing coordinate-input lemma is adopted,
not counted as a new theorem. No independent review or formalization is
claimed, and neither conditional exponent is an achieved bound.
