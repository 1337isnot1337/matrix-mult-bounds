# A larger correction budget from spectral localization

October 21, 2026. Written conditional argument from the owner-directed
research session, with a same-session agent audit. **No construction
satisfying the premise is supplied, and no smaller exponent is proved.**

The [linear-correction criterion](README.md) can tolerate more than linear
auxiliary border rank. This follows from the already established
[one-coordinate endpoint bound](../2026-10-20-critical-character-extension/README.md),
equation (7), rather than from a new tensor restriction. The sharper budget
is useful when evaluating proposed error tensors.

## Statement

Fix an integer b at least four and a real alpha with

\[
1\leq\alpha<\frac32.
\]

Suppose that for an unbounded sequence of positive integers n there are
complex tensor degenerations

\[
Q(n,b)\oplus R_n\ \unrhd\ M(l_n,b,r_n),
\qquad \frac{l_n}{n},\frac{r_n}{n}\longrightarrow1,
\qquad \underline R(R_n)\leq Cn^\alpha,
\tag{1}
\]

with C independent of n. The same sequence, maps and auxiliary tensors
must work independently of the tensor character. The source Q, its
orientations and the border-rank convention are those in the earlier note.

Let d_b be the unique positive root of

\[
d_b(6b)^{d_b}=12b^{3/2},\qquad B_b=3/d_b.
\]

Then the following implication holds:

\[
\boxed{\quad
\omega\leq
\max\left\{B_b,\ \frac94-\left(\frac32-\alpha\right)^2\right\}.
\quad}
\tag{2}
\]

Both terms on the right are below 9/4. In particular, for b=4, either
alpha=4/3 or alpha=137/100 still gives the strict rational consequence

\[
\omega<\frac{30000}{13433}<2.2334.
\tag{3}
\]

These are conditional conclusions. The available small tensor maps do not
satisfy the unbounded near-full premise (1).

## Why localization gives the extra room

Fix a character with dot-product parameters p_i, and set

\[
S=p_1+p_2+p_3,\qquad \delta=\frac94-S.
\]

The existing 9/4 theorem gives delta at least zero. For S>2 the earlier
one-coordinate inequality gives

\[
p_i\leq\frac34-\delta+\sqrt\delta,
\qquad
\boxed{S-p_i\geq\frac32-\sqrt\delta.}
\tag{4}
\]

Here delta is less than 1/4, so the square-root rearrangement has the
required nonnegative endpoints. If

\[
S>\frac94-\left(\frac32-\alpha\right)^2,
\tag{5}
\]

then sqrt(delta)<3/2-alpha. Consequently every pair sum S-p_i is
strictly greater than alpha. Strictness in (5) is essential.

Let a_i(n) be the character of the cyclically oriented paired source
whose n-squared leg is i. The previous note proves

\[
a_i(n)\leq n^{S-p_i}b^{2p_i},\qquad
\prod_i a_i(n)=P(n,b)^{2S}.
\tag{6}
\]

Applying (1) in all three orientations therefore gives

\[
\prod_i\bigl(a_i(n)+Cn^\alpha\bigr)
\ \geq\ n^{2S}b^S(1+o(1)).
\tag{7}
\]

The near-full outer dimensions cause only the displayed relative factor.
After expansion, the seven terms containing an auxiliary factor have
the following exponent gaps below 2S:

| Number of auxiliary factors | Positive gap |
|---:|---|
| One, replacing a_k | S-p_k-alpha |
| Two, leaving a_i | S+p_i-2alpha |
| Three | 2S-3alpha |

The first three gaps are positive by (4)--(5). Each second-row gap is
the sum of two first-row gaps: if {i,j,k}={1,2,3}, then

\[
S+p_i-2\alpha
=(S-p_j-\alpha)+(S-p_k-\alpha).
\]

The third-row gap is the sum of all three first-row gaps. Thus every
auxiliary term in (7) is o(n^(2S)). Dividing by n^(2S) yields

\[
\liminf\frac{P(n,b)}n\geq\sqrt b
\tag{8}
\]

along the construction sequence.

For d=3/S, the homogeneous concavity and replication calculation already
proved in the linear-correction note gives

\[
\limsup\frac{P(n,b)}n\leq\frac{d(6b)^d}{12b}.
\tag{9}
\]

If S>B_b, then d<d_b, so strict monotonicity of d(6b)^d makes (9)
strictly less than sqrt(b), contradicting (8). No character can exceed
both terms in (2), which proves the conditional bound.

## Exact rational examples

At alpha=4/3, the second term of (2) equals 20/9. At alpha=137/100,
it equals 22331/10000. Both are strictly less than 30000/13433.
The earlier integer certificate proves B_4<30000/13433. Hence (3)
follows in both cases without relying on decimal root finding.

At alpha=7/5 and alpha=149/100 the localization terms are respectively
56/25=2.24 and 22499/10000=2.2499. They exceed the certified upper
bound for B_4, so (2) gives these respective conditional bounds.

## A qualitative endpoint version

The weaker rate assumption

\[
\underline R(R_n)=o(n^{3/2})
\tag{10}
\]

also suffices to imply omega<9/4, without supplying a numerical gap.
Indeed, an endpoint character has p_1=p_2=p_3=3/4 by the existing
endpoint rigidity theorem. Equation (6) bounds every a_i by a constant
times n^(3/2). Each term containing (10) is then o(n^(9/2)), so (8)
holds at d=4/3. For b>=4, the exact comparison 81b>256 makes (9)
strictly less than sqrt(b), a contradiction.

The normalized tensor spectrum is compact and the evaluation giving S
attains its maximum. This fact is explained in the previous homogeneous
rigidity note and is also stated as Proposition 4.2 in Alman--Li,
[*Asymptotic Rank Speedup Theorems, Revisited*, arXiv:2605.21738v1](https://arxiv.org/html/2605.21738v1#S4.SS1),
20 May 2026, with credit to Strassen's spectrum framework. Excluding all
endpoint characters therefore gives a strict maximum below 9/4. It does
not give an explicit numerical gap from the rate assumption (10) alone.

## Verification and provenance

The tensor inputs remain OpenAI's character and replication framework
and the already attributed Uznański rescaling and offset inequalities.
This note combines the previous local endpoint localization and
correction-budget arguments. It asserts no historical priority or
independent mathematical review.

`superlinear_budget.py` checks the rational comparisons, all seven
correction exponent gaps on a rational parameter grid in the algebraic
angular region, and a strict-boundary negative control. It also repeats
the integer root comparison used in (3). These finite checks do not
construct any of the tensors in (1) or prove the universal statement
without the written argument above.
