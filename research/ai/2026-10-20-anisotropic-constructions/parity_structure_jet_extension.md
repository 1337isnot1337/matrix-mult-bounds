# A Laurent collision retaining both off-diagonal matrix arms

Put `n=a-2`, for an integer `a>=3`. The exact
[free-interior maps](parity_structure_free_interior.md) give

\[
A(a,a)\longrightarrow M_{n+1}\oplus M_{n+1}\oplus M_n.
\tag{1}
\]

The [first collision](parity_structure_jet_collision.md) retained
`3n^2+2` directions from (1). This extension retains all

\[
D=3n^2+4n+2=2(n+1)^2+n^2
\]

directions on every leg. It produces the explicit tensor below, with
all Laurent coefficients checked against the original source.
For A(8,8), `n=6` and `D=134`. This remains a constructive control,
not the 778-dimensional `M27 direct_sum M7` target and not an exponent
improvement. It supplies a concrete limit in which matrix cores and
their off-diagonal interactions survive together. No historical
priority is claimed for coefficient-extraction collisions.

## 1. The limiting tensor

On each of the three target legs use three n-by-n matrices
`X_0,X_1,X_2`, two n-by-1 columns `u_X,c`, two 1-by-n rows `v_X,c`,
and two scalars `d_X,c`, where `c=+,-`. Use the same naming convention
on legs Y and Z. Define

\[
\begin{aligned}
L_n={}&\sum_{r+s+t=2}\operatorname{tr}(X_rY_sZ_t)\\
&+\sum_{c\in\{+,-\}}\bigl[
\operatorname{tr}(X_0u_{Y,c}v_{Z,c})
+\operatorname{tr}(u_{X,c}v_{Y,c}Z_0)
+\operatorname{tr}(v_{X,c}Y_0u_{Z,c})
+d_{X,c}d_{Y,c}d_{Z,c}\bigr].
\end{aligned}
\tag{2}
\]

The first sum has six matrix traces. The remaining six matrix/column/row
terms retain every off-diagonal variable from the first two blocks of
(1). The two scalar terms are separate summands. Thus the claimed
degeneration is

\[
A(a,a)\ \rightsquigarrow\ L_{a-2}.
\tag{3}
\]

All `D` directions are necessary in (2): on every flattening, distinct
rows have disjoint nonempty coefficient supports. The exact verifier
checks this statement on the complete constant coefficient tensor.
In particular, the limit has not silently discarded any of the added
off-diagonal directions.

## 2. Maps and all remainder terms

Use parameter `t` and put

\[
P_X(z)=X_0+zX_1+z^2X_2.
\]

For the first two matrix blocks of (1), with `c=+1,-1`, the first two
leg maps are

\[
X\longmapsto
\begin{pmatrix}
P_X(ct^3)&t^3u_{X,c}\\
2t^3v_{X,c}&t^2d_{X,c}
\end{pmatrix},
\qquad
Y\longmapsto
\begin{pmatrix}
P_Y(ct^3)&t^3u_{Y,c}\\
2t^3v_{Y,c}&t^2d_{Y,c}
\end{pmatrix}.
\tag{4}
\]

The third leg map on that block is

\[
Z\longmapsto \frac1{2t^6}
\begin{pmatrix}
P_Z(ct^3)&t^3u_{Z,c}\\
2t^3v_{Z,c}&2t^2d_{Z,c}
\end{pmatrix}.
\tag{5}
\]

On the last, n-by-n block of (1), use `X_0,Y_0,-Z_0/t^6`.
The first two block traces therefore cancel the degree-zero and all
odd-degree terms of the core evaluation sum, exactly as in the
three-point collision.

Expanding these three block traces gives, with matrix order preserved,

\[
\begin{aligned}
T(t)={}&L_n
+t^6\sum_{r+s+t'=4}\operatorname{tr}(X_rY_sZ_{t'})
+t^{12}\operatorname{tr}(X_2Y_2Z_2)\\
&+\sum_{c=\pm1}\sum_{r=1}^2 c^r t^{3r}
\bigl[
\operatorname{tr}(X_ru_{Y,c}v_{Z,c})
+\operatorname{tr}(u_{X,c}v_{Y,c}Z_r)
+\operatorname{tr}(v_{X,c}Y_ru_{Z,c})\bigr]\\
&+t^2\sum_{c=\pm1}\bigl[
d_{X,c}v_{Y,c}u_{Z,c}
+d_{Y,c}v_{Z,c}u_{X,c}
+2d_{Z,c}v_{X,c}u_{Y,c}\bigr].
\end{aligned}
\tag{6}
\]

