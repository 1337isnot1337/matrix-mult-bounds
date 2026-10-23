# Exact ordinary rank of the full one-dependency residual

October 23, 2026. Owner-directed Codex continuation. This is a written,
unreviewed proof, with separate checks inside the same generating session.
The finite certificates check its explicit inputs. They do not constitute
independent mathematical review or formalization.

## Result and scope

Fix a field \(k\), an integer \(b\ge2\), and

\[
n=b+2,\qquad r=n-1=b+1,\qquad s=b-1=r-2.
\]

Let \(E_{n,b}\) be the actual residual of the integer product-oblique maps
in the [preceding construction](../2026-10-23-oblique-paired-repair/proof.md):

\[
Q(n,b)\longrightarrow M(r,4,r)-E_{n,b}.
\]

Then, over every field,

\[
\boxed{R(E_{b+2,b})=4r-1=4b+3.}                 \tag{1}
\]

In particular, the full residual of concise format \(9\times11\times11\)
at \((n,b)=(6,4)\) has ordinary tensor rank exactly nineteen. This
proves optimality of the nineteen scalar corrections for these fixed
source maps. It does not optimize over other maps on \(Q(6,4)\).

The [existing polynomial construction](proof.md) supplies a formal
border repair with \(4r-2\) terms. Together with concision, it gives

\[
2r+1\le\underline R(E_{b+2,b})\le4r-2
\quad\text{over }\mathbb C.                    \tag{2}
\]

The same flattening lower bound and explicit formal degeneration hold
over every field. At \(b=4\), the interval is eleven through eighteen.
This note does not determine the optimal border rank. No smaller
matrix multiplication exponent follows.

## 1. The core and the two groups of outer terms

Use the target bases \(a_{ij},b_{ih},c_{hj}\), where

\[
M(r,4,r)=\sum_{i,j=0}^{r-1}\sum_{h=0}^3a_{ij}b_{ih}c_{hj}.
\]

Write \(J=\{0,\ldots,r-1\}\setminus\{0,s\}\), so \(|J|=r-2\).
The prior residual formula has one bad outer mode, namely \(s\).
Define

\[
\begin{array}{lll}
u=a_{s0},&v=a_{0s},&w=a_{ss},\\
X=b_{s0}-b_{01},&Z=b_{s2}-b_{03},&a=b_{00},\\
\eta=b_{01},&y=b_{s1},&\\
P=c_{00},&Q=c_{20},&R=c_{0s}-c_{20},\\
S=c_{1s}-c_{30},&T=c_{2s}.&
\end{array}                                                       \tag{3}
\]

The full residual is exactly

\[
E_{b+2,b}=K+H+V,                                  \tag{4}
\]

where

\[
\begin{split}
K={}&u(XP+ZQ)+v(aR+\eta S)
       +w(XQ+ZT+\eta R+yS+XR),\\
H={}&\sum_{j\in J}a_{sj}(Xc_{0j}+Zc_{2j}),\\
V={}&\sum_{i\in J}a_{is}(b_{i0}R+b_{i1}S).
\end{split}                                                       \tag{5}
\]

To check (4), specialize the prior three-term formula to its single
bad mode:

\[
\begin{split}
E_{b+2,b}={}&\sum_{j=0}^{r-1}a_{sj}(Xc_{0j}+Zc_{2j})\\
 &+\sum_{i=0}^{r-1}a_{is}(b_{i0}R+b_{i1}S)-wXR.
\end{split}                                                       \tag{6}
\]

The \(j=0\) and \(i=0\) terms give the \(u\) and \(v\) parts of
\(K\). At the common corner, substitute \(c_{0s}=Q+R\) and
\(b_{s0}=X+\eta\). The result is the displayed \(w\) part of
\(K\). All other terms give \(H+V\).

The core \(K\) has ordinary rank seven over every field by the
separate [core proof](ordinary_rank.md). The seven explicit products
there and the \(4(r-2)\) displayed products in \(H+V\) give

\[
R(E_{b+2,b})\le7+4(r-2)=4r-1.                    \tag{7}
\]

### The support splittings hold in every characteristic

The first support has the direct sum

\[
A_K=\langle u,v,w\rangle,\quad
A_H=\langle a_{sj}:j\in J\rangle,\quad
A_V=\langle a_{is}:i\in J\rangle.
\]

These are disjoint sets of the original first coordinates. On the
second and third legs set

\[
\begin{array}{ll}
B_K=\langle X,Z,a,\eta,y\rangle,&
B_V=\langle b_{i0},b_{i1}:i\in J\rangle,\\
C_K=\langle P,Q,R,S,T\rangle,&
C_H=\langle c_{0j},c_{2j}:j\in J\rangle.
\end{array}                                                       \tag{8}
\]

The second support is \(B_K\oplus B_V\), and the third is
\(C_K\oplus C_H\). Independence is visible from the original indices:
the core uses second-leg outer indices \(0,s\), and third-leg outer
indices \(0,s\). Every outer term in the relevant complementary
support uses an index in \(J\). Within the core, the five vectors on
each long leg are independent. For example, the selected coordinates

\[
(b_{s0},b_{s2},b_{00},b_{01},b_{s1})\quad\text{and}\quad
(c_{00},c_{20},c_{0s},c_{1s},c_{2s})
\]

give embedding minors of determinant one, in the orders of (8).
Appending the outer coordinate vectors preserves determinant one.
These arguments also apply in characteristic two.

The tensor \(H\) has full third support \(C_H\), of dimension
\(2(r-2)\): its corresponding contractions are the independent vectors
\(a_{sj}\otimes X\) and \(a_{sj}\otimes Z\). Similarly, \(V\) has
full second support \(B_V\), of dimension \(2(r-2)\), with independent
contractions \(a_{is}\otimes R\) and \(a_{is}\otimes S\).

