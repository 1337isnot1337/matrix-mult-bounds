# A rank-loss requirement for two-sided singular conjugation

October 23, 2026. Owner-directed Codex work. Written and unreviewed.
This is a scoped obstruction, not an improved matrix exponent.

## 1. The complete source family

Use the canonical A4 matrix slices and the existing invertible source unit.
After that constant normalization and the middle-coordinate permutation,
the 112 source slices are

\[
H_{k,i,s}=J_k\otimes G_{i,s},\qquad
(J_k)_{q',q}=\mathbf 1_{q'=q+3-k},
\]

where k runs from zero through six, i,s from zero through three,
q,q' from zero through three, and every G matrix has size 28.
The exact outer formulas, with lexicographic indices, are

\[
S(f)_{(j,L),(H,r)}=f_{H-j,L-r},\quad
K=S(\sum_{i+s=3}e_{i,s}),\quad G(f)=K^{-1}S(f).
\]

These are the credited source conventions of the merged cyclic-source
and fixed-resolvent packages. The integer inverse of K is checked exactly.
In particular,

\[
N=H_{0,0,0}=E_{3,0}\otimes G_{0,0},\quad N^2=0,
\quad\operatorname{rank}N=16.
\]

For a parameter z tending to infinity, set g(z)=I+zN. The new family is

\[
H(z)=g(z)^{-1}H g(z)
=H+z(HN-NH)-z^2NHN.                         \tag{1}
\]

It uses the complete source space, not only its conic fourteen-row
incidence. In the degeneration parameter t=z^-1, both long maps can
have singular leading terms. This differs from the prior one-sided
resolvent g(z)^-1 H.

Let L be the full limiting 112-dimensional slice space of (1).
The exact coefficient calculation supplies 112 polynomial combinations
of the original slices whose highest coefficients are independent.
There are 50 combinations of degree zero, 46 of degree one, and 16 of
degree two. Their complete leading matrices are retained as a certificate.
The transformations can contain powers of z; they account for all
first-leg cancellations and do not identify a raw leading-coefficient
span with the saturated limit.

The acceptance conditions for this computation are:

1. Reconstruct all original source matrices and their normalization.
2. Expand every retained polynomial combination using (1).
3. Check its stated highest degree and complete leading matrix.
4. Check independence of all 112 leading matrices. Full rank modulo a
   prime proves independence over the rationals, hence over the complexes.

Each normalized polynomial combination belongs to the regular lattice
of the source slice space over the Laurent field. The independent 112
constant terms therefore span L: the original space has dimension 112,
so its saturated lattice has rank 112 and its reduction has that same
dimension. This is a finite exact certificate for the entire limit.

## 2. A twelve-dimensional scalar subspace

Number the normalized coordinates by

\[
(q,H,r)\longmapsto 28q+4H+r.
\]

Put

\[
S=\operatorname{span}\{e_{100},e_{101},\ldots,e_{111}\}.
\]

Every X in L acts on S as a scalar:

\[
X|_S=\lambda(X)I_S.                         \tag{2}
\]

The certificate checks this column identity for every one of the 112
leading matrices, over the integers. It also checks that L contains I.
For interpretation, all nondiagonal middle blocks of L lie strictly
below the four-by-four block diagonal. Its diagonal blocks are spanned
by I and I4 tensor G00. The last twelve outer coordinates lie in
ker G00. The literal column checks, rather than this description alone,
are the finite acceptance condition.

## 3. Compression can recover directions, but only the lost number

Let P have size 110 by 112 and C have size 112 by 110, both of full
rank, over the complexes. They are arbitrary constant maps. In particular,
they need not preserve S or the middle grading, and PC need not be I.
Compress the entire polynomial family (1), and let L' be its full
saturated limiting matrix space in Mat110. Define

\[
D=\dim(PLC),\qquad \ell=112-D.
\]

First,

\[
PLC\subseteq L'.                             \tag{3}
\]

Indeed, a regular Laurent-field slice curve with constant term X in L
compresses to a regular slice curve with constant term PXC. This is
valid even if that constant term is zero. Thus every nonzero projected
leading direction is in the true compressed limit.

