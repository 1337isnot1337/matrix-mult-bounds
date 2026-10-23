# A sharp dimension cap for all-singular A4 source subspaces

October23,2026. Written, unreviewed, computer-assisted proof over C.
Prepared with OpenAI Codex under owner direction. No independent review,
formalization, target construction or exponent improvement is claimed.

## 1. Source and exact statement

Use the pinned cyclic source A4 with coefficient space A=C^112, indexed
by(i,k,s), where0<=i,s<=3 and0<=k<=6. Its112-square matrix slice has
rows(j,p,L), columns(H,q,r), and entry

    M(F)_((j,p,L),(H,q,r))=F_(H-j,p+q,L-r),               (1)

with F zero outside its allowed indices. Here j,p,q,r range0,...,3
and H,L range0,...,6. This is the maintained literal source convention.

**Theorem.** A complex linear subspace W of A whose every slice M(F)
is singular has dimension at most96. The bound is attained. Equivalently
every complex linear subspace of dimension at least97 contains an
invertible source slice.

The quantifier includes arbitrary dense complex subspaces. It is not
limited to coordinate subspaces, rational points or a finite search.
The proof uses sixteen explicit finite unit witnesses and a general
rank-preserving diagonal limit.

## 2. General packing lemma with a distinct-weight action

Let A have a coordinate basis e_1,...,e_n, and let X be a closed cone
in A invariant under a diagonal C* action with distinct integer weights.
Suppose there are m pairwise disjoint coordinate supports S_1,...,S_m,
each supporting a vector outside X. Then every linear subspace W
contained in X has dimension at most n-m.

To prove this, put W in row-echelon form in coordinates ordered by
increasing weight. For each pivot, scale its transformed basis vector by
the negative pivot weight. Every coordinate below the pivot is zero;
every surviving nonpivot coordinate has strictly larger weight. As
t tends to zero, these scaled vectors converge to the distinct pivot
coordinate vectors. They form a regular basis for the limiting subspace
W_0, which is the coordinate span on those pivots and has dimension dim W.

Every fixed linear combination of that regular basis lies in X for
nonzero t, by invariance and linearity of W. Closedness of X puts its
limit in X too. Hence W_0 is contained in X. This is an elementary
Grassmannian limit; no Borel fixed-point theorem is required.

If the complement of the pivot coordinates had fewer than m elements,
one of the m disjoint sets S_i would be fully contained in W_0's
coordinate set. Its witness outside X would then belong to W_0, a
contradiction. Thus codim W>=m.

The lemma needs a common diagonal action preserving X, distinct source
weights, disjoint supports, and actual witnesses outside X. An arbitrary
coordinate screen without these hypotheses does not imply the result.

## 3. A rank-preserving action for the full source

Give source coefficient(i,k,s) weight

    w(i,k,s)=i+4k+28s.

These are precisely112 distinct integers0,...,111. Substituting(1),
the weight of a nonzero matrix entry is

    (H-j)+4(p+q)+28(L-r)
       =(-j+4p+28L)+(H+4q-28r).                        (2)

Thus multiplying source coefficients by t^w multiplies M(F) on the
left and right by invertible diagonal Laurent matrices for every
t nonzero. In particular the action preserves matrix rank, and hence
the closed singular cone X={F:det M(F)=0}.

The source weights are deliberately different from the flattened index
order(i,k,s). Only their distinctness and the row/column decomposition
(2) are needed. The verifier checks(2) for every allowed matrix entry.

## 4. Sixteen disjoint exact unit witnesses

For each c,d in{0,1,2,3}, define F^(c,d) by

    F^(c,d)_(i,k,s)=1 if(i+s) mod4=c and k mod4=d,
                   0 otherwise.

