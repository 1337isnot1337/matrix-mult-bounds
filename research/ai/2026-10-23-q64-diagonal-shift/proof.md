# A diagonal-shift restriction requires a quadratic correction

October 23, 2026. Written, unreviewed, owner-directed Codex research.

This note studies one explicit restriction of the maintained paired source
\(Q(n,4)\). It proves that the correction needed to reach
\(M(n,4,n)\) has border rank at least \(n^2\). This excludes the chosen
maps from the linear-cost correction route. It does not exclude other maps.

## Tensors and maps

Use the maintained source convention

\[
Q(n,4)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{3}
 A_{p,q}B_{y,q+v}C_{p+y,v}
\]

and target

\[
M(n,4,n)=\sum_{i,h=0}^{n-1}\sum_{j=0}^{3}
 a_{i,h}b_{i,j}c_{j,h}.
\]

Consider these linear maps from the three source legs to the target legs:

\[
\begin{aligned}
A_{p,q}&\longmapsto
  \sum_{\substack{0\le t<4\\p+t<n\\q+t<n}}a_{q+t,p+t},\\
B_{y,s}&\longmapsto
  \begin{cases}b_{s,y}&s<n,\\0&s\ge n,\end{cases}\\
C_{z,v}&\longmapsto
  \begin{cases}c_{v,z}&z<n,\\0&z\ge n.\end{cases}
\end{aligned}
\tag{1}
\]

Let \(S_n\) be the image of \(Q(n,4)\) under (1), and set
\(D_n=M(n,4,n)-S_n\). In a direct-sum construction using these fixed
maps on the \(Q(n,4)\) summand, the auxiliary summand must restrict to
\(D_n\).

## A projection of the first-leg flattening

Write an arbitrary first-leg coefficient vector as \(x=(x_{i,h})\).
The coefficient of \(b_{s,0}c_{0,z}\) in \(D_n(x)\) is

\[
x_{s,z}-\sum_{\substack{0\le t<4\\s+t,z+t<n}}x_{s+t,z+t}
=-\sum_{\substack{1\le t<4\\s+t,z+t<n}}x_{s+t,z+t}.
\tag{2}
\]

For \(b_{s,1}c_{1,z}\), the coefficient is \(x_{s,z}\) if
\(s=0\) or \(z=0\). If \(s,z\ge1\), it is

\[
x_{s,z}-\sum_{\substack{0\le t<4\\s-1+t,z-1+t<n}}
x_{s-1+t,z-1+t}
=-\sum_{\substack{t\in\{0,2,3\}\\s-1+t,z-1+t<n}}
x_{s-1+t,z-1+t}.
\tag{3}
\]

Project \(D_n(x)\) to the \(n^2\) coordinates indexed by \((s,z)\)
that sum the coefficients of \(b_{s,0}c_{0,z}\) and
\(b_{s,1}c_{1,z}\). Every term in (2) and (3) shifts both outer
indices equally, so this projected map preserves each diagonal
\(s-z=\delta\).

For \(\delta\in\{-(n-1),\ldots,n-1\}\), that diagonal has length
\(L=n-|\delta|\). Number its positions from \(k=0\) at the endpoint
whose smaller coordinate is zero. The block matrix \(T_L\) of the
projected map has the following rows, omitting columns outside
\(0,\ldots,L-1\):

\[
\begin{array}{ll}
k=0:& x_0-x_1-x_2-x_3,\\[2mm]
k\ge1:&-x_{k-1}-2x_{k+1}-2x_{k+2}-x_{k+3}.
\end{array}
\tag{4}
\]

Thus the projected first-leg flattening is a direct sum of the blocks
\(T_L\), one for each diagonal.

## Each diagonal block is nonsingular

Reduce (4) modulo two. The first row becomes
\(x_0+x_1+x_2+x_3\), with out-of-range terms omitted. Each later row
becomes

\[
x_{k-1}+x_{k+3},
\tag{5}
\]

again omitting out-of-range terms.

For \(L\ge4\), the last three rows force
\(x_{L-4}=x_{L-3}=x_{L-2}=0\). The rows with
\(1\le k\le L-4\) give \(x_{k-1}=x_{k+3}\). Hence each residue
class modulo four is constant along its positions, and three consecutive
zero coordinates kill three residue classes. The first row contains
exactly one position in the remaining class, so it kills that class too.
For \(L=1,2,3\), the first row together with the truncated rows in (5)
directly forces every coordinate to zero. Therefore every \(T_L\) is
nonsingular over \(\mathbb F_2\), and its integer determinant is odd.
It is consequently nonsingular over \(\mathbb C\).

The projected first-leg flattening has rank
\[
\sum_{\delta=-(n-1)}^{n-1}(n-|\delta|)=n^2.
\]
Since projection cannot increase rank, the first-leg flattening of
\(D_n\) has rank at least \(n^2\). Its first leg has dimension \(n^2\),
so the rank is exactly \(n^2\).

Tensor rank and border rank dominate every flattening rank. Also,
restriction cannot increase border rank. Therefore any auxiliary tensor
that restricts to \(D_n\) has border rank at least \(n^2\). The fixed
maps (1) cannot be completed with an \(O(n)\)-border-rank correction.

## Verification and limits

The standard-library verifier reconstructs the literal source and target
coefficients, forms the correction, projects the two blocks above, and
checks the diagonal-block formula and full rank modulo two for sizes
\(n=1,\ldots,12\). The all-size result is the proof above; the finite
replay is a control of its indexing, not its asymptotic argument.

The result covers only maps (1). It does not address arbitrary
restrictions of \(Q(n,4)\), other auxiliary decompositions, or any
general lower bound for the paired-source route. It establishes no
matrix-multiplication exponent improvement. No independent mathematical
review or Lean formalization is claimed.
