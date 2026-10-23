# Every constant compression of the fixed A4 conjugation family fails

October 23, 2026. Claim `AI-A4-ARBITRARY-COMPRESSION-001`.
Written proof with exact finite acceptance; unreviewed. Checks by agents
in the generating session are not independent mathematical review.

## 1. Statement and scope

Use the literal outer source and normalization from the preceding
[low-rank reduction](../2026-10-23-conjugation-limit/LOW_RANK_REDUCTION.md),
claim `AI-A4-TWOSIDED-LOWRANK-003`. In particular,

\[
S(f)_{(j,L),(H,r)}=f_{H-j,L-r},\qquad
K=S\!\left(\sum_{i+s=3}e_{i,s}\right),\qquad G(f)=K^{-1}S(f),
\]

where \(0\le j,r\le3\), \(0\le H,L\le6\), and coefficients outside
\(0\le i,s\le3\) are zero. Put \(G_{i,s}=G(e_{i,s})\),
\(G=\operatorname{span}\{G_{i,s}\}\), \(F=G_{0,0}\), and

\[
\mathcal E=G+[G,F]+FGF\subset\operatorname{Mat}_{28}(\mathbb C).
\]

The 46-element ordered basis consists of the 16 matrices \(G_{i,s}\),
the 14 commutators \(G_{i,s}F-FG_{i,s}\) other than indices \((0,0)\)
and \((0,3)\), and the 16 matrices \(FG_{i,s}F\), in lexicographic
order within each group. Its independence was established in the
preceding reduction and is also checked directly here.

**Theorem.** For every \(U,W\subset\mathbb C^{28}\) with
\(\dim U=26\) and \(\dim W=2\),

\[
\dim\{X\in\mathcal E:X(U)\subset W\}\le8.                 \tag{1}
\]

Equivalently, every rank-26 pair \(P:\mathbb C^{28}\to\mathbb C^{26}\),
\(C:\mathbb C^{26}\to\mathbb C^{28}\) satisfies

\[
\boxed{\dim(P\mathcal EC)\ge38.}                         \tag{2}
\]

The preceding low-rank reduction identifies the compression kernel of
the full 112-dimensional conjugation limit with a subspace of (1).
Therefore every constant rank-110 compression of that limit has
dimension at least 104. The necessary upper bound for a full
\(M(10,10,11)\) target is 103, even after allowing the first map to have
arbitrary Laurent poles. Thus this theorem excludes every constant
compression in that one fixed two-sided conjugation family.

This is not a statement about arbitrary moving long-factor maps,
different conjugations, or all degenerations of the A4 source. It does
not construct a matrix multiplication target or change an exponent.
The numerical bound 38 is not asserted to be sharp.

## 2. A torus limit reduces arbitrary flags to graded flags

Give coordinate \((H,r)\), numbered \(4H+r\), weight \(H-r\). Let
\(V_j\) be the weight-\(j\) subspace and let \(D(t)\) multiply it by
\(t^j\). The weight dimensions for \(j=-3,\ldots,6\) are

\[
(1,2,3,4,4,4,4,3,2,1).                                  \tag{3}
\]

Direct substitution in the source formula gives

\[
\deg G_{i,s}=3-i-s,\quad
\deg [G_{i,s},F]=6-i-s,\quad
\deg FG_{i,s}F=9-i-s.                                    \tag{4}
\]

Here a matrix of degree \(d\) maps \(V_j\) into \(V_{j+d}\).
Consequently \(D(t)\mathcal ED(t)^{-1}=\mathcal E\). The dimensions
of \(\mathcal E_d\), for \(d=-3,\ldots,9\), are

\[
(1,2,3,5,5,5,5,5,5,4,3,2,1).                            \tag{5}
\]

