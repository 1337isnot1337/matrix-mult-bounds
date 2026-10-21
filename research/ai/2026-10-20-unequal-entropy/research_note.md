# A sharp all-size certificate for the unequal determinant filtration

October 20, 2026. AI-derived written proof with exact arithmetic certificates.
No independent mathematical review or Lean formalization is claimed.
**The matrix multiplication exponent is unchanged.**

## 1. Question and result

This completes the all-size question R7 in `docs/research_directions.md`.
The preceding full-filtration note proved a `39/40` upper bound for balanced
sources and checked unequal source lengths through 12. That note left the
all-size unequal-source bound open.

Use the existing recurrence and matching profile

\[
h_1=1,\qquad h_{n+1}=\frac{3n+1}{3n}h_n,\qquad
P_*(a,b)=h_{\min(a,b)}\frac{2\max(a,b)+\min(a,b)-1}{2}.
\]

The recurrence is external work from OpenAI's 9/4 proof. The matching
two-variable profile is prior work in this repository. For positive lengths,
write

\[
W(a,c)=\sum_{i=0}^{\min(a,c)-1}h_{a+c-1-2i}^{3/2},\qquad
R(x,y)=\frac{P_*(x,y)}{h_xh_y},
\]

and retain the previous all-distribution upper certificate

\[
U(a,b,c,d)=R(a+c-1,b+d-1)[W(a,c)W(b,d)]^{2/3}. \tag{1}
\]

**Theorem (AI-UNEQUAL-ENTROPY-001).** For every four integers
`a,b,c,d >= 2`,

\[
\boxed{
\frac{U(a,b,c,d)}{P_*(a,b)P_*(c,d)}\le B,
\qquad
B=\frac{81}{350}\left(1+\frac{14\sqrt{14}}{27}\right)^{4/3}.
} \tag{2}
\]

Equality holds exactly when `a=b=c=d=2`. At every other source,

\[
\frac{U(a,b,c,d)}{P_*(a,b)P_*(c,d)}\le\frac{97}{100}<B.
\tag{3}
\]

The exact root certificates give

\[
0.974772906<B<0.974772907<39/40.
\]

The number `B` is the sharp constant for the certificate `U`. This statement
does not claim that `B` is the sharp constant for the entropy optimization
itself.

For completeness, the entropy expression from the preceding note is

\[
E(q)=\exp\left(\frac43\min\{H(q_X),H(q_Y),H(q_Z)\}
                 +\sum_{i,j}q_{ij}\log P_*(A_i,B_j)\right),
\]

where `A_i=a+c-1-2i`, `B_j=b+d-1-2j`, `q` is a probability distribution,
and the third index is `i+j`. The earlier proof gives `E(q) <= U` for every
distribution. Consequently (2) supplies a uniform gap of more than 2.5227
percent for this score over **all** unequal source lengths at least two.

The result concerns this explicitly defined score. It does not supply a
weighted tensor-extraction theorem, exclude every tensor construction, or
show that `P_*` extends to an actual tensor character. No smaller exponent
follows from this obstruction.

## 2. Three elementary recurrence bounds

The recurrence gives

\[
\frac{h_n^3}{n}\text{ increasing},\qquad
\frac{h_n^3}{3n-1}\text{ decreasing}. \tag{4}
\]

These are strict for consecutive positive integers. The first follows from

\[
\left(1+\frac1{3n}\right)^3-\left(1+\frac1n\right)
=\frac{9n+1}{27n^3}>0.
\]

For the second, cross multiplication leaves

\[
27n^3(3n+2)-(3n+1)^3(3n-1)=6n+1>0.
\]

We also need that `w_n=h_n^(3/2)` is discretely concave. Put
`r_n=(1+1/(3n))^(3/2)` and `d_n=w_(n+1)-w_n`. Convexity of
`(1+x)^(3/2)` and the mean value theorem give

