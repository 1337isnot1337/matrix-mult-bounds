# What the two-source determinant filtration actually adds

October 20, 2026. AI-derived written proof by Codex, directed by the repository
owner. Base revision: `5d831b4`. No independent review or Lean formalization.
No improvement of the matrix-multiplication exponent is claimed.

## Result and consequence

R2 is settled by a general scalar argument: **the entire three-family
two-source filtration system is equivalent to separate concavity, including
the zero boundary**, for positive, symmetric, edge-normalized profiles.
Consequently the earlier matching profile satisfies all these inequalities at
all positive integer sizes. The old finite grid was not the reason to expect
compatibility; the families have no further force on this class of profiles.

This closes the specific proposal to improve 9/4 by adding only the fixed-label
inequalities (11)-(12) of the first-pass note. It does not exclude extracting
several label fibers together, using oriented character data, or using tensor
identities outside this family. It is not a lower bound on matrix multiplication.

## 1. Precise theorem

Let `F` be a positive function on pairs of positive integers with

$$F(a,b)=F(b,a),\qquad F(1,b)=b.$$

Set `F(a,0)=F(0,a)=0`. Say it is separately concave through zero if its
increments on each nonnegative integer axis are nonincreasing. In particular,
the boundary condition is

$$F(a,2)\le 2F(a,1)=2a. \tag{B}$$

For positive integers `a,b,c,d`, write

$$A_i=a+c-1-2i\quad(0\le i<\min(a,c)),$$
$$B_j=b+d-1-2j\quad(0\le j<\min(b,d)).$$

Then separate concavity through zero is equivalent to the following system:

$$\sum_j F(A_i,B_j)\le F(a,b)F(c,d)\quad\text{for every }i, \tag{X}$$
$$\sum_i F(A_i,B_j)\le F(a,b)F(c,d)\quad\text{for every }j, \tag{Y}$$
$$\sum_{i+j=k}F(A_i,B_j)\le F(a,b)F(c,d)
\quad\text{for every }k. \tag{Z}$$

Empty sums are zero. The indices in (Z) must also lie in their displayed
ranges. These are the earlier fixed-input and fixed-output filtration families.

## 2. Two elementary lemmas

**Monotonicity.** A positive concave sequence on all positive integers is
nondecreasing. Otherwise a negative increment, and every subsequent increment,
would be bounded above by the same negative number, eventually contradicting
positivity. Thus `F` is nondecreasing on both positive axes.

**Endpoint product bound.** Put `A=a+c-1`. Separate concavity and edge
normalization give

$$F(a,b)F(c,d)\ge
\min\{bF(A,d),\ dF(A,b)\}. \tag{E}$$

To prove this when `A>1`, a positive concave sequence is log-concave:

$$u_s^2\ge\left(\frac{u_{s-1}+u_{s+1}}2\right)^2
\ge u_{s-1}u_{s+1}.$$

Hence

$$g(s)=\log F(s,b)+\log F(A+1-s,d),\quad 1\le s\le A,$$

is a concave sequence. A concave sequence lies above the chord between its
endpoints, and therefore above their minimum. Evaluate at `s=a`, then
exponentiate. The endpoint products are `b F(A,d)` and `d F(A,b)`.
For `A=1` the assertion is equality. No zero-boundary assumption was needed
for (E).

## 3. Proof that concavity implies all three families

First prove (X) for `i=0`, so `A_0=A`. Set `q=min(b,d)`. The positive integers
`B_j` have total

$$\sum_{j=0}^{q-1}B_j=q(b+d-q)=bd.$$

Pad this list with zeros to have exactly `b` entries. Its mean is the integer
`d`. Jensen's inequality for the piecewise linear concave interpolation of
`F(A,.)` on the nonnegative integers yields

$$\sum_j F(A,B_j)\le bF(A,d).$$

Padding the same list to `d` entries instead gives

$$\sum_j F(A,B_j)\le dF(A,b).$$

