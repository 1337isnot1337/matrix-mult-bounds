# The first noninjective C-leg Koszul degree of a canonical Full sum

Date: 2026-10-23. Owner-directed Codex work. Draft for same-session audit.

## 1. Statement

Let `a,c>=1` and `b_1,...,b_c>=1` be integers. Over the complex numbers,
form the canonical common-first partial sum

\[
T=\sum_{r=1}^{c}\mathrm{Full}(a,b_r).
\]

Every source block uses the same first coefficient basis. Put

\[
N=\sum_r b_r,\qquad M=N+c(a-1).
\]

For the C-leg Koszul map

\[
K_C^a(T):B^*\otimes\Lambda^a C
\longrightarrow A\otimes\Lambda^{a+1}C,
\tag{1}
\]

the exact kernel dimension and rank are

\[
\boxed{\dim\ker K_C^a(T)=\binom{N+a}{a+1}},
\tag{2}
\]

\[
\boxed{\operatorname{rank}K_C^a(T)
=N\binom{M}{a}-\binom{N+a}{a+1}}.
\tag{3}
\]

The result does not permit independent changes of the first coefficient basis
in different blocks. Global changes of any leg preserve the rank.

For `10 Full(5,10)`, the degree-five map has domain dimension 41696552800,
kernel dimension 1609344100, and rank **40087208700**. Its codomain dimension
is 46908621900. This is an exact source value for the remaining candidate
screen, not a calculation of the mixed target rank or a degeneration.

## 2. Polynomial and exterior coordinates

Let `P_d` denote the space of polynomials of degree at most `d` in one variable.
Identify

\[
A^*=P_{a-1},\qquad B_r^*=P_{b_r-1},\qquad C_r=P_{a+b_r-2}.
\]

The literal tensor is ordinary polynomial multiplication on every block:

\[
T_r=\sum_{k=0}^{a-1}\sum_{j=0}^{b_r-1}
a_k\otimes b_{r,j}\otimes c_{r,k+j}.
\]

Consequently, for `g` in `B_r^*` and `xi` in `wedge^a C`, (1) sends

\[
g\otimes\xi\longmapsto
\sum_{k=0}^{a-1}a_k\otimes(z^k g)\wedge\xi,
\tag{4}
\]

with `z^k g` in `C_r`.

Decompose the codomain by nonnegative block occupancies `m_r` of sum
`n=a+1`. The corresponding domain component is

\[
\bigoplus_{r:m_r>0}
B_r^*\otimes\Lambda^{m_r-1}C_r
\otimes\bigotimes_{s\ne r}\Lambda^{m_s}C_s.
\tag{5}
\]

For this fixed occupancy, introduce `n` variables `z_1,...,z_n`, grouped
into consecutive color classes of sizes `m_r`. A vector in `wedge^m P_d`
is represented by its alternating polynomial in `m` variables: the basis
wedge `z^{i_1} wedge ... wedge z^{i_m}` maps to
`det(z_j^{i_k})`. This is an isomorphism onto the alternating polynomials
of degree at most `d` in each variable.

An element of (5) therefore gives a tuple of polynomials `f_1,...,f_n`.
For an index `i` of color `r`, its marked variable `z_i` is the `B_r^*`
factor, and all unmarked variables represent the exterior C factors. Include
the exterior insertion sign `(-1)^(i-1)` in `f_i`. The degree bounds are

\[
\deg_{z_i}f_i\le b_r-1,\qquad
\deg_{z_j}f_i\le a+b_{\mathrm{color}(j)}-2\quad(j\ne i).
\tag{6}
\]

Within each color, permuting variables acts on the tuple by the exterior
sign and the corresponding permutation of its components. For example,
transposing two variables of the same color changes the sign and exchanges
the two marked components; it changes the sign of every other component.
Conversely, a tuple with this covariance and (6) determines an element of
(5): choose one marked position in each color, then read its alternating
polynomial in all unmarked positions.

The wedge insertion in (4), expanded by the marked position, shows that
the element is in the kernel exactly when

\[
\sum_{i=1}^{n}z_i^k f_i=0,
\qquad k=0,1,\ldots,a-1.
\tag{7}
\]

No interpolation at finitely many points is being used: these are identities
in the polynomial ring `C[z_1,...,z_n]`.

