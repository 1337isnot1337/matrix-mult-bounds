# A rowspace obstruction for two fixed rank-one degree-13 maps

## Precise statement

Consider the stated torus profile for an ordinary restriction

\[
 A(8,8)\longrightarrow M_{27}\oplus M_7.
\]

The M27 vertex multiplicities at charges 0 through 14 are

\[
 (1,1,2,2,2,2,2,3,2,2,2,2,2,1,1).
\]

Let `L`, `P` and `H` be the unique M27 vertices at charges 0, 13 and
14. In the 64-dimensional physical source space, put

\[
 u=e_{(7,0)},\quad v=e_{(0,7)},\quad b=e_{(6,0)}.
\]

**There is no such torus restriction if, on two cyclically adjacent
legs X and Y, the maps send `E_(H,L)` to a nonzero scalar multiple of
`E_(u,v)` and `E_(P,L)` to a nonzero scalar multiple of `E_(b,v)`.**

The two scalar multiples on each leg may differ. The maps need not be
equal on different legs. All other source coefficients may vary.
The proof does not use either negative extreme, any negative degree-13
map, or the degree-13 map on the third leg. In common source coordinates
the two prescribed matrices are `F(7,0,7)` and `F(6,0,7)`.

This closes the degree-13 rank-one choice in the stored endpoint
constructions, independently of how their remaining boundary channels
are filled. It is stronger than rejecting a particular boundary seed.
It does **not** exclude general two-dimensional source pencils at
degree 13, other torus profiles, or arbitrary source degenerations.
No matrix multiplication exponent improvement is established.

The argument was checked by the parent and root as second agents in
this generating session; no external independent review or formalization
has occurred. The accompanying standard-library script checks the
coordinate identities and dimension counts used below.

## Source rows, columns and adjacent charges

Use the common physical matrix convention

\[
 W(F)_{(i,q),(p,s)}=F_{i,p+q,s},\qquad 0\le i,p,q,s<8.
\]

The common source coordinate `F(i,k,s)` has weight `i+s-k`. For each
charge q, let `V_q` be the physical subspace of charge `q-7`, with basis
`(i,j)` satisfying `i-j=q-7`, ordered by increasing i. Its dimension is

\[
 d_q=8-|q-7|.
\]

For a lift on any leg, define three lists of target linear forms:

\[
\begin{aligned}
 R(q)&=e_v^T J\big|_{V_q},
 &R(q)_{(i,j)}&=F(0,7+i,j),\\
 C(q)&=J e_u\big|_{V_q},
 &C(q)_{(i,j)}&=F(i,7+j,0),\\
 K(q)&=J e_b\big|_{V_q},
 &K(q)_{(i,j)}&=F(i,6+j,0).
\end{aligned}
\]

Their target-form weights are respectively `-q`, `q-14` and `q-13`.
Here a coordinate expression denotes its coefficient as a linear form
in the target input; the three leg maps can have unrelated coefficients.

For `0 <= q <= 6`, the coordinates of `K(q)` are exactly the first
`q+1` coordinates of `C(q+1)`. This follows by replacing j by `j-1`:
the first physical index i does not change, and every j in this range
is positive. Thus

\[
 K(q)=C(q+1)\big|_{\text{first }q+1\text{ rows}}.
 \tag{1}
\]

At the high end the corresponding identities needed here are

\[
\begin{aligned}
 R(12)_0&=C(2)_0=F(0,12,0),\\
 K(12)&=(F(5,6,0),\ C(13)_0,\ C(13)_1).
\end{aligned}
\tag{2}
\]

In particular `C(2)` has three rows, `R(12)` has three columns, and
`C(13)` has two rows. The term `F(5,6,0)` in the second line is unrestricted;
the proof will eliminate its coefficient rather than setting it to zero.

## The slice identities and a general low-charge inequality

For a vertex t of charge q, use these distinct target coordinate forms:

\[
 U_q=(E_{L,t})_t,\qquad
 V_q=(E_{t,H})_t,\qquad
 S_q=(E_{t,P})_t.
\]

An extreme source matrix `E_(u,v)` gives the identities

\[
 R_Y(q)C_Z(q)=\text{nonzero scalar}\cdot U_q(Y)V_q(Z).
 \tag{3}
\]

The rank-one predecessor `E_(b,v)` instead gives