\[
r_n-1\ge\frac1{2n},\qquad
r_{n+1}-1\le\frac{\sqrt{1+1/(3n+3)}}{2(n+1)}.
\]

It follows that

\[
\left(\frac{d_{n+1}}{d_n}\right)^2
\le\frac{(3n+1)^3(3n+4)}{81n(n+1)^3}<1. \tag{5}
\]

The final strict inequality follows because denominator minus numerator is
`54n^3+108n^2+42n-4`, which is positive for `n>=1`. Thus `w_n` has a
concave piecewise-linear extension. The indices in `W(a,c)` have arithmetic
mean `max(a,c)`, so Jensen's inequality yields

\[
\boxed{W(a,c)\le\min(a,c)h_{\max(a,c)}^{3/2}.} \tag{6}
\]

The estimates in (4)--(6) hold at every positive integer size. Their use
below does not depend on asymptotic expansions of the gamma function.

## 3. Reducing all four lengths to a rational inequality

The quotient in (2) is invariant under exchanging the two source tensors,
and under simultaneously exchanging their inputs. These operations let us
assume that `a` is a minimum of the four lengths.

Define

\[
\begin{aligned}
m&=\min(b,d),&M&=\max(b,d),\\
\ell&=\min(c,d),&L&=\max(c,d),\\
e&=\min(c,M),&N&=\max(c,M),\\
u&=\min(a+c-1,b+d-1),&v&=\max(a+c-1,b+d-1),\\
X&=2b+a-1,&Y&=2L+\ell-1,&V&=2v+u-1.
\end{aligned}
\]

Here `e>=ell` and `N<=v`. Applying (6) to both weight sums in (1), and
then applying (4), gives

\[
\begin{aligned}
\left(\frac{U}{P_*(a,b)P_*(c,d)}\right)^3
&\le\frac{8a^2m^2 V^3}{X^3Y^3}
      \frac{h_c^3h_M^3}{h_v^3h_a^3h_\ell^3}\\
&=\frac{8a^2m^2 V^3}{X^3Y^3h_a^3}
      \frac{h_N^3}{h_v^3}\frac{h_e^3}{h_\ell^3}\\
&\le\boxed{\frac{8a^2m^2N(3e-1)V^3}
                 {v h_a^3(3\ell-1)X^3Y^3}.} \tag{7}
\end{aligned}
\]

All denominators are positive. For fixed `a`, the assertion that the last
quantity is at most `(97/100)^3` is the polynomial inequality

\[
\Phi_a=
\left(\frac{97}{100}\right)^3 h_a^3
v(3\ell-1)X^3Y^3
-8a^2m^2N(3e-1)V^3\ge0. \tag{8}
\]

When `a>=11`, set `c_11=h_11^3/11`. Equation (4) gives `h_a^3>=c_11 a`.
It therefore suffices to check

\[
\Psi=
\left(\frac{97}{100}\right)^3 c_{11}
v(3\ell-1)X^3Y^3
-8am^2N(3e-1)V^3\ge0. \tag{9}
\]

Equations (8) and (9) are the entire arithmetic content of the tail
certificates. No optimizer output is used as an acceptance decision.

## 4. Exhaustive ordering cones and positive coefficients

There are six possible weak orderings of `b,c,d` above `a`. In each ordering,
write the consecutive gaps as `x,y,z >= 0`. For example, the ordering `bcd`
means

\[
b=a+x,\qquad c=a+x+y,\qquad d=a+x+y+z.
\]

The minimum and maximum symbols in Section 3 are then fixed. When the last
letter is not `c`, one always has `a+c-1 <= b+d-1`. When `c` is last, the
difference between these quantities is `z-x`. Split those two orderings
into two cones:

- `lo`: replace `x` by `x+z`. This covers `z<=x` in the original gaps.
- `hi`: replace `z` by `x+z`. This covers `z>=x` in the original gaps.

