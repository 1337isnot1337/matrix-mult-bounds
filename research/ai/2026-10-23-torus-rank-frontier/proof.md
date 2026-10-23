# A4 source spaces below rank 48 and the long-rank sum 176

October 23, 2026. Written, unreviewed owner-directed OpenAI Codex work
over C. No independent mathematical review, formalization, historical
priority, target construction, or exponent improvement is claimed.

## 1. Statements and prior inputs

Use the canonical cyclic source A4, with 112 parameters and slices

    M(F)_((j,p,L),(H,q,r)) = F_(H-j,p+q,L-r),               (1)

where i,j,p,q,r,s range from 0 to 3, the long indices range from 0 to 6,
and out-of-range short coefficients are zero. This is the coefficient
formula of the literal product

    X_i Y_j Z_(i+j), Y_p Z_q X_(p+q), Z_r X_s Y_(r+s).

The new assertions are:

1. If V is any complex linear parameter space and every F in V has
   rank M(F)<48, then dim V<=24.
2. In every complete Laurent degeneration

       B(t) M(F(t)(X)) C(t) = X tensor I_11+O(t),
       X in Mat_10(C),                                    (2)

   independently scalar-balance B,C so that each is regular with a
   nonzero constant coefficient, compensating by the inverse product
   scalar in F. Their constant ranks b,c satisfy b+c<=176.

The source and ordinary A4 restriction obstruction are prior work. The
rank-preserving torus and eight-pair certificate are adopted from the
[rank-23 package](../2026-10-23-torus-low-rank/proof.md), repeated below
to make this deduction readable without an implementation dependency.
The [saturated support condition](../2026-10-20-graded-quantum-flags/saturation.md)
is also prior work. PR122 at a284807699bc95e252087b3503b49da483116788
applied that condition to source spaces below rank 32 and obtained the
sum bound 192. The present extension reaches rank 47 and the sum 176.
No PR113 or PR122 code is imported.

## 2. A torus reduces bounded-rank spaces to coordinate spaces

Multiply each source coordinate F_(i,k,s) by t^(i+4k+28s).
In (1), this is an invertible diagonal row and column transformation
for every t!=0: the row weight is -j+4p+28L and the column weight is
H+4q-28r. Their sum is i+4k+28s. All 112 parameter weights are distinct.

Let V have dimension d and lie in any closed matrix-rank locus. Order
the coordinates by weight and choose an echelon basis v_1,...,v_d with
distinct leading coordinates and no smaller nonzero coordinates. Apply
the torus to each v_j and divide it by its leading power of t. These
vectors are regular at t=0 and tend to distinct coordinate vectors.

For every constant linear combination, its value at t!=0 belongs to
the torus image of V and retains the rank bound. Its entries are regular;
the minors expressing the rank bound vanish and still vanish at zero.
Consequently the coordinate limiting d-plane retains the rank bound.
It is enough to bound the dimension of such coordinate spaces. This
argument keeps dimension exactly and is not a numerical limiting test.

## 3. The 28-by-28 biform blocks and the eight-pair bound

For a four-by-four array g, define

    R(g)_((j,L),(H,r)) = g_(H-j,L-r),                    (3)

with row indices 0<=j<4, 0<=L<7, and column indices 0<=H<7, 0<=r<4.
Again use zero for out-of-range coefficients. If F is supported at one
middle coordinate k, with F_(i,k,s)=g_(i,s), then, after fixed row and
column reorderings,

    M(F)=H_k tensor R(g),
    (H_k)_(p,q)=1 if p+q=k, and 0 otherwise.             (4)

The scalar ranks of H_k are (1,2,3,4,3,2,1). A monomial g=e_(i,s)
has R(g) rank 16: it has sixteen ones in distinct rows and columns.
Thus the 112 source coordinate slices have ranks

    16,32,48,64,48,32,16 according to their middle k.    (5)

We use this consequence of the prior rank-23 theorem:

> A linear space of g arrays with every R(g) of rank at most 23 has
> dimension at most eight.                               (6)

It can be proved directly by the same torus. Pair the sixteen short
coordinates into the eight pairs

    (i,s) <-> (i+2 mod 4,s+2 mod 4).

For each pair, R of the sum of its two coordinate vectors has a
24-by-24 minor of determinant 1. The exact minor indices are exported
and replayed from (3). A bounded-rank-23 coordinate space cannot contain
both coordinates of a pair, so it has at most eight coordinates. The
torus argument proves (6) for arbitrary complex spaces as well.
This is the credited matching certificate, not a new classification of
all rank-23 spaces.

## 4. The dimension-24 theorem below rank 48

Let V now be a coordinate space with every source slice of rank below
48. Formula (5) restricts its middle coordinates to {0,1,5,6}.

Three middle pairs cannot occur together. The p and q supports of H_0
are both {0}; those of H_1 are {0,1}; those of H_5 are {2,3}; and those
of H_6 are {3}. Hence any two source coordinate vectors with middle
coordinates (0,5), (1,6), or (1,5) have disjoint row and column supports.
Their sum has rank respectively 48,48, or 64, by (5). This works for
every choice of the two short-coordinate pairs, not just matching ones.

It follows that the middle support of V is contained in one of

    {0,1}, {0,6}, {5,6}.                               (7)

For support in {0,1}, the pure middle-1 component is itself a linear
subspace of V. By (4), every one of its slices has rank 2 rank R(g)<48.
Its g-space therefore has dimension at most eight by (6). The middle-0
component has at most sixteen parameters. Their dimensions add because
V is coordinate, giving dim V<=24. The support {5,6} is identical,
using the rank-two H_5 and the rank-one H_6.

