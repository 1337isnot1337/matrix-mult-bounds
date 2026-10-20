# External 9/4 argument and local dependency boundary

This page summarizes the external proof route. OpenAI supplies the 9/4 theorem and its original constructions. The current repository supplies neither a replacement proof of that theorem nor a fresh Lean build. [OAI26](literature.md#oai26)

## External theorem stack

The route uses tensor characters, monotonicity under degeneration, shared-leg separation, convolution inequalities, and a discrete-growth estimate. For a nonzero tensor $T$, the profile is

$$\mathcal P(T)=\left(\prod_{\pi\in S_3}\lambda_\pi(T)\right)^{1/(6t)},\qquad P(a,b)=\mathcal P(C(a,b)).$$

The scalar consequences are

$$P(a,b)=P(b,a)>0,\qquad P(1,b)=b,$$
$$2P(a,b)\ge P(a,b-1)+P(a,b+1)\quad(b\ge2),$$
$$P(a,3b+a-1)\ge3P(a,b),\qquad P(a,b)\le(a+b-1)^{1/t}.$$

The discrete argument forces diagonal growth of order at least $a^{4/3}$. The upper bound then forces $t\le3/4$, and the detecting-character argument gives $\omega\le9/4$. [OAI26, Sections 2-5](literature.md#oai26)

## Local addition

The local note proves that the first three scalar conditions have the pointwise-minimal solution

$$P_*(a,b)=h_m\left(M+\frac{m-1}{2}\right),\quad m=\min(a,b),\quad M=\max(a,b).$$

Here $h_1=1$ and $h_{a+1}=(1+1/(3a))h_a$. This recurrence already occurs in OpenAI's intermediate lower bound. The local contribution is its matching two-variable extension and the accompanying feasibility proof.

The profile also satisfies the rank upper bound at $t=3/4$ and the replication constraint at that value. Thus those scalar constraints cannot establish $t<3/4$. This conclusion does not cover every property of actual characters. [Local note, Section 2](../research/ai/2026-10-20/research_note.md#2-exact-pointwise-solution-of-the-scalar-system)

## What a new inequality must accomplish

An inequality that excludes $P_*$ removes one scalar model. Another feasible model can still retain $a^{4/3}$ growth. An exponent claim therefore needs a uniform growth argument or another complete route to matrix multiplication.

One sufficient target is a fixed $\eta>0$ such that every relevant character satisfies

$$P(a,4a-1)\ge(3+\eta)P(a,a)$$

for all sufficiently large $a$. The threshold can depend on the character. The same positive $\eta$ must work for all characters. Under this premise, the local conditional argument gives

$$\omega\le\frac9{4+2\eta}.$$

The premise remains unproved. The value $1500/667$ for $\eta=1/1000$ is a conditional illustration, not a new upper bound. [Local note, Section 6](../research/ai/2026-10-20/research_note.md#6-an-explicit-sufficient-target-for-a-smaller-exponent)