All degree indices lie in `0,1,2`. The symbol `t'` in the first sum
is an index, distinct from the parameter `t`. Every term after `L_n`
has strictly positive parameter degree. Formula (6) proves the limit,
including cancellation of all negative powers and all unwanted
constant mixed coefficients.

For nonzero `t`, the maps on the D selected source directions are
invertible. The core entries use the invertible evaluation matrix at
the three distinct points `t^3,-t^3,0`; each arm and scalar direction
has its own nonzero diagonal scale. Thus the construction is a
contraction of the full intermediate tensor (1), not an expansion of
its coordinate count.

## 3. Why this intermediate source needs a singular limit

The concise D-by-D-by-D tensor `L_n` is not an ordinary restriction of
the equal-format tensor

\[
S_n=M_{n+1}\oplus M_{n+1}\oplus M_n.
\]

Every such ordinary restriction would use invertible maps, because
the target has full flattening ranks D. But `S_n` has an invertible
slice, obtained from the identity matrix in each summand, whereas
`L_n` has no invertible slice.

To prove the latter assertion, fix an X parameter with `X_0`
invertible, and choose arbitrary rows `v_Y,+` and `v_Y,-`. Set every
other Y parameter to zero except

\[
Y_2=-X_0^{-1}\bigl(u_{X,+}v_{Y,+}+u_{X,-}v_{Y,-}\bigr).
\tag{7}
\]

The only remaining Z coefficient in (2) is

\[
\operatorname{tr}\bigl[
(X_0Y_2+u_{X,+}v_{Y,+}+u_{X,-}v_{Y,-})Z_0\bigr]=0.
\]

The arbitrary pair of row vectors gives a `2n`-dimensional left
kernel. Thus these slices have rank at most `D-2n`. Since the set
`det(X_0)!=0` is dense and matrix rank at most `D-2n` is closed, the
same upper bound holds for every X slice. It is attained at
`X_0=I`, both `d_X,c=1`, and all other X parameters zero: the core
anti-diagonal has rank `3n^2`, the two upper/lower arm pairings add
`2n`, and the two scalar entries add two. Cyclic symmetry gives the
same maximum slice rank on the other legs.

Consequently a singular limit is necessary for this stated
intermediate source. This does not exclude other ordinary maps from
the much larger full A(a,a) source to `L_n`.

## 4. Exact replay and scope

The [sparse maps](parity_structure_jet_extension_sparse.json) use the
same original source-column conventions as the first collision.
Each entry stores target row, source column, parameter exponent and
integer numerator; map denominators are `(1,1,2)`.
The standard-library verifier reads every original source term and
collects the complete Laurent polynomial over integers. Its expected
tensor is computed independently from the block-trace expansion (6).

For A(8,8), all 262,144 original source terms are examined, of which
902 meet all three maps. Each map has 278 monomials and uses 134
distinct original source coordinates. The remaining nonzero powers
are exactly:

| Power | Nonzero coefficients |
| ---: | ---: |
| 0 | 1,514 |
| 2 | 36 |
| 3 | 216 |
| 6 | 1,512 |
| 12 | 216 |

Every constant coefficient is one. The verifier proves all three
constant flattening ranks are 134 from disjoint supports. It also
changes a nonzero upper-arm coefficient to twice its value and rejects
the altered identity. A second control runs the complete smallest
case `a=3`, whose target has nine coordinates and fourteen constant
terms.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_jet_extension.py
python -S -m unittest discover -s tests -p test_parity_structure_jet_extension.py -v
```

The only local code dependency is
`parity_structure_jet_collision.py`, which supplies the full source
iterator and sparse Laurent contraction. No numerical package or
external solver is needed. The [report](parity_structure_jet_extension_certificate.json)
records the exact replay separately from the maps.

This family retains all 134 directions from (1); postcomposing it
still cannot reach a concise tensor with 778 directions per leg.
Any construction of the current target must add original source
directions before the limit. Formula (6) identifies the powers and
matrix couplings that such an extension would have to handle; it does
not certify those additional directions or an exponent improvement.
