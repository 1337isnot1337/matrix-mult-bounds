# A complete degree-13 obstruction for one torus profile

## Statement and scope

There is no ordinary restriction

\[
 A(8,8)\longrightarrow M_{27}\oplus M_7
\]

that preserves the following integer grading on all three legs. The
source coordinate `F(i,k,s)` has weight `i+s-k`. Each of the three
27-dimensional target vertex spaces has charge multiplicities

\[
 (1,1,2,2,2,2,2,3,2,2,2,2,2,1,1)
 \qquad\text{at charges }0,\ldots,14,
 \tag{1}
\]

and each seven-dimensional vertex space has one vertex at every charge
from 0 to 6. A matrix unit has weight equal to its row charge minus
its column charge. The three maps may be unrelated and may use arbitrary
coefficients in every source weight block. In particular, the theorem
does not fix any of the boundary seeds used in earlier experiments.

This excludes the complete stated profile for **ordinary grading-preserving
maps**. It does not exclude other common charge profiles, different
charge lists on the three target vertex spaces, ungraded restrictions,
or arbitrary singular limits. It does not change the ordinary finite
source frontier or establish a smaller matrix multiplication exponent.

The proof uses the local
[two-leg rank-chain theorem](parity_balancing_rankone_13_chain.md) and its
[four symmetry versions](parity_balancing_rankone_13_symmetry.md).
The remaining ingredients are the product tables and finite cyclic
classification below. The argument was checked by two other agents in
this generating session; no external independent review or formalization
has occurred. The accompanying standard-library program replays the
finite coordinate and polynomial identities, including every Boolean
case in the classification.

## Extreme units and the two source pencils

Use the physical source realization

\[
 W(F)_{(i,q),(p,s)}=F(i,p+q,s),\qquad 0\le i,p,q,s<8.
 \tag{2}
\]

The tensor is `tr(W(X) W(Y) W(Z))`. An ordinary restriction is specified
by maps from target inputs into the source coordinate spaces that make
this trace equal to the target trace. Each map is injective because
the target tensor is concise: a nonzero matrix input has a nonzero
trace pairing with some two other matrix inputs.

Write `L=0`, `L1=1`, `P=25`, and `H=26` for the unique vertices at
charges 0, 1, 13, and 14. The two negative degree-13 target units are

\[
 N_1=E_{L,P},\qquad N_2=E_{L1,H},
\]

and the positive ones are

\[
 P_1=E_{P,L},\qquad P_2=E_{H,L1}.
\]

There are no other target units at either degree. The complete negative
source degree-13 basis, and its positive reflection, are

\[
\begin{array}{lll}
 P=F(0,13,0),&Q=F(0,14,1),&R=F(1,14,0),\\
 P'=F(7,1,7),&Q'=F(7,0,6),&R'=F(6,0,7).
\end{array}
 \tag{3}
\]

The letter `P` in the source basis is distinguished from the vertex
label by its coordinate expression or prime. On each leg `i` denote
the negative two-by-three coefficient matrix by `[p_i q_i r_i]` and
the positive one by `[s_i t_i u_i]`. Each column is a two-vector in
the corresponding target basis. For example, the image of `N_1` is
`p_i1 P+q_i1 Q+r_i1 R`. Both coefficient matrices have row rank two.

The extreme source blocks have dimension one. Consequently the target
units `E_(H,L)` and `E_(L,H)` map on every leg to nonzero scalar multiples
of `F(7,0,7)` and `F(0,14,0)`, respectively. Put

\[
 a=F(0,7,7),\qquad b=F(7,7,0).
\]

Contracting the two extreme maps, in their respective orders, gives
on the remaining target input `Z`

\[
 a(J(Z))=\lambda z_{LL},\qquad
 b(J(Z))=\mu z_{HH},\qquad \lambda,\mu\ne0.
 \tag{4}
\]

The scalars can depend on the leg and order. No simultaneous
normalization of the six extreme maps is assumed or needed.

## The universal product tables

For a third arbitrary source input, the trace pairing of the negative
basis on the left with the positive basis on the right is

\[
\begin{array}{c|ccc}
 &P'&Q'&R'\\ \hline
 P&v&h&a\\
 Q&a&0&0\\
 R&w&a&0
\end{array}
\quad
\begin{aligned}
 h&=F(0,6,6),\\
 v&=F(1,7,6),\\
 w&=F(1,8,7).
\end{aligned}
 \tag{5}
\]

For the opposite order the table has the same pattern:

