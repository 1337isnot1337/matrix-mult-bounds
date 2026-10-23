# A six-term core degeneration and an eighteen-scalar paired repair

October 23, 2026. Owner-directed Codex research. Written proof and exact
integer certificates, with separate checking inside the same session.
These checks are not independent mathematical review. No historical
priority, formalization, or improvement of omega is claimed.

## Result

The ordinary integer maps in the preceding oblique-repair package give

\[
Q(6,4)\longrightarrow M(5,4,5)-E,
\qquad (r_A(E),r_B(E),r_C(E))=(9,11,11),\qquad R(E)\le19.
\]

This follow-up keeps those maps and improves the correction by a
polynomial degeneration:

\[
\boxed{Q(6,4)\oplus D_{18}\ \unrhd\ M(5,4,5).}
\tag{1}
\]

Here D_s denotes s independent scalar products and the relation denotes
formal degeneration. The displayed maps have integer polynomial
coefficients. They give the formal degeneration over every field; over
the complex numbers, they give the usual border-rank statement
`border_rank(E)<=18`. The earlier bound `R(E)<=19` is an ordinary tensor
rank bound. We do not assert an eighteen-term ordinary decomposition or
optimal border rank for the whole residual.

The construction replaces a seven-term correction core by a six-term
degeneration. A unit minor of its Koszul map proves that this core has
border rank exactly six over C. The same minor proves the corresponding
formal lower bound in every characteristic.
The separate [ordinary-rank proof](ordinary_rank.md) establishes rank
exactly seven for this isolated core over every field.

There is also an all-size family. Write

\[
b\ge2,\quad n\ge b+1,\quad r=n-1,\quad d=r-b,\quad
s=b-1,\quad m=\min(d,s).
\]

For the existing oblique residual E_(n,b), this package constructs

\[
R(E_{n,b})\le4rd-m^2,\qquad
\underline R(E_{n,b})\le4rd-2m^2.
\tag{2}
\]

The second inequality is realized by the same type of integer polynomial
degeneration as (1). When d=0, the residual is zero. These are upper
bounds, not optimality assertions about E_(n,b).

| Source | Target | Direct scalar terms | Ordinary grid bound | Border grid bound |
|---|---|---:|---:|---:|
| Q(6,4) | M(5,4,5) | 20 | 19 | 18 |
| Q(7,4) | M(6,4,6) | 48 | 44 | 40 |
| Q(8,4) | M(7,4,7) | 84 | 75 | 66 |
| Q(9,4) | M(8,4,8) | 128 | 119 | 110 |

## 1. The core and six polynomial products

Use independent first-leg coordinates u,v,w, second-leg coordinates
X,Z,a,eta,y, and third-leg coordinates P,Q,R,S,T. The core is

\[
K=u(XP+ZQ)+v(aR+\eta S)
  +w(XQ+ZT+\eta R+yS+XR).
\tag{3}
\]

Set q=t^2(1-t). Define six polynomial rank-one terms:

\[
\begin{aligned}
F_1={}&(u+w)(X+Z)\,q(Q+R),\\
F_2={}&uX\,q(P-Q-R),\\
F_3={}&(w+tv)Z
  \bigl[q(T-Q)-(t+t^2)R-(1+t^2)S\bigr],\\
F_4={}&(v+w)\bigl[q\eta+(t+t^3)Z\bigr]\,(R+S),\\
F_5={}&(v+tu)\bigl[q(a-\eta)+(-t+t^2)Z\bigr]R,\\
F_6={}&w\bigl[q(y-\eta)+(1-t+t^2-t^3)Z\bigr]S.
\end{aligned}
\tag{4}
\]

Every bracket belongs to one tensor leg. Direct expansion gives

\[
\boxed{\sum_{j=1}^6F_j
  =t^2(1-t)(K+tH),\qquad
H=vZ(T-Q)+u(a-\eta)R.}
\tag{5}
\]

Thus the degree-zero and degree-one coefficient tensors vanish. The
degree-two coefficient is K, the degree-three coefficient is H-K, and
the degree-four coefficient is -H. There are no other degrees.
`border_six.py` reconstructs all 75 tensor coordinates and compares their
complete integer polynomials. In particular, its check includes every
off-support coordinate.

Equation (5) is a six-term formal degeneration. Its coefficients are
integers and its leading scalar coefficient is one, so no field
characteristic is excluded. Over C, dividing the complete tensor by
t-squared and taking t to zero proves `border_rank(K)<=6`.

### How the polynomial identity was obtained

Remove the last term wXR from (3). The remaining two binary-convolution
pieces have three-term decompositions with first factors

\[
(u+w),u,w\quad\hbox{and}\quad(v+w),v,w.
\]

Replace the third listed first-leg factor in the first group by w+tv,
and the second listed first-leg factor in the second group by v+tu.
The first three products have second
factors in span(X,Z), while the last three have third factors in
span(R,S). Adding arbitrary R,S components to the first group's third
factors and arbitrary X,Z components to the last group's second factors
therefore changes only the mixed block
`span(u,v,w) tensor span(X,Z) tensor span(R,S)`.

The twelve mixed coefficient equations have determinant
`-t^2(t-1)` in the specified basis. A direct solution adds R, -R, and

\[
\frac{t+1}{t(t-1)}R+\frac{t^2+1}{t^2(t-1)}S
\]

to the first group's third factors. It adds, respectively,

\[
-\frac{t^2+1}{t(t-1)}Z,\qquad-\frac1tZ,\qquad
\frac{t^2+1}{t^2}Z
\]

to the last group's second factors. The mixed block becomes exactly
wXR. The two diagonal blocks change by tH, and no other block appears.
Clearing the common factor q gives (4). This derivation explains the
construction; the polynomial identity (5) is the acceptance certificate
and does not rely on a numerical solve.

