# A cube determinant excludes a saturated degree-13 pair

## Statement

Consider an ordinary grading-preserving restriction of `A(8,8)` to a
matrix multiplication tensor with three possibly different vertex
charge lists, each supported on the integers 0 through 14. The source
weight is `i+s-k` as in
[the degree-13 pencil proof](torus_degree13_pencils.md). Other direct
summands of the target are allowed if they have no coordinates at
weights 13, -13, 14, or -14.

Suppose every vertex list has exactly one vertex at charge 0 and one
at charge 14. If one intermediate vertex list has two vertices at
charge 13, and the other two vertex lists each have one vertex at
charge 1, then no such restriction exists. The reflected statement
also holds: two vertices at charge 1 are impossible when the other
two lists each have one vertex at charge 13.

The lists can differ on every other charge. This result concerns
ordinary maps, and does not exclude arbitrary singular limits.
It is a local compatibility obstruction, not an improved exponent.
The argument was checked by the parent and another agent in this
generating session; no external independent review or formalization
has occurred.

## Two saturated blocks and one target input

Let the intermediate vertex space be `V_j`, and use the consecutive
target legs `Hom(V_j,V_i)` and `Hom(V_k,V_j)`. The negative degree-13
subspace of the first leg consists of two units from charge 13 in
`V_j` to charge 0 in `V_i`, and one unit from charge 14 in `V_j` to
charge 1 in `V_i`. Its dimension is three. The positive degree-13
subspace of the second leg has the transposed pattern: two units
from charge 0 in `V_k` to charge 13 in `V_j`, and one from charge 1
in `V_k` to charge 14 in `V_j`. It too has dimension three.

The source weight blocks at both degrees have dimension three.
Because a map realizing a concise target tensor is injective, the
two maps on these blocks must be isomorphisms. The source bilinear
slice for a third input is therefore subject only to independent
invertible row and column transformations.

In the bases `P,Q,R` and `P',Q',R'` of the linked proof, that source
slice is

\[
 G=\begin{pmatrix}
 v&h&a\\
 a&0&0\\
 w&a&0
 \end{pmatrix},
 \qquad a=F(0,7,7).
 \tag{1}
\]

In particular,

\[
 \det G=a^3.
 \tag{2}
\]

Take the third target input to be the matrix unit between the
charge-zero endpoints of `V_i` and `V_k`, in the trace-compatible
order. The extreme degree -14 unit on the first target leg and
the extreme degree +14 unit on the second multiply to a unit whose
trace with this third input is one. Their source images are nonzero
scalar multiples of `F(0,14,0)` and `F(7,0,7)`. The physical product
is the diagonal unit at `(0,7)`, so the complete tensor identity
forces `a` on the lifted third input to be nonzero. No normalization
of either extreme coefficient is used.

By (2), the source slice consequently has rank three. The target
slice at that input is, in the ordered bases just described,

\[
 \begin{pmatrix}1&0&0\\0&1&0\\0&0&0\end{pmatrix}.
 \tag{3}
\]

It has rank two: the two channels through the intermediate charge-13
space contribute, while the channel joining the outer charge-one
vertices does not. Invertible changes on the first two blocks cannot
change rank. The ranks in (1) and (3) therefore contradict the
restriction identity.

The positive-negative product table has the same pattern with
`b=F(7,7,0)` in place of `a`. Testing the charge-14 endpoint gives
the reflected assertion. Equivalently, apply the exact source and
target charge-reflection symmetries.

## Consequence when the four boundary multiplicities are positive

Suppose all three vertex lists have positive multiplicities at
charges 0, 1, 13, and 14, and no charges outside the interval 0 to 14.
Dimension one of the source extreme blocks first forces every
endpoint multiplicity at charges 0 and 14 to equal one. Write
`l_j=m_j(1)` and `h_j=m_j(13)`.

The dimensions of the degree-13 target blocks on consecutive legs
are sums of the form `h_j+l_i`. They are at most the source dimension
three. Since every `h_j,l_i` is positive, every one is at most two.
If some `h_j` were two, the two other `l` values would each be one,
and the theorem would give a contradiction. If some `l_j` were two,
the reflected theorem would give the same contradiction. Thus

\[
 m_j(0)=m_j(1)=m_j(13)=m_j(14)=1
 \quad\text{for every vertex space }j.
 \tag{4}
\]

The positivity hypothesis is essential to this deduction. For
example, if one adjacent charge-one multiplicity is zero, only one
of the two degree-13 maps need be an isomorphism, and this proof
does not apply. Such profiles remain part of the construction search.
This note also does not replace the separate degree-13 pencil proof
for the earlier profile, whose two degree-13 target blocks both had
dimension two.

## Exact controls

`torus_saturated_pencil.py` checks the determinant identity as a
formal polynomial, rechecks the 18 ordered source-coordinate products,
and reconstructs the target rank-two slice from matrix-unit products.
It also checks 48 exact numerical specializations with arbitrary
nonzero boundary coefficients. The latter checks are controls; the
formal identity and rank argument give the universal statement.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/torus_saturated_pencil.py
python -S -m unittest discover -s tests -p test_torus_saturated_pencil.py -v
```

The exact report is
`results/anisotropic-constructions-2026-10-20/torus-saturated-pencil.json`.