\[
\begin{array}{c|ccc}
 &P&Q&R\\ \hline
 P'&v'&h'&b\\
 Q'&b&0&0\\
 R'&w'&b&0
\end{array}
\quad
\begin{aligned}
 h'&=F(7,8,1),\\
 v'&=F(6,7,1),\\
 w'&=F(6,6,0).
\end{aligned}
 \tag{6}
\]

These tables follow by multiplying the physical matrices in (2).
For example, `P` is the sum of the units
`E_((0,7),(6,0))` and `E_((0,6),(7,0))`, while `R'` is
`E_((6,0),(0,7))`. Their product is the diagonal unit at `(0,7)`,
whose trace pairing with `W(F)` is exactly `a`.

Now take a negative pencil on leg `i` and the positive pencil on the
next leg `j=i+1`, with indices modulo three. Suppress the leg subscripts
temporarily. The two-by-two matrix of bilinear coefficient forms is

\[
 vps^T+hpt^T+wrs^T+a(pu^T+qs^T+rt^T).
 \tag{7}
\]

The required target matrix is `diag(z_LL,z_L1L1)`. Let
`ell=(-p_2,p_1)^T` and `m=(-s_2,s_1)^T`. Contracting (7) by
`ell^T` and `m` kills all three terms with `v,h,w`, as well as the
first two terms multiplied by `a`. With (4), comparison of the two
independent target diagonal forms gives

\[
 p_1s_1=0,\qquad
 p_2s_2=\lambda\det(p,r)\det(s,t).
 \tag{8}
\]

In particular, if both determinants are nonzero, then `p_2` and `s_2`
are nonzero. This calculation does not require any of the other
third-input coefficient forms to be independent.

For a positive pencil on leg `i` followed by a negative one on `j`,
the required matrix is `diag(z_PP,z_HH)`. Applying the same calculation
to (6) gives

\[
 s_2p_2=0,\qquad
 s_1p_1=\mu\det(s,u)\det(p,q).
 \tag{9}
\]

If all four displayed projection determinants are nonzero on every
leg, (8) forces every `p_i2` and `s_i2` to be nonzero. Equation (9) on
any consecutive pair then gives a contradiction. It remains to treat
the singular projections; they cannot be discarded as nongeneric.

## Singular projections force specified pure rows

The extreme slices imply the following column-span containments on
each leg:

| Projection columns | Required vector in their span | Physical projection |
| --- | --- | --- |
| `p,r` | `(0,1)` | `J(N) e_(7,0)` |
| `p,q` | `(1,0)` | `e_(0,7)^T J(N)` |
| `s,t` | `(0,1)` | `e_(7,0)^T J(P)` |
| `s,u` | `(1,0)` | `J(P) e_(0,7)` |

For example, multiplying a negative target input by `E_(H,L)` gives
zero on `N_1` and the nonzero unit `E_(L1,L)` on `N_2`. In the source,
this product factors through `J(N)e_(7,0)`, whose only channels have
coefficient columns `p,r`. Pairing with the appropriate third target
unit shows that `(0,1)` lies in their column span. The other three
rows follow from the corresponding left or right extreme products.

Define four singularity types on leg `i`:

| Type | Vanishing determinant | Consequence |
| --- | --- | --- |
| `A_i` | `det(p_i,r_i)=0` | `p_i1=r_i1=0`; `N_1` maps to a nonzero multiple of `Q` |
| `B_i` | `det(p_i,q_i)=0` | `p_i2=q_i2=0`; `N_2` maps to a nonzero multiple of `R` |
| `C_i` | `det(s_i,t_i)=0` | `s_i1=t_i1=0`; `P_1` maps to a nonzero multiple of `R'` |
| `D_i` | `det(s_i,u_i)=0` | `s_i2=u_i2=0`; `P_2` maps to a nonzero multiple of `Q'` |

A singular two-by-two projection containing the specified nonzero
vector has exactly that one-dimensional column span. This proves the
zero-coordinate conclusions. The remaining pure coefficient is
nonzero because the full target-to-source map is injective.

For each individual type, the
[rank-chain theorem and its symmetries](parity_balancing_rankone_13_symmetry.md)
exclude its occurrence on two different legs. There are three cyclic
legs, so every pair is adjacent in one of the two cyclic orders.
Thus each of `A,B,C,D` occurs on at most one leg. The theorem permits
arbitrary nonzero multiples of the pure row and of its extreme partner,
as required here.

## Mixed types and the cyclic implications

Two types on distinct legs are excluded by direct products:

\[
 A_i C_j\text{ is impossible, and }B_i D_j\text{ is impossible}
 \qquad(i\ne j).
 \tag{10}
\]

