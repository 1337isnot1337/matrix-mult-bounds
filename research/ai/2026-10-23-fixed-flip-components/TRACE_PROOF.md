# Positive trace forbids further subset deletion in the five-split component

**Claim `AI-EXTERNAL-FIVE-SPLIT-TRACE-005`. Written proof, unreviewed.**

This continuation concerns the explicit
[five-split seed](../2026-10-23-flip-escape/five_split.md), whose constant
surviving tensor S and discarded tensor D satisfy

\[
M(4,5,5)=S+D.
\]

The construction already makes D tend to zero under a physical
stabilizer family. The present claim is that finite standard flips of
the 76 surviving terms cannot enable a further nonempty-subset deletion.
It does not concern the different four-split seed or all possible ways
of reducing border rank.

## 1. The isolated blocks remain isolated over Laurent fields

The companion component certificate partitions the five-split seed
into 53 blocks: 36 singletons, 15 pairs, and two blocks of size five.
For each block g, let A_g, B_g, C_g be its three factor spans. On every
leg, spans from distinct blocks have zero intersection. The exact proof
uses the full-rank concatenations modulo 101, so the corresponding
integer minors are nonzero over Q and C.

These same minors remain nonzero in every extension field of C, including
C((epsilon)). Thus extension of scalars preserves all the zero
intersections. Any nonzero common factor of two terms belongs to the
intersection of their block spans. Terms in different blocks therefore
cannot participate in a shared-factor flip over such a field.

A flip within one block makes linear combinations of that block's
factors. It preserves the block tensor and keeps every factor inside
its respective block span. Repeating this argument proves containment
for any finite sequence of standard flips, including coefficients that
are rational or formal Laurent functions. A term gauge multiplies its
three factors by nonzero scalars whose product is one, preserving the
rank-one tensor term exactly. Such gauges and permutations do not alter
the conclusion. A common invertible physical change maps
the block spans isomorphically and also preserves their intersections.

## 2. Every block decomposition has its minimum flattening term count

Fix a block with r terms. Write

\[
Z_i=U_i\otimes W_i,\qquad
S_g=\sum_{i=1}^{r}Z_i\otimes V_i,
\]

where this display permutes the tensor legs only for the flattening
argument. Both the Z_i and the V_i are independent, as the component
certificate checks. Thus the V-flattening of S_g has rank r.

After any of the allowed flips, the same block tensor still has r
displayed terms. Its V-flattening rank is still r. Therefore none of
these terms can be zero, both new lists are independent, and their spans
are exactly the original flattening image spaces. In particular the
new Z list lies in the r-dimensional space K_g=span(Z_i), even though
the ambient product A_g tensor C_g may be larger.

Let Z and V denote the matrices of the original basis columns. Every
new r-term factorization of this flattening has the form

\[
Z'=ZG,\qquad V'=VG^{-T},\qquad G\in\mathrm{GL}_r(F),
\]

over the chosen extension field F. To see this, express the new Z basis
in the old basis. The resulting invertible matrix G then uniquely
determines the V basis by equality of the two rank-r matrix
factorizations. The requirement that each Z'_i itself equal U'_i tensor
W'_i only restricts the possible matrices G; it cannot invalidate this
factorization identity. Thus the argument covers all standard flips.

The same rank argument forbids an exact zero-term or merge reduction
inside these isolated blocks. It does not prohibit a later singular
limit from changing a flattening rank.

## 3. Exact scalar trace pairings

On the permuted flattening define the bilinear pairing

\[
H(U\otimes W,V)=\operatorname{tr}(UVW).
\]

The stored integer certificate computes the complete matrix

\[
H_g(i,j)=\operatorname{tr}(U_i V_j W_i)
\]

for every one of the 53 blocks. It is c_g I_r, with c_g in {1,2}.
The two new five-term blocks have c_g=1:

\[
\{16,54,57,60,63\},\qquad
\{31,47,48,51,52\}.
\]

The new pair {26,32} also has c_g=1. Counting all terms with multiplicity
gives 52 traces equal to one and 24 equal to two.

For the refactorization in Section 2, the new pairing matrix is

\[
H'_g=G^T H_gG^{-T}=c_g I_r.
\]

Consequently every individual tensor term retains trace c_g after
every allowed finite flip sequence. This identity holds over arbitrary
characteristic-zero extension fields, including Laurent fields. It
places no bound on the size, pole order, or complex arguments of the
flip coefficients. Term gauges preserve the complete term trace.

## 4. Include the original discarded error in the invariant

For a tensor E define the linear functional

\[
L(E)=\sum_a\operatorname{tr}(A_aB_aC_a)
\quad\text{when}\quad E=\sum_aA_a\otimes B_a\otimes C_a.
\]

This is independent of the displayed decomposition because it is a
linear contraction of tensor coordinates. It is invariant under the
physical changes

\[
(U,V,W)\mapsto(R^{-1}US,S^{-1}VT,T^{-1}WR).
\]

The five original discarded terms each have trace zero, which the
certificate checks directly. Hence L(D)=0 before and after any common
physical change or parameter substitution.

Let T be a nonempty subset of the surviving terms after any allowed
finite flips. The preceding sections give

\[
L(D+T)=L(D)+L(T)=\sum_{i\in T}c_{g(i)}>0.
\]

This is a fixed positive integer, also when the factor coefficients
depend on a Laurent parameter. Deleting T leaves
S-T=M-(D+T). Since the physical action fixes M, obtaining M as its limit
would require D+T to tend to zero. The nonzero invariant L makes that
impossible. The argument permits cancellation between D and T; it does
not assume that the individual discarded terms tend to zero separately.

The same proof works if physical changes are interleaved with flips.
Their linear action commutes with the shared-factor refactorizations,
and the trace pairing and block intersections are preserved throughout.

## 5. Verification and limits

Run `python research/ai/2026-10-23-fixed-flip-components/trace_invariant.py`.
It checks the source pin, exact five replacements, all block span and
flattening certificates, every integer pairing entry, and all five
discarded traces. `trace_certificate.json` retains the complete pairings.

This is a written unreviewed proof with exact finite input certificates.
It closes further nonempty-subset deletion by the physical stabilizer
after finite standard flips of this one five-split seed. New splits,
other seeds, nonstandard changes of decomposition, and limits in which
nonzero terms merge are outside the statement. The four-split component
has nonscalar trace pairings and is not excluded by this argument.
No general border-rank lower bound, matrix target, exponent improvement,
historical priority, formalization, or independent review is claimed.

The original exact matrix algorithm and the nilpotent-factor deletion
viewpoint retain the external attribution in the split package. The
scalar-pairing refactorization argument is the local continuation of
the earlier closed-component proof, with its hypotheses enlarged from
common-W pairs to complete minimum-rank V-flattening blocks.
