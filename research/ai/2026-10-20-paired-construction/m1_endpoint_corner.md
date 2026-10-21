# The natural corner of the endpoint M1 seed

## Statement and scope

Over the complex numbers, the explicit tensor `R` of format
`(16,18,18)` constructed below **cannot degenerate to `M(4,4,4)`**.
It is an exact ordinary restriction of `Q(6,4)`, but passing to this
particular corner loses a property needed by M4.

The consequence for the ongoing search is specific. At the endpoint
M1 leading point extracted from the certified Q54-to-M4 maps, suppose
the first nonzero cross terms have kernel

\[
K_2=P\otimes P,\qquad
P=\langle 1-t^4,t^2,t^3,t^5\rangle.
\]

If the corner is obtained from this kernel by the stated next long-leg
coefficients, those coefficients factor through `R`. They cannot produce
M4, even by a further degeneration of `R`. This rules out retaining the
inherited three new outer rows and merely supplying a fourth row when
that setup has exactly this kernel. It does not exclude a different
kernel, moving leading maps, another valuation pattern, a partial target,
or a general degeneration from Q64.

The coefficient identity and the obstruction are AI-derived work from
this session. The general projective facts used to pass to limits are
external and cited below. The proof has same-session checks; no external
mathematical review is claimed. There is no smaller-exponent claim.

## 1. The old endpoint maps and their kernel

The source convention is

