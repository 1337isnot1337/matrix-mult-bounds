# The standard-flip component of the pinned rank-76 seed

**Claim `AI-EXTERNAL-FLIP-COMPONENT-001`. Written proof, unreviewed.**

Work over the complex numbers. The same argument holds over any
characteristic-zero field. The input is exactly the 76-term integer
M(4,5,5) decomposition retained in the
[external seed package](../2026-10-21-external-grid-seed/README.md).
Its SHA-256 is recorded in `sources.json` and checked before replay.

## 1. Statement and allowed moves

A standard shared-factor flip replaces two terms with a common factor
by an invertible two-term refactorization on the other two legs. For
example, with common W, write the terms as

\[
 (U_1\otimes V_1+U_2\otimes V_2)\otimes W.
\]

For any \(G\in\mathrm{GL}_2(\mathbb C)\), replace the two lists by
\(U'=UG\) and \(V'=VG^{-T}\). Their sum is unchanged. Elementary
shared-factor flips are particular cases. A term gauge rescales its
three factors by nonzero scalars whose product is one. Reordering terms
is also allowed. Rank-increasing splits are not allowed in this section.

**Theorem.** After any finite sequence of these moves on the pinned seed:

* every flip still occurs inside one of the original proportional-W
  classes;
* no term is zero, and no proportional pair can be merged to reduce rank;
* each term has \(\operatorname{tr}(UVW)\) equal to its original class
  scalar, either one or two;
* no nonempty subset of the resulting terms can tend to zero under the
  physical matrix-multiplication stabilizer.

The conclusion concerns this move component. It does not exclude other
decompositions, rank-increasing moves, or general degenerations.

## 2. Exact input certificates

Interpret U, V, W as matrices of sizes 4-by-5, 5-by-5 and 5-by-4. Flatten
each matrix in row-major order. Normalize the first nonzero W entry to
one, moving its original sign into U. There are 58 proportional-W
classes: 40 singletons and 18 pairs. The paired term indices are
zero-based:

```
(18,25) (22,29) (33,34) (35,37) (38,39) (40,41)
(47,48) (49,68) (50,53) (51,52) (54,57) (55,73)
(56,75) (58,59) (60,63) (61,62) (64,74) (69,72)
```

For each class g, let A_g and B_g be the spans of its U and V vectors.
For every distinct pair g,h, the concatenated U lists and concatenated
V lists are linearly independent. The certificate supplies one maximal
minor with determinant +1 or -1 for each concatenation. There are
\(2\binom{58}{2}=3306\) witnesses. The verifier evaluates every determinant
by its permutation formula, independently of the unit-pivot method
that generated the witness columns. In particular,

\[
A_g\cap A_h=0,\qquad B_g\cap B_h=0.
\]

These finite independence facts hold over every field. They also show
that the U and V lists inside each paired class are independent.

For normalized W_g, define the class trace pairing

\[
C_g(a,b)=\operatorname{tr}(U_{g,a}V_{g,b}W_g).
\]

Direct integer replay gives \(C_g=c_g I\), where c_g is one or two.
Counting terms with multiplicity gives 52 values one and 24 values two.
The complete certificate stores the class membership and unit minors;
the verifier recomputes every trace pairing directly from the seed.

## 3. Closure under arbitrary finite standard flips

Initially, terms from distinct classes cannot share a U direction or a
V direction, because their spans intersect trivially. They cannot share
a W direction by the definition of the classes.

Suppose this remains true after some moves. A new shared-factor flip
must occur inside one class. A singleton admits none. A paired class
has independent U and V lists, so only W can be the shared factor.
The invertible refactorization leaves both spans A_g and B_g unchanged
and keeps each list independent. Thus its factors remain nonzero and
cannot become proportional within that class. Its W direction is also
unchanged. The cross-class span intersections remain trivial.

Induction proves closure for every finite sequence. Term gauges do not
change any of these spans or proportionality properties. No zero term
or pair with two shared factor directions appears, so the usual exact
rank reductions are unavailable. This does not assert global optimality
of rank 76.

## 4. Trace invariance inside each class

In normalized coordinates a class refactorization has

\[
U'_a=\sum_i U_iG_{ia},\qquad
V'_b=\sum_j V_j(G^{-1})_{bj}.
\]

Its complete trace pairing is

\[
C'_g=G^T C_gG^{-T}=c_g I.
\]

In particular every new term still has trace c_g. This identity is
valid for arbitrary complex invertible G, with no integrality or
bounded-coefficient assumption. Term gauges preserve the trace of the
complete term as well.

## 5. Physical stabilizer deletion is impossible in this component

The physical action uses invertible matrices R, S, T of sizes 4, 5, 5:

\[
U\mapsto R^{-1}US,\quad
V\mapsto S^{-1}VT,\quad
W\mapsto T^{-1}WR.
\]

It preserves \(\operatorname{tr}(UVW)\). On a sum of rank-one tensor terms,
the functional

\[
L\left(\sum_iU_i\otimes V_i\otimes W_i\right)
=\sum_i\operatorname{tr}(U_iV_iW_i)
\]

is linear and invariant. Every nonempty subset in the flip component
has L equal to a positive integer. Its physical stabilizer orbit closure
therefore does not contain zero: the equation L=constant remains valid
under limits. Equivalently, no Laurent parameter family of physical
changes can make that subset have only positive coefficient valuations.
Each individual product UVW is also non-nilpotent, since its trace is
nonzero.

The characteristic-zero hypothesis matters for this last conclusion.
Positive integer traces can vanish in positive characteristic; the
field-independent unit minors do not remove that limitation.

## 6. Attribution and verification scope

The matrix multiplication algorithm is external work by Fawzi et al.
(Nature, 2022), using the pinned conversion credited in the seed package.
The standard-flip and stabilizer-null-cone viewpoints are described by
[Dumitriu et al., arXiv:2610.13905v1, Sections 2.1--2.3](https://arxiv.org/html/2610.13905v1).
The local contribution is the exact class certificate and this scoped
component proof. The proof uses elementary linear algebra and the trace
invariant; it does not need the external paper's general null-cone theorem.

Run `python research/ai/2026-10-23-flip-escape/verify_component.py` from
the repository root. The command checks the seed hash, every class pair,
all 3306 unit minors, and every class trace pairing. Unit tests also
reject a changed determinant and a missing witness, and exercise a
nontrivial rational two-term refactorization. These are finite exact
controls, not independent mathematical review.
