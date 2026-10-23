# A border-rank lower bound from the long-leg equalizer

October 23, 2026. Owner-directed Codex continuation. Claim
`AI-OBLIQUE-BORDER-EQUALIZER-001` is written and unreviewed. Separate
checks by agents in the generating session are not independent
mathematical review or formalization.

## Result and scope

Fix a field \(k\), an integer \(b\ge2\), \(n=b+2\) and \(r=b+1\). Let
\(E_{n,b}\) be the actual residual of the existing integer product-oblique
maps

\[
Q(n,b)\longrightarrow M(r,4,r)-E_{n,b}.
\]

The [preceding ordinary-rank proof](../2026-10-23-oblique-border-repair/full_residual_rank.md)
identifies its concise format as
\((2r-1)\times(2r+1)\times(2r+1)\). We prove

\[
\boxed{\underline R(E_{b+2,b})\ge2r+2.}                 \tag{1}
\]

Here geometric border rank is taken over an algebraic closure of \(k\).
The same obstruction applies to formal degenerations over every field.
Over \(\mathbb C\), this is the usual tensor border rank.

For \((n,b)=(6,4)\), the result improves the lower endpoint from eleven
to twelve:

\[
\boxed{12\le\underline R(E_{6,4})\le18,
\qquad R(E_{6,4})=19.}                              \tag{2}
\]

The upper bound and ordinary equality are inherited from the
[polynomial construction](../2026-10-23-oblique-border-repair/proof.md)
and the preceding ordinary-rank proof. The source maps and residual are
unchanged. Neither border-rank optimality nor an obstruction for other
source maps is claimed. No smaller matrix multiplication exponent follows.

## 1. A closed necessary condition for minimal border rank

