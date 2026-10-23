# An integer oblique repair of the paired polynomial source

October 23, 2026. Owner-directed Codex work. Complete coefficient and
scalar-decomposition certificates, with same-session separate checking.
No independent mathematical review, historical priority, or improvement
of the matrix multiplication exponent is claimed.

## Result

There are explicit integer local maps from `Q(6,4)` to
`M(5,4,5)-E`, with

\[
(r_A(E),r_B(E),r_C(E))=(9,11,11),\qquad R(E)\le19.
\tag{1}
\]

Thus `Q(6,4) direct-sum D_19` restricts to `M(5,4,5)`, where D_19
is nineteen independent scalar products. The nineteen rank-one correction
terms are supplied and replayed exactly. This is an ordinary restriction;
it uses no parameter, limit, Laurent pole, or numerical fit.

For comparison, embedding the existing exact `M(4,4,4)` construction
into this target leaves a missing-corner residual with ranks `(9,20,20)`
and the naive 36 scalar terms. The new residual has different flattening
ranks, so it is not merely a change of bases of that residual. No claim
is made that 19 is its optimal tensor rank. A simpler direct decomposition
has twenty terms; a seven-term convolution core saves one term.

A separately supplied nonproduct middle-space variant has the same
global ranks `(9,11,11)`, with a verified **24-term** scalar repair.
Its piece ranks differ from those of the product witness; they are not
inferred from its global ranks.

The general product family is constructive. For integers b>=2 and
n>=b+1, put r=n-1 and d=r-b. The maps below satisfy

\[
Q(n,b)\longrightarrow M(r,4,r)-E,
\qquad R(E)\le4rd.
\tag{2}
\]

When d>0, the exact residual flattening ranks are

\[
\boxed{(r^2-b^2,\ 2r+d,\ 2r+d).}
\tag{3}
\]

When d=0, the residual vanishes. In particular, one missing source inner
coordinate can be repaired as

\[
Q(k+1,k-1)\oplus D_{4k-1}\ge M(k,4,k)\qquad(k\ge3).
\tag{4}
\]

The source width in (4) grows with k. It does not establish a near-full
fixed-width family with a small asymptotic repair.

## 1. Conventions and the oblique polynomial decoder

The source and target are

\[
Q(n,b)=\sum_{p,q<n}\sum_{y,v<b}A_{pq}B_{y,q+v}C_{p+y,v},
\qquad
M(r,4,r)=\sum_{i,j<r}\sum_{\alpha<4}a_{ij}b_{i\alpha}c_{\alpha j}.
\]

Let s=b-1 and m=n+b-1. Use the outer polynomial basis

\[
U=(t,t^2,\ldots,t^{n-2},1-t^{n-1})\subset P_{n-1},
\qquad W=(1,t^s)\subset P_{b-1}.
\]

The product matrix D has rows `D_(2i+v,z)=[t^z]U_i W_v`.
Its dimension is `2r by m`. Its repeated monomial products are exactly

\[
U_iW_0=U_{i-s}W_1\quad(i\in J),
\qquad J=\{b-1,\ldots,n-3\},\quad |J|=d.
\tag{5}
\]

Choose the copy on the right of each equality for decoding. In the dual
L, the rows `(i,0)` with i in J are zero; every other product is decoded
to its own coordinate. The complete identity is

\[
LD^{\mathsf T}=P=I-N,
\qquad
N=\sum_{i\in J}(e_{i,0}-e_{i-s,1})e_{i,0}^{\mathsf T}.
\tag{6}
\]

Here is an explicit integer L. For an ordinary outer monomial with
index i<r-1, retain its unshifted row only when i is not in J:

\[
L_{i,0}=\epsilon_{i+1}
 +[i+1=s]\epsilon_{n+b-2},\qquad i\notin J.
\]

For every ordinary outer monomial retain its shifted row:

\[
L_{i,1}=\epsilon_{i+b}+[i+b=n-1]\epsilon_0.
\]

For the last outer polynomial set
`L_(r-1,0)=epsilon_0` and `L_(r-1,1)=-epsilon_(n+b-2)`.
These formulas check (6) directly, including the two nonmonomial products.
The decoder differs from the old reference's equal-weight average of
each repeated pair. That averaging spreads a dependency across two
outer coordinates; (6) assigns it to one.

## 2. Local tensor maps and the complete residual formula

Use the three local maps

\[
A_{pq}\mapsto\sum_{i,j}U_j(p)U_i(q)a_{ij},
\]

\[
B_{y,z}\mapsto\sum_{i<r,a,v<2}W_a(y)L_{i,v;z}b_{i,2a+v},
\qquad
C_{z,v_0}\mapsto\sum_{j<r,a,v<2}L_{j,a;z}W_v(v_0)c_{2a+v,j}.
\tag{7}
\]

Indices i,j in (7) range over r, and a,v over two. Their contraction
coefficient is