Suppose a pair violates (1). Apply \(D(t)\) simultaneously to both
subspaces. For \(t\ne0\) this preserves the compression-kernel
dimension. Both Grassmannians have limits at \(t=0\): in Pluecker
coordinates, remove the smallest common power of \(t\) and set
\(t=0\). The limits have the same dimensions and are fixed by the
torus, so they split as direct sums of their intersections with the
\(V_j\). The condition that the kernel dimension is at least nine
is closed, because it says that a linear map from the fixed
46-dimensional space \(\mathcal E\) has rank at most 37. In any
Grassmannian chart this is the vanishing of its 38-minors. It therefore
holds at the limiting pair too.

It is enough to prove (1) for graded \(U,W\). Define the loss budgets

\[
a_j=\dim V_j-\dim(U\cap V_j),\qquad b_j=\dim(W\cap V_j).
\]

They are nonnegative integers with \(\sum a_j=\sum b_j=2\), bounded
by (3). There are 53 possible budgets of each kind, hence 2,809 pairs.
This finite enumeration does not restrict the subspaces inside a weight
space to coordinate subspaces. Those subspaces remain arbitrary.

For graded flags the kernel splits into homogeneous pieces \(K_d\).
For each block \(X_{j+d,j}\) of a member of \(K_d\),

\[
\operatorname{rank}X_{j+d,j}\le a_j+b_{j+d}.              \tag{6}
\]

Indeed its restriction to a subspace of codimension \(a_j\) has image
dimension at most \(b_{j+d}\). When the right side is zero, the entire
block vanishes, imposing exact linear equations on \(\mathcal E_d\).

## 3. Linear equations and quadratic minors cover 2,806 pairs

The acceptance program reconstructs all source matrices over the
rationals. For each budget pair and degree, it takes the rational
nullspace of every zero-cap block in (6). Let \(q_d\) be its dimension.
The sum \(\sum q_d\) is at most eight for 2,781 of the 2,809 pairs.

For each of the remaining 28 pairs, use coordinates \(z_0,\ldots,z_{q_d-1}\)
in that nullspace. Every \((a_j+b_{j+d}+1)\)-minor of each remaining
block vanishes on \(K_d\), whenever that minor fits inside the block.
For quadratic minors, remove nonzero rational scalar factors, deduplicate
the resulting polynomials, and take their sum \(Q\). Let \(r\) be the
exact rank of its Hessian. Then

\[
\dim K_d\le q_d-\lceil r/2\rceil.                       \tag{7}
\]

To see this, a quadratic form vanishing on a linear subspace has zero
polar form on that subspace. Modulo the \((q_d-r)\)-dimensional radical,
a totally isotropic subspace for a nondegenerate symmetric form has
dimension at most \(\lfloor r/2\rfloor\). This proves (7) over
\(\mathbb C\). Independently, any nonzero minor polynomial implies
\(\dim K_d\le q_d-1\); a proper linear subspace cannot have full
dimension. Take the better of these bounds.

These exact calculations settle 25 more budget pairs. Only the following
three remain. The table lists their nonzero budgets and the bound before
the extra arguments below.

| Pair | Nonzero input losses | Nonzero output dimensions | Bound |
| --- | --- | --- | ---: |
| A | \(a_{-3}=a_{-2}=1\) | \(b_4=b_5=1\) | 9 |
| B | \(a_{-2}=a_{-1}=1\) | \(b_4=b_5=1\) | 12 |
| C | \(a_{-2}=a_{-1}=1\) | \(b_5=b_6=1\) | 9 |

All enumerated linear constraints, polynomial minors, Hessian ranks and
coverage counts are checked in exact rational arithmetic. No modular
rank upper bound, sampled flag, numerical tolerance, or Groebner-basis
dimension calculation is used for acceptance.

## 4. Three small homogeneous minor arguments

The following coefficient relations are checked as exact rational linear
combinations of the block minors. Their coefficients are retained in the
certificate, so acceptance does not need to rediscover them.

### Degree five with block caps \((1,2,1)\)

In the ordered degree-five basis

\[
([G_{01},F],[G_{10},F],FG_{13}F,FG_{22}F,FG_{31}F),
\]

six necessary quadratic equations are

