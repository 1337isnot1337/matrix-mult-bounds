# Independent exterior-kernel and slice-cokernel controls

Date: 2026-10-23. These exact controls were developed during the search
for the remaining C-leg comparisons. The later theorem in
[source_c_koszul.md](source_c_koszul.md) proves that the source has the
maximum possible C-leg Koszul rank in every degree. Consequently every
C degree now passes for every target of this format. The partial bounds
below remain independent evidence and reusable elementary arguments;
their inconclusive cases are not open Koszul tests.

## 1. Exterior multiples of the degree-one kernel

Write E for the exterior algebra of the 140-dimensional output space C.
The maps K_(C,p) are the homogeneous pieces of the E-module map

\[
B^*\otimes E\longrightarrow A\otimes E,
\qquad b\otimes\xi\longmapsto
\sum_i a_i\otimes T(a_i^*,b)\wedge\xi.
\]

Thus the kernel is closed under multiplication on the right by exterior
monomials. The sign follows directly from the displayed formula and
associativity of the wedge product.

The degree-one graph certificates give 428 independent kernel vectors
for the target. Each is an indicator vector on one ungrounded component.
Lift each vector to the global domain B* tensor C using the frozen block
offsets. The resulting supports are disjoint. The additive verifier
checks all 428 lifted vectors directly against the full unsplit tensor
coefficients, in addition to their block certificates.

Order monomials first by the B index and then by colexicographic order
on the exterior C monomial. In degree one, this is simply the ordered
pair (B index, C index). Let D_j be the C variables that occur as leading
monomials at B index j, and put d_j=|D_j|. The exact list is saved in
shadow_verification.json; its sum is 428.

Fix a p-element set J meeting D_j. Choose one k in J intersect D_j,
and multiply the relation with leading term b_j tensor c_k by the
wedge of J without k. Its leading monomial is b_j tensor c_J.
Indeed the leading term survives. Every other term either vanishes
or remains smaller: multiplication by a common disjoint set preserves
colex order, and the B index is unchanged by exterior multiplication.
The coefficient of the leading term is 1 or -1.

Choose one such product for each pair (j,J). All these leading monomials
are different, so the products are linearly independent. This proves

\[
\dim\ker K_{C,p}(T)\ge H_p
:=\sum_{j=0}^{99}
\left[\binom{140}{p}-\binom{140-d_j}{p}\right].
\tag{1}
\]

This is a lower bound. Products of the original relations can also
have additional independent linear combinations, which are not counted.

For p=5, the exact value in (1) is 4,930,805,426. The exact source
kernel has dimension binom(105,6)=1,609,344,100. Thus this elementary
certificate alone proves the C-degree-five comparison with a kernel
slack of 3,321,461,326.

## 2. A projected-source comparison

Index the source blocks by r=0,...,9. Identify their B polynomials with
one length-100 polynomial by

\[
(f_0,\ldots,f_9)\longmapsto\sum_{r=0}^9 z^{10r}f_r(z).
\]

Apply the same shifted sum to their output polynomials. The products
intertwine exactly, so this linear output projection takes the source
to Full(5,100), with third dimension 104. Embed that output into the
original 140-dimensional C space, leaving 36 unused coordinates.

The single Full(5,100) block has maximal matrix rank in every output
Koszul degree, by the elementary windows in source_koszul_tails.md.
Splitting each exterior power by the number of unused coordinates gives

\[
L_p=\sum_{j=0}^{103}
\min\!\left(100\binom{104}{j},5\binom{104}{j+1}\right)
\binom{36}{p-j}.
\tag{2}
\]

An output projection is a limit of invertible output maps. Koszul ranks
are invariant under invertible maps, and their minors are polynomial,
so projection cannot increase rank. Therefore rank K_(C,p)(S)>=L_p.
At the time of this calculation, (2) supplied the bounds

\[
U_p=100\binom{140}{p}-L_p
\quad\text{on the source kernel, and}\quad
V_p=5\binom{140}{p+1}-L_p
\quad\text{on its cokernel}.
\tag{3}
\]

The later source theorem proves rank K_(C,p)(S)=L_p, so these bounds
are in fact exact. That equality is not needed for the sufficient
comparisons in this note. Exact evaluation shows H_p>=U_p for p=5,6.
For p=7,...,39 the bound H_p alone is inconclusive.

## 3. Cokernel vectors from a basis of low-rank first slices

Fix a volume form on C and set q=139-p. Exterior duality identifies
the transpose of K_(C,p), up to the standard harmless signs, with

\[
A^*\otimes\Lambda^q C\longrightarrow
B\otimes\Lambda^{q+1}C.
\]

For a first covector alpha, let U_alpha be the image in C of its slice
B* -> C, and let r_alpha=dim U_alpha. If a q-wedge contains the full
r_alpha-dimensional space U_alpha, every slice coefficient wedges to
zero. This gives a kernel subspace of dimension

\[
\binom{140-r_\alpha}{q-r_\alpha}
=\binom{140-r_\alpha}{p+1},
\]

with out-of-range binomial coefficients interpreted as zero. If five
covectors form a basis of A*, their subspaces are independent in the
first factor. Their dimensions can therefore be added to bound the
original cokernel.

The five coordinate first slices have literal ranks
(62,68,72,68,62). They give the cokernel lower bound

\[
J_p^{\rm coord}
=2\binom{78}{p+1}+2\binom{72}{p+1}+\binom{68}{p+1}.
\tag{4}
\]

A stronger basis is provided by alpha(t)=(1,t,t^2,t^3,t^4) at
t=0,1,2,3,4. The Vandermonde determinant is nonzero. Each Full or
Mid block has its full smaller slice rank, and each shared-output
block has rank one because its entries are t^(j+k)=t^j t^k.
Every one of these five slices consequently has rank
44+12+6=62. This gives

\[
J_p^{\rm eval}=5\binom{78}{p+1}.
\tag{5}
\]

The verifier also checks the coordinate and evaluation slice ranks
by literal rational elimination, without relying on the formulas.
Comparison with V_p certifies p=12,...,39 using (4), and
p=11,...,39 using (5).

## 4. Historical coverage and current conclusion

| Independent sufficient comparison | Degrees certified in 5,...,39 |
| --- | --- |
| Degree-one kernel exterior multiples | 5,6 |
| Coordinate-slice cokernel | 12,...,39 |
| Evaluation-slice cokernel | 11,...,39 |
| Union of these bounds | 5,6 and 11,...,39 |

These elementary comparisons alone left degrees 7,...,10 undecided.
The all-degree source theorem now settles those degrees, and every
other C degree, as passing. A negative gap in the saved sufficient-bound
table means only that its chosen bound does not decide that comparison.
It is not a rank obstruction to the candidate.

The source projection and coordinate-slice argument were supplied by
the coordinating agent; the global leading-term calculation and
evaluation-basis improvement were developed by the frontier agent.
These are deductions in one owner-directed AI session. No independent
review, priority, construction, or exponent improvement is claimed.

Run `verify_shadow.py` to replay the exact result table. The additional
unit tests construct small exterior products explicitly, check them
against unsplit Koszul matrices, and verify their independence by
rational elimination. The large-degree witnesses are represented by
the exact counting proof, not expanded into billions of vectors.