## 3. Primitive Vandermonde syzygies

The coefficient matrix in (7) is the `a`-by-`a+1` Vandermonde matrix. It
has rank `a` over the fraction field. Its kernel over that field is generated
by the signed maximal-minor vector

\[
v_i=(-1)^{i-1}
\prod_{\substack{j<\ell\\j,\ell\ne i}}(z_\ell-z_j).
\tag{8}
\]

These maximal minors have no nonconstant common divisor. Each possible
linear factor `z_ell-z_j` is absent when the omitted index is `j` or `ell`,
and every minor is a product of such factors. For `a=1`, the products are
empty and equal one, so the same statement holds.

It follows that every polynomial solution of (7) is uniquely

\[
f_i=h\,v_i\qquad(1\le i\le n)
\tag{9}
\]

for a polynomial `h`. To see that `h` has no denominator, write it as a
reduced fraction. Since all `h v_i` are polynomials, every irreducible
denominator factor would divide all `v_i`, contradicting their greatest
common divisor being one.

The signed cofactor vector transforms under a permutation of its variables
by that permutation's sign and the corresponding permutation of components.
This is the same covariance as the tuple `f`. Equation (9) therefore says
that `h` is symmetric separately within each color class.

The minor `v_i` is independent of `z_i`. The marked-variable inequality
in (6) thus gives

\[
\deg_{z_i}h\le b_{\mathrm{color}(i)}-1.
\tag{10}
\]

Conversely, suppose `h` is separately symmetric and satisfies (10).
For `j!=i`, the degree of `v_i` in `z_j` is `a-1`. Thus `h v_i` satisfies
both bounds in (6), has the required exterior covariance, and solves (7).
It gives an actual element of the kernel component (5).

We have proved a linear isomorphism between that kernel component and the
space of separately symmetric polynomials with the bounds (10).

## 4. Counting the kernel

Symmetric polynomials in `m` variables with degree at most `b-1` in each
variable have the monomial-symmetric basis indexed by multisets of `m`
elements from `0,...,b-1`. Their dimension is

\[
\binom{b+m-1}{m}.
\]

Thus the exact kernel dimension at occupancy `(m_1,...,m_c)` is

\[
\prod_{r=1}^{c}\binom{b_r+m_r-1}{m_r}.
\tag{11}
\]

This includes an empty color with `m_r=0`, whose factor is one. Summing
over occupancies of total `a+1`, the generating-function identity

\[
\prod_r(1-t)^{-b_r}=(1-t)^{-N}
\]

gives (2). Subtracting from the domain dimension in (1) proves (3).

The argument also covers a single width-one block: then `M=a`, the map
in (1) has zero codomain, and both (2) and the direct kernel dimension
are one.

## 5. Exact coefficient controls

The same occupancy/weight construction used for the mixed-candidate B-leg
calculation was applied directly to the C-leg coefficients at `a=5,p=5`:

| Canonical source profile | N | M | Literal rank | Literal kernel | Formula |
| --- | ---: | ---: | ---: | ---: | ---: |
| `2 Full(5,1)` | 2 | 10 | 497 | 7 | 7 |
| `3 Full(5,1)` | 3 | 15 | 8981 | 28 | 28 |
| `2 Full(5,2)` | 4 | 12 | 3084 | 84 | 84 |
| `Full(5,1)+Full(5,2)` | 3 | 11 | 1358 | 28 | 28 |

All four ranks use exact standard-library integer elimination. The controls
include repeated colors; their dimensions agree with (11). They support
the coordinate conventions, not the universal proof by themselves.

## 6. Scope and provenance

This is a same-session continuation. The root agent proposed the polarized
column-kernel map from `Sym^(a+1)(B^*)`; the audit agent independently
identified its expected dimension through the Vandermonde cofactor equations.
The argument above establishes the complete kernel for the canonical Full
sum, with no need to assume a determinantal-resolution theorem.

Polynomial multiplication, exterior coordinates, Vandermonde determinants,
and unique factorization are standard algebra. No historical priority,
independent mathematical review, or formalization is claimed. This result
computes a source rank; it does not exclude the new mixed candidate, compute
its C-leg degree-five rank, or improve a matrix-multiplication exponent.