## 2. A field-independent lower bound for the core

For any tensor T in A tensor B tensor C with dim(A)=3, consider the
linear map

\[
\Phi_T:A\otimes B^*\longrightarrow\Lambda^2 A\otimes C,
\qquad x\otimes\beta\longmapsto
\sum_j (a_j\wedge x)\otimes\beta(b_j)c_j,
\]

where `T=sum_j a_j tensor b_j tensor c_j`. This map is independent of
the chosen expression for T and is linear in T. For a rank-one tensor,
the wedge map has rank at most two, so `rank(Phi_T)<=2`.
Consequently a sum of k rank-one tensors has Koszul rank at most 2k.
Matrix rank conditions are closed because they are defined by minors,
so the same inequality holds in a formal degeneration or a complex
border-rank limit.

For K, the map is a 15-by-15 integer matrix. With row order
`(u wedge v, u wedge w, v wedge w) tensor (P,Q,R,S,T)` and column order
`(u,v,w) tensor (X*,Z*,a*,eta*,y*)`, its rows

`0,1,2,3,5,6,7,8,9,12,13`

and columns

`0,1,2,3,4,5,6,8,9,10,11`

give an 11-by-11 minor of determinant +1. `core-koszul.json` stores the
full map, these indices, and a singleton-row/column Laplace certificate.
The verifier reconstructs the map directly from (3) and replays the
determinant. The minor is nonzero in every characteristic. Hence every
formal rank bound is at least ceil(11/2)=6, which matches (5).

This proves the core's border-rank result. The separate
[ordinary-rank argument](ordinary_rank.md) proves that the core has
ordinary rank seven. Neither argument proves optimal ordinary or border
rank for the full n=6 residual.

## 3. Disjoint cores in the general residual

The inherited product maps have bad outer indices

\[
J=\{s,s+1,\ldots,r-2\},\qquad |J|=d.
\]

Let

\[
I_0=\{i\in J:i-s\notin J\},\qquad |I_0|=m=\min(d,s).
\]

The direct scalar decomposition uses two terms for each first coordinate
with exactly one bad index and four terms for each coordinate with both
indices bad. Its total is 4rd.

For every ordered pair `(i,j)` in I_0 squared, put k=i-s and ell=j-s.
The three first coordinates

\[
u=a_{i,\ell},\qquad v=a_{k,j},\qquad w=a_{i,j}
\]

have eight direct terms. Substitute

\[
\begin{gathered}
X=b_{i,0}-b_{k,1},\quad Z=b_{i,2}-b_{k,3},\quad
a=b_{k,0},\quad\eta=b_{k,1},\quad y=b_{i,1},\\
P=c_{0,\ell},\quad Q=c_{2,\ell},\quad
R=c_{0,j}-c_{2,\ell},\quad
S=c_{1,j}-c_{3,\ell},\quad T=c_{2,j}.
\end{gathered}
\tag{6}
\]

Those eight terms become exactly K. The three kinds of first coordinates
are bad/good, good/bad, and bad/bad, respectively. Each kind determines
i and j uniquely. Thus all m-squared selected triples are disjoint,
even when other bad indices have bad predecessors.

The inherited seven-term ordinary core replaces eight terms by seven,
giving the first bound in (2). Equation (5) replaces them by six
polynomial terms. Multiply each remaining direct rank-one term by q in
one leg. Summing all terms gives the exact identity

\[
\sum_{\nu=1}^{4rd-2m^2}G_\nu(t)
  =q\bigl(E_{n,b}+tH_{n,b}\bigr),
\tag{7}
\]

where H_(n,b) is the sum of the substituted H terms. This proves the
second bound in (2). No assumption about disjoint second or third
supports is needed: disjoint first coordinates identify which direct
terms are replaced, and the polynomial identities are then added.

## 4. Complete source degeneration and verification

The old maps send Q(n,b) to `M(r,4,r)-E_(n,b)`. Multiply their first-leg
map by q, and use the terms in (7) as the three local maps on an added
diagonal tensor. The complete image is

\[
q(M-E_{n,b})+q(E_{n,b}+tH_{n,b})
  =q(M+tH_{n,b})
  =t^2M+O(t^3).
\tag{8}
\]

This supplies the actual degeneration maps, including the common leading
power. At n=6,b=4, the source `Q(6,4) direct-sum D_18` has format
`(54,54,54)` and the target has format `(25,20,20)`. `witness.json`
contains all three polynomial local maps, all eighteen residual terms,
the error H, the source replay, the six canonical core terms, the Koszul
certificate summary, and 72 exact family controls.

The field-independent formal identity is checked using only standard
Python integer and rational arithmetic. Separate same-session checks
also reconstructed the canonical 75-coordinate identity and native
source contractions for n=6,7,8,9 at b=4 using a prior repository
contraction implementation.

```bash
python research/ai/2026-10-23-oblique-border-repair/border_six.py \
  --output /tmp/oblique-border-witness.json --repository .
python -m unittest discover -s tests -p test_oblique_border_repair.py -v
```

Four immutable local-source hashes credit the preceding ordinary map and
repair package. This follow-up does not change those maps or its separate
nonproduct witness.

## 5. Scope

The n=6 finite improvement gate already fails with zero residual, as
shown in the preceding package. A smaller scalar correction does not
change that fact. The earlier residual-piece character envelope is also
smaller than eighteen; no stronger endpoint character bound is asserted
from the scalar count alone.

At fixed b, the residual still has quadratic first support and the
border repair in (2) remains quadratic. These constructions do not meet
the near-full fixed-width small-repair criterion. Their positive content
is the explicit finite degeneration, the reusable disjoint-core repair,
and the exact border rank of the small core.
