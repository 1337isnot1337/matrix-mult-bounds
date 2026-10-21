# A complete Laurent collision composed with the current matrix cores

## Constructed limit

For every integer `a>=3`, put `n=a-2` and let

\[
 J_3=\sum_{r+s+t=2}e_r\otimes e_s\otimes e_t,
 \qquad 0\le r,s,t\le2.
\]

The following explicit degeneration is available:

\[
 A(a,a)\ \rightsquigarrow\ (M_n\otimes J_3)\oplus M_1\oplus M_1.
 \tag{1}
\]

For A(8,8), the target has 110 coordinates on each leg and 1,298
nonzero coefficients. The [sparse Laurent maps](parity_structure_jet_collision_sparse.json)
contain 254 monomials per leg. A standard-library verifier contracts
them against all 262,144 source terms, retains every Laurent power,
and checks the full polynomial identity. All negative powers cancel
exactly, and every undesired constant coefficient is zero.

This is a positive singular-construction control using the existing
matrix cores. It is not the requested `M27 direct_sum M7` target and
does not improve the matrix multiplication exponent. The collision is
the elementary three-point coefficient-extraction identity; no
historical priority is claimed for it. The project-specific output is
its explicit composition with the recorded A(a,a) maps and its complete
Laurent coefficient certificate. There has been no external independent
review or formalization.

## The scalar collision and its exact remainder

For three variables on each leg write

\[
 P_X(t)=x_0+t x_1+t^2x_2,
\]

and define `P_Y,P_Z` in the same way. Consider the sum of three rank-one
tensors

\[
 \frac{P_X(\epsilon)P_Y(\epsilon)P_Z(\epsilon)
       +P_X(-\epsilon)P_Y(-\epsilon)P_Z(-\epsilon)
       -2x_0y_0z_0}{2\epsilon^2}.
 \tag{2}
\]

The constant numerator cancels, and the two evaluation points cancel
every odd degree. Consequently (2) is exactly

\[
 \sum_{r+s+t=2}x_ry_sz_t
 +\epsilon^2\sum_{r+s+t=4}x_ry_sz_t
 +\epsilon^4x_2y_2z_2.
 \tag{3}
\]

All indices range from zero to two. There are respectively six, six
and one coefficients in these three groups. This is a finite Laurent
identity, with no limiting error estimate needed to establish it.
The first factor is the trace tensor of `C[t]/(t^3)`: multiply the three
polynomials modulo `t^3` and read the coefficient of `t^2`.

The source of (2) is the diagonal tensor of size three. Assign the
first two leg maps the evaluation rows at nodes `1,-1,0`; put the
weights `1/2,1/2,-1` and the factor `epsilon^-2` on the third leg.
This explains both the pole and its exact cancellation. The finite
maps are invertible for every nonzero epsilon.

### Why this scalar control requires a singular limit

The three slices of `J_3` are linearly independent, and the first slice
is

\[
 S_0=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}.
\]

It is its own inverse. With the second slice, normalization gives

\[
 S_1S_0^{-1}=\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix}.
 \tag{4}
\]

This is a nonzero nilpotent matrix with nilpotence index three.
If a concise 3-by-3-by-3 tensor were an ordinary restriction of the
size-three diagonal tensor, all three maps would be invertible. After
choosing any invertible slice, its normalized slice matrices would
therefore be simultaneously conjugate to diagonal matrices. A nonzero
nilpotent matrix cannot be diagonalizable, contradicting (4).

Thus diagonal-three does not ordinarily restrict to `J_3`, while (2)
does degenerate to it. The border rank of `J_3` is exactly three: the
explicit limit supplies the upper bound and conciseness supplies the
lower bound. This argument concerns the scalar control's diagonal
source. It does not assert that the larger A(8,8) source has no other
ordinary realization of the same small jet tensor.

## Composing the collision with A(a,a)

The previously certified
[free-interior construction](parity_structure_free_interior.md) gives

