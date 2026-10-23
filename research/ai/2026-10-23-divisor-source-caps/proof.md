# Sharp divisor-strip caps for balanced cyclic source spaces

October23,2026. Owner-directed Codex work, written and unreviewed.
No independent review, formalization or exponent improvement.

## 1. All-size statement

Let a>=2 and let d<a be a positive divisor of a. Put p=a/d>=2.
For the complex balanced cyclic source A_a, let M be its N-by-N slice
map with N=a^2(2a-1). Then

    max {dim V: rank M(f)<=a(a+d)-1 for every f in V}=ad.    (1)

More precisely the same maximum ad holds for every integer rank ceiling q
in the interval

    a(a+d-1)<=q<a(a+d).                                  (2)

The subspaces V are arbitrary complex linear subspaces; there is no
coordinate, torus-invariance, fixed-middle-factor or homogeneity
hypothesis. All a and their proper divisors are quantified, not just
the finite parameters in the verifier.

Examples of(2) are a=4,d=2: ceilings20--23 and cap8; a=6,d=2:
ceilings42--47 and cap12; a=6,d=3: ceilings48--53 and cap18; and
a=9,d=3: ceilings99--107 and cap27. The A4 instance is the prior
PR129 theorem, which retains its source credit and authorship. The
all-size divisor-cycle and residue-block arguments below are this
continuation, without a historical-priority claim.

## 2. Source convention and rank-preserving specialization

Use the maintained canonical coefficients

    M(F)_((j,b,L),(H,c,r))=F_(H-j,b+c,L-r),

where j,b,c,r range from0 to a-1 and H,L from0 to2a-2. Out-of-range
source coefficients are zero. Set m=2a-1. The diagonal action

    D(t) F_(i,k,s)=t^(i+a*k+a*m*s) F_(i,k,s)

has all N distinct weights0,...,N-1. For t nonzero its source matrices
are related by invertible row and column scalings:

    M(D(t)F)_((j,b,L),(H,c,r))
       =t^(-j+a*b+a*m*L) M(F)_((j,b,L),(H,c,r))
                                    t^(H+a*c-a*m*r).     (3)

Thus it preserves every slice rank. Apply the credited coordinate-limit
argument of [PR129](../2026-10-23-torus-low-rank/proof.md), Section3.
For completeness, order coordinates by these weights and put a basis
of V in reduced row-echelon form. Divide D(t) times each basis vector
by its pivot's power of t. The resulting vectors are polynomial and
specialize to their distinct coordinate pivots. Every constant linear
combination has rank at most q for t nonzero, so its(q+1)-minors also
vanish at zero. The limiting coordinate subspace has the same dimension
and lies in the same bounded-rank locus. It suffices to bound coordinate
subspaces. No assertion that the original V is invariant is used.

## 3. Only one middle extreme can occur

A coordinate slice e_(i,k,s) has rank a^2 h_k, where

    h_k=min(k+1,a,2a-1-k).

Each solution of b+c=k contributes an independent a^2 matching. Since
d<=a/2, the ceiling in(1) is strictly below2a^2. Thus a bounded-rank
coordinate subspace can use only k=0 or k=2a-2. A sum of one nonzero
coordinate at each extreme has rank2a^2: the two matrices occupy
disjoint b/c row and column blocks. Both extremes cannot occur together.

At one extreme, identify the coordinates with an a-by-a grid(i,s).
Its source matrix has the same rank as the biform coefficient matrix

    R_a(g)_((j,L),(H,r))=g_(H-j,L-r).                    (4)

The remaining middle blocks are zero. Here j,r<a and H,L<2a-1.

## 4. Two coordinates in a divisor cycle force rank at least a(a+d)

Partition the grid into orbits of

    tau(i,s)=((i+d) modulo a,(s+d) modulo a).

Every orbit has length p=a/d, hence there are a^2/p=ad orbits. Two
distinct points in one orbit differ in both coordinates by nonzero
multiples of d. Remove their common monomial factor. This only shifts
nonzero output rows and columns in(4), preserving rank: all nonzero
coefficient ranges remain inside the full convolution ranges.

Their biform is consequently one of

    1+x^(alpha*d)z^(beta*d),
    x^(alpha*d)+z^(beta*d),                              (5)

with1<=alpha,beta<=p-1. This includes different wraparound directions
on the two axes. Put X=x^d,Z=z^d, and let g_0(X,Z) be the corresponding
two-monomial p-by-p biform in(5).