\[
Q_{6,4}=\sum_{p,q=0}^{5}\sum_{y,v=0}^{3}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

Take old outer indices `i=h=0` in the exact Q54-to-M4 restriction.
On the four old B coordinates, its nonzero source columns are

\[
B_{0,1},\quad B_{0,0}+B_{0,4},\quad
B_{3,1},\quad B_{3,0}+B_{3,4}.
\]

On the four old C coordinates, they are

\[
C_{1,0},\quad C_{1,3},\quad
C_{0,0}+C_{4,0},\quad C_{0,3}+C_{4,3}.
\]

The first source quotient is the tensor square of

\[
f(a)=(a_1,a_0+a_4),\qquad a\in\mathbb C[t]_{\le5}.
\]

Thus `ker f=P` as above, the old pre-A rank is four, and
`ker(f tensor f)` has dimension 32. The candidate corner `P tensor P`
has dimension 16.

Write

\[
(p_0,p_1,p_2,p_3)=(1-t^4,t^2,t^3,t^5).
\]

For first-cross terms to vanish on this corner, every new B coordinate
on source rows `y=1,2` must annihilate

\[
E=P+t^3P
=\langle1-t^4,t^2,t^3,t^5,t^6,t^7,t^8\rangle.
\]

The same condition holds on source C columns `v=1,2`. To see the B
condition directly, the old C contraction of `p_0` isolates `y=1` in
its first output component; that of `p_1` isolates `y=2` in the second;
that of `p_2` isolates `y=1` in the second. The old C contraction of
`p_3` is zero. Applying this to arbitrary `q in P` and `v=0,3` gives
the asserted annihilators. The C argument is the transpose.

If `epsilon_s` extracts the coefficient of `t^s`, then

\[
E^\perp=\langle\epsilon_1,\epsilon_0+\epsilon_4\rangle.
\]

Consequently, the corner-compatible long maps have 22 available source
dimensions on each leg: nine arbitrary coefficients on each endpoint
row or column `0,3`, and two coefficients on each interior row or column
`1,2`.

## 2. The exact endpoint and interior decomposition

There are no mixed endpoint/interior terms in the corner. If `y` is
interior and `v` is an endpoint, the B functional annihilates `t^v P`.
If `y` is an endpoint and `v` is interior, the C functional annihilates
`t^y P`.

The endpoint product map is

\[
\mu:P\otimes\langle1,t^3\rangle\longrightarrow E,
\]

with output basis

\[
(e_0,\ldots,e_6)=(1-t^4,t^2,t^3,t^5,t^6,t^7,t^8).
\]

Its complete table is

| Input | Multiply by 1 | Multiply by `t^3` |
|---|---|---|
| `p0=1-t^4` | `e0` | `e2-e5` |
| `p1=t^2` | `e1` | `e3` |
| `p2=t^3` | `e2` | `e4` |
| `p3=t^5` | `e3` | `e6` |

The only product relation is `p3 tensor 1 = p1 tensor t^3`.
The paired endpoint tensor has long support dimensions 14 and 14.

The interior product is multiplication by `t,t^2`, followed by the two
functionals spanning `E^perp`. For `a=sum a_i p_i`, its matrix, with
rows indexed by `t,t^2`, is

\[
J(a)=\begin{pmatrix}a_0&a_2\\0&a_1\end{pmatrix}.
\]

Equivalently, its three tensor terms are

\[
p_0\,u_0\,w_0+p_1\,u_1\,w_1+p_2\,u_0\,w_1.
\]

Using shared A coordinates `A_pq`, the complete corner is

\[
\begin{aligned}
R={}&\sum_{p,q,y,v,a,b}
\mu_{pya}\mu_{qvb}\,
A_{pq}B^{\rm end}_{yb}C^{\rm end}_{av}\\
&+\sum_{p,q,y,v,a,b}
J_{pya}J_{qvb}\,
A_{pq}B^{\rm int}_{yb}C^{\rm int}_{av}.
\end{aligned}
\tag{1}
\]

The two summands use disjoint long-leg blocks but share the A leg.
They are not a tensor direct sum on all three legs. The interior blocks
have dimension four each. Four of the 22 allowed dimensions on each
long leg vanish from (1), leaving the concise format `(16,18,18)`.

The script gives explicit integer maps from every native source
coordinate to this format. It contracts all 576 source terms and checks
all 5,184 resulting coefficient positions against (1), including every
zero position. There are 90 nonzero coefficients. Exact rational
flattening ranks are `(16,18,18)`.

## 3. A three-dimensional space of slices of rank at most three

Restrict a B functional to the interior block and write its values as

\[
x=\begin{pmatrix}x_{00}&x_{01}\\x_{10}&x_{11}\end{pmatrix}.
\]

The four interior C coefficients in the resulting A-by-C slice are

\[
\begin{array}{c|l}
C^{\rm int}_{0,0}&a_0(b_0x_{00}+b_2x_{01})\\
C^{\rm int}_{0,1}&a_0b_1x_{01}\\
C^{\rm int}_{1,0}&a_1(b_0x_{10}+b_2x_{11})
                         +a_2(b_0x_{00}+b_2x_{01})\\
C^{\rm int}_{1,1}&a_1b_1x_{11}+a_2b_1x_{01}.
\end{array}
\tag{2}
\]

Here `a_i,b_j` describe first-input coordinates on the two copies of P;
their products denote the corresponding sixteen linear A coordinates.

Set `x01=0`. The second C column vanishes identically. Therefore

\[
L=\{x\in(B^{\rm int})^*:x_{01}=0\}\subset B_R^*
\]

has dimension three, and every slice `R(x)`, `x in L`, has rank at most
three. This is a uniform linear-support bound for every linear
combination, not just three separately tested basis slices. The choice
`x00=x11=1, x10=0` has rank exactly three.

## 4. Compression and degeneration exclusion

We use the following slice-locus observation. Suppose a tensor S with
B dimension `d` has an `ell`-dimensional linear subspace of B
functionals whose slices all have rank at most `r`. If a target B
dimension `b` satisfies `b+ell>d`, then every ordinary image of S in
that target format has a nonzero B functional with slice rank at most
`r`.

Indeed, if the B map is not surjective, its image tensor has a zero
slice. Otherwise its dual embeds a `b`-dimensional subspace of the
original dual B space. This subspace meets the low-rank subspace
nontrivially by the ordinary linear dimension inequality. Maps on A
and C cannot increase the rank of that slice. This is the linear case
of the projective intersection principle in the Stacks Project,
[Tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R), Lemma 33.34.3,
accessed 2026-10-21.

The property persists under degeneration over an algebraically closed
field. In a fixed target tensor space V, consider

\[
\mathcal I_r=\{(T,[\beta])\in V\times\mathbb P(B^*):
\operatorname{rank}T(\beta)\le r\}.
\]

Its equations are the `(r+1)`-minors of the slice matrix, so it is
closed. Projection to V is a projective morphism, hence closed. The
image is exactly the tensors possessing a nonzero B functional with
slice rank at most `r`. The projective-proper fact is the Stacks
Project, [Tag 01WC](https://stacks.math.columbia.edu/tag/01WC), Lemma
29.44.5; proper morphisms are universally closed by
[Tag 01W0](https://stacks.math.columbia.edu/tag/01W0), Definition
29.42.1. Both were accessed 2026-10-21. Thus the Zariski closure of
ordinary images retains the low-rank slice property.

For (1), the exact dimensions are

\[
d=18,\quad \ell=3,\quad b=16,\quad r=3,
\qquad16+3>18.
\]

Every ordinary image and every degeneration of R into target format
`(16,16,16)` has a nonzero B functional whose slice rank is at most
three. A B slice of `M(4,4,4)` is, after reordering bases, the tensor
product of a nonzero `4 by 4` matrix with `I4`. Its rank is at least
four. Therefore

\[
\boxed{R\not\unrhd M(4,4,4).}
\]

## 5. A separate ordinary-restriction check

The family `p3 tensor P`, where `p3=t^5`, has dimension four. Its
interior correction vanishes because `J(p3)=0`. Every nonzero endpoint
slice in this family has rank four: each nonzero polynomial multiplied
by `1,t^3` gives two independent polynomials, and the two factor ranks
multiply. The family's aggregate long supports have dimensions
`(14,4)`, checked exactly by the script.

If an ordinary map sent R to M4, its A map would be invertible by
conciseness. This family would become a four-dimensional space of
rank-one `4 by 4` matrices, tensored with I4. Every linear space of
rank-one matrices has either a fixed image or a fixed coimage: two
members with independent images and independent coimages would have a
rank-two sum. At dimension four, its aggregate long supports in M4
must therefore be `(4,16)` or `(16,4)`. Neither can be obtained by
compressing `(14,4)`. This supplies another ordinary exclusion, while
the preceding low-rank slice proof also covers degeneration.

In particular, the rank of the pure slice `p3 tensor p3` is exactly
four. Matching the format of Q(4,3) does not identify the corner with
that source or supply a minimum-slice-rank-nine obstruction.

## Exact replay

```bash
python -S research/ai/2026-10-20-paired-construction/m1_endpoint_corner.py
python -S -m unittest discover -s tests -p 'test_m1_endpoint_corner.py'
```

The adjacent JSON stores all native maps, all canonical nonzero
coefficients, all coefficient-check counts, the rational flattening
ranks, and the low-rank support controls. Verification uses only the
Python standard library. It proves the finite identities and records
the stated algebraic obstruction; it does not turn the unfinished
general construction into a result.
