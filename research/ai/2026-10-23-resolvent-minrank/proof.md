# Sharp minimum rank for the singular-resolvent limit space

October 23, 2026. Written and unreviewed. No smaller exponent is established.

Claim `AI-RESOLVENT-SHARP-MINRANK-001` concerns the fixed matrix space introduced in
[PR103](https://github.com/1337isnot1337/matrix-mult-bounds/pull/103).
The source convention, source unit, nilpotent, and initial limiting space retain
their predecessor credits. The immutable source records are in `sources.json`.

The new result is

\[
\dim W=112,\qquad \min_{X\in W\setminus\{0\}}\operatorname{rank}X=6.
\]

This is ordinary matrix rank. It is not tensor slice rank.
The finite integer certificate works over every field. The Laurent application
in Section 5 uses the complex field.

## 1. Exact source formulas

Let the indices \(i,j,p,q,r,s\) range from 0 through 3.
Let \(H,L,k\) range from 0 through 6.
The original source slice has rows \((j,p,L)\), columns \((H,q,r)\), and entries

\[
M(F)_{(j,p,L),(H,q,r)}=F_{H-j,p+q,L-r}.
\]

Coefficients outside the two short index ranges are zero.
The source unit is \(F_*[i,k,s]=1\) exactly when \(i+s=3\) and \(k=3\).
This is the convention in the maintained cyclic-source proof.

Define an outer matrix with rows \((j,L)\) and columns \((H,r)\):

\[
S(f)_{(j,L),(H,r)}=f_{H-j,L-r},\qquad 0\le i,s\le3.
\]

The row and column orders are lexicographic. Both matrix dimensions are 28.
Set \(f_*[i,s]=1\) exactly when \(i+s=3\), and define

\[
K=S(f_*),\qquad G(f)=K^{-1}S(f),\qquad G_{00}=G(e_{00}),
\qquad Q(f)=G_{00}G(f).
\]

The maintained source-unit proof gives an integer inverse of \(K\).
The new verifier reconstructs that inverse and verifies both identities over
the integers. A modular calculation proposes the inverse. Exact integer
multiplication is the acceptance condition.

After the middle coordinate comes first, normalized source slices have the form

\[
H(F)=\sum_{k=0}^6J_k\otimes G(f_k),\qquad
(J_k)_{q',q}=\mathbf1_{q'=q+3-k}.
\]

Here \(f_k[i,s]=F[i,k,s]\), and unavailable matrix indices give zero entries.
The verifier compares this factorization with all 112 literal source
coefficient matrices. It uses the original coordinate orders in that comparison.

In particular,

\[
N=H(e_{000})=E_{3,0}\otimes G_{00},\qquad N^2=0,
\qquad\operatorname{rank}N=16.
\]

## 2. The mixed outer block has sharp minimum rank six

Consider

\[
\mathcal X=\{G(g)+Q(f):f,g\in\mathbb F^{16}\}.
\]

Left multiplication by \(K\) gives the equivalent space

\[
K\mathcal X=\{S(g)+S(e_{00})G(f):f,g\in\mathbb F^{16}\}.
\]

The relation \(Q(f_*)=G_{00}\) removes one parameter.
Replace \(f\) by \(f-f_{03}f_*\) and \(g\) by \(g+f_{03}e_{00}\).
The represented matrix is unchanged, and the new coefficient \(f_{03}\) is zero.
The resulting 31 generators use all 16 coefficients of \(g\), followed by the
15 retained coefficients of \(f\), in lexicographic order.

The certificate gives 31 successive restrictions of this parameter space.
Each step specifies a linear form \(\ell\) and six distinct rows and columns.
The indicated submatrix is lower triangular. Each diagonal entry is
\(\ell\) or \(-\ell\). Its determinant is therefore \(\ell^6\) or \(-\ell^6\).
These are polynomial identities in all current parameters.

Suppose the represented matrix has rank at most five.
The first indicated determinant vanishes, so its linear form is zero.
A coefficient of that form is 1 or \(-1\).
It permits an integer substitution that removes one parameter.
The next certificate applies to the resulting matrix space.
After 31 such steps, no parameters remain.

Thus a matrix in this space has rank at most five only when it is zero.
The same argument proves independence of the 31 generators.
A nontrivial relation represents zero with nonzero parameters, which contradicts
their successive elimination.

The verifier reconstructs every coefficient matrix from the source formula.
It verifies every entry above each indicated diagonal, each diagonal form,
each unit substitution, and exhaustion of all parameters.
The discovery search and finite-field samples are not acceptance premises.

The matrix \(S(e_{00})G(e_{00})\) is nonzero. Its only nonzero rows are
0, 7, 14, 21, 22, and 23, with zero-based indexing.
Its rank is at most six. The proved lower bound gives rank exactly six.
Consequently

\[
\dim\mathcal X=31,\qquad \operatorname{minrank}\mathcal X=6.
\]

All diagonal factors and elimination pivots are units over the integers.
The argument therefore holds over every field, including characteristics two
and three.

## 3. The full limit space

The uncompressed space of PR103 is

\[
W=\operatorname{span}\bigl(
\{NH(F):f_k=0\text{ for }k<3\},
\{H(G):g_k=0\text{ for }k\ge3\},I_{112}\bigr).
\]

The matrices \(J_0,J_1,J_2\) shift the middle coordinate upward by 3, 2, and 1.
The product \(J_0J_k\) equals \(E_{3,k-3}\) for \(k\ge3\).
Thus the four-by-four outer block form has these parameters:

| Part | Parameters |
| --- | ---: |
| Scalar identity | 1 |
| \(J_2\otimes G(g_2)\) | 16 |
| \(J_1\otimes G(g_1)\) | 16 |
| Block \((3,0)\), equal to \(G(g_0)+Q(f_3)\) | 31 |
| Blocks \((3,1),(3,2),(3,3)\), equal to \(Q(f_4),Q(f_5),Q(f_6)\) | 48 |

The outer source space has dimension 16 and minimum nonzero rank 16.
The maintained triangular-minor proof gives this fact. The new verifier also
replays its 16 possible leading-coefficient cases directly.

The mixed-block theorem implies that \(Q\) is injective.
Indeed, its gauge relation translates \(Q(f)=0\) into a relation between the
31 independent mixed generators. All gauge coefficients vanish, forcing \(f=0\).

The indicated parts are independent. Blocks \((0,0),(1,0),(2,0)\) first recover
the scalar, \(g_2\), and \(g_1\). The remaining distinct blocks recover the other
parameters. Hence \(\dim W=1+16+16+31+48=112\).

A nonzero scalar gives a rank-28 block at \((0,0)\).
If the scalar vanishes, a nonzero \(g_2\) or \(g_1\) gives a block of rank at
least 16. Otherwise, only the final outer block row remains.
Every nonzero block in that row has rank at least six by Section 2.

Thus every nonzero matrix in \(W\) has rank at least six.
The matrix with only block \((3,1)=Q(e_{00})\) attains rank six.
This proves the stated sharp minimum.

## 4. Compression and equality constraints

Let \(P\) have size \(110\times112\), and let \(C\) have size
\(112\times110\). Both matrices in this section are constant.
The elementary restriction bound is

\[
\operatorname{rank}(PXC)\ge\operatorname{rank}X
-(112-\operatorname{rank}P)-(112-\operatorname{rank}C).
\]

If both maps have rank 110, the total loss is at most four.
Therefore the compression \(W\to PWC\) is injective.
In particular \(\dim PWC=112\) for every pair with \(PC=I_{110}\).
This removes the generic rank hypothesis of PR103.

More generally, a total rank loss of at most five still gives injectivity.
This includes a pair with ranks 110 and 109 in either order.

Suppose instead that both maps have rank 109 and \(PXC=0\) for a nonzero
\(X\in W\). The total rank loss is at most six.
Section 3 forces \(\operatorname{rank}X=6\).
Write \(U=\operatorname{im}C\) and \(L=\ker P\).
Their dimensions are 109 and three.

The restriction of \(X\) to \(U\) has rank at least three.
Its image lies in \(L\), so its rank is exactly three.
Its kernel has dimension 106, which equals \(\dim\ker X\).
Consequently

\[
\ker X\subset U,\qquad X(U)=L,\qquad U=X^{-1}(L).
\]

Section 3 also shows that every rank-six matrix in \(W\) has only its final
outer block row nonzero. Let \(J_3\) denote that 28-dimensional output layer.
Then \(\operatorname{im}X\subset J_3\), so \(L\subset J_3\).
Thus a nontrivial compression kernel requires this specific alignment.
The statement concerns these compression factors. It does not classify
arbitrary tensor degenerations with two singular long-map limits.

## 5. Relation to the fixed resolvent

PR103 studies \(B(t)=P(tI+N)^{-1}\) with constant \(P,C\) and \(PC=I_{110}\).
Its argument requires \(\dim PWC=112\). Section 4 supplies that condition for
every such pair.

The same limiting-space argument permits regular \(P(t),C(t)\) with an
invertible leading product. A constant normalization makes \(P(0)C(0)=I_{110}\).
After a scalar moves into the unrestricted first map, the relevant curves are

\[
A_t(f)=P(t)(N-tI)H(f)C(t).
\]

High-middle source coefficients give limits \(P_0NH(f)C_0\).
For low-middle coefficients, \(NH(g)=0\), so \(-A_t(g)/t\) gives
\(P_0H(g)C_0\). The source vector \(e_{000}+tF_*\) gives
\(-t^2P(t)C(t)\), and division by \(-t^2\) gives the identity limit.

These curves have 112 independent constant matrices by Section 4.
They form a basis of the entire Laurent span, whose dimension is at most 112.
A regular curve cannot have a pole in its coefficients relative to this basis.
A leading pole produces a nontrivial relation among the independent constants.
Thus its limit belongs to \(P_0WC_0\).

The invariant-subspace argument of PR103 then excludes its specified matrix
target. This is a narrow consequence for the fixed resolvent.
The concurrent regular-long-leg theorem gives a broader target exclusion.
The sharp minimum-rank theorem here remains a separate structural result.

No arbitrary singular degeneration, improved exponent, independent mathematical
review, or formalization is claimed. The rank and dimension arguments in prose
remain written proofs. The integer coefficient identities have a reproducible
finite verifier.
