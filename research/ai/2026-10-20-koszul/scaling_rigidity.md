# Actual rescaled profiles and endpoint rigidity without differentiability

Date: 2026-10-20. AI-derived written proof, unreviewed and not formalized.
No smaller exponent is established. This closes the analytic applicability gap
in the second-pass rigidity/curvature drafts; the required positive gain remains
unproved.

## 1. External input and an actual character profile

For every tensor character $\lambda$, let $p_X,p_Y,p_Z$ be its dot-product
parameters and $t=(p_X+p_Y+p_Z)/3>0$. We use Uznański's
[*Rectangular matrix multiplication from polynomial products*,
arXiv:2610.10494v2](https://arxiv.org/abs/2610.10494v2), Lemma 4.1 and Appendix F.
For each orientation $\pi$, they establish the positive continuous limit

$$g_\pi(x,y)=\lim_{N\to\infty}
\frac{\lambda_\pi(C(\lceil Nx\rceil,\lceil Ny\rceil))}{N}.$$

These functions are homogeneous of degree one and bounded between
$\min(x,y)$ and $x+y$. This is an imported theorem, not a new construction
or a local Lean rebuild. Its proof uses the replication degeneration, common
integer scales, and monotonicity; it does not assume character continuity.

Set $d=1/t$ and

$$F(x,y)=\left(\prod_{\pi\in S_3}g_\pi(x,y)\right)^{1/(6t)}
=\lim_{N\to\infty}\frac{P(\lceil Nx\rceil,\lceil Ny\rceil)}{N^d}.$$

Thus $F$ is positive, continuous, symmetric, coordinatewise nondecreasing,
homogeneous of degree $d$, and $F(x,y)\le(x+y)^d$.
OpenAI's discrete concavity of $P$ passes to rational convex combinations at a
common integer scale, then to real points by continuity. Hence $F$ is separately
concave. Shifted tripling passes to the limit as

$$F(x,3y+x)\ge3F(x,y). \tag{1}$$

To justify its moving rounded arguments, sandwich the rescaled integer lengths
between any two nearby fixed real lengths and use monotonicity and continuity.
This avoids an assumption of uniform convergence. The same observation removes
rounding errors in the concavity passage. All the analytic properties above
hold for each actual character; no differentiability assumption has been added.

## 2. A one-sided derivative argument

Let $f(s)=F(1,s)$ and $c=f(1)>0$. Concavity on the open interval $(0,\infty)$
gives finite one-sided derivatives at 1, with $f'_-(1)\ge f'_+(1)$.
Symmetry and homogeneity imply

$$f(s)=s^d f(1/s),\qquad f'_+(1)=dc-f'_-(1).$$

For the derivative identity, insert $s=1+h$ with $h\downarrow0$; then
$1/s=1-h+O(h^2)$ approaches 1 from the left. Therefore

$$f'_+(1)\le\frac d2c. \tag{2}$$

For every $s\ge1$, concavity bounds $f(s)$ by its right tangent at 1.
Together with (1) at $(1,1)$ this gives

$$3c\le f(4)\le c+3f'_+(1)\le(1+3d/2)c.$$

Consequently $d\ge4/3$, recovering the baseline. This is a rederivation of
its growth conclusion, not a new exponent result.

## 3. Endpoint rigidity for every actual critical character

Suppose $t=3/4$, equivalently $d=4/3$. Every inequality in the preceding display
is an equality. In particular $f'_-(1)=f'_+(1)=2c/3$, and concavity forces $f$
to equal its tangent on $[1,4]$. Put $K=2c/3$ and $L(s)=K(s+1/2)$.
Concavity gives $f(s)\le L(s)$ for all $s\ge1$.

Starting with $s_0=1$, let $s_{j+1}=3s_j+1$. If $f(s_j)=L(s_j)$, (1) gives
$f(s_{j+1})\ge3L(s_j)=L(s_{j+1})$, so equality holds there as well. These
points tend to infinity. Concavity between consecutive points and the tangent
upper bound force $f=L$ everywhere on $[1,\infty)$.
Symmetry and homogeneity now give the forced form

$$\boxed{F(x,y)=K\min(x,y)^{1/3}
\left(\max(x,y)+\frac{\min(x,y)}2\right),\quad K>0.} \tag{3}$$

This removes the previous draft's global continuous-differentiability premise
and proves applicability to actual characters by the cited rescaling theorem.
It does not produce a critical character or exclude one. The constant $K$ is
not asserted to equal the first-pass matching profile's constant.

## 4. Curvature criterion with the analytic bridge supplied

For an actual character define its normalized curvature

$$\delta_\lambda=
\frac{2F(1,2)-F(1,1)-F(1,3)}{F(1,1)}\ge0.$$

Write $s_i=f(i+1)-f(i)$ for $i=1,2,3$. Concavity gives
$s_3\le s_2=s_1-\delta_\lambda c$, and (2) gives $s_1\le dc/2$.
Consequently

$$3c\le f(4)=c+s_1+s_2+s_3
\le(1+3d/2-2\delta_\lambda)c.$$

Thus every character individually satisfies

$$d\ge\frac43(1+\delta_\lambda),\qquad
3t\le\frac9{4(1+\delta_\lambda)}. \tag{4}$$

If an additional tensor argument supplies a character-independent lower bound
$\delta_\lambda\ge\delta_0>0$, the detecting-character argument gives

$$\omega\le\frac9{4(1+\delta_0)}<\frac94.$$

**The sole new premise needed in this criterion is the uniform positive
curvature bound. It is not proved here.** At the critical form (3) this
curvature is exactly zero. A single finite improvement of $P_*$ does not
establish it, nor does positive curvature for a finite sample of profiles.

It is enough to prove the positive curvature bound only for characters with
$t\ge t_0$, for some fixed $t_0<3/4$. The remaining characters already give
$3t<3t_0$, so the conclusion would be

$$\omega\le\max\left\{3t_0,\frac9{4(1+\delta_0)}\right\}<\frac94.$$

This weaker premise focuses the search on characters near the critical value;
it is also unproved.

## Dependencies and remaining task

- External: Uznański v2, Lemma 4.1 / Appendix F (the actual rescaling limit).
- External: OpenAI, pinned revision
  `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, Lemmas 4.1-4.2 and 2.2
  (concavity, tripling, detecting characters).
- Local antecedent: second-pass note, Sections 4-5 (the conditional C1
  calculation), preserved without editing.
- Local completion: one-sided derivatives replace the C1 assumption and the
  external rescaling theorem supplies the actual-character bridge.
- Unresolved: derive a tensor constraint excluding the critical form or forcing
  the uniform positive curvature in (4), with the full quantifiers intact.
