# An exact coupled repair of two endpoint responses

Claim ID: **AI-SPIN-DOUBLE-ENDPOINT-121**.

## Status and recovery scope

There are explicit ordinary rational maps

\[
A(8,8)\longrightarrow M(3,3,27)
\tag{1}
\]

whose complete first response vanishes at both \(F(7,0,7)\) and
\(F(7,2,7)\). Its response is supported on the other 190 coordinates
with long index \(k<3\), and its exact rank is 190. The preimage of the
current nine-dimensional first target leg consequently has dimension 779.

The first implementation of this claim was lost in a filesystem rollback.
Its recorded map hash was
`e2cc86faa681bbaccec8405fafe4d6c1918016f2d024d2c05bc146884cc2ee9f`.
This package reconstructs the same theorem with **fresh rational graph
coefficients**. It does not claim to reproduce the lost byte sequence or
its full map entries. The deleted channels and two orthogonal graph spaces
were retained from that construction; the boundary complement was rebuilt.

All accepted computations use Python integers and rational arithmetic in
the standard library. This is local work generated in the current session,
with no historical priority claim or external independent review.
Neither the dimension 779 nor the rectangular identity (1) constructs a
full target that improves the matrix multiplication exponent.

## 1. Exact graph changes of the balanced module

Start with the [balanced 32-channel module](parity_balancing_spin44.md).
Write its maps as \(X_{IJ},Y_{J\alpha},Z_{I\alpha}\), where
\(I,J<3\) and \(\alpha<32\). Its source contraction is

\[
T(X_{IJ},Y_{J'\alpha},Z_{I'\beta})
=\delta_{I,I'}\delta_{J,J'}\delta_{\alpha,\beta}.
\tag{2}
\]

Delete the five middle channels

\[
D=(0,4,8,16,24)
\]

and retain all other channels in increasing order. The retained Y and Z
rows are denoted \(Y_R,Z_R\), each with 81 rows. Keep the original nine
X rows. Let

\[
S=\begin{pmatrix}1&0&0&-2&1\\0&1&0&2&2\\0&0&1&0&2\end{pmatrix},
\qquad
U=\begin{pmatrix}2&-2&0&1&0\\-1&-2&-2&0&1\end{pmatrix}.
\tag{3}
\]

The letter U here is the matrix saved under the JSON key `T`.
Direct integer multiplication gives \(SU^T=0\).
For each old outer vertex, combine its five omitted Y rows using the
three rows of S. Across the three outer vertices this gives nine rows
\(G_Y\). Similarly use the two rows of U to form six omitted-row
combinations \(G_Z\).

For arbitrary matrices \(A\in\mathbb Q^{81\times9}\) and
\(B\in\mathbb Q^{81\times6}\), set

\[
Y'=Y_R+A G_Y,\qquad Z'=Z_R+B G_Z.
\tag{4}
\]

Every term of (2) with one retained channel and one omitted channel is
zero. A term with both corrections has coefficient equal to a linear
combination of entries of \(SU^T\), for each possible pair of outer
vertices. Hence it is also zero. Therefore (4) preserves the complete
\(M(3,3,27)\) identity for every A and B. This permits arbitrary mixing
of outer indices in the correction coefficients.

## 2. The two endpoint forms reduce to 18 boundary coordinates

Both old maps and all omitted-row combinations remain in their literal
low supports: Y has physical first index \(p<2\) and long index at most
9, and Z has physical last index \(q<2\) and long index at most 9.
At a first source coordinate \(F(7,k,7)\), the source equations give

\[
\sum_{p+q=k}\sum_{r,j=0}^7 Y(p,7+r,j)Z(r,7+j,q).
\tag{5}
\]

The low long-index supports reduce r and j to \(0,1,2\).
For k=0 only \((p,q)=(0,0)\) remains; for k=2 only \((1,1)\)
remains. Each endpoint is thus a nine-coordinate dot product. Order
the combined boundary coordinates by

\[
\begin{aligned}
Y &: (p,r,j),\quad p<2,\ r,j<3,\quad F(p,7+r,j),\\
Z &: (q,r,j),\quad q<2,\ r,j<3,\quad F(r,7+j,q).
\end{aligned}
\tag{6}
\]

