# An integral direct-sum construction in the full source

October 21, 2026. This note gives explicit ordinary restrictions

\[
A(a,a)\longrightarrow M(2a-2)\oplus M(a-2),\qquad a\ge3.
\]

In particular, the full source A(5,5) restricts to M8 plus M3. This is a
constructive control family. It does not improve the matrix multiplication
exponent, and it is not a construction from the parity degeneration.
No historical priority, external independent review, or formal verification
is claimed.

## Polynomial data

Put d=a-1 and k=x^d-1. Let P_d be the polynomials of degree at most d.
Use the ordered short-leg families

\[
U=(1,k),\qquad V=(x,x^2,\ldots,x^{d-1},k).
\]

The 2d products U_alpha V_beta are independent. Indeed, a relation
v_0+k v_1=0 with v_0,v_1 in span(V) forces v_1 to be constant, by degrees.
The functional

\[
h(f)=[x^0]f+[x^d]f+[x^{2d}]f
\]

vanishes on every such product, whereas h(1)=1. In particular span(V)
contains no nonzero constant, so v_1=v_0=0. Adjoining 1 to the products
therefore gives a basis of P_(2d).

The dual rows R_(alpha,beta), followed by h, are integral. Writing e_j
for extraction of the coefficient of x^j, they are

\[
\begin{aligned}
R_{0,j}&=e_j+e_{j+d}, &R_{1,j}&=e_{j+d} &&(1\le j<d),\\
R_{0,k}&=e_d+2e_{2d}, &R_{1,k}&=e_{2d},\\
h&=e_0+e_d+e_{2d}.
\end{aligned}
\]

Thus the short maps U,V and the 2d long maps R restrict C(a,a) to the
outer-product tensor of dimensions (2,d,2d). Three cyclic copies give
the M(2d) core.

The Hankel matrix H=(h_(i+j)) on P_d has kernel span(k). Its nonzero
pairings are the first and last coordinate pairings and the antidiagonal
pairings i+j=d. Define

\[
P=(x,x^2,\ldots,x^{d-1}),\qquad
Q=(x^{d-1},x^{d-2},\ldots,x).
\]

Then

\[
P H Q^{\mathsf T}=I_{d-1},\qquad
U H V^{\mathsf T}=0,\qquad U H Q^{\mathsf T}=0.
\]

Every identity is over the integers. One can interpret H as the normalized
sum of evaluations at the d-th roots of unity, but no algebraic numbers
are needed in the restriction matrices.

## Complete maps and vanishing of mixed coefficients

The source coefficient is one at

\[
X=(i,p+q,s),\quad Y=(j,p,r+s),\quad Z=(i+j,q,r).
\]

For the M(2d) core, write vertices

\[
I=(\alpha_1,\beta_2),\quad
J=(\alpha_2,\beta_3),\quad
K=(\alpha_3,\beta_1),
\]

where alpha ranges over two values and beta over d values. The maps are

\[
\begin{aligned}
A_{(I,J),(i,t,s)}&=U_{\alpha_1,i}R_{(\alpha_2,\beta_2),t}V_{\beta_3,s},\\
B_{(J,K),(j,p,u)}&=V_{\beta_1,j}U_{\alpha_2,p}R_{(\alpha_3,\beta_3),u},\\
C_{(K,I),(v,q,r)}&=R_{(\alpha_1,\beta_1),v}V_{\beta_2,q}U_{\alpha_3,r}.
\end{aligned}
\]

For the M(d-1) block, whose vertices i',j',k' range from zero through d-2,
append the rows

\[
\begin{aligned}
A'_{(i',j'),(i,t,s)}&=P_{j',i}h_t Q_{i',s},\\
B'_{(j',k'),(j,p,u)}&=Q_{j',j}P_{k',p}h_u,\\
C'_{(k',i'),(v,q,r)}&=h_v Q_{k',q}P_{i',r}.
\end{aligned}
\]

Three core rows contract to M(2d), by R(UV)=I. Three appended rows contract
to M(d-1), by P H Q^T=I.

If a coefficient uses one appended row and two core rows, the long h in
the appended row contracts U and V from the two core rows. The factor
U H V^T is zero. If a coefficient uses two appended rows and one core row,
the U factor from the core row pairs with Q from the adjacent appended row
through H. The factor U H Q^T is zero. This covers every mixed choice and
proves the direct-sum assertion coefficient by coefficient.

## Exact verification and saved arrays

`parity_structure_direct_sum.py` recomputes the two polynomial inverse
identities, the three Hankel identities, the original full source, and
every coefficient of the image. Integer accumulation is exact.

| a | Source format | Exact target | Target format | Target terms |
| ---: | ---: | --- | ---: | ---: |
| 3 | 45 cubed | M4 plus M1 | 17 cubed | 65 |
| 4 | 112 cubed | M6 plus M2 | 40 cubed | 224 |
| 5 | 225 cubed | M8 plus M3 | 73 cubed | 539 |
| 6 | 396 cubed | M10 plus M4 | 116 cubed | 1,064 |

All four complete coefficient checks pass. The saved A(5,5) matrices are
in `parity_structure_direct_sum_maps.npz`, keys A,B,C. They have shape
(73,225), with target coordinates first. Each has 207 nonzero entries,
all in {-2,-1,1,2}. U,V,R,h,P,Q are included as well. The JSON certificate
records the exact checks and the source and target formats.

Source flattening orders agree with `parity_structure.py`:

    X: (i*(2a-1)+t)*a+s,
    Y: (j*a+p)*(2a-1)+u,
    Z: (v*a+q)*a+r.

For a=5, core rows are ordered 8*I+J, 8*J+K, 8*K+I. The M3 rows have
offset 64 and order 3*i'+j', 3*j'+k', 3*k'+i'. This gives an exact
M8-plus-M3 seed with all mixed coefficients zero.

Run from the repository root:

    python research/ai/2026-10-20-anisotropic-constructions/parity_structure_direct_sum.py

## Correction of an additional-scalar candidate

During construction, the root and this worker considered adjoining a
scalar with both short polynomials equal to 1 and long functional h.
Taken with only the M(2d) core, it is independent. Taken with both the
core and M(d-1), it creates mixed coefficients involving one row from
each of the three proposed blocks. This candidate was not a verified
claim, and it is not part of the construction above.

The executable checks that failure explicitly. All intended coefficients
of the three proposed blocks remain correct, but there are exactly
3(d-1)^2 additional mixed coefficients in the checked cases. At a=5
there are 27, including coefficient one at target rows (0,73,72), with
the tentative scalar at row 73. Orthogonality between the two new sectors
does not remove this term because their connecting edge uses the core
long functional R. No degeneration removing these terms is asserted.

## Why the preceding M9 core could not accept a fixed independent block

The preceding integral M9 construction uses short spaces of dimensions
three and three whose nine products span all of P8. Contracting A(5,5)
with two of those fixed core maps gives an injective linear map on the
entire third source leg. Its three tensor factors have ranks 5,9,5.
The middle factor is the checked invertible product matrix. Each end
factor is injective because it includes multiplication by a nonzero
polynomial, followed by an invertible long-basis change.

A new direct-sum row would have to lie in the kernel of this map, so
it would be zero. This explains the change to a 2-by-4 product basis:
its products have codimension one, and the remaining long functional h
provides the new multiplication block. This is an exact statement about
keeping those specific core maps fixed; it does not exclude another M9
embedding or a larger construction with changing core maps.
