# An exact integer restriction Q(5,4) to M(4,4,4)

## Result and scope

There is an ordinary restriction over the integers

\[
Q_{5,4}\ge M(4,4,4).
\]

The supplied maps have entries in \(\{0,1,-1\}\). They apply to all 400
source terms, and the complete 16 by 16 by 16 coefficient tensor equals
the standard matrix multiplication tensor. The certificate checks its 64
nonzero coefficients and all 4,032 off-support coefficients. It remains
valid over every field.

More generally, the same construction proves

\[
Q_{k+1,k}\ge M(k,4,k)\qquad(k\ge2).
\]

This is a useful exact construction and numerical-search calibration.
It is **not an improvement of the matrix multiplication exponent**, and
no novelty claim is made. Its product-subspace mechanism has an explicit
dimension limitation stated below.

The construction was recovered during the same session from the rowspace
structure of a numerical Q(5,4) solution. The exact certificate does not
use that numerical solution. The proof and coefficient checks are
reproducible here; no external mathematical review is claimed.

## Conventions

The source is

\[
Q_{n,m}=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

For \(n=k+1,m=k\), its format is
\(((k+1)^2,2k^2,2k^2)\). The target is

\[
M(k,4,k)=\sum_{i,h=0}^{k-1}\sum_{j=0}^3
a_{i,h}b_{i,j}c_{j,h},
\]

of format \((k^2,4k,4k)\). Thus the B and C variables have the usual
row-by-column multiplication convention, and the A variables index its
output coefficients.

## Two injective convolution restrictions

Let \(P_d\) denote polynomials of degree at most \(d\). Take

\[
U=\langle t,t^2,\ldots,t^{k-1},1-t^k\rangle\subset P_k,
\qquad W=\langle1,t^{k-1}\rangle\subset P_{k-1}.
\]

Write their ordered bases as \(U_i\), \(0\le i<k\), and
\(W_v\), \(0\le v<2\). The multiplication map

\[
U\otimes W\longrightarrow P_{2k-1}
\]

is a unimodular isomorphism. Its products are the monomials of degrees
1 through \(2k-2\), together with \(1-t^k\) and
\(t^{k-1}-t^{2k-1}\). The two monomials \(t^k\) and
\(t^{k-1}\) already occur among the first products. Adding or subtracting
them recovers the missing monomials 1 and \(t^{2k-1}\), using only integer
operations. This proves the assertion over the integers.

Let \(D_{2i+v,s}=[t^s]U_i(t)W_v(t)\), and let
\(L=(D^T)^{-1}\). In particular,

\[
\sum_s D_{2i+v,s}L_{2i'+v',s}=\delta_{i,i'}\delta_{v,v'}.
\tag{1}
\]

For \(k=4\), the ordered products are

\[
t,\ t^4,\ t^2,\ t^5,\ t^3,\ t^6,\ 1-t^4,\ t^3-t^7.
\]

The exact dual is

\[
L=\begin{pmatrix}
0&1&0&0&0&0&0&0\\
1&0&0&0&1&0&0&0\\
0&0&1&0&0&0&0&0\\
0&0&0&0&0&1&0&0\\
0&0&0&1&0&0&0&1\\
0&0&0&0&0&0&1&0\\
1&0&0&0&0&0&0&0\\
0&0&0&0&0&0&0&-1
\end{pmatrix}.
\]

The JSON certificate also stores both D and L, and checks both
\(LD^T=I\) and \(D^TL=I\).

## The three sidewise maps

Denote polynomial coefficients by \(U_i(p)=[t^p]U_i\) and
\(W_v(y)=[t^y]W_v\). Use the following maps:

\[
A_{p,q}\longmapsto
\sum_{i,h=0}^{k-1}U_h(p)U_i(q)a_{i,h},
\tag{2}
\]

\[
B_{y_0,s}\longmapsto
\sum_{i=0}^{k-1}\sum_{y,v=0}^1
W_y(y_0)L_{2i+v,s}\,b_{i,2y+v},
\tag{3}
\]

\[
C_{z,v_0}\longmapsto
\sum_{h=0}^{k-1}\sum_{y,v=0}^1
L_{2h+y,z}W_v(v_0)\,c_{2y+v,h}.
\tag{4}
\]

These are ordinary local linear maps on the three source spaces. They
contain no parameter, pole, limit, or coefficient depending on another
tensor leg.

Substitution in the source separates its two convolution sums. For the
coefficient of \(a_{i,h}b_{i',2y'+v'}c_{2y+v,h'}\), the first sum is

\[
\sum_{p,y_0}U_h(p)W_{y'}(y_0)L_{2h'+y,p+y_0}
=\delta_{h,h'}\delta_{y',y},
\]

and the second is

\[
\sum_{q,v_0}U_i(q)W_v(v_0)L_{2i'+v',q+v_0}
=\delta_{i,i'}\delta_{v,v'}.
\]

Both equalities are (1). Therefore the result is exactly

\[
\sum_{i,h<k}\sum_{y,v<2}
a_{i,h}b_{i,2y+v}c_{2y+v,h}=M(k,4,k).
\]

## Why the numerical point admitted this recovery

At the numerical Q(5,4) point, the A-map rowspace factors as
\(U_4\otimes V_4\subset\mathbb C^5\otimes\mathbb C^5\).
The C-map rowspace factors as
\(\mathbb C^8\otimes W_2\subset\mathbb C^8\otimes\mathbb C^4\).
After changing the second convolution output basis by the invertible
product map \(V_4\otimes W_2\to P_7\), the B-map rowspace factors as
\(V_4\otimes H_4\), with
\(H_4\subset P_3\otimes W_2\). The remaining product map
\(U_4\otimes H_4\to P_7\otimes W_2\) is invertible at that point.
These are numerical diagnostics of that point, not premises of the proof.

Selecting the simpler rational choice \(H=W\otimes W\) gives the
two-injection certificate above. Its coefficients are proved exactly.

## General template and its limitation

More generally, choose k-dimensional subspaces of each n-dimensional
outer polynomial factor and a- and b-dimensional subspaces of the two
m-dimensional inner factors. If both multiplication maps are injective,
their left inverses give a restriction

\[
Q_{n,m}\ge M(k,ab,k).
\]

The two necessary dimension inequalities for this template are

\[
ka\le n+m-1,\qquad kb\le n+m-1.
\]

For the balanced two-by-two split producing inner dimension four,
\(k\le\lfloor(n+m-1)/2\rfloor\). At fixed source inner dimension four,
this gives only \(k\le\lfloor(n+3)/2\rfloor\). In particular, the
Q(5,4) construction does not imply Q(n+1,4) to M(n,4,n) for n greater
than four. This limitation applies to the stated product-subspace
mechanism; it does not exclude more general restrictions.

## Exact checks and replay

For k=4 the maps contain 25, 20, and 20 nonzero integer entries.
Of the 400 source terms, 300 map to zero. The remaining terms expand
to 144 signed contributions. There are 36 off-support positions at
which contributions cancel, and the final tensor has exactly the
64 prescribed unit coefficients.

`q54-exact.json` contains the complete dense maps, D, L, dimensions,
flattening conventions, and coefficient counts. The tests independently
contract those saved maps, check every one of the 4,096 tensor
coefficients, check the standard product on all 256 pairs of matrix-unit
inputs, and check the integer family at k=2 through 8.

```bash
python research/ai/2026-10-20-paired-construction/outer_product_injection.py
python -m unittest discover -s tests -p test_outer_product_injection.py -v
```

The complete coefficient identity establishes this restriction. It does
not establish a smaller value of omega or uniqueness of the construction.