\[
P_{i'v',iv}P_{j'a',ja}
\]

at `a_(i,j) b_(i',2a+v') c_(2a'+v,j')`. Expanding `P=I-N`
gives the following actual tensor E. Define

\[
X_{i,a}=b_{i,2a}-b_{i-s,2a+1},\qquad
Y_{j,v}=c_{v,j}-c_{2+v,j-s}.
\]

Then

\[
\begin{aligned}
E={}&\sum_{i\in J,j<r,a<2}a_{ij}X_{i,a}c_{2a,j}\\
&+\sum_{i<r,j\in J,v<2}a_{ij}b_{i,v}Y_{j,v}\\
&-\sum_{i,j\in J}a_{ij}X_{i,0}Y_{j,0}.
\end{aligned}
\tag{8}
\]

Equation (8) is checked against every coefficient of the contraction,
including every off-target coefficient. Negative signs are part of the
actual residual, not a formal subtraction in a tensor semiring.

## 3. Scalar repair and exact flattening ranks

When exactly one of i,j is in J, the matrix coefficient of a_ij in E
is a sum of two rank-one matrices. When both are in J, its five apparent
terms in (8) combine into four:

\[
\begin{aligned}
E_{ij}={}&b_{i,0}c_{0,j}
 +(b_{i,2}-b_{i-s,3})c_{2,j}\\
&+b_{i,1}(c_{1,j}-c_{3,j-s})
 -b_{i-s,1}c_{2,j-s}.
\end{aligned}
\tag{9}
\]

Thus the total number of scalar terms is

\[
2\,[2d(r-d)]+4d^2=4rd.
\]

The two factors in each two-term slice are independent. In (9), its
four B factors and its four C factors are independent, so those slice
matrix ranks are exactly two and four respectively. This proves the
scalar upper bound by explicit terms, without inferring it from output
support alone.

Only the bad rows or bad columns occur in the first leg, giving the
upper bound `r_A(E)<=r^2-b^2`. For each such output `(i,j)`, take the
B/C coordinate `b_(i,0)c_(0,j)`. Its coefficient is exactly a_ij in
(8), and no other first coordinate contributes. These coordinates give
an identity minor of size `r^2-b^2`, proving equality.

The B support is spanned by all `b_(i,0),b_(i,1)` and by
`X_(i,1)` for i in J. These `2r+d` vectors are independent. They all
belong to the concise support: fixing any bad column, the two-term
slices provide the first two vectors for each good row, while (9)
provides them and X_(i,1) for each bad row. Thus its dimension is
exactly `2r+d`. The C calculation is the transpose. This proves (3).

These arguments use only coefficients 0,1,-1 and independent coordinate
vectors, so the product-family identities, scalar upper bound, and rank
formulas hold over every field.

### A seven-term core when there is one dependency

If n=b+2, then J={s} with s=b-1 and r=b+1. Consider the three first
coordinates u=a_(s,0), v=a_(0,s), and w=a_(s,s). Abbreviate

\[
\begin{gathered}
X=b_{s,0}-b_{0,1},\quad Z=b_{s,2}-b_{0,3},\quad
a=b_{0,0},\quad \eta=b_{0,1},\quad y=b_{s,1},\\
P=c_{0,0},\quad Q=c_{2,0},\quad
R=c_{0,s}-c_{2,0},\quad S=c_{1,s}-c_{3,0},\quad T=c_{2,s}.
\end{gathered}
\]

The residual on these coordinates is

\[
u(XP+ZQ)+v(aR+\eta S)+w(XQ+ZT+\eta R+yS+XR).
\]

Its seven rank-one terms are

\[
\begin{aligned}
&(u+w)(X+Z)Q+uX(P-Q)+wZ(T-Q)\\
&+(v+w)\eta(R+S)+v(a-\eta)R+w(y-\eta)S+wXR.
\end{aligned}
\tag{9a}
\]

This is the sum of two elementary rank-three binary-convolution
identities and one scalar term. The other row and column coordinates
need `4(r-2)` terms. Thus the total is `7+4(r-2)=4r-1`, proving (4).
`karatsuba_repair.py` supplies and expands every term, including the
combined first-leg factors u+w and v+w. The decomposition holds over
every field and is an upper bound, not an optimality assertion.

## 4. The n=6 residual pieces and endpoint repair cost

Here r=5, s=3 and J={3}. Split E according to its first coordinate:

| Piece | First support | Exact ranks | Rank-pair product | Direct scalar terms |
|---|---|---|---:|---:|
| Row | i=3, j!=3 | (4,2,8) | 8 | 8 |
| Column | i!=3, j=3 | (4,8,2) | 8 | 8 |
| Corner | i=j=3 | (1,4,4) | 4 | 4 |

The row and column pieces are copies of the corresponding inner-width-two
matrix products after changes of bases. The displayed ranks and explicit
terms suffice for their costs; no classification claim is needed.