\[
 A(a,a)\longrightarrow M_{a-1}\oplus M_{a-1}\oplus M_{a-2}.
\]

Restrict each of the first two matrix blocks to its leading `n`-vertex
block and its remaining diagonal scalar. This gives

\[
 A(a,a)\longrightarrow M_n\oplus M_n\oplus M_n\oplus M_1\oplus M_1.
 \tag{5}
\]

The three `M_n` maps use common source coordinates

| Core | Image of matrix unit `E_ij` |
| --- | --- |
| First | `F(i,j,0)` |
| Second | `F(a-1-i,2a-2-j,a-1)` |
| Third | `F(j+1,a-1,a-2-i)` |

Here `0<=i,j<n`. The two retained scalars are obtained by taking
`i=j=n` in the first and second rows. The third row's transpose
preserves the standard cyclic matrix multiplication orientation.
All three physical legs use the appropriate original source-column
permutations from the free-interior package.

Replace each scalar variable in (2) by an `n`-by-`n` matrix and take
the trace of the ordered product. Scalar evaluation parameters commute
with the matrices, so the same coefficient calculation proves (3),
with each coefficient replaced by a matrix trace. The matrix order
remains `X,Y,Z`; commutativity of the matrices is never assumed.
Keep the two scalar summands of (5) separate. This proves (1).

For a jet degree `d` and matrix entry `(i,j)`, the target row is
`d*n*n+n*i+j`. On the first two legs, core `c` receives the coefficient
`lambda_c^d * epsilon^d`, where `lambda=(1,-1,0)`. On the third leg it
receives

\[
 \tfrac12 w_c\lambda_c^d\epsilon^{d-2},
 \qquad w=(1,1,-2).
\]

The two scalar rows have constant coefficient one. The saved format
uses denominators `(1,1,2)`, so their third-leg numerators are two.
All other map coefficients are zero.

## Full exact replay

The verifier does not infer mixed-term cancellation from a saved
success flag. It loops over every original source term, expands the
three sparse Laurent maps, and collects integer numerator coefficients
indexed by `(epsilon_power,X_row,Y_row,Z_row)`.

For the A(8,8) instance, 650 source terms meet all three maps. Before
cancellation, powers -2 through 4 appear. After exact collection:

| Epsilon power | Nonzero coefficients | Meaning |
| ---: | ---: | --- |
| 0 | 1,298 | Six jet-index patterns times `6^3`, plus two scalars |
| 2 | 1,296 | Six jet-index patterns with total degree four |
| 4 | 216 | The all-degree-two pattern |

Every numerator is two and the common contraction denominator is two.
All other coefficients, including all negative powers and all mixed
scalar/matrix coefficients, are zero. Because the three displayed
supports are disjoint, the squared Frobenius error from the limit is
exactly `1296*epsilon^4+216*epsilon^8` for real epsilon.

The certificate also replaces one nonzero map numerator by twice its
value and verifies that the complete Laurent identity fails. The small
`a=3` instance is checked separately, alongside the scalar normalized
slice calculation (4).

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_collision.py
python -S -m unittest discover -s tests -p test_parity_structure_jet_collision.py -v
```

The [exact report](parity_structure_jet_collision_certificate.json) is
separate from the sparse map data. Both can be replayed without NumPy,
SymPy, a numerical tolerance or an external solver.

## Consequence for the next construction step

This control demonstrates a concrete cancellation mechanism: three
ordinary matrix components coalesce while diverging coefficients cancel,
and their limit contains the multiplication law of a nonreduced algebra.
It gives an exact template for Laurent coefficient bookkeeping on the
current source and for retaining an entire matrix core through such a
collision.

The composed family uses only 110 selected source directions per leg.
Postcomposing it cannot produce the 778-dimensional current target.
A useful larger construction must introduce additional original source
directions before taking the limit, while checking their negative and
constant mixed coefficients together with the core. The remaining
off-diagonal directions in the two `M7` blocks are one concrete set to
retain in the next extension; they are not part of this certified target.