Both orders matter. If a negative `A` leg precedes a positive `C` leg,
the source product `Q R'` is zero, whereas `N_1 P_1` requires `z_LL`.
In the opposite order `R' Q` gives only a nonzero multiple of `b`,
which by (4) is proportional to `z_HH`; the target requires the
independent form `z_PP`. For `B` before `D`, the source product
`R Q'` gives only `a`, proportional to `z_LL`, while the target
requires `z_L1L1`. For `D` before `B`, `Q' R` is zero whereas the
target requires `z_HH`. All scalar coefficients of the prescribed
pure maps are nonzero and do not change these contradictions.

Equations (8) and (9) also give, for every `i` modulo three,

\[
\begin{aligned}
 (B_i\lor D_{i+1})&\ \Longrightarrow\ (A_i\lor C_{i+1}),\\
 (C_i\lor A_{i+1})&\ \Longrightarrow\ (D_i\lor B_{i+1}).
\end{aligned}
 \tag{11}
\]

Indeed, if both types on the right of the first implication are absent,
the determinants in (8) are nonzero and hence `p_i2,s_(i+1)2` are
nonzero. This excludes both types on its left. The second implication
uses the nonzero coordinates in (9) in exactly the same way.

Each type now has four possible locations: absent, or one of the three
legs. Among these `4^4=256` assignments, (10) and (11) leave exactly
the following ten:

| Locations of `A,B,C,D` | Number | Form |
| --- | ---: | --- |
| `(-1,-1,-1,-1)` | 1 | All four types absent |
| `(i,i,-1,-1)` | 3 | `A=B` on one leg |
| `(-1,-1,i,i)` | 3 | `C=D` on one leg |
| `(i,i,i,i)` | 3 | All four on one leg |

Here `-1` denotes absence and `i` ranges over 0, 1, and 2. This is a
finite part of the proof. The accompanying program exhausts all 256
assignments, and the regression test separately exhausts the 4,096
Boolean incidence assignments before imposing the at-most-one condition.
The predicates are precisely (10) and (11); no numerical rank decision
enters the enumeration.

## The double-singular cases

Suppose `A=B` on one leg. The negative coefficient columns then have
the form

\[
 p=0,\qquad q=(q_1,0)^T,\qquad r=(0,r_2)^T,
 \qquad q_1r_2\ne0.
\]

Use any positive pencil on the next leg. By (5), the coefficient
of the off-diagonal target pair `N_1,P_2` is `q_1 s_2 a`. Its required
value is zero. Since `a` is a nonzero multiple of `z_LL`, this forces
`s_2=0`. The diagonal pair `N_2,P_2` now has coefficient `r_2 t_2 a`,
which cannot equal the independent form `z_L1L1`. Thus `A=B` is
impossible, independently of all other singularity types.

For completeness, if `C=D` on a leg then

\[
 s=0,\qquad t=(0,t_2)^T,\qquad u=(u_1,0)^T,
 \qquad t_2u_1\ne0.
\]

The off-diagonal pair `P_2,N_1` on the next negative leg gives
`t_2 p_1 b=0`, so `p_1=0`. The diagonal pair `P_1,N_1` then gives
only `u_1 q_1 b`, which cannot equal the independent form `z_PP`.
Hence `C=D` is also impossible. These arguments could alternatively
be exchanged by the exact source and target symmetries.

Nine assignments in the table are therefore impossible. The remaining
all-absent assignment is the all-generic case already contradicted by
(8) and (9). This proves the stated ordinary torus-profile exclusion.

## Exact replay and remaining construction problem

The program checks all 17,280 coefficients in the 18 ordered source
products (5) and (6), the two extreme products, all four physical
endpoint projections, ten formal polynomial identities, the four
ordered mixed-type contradictions, and all 256 singularity assignments.
The tests include a deliberately altered product-table coefficient and
an independent Boolean-incidence enumeration. These checks support the
written proof and do not constitute a formal proof assistant certificate.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/torus_degree13_pencils.py
python -S -m unittest discover -s tests -p test_torus_degree13_pencils.py -v
```

The saved report is
`results/anisotropic-constructions-2026-10-20/torus-degree13-pencils.json`.
Earlier exact partial embeddings and anchor identities remain valid
within their recorded scopes; none extends to the complete target with
the present grading. Further construction work must change this profile
or the ordinary grading-preserving model. The ungraded target
`A(8,8) -> M27 direct_sum M7` remains unconstructed and is not excluded
by this note.