The residual-rank criterion from
[pending PR130, pinned at 121be1c](https://github.com/1337isnot1337/matrix-mult-bounds/blob/121be1c232b117e884defdb74ba4527c55b70172/research/ai/2026-10-23-residual-rank-repair/proof.md)
therefore gives the endpoint character bound

\[
\lambda(E)\le2\,8^{3/4}+4^{3/4}.
\tag{10}
\]

Using the whole residual gives the weaker `99^(3/4)`, whereas the whole
embedded-corner residual gives `180^(3/4)`. The comparison uses exactly
the same stated envelope; it does not assert optimal character values.

There is no exponent improvement here. For this source and target, even
the zero-error version of the finite gate fails:

\[
(5\cdot4\cdot5)^{3/4}=10\sqrt{10}
<10\sqrt{30}
=\frac{\sqrt{2\cdot4\,(2\cdot6+4-1)^3}}3.
\]

## 5. A nonproduct middle space

The second n=6 witness uses

\[
H=(1\otimes W_0,\quad
   1\otimes W_1+(t+2t^2)\otimes W_0,\quad
   t^3\otimes W_0,\quad t^3\otimes W_1).
\]

This four-space is not K tensor W for a two-space K. Its projection onto
the W_1 coordinate is `span(1,t^3)`, which would force K to be that
space; its W_0 coefficient `t+2t^2` lies outside it.

Use the same B product decoder L. For the middle products U_j H_alpha,
retain all twenty input rows except 12 and 13. The eighteen retained
products form a basis of `P_8 tensor W`; their exact integer dual gives
the C map. All product rows, the selected basis, the dual and the three
tensor maps are stored in `witness.json`.

Its complete coefficient replay gives global residual ranks `(9,11,11)`.
Its row, column and corner pieces have ranks `(4,3,9)`, `(4,8,2)` and
`(1,4,4)`, respectively. The supplied scalar certificate has 24 terms.
Neither the product witness's direct 20-term count nor its improved
19-term count automatically transfers to this variant.

## 6. Scaling and scope of the construction

At fixed width b=4, the number of repeated products is d=n-5. The stated
one-sided decoder uses exactly these d bad outer modes. Its first rank
is `(n-1)^2-16`; the residual does not have small first support as n grows.

More generally, any coordinate decoder that selects one representative
per duplicated monomial must omit n-5 input products. Each outer mode
contains only two product coordinates. Concentrating these omissions
therefore requires at least `ceil((n-5)/2)` outer modes. This counting
statement concerns coordinate decoders for the stated polynomial space;
it says nothing about arbitrary long maps or degenerations.

For these supplied oblique maps, changing only the first map cannot
reduce the first residual rank. The B map has zero output coordinates
`b_(i,0),b_(i,2)` for i in J; the C map has zero coordinates
`c_(0,j),c_(1,j)` for j in J. Hence the B/C coordinate
`b_(i,0)c_(0,j)` is absent from the image whenever i or j belongs to J,
regardless of the first map. Its coefficient in the residual is therefore
exactly a_ij. These coordinates give an identity minor of size `r^2-b^2`
for every first map, and the displayed map attains that lower bound.
Equivalently, the intersection of the fixed source slice space with the
target slice space consists exactly of the b-squared good-row/good-column
slices. The n=6 certificate also
reconstructs an attaining first map by exact quotient elimination.

The [older equal-weight product decoder](../2026-10-23-product-longmap-residual/README.md)
has a different pair of long maps and a first residual minimum of 16 at
n=6 in characteristic different from two. Our minimum is nine over every
field. Changing the decoder changes the slice space. Neither fixed-map
calculation excludes other tensor constructions.

## 7. Exact files and replay

`verify.py` constructs the integer maps, checks the decoder identity,
contracts every coefficient of the native source, compares (8), splits the
actual residual, and replays both the direct and improved scalar
decompositions. `karatsuba_repair.py` supplies the seven-term core.
`exact.py` also supports rational and prime-field map files and supplies explicit
factorizations witnessing all three residual support ranks. Prime-field
results are never promoted to rational upper bounds.

`witness.json` contains both complete n=6 witnesses. `family-controls.json`
checks fixed-width n=5 through10 and additional one-dependency sizes.
The tests include deliberately false residual declarations, a modular
rank drop, rejected inexact inputs, and separate scalar counts for the
two variants.

```bash
python research/ai/2026-10-23-oblique-paired-repair/verify.py \
  --output /tmp/oblique-witness.json --family-output /tmp/oblique-family.json
python -m unittest discover -s tests -p test_oblique_paired_repair.py -v
```

The existing exact product-injection construction, the old equal-weight
projection reference, and the mixed-middle construction template are
credited in `sources.json`. The oblique selection, residual formulas,
repair counts and present exact witnesses are local deductions from them.
The verifier checks six local source hashes. The seventh source is the
immutable pending-PR130 link used only in Section 4; its hash is recorded
separately, and replay does not require that unmerged package locally.