The generic compressed slice space has dimension at most 112. Its
saturated limit has the same dimension as that generic space, so

\[
\dim L'-\dim(PLC)\le112-D=\ell.              \tag{4}
\]

This inequality does not assume that compression preserves the generic
rank. In the present A4 family it in fact does preserve that rank:
every nonzero uncompressed source slice over the Laurent field has
ordinary matrix rank at least sixteen, by the credited all-field source
minimum-rank theorem. Conjugation preserves that rank. The two
codimension-two projections can lower it by at most four, so no nonzero
source slice is killed. Hence dim L'=112 here. The weaker inequality
(4) is sufficient for the argument.

Since dim S=12 and im C has codimension two,

\[
\dim(S\cap\operatorname{im}C)\ge10.
\]

Choose a nonzero v in C110 such that Cv lies in S. Equation (2) gives

\[
(PXC)v=\lambda(X)PCv\qquad(X\in L).
\]

Therefore evaluation of PLC at v has dimension at most one. The vector
PCv may be zero, which only strengthens the bound. Adding at most ell
directions by (4) gives

\[
\dim(L'v)\le1+\ell.                        \tag{5}
\]

## 4. The full matrix target requires at least nine lost directions

For the matrix-multiplication slice space

\[
A=\operatorname{Mat}_{10}\otimes I_{11}
   \subset\operatorname{Mat}_{110},
\]

evaluation at any nonzero v has dimension at least ten. Identify v
with a 10 by 11 matrix of ordinary rank r. The image of X -> Xv
has dimension 10r, so its dimension is at least ten. Independent
invertible row and column changes preserve this lower bound for every
nonzero evaluation vector.

If the compressed family (1), with any Laurent first map, degenerates
to M(10,10,11), its 100 target slices lie in L'. Consequently
dim(L'v) is at least ten for every nonzero v. Equation (5) then implies

\[
\boxed{\ell\ge9,\qquad \dim(PLC)\le103.}    \tag{6}
\]

This is the claimed rank-loss requirement. It includes arbitrary finite
Laurent orders in the first map. It does not discard the directions
that reappear after compression kills a leading coefficient. No bound
on their orders is used.

More generally, the same proof applies whenever a D-dimensional matrix
space has a limiting s-dimensional scalar subspace, an input compression
of codimension less than s, and a target with minimum nonzero evaluation
rank m. A successful compression must lose at least m-1 leading slice
directions. These are ordinary ranks and dimensions, not tensor slice rank.

## 5. Complete principal coordinate-compression census

For each two-element subset h of the 112 normalized coordinates, let
C_h include the other 110 coordinates and let P_h=C_h^T. The completed
exact finite census covers all binomial(112,2)=6216 such pairs.

Every projected limiting space P_h L C_h has rank at least 108 over
the certificate prime 1009, hence dimension at least 108 over C.
Thus ell is at most four, below the necessary nine in (6). This
excludes every principal coordinate compression in this specified
two-sided conjugation family.

The finite-field rank is used only as a lower certificate for complex
dimension. No equality of modular and complex ranks is needed for this
exclusion. The numerical rank histogram, exact whole-space certificate,
coverage formula, and corruption controls are retained separately.

## 6. Remaining construction question

The result does not exclude every A4 degeneration. It concerns one fixed
square-zero source slice, its two-sided conjugation family, and constant
long-map compressions. A successful compression in that family would
have to lie on the determinantal locus dim(PLC)<=103. Its existence is
not settled here. Moving compressions, different source-unit paths,
and products of noncommuting unipotent factors remain separate questions.

The source matrices, normalization, and minimum source slice rank retain
their prior attribution. Saturated lattices and evaluation-rank bounds
are elementary linear algebra and are not claimed as historical
discoveries. The local additions are the complete two-sided limiting
space, its scalar-action subspace, the compression rank-loss requirement,
and the finite principal-compression exclusion. Same-session verification
is not independent mathematical review or formalization.