For support in {0,6}, write its two independent g-spaces as V_0,V_6.
The two source blocks have disjoint rows and columns, so

    rank M(g_0 at middle 0 + g_6 at middle 6)
      = rank R(g_0)+rank R(g_6).                         (8)

If both V_0 and V_6 had dimension at least nine, (6) would supply one
g in each whose R-rank is at least 24. Their sum belongs to V and has
source rank at least 48, a contradiction. One component therefore has
dimension at most eight, while the other has at most sixteen. Again
dim V<=24. Section 2 now proves the theorem for arbitrary complex V.

The upper bound 24 is not asserted to be sharp. Its strict rank threshold
is essential to this proof: middle 2 and 4 become available at rank 48,
and (6) no longer limits the rank-two blocks to dimension eight.

Two simpler consequences of the same coordinate argument will be used
below. Below rank 16 a source subspace is zero. Below rank 32 only
middle 0 and 6 can occur, and they cannot both occur because a sum of
one coordinate from each has rank 32. Therefore every such subspace
has dimension at most sixteen. This recovers, for A4, the weaker bound
used in PR122 without needing the full low-rank-locus classification.

## 5. The credited saturated target-support inequality

For regular B,C of constant ranks b,c, let S(t) be the 112-row first
flattening of their projected source and put rho=rank S(0). Let L be its
row space over C((t)), of dimension d<=112, and let

    Lambda = L intersect C[[t]]^(110*110).

This saturated lattice is free of rank d and its reduction L_0 embeds
in the residue space: if a lattice vector is divisible by t in the
ambient space, dividing by t leaves a regular vector of L and hence
another lattice vector. Thus dim L_0=d. The row space W_0 of S(0), of
dimension rho, lies in L_0 and has the joint supports prescribed by B_0,C_0.

Every regular row of F(t)S(t) also lies in this lattice, even when F has
poles. Its constant target row space Z={X tensor I_11} is a 100-dimensional
subspace of L_0. Therefore dim(Z intersect W_0)>=100+rho-112=rho-12.

For a parameter subspace E of matrices X whose X tensor I_11 lie in W_0,
let p,q be the dimensions of the joint column and row spaces of E.
The corresponding joint spaces of X tensor I_11 have dimensions 11p,11q.
They fit in the prescribed leading supports, so

    p<=floor(b/11), q<=floor(c/11), dim E<=p*q.

Combining these facts gives the prior necessary inequality

    rho <= 12+floor(b/11)*floor(c/11).                   (9)

Equivalently, for the constant cancellation kernel

    K={F:B_0 M(F) C_0=0}, h=dim K=112-rho,

we have

    h >= 100-floor(b/11)*floor(c/11).                   (10)

This argument covers every Laurent pole order and arbitrary higher
regular coefficients. Its attribution is retained in the source pins.

## 6. Exclude all balanced long-rank sums above 176

Put delta=224-b-c. Every F in K has rank M(F)<=delta, since two-sided
compression loses at most (112-b)+(112-c) matrix ranks. Sections 2-4 give

    delta<16 => h=0;
    delta<32 => h<=16;
    delta<48 => h<=24.                                  (11)

First suppose 177<=b+c<=192. Then 32<=delta<=47, so h<=24. But

    floor(b/11)+floor(c/11)<=floor(192/11)=17,

whose maximum integer product is 8*9=72. Equation (10) forces h>=28,
a contradiction. This is the new range beyond PR122.

If 193<=b+c<=208, then h<=16. Equation (10) requires the two floors to
have product at least 84. Each floor is at most ten. If both were at
most nine, their product would be at most 81. Thus one floor is ten,
which requires its map rank to be 110, and the other is at least nine,
which requires rank at least 99. Their sum would be at least 209,
contrary to this case.

Finally, if b+c>=209, then delta<=15 and h=0. The projected flattening
S(t) has a unit maximal minor and a right inverse over C[[t]]. Since
F(t)S(t) is regular, F itself is regular. Specializing (2) gives an
ordinary restriction. Target concision forces both long maps to have
rank 110. Their source defects are two each, so any nonzero lifted
source slice has target rank at least 16-2-2=12. A rank-one X has target
slice rank 11, a contradiction. This repeats the credited ordinary A4
obstruction only after proving the required regularity.

All cases above 176 are excluded. Any Laurent pair B,C can be balanced
independently by scalar powers of t, compensating in F, so this bound
holds for every candidate's scalar-balanced leading long ranks. It
requires a total target rank loss of at least 220-176=44.

## 7. Scope and exact controls

The proof establishes an upper dimension bound and a necessary rank
frontier. It supplies no complete degeneration, no witness at sum 176,
no sharpness theorem for 24 or 176, and no exponent improvement.

The verifier reconstructs all 4096 literal source terms, every monomial
slice, the fixed tensor-factor multiplicities, eight determinant-one
minors, and all 768 prohibited middle-pair sums. It enumerates the
12,321 pairs 0<=b,c<=110 with (10)-(11) and the ordinary-regime gate.
The saved record is replayed, and corruption controls reject altered
source pins, minors, rank budgets, and inflated claims. These finite
calculations support the proof; they do not formalize its arbitrary
complex-subspace or all-order quantifiers. The written claims remain
unreviewed. Historical source files are unchanged.
