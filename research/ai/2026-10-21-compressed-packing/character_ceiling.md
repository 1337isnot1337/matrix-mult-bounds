# Character ceiling for the compressed alternative tensor

Date: 2026-10-21. AI-derived proof with exact finite controls.

The compressed construction in [README.md](README.md) gives the genuine
degeneration `C(2s,N) -> U_(2s)`, where `N=s(2s+1)`. Its constant tensor is
the sum of three retained fat-point slices and two error families. This
note gives an upper bound on the character of that actual tensor.

The endpoint equality of the three dot-product exponents follows from
Uznański v2, Proposition 5.2, as proved in the repository's
[finite amplitude note](../2026-10-20-koszul/finite_amplitude.md).
Character additivity, monotonicity and the existing scalar lower profile
retain the external and local attributions given there.

At an endpoint character, with all three dot-product exponents equal to
`3/4`, the bound is

\[
\boxed{\lambda(U_{2s})\le M_s:=
 \sum_{j=1}^{s-1}j^{3/4}+\sum_{j=1}^{s-2}j^{3/4}
 +(s^2+s-2)^{3/4}+2(s^2+s)^{3/4}.}                 \tag{1}
\]

The second sum is empty when `s<=2`; the first central term is zero at
`s=1`. The same upper bound holds for every leg permutation. In particular,

\[
\limsup_{s\to\infty}
 \frac{\bigl(\prod_{\pi\in S_3}\lambda(U_{2s}^{\pi})\bigr)^{1/6}}
 {\bigl(\prod_{\pi\in S_3}\lambda(C(2s,N)^{\pi})\bigr)^{1/6}}
 \le\frac47.                                             \tag{2}
\]

Consequently this specific alternative tensor cannot supply the required
unbounded character growth. This conclusion leaves the full Laurent
identity, other ways to cancel its negative coefficient, and different
constant tensors open. It is stronger than a ceiling limited to matrix
extraction: (1) bounds the actual character of `U_(2s)`.

## 1. Nested truncated multiplication tensors

For an integer `r>=1`, define

\[
A_r=\sum_{i=1}^{r}\ \sum_{x+a+c=i-1}
 X_xY_{i,a}Z_{i,c},                                      \tag{3}
\]

where all indices in the inner sum are nonnegative. The shared coordinates
are `X_0,...,X_(r-1)`. The nonshared spaces of distinct `i` are disjoint.
Set `A_0=0`.

Let `B_X(k)` be a dot product of length `k`, with a one-dimensional shared
`X` leg. For any character with `lambda(B_X(k))=k^(p_X)`,

\[
\lambda(A_r)\le\sum_{j=1}^{r}j^{p_X}.                    \tag{4}
\]

Here is an explicit degeneration proving (4). Reverse each output basis,
so that `Z_(i,c)` is relabelled by `b=i-1-c`. The `X_x` slice of block `i`
is then the matrix of multiplication by `t^x` on `K[t]/t^i`, up to a
transpose determined by the input/output convention.

Over a characteristic-zero field put

\[
 f_i(t,\epsilon)=\prod_{j=1}^{i}(t-\epsilon j),
 \qquad C_i(\epsilon)=\text{multiplication by }t
                   \text{ on }K[t]/f_i(t,\epsilon).
\]

Use the power basis `1,t,...,t^(i-1)` and form the tensor with slices
`C_i(epsilon)^x`, for `0<=x<r`, on every block. Its entries are polynomial
in `epsilon`. At zero it is exactly (3), including the zero powers when
`x>=i`.

For nonzero `epsilon`, evaluation at `epsilon,2 epsilon,...,i epsilon`
diagonalizes block `i`. Its one-dimensional summands have shared vectors

\[
v_j(\epsilon)=(1,\epsilon j,(\epsilon j)^2,
                    \ldots,(\epsilon j)^{r-1}),\quad 1\le j\le i.
\]

The `r` vectors `v_1,...,v_r` form an invertible Vandermonde matrix over
`K(epsilon)`. A single change of the shared basis therefore works in
every block at once. Vector `v_j` occurs in blocks `j,...,r`, with
multiplicity `r-j+1`. Thus the generic tensor is isomorphic to

\[
D_r=\bigoplus_{j=1}^{r}B_X(r-j+1).
\]

We have proved `D_r -> A_r`. Character additivity and monotonicity give
(4). The characteristic-zero statement is sufficient for the character
comparison here; no assumption about distinct integer residues in small
positive characteristic is used.

## 2. Reindexing the two error families