The same adapted bases make \(E\) concise in format
\((2r-1)\times(2r+1)\times(2r+1)\). The core is concise in its
\(3\times5\times5\) format. The outer coordinates add independent
flattening rows, as their new first and long coordinates show directly.

## 2. A two-leg projection lemma

Let \(A=A_0\oplus A_1\) and \(C=C_0\oplus C_1\). Suppose

\[
T=T_0+T_1,\qquad
T_0\in A_0\otimes B\otimes C_0,\qquad
T_1\in A_1\otimes B\otimes C_1,
\]

and \(T_1\) has full third support \(C_1\), of dimension \(d\). Then

\[
\boxed{R(T)\ge R(T_0)+d.}                        \tag{9}
\]

Take an ordinary decomposition with \(R(T)\) terms. Its third factors
span a space containing the third support of \(T\). Their projections
to \(C_1\) therefore span \(C_1\). Select \(d\) factors
\(c_i=c_i^0+c_i^1\) whose \(C_1\)
projections form a basis. There is a linear map \(L:C_1\to C_0\)
with \(L(c_i^1)=c_i^0\) for all selected factors. Consequently

\[
\pi(c_0+c_1)=c_0-L(c_1)
\]

fixes \(C_0\) and kills all \(d\) selected factors. Apply \(\pi\)
on the third leg, then the projection \(A\to A_0\) on the first.
The latter removes \(T_1\), while both maps preserve \(T_0\).
At most \(R(T)-d\) terms remain, proving (9).

The lemma works over every field. Its version with the second and
third legs interchanged follows by permuting factors. Enlarging the
ambient spaces does not affect its application: projections back onto
the displayed supports preserve the tensor and cannot increase rank.

## 3. Applying the lemma twice

Apply (9) to

\[
T_0=K+V,\quad T_1=H,\quad
A_0=A_K\oplus A_V,\quad A_1=A_H,\quad
C_0=C_K,\quad C_1=C_H.
\]

All hypotheses follow from (8), and \(\dim C_H=2(r-2)\). Hence

\[
R(E_{b+2,b})\ge R(K+V)+2(r-2).                  \tag{10}
\]

Now interchange the second and third legs in (9), taking

\[
T_0=K,\quad T_1=V,\quad
A_0=A_K,\quad A_1=A_V,\quad
B_0=B_K,\quad B_1=B_V.
\]

It gives

\[
R(K+V)\ge R(K)+2(r-2)=7+2(r-2).                \tag{11}
\]

Combining (7), (10), and (11) proves (1). This argument uses the
specific two-leg support splittings. It does not assert a general
additivity theorem for overlapping embedded cores.

## 4. Border rank and the middle Koszul ceiling

The projections in the lemma depend on a proposed ordinary
decomposition. For a degeneration, these projections can have poles
and amplify higher-order error terms. Thus (9) supplies no border-rank
lower bound by the argument above.

There is also a structural limit on the most direct middle Koszul
test. Equation (5) puts every first slice in

\[
U\otimes C+B\otimes W,\qquad
U=\langle X,Z\rangle,\quad W=\langle R,S\rangle,
\quad\dim U=\dim W=2.
\]

For \(a=\dim A\), the first-leg Koszul map

\[
\Phi_E^{A,p}:\Lambda^pA\otimes B^*
             \longrightarrow\Lambda^{p+1}A\otimes C
\]

therefore satisfies

\[
\operatorname{rank}\Phi_E^{A,p}
\le2\binom ap+2\binom a{p+1}.                   \tag{12}
\]

Indeed, the \(U\)-supported part factors through a domain of dimension
\(2\binom ap\). The other part has image in
\(\Lambda^{p+1}A\otimes W\), of dimension \(2\binom a{p+1}\).
Matrix-rank subadditivity gives (12).

For the \(n=6\) residual, \(a=9,p=4\), this ceiling is 504.
The map is \(1386\times1386\), and its rank-one divisor is
\(\binom84=70\). A rank of at least 1191 would be needed to
prove border rank at least eighteen. Thus this middle Koszul test
cannot establish optimality of the eighteen-term degeneration. The
certificate here checks this analytic ceiling; it does not claim an
exact large-matrix Koszul rank computation.

## 5. Reproduction and evidence

Run from the repository root:

```sh
python -S research/ai/2026-10-23-oblique-border-repair/full_residual_rank.py
python -m unittest discover -s tests -p 'test_oblique_full_residual_rank.py' -v
```

The new verifier uses only the Python standard library and integer
identities. Its saved certificate contains the adapted bases, unit
minors, concise coefficients, flattening pivots, and two separate
support dimensions. It checks \(b=2,3,4,5,6,7,8,12\), replaying the
inherited \(4r-1\) ordinary products for each case. These finite
controls support the formulas; the all-size conclusion is the proof
in Sections 1–3.

For \(n=6,b=4\), it independently contracts all 576 native
paired-source coefficients through the already exported maps. It then
compares all 10000 target coordinates with the saved residual and
with (4). The original maps, ordinary products, polynomial degeneration,
and their existing tests remain unchanged.

The four prior source hashes remain unchanged. The follow-up record in
`sources.json` additionally pins the prior core proof, its verifier and
certificate, and the exported ordinary-map witness at base `b6c38513`.
The projection argument and its application were derived and checked by
agents in this same session. Claim `AI-OBLIQUE-FULL-ORDINARY-RANK-004`
remains written and unreviewed. The smaller 18-term border repair
is compatible with ordinary rank nineteen.
