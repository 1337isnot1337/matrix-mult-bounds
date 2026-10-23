# Low-degree Koszul ranks on the long legs of the paired source

AI-derived written proof, October 23, 2026. The proof is unreviewed and does
not establish an exponent improvement. It determines only the first `a`
Koszul ranks on each long leg; degrees `p>=a` remain open.

Let `D=a-1`, `m=2a-1`, and `N=am`. The paired source has format
`(a^2,N,N)` and coefficients

```text
P_a = sum A_(p,q) B_(y,q+v) C_(p+y,v),
```

where `p,q,y,v` range from `0` to `D`, the first index of `B` ranges to
`D`, its second index ranges to `2D`, the first index of `C` ranges to `2D`,
and its second index ranges to `D`.

For the `B` long leg, write

```text
K_p(P_a; B): exterior^p B tensor A* -> exterior^(p+1) B tensor C.
```

The claim is

```text
rank K_p(P_a; B) = a^2 * binom(N,p),   0 <= p <= a-1.
```

Thus these maps are injective. An explicit tensor symmetry below gives the
same ranks for the `C` long leg.

## Interpolation form of the source

Set `V_d=H^0(P^1,O(d))`. The first convolution factor is multiplication
`V_D tensor V_D -> V_(2D)`. The second is the same multiplication with its
`V_(2D)` output in the `B` leg. Choose `m=2D+1` distinct rational points
`t_1,...,t_m`, and let `ell_i` be their Lagrange polynomials of degree at
most `2D`. The exact identity

```text
f*g = sum_i f(t_i) g(t_i) ell_i
```

gives the second factor as `sum_i u_i tensor ell_i tensor c_i`, where `u_i`
and `c_i` are evaluation vectors in the two `a`-dimensional factors. Any
`a` of the `u_i` are independent, and any `a` of the `c_i` are independent:
the corresponding determinant is a nonzero Vandermonde product.

Consequently, after a basis change on `B`,

```text
B = direct_sum_(i=1)^m W_i,   dim W_i=a,
```

and the coefficient of `W_i` carries the `A_2` evaluation `u_i` and
`C_2` evaluation `c_i`.

## Injectivity proof

The flattening of the first multiplication factor

```text
phi: A_1* -> W_1* tensor C_1
```

is injective. In the original monomial bases, the `a` slices are distinct
shifts; for example, their entries with input exponent zero have distinct
output exponents.

Take a kernel vector `x` and expand it in the exterior basis induced by the
blocks `W_i`:

```text
x = sum_I (wedge I) tensor alpha_I,
alpha_I in A_1* tensor A_2*.
```

Let `S(I)` be the set of blocks used by `I`; then `|S(I)|<=p`. Fix `i` not
in `S(I)` and add a basis vector from `W_i` to `I`. In the corresponding
output wedge coordinate, terms can arise by deleting any one of its
`p+1` basis vectors. A term obtained by deleting a vector from block `j`
has `C_2` factor `c_j`. The vectors `c_j` for the blocks in
`S(I) union {i}` are independent because
`|S(I) union {i}|<=p+1<=a`. Projecting to the `c_i` component leaves only
the term obtained by deleting the newly added `W_i` vector. Varying that
new basis vector over `W_i` shows that the full tensor
`phi((id tensor u_i)(alpha_I))` in `W_i* tensor C_1` is zero.

Since `phi` is injective, the kernel equation implies

```text
(id tensor u_i)(alpha_I)=0   for every i not in S(I).
```

There are `m-|S(I)| >= m-p >= a` such evaluation vectors. Any `a` span
`A_2`, so these equations force `alpha_I=0`. This holds for every `I`,
and hence `x=0`.

The coefficient map is over `C`; the proof uses only distinct interpolation
points and exact Vandermonde nonvanishing. No modular source rank is used as
a complex upper bound.

## The other long leg and target scope

The coefficient tensor is preserved by the basis permutations

```text
A_(p,q) -> A_(q,p),
B_(y,j) -> C_(j,y),
C_(z,v) -> B_(v,z).
```

They exchange `B` and `C`, so the same rank formula holds on the other long
leg.

For a target padded to `(a^2,N,N)`, with its short source leg matched to a
target leg of dimension `d_A<=a^2`, either long-leg Koszul map (after
reordering legs to keep that short leg as `A`) has domain dimension at
most `d_A*binom(N,p)`. In the proved range the source rank is
`a^2*binom(N,p)`, so no such target can have a larger long-leg rank. The
result therefore closes the low-degree part `0<=p<=a-1` of this screening
route; it does not screen degrees `p>=a` or exclude any of the 28 saved
formats by itself.

The exact interpolation and frontier checks are in `verify.py`. Claims
remain written and unreviewed; no smaller exponent is established.