Both paddings are valid since `q<=min(b,d)`. Zero entries contribute zero.
Together with (E), these inequalities prove (X) for `i=0`. Monotonicity and
`A_i<=A_0` give every other (X). Symmetry gives (Y).

For (Z), the valid `j=k-i` are distinct and form a subset of the (X) sum.
Termwise monotonicity gives

$$\sum_{i+j=k}F(A_i,B_j)
\le\sum_{i+j=k}F(A_0,B_j)
\le\sum_jF(A_0,B_j).$$

The last expression is already bounded by the source product. This proves
all three families, including singleton blocks and input lengths equal to one.

## 4. Converse and the necessary boundary hypothesis

In (X), take `c=1,d=2`. There is only `i=0`. For `b>=2` this is

$$F(a,b+1)+F(a,b-1)\le2F(a,b),$$

and for `b=1` it is exactly (B). Symmetry supplies the other axis. This proves
the converse and completes the equivalence.

The zero boundary cannot simply be omitted. For example,

$$F(a,b)=ab+(a-1)(b-1)$$

is positive, symmetric, normalized, and separately affine on the positive
integers. It even satisfies shifted tripling: its surplus is
`(a-1)(2a+1)>=0`. Yet at `(a,b,c,d)=(2,1,1,2)`, (X) would say `5<=4`.
Thus this note does not claim that the original S1-S3 alone imply the complete
filtration system. The example is not feasible for the original rank bound at
`t=3/4` and is not a tensor-character construction.

## 5. Application to the matching profile and actual characters

The earlier profile is

$$P_*(a,b)=h_{\min(a,b)}
\left(\max(a,b)+\frac{\min(a,b)-1}{2}\right),$$
$$h_1=1,\qquad h_{n+1}=\frac{3n+1}{3n}h_n.$$

Its positive-axis concavity was proved in the first pass, Section 2.1. For the
remaining zero boundary, `P_*(1,2)=2`; when `a>=2`,

$$P_*(a,2)=\frac43\left(a+\frac12\right)\le2a.$$

It is therefore separately concave through zero. The theorem proves its
compatibility with (X)-(Z) for every positive quadruple, replacing the open
all-size question behind EXP-FILTRATION-002. The old finite result remains
historical evidence with its original scope.

Actual symmetrized character profiles also have the zero boundary. There is
an elementary restriction

$$B_Y(a)\otimes B_X(b)\ \ge\ C(a,b).$$

The source is `sum_{u,v} x_u y_v z_{uv}`; substitute `z_{uv}=z_{u+v}`.
Each oriented dot product of size `r` has symmetrized profile `r`. Tensor
multiplicativity and restriction monotonicity therefore give

$$P(a,b)\le ab.$$

In particular `P(a,2)<=2a`. OpenAI's discrete concavity, symmetry and
normalization supply the other hypotheses. Thus on actual profiles these
three two-source families already follow from the ordinary concavity and this
elementary restriction; they add no new scalar constraint there.

## 6. Verification and next mathematical gap

`verify.py` checks the proof's intermediate bounds with exact rational
arithmetic, including nontrivial large and unequal lengths. The regression
tests include other normalized concave profiles, the failed boundary example,
and a direct coordinate check of the elementary restriction. These support
implementation correctness. Sections 1-5, not the finite tests, are the
all-integer proof.

The next useful question must retain information discarded by taking one label
fiber: a coupled extraction of several fibers, an oriented inequality not
recoverable from the six-factor symmetrization, or a different exact tensor
construction. This theorem does not supply such a construction or a uniform
tripling gain.

## Sources and attribution

- [First-pass local note](../2026-10-20/research_note.md), Sections 2 and 4:
  matching profile and the precise proposed product-filtration families.
- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf),
  Sections 2-4: character and dot-product rules, shared-leg entropy,
  normalization and discrete concavity. The pinned PDF text was inspected
  locally; its Lean proof was not rebuilt.
- Jensen's inequality, log-concavity of positive concave sequences, and the
  determinant filtration are standard tools. This is a local rederivation and
  synthesis; historical priority and independent review are not claimed.