The first nine coordinates belong to the first endpoint, and the last
nine to the second. All matrices in the rest of this section can be
formed from integer map numerators; their common base denominators
cancel out of the zero equations.

Let \(F\in\mathbb Z^{9\times18}\) be the boundary of \(G_Y\), and
\(G\in\mathbb Z^{6\times18}\) the boundary of \(G_Z\). Write the
retained numerator boundaries as \(R_Y,R_Z\in\mathbb Z^{81\times18}\).
The generator chooses an explicit five-row integer matrix L, saved
under `split_boundary_section` in
[the witness](../../../results/anisotropic-constructions-2026-10-20/parity_structure_spin44_double_endpoint_witness.json).
Its first two rows have support in the first nine coordinates, and its
last three rows in the final nine. The following exact properties hold:

\[
C=\begin{bmatrix}G\\L\end{bmatrix}\text{ has row rank }11,
\quad R_Z\subseteq\operatorname{rowspan}C,
\quad FL^T\text{ has column rank }5.
\tag{7}
\]

The first two assertions allow a unique decomposition

\[
R_Z=C_GG+C_LL.
\tag{8}
\]

Set \(B=-C_G\). The changed Z boundary is then \(C_LL\).
The last assertion in (7) permits a rational solution of

\[
AFL^T=-R_YL^T.
\tag{9}
\]

Consequently the changed Y boundary \(R_Y+AF\) annihilates all rows
of L. Since L is split between the two disjoint endpoint blocks,
each of the two forms in (5) vanishes separately for every changed
Y/Z target-row pair. This proves the two endpoint cancellations.

For reproducibility, the generator derives (8) from an invertible
11-by-11 column submatrix of C. It derives (9) from an invertible
5-by-5 row submatrix of \(FL^T\), setting the other four correction
coordinates to zero. Every operation is over \(\mathbb Q\).
The witness contains the resulting A and B, both selected submatrices,
and the actual integer section L. The accepted verifier also rebuilds
all maps from those graph factors and the pinned base-map bytes.

## 3. Complete source replay and exact rank

The actual rational maps have common denominators

\[
(2,\ 1{,}026{,}009{,}600,\ 72)
\]

and respectively \((16,8962,2654)\) nonzero entries.
These coefficients differ from the lost original implementation.
The complete verifier iterates all 262,144 original source terms,
checks all 59,049 target coefficients, and verifies exactly 243 unit
terms with every other coefficient zero.

It separately builds the first response for every original source
coordinate. The actual nonzero support is

\[
\{F(i,k,s):i,s<8,\ k<3\}\setminus
\{F(7,0,7),F(7,2,7)\}.
\tag{10}
\]

This gives a rank upper bound of 190. A saved 190-by-190 minor of the
actual integer response matrix has determinant 24842 modulo 65521.
The nonzero residue proves a matching rank lower bound over \(\mathbb Q\).
The verifier recomputes the entire minor, including all response entries;
it does not accept a saved rank assertion.

The first kernel therefore has dimension \(960-190=770\).
Its coordinate basis is the 768 coordinates with \(k\geq3\), together
with the two killed endpoints. The target's nine first images have
independent responses by the exact matrix-tensor identity. The preimage
of their span has dimension \(770+9=779\).
This is a necessary allowance for potential extensions retaining these
Y/Z rows. The remaining compatible target entries are unconstructed.

## 4. Reproduction and limitations

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin44_double_endpoint_generate.py
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_spin44_double_endpoint.py
python -S -m unittest discover -s tests -p 'test_parity_structure_spin44_double_endpoint.py' -v
```

The generator, verifier and tests require only the standard library.
The tests include a nonzero-to-nonzero map tamper, a changed graph
coefficient, and a changed nonzero-minor residue. The current saved
maps are an ordinary rational restriction; no limiting parameter or
approximate coefficient equality is used.

Recovery and rerunning checks do not count as a new theorem beyond
claim 121. The new coefficient choice is explicitly identified so
the old and recovered artifacts cannot be confused.