\[
\begin{aligned}
&z_2(z_2-2z_3+z_4)=0,\\
&z_2(z_1+3z_2-3z_3+z_4)=0,\\
&z_2(z_0-2z_1-3z_2+z_3)=0,\\
&z_4(z_2-2z_3+z_4)=0,\\
&z_4(z_0+z_3-2z_4)=0,\\
&z_4(z_0-z_1-z_4)=0.                                    \tag{8}
\end{aligned}
\]

Consider any linear subspace on which these equations and the necessary
cubic middle-block determinant vanish. If \(z_2\) is not identically
zero on that subspace, the first three equations force

\[
z_2=2z_3-z_4,\quad z_1=-3z_3+2z_4,\quad z_0=-z_3+z_4.
\]

The fifth equation then forces \(z_4=0\), leaving at most one dimension.
This uses that a product of polynomial functions on a vector space is
zero only if one factor is identically zero. If \(z_2=0\) identically
but \(z_4\) is not, (8) instead forces
\((z_0,z_1,z_2,z_3,z_4)=(3,1,0,1,2)z_3\).

If both \(z_2,z_4\) vanish identically, the middle determinant becomes

\[
z_3(z_0z_1-z_0z_3+z_1z_3+3z_3^2).                       \tag{9}
\]

This is a nonzero polynomial on the remaining three-dimensional space.
Hence the linear subspace has dimension at most two. We have proved
\(\dim K_5\le2\) for caps \((1,2,1)\).

### Degree five with block caps \((1,1,1)\)

The same six equations (8) hold. The additional 2-minors imply

\[
z_2^2-4z_3^2+z_4^2=0,\qquad z_0z_1-3z_3^2=0.             \tag{10}
\]

The cases where \(z_2\) or \(z_4\) is nonzero already have dimension
at most one. When both vanish, (10) forces \(z_3=0\) and \(z_0z_1=0\).
One of the last two coordinate functions then vanishes identically.
Thus \(\dim K_5\le1\). This improves the bound by one for each of
pairs A and C, giving total kernel dimension at most eight.

### Degree four with four block caps equal to one

The ordered basis is

\[
([G_{02},F],[G_{11},F],[G_{20},F],FG_{23}F,FG_{32}F).
\]

The necessary 2-minors imply the following ten quadratic relations:

\[
\begin{aligned}
&z_0^2-z_0z_2+z_1z_2-z_3^2-3z_4^2=0,\\
&z_0z_1-z_0z_2+z_2^2-3z_3^2-z_4^2=0,\\
&-z_0z_2+z_1^2-z_1z_2+z_2^2-z_3^2+z_4^2=0,\\
&z_0z_3+z_3^2=z_1z_3+z_3^2=z_2z_3+2z_3^2=0,\\
&z_0z_4-2z_4^2=z_1z_4-z_4^2=z_2z_4-z_4^2=z_3z_4=0.
                                                                  \tag{11}
\end{aligned}
\]

On a linear subspace satisfying (11), if \(z_4\) is not identically
zero, all coordinates are determined by \(z_4\): they are proportional
to \((2,1,1,0,1)\). If \(z_4=0\) identically but \(z_3\) is not,
they are proportional to \((-1,-1,-2,1,0)\).

It remains to set \(z_3=z_4=0\). If \(z_2=0\) identically, the first
and third equations force \(z_0=z_1=0\). Otherwise the first equation
gives \(z_1z_2=z_0z_2-z_0^2\), and the second yields

\[
(z_0-z_2)(z_0^2+z_2^2)=0.
\]

Over \(\mathbb C\) one of \(z_0-z_2,z_0-\mathrm i z_2,
z_0+\mathrm i z_2\) vanishes identically. Substitution in the first
equation determines \(z_1\) as a multiple of \(z_2\). The dimension
is again at most one. Therefore \(\dim K_4\le1\).

## 5. Shared flags settle the last budget

For pair B, all homogeneous kernel pieces outside degrees four through
eight are zero. Section 4 gives \(\dim K_4\le1\) and
\(\dim K_5\le2\). It remains to prove

\[
\dim K_6+\dim K_7+\dim K_8\le5.                         \tag{12}
\]