The sixteen supports partition all112 source coordinates. Each matrix
M(F^(c,d)) has nonzero determinant modulo1009. The exported certificate
contains every support and modular determinant, with a literal-source
replay and complete modular elimination. Nonzero modular determinant of
an integer matrix proves its integer determinant nonzero, so all sixteen
matrices are invertible over C. This is an exact fixed finite certificate,
not a sampled inference about complex coefficients.

There is also an independent integer check. Reorder rows as(p,j,L) and
columns as(q,H,r). Each full matrix becomes H_d tensor K_c, where
H_d is the4-by4 permutation matrix with entry1 exactly when
(p+q) mod4=d, and K_c is the28-by28 matrix with entry1 exactly when
0<=H-j,L-r<=3 and(H-j+L-r) mod4=c. Exact integer determinants of
K_0,K_1,K_2,K_3 are respectively-1,1,-1,1. Thus all sixteen full
matrices have determinant of absolute value one. The verifier checks
this factorization on every matrix entry as well as modular elimination.

Apply the general packing lemma with n112,m16 and the singular cone
and action of Section3. It gives dim W<=112-16=96, for every complex
all-singular linear subspace W.

## 5. Sharpness

Take source row(j,p,L)=(0,0,0). Its only potentially nonzero entries
in(1) are F_(H,q,0), with0<=H,q<=3, on the sixteen distinct columns
(H,q,0). They are sixteen distinct independent source coefficients.
Set all those coefficients to zero. The resulting coordinate subspace
has dimension112-16=96 and every source matrix has this zero row.
It is therefore entirely singular and attains the bound.

This also agrees with the prior all-size minimum row-contraction rank16,
but the displayed kernel proves attainment directly. Sharpness concerns
the source linear-space cap, not attainability of any target degeneration.

## 6. A first-map leading-rank consequence

Consider any complete Laurent degeneration from A4 to M(10,10,11).
Assume its first lift F:Mat10 -> A is regular. Assume a constant
110-by109 injection H makes C H regular with rank109 limit; the
unselected long-map coefficients and the whole opposite long map B
may have arbitrary finite poles.

Then F_0(Mat10) consists entirely of singular source slices and has
dimension at most96. In particular a leading first-map rank at least97
is impossible in this chart.

Indeed, suppose this image contains an invertible source slice.
The polynomial det M(F_0(X)) in the100 target coordinates is then
nonzero. The target determinant det X is another nonzero polynomial.
Their product is nonzero in the integral domain C[Mat10]. Hence there
exists X_* for which both X_* and M(F_0(X_*)) are invertible.

The target slice at X_* is X_* tensor I11. A constant invertible target
row change makes that target slice the identity while preserving all
source minima, target dimensions and regularity of C H. The source
unit S=M(F(X_*)) is regular invertible at zero. Consequently C H and
S C H are both regular with rank109 limits. The
[partial-frame exclusion](../2026-10-23-partial-regular-frames/proof.md),
Section5, rules out this degeneration.

Therefore the entire leading source image is singular. The sharp cap
proved above bounds its dimension by96. No injectivity of F_0 was assumed.
The assertion also applies when C is entirely regular and its constant
rank is at least109. Tensor-leg symmetry gives the corresponding
statements after exchanging the long legs or choosing a different
matrix-target orientation.

This does not treat polar first maps or long maps without suitable
109-column regular frames. It does not construct any target with
leading rank96 or prove that this target bound is sharp. The general
degeneration and exponent questions remain open.

## 7. Attribution and verification boundary

The canonical cyclic source convention and earlier unit, minimum-rank
and ordinary-map proofs retain their credits and exact pins. The sixteen
residue-class units, elementary diagonal packing proof, sharp singular
space cap and its leading-rank consequence are local continuations.
The previous partial-frame theorem supplies the final Laurent exclusion.
No new external theorem is imported.

The verifier checks the finite unit certificates, all source weight
identities and the sharp zero-row kernel. Those exact finite checks
support, without formalizing, the all-complex-subspace diagonal limit
and the all-order Laurent application. The proof remains unreviewed.
