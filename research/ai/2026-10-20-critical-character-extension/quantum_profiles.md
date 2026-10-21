# A valid higher-difference test for the quantum-character family

October 20, 2026. AI-derived calculation and written proof, unreviewed.
This verifies the proposed higher-difference test on an existing family of
actual tensor characters. It does not prove the test for every character
and does not improve the matrix multiplication exponent.

## 1. Exact convolution values

Let theta=(theta_i,theta_j,theta_k) be nonnegative with sum one. Denote the
complex quantum functional by F_theta. We use its entropy definition and
universal spectral-point theorem from Christandl--Vrana--Zuiddam,
*Universal points in the asymptotic spectrum of tensors*,
[arXiv:1709.07851v3](https://arxiv.org/html/1709.07851v3), Sections 3.2--3.4.
These are imported tensor-theoretic results.

For the oriented polynomial convolution with input lengths a,b,

\[
F_\theta(C_{ij}(a,b))
 =a^{\theta_i}b^{\theta_j}(a+b-1)^{\theta_k}. \tag{1}
\]

Here is an explicit verification that its orbit reaches the simultaneous
dimension upper bounds needed for (1). Scale its coefficient at (u,v,u+v)
to

\[
c_{uv}=\left[
\frac{\binom{a-1}{u}\binom{b-1}{v}}
     {\binom{a+b-2}{u+v}}
\right]^{1/2}.
\tag{2}
\]

This is a product of three nonzero diagonal leg scalings, so the scaled
tensor is in the original GL orbit. Every principal reduced matrix is
diagonal: fixing the other two indices fixes the remaining index.

The sum of the squared coefficients is a+b-1, and their marginals are

\[
\sum_v c_{uv}^2=\frac{a+b-1}{a},\qquad
\sum_u c_{uv}^2=\frac{a+b-1}{b},\qquad
\sum_{u+v=w}c_{uv}^2=1.
\tag{3}
\]

The last identity is Vandermonde's binomial identity. For the first, use

\[
\binom{L}{w}^{-1}
 =(L+1)\int_0^1 t^w(1-t)^{L-w}\,dt,
\qquad L=a+b-2.
\]

After summing in v, the binomial theorem leaves
(L+1) binom(a-1,u) times the beta integral with exponents u,a-1-u,
which equals (a+b-1)/a. The second identity follows by interchange.
Thus the normalized marginals are the uniform distributions in dimensions
a,b,a+b-1. Their weighted entropy is the logarithm of the right side of
(1), which is also the dimension upper bound for every orbit point.
This proves (1) from the cited entropy definition.

The same uniform-marginal argument for convolution blocks appears in the
repository's earlier [recoupling note](../2026-10-20-clebsch-gordan/subrank_blocks.md).
The explicit beta-integral calculation above is supplied for this application;
the balancing construction is not claimed as new.

## 2. All alternating derivative signs

For this family, the dot-product parameters are p_i=1-theta_i, so their
sum is exactly two. If p_i>0, the oriented powered limit is

\[
Q_{ij}(s)=\lim_{N\to\infty}
\left(\frac{F_\theta(C_{ij}(N,\lceil Ns\rceil))}{N}\right)^{1/p_i}
 =s^\beta(1+s)^{1-\beta},
\qquad \beta=\frac{\theta_j}{1-\theta_i}\in[0,1].
\tag{4}
\]

For 0<beta<1, direct differentiation gives

\[
Q'_{ij}(s)=s^{\beta-1}(1+s)^{-\beta}(s+\beta)>0,
\]

\[
-Q''_{ij}(s)
 =\beta(1-\beta)s^{-(2-\beta)}(1+s)^{-(1+\beta)}.
\tag{5}
\]

Every derivative of s^(-alpha), and likewise of (1+s)^(-alpha), has
alternating sign for alpha>0. Leibniz's formula applied to (5) therefore
proves

\[
(-1)^{n-1}Q_{ij}^{(n)}(s)>0
\quad(s>0,\ n\ge2).
\tag{6}
\]

At beta=0 or one, Q is affine and these derivatives vanish. Thus Q' is
completely monotone for every member of this quantum-character family.
This is a direct calculation, not an appeal to regularity of an arbitrary
spectral point.

Repeated application of the fundamental theorem of calculus gives

\[
\Delta_h^5 Q_{ij}(s)
 =\int_{[0,h]^5}Q_{ij}^{(5)}(s+t_1+\cdots+t_5)
  \,dt_1\cdots dt_5\ge0
\quad(s,h>0).
\tag{7}
\]

In particular this holds at s=4/5,h=1/20, the exact stencil that rejects
the hypothetical 9/4 profile in [the endpoint note](README.md), Section 5.

## 3. What this does and does not establish

The test is compatible with an actual universal family of tensor characters,
including every flattening character. Those characters all have square
objective p_i+p_j+p_k=2. They do not approach the hypothetical 9/4 endpoint.
Proving (7) on this family cannot be extended to all characters by density,
convexity, or continuity: no required density or classification theorem has
been supplied.

The more recent Sakabe--Dogan--Walter result,
[*Strassen's support functionals coincide with the quantum functionals*,
arXiv:2601.21553v1](https://arxiv.org/html/2601.21553v1), Theorem 1.1,
identifies upper support functionals with this quantum family for all
complex tensors. It does not identify the quantum family with the entire
asymptotic spectrum. Consequently it also does not supply the missing
universal higher-difference premise.

There is also a classification result for the boundary. Alman--Li--Pratt,
[*The edge of the asymptotic spectrum of tensors*,
arXiv:2604.01386v2](https://arxiv.org/html/2604.01386v2),
Theorem 1.6 / Corollary 8.10, proves that every spectral point with one
dot-product exponent equal to one is an edge support functional. Over the
complex numbers, the preceding identification and calculation therefore
prove (7) for **every** character on that boundary. This does not address
characters near the interior point (3/4,3/4,3/4).

The next construction would have to establish a new inequality for arbitrary
tensor characters. The existing concavity, tripling, rank, and replication
constraints do not imply (7), since the repository's critical profile
satisfies those constraints and fails this stencil.

## 4. Exact values on canonical matched sums

There is a useful finite comparison as well. Consider convolution blocks
C(a,b_h) with the same first-input coefficient basis, disjoint second
inputs, and disjoint outputs. Denote their matched sum by T. With
p=1-theta_i>0 and beta=theta_j/p, one has

\[
\boxed{F_\theta(T)
 =a^{\theta_i}
 \left(\sum_h b_h^\beta(a+b_h-1)^{1-\beta}\right)^p.}
\tag{8}
\]

The common-basis assumption here is intentional. Formula (8) is not
asserted for arbitrary independent changes of the first-input basis.

To prove the upper bound, use the equality between the quantum functional
and the upper support functional cited above, and choose the displayed
coefficient basis. In any probability distribution on this support, the
block label h is determined by the second input and also by the output.
If its distribution is r, the three marginal entropies are bounded by

\[
H(X)\le\log_2a,\quad
H(Y)\le H(r)+\sum_hr_h\log_2b_h,\quad
H(Z)\le H(r)+\sum_hr_h\log_2(a+b_h-1).
\]

Maximizing their theta-weighted sum over r gives the logarithm of (8).

For the reverse inequality, apply the diagonal scalings (2) in every
block. Their required first-input scaling is the same,
\(\sqrt{\binom{a-1}{u}}\), so they can all be performed simultaneously.
Scale the whole h-th block to have normalized mass r_h. Its first-input
marginal is uniform, and the other two marginals are uniform inside that
block. Thus the three entropy upper bounds are attained simultaneously.
Choose r proportional to \(b_h^\beta(a+b_h-1)^{1-\beta}\). This proves
(8). If p=0, the functional is the first-input flattening rank a instead.

In particular, for the canonical matched sums T_+(n), T_-(n) in
[the stencil obstruction](stencil_obstruction.md),

\[
F_\theta(T_+(n))\ge F_\theta(T_-(n))
\quad\hbox{for every theta.}
\tag{9}
\]

Indeed the difference between the sums inside (8) is the fifth forward
difference, at b=16n with step n, of

\[
b\longmapsto b^\beta(b+20n-1)^{1-\beta}.
\]

After a positive change of scale, this is the function in (4). Its fifth
derivative is positive for 0<beta<1 and zero at the endpoints. Hence (9)
is strict when theta_j and theta_k are both positive, and is equality
otherwise.

The exact Koszul witnesses in the linked note nevertheless exclude a
finite degeneration in either direction. Consequently (9) gives a
concrete case where checking all quantum characters cannot decide finite
degeneration. This is consistent with their role in the asymptotic
spectrum. No asymptotic comparison between these two tensors is claimed.

## 5. Exact controls

`quantum_controls.py` checks all three rational squared-coefficient
marginals in (3) for every 1<=a,b<=16. It separately differentiates (5)
as a sum of products to verify the asserted fifth-derivative formula at
rational beta,s. Finally it encloses the stencil in (7) for beta=1/8,...,7/8
using integer eighth-root intervals. No floating-point value decides a sign.
The finite matched-stencil signs in (9) are checked the same way at n=1,2
for those seven beta values, with the finite offset 20n-1 retained.
These are finite algebra and implementation checks; the universal statements
about this particular family rest on the proof above and the cited theorem.

```
python research/ai/2026-10-20-critical-character-extension/quantum_controls.py
```

