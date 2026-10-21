# A nonzero correction allowance at the critical growth rate

October 21, 2026. Written conditional argument from the owner-directed
research session, with a same-session agent audit. **No family satisfying
the premise is constructed. No smaller exponent is established here.**

The [previous correction criterion](superlinear_budget.md) permits
auxiliary border rank growing slower than n to the power 3/2. A small
enough nonzero leading coefficient at that critical power also suffices.
The argument excludes endpoint characters directly. Its consequence is
qualitative and does not provide a numerical exponent below 9/4.

## Precise statement

Fix integers \(b\ge4\) and \(h\ge1\), and positive real numbers
\(\rho,\sigma\). For one unbounded sequence of positive integers n,
suppose there are genuine complex tensor degenerations

\[
Q(n,b)\oplus R_n\ \unrhd\ M(l_n,h,r_n),
\qquad \frac{l_n}{n}\longrightarrow\rho,\qquad
\frac{r_n}{n}\longrightarrow\sigma.
\tag{1}
\]

All source tensors, auxiliary tensors, dimensions and maps in this family
are fixed independently of the tensor character. Every individual map
must satisfy its complete degeneration identity. Uniform Laurent orders
or convergence rates across different n are not assumed.

Write \(\underline R(R_n)\) for auxiliary tensor border rank and suppose

\[
C:=\limsup_{n\to\infty}
 \frac{\underline R(R_n)}{n^{3/2}}<\infty
\tag{2}
\]

along that same sequence. Then the following is a sufficient condition:

\[
\boxed{\quad
C<(\rho\sigma h)^{3/4}-\frac43\sqrt b
\quad\Longrightarrow\quad \omega<\frac94 .
\quad}
\tag{3}
\]

The strict inequality requires a positive right side. The statement gives
no conclusion at equality. It also gives no claim when the cost in (2)
is unbounded.

For the near-full width-four case \(b=h=4\) and \(\rho=\sigma=1\), the
allowance is

\[
C<2\sqrt2-\frac83=0.161760458\ldots.
\tag{4}
\]

In particular, the unconstructed family

\[
Q(n,4)\oplus R_n\unrhd M(l_n,4,r_n),\qquad
l_n/n,r_n/n\to1,\qquad
\underline R(R_n)\le\frac4{25}n^{3/2}+o(n^{3/2})
\tag{5}
\]

would imply a strict improvement. The number 4/25 is a coefficient in an
auxiliary-rank budget, not a matrix multiplication exponent.

## Endpoint proof

Assume for contradiction that a tensor character attains the endpoint
\(S=p_1+p_2+p_3=9/4\). The previously established
[endpoint rigidity](../2026-10-20-critical-character-extension/README.md)
forces \(p_1=p_2=p_3=3/4\).

Let \(Q_i(n,b)\) be the cyclic permutation with the two n-dimensional
inputs sharing leg i, and put \(a_i(n)=\lambda(Q_i(n,b))\).
The [earlier paired calculation](README.md), equations (5) and (8), gives

\[
\prod_{i=1}^3a_i(n)=P(n,b)^{9/2},
\qquad
\limsup_{n\to\infty}\frac{P(n,b)}n
\le L_b:=\frac23(6b)^{1/3}.
\tag{6}
\]

Only the symmetrized product is used. The proof does not assume that
individual finite-size oriented profiles coincide or have limits.

At the endpoint, all three cyclic target characters have the same value
\((l_n h r_n)^{3/4}\). The auxiliary character in each orientation is
bounded above by the same border rank. Monotonicity of (1) therefore
implies, separately for each i,

\[
a_i(n)+\underline R(R_n)\ge(l_n h r_n)^{3/4}.
\tag{7}
\]

Set \(A=(\rho\sigma h)^{3/4}\). Dividing by \(n^{3/2}\), taking the lower
limit, and using (2) gives

\[
\liminf\frac{a_i(n)}{n^{3/2}}\ge A-C.
\tag{8}
\]

The premise in (3) makes \(A-C>0\). Thus the product of the three
nonnegative sequences has lower limit at least \((A-C)^3\).
Equation (6) supplies the opposing upper bound:

\[
(A-C)^3
\le
\liminf\prod_i\frac{a_i(n)}{n^{3/2}}
\le
\limsup\left(\frac{P(n,b)}n\right)^{9/2}
\le L_b^{9/2}
=\frac{64}{27}b^{3/2}.
\tag{9}
\]

The final equality follows from \(L_b^3=16b/9\).
Taking positive cube roots yields

\[
A-C\le\frac43\sqrt b,
\tag{10}
\]

contradicting the strict premise. This excludes every endpoint character.

The normalized complex tensor spectrum is compact, and the continuous
matrix-character evaluation attains its maximum. Together with the
spectral characterization of omega and the external 9/4 theorem, the
absence of an endpoint character gives \(\omega<9/4\).
Compact attainment is stated in Alman--Li,
[*Asymptotic Rank Speedup Theorems, Revisited*, arXiv:2605.21738v1](https://arxiv.org/html/2605.21738v1#S4.SS1),
Proposition 4.2, with credit to Strassen's spectrum framework.
This compactness step is why merely excluding equality is enough here.

## Exact budget comparisons

The width-four choice \(C=4/25\) needs no decimal approximation:

\[
\frac83+\frac4{25}=\frac{212}{75}>0,\qquad
8-\left(\frac{212}{75}\right)^2=\frac{56}{5625}>0.
\tag{11}
\]

Consequently \(212/75<2\sqrt2\), proving the strict margin in (5).
The verifier also brackets the radical in (4) by rational numbers
whose squared endpoints bracket two.

For \(b=h=16\) and full limiting outer ratios, the allowed coefficient is
strictly below \(8/3\); \(C=5/2\) is a rational admissible choice.
For \(b=h=81\), it is strictly below 15. These comparisons illustrate
the budget formula and supply no construction.

The older little-o assumption is the case \(C=0\) of this criterion.
At \(h=b\) and full outer ratios, positivity is equivalent to
\(81b>256\), the same width threshold as before.
For an auxiliary bound of order \(n^\alpha\) with fixed \(\alpha<3/2\),
the earlier localization theorem remains stronger because it also gives
an explicit conditional numerical exponent.

## Verification, provenance and limits

The proof uses the existing paired product identity, thin-slope upper
bound, endpoint rigidity and compact spectrum attainment. The tensor
character framework and 9/4 theorem remain attributed to OpenAI's pinned
paper; replication and oriented rescaling retain the earlier notes'
credit to Uznański, arXiv:2610.10494v2. The new deduction compares each
cyclic target inequality before taking their product.

The adjacent standard-library verifier checks exact budget inequalities,
the strict width-four margin, the radical bracket, the source-constant
power identity and negative/equality controls. These finite checks do not
prove the missing maps or replace the quantified argument. The other
research agent's audit occurred in this same generating session and is
not independent mathematical review.

    python -S research/ai/2026-10-21-correction-budget/critical_coefficient.py
    python -S -m unittest discover -s tests -p test_critical_correction_coefficient.py -v

No explicit numerical gap below 9/4 follows from the qualitative family
hypothesis alone in this proof. No such family has yet been found.