Use the increasing original coordinate order within each weight space.
Write

\[
A=U\cap V_{-2}=\langle(a,b)\rangle,\quad
B=U\cap V_{-1},\quad L=W\cap V_4,\quad M=W\cap V_5.
\]

Here \(A,M\) are lines in \(\mathbb C^2\), \(B\) is a plane in
\(\mathbb C^3\), and \(L\) is a line in \(\mathbb C^3\). Put
\(\delta=a-b\), \(u=(1,-2)^T\), and write \(k_d=\dim K_d\).

The only degree-eight matrices are \(FG_{01}F,FG_{10}F\). Their two
nonzero blocks are \(z_0e_2:V_{-3}\to V_5\) and
\(z_1e_2^*:V_{-2}\to V_6\). Thus

\[
k_8={\bf1}_{M=\langle e_2\rangle}
       +{\bf1}_{A=\langle e_1\rangle}.                  \tag{13}
\]

In degree seven, the boundary blocks impose
\(z_0e_3\in L\) and \(z_2e_3^*|_B=0\). The middle block on \((a,b)\)
is

\[
\delta(-z_0+2z_1-z_2)u+bz_1e_2\in M.                  \tag{14}
\]

Always \(k_7\le3\). If \(k_8=2\), then \(A=\langle e_1\rangle\)
and \(M=\langle e_2\rangle\), so (14) imposes the nonzero equation
\(-z_0+2z_1-z_2=0\). Consequently

\[
k_7+k_8\le4.                                           \tag{15}
\]

In degree six, the two outer blocks force the coefficients of
\(FG_{03}F\) and \(FG_{30}F\) to vanish. Write the remaining
coefficients of \(FG_{12}F,FG_{21}F\) as \(x,y\). The block
\(V_{-2}\to V_4\) applied to \((a,b)\) is

\[
x(-\delta,3\delta,-3\delta+b)^T
+y(2\delta,-3\delta,0)^T.                               \tag{16}
\]

If \(k_6=2\), both coefficient vectors must lie in the line \(L\).
Their first-two-coordinate determinant is \(-3\delta^2\), forcing
\(\delta=0\). Since \((a,b)\ne0\), this gives
\(A=\langle(1,1)\rangle\) and \(L=\langle e_3\rangle\).

The other remaining block, \(V_{-1}\to V_5\), is

\[
u(xr+ys)+ye_2e_3^*,\qquad
r=(2,-1,-1),\quad s=(-1,2,-1).                           \tag{17}
\]

If \(M\ne\langle u\rangle\), the coefficient of \(x\) forces
\(B=\ker r\). But \(\det(r,s,e_3^*)=3\), so \(s,e_3^*\) restrict
to independent functionals on \(B\). Since \(u,e_2\) are independent,
the coefficient of \(y\) then has rank two on \(B\), a contradiction.
Therefore \(M=\langle u\rangle\), and (17) forces \(B=\ker e_3^*\).

At this unique flag tuple, (13) gives \(k_8=0\), and (14) gives
\(z_1=0\), with no boundary restrictions. Hence \(k_7=2\) and the
total in (12) is four. For every other tuple, \(k_6\le1\), and (15)
proves (12). Adding the degree-four and degree-five bounds gives eight.
Together with Sections 2--4 this proves (1) for every complex pair.

## 6. Acceptance and contribution boundaries

The finite acceptance reconstructs the literal \(S_{i,s}\), inverts
the exact unit \(K\), forms all 46 matrices, checks their independence
and grading, and covers all 2,809 grade-budget pairs. It accepts the
extra polynomial identities by exact linear-combination certificates
and reconstructs the degree-six through degree-eight blocks used in
(13)--(17). The analytic arguments turning those identities into a
universal statement are the written proof above.

This package supplies the new compression inequality (1). It imports
the full conjugation-limit construction, low-rank support reduction,
and scalar-action target obstruction with their prior attribution.
Those proofs and their retained certificates remain unchanged.
The theorem is written and unreviewed, not formalized. Passing its
acceptance program or repository tests does not supply independent
mathematical review.