This is the established pairwise symmetry Lie-algebra condition,
equivalently the two-factor 111 test; see J. M. Landsberg,
[*Secant varieties and the complexity of matrix multiplication*](https://arxiv.org/pdf/2208.00857.pdf),
arXiv:2208.00857v1, Sections 5.4 and 6.1, printed page 9. That source
works over \(\mathbb C\). The elementary proof below states the
rectangular-first-leg version and its characteristic-independent scope.

Let \(T\in A\otimes B\otimes C\), with
\(\dim B=\dim C=m\). Define the linear map

\[
\Phi_T:\operatorname{End}(B)\oplus\operatorname{End}(C)
\longrightarrow A\otimes B\otimes C,
\qquad
\Phi_T(L,M)=(1\otimes L\otimes1)T-(1\otimes1\otimes M)T.
                                                               \tag{3}
\]

Then

\[
\underline R(T)\le m
\quad\Longrightarrow\quad
\dim\ker\Phi_T\ge m,
\quad\text{equivalently}\quad
\operatorname{rank}\Phi_T\le2m^2-m.                \tag{4}
\]

To prove this, first take
\(T=\sum_{i=1}^m a_i\otimes b_i\otimes c_i\), where both
\((b_i)\) and \((c_i)\) are bases. For every
\(\lambda=(\lambda_1,\ldots,\lambda_m)\), define

\[
L_\lambda b_i=\lambda_i b_i,
\qquad M_\lambda c_i=\lambda_i c_i.
\]

These give \(m\) independent elements of \(\ker\Phi_T\). In the
parameter space of all \(m\)-term decompositions, the two basis
conditions define a nonempty dense open set. Matrix entries of
\(\Phi_T\) depend linearly on \(T\), so the rank upper bound in (4)
is defined by polynomial minors. Those minors vanish on the dense
parameter set, hence on every tensor of rank at most \(m\), and then
on its Zariski closure. This proves (4).

The proof works over an algebraic closure in every characteristic.
Polynomial minor identities also specialize along any formal
degeneration. It requires no invertible slice and no concision hypothesis
on \(A\). It applies only to the displayed minimal-rank threshold
\(m\); the same conclusion has not been asserted for border rank
\(m+1\).

## 2. The actual residual in adapted bases

The prior proof supplies independent support bases, with unit embedding
minors, in which

\[
E=K+\sum_{j=1}^{r-2}h_j(Xp_j+Zq_j)
       +\sum_{j=1}^{r-2}v_j(x_jR+y_jS),              \tag{5}
\]

where

\[
K=u(XP+ZQ)+v(aR+\eta S)
       +w(XQ+ZT+\eta R+yS+XR).                    \tag{6}
\]

The first basis is \((u,v,w,h_1,\ldots,h_{r-2},v_1,\ldots,v_{r-2})\).
The second basis consists of \((X,Z,a,\eta,y)\) and all pairs
\((x_j,y_j)\). The third consists of \((P,Q,R,S,T)\) and all pairs
\((p_j,q_j)\). Thus both long dimensions are \(m=2r+1\).

For clarity, \(v\) and each \(v_j\) are distinct first-leg vectors;
\(y\) and each \(y_j\) are distinct second-leg vectors. The embedding
and original tensor convention are inherited, not new constructions.
The verifier independently expands (5) and contracts the exported
\(Q(6,4)\) source maps to check the actual finite tensor.

## 3. The equalizer has dimension two

We show that every solution of \(\Phi_E(L,M)=0\) is

\[
(L,M)=\alpha(I_B,I_C)+\mu(N_B,N_C),                \tag{7}
\]

where \(N_B(y)=Z\), \(N_C(T)=S\), and both operators vanish on
their other basis vectors.

Compare the coefficient of \(u\). Its two independent second and
third factors force

\[
\begin{array}{ll}
LX=\alpha X+\beta Z,&LZ=\gamma X+\delta Z,\\
MP=\alpha P+\gamma Q,&MQ=\beta P+\delta Q.
\end{array}                                                     \tag{8}
\]

There are no components outside the displayed spans: projecting the
equality to \(B/\langle X,Z\rangle\), or to
\(C/\langle P,Q\rangle\), sets those components to zero.
Similarly, the coefficient of \(v\) gives

\[
\begin{array}{ll}
MR=pR+qS,&MS=tR+sS,\\
La=pa+t\eta,&L\eta=qa+s\eta.
\end{array}                                                     \tag{9}
\]

In the \(w\) coefficient, compare respectively
\(X\otimes P\), \(X\otimes T\), \(a\otimes R\),
\(y\otimes R\), \(X\otimes Q\), and \(\eta\otimes R\).
They give

\[
\beta=\gamma=q=t=0,\qquad\delta=\alpha,\qquad s=p.
                                                               \tag{10}
\]

The remaining \(w\) equality becomes

\[
(\alpha-p)X\otimes R
 +Z\otimes(\alpha T-MT)+(Ly-py)\otimes S=0.        \tag{11}
\]

Its \(X\otimes R\) coefficient gives \(\alpha=p\). The remaining
two simple terms imply

\[
Ly=\alpha y+\mu Z,
\qquad MT=\alpha T+\mu S.                          \tag{12}
\]

This also excludes all components in the outer supports. Finally, each
\(h_j\) coefficient forces \(Mp_j=\alpha p_j\) and
\(Mq_j=\alpha q_j\); each \(v_j\) coefficient forces
\(Lx_j=\alpha x_j\) and \(Ly_j=\alpha y_j\). This proves (7).
Both displayed pairs satisfy the equality and are independent. Therefore

\[
\boxed{\dim\ker\Phi_E=2,\qquad
\operatorname{rank}\Phi_E=2(2r+1)^2-2.}            \tag{13}
\]

No division was used. The argument and the independent basis vectors
apply in every characteristic. Since \(m=2r+1>2\), equations (4) and
(13) imply \(\underline R(E)>m\), proving (1).

## 4. Exact certificate and limits of the evidence

At \((n,b)=(6,4)\), \(\Phi_E\) has 242 columns and 1089 possible
output rows. Of these rows, 392 are nonzero. The saved certificate gives
a \(240\times240\) minor with determinant \(-1\), together with
the two explicit kernel generators. Border rank at most eleven would
force matrix rank at most 231. Thus even a nonzero minor of order 232
would suffice; the saved unit minor certifies the full rank in every
characteristic.

The standard-library verifier reconstructs the sparse matrix from all
21 nonzero adapted tensor coefficients. It replays the selected minor,
checks both kernel generators, and checks eight controls at
\(b=2,3,4,5,6,7,8,12\). Every control is compared with the preceding
support certificate. Four source hashes are checked. An independent
native contraction uses all 576 source terms and compares all 10000
target coordinates with the adapted tensor and saved residual. Literal
tensor and native residual hashes make that identification explicit.

The all-size conclusion is the coefficient proof above, not an
extrapolation from those eight controls. Full-space and projected Koszul
screens motivated a different test but provide no exclusion of other
flattenings. The ordinary two-leg projection lemma remains an ordinary
rank argument; it is not used in (1). Whether the fixed full residual
has border rank twelve, eighteen, or an intermediate value remains open.

Run from the repository root:

```sh
python -S research/ai/2026-10-23-oblique-border-equalizer/verify.py
python -m unittest discover -s tests -p 'test_oblique_border_equalizer.py' -v
```
