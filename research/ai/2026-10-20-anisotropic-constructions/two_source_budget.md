# A sharp capacity bound for two source summands

October 21, 2026. This note gives a necessary dimension bound for a
restriction or degeneration from two arbitrary tensors to a square
matrix tensor. An explicit majority-block construction attains the
bound for appropriate source tensors. The finite convolution-source
scans identify conditional targets only. No smaller matrix
multiplication exponent is established.

## 1. The two-source bound

Suppose each leg of a tensor `T` has dimension at most `N_T`, and each
leg of `U` has dimension at most `N_U`. If

\[
 T\oplus U\rightsquigarrow M_n,
\]

then

\[
 \boxed{\sqrt{\max(0,n^2-N_T)}+
 \sqrt{\max(0,n^2-N_U)}\le n.}                 \tag{1}
\]

Here an arrow permits an ordinary restriction or an algebraic
degeneration. In particular, when both source summands have all leg
dimensions at most `N`,

\[
 \boxed{N\ge \left\lceil\frac{3n^2}{4}\right\rceil.} \tag{2}
\]

This is a condition on each summand's leg dimensions, not on their
tensor ranks, and it applies without any convolution or symmetry
assumption on the source tensors.

### Six simultaneous kernel spaces

Write `d=max(0,n^2-N_T)` and `e=max(0,n^2-N_U)`. On each target leg,
the map into the `T` source variables has a kernel containing a
`d`-dimensional space `K_i`, and the map into the `U` source variables
has a kernel containing an `e`-dimensional space `L_i`. If one input
is in `K_i` and the next cyclic input is in `L_(i+1)`, both source
summands vanish, one on each of those inputs. The same holds with
`K` and `L` exchanged.

Identify the three target parameter spaces with `Mat_n`, so that
their trilinear form is `tr(XYZ)`. The nondegenerate trace pairing
gives the six product conditions

\[
 K_iL_{i+1}=0,\qquad L_iK_{i+1}=0
 \quad(i\bmod3).                              \tag{3}
\]

For a degeneration, take the six kernel subspaces at a nonzero
parameter, with the fixed dimensions `d,d,d,e,e,e`. Their simultaneous
Grassmann limits exist after a base change. Incidence with a tensor's
zero contractions is closed, so (3) still holds for the limiting
matrix tensor. This argument does not require separate limits of
the two source summands.

Let `r_i` be the dimension of the sum of the images of matrices in
`K_i`, and let `s_i` be the corresponding dimension for `L_i`.
Condition (3) implies that every matrix in `K_i` annihilates the
`s_(i+1)`-dimensional image space of `L_(i+1)`, and takes its values in
an `r_i`-dimensional space. Consequently

\[
 d\le r_i(n-s_{i+1}),\qquad
 e\le s_i(n-r_{i+1}).                          \tag{4}
\]

For equal dimensions, multiplying all six inequalities immediately
gives

\[
 d^6\le\prod_i r_i(n-r_i)s_i(n-s_i)
 \le \left\lfloor\frac{n^2}{4}\right\rfloor^6,
\]

which proves (2).

For the unequal case put

\[
 R=(r_1r_2r_3)^{1/3},\qquad S=(s_1s_2s_3)^{1/3}.
\]

Hölder's inequality, applied to the two triples `s_i` and `n-s_i`,
gives

\[
 S+\bigl(\prod_i(n-s_i)\bigr)^{1/3}\le n.
\]

Multiplying each triple of inequalities in (4) and applying this
bound and its `r_i` counterpart yields

\[
 d\le R(n-S),\qquad e\le S(n-R).
\]

Finally Cauchy–Schwarz gives

\[
 \sqrt d+\sqrt e
 \le\sqrt{R(n-S)}+\sqrt{S(n-R)}\le n,
\]

proving (1). The dimension argument is valid for ordinary maps over
any field, and for algebraic degenerations after extending to an
algebraic closure. The inequalities on dimensions are inequalities
between nonnegative real numbers.

### A separately supplied correction

If `N_T<n^2`, formula (1) requires

\[
 N_U\ge 2n\sqrt{n^2-N_T}-(n^2-N_T).            \tag{5}
\]

This is stronger than the one-kernel lower bound
`N_U>=n*ceil(sqrt(n^2-N_T))` in some relevant ranges. The exact
integer acceptance test for (1) uses no floating-point square roots:
with `h=n^2-d-e`, require `h>=0` and `4*d*e<=h^2`.

## 2. An explicit construction attaining the bound

Partition the `n=r+s` matrix vertices into groups of sizes `r,s`.
Let `T_(r,s)` be the trace tensor on block matrices

\[
 \begin{pmatrix}0&B\\C&D\end{pmatrix},
\]

with common leg dimension `n^2-r^2`. Let `U_(r,s)` instead have its
bottom-right block zero, with common dimension `n^2-s^2`. There is an
ordinary restriction

\[
 T_{r,s}\oplus U_{r,s}\longrightarrow M_{r+s}.  \tag{6}
\]

On each leg, send every target matrix unit to its identically named
coordinate in each source summand where that coordinate is present.
A matrix multiplication term is a directed triangle on three matrix
vertices. Exactly one of the two vertex groups contains a majority
of those three vertices. The term occurs in the source tensor whose
zero block is the other group, and is absent from the other source.
Thus every target term occurs once, and no other terms occur.