\[
 R_Y(q)K_Z(q)=\text{nonzero scalar}\cdot U_q(Y)S_q(Z).
 \tag{4}
\]

The scalar depends on the selected fixed image and is irrelevant to
all rowspace statements. These equations follow directly from
`tr(E_(u,v) J_Y J_Z)=e_v^T J_Y J_Z e_u` and its version with b.

Equations (1), (3) and (4) imply an adjacent-charge necessary condition.
If the M27 vertex multiplicities are `m_q`, then the rowspace of
`C(q+1)` must contain the `m_(q+1)` independent forms `V_(q+1)` from
(3), and the `m_q` independent forms `S_q` from (4). The two sets are
disjoint matrix coordinates, since their column vertices are H and P.
Hence

\[
 \boxed{m_q+m_{q+1}\le q+2\qquad(0\le q\le6).}
 \tag{5}
\]

The present profile satisfies all seven inequalities. They are equalities
at q=0, 1 and 2. Equality at q=1 is the decisive extra information: it
determines the entire rowspace of `C(2)`, not just its dimension.

## The rank chain

Assume the prescribed source images on X and Y, and suppose a complete
target restriction exists.

**First, the X slices determine the rowspace of `C_Z(2)`.**
Equation (3) at q=2 puts the two forms `V_2` in that rowspace.
Equation (4) at q=1, together with (1), also puts the single form
`S_1` there. These are three distinct matrix coordinates, and `C_Z(2)`
has only three rows. Therefore

\[
 \operatorname{rowspan}C_Z(2)=\operatorname{span}(V_2,S_1).
 \tag{6}
\]

The two forms `U_12` are different target coordinates of the same
weight -12. No row in (6) has a coefficient on either of them. By the
first shared-coordinate identity in (2), the first column of `R_Z(12)`
also vanishes on both `U_12` input vectors.

**Second, the Y extreme slice forces an invertible remaining block.**
Restrict (3) for the Y anchor, at q=12, to the two-dimensional `U_12`
subspace of the Z input. On that subspace write

\[
 R_Z(12)\big|_{U_{12}}=(0\mid B),
\]

where B is a two by two matrix. The required target bilinear form has
rank two. Its product through `(0|B)` can have rank two only if B is
invertible.

**Third, the Y predecessor slice exhausts the rowspace of `C_X(13)`.**
Use (4) for the Y anchor at q=12, again restricted to the two `U_12`
inputs. The second identity in (2) and the zero first column give

\[
 B\,C_X(13)=\text{nonzero scalar}\cdot S_{12}.
\]

The unrestricted coordinate `F(5,6,0)` has disappeared because its
coefficient is zero. Since B is invertible, the two rows of `C_X(13)`
span exactly the two forms `S_12`.

**Finally, the Y extreme slice requires a third independent form.**
Equation (3) for the same Y anchor at q=13 requires the nonzero form
`V_13` to lie in the rowspace of `C_X(13)`. It is a third distinct
matrix coordinate, independent of both forms `S_12`. A two-dimensional
rowspace cannot contain all three. This is the contradiction.

Only the X and Y selected source images entered this chain. It uses
exact coefficient identities and finite-dimensional linear algebra;
it does not assume a common basis for the three unknown maps or any
fixed completion outside the four prescribed source images.

## Exact coordinate replay

`parity_balancing_rankone_13_chain.py` expands both prescribed source
slices by enumerating all 262,144 source terms. Each slice has 64 terms.
The script compares the complete symbolic coordinate pairs against
the displayed `R*C` and `R*K` factorizations. It checks all seven shifts
in (1), both identities in (2), and the distinct target coordinates
responsible for the `3 > 2` rowspace contradiction.

The code is a replay of the finite ingredients of the written proof.
It does not infer a universal theorem merely from numerical examples.
The ordinary restriction exclusion follows from the rank chain above.

```bash
python -S research/ai/2026-10-20-anisotropic-constructions/parity_balancing_rankone_13_chain.py
python -S -m unittest discover -s tests -p test_parity_balancing_rankone_13_chain.py -v
```

The exact coordinate certificate is
`results/anisotropic-constructions-2026-10-20/parity_balancing_rankone_13_chain.json`.
The next boundary search must vary the degree-13 pencils themselves,
instead of keeping the adjacent rank-one images and changing only the
later channel assignments.