Decompose(4) by j and H modulo d and by L and r modulo d. Nonzero
entries require j=H modulo d and L=r modulo d. Each of the d^2 residue
blocks, after subtracting its residues and dividing the indices by d,
is exactly R_p(g_0), with possibly extra zero rows or columns. The
input j and r each have exactly p indices in their residue. The
nonzero output H and L indices are at most2p-2 after rescaling; all
these indices fit in the original full ranges. The extra possible
indices2p-1 carry zero coefficients. Therefore

    rank R_a(g)=d^2 rank R_p(g_0).                       (6)

The prior [biform block lemma](../2026-10-20-anisotropic-constructions/slice_rank_gap.md),
Section1, proves over C that a nonseparable p-by-p biform has
rank R_p at least p^2+p. Both biforms in(5) are nonseparable: their
coefficient matrices have two independent nonzero rows and columns.
This local written lemma and its cited bundle-splitting input retain
their prior status and credit; no new proof of that input is claimed.
Combining it with(6) gives

    rank R_a(g)>=d^2(p^2+p)=a^2+ad=a(a+d).              (7)

A coordinate subspace with ceiling a(a+d)-1 therefore contains at most
one coordinate from each divisor orbit. Its dimension is at most ad.
The specialization in Section2 transfers that bound to every complex V.

## 5. A strip attains the bound throughout the stated interval

Take the ad independent coordinates

    k=0,       0<=i<d,       0<=s<a.

Every source slice in their span uses only columns with c=0,
0<=H<=a+d-2 and0<=r<a. Thus its rank is at most a(a+d-1). This gives
an ad-dimensional witness for every ceiling in(2). Combined with the
upper bound, it proves(1)--(2). The strip is a source linear space,
not a degeneration to a matrix target.

## 6. An all-size singular-long-leg corollary

Let Xi(X)=X tensor I_n for X in Mat_m(C), with R=mn<=N and k=N-R.
Suppose a complete Laurent degeneration has one regular long map C of
limiting rank R-c. If

    m>ad,       n+2k+c<a(a+d),       a^2>3k+c,            (8)

then no such degeneration exists. The other two maps may have arbitrary
finite poles, with no original unit-lift assumption.

This adopts the credited [unit-kernel argument of PR113](https://github.com/1337isnot1337/matrix-mult-bounds/blob/08ac3e983e270cf3df4e26d960ceb16415f7ef31/research/ai/2026-10-23-one-regular-leg/proof.md)
and active-ruling argument of PR129. The latter's pinned local proof
includes the complete kernel identity. Scalar-balance F to be regular with
F_0 nonzero. The target unit gives an exact regular right inverse D of
the other long map after regular output normalization. The correction

    W_X=M(F(X))C-D B M(F(X))C

is regular of generic rank at most k. At zero,

    M(F_0(X)) C_0=D_0 Xi(X)+W_X(0),       rank W_X(0)<=k.

For rank-one X=uv^T, the source-lift rank is at most n+2k+c, so it is
below the cap threshold in(1). If that lift is nonzero, the source
minimum a^2 gives

    rank(D_0((uv^T) tensor I_n))>=a^2-2k-c>k.

Choose u with at least one nonzero lifted rank-one parameter. The rank
on the left is independent of nonzero v, because v^T tensor I_n is
surjective. Any nonzero v in the kernel of v |-> F_0(uv^T) would make
the same rank at most k, a contradiction. This entire m-dimensional
ruling is therefore injected into a source linear space with ceiling
below a(a+d), whose dimension is at most ad. The inequality m>ad is
impossible. This proves(8). The long-leg transpose is analogous.

For a=4,d=2,m=10,n=11,k=2, (8) excludes c<=8. This recovers PR129's
rank102 cutoff and is not a new A4 frontier claim. No asymptotic target
family or exponent improvement follows from these source obstructions.

## 7. Verification and provenance

The source formula, source minimum and biform block-rank gap retain
their exact predecessor pins. Torus specialization and active-ruling
injection retain PR129's credit, and the regular unit-kernel correction
retains PR113's. The all-size divisor partition, residue-block identity
and sharp interval are this continuation. The source gap inherits the
external P1 bundle-splitting dependency stated in its pinned proof.
All local proof claims remain written and unreviewed.

The finite verifier checks divisor orbits, literal residue-block source
identities, exact nonseparable biform minors, strip support counts and
the recovered A4 cutoff, with explicit finite parameter ranges. Those
calculations do not replace the all-integer argument above, constitute
independent review or construct an improving matrix target.