Both source tensors are concise: any retained matrix unit occurs
in a triangle completed by a vertex in the group whose diagonal
block is retained, and two other matrix coordinates uniquely
determine the first one. Their dimension deficits are exactly
`r^2,s^2`, so equality holds in (1).

When `r=s`, the two sources are isomorphic by exchanging the vertex
groups. Write their common tensor as `T_s`. Its common leg dimension
is `3s^2`, and its trilinear form is

\[
 \operatorname{tr}(B_XD_YC_Z)
 +\operatorname{tr}(C_XB_YD_Z)
 +\operatorname{tr}(D_XC_YB_Z)
 +\operatorname{tr}(D_XD_YD_Z).                \tag{7}
\]

Consequently `T_s direct_sum T_s` restricts to `M_(2s)`. This is a
complete source identity, not a claim that a convolution tensor
already supplies `T_s`. The exact control regenerates both block-zero
trace tensors and contracts their coordinate maps, checking all
coefficients for vertex pairs `(1,1),(2,2),(2,3),(3,4)`.

## 3. The first surviving equal-copy convolution budget

Let `A(a,b)` have common dimension `N=ab(a+b-1)`, and put
`c=3(a+b)-2`. Suppose two copies of this source supply `M_n`. For a
detecting character with dot-product parameter sum `p`, the source
inequality is `2*lambda(A(a,b))>=n^p`. Reflecting all source legs gives
the same inequality for the other cyclic orientation. Multiplying
the two inequalities and using the existing six-orientation
comparison gives

\[
 (6n)^p\le2c^3.                                \tag{8}
\]

This derivation does not identify either individual character value
with the symmetric profile when `a` and `b` differ. The two
orientations are retained throughout.

At the critical exponent `p=9/4`, a prospective improvement requires

\[
 (6n)^9>16c^{12}.                              \tag{9}
\]

For each `2<=a<=b` with `N<=2904`, the exact scan takes
`n=floor(sqrt(4N/3))`, the largest square target permitted by (2).
Testing this largest target suffices because the score is increasing
in `n`. Every source format with `N<2904` fails (9). The first relaxed
survivor is

\[
 2A(11,12)\rightsquigarrow M_{62},
 \qquad N=2904,\qquad \left\lceil3\cdot62^2/4\right\rceil=2883.
                                                               \tag{10}
\]

No maps establishing (10) are known in this package. If they were
constructed, the exact integer inequality

\[
 372^{2249}>601526^{1000}
 \quad\text{where }601526=2\cdot67^3
\]

would give the conditional exponent bound `omega<2.249` through the
existing detecting-character argument. This is not an attained bound.

The former proposed pairs `2A(7,8)->M35` and `2A(8,8)->M38` fail (2),
so they are excluded even as singular degenerations. The earlier
one-kernel source-dimension test was insufficient for those pairs.

## 4. Ordinary majority targets need additional room

The sharp abstract model suggests the structured intermediate target
`A(11,12)->T31`, since `T31` has dimension 2,883. That ordinary
restriction is impossible. A rank-one parameter in a `B` block of
(7) has target slice rank `s`, and the same holds for a `C` block.
An ordinary lift through a concise `3s^2`-dimensional target has
source slice rank at most

\[
 s+2\bigl(N-3s^2\bigr).                        \tag{11}
\]

The minimum nonzero source slice rank of `A(a,b)` is `ab`. For
`(a,b,s)=(11,12,31)`, (11) is `31+42=73`, below `132=11*12`.
This excludes the ordinary intermediate, while singular maps remain
outside this argument.

The existing Hankel-symbol theorems give additional cheap ordinary
tests. The `s^2`-dimensional `B` block is an injectively lifted matrix
space, and its rank-one parameters form a Segre variety whose target
slices all have rank `s`. The dimension conclusions of those theorems
depend on precisely these properties, not on the other coefficients
of the target tensor. With `k=N-3s^2`, they require

\[
 s^2>rab\quad\Longrightarrow\quad s+2k\ge(r+1)ab
 \quad\text{if }1\le r<\min(a,b),\ 3r\le a+b-1. \tag{12}
\]

At the separately proved boundary `a+b-1=3r-1`, `r>=2`, replace the
dimension cap `rab` by `max(r,4)ab`. The
[fixed-support proof](hankel_symbol_dimension.md) and
[first-boundary proof](hankel_boundary_dimension.md) supply the exact
scopes. No unproved extension to shorter Hankel sequences is used.

The saved scan applies (11), (12), and that first-boundary rule to
every score-eligible balanced majority target in sources of dimension
at most 14,364. The first survivor of these particular ordinary tests
is `A(18,21)->T64`, with common source dimension 14,364 and target
dimension 12,288. This remains an unconstructed, large target; passing
the tests is not evidence that a map exists. The scan does not exclude
arbitrary two-source maps that do not factor through the majority
model, or singular majority constructions.

## Replay and review scope

The [saved report](../../../results/anisotropic-constructions-2026-10-20/two-source-budget.json)
contains all finite source records, the exact majority controls, the
conditional integer comparison, and the reasons for each ordinary
majority exclusion. The implementation and tests use only the Python
standard library.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/two_source_budget.py
python -S -m unittest discover -s tests -p test_two_source_budget.py
```

The equal-copy kernel argument was checked by a second agent in this
generating session. There has been no external independent review or
proof-assistant formalization.
