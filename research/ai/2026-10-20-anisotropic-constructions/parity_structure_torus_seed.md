# Exact torus seed for the A(8,8) target

October 21, 2026. The explicit monomial maps below give

\[
A(8,8)\longrightarrow M_{12}\oplus M_3.
\]

They embed as an exact partial target in the currently unconstructed
\(M_{27}\oplus M_7\) target. They do not establish that full restriction
or an improved matrix multiplication exponent. The seed core may move
in a subsequent search; retaining its maps is not a construction premise.

## The complete seed

Use source coordinates

\[
X=(i,p+q,s),\qquad Y=(j,p,r+s),\qquad Z=(i+j,q,r),
\]

with all six short indices from 0 through 7. Source leg dimensions are
960. The common torus charges, after the displayed cyclic ordering, are

\[
i+s-k,\qquad j+p-u,\qquad q+r-v.
\]

For the large seed block take the monomial spaces

\[
U=(1,x,x^6,x^7),\qquad V=(1,x^2,x^4).
\]

Their twelve products are precisely the monomials of degrees 0 through
11, without repetition. Write their exponents as \(u_\alpha,v_\beta\),
and index twelve vertices by \((\alpha,\beta)\). The dual product
functional is the coefficient of degree \(u_\alpha+v_\beta\).
The three source maps for target edge \(I=(\alpha,\beta)\),
\(J=(\gamma,\delta)\) select

\[
\begin{aligned}
X_{IJ}&=(u_\alpha,u_\gamma+v_\beta,v_\delta),\\
Y_{IJ}&=(v_\delta,u_\alpha,u_\gamma+v_\beta),\\
Z_{IJ}&=(u_\gamma+v_\beta,v_\delta,u_\alpha).
\end{aligned}
\]

The twelve vertex charges \(u_\alpha-v_\beta\) are distinct and fill
the interval from −4 through 7. Every map entry has coefficient 1.

For the small seed block, indexed by vertices 0, 1, 2, select

\[
X_{ij}=(7-i,14-j,7),\quad
Y_{ij}=(7,7-i,14-j),\quad
Z_{ij}=(14-j,7,7-i).
\]

The vertex charges are \((0,-1,-2)\). Direct substitution in the six
source indices gives exactly the 27 terms of \(M_3\).

There are no mixed terms. A term with two large-block legs and one
small-block leg would require a product of U and V to have degree at
least 12; every such product has degree at most 11. For a term with
two small-block legs and one large-block leg, the large leg contributes
a V exponent at most 4. Its paired short index is at most 7, so their
sum cannot reach the small block's long indices 12 through 14. This
argument applies in each of the three cyclic positions.

Consequently each leg map has shape 153 by 960 and exactly 153 entries,
all equal to 1. The image has exactly \(12^3+3^3=1755\) nonzero tensor
coefficients.

## The live target charge profile

The parent agent supplied this common profile at all three target
vertices. The 27-vertex block has the following multiplicities at
charges 0 through 14:

\[
(1,1,2,2,2,2,2,3,2,2,2,2,2,1,1).
\]

The seven-vertex block has one vertex at each charge from 0 through 6.
The exact per-leg charge capacities are:

| Absolute charge | Source dimension | Target dimension | Remaining dimension |
|---:|---:|---:|---:|
| 0 | 64 | 60 | 4 |
| 1 | 63 | 56 | 7 |
| 2 | 61 | 53 | 8 |
| 3 | 58 | 48 | 10 |
| 4 | 54 | 43 | 11 |
| 5 | 49 | 38 | 11 |
| 6 | 43 | 31 | 12 |
| 7 | 36 | 26 | 10 |
| 8 | 28 | 20 | 8 |
| 9 | 21 | 16 | 5 |
| 10 | 15 | 12 | 3 |
| 11 | 10 | 8 | 2 |
| 12 | 6 | 5 | 1 |
| 13 | 3 | 2 | 1 |
| 14 | 1 | 1 | 0 |

The table is symmetric in the sign of the charge. Every target charge
space fits. This is a necessary dimension check only. The unrestricted
maps within these charge spaces have 114,666 coefficients across all
three legs.

Embed the twelve seed vertices by shifting their charges by 5, so
they occupy one vertex at every charge from 1 through 12 in the
27-vertex block. Embed the three small seed vertices by shifting
their charges by 2 in the seven-vertex block. These blockwise shifts
leave edge charges unchanged. The exported full-format maps have
shape 778 by 960 and retain all 1755 seed coefficients exactly.
Their squared relative residual from the full target is exactly

\[
\frac{18271}{20026},
\qquad 20026=27^3+7^3.
\]

## Extreme-charge positive control

An additional exact control realizes \(M_2\) with vertex charges
0 and 14. In the common physical ordering \(F_{i,k,s}\), its four
matrix units select

\[
E_{00}:F_{0,7,7},\quad E_{01}:F_{0,14,0},\quad
E_{10}:F_{7,0,7},\quad E_{11}:F_{7,7,0}.
\]

The source Y and Z legs use the cyclic permutations of these same
physical coordinates. The charge ±14 maps are opposite physical
matrix units. Their degree-zero partners also have entries outside
that two-dimensional physical corner, but the full coefficient replay
checks that these entries create no additional cubic coefficients.
This control is separate from the \(M_{12}\oplus M_3\) seed; their
maps are not asserted to coexist with both cores fixed.

## Exact replay and exports

`parity_structure_torus_seed.py` uses only the Python standard library
for generation and exact replay. It checks every one of the 262,144
source terms against both the full seed tensor and its embedded partial
target, checks all map charges and the complete capacity table, and
rejects a coefficient changed from 1 to 2. It also checks all eight
coefficients of the extreme-charge M2 control.

The complete sparse maps are in
`parity_structure_torus_seed_sparse.json`, and the recomputed results
are in `parity_structure_torus_seed_certificate.json`. The optional
`--npz` flag exports NumPy initializers without making NumPy a replay
dependency. `parity_structure_torus_seed_maps.npz` contains the 153-row
seed; `parity_structure_torus_target27_7_maps.npz` contains the 778-row
embedded partial target.

Run the maintained exact replay with:

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_torus_seed.py
```

The construction and coefficient replay were produced in this generating
session. The target charge profile was supplied by another agent and
recomputed here. No external independent review or formalization is
claimed.
