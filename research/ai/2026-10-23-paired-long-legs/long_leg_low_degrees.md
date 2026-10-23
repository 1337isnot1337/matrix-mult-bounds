# Koszul ranks through the first support threshold on the paired source

AI-derived written proof, October 23, 2026. The proof is unreviewed and does
not establish an exponent improvement. It determines the Koszul ranks on
each long leg for `0<=p<=a`; degrees `p>=a+1` remain open.

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
rank K_p(P_a; B) = a^2 * binom(N,p),   0 <= p <= a.
```

Thus these maps are injective. The boundary degree `p=a` is handled
separately below. An explicit tensor symmetry gives the same ranks for the
`C` long leg.

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

## The boundary degree `p=a`

Write `x=sum_I (wedge I) tensor alpha_I` as before. If `|S(I)|<=a-1`, add a
basis vector from an unused block `W_i`. The output wedge has at most `a`
blocks. Their `c_j` are independent, so projection to `c_i` isolates the
term from `alpha_I` and gives

```text
phi((id tensor u_i)(alpha_I)) = 0.
```

Varying the added vector gives this for every unused `i`. There are at least
`m-(a-1)=a` such evaluation vectors, so `alpha_I=0` as above. It remains to
consider `|S(I)|=a`, where `I` has one vector from each block in its support.

We need one elementary fact about the first multiplication factor. Write
`A_1*=span(epsilon_0,...,epsilon_D)` and
`C_1=span(gamma_0,...,gamma_(2D))` in their dual and monomial bases. Let
`b_y` be the basis vector in `W_i` corresponding to the degree-`y` monomial
of the `B_1` factor. For `beta=sum_r beta_r epsilon_r` in `A_1*`, its slice is

```text
psi_y(beta) = sum_(r=0)^D beta_r gamma_(r+y) in C_1,   0<=y<=D.
```

Each `psi_y` is injective. Also, if a family `beta_y in A_1*` satisfies
`psi_z(beta_y)=psi_y(beta_z)` for every `y<z`, then

```text
beta_y = lambda epsilon_y,   0<=y<=D,
```

for one scalar `lambda`. Adjacent pairs give
`beta_(y+1,0)=beta_(y,D)=0` and
`beta_(y+1,r)=beta_(y,r-1)` for `1<=r<=D`. The recurrence makes each
diagonal of the coefficient array constant; the two boundary equations kill
every diagonal except `r=y`.

Fix a set `J` of `a+1` blocks and choose one basis vector, with index `y_j`,
from each. The coefficient of this output wedge is

```text
sum_(j in J) sign(j) c_j tensor psi_(y_j)((id tensor u_j)(alpha_(J\{j}))) = 0.
```

Any `a` of these `a+1` vectors `c_j` are independent. Their unique linear
relation has every coefficient nonzero. For distinct `j,k in J`, fix all
indices except `y_j=x` and `y_k=y`. The dependence of the two corresponding
terms on these indices gives

```text
psi_x(U_j(y)) = constant * psi_y(U_k(x)),
```

where `U_j(y)=(id tensor u_j)(alpha_(J\{j}))`, `U_k(x)` is defined
similarly, and the nonzero constant absorbs the fixed wedge signs and the
coefficients of the `c_j` relation. Scale the two families by fixed
nonzero constants to write this as `psi_x(beta_y)=psi_y(gamma_x)`. Each
`psi_x` is injective, so setting `x=y` gives `beta_x=gamma_x`. The equation
then becomes `psi_x(beta_y)=psi_y(beta_x)`, and the adjacent-slice identity gives
`beta_y=lambda epsilon_y` for one scalar `lambda`.

Fix `I=J\\{j}` and put `U_j=(id tensor u_j)(alpha_I)`. For each coordinate
`k in I`, apply this pair argument with `j` and `k`, fixing the remaining
block indices. It says that along coordinate `k`, the coefficient of `U_j`
in the `epsilon_r` direction is supported at `r=y_k`, with one common value
as `y_k` varies. Choose two distinct coordinates `k,h in I`, and fix all
other indices. Whenever `y_k!=y_h`, the `k` condition allows a coefficient
at `r=y_k`, while the `h` condition forces that coefficient to be zero.
Since `D>=1`, for each fixed `y_h` there is such a `y_k`; thus the common
value is zero and `U_j=0`. This holds for every `j` outside `I`.

Consequently, for a support set `S` of size `a`, `alpha_I` is annihilated by
all `u_j` with `j` outside `S`. These `a-1` evaluation vectors are
independent, so their common annihilator in `A_2*` is a line. Write
`alpha_I=beta_I tensor ell_S` using a fixed nonzero `ell_S` on that line.
For every `i in S`, `ell_S(u_i)` is nonzero, since otherwise `ell_S` would
annihilate `a` independent evaluation vectors.

Take an output wedge with support `S` in which block `i` contributes two
distinct basis vectors `y,z`, and each other block contributes one. Terms
deleting a singleton block come from supports of size `a-1`, already zero.
Projecting the remaining coefficient to `c_i` gives, after dividing by
`ell_S(u_i)`,

```text
psi_z(beta_y) = psi_y(beta_z),   y<z,
```

where the other `a-1` block basis vectors are held fixed and `beta_y` is the
`A_1*` factor of the corresponding `alpha_I`. Thus along each block
coordinate the same identity says that the coefficient array is supported on
`r=y` and is constant as `y` varies. Choose two distinct blocks `i,k in S`,
possible because `a>=2`, and fix all other block coordinates. For fixed
`y_k`, the condition along `i` says that the coefficient at `r=y_i` has the
same value for every `y_i`. The condition along `k` forces that coefficient
to vanish whenever `y_i!=y_k`. Since `D>=1`, for each fixed `y_k` there is
such a `y_i`; hence the common value is zero. All coefficients of `alpha_I`
vanish. This proves injectivity also at `p=a`.

The argument uses exact coefficient identities over `C`; the modular checks
below are finite controls in the original monomial convention, not premises
of this proof.

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
result therefore closes the range `0<=p<=a` of this screening route; it does
not screen degrees `p>=a+1` or exclude any of the 28 saved formats by itself.

The exact interpolation and frontier checks are in `verify.py`. Claims
remain written and unreviewed; no smaller exponent is established.