This gives eight cones. The substitutions cover every nonnegative gap
triple, including their boundaries; overlapping equality cases cause no
problem.

### Minimum at least eleven

Substitute `a=11+s` and the corresponding gap expressions into (9).
Every coefficient in each of the resulting eight polynomials in
`s,x,y,z` is strictly positive. The verifier records 3,614 nonzero
coefficients across these eight polynomials, all of total degree at most
eight. Positive coefficients imply (9) throughout the nonnegative real
orthant and hence at every required integer point.

### Minimum from two through ten

Fix each `a` in `2,...,10` and substitute the eight cone expressions into
(8). For each of its three gap variables, the verifier finds a threshold
`K<=3` such that replacing that variable by `K+z` makes every coefficient
nonnegative. This produces 216 tail certificates and checks 29,943
nonzero coefficients.

For each fixed minimum and cone, the three certificates cover every point
where at least one gap reaches its associated threshold. All points left
over lie in the explicit finite box with each gap below its threshold.
After duplicate tuples are removed, precisely 37 source tuples remain.
Their largest coordinate is 10. These are the residual tuples of a proved
tail decomposition, not a sample used to infer an all-size claim.

The verifier encloses every `sqrt(h_n^3)` between rationals with denominator
`10^15`, using an integer square root. It substitutes upper endpoints into
(1) cubed. Every residual tuple other than `(2,2,2,2)` has a certified cube
strictly below `(97/100)^3`. Together with the tail certificates, this
proves (3) at every nonexceptional source.

The certificate records each cone, each small-minimum threshold, each
polynomial's number of monomials and minimum coefficient, a hash of the
complete normalized integer coefficient list, and both rational endpoints
for every finite residual. The verifier generates the coefficient lists
directly from (8) and (9); hashes summarize them and are not substitutes
for the positivity checks.

## 5. The sharp exceptional source

At `a=b=c=d=2`,

\[
h_2=\frac43,\qquad h_3=\frac{14}{9},\qquad
P_*(2,2)=\frac{10}{3},\qquad R(3,3)=\frac{18}{7},
\]

and

\[
W(2,2)=1+\frac{14\sqrt{14}}{27}.
\]

Direct substitution into (1) gives the expression `B` in (2). The rational
root enclosures verify

\[
(97/100)^3<(0.974772906)^3<B^3
<(0.974772907)^3<(39/40)^3.
\]

This proves the upper bound, its stated sharpness for `U`, and the unique
equality case. A source with some length equal to one is outside this
theorem: a singleton marginal has zero entropy, and the earlier note uses
a different direct bound there.

## 6. Reproduction and attribution

From the repository root:

```sh
python research/ai/2026-10-20-unequal-entropy/unequal_entropy.py \
  --output results/unequal-entropy-2026-10-20/certificate.json
python -m unittest discover -s tests -p test_unequal_entropy.py -v
```

The maintained verifier uses only the Python standard library. Its exact
controls check the cone decomposition, the polynomial expansion against a
separate scalar formula, all tail certificates, the complete residual
set, and negative-coefficient tampering. The general analytic proof is
Sections 2--5; finite controls do not establish an exponent improvement.

Prior inputs:

- OpenAI, *An Upper Bound of 9/4 for the Matrix Multiplication Exponent*,
  [pinned revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf),
  Sections 4--5: the growth recurrence and external exponent theorem.
- `research/ai/2026-10-20/research_note.md`: the previously constructed
  matching scalar profile. This archive is unchanged.
- `research/ai/2026-10-20-full-filtration/research_note.md`, inspected Git blob
  `3cd953da312bc3c8530cf0b8b0cd481ac8a9fbf3`: the definition of the optimistic
  score, its all-distribution upper certificate `U`, and the prior balanced
  bound. The new result begins with the all-size control of that certificate.

No historical priority claim is made for the elementary recurrence estimates
or the positive-coefficient method. The all-size unequal-source deduction and
its exact certificates were produced in this research session.