Use the notation and formula (2) of the compressed-packing README.
In its first error family, replace the global shared index `q` by
`x=2s-1-q`. Its defining relation becomes

    x+a+c=i-1.

The unused endpoint coordinates `a=i` or `c=i` do not occur. Therefore
the first family is exactly `A_(s-1)`, after harmless relabelling of its
nonshared coordinates.

In the second family put `a'=i-a` and `c'=i-1-c`. Its global shared index
`x=a+c-i-1` satisfies

    x+a'+c'=i-2.

Consequently the second family is `A_(s-2)`. Their shared-coordinate
ranges are disjoint. Some nonshared coordinates are shared between the
two families and the central tensor; this causes no difficulty for an
upper bound. The sum of these three tensors is an ordinary restriction
of their direct sum, by identifying the copied coordinates.

## 3. The three central slices

For the fat-point tensor `T_m`, a fixed `X_q` slice has one term for each
pair

    0<=a<=q,  0<=b<=m-1-q,

with the unique opposite pair `c=q-a`, `d=m-1-q-b`. It is a permutation
matrix on those rows and columns, so its rank is exactly

\[
(q+1)(m-q).                                             \tag{5}
\]

At `m=2s`, the three retained shared indices are `s-2,s-1,s`, when present.
Their ranks are `s^2+s-2`, `s^2+s`, and `s^2+s`. The central tensor is a
restriction of the direct sum of the three corresponding dot products.
Combining this with (4) proves (1). At `s=1` there are only two retained
slices; the displayed zero term handles that case.

## 4. Comparison with the existing source profile

Write

\[
h_1=1,\qquad h_{n+1}=\left(1+\frac1{3n}\right)h_n,
\qquad
P_*(a,b)=h_{\min(a,b)}
             \left(\max(a,b)+\frac{\min(a,b)-1}{2}\right).
\]

The existing endpoint scalar lower bound is

\[
\bigl(\prod_{\pi\in S_3}\lambda(C(a,b)^\pi)\bigr)^{2/9}
 \ge P_*(a,b).
\]

The product exponent `2/9` is the geometric mean followed by the power
`4/3`. In particular, the geometric mean itself is at least
`P_*(a,b)^(3/4)`. This is a symmetrized statement; we do not apply it
separately to each oriented source.

The recurrence gives `h_n>=n^(1/3)`: cube the inequality
`1+1/(3n)>=(1+1/n)^(1/3)` and telescope. Since `N=s(2s+1)>=2s^2`,

\[
P_*(2s,N)^{3/4}\ge 2s^{7/4}.                           \tag{6}
\]

Monotonicity of `x^(3/4)` and integration give

\[
M_s\le\frac87s^{7/4}+3(s^2+s)^{3/4}
      =\left(\frac87+o(1)\right)s^{7/4}.
\]

Equations (1) and (6) prove (2). Equivalently the ratio of powered,
symmetrized character values has upper limit at most `(4/7)^(4/3)`.

For an explicit large-size threshold, when `s>=154`,

\[
2401(s+1)^3\le16s^4,
\]

which implies `3(s^2+s)^(3/4)<=6s^(7/4)/7`. This polynomial inequality
holds because, after substituting `s=154+u`, its right side minus left
side is

\[
58154621+60692821u+1160271u^2+7455u^3+16u^4.
\]

Thus `M_s<=2s^(7/4)<=P_*(2s,N)^(3/4)` for all `s>=154`.
The companion verifier also certifies `M_s<P_*(2s,N)^(3/4)` for every
integer `60<=s<=153`, using rational intervals for fourth roots.
Together these checks give this strict comparison for every even
`m>=120`. For smaller sizes the displayed upper estimate may exceed
the source lower bound; that is not a positive lower bound for the
alternative tensor and does not assert an exponent improvement.

## 5. Reproduction and scope

```sh
python research/ai/2026-10-21-compressed-packing/verify_character_ceiling.py --output results/compressed-packing-2026-10-21/character_ceiling.json
```

The verifier checks the two error reindexings, every central slice as a
partial permutation matrix, the nilpotent powers, and the integer root
identities behind the simultaneous Vandermonde diagonalization. It also
checks the exact polynomial threshold and the stated finite rational
interval comparisons. The all-size argument is the proof above, not an
extrapolation from those finite controls.

This ceiling concerns `U_m=T_m^central+E_m^-` from the specified
compressed degeneration. It does not exclude a different limit obtained
from the full Laurent identity, an improved packing, or a new cancellation
construction. Same-session AI review is not external mathematical
certification. No improvement of the matrix-multiplication exponent is
claimed.
