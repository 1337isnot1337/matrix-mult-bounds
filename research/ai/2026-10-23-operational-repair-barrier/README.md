# A subquadratic repair barrier for the existing formal operations

October 23, 2026. Written AI-derived deduction with same-session agent
checks; no independent mathematical review or Lean formalization.
**This is a barrier for a specified formal calculus. It does not exclude
actual tensor degenerations and does not improve the matrix multiplication
exponent.**

Fix an integer width `b >= 2`. A derivation within the formal preorder of
Amanov--van den Berg--Zuiddam cannot produce a near-full target
`M(l_n,b,r_n)` from `Q(n,b)` and `O(n^alpha)` scalar repair terms for any
fixed `alpha < 2`, when `l_n/n` and `r_n/n` tend to one. For fixed outer
defects, a more precise necessary repair bound is

\[
\liminf_{n\to\infty}\frac{s_n\ln n}{n^2}
\ \geq\ \frac{1}{e}\ln\frac{b^2}{2b-1}.
\tag{1}
\]

Every logarithm in this note is the natural logarithm. At width four the
right side lies strictly between `0.304118051531` and `0.304118051532`.
Section 4 permits outer defects of order `n/ln n` as well. Section 5
proves that the coefficient in (1) is optimal over the entire external
`F_theta` family, including parameters approaching the simplex corners.
This does not assert optimality over all formal monotones or establish
that a formal repair construction attains the necessary bound.

## 1. Imported result and formal-expression conventions

The external input is Alimzhan Amanov, Maxim van den Berg and Jeroen
Zuiddam, [*Multiplying matrices via polynomials: exposition and barriers*,
arXiv:2610.30054v1](https://arxiv.org/html/2610.30054v1), submitted October
21, 2026. Definition 5.3 specifies a preorder on formal expressions, and
Definition 5.5 defines positive functions `F_theta`. Proposition 5.9 proves
their monotonicity for that preorder. They add on full direct sums and
multiply on tensor products. The preorder contains the paper's polynomial
rank, separation, concavity and tripling ingredients, together with the
stated restrictions, isomorphisms and combination rules. We import this
result, including its scope, rather than proving it here.

Write `T <=_op S` for precisely that formal preorder. The functions are
defined on expressions; the paper does not assert that they are invariants
of tensors or monotone under every degeneration. Its Definition 5.5
explicitly makes this distinction. The local contribution below evaluates
these external functions on the repository's paired expressions and
derives repair-cost consequences.

Let `P_(a,b,a+b-1)` denote the polynomial multiplication expression, and
use the particular paired expression

\[
Q(n,b)=P_{n,b,n+b-1}\otimes P_{n,n+b-1,b}.
\tag{2}
\]

After fixed reversals of each polynomial-output coordinate, it represents
the repository's existing coefficient tensor

\[
\sum_{i,k=0}^{n-1}\sum_{y,v=0}^{b-1}
A_{i,k}B_{y,k+v}C_{i+y,v},
\]

with leg dimensions `(n^2,b(n+b-1),b(n+b-1))`. The target convention is

\[
M(l,h,r)=\sum_{i<l,\ j<h,\ k<r}a_{i,k}b_{i,j}c_{j,k},
\]

with leg dimensions `(lr,lh,hr)`. As a formal expression, take
`P_(r,1,r) tensor P_(l,l,1) tensor P_(1,h,h)`.
This is the paper's `<r,l,h>`, after the fixed dot-product coordinate
reversals and grouping the product coordinates.
The middle width therefore has the first dot-product exponent. Using the
paper's literal `<l,h,r>` would put that exponent on the wrong dimension.
The existing [integral restriction note](../2026-10-20-paired-construction/outer_product_injection.md)
supplies the coefficient convention; its constructions are unchanged.

Let `I_s` be a direct sum of `s` scalar units, so `F_theta(I_s)=s`.
When `s=0`, omit this summand. Scalar repair means this precise formal
source. An arbitrary auxiliary tensor's actual border rank is not a
permitted substitute unless its rank bound is also derived within the
formal preorder.

## 2. The finite repair inequality

Choose a real parameter `1 < p < 2` and set

\[
\theta=\left(\frac{2-p}{p},\frac{p-1}{p},\frac{p-1}{p}\right).
\]

The three external dot-product exponents specialize to

\[
(\pi_1,\pi_2,\pi_3)=\left(p(2-p),\frac p2,\frac p2\right).
\tag{3}
\]

For the generator with dimensions `(n,b,n+b-1)`, the transformed input
dimensions in Definition 5.5 are

\[
A_n=\frac{pn-(2-p)}{2(p-1)},\qquad
B=1+p(b-1).
\]

The branch `B <= A_n` is exactly

\[
n-1\geq2(p-1)(b-1).
\tag{4}
\]

In particular, `n >= 2b-1` suffices uniformly for `1 < p < 2`.
This sufficient condition is not necessary. For example, `n=6,b=4,p=7/4`
satisfies (4), whereas `p=19/10` does not.

In this branch, direct substitution into the generator formula gives

\[
F_p(P_{n,b,n+b-1})
= B^{1-p/2}\bigl(n+(2-p)(b-1)\bigr)^{p/2}.
\]

Indeed, the second factor inside Definition 5.5 is
`theta_1 B+(1-theta_1) A_n = n+(2-p)(b-1)`.
The second and third entries of `theta` are equal, so the second paired
generator has the same value. Multiplicativity and (3) now give

\[
\begin{aligned}
F_p(Q(n,b))
  &= [1+p(b-1)]^{2-p}[n+(2-p)(b-1)]^p,\\
F_p(M(l,h,r))
  &= (lr)^{p/2}h^{p(2-p)}.
\end{aligned}
\tag{5}
\]

**Finite necessary condition.** If positive integer dimensions satisfy
(4), and a formal relation

\[
M(l,h,r)\leq_{\rm op}Q(n,b)\oplus I_s
\tag{6}
\]

holds, then

\[
s\geq (lr)^{p/2}h^{p(2-p)}
       -[1+p(b-1)]^{2-p}[n+(2-p)(b-1)]^p.
\tag{7}
\]

This follows by applying the imported monotone to (6), using (5) and
additivity, and subtracting the source value. It holds separately for
every permitted `p`; a parameter may depend on `n`.

A common formal tensor catalyst cancels from this argument because its
value is positive. The same bound holds in the formal asymptotic closure:
apply multiplicativity to a tensor power and take its root to remove a
scalar factor of size `2^o(k)`. This is also the closure considered in the
external paper's Example 5.10. Neither observation extends (7) to
arbitrary actual degenerations.

## 3. Every fixed subquadratic repair is excluded in this calculus

For `b > 1` and `1 < p < 2`, define

\[
D_b(p)=b^{p(2-p)}-[1+p(b-1)]^{2-p}.
\tag{8}
\]

Strict convexity of `x^p` gives its strict tangent inequality at one:

\[
b^p>1+p(b-1).
\]

Raising both positive sides to `2-p` proves `D_b(p)>0` at every size and
parameter in the stated range. This is an all-size argument, not a
conclusion from the finite checks.

Suppose (6), with `h=b`, holds along an unbounded sequence and
`l_n/n -> 1`, `r_n/n -> 1`. For any fixed `p` in `(1,2)`, (4) eventually
holds. Divide (7) by `n^p` and pass to a lower limit:

\[
\liminf\frac{s_n}{n^p}\geq D_b(p)>0.
\tag{9}
\]

For any fixed `alpha < 2`, choose `max(1,alpha) < p < 2`.
Equation (9) contradicts `s_n=O(n^alpha)`. Fixed nonnegative outer defects
`l_n=n-c_l`, `r_n=n-c_r` give the more precise expansion

\[
s_n\geq D_b(p)n^p-O_{b,p,c_l,c_r}(n^{p-1}).
\]

The statement is about formally derived repairs. It does not change the
existing [conditional actual-degeneration criterion](../2026-10-21-correction-budget/superlinear_budget.md),
which uses actual complex tensor characters and remains a valid open
construction route. In particular, the external formal functionals used
here are not additional actual characters to insert into that argument.

## 4. The logarithmic lower bound and outer-dimension losses

Put

\[
A=\ln\frac{b^2}{2b-1}>0,\qquad L=\ln n.
\]

Assume `0 < l_n,r_n <= n` and define the logarithmic product deficit

\[
\delta_n=\ln\frac{n^2}{l_n r_n}\geq0.
\]

Suppose, for some finite `alpha >= 0`,

\[
\limsup L\delta_n\leq\alpha.
\tag{10}
\]

Then any family of formal relations (6), with `h=b`, must satisfy

\[
\boxed{\displaystyle
\liminf\frac{s_n\ln n}{n^2}
\geq A\exp\left(-1-\frac{\alpha}{A}\right).}
\tag{11}
\]

**Proof.** Fix `t > 0` and use the permitted moving parameter
`p_n=2-t/L`. It lies in `(1,2)` and satisfies (4) for all sufficiently
large `n`. Write `epsilon=t/L`. The target in (5), divided by `n^p`, is

\[
\exp\left(-\frac p2\delta_n+p\epsilon\ln b\right),
\]

and the similarly normalized source is

\[
\exp\left(
\epsilon\ln[1+p(b-1)]
+p\ln\left[1+\frac{\epsilon(b-1)}n\right]\right).
\]

Condition (10) gives `delta_n=O(1/L)`. Taylor expansion at zero is uniform
under this bound. Thus the target minus source, after multiplication by
`L/n^p`, is

\[
t\bigl(2\ln b-\ln(2b-1)\bigr)-L\delta_n+o(1)
=tA-L\delta_n+o(1).
\]

Since `n^p=n^2 exp(-t)`, (7) implies

\[
\liminf\frac{s_nL}{n^2}\geq e^{-t}(tA-\alpha).
\]

The right side is maximized at `t=1+alpha/A`, where its value is the
right side of (11). This proves the claim.

Fixed nonnegative defects give `L delta_n -> 0`, recovering (1).
More generally, if

\[
l_n=n-\kappa_l\frac n{\ln n}+o\left(\frac n{\ln n}\right),\qquad
r_n=n-\kappa_r\frac n{\ln n}+o\left(\frac n{\ln n}\right),
\]

with nonnegative `kappa_l,kappa_r`, then one may take
`alpha=kappa_l+kappa_r`. Every finite such loss retains a positive
coefficient in (11). For unrestricted `o(n)` losses, Section 3 still
excludes every fixed subquadratic power; it does not alone provide a
positive constant at the finer scale `n^2/ln n`.

## 5. Sharpness over the entire external parameter family

Let `theta=(u,v,w)` be any positive triple of sum one. Write
`pi_1=u/[(1-v)(1-w)]`, and define `pi_2,pi_3` cyclically, as in the
external paper. These exponents lie in `(0,1)`. For `1<=l,r<=n`, put

\[
G_\theta(n,l,r)
=F_\theta(M(l,b,r))-F_\theta(Q(n,b)).
\]

We prove the uniform finite upper bound

\[
\boxed{\displaystyle
\sup_\theta G_\theta(n,l,r)
\leq\frac{A}{e}\frac{n^2}{\ln(n/b^2)}\qquad(n>b^2).}
\tag{12a}
\]

The supremum includes every permitted parameter, without a condition
such as (4). The symmetric choice from Section 4 attains the resulting
asymptotic upper bound. Therefore, for fixed nonnegative outer defects,

\[
\lim_{n\to\infty}\frac{\ln n}{n^2}
\sup_\theta G_\theta(n,n-c_l,n-c_r)=\frac A e.
\tag{12}
\]

This concerns the strength of the imported family of necessary repair
certificates. It does not prove that `n^2/ln n` formal repair is
sufficient, or that every formal monotone has this limitation.

### 5.1. A source lower bound valid in both generator branches

Set

\[
A_n=1+\frac{n-1}{1-u},\qquad
B_2=1+\frac{b-1}{1-v},\qquad
B_3=1+\frac{b-1}{1-w}.
\]

We claim

\[
F_\theta(P_{n,b,n+b-1})\geq n^{\pi_2}B_2^{1-\pi_2}.
\]

When `A_n>=B_2`, the generator formula is
`B_2^(1-pi_2)[n+u(B_2-1)]^pi_2`, which proves the claim.
When `A_n<B_2`, put `z=B_2/A_n>1`. The generator formula becomes
`A_n[v+(1-v)z]^pi_1`. Weighted AM-GM and the exponent identity

\[
v+(1-v)z\geq z^{1-v},\qquad
\pi_1(1-v)=1-\pi_2+u\pi_2\geq1-\pi_2
\]

give a lower bound `A_n*z^(1-pi_2)`. This equals
`A_n^pi_2*B_2^(1-pi_2)` and is at least the claimed bound, since `A_n>=n`.
Interchanging legs two and three and multiplying gives

\[
F_\theta(Q(n,b))\geq n^{\pi_2+\pi_3}C,\qquad
C=B_2^{1-\pi_2}B_3^{1-\pi_3}.
\tag{12b}
\]

### 5.2. A uniform entropy-ratio inequality

Define

\[
\epsilon=2-\pi_2-\pi_3>0,\qquad
H=\pi_1\ln b-(1-\pi_2)\ln B_2-(1-\pi_3)\ln B_3.
\]

We will use the two inequalities

\[
0<H\leq A\epsilon,\qquad \pi_1\leq2\epsilon.
\tag{12c}
\]

Put `x=1-v`, `y=1-w`, so `0<x,y<1` and `x+y>1`, and define

\[
\phi(z)=\frac{\ln b}{z}-\ln\left(1+\frac{b-1}{z}\right).
\]

Direct substitution gives

\[
\frac H\epsilon
=\frac{x(1-y)\phi(x)+y(1-x)\phi(y)}{x(1-y)+y(1-x)}.
\]

The function `phi` vanishes at one and is strictly decreasing, since

\[
z^2\phi'(z)=-\ln b+\frac{(b-1)z}{z+b-1}
\leq-\ln b+\frac{b-1}{b}<0.
\]

Thus the displayed weighted average is positive. By symmetry, assume
`x<=y`. If `x>=1/2`, both entries in that average are at most
`phi(1/2)=A`. If `x<1/2`, fix x and decrease y to its boundary value
`1-x`. This increases the average: the weight on the larger value
`phi(x)` has derivative `-x(1-x)/(x+y-2xy)^2<0` with respect to y,
and `phi(y)` also decreases with y.

At `y=1-x`, the ratio becomes

\[
\frac{\ln b-f(x)-f(1-x)}{x^2+(1-x)^2},\qquad
f(z)=z^2\ln\left(1+\frac{b-1}{z}\right).
\]

The function f is strictly convex. Indeed, with
`t=(b-1)/(z+b-1)` in `(0,1)`,

\[
f''(z)=-2\ln(1-t)-2t-t^2
=2\sum_{k=3}^\infty\frac{t^k}{k}>0.
\]

Consequently the numerator is at most `A/2`, while the denominator is
at least `1/2`. This proves `H/epsilon<=A`.
For the second inequality in (12c), direct substitution gives

\[
\frac{\pi_1}{\epsilon}=\frac{2-x-y}{x+y-2xy}\leq2.
\]

To verify the last step, write `s=x+y` in `(1,2)` and use
`3s-4xy>=3s-s^2>=2`. These arguments cover parameters arbitrarily
close to the simplex boundary and corners.

### 5.3. Optimizing the uniform upper bound

The target is at most `n^(2-epsilon)*b^pi_1`. Combining (12b)--(12c),

\[
G_\theta(n,l,r)
\leq n^{2-\epsilon}b^{\pi_1}(1-e^{-H})
\leq A\epsilon b^{2\epsilon}n^{2-\epsilon}.
\]

For `L'=ln(n/b^2)>0`, the right side is
`A*n^2*epsilon*exp(-epsilon*L')`, whose maximum over all positive
epsilon is `A*n^2/(e*L')`. This proves (12a). The moving symmetric
parameter from Section 4 gives the matching lower limit in (12).

### 5.4. Sharpness with logarithmic outer losses

Let `delta=ln[n^2/(lr)]>=0` and
`Delta=pi_3*ln(n/l)+pi_2*ln(n/r)`. Since each of `pi_2,pi_3` is at
least `1-epsilon`, we have `Delta>=(1-epsilon)delta`.
The exact target value and (12b) give

\[
G_\theta(n,l,r)
\leq n^{2-\epsilon}b^{\pi_1}(e^{-\Delta}-e^{-H}).
\]

For nonnegative H and Delta,
`[exp(-Delta)-exp(-H)]_+ <= [H-Delta]_+`, where `[z]_+=max(z,0)`.
Applying (12c) and this inequality yields

\[
\max(G_\theta,0)
\leq n^2e^{-\epsilon L'}[(A+\delta)\epsilon-\delta]_+.
\]

The scalar maximum occurs at
`epsilon=1/L'+delta/(A+delta)`. Allowing all nonnegative epsilon
enlarges the range of actual parameters, so it gives the valid bound

\[
\boxed{\displaystyle
\sup_\theta\max(G_\theta,0)
\leq\frac{n^2(A+\delta)}{eL'}
\exp\left(-\frac{\delta L'}{A+\delta}\right).}
\tag{12d}
\]

If `delta_n*ln n -> alpha<infinity`, its normalized limit is
`A*exp(-1-alpha/A)`. Section 4 attains that coefficient with
`p_n=2-(1+alpha/A)/ln n`. Thus the coefficient is optimal over the
entire external family whenever this scaled deficit has a limit.
The necessary lower bound (11) still needs only its stated upper-limit
hypothesis; convergence is used here for the matching sharpness claim.

## 6. Exact finite evidence and reproduction

For `p=a/q` in lowest terms, the program raises both sides of the
no-repair comparison in (7) to `2q^2` and clears denominators. Its exact
acceptance comparison is

\[
q^{4q^2}(lr)^{aq}h^{2a(2q-a)}
>
[q+a(b-1)]^{2q(2q-a)}
[qn+(2q-a)(b-1)]^{2aq}.
\tag{13}
\]

The common positive power preserves order. Integer root intervals also
give certified lower bounds when scalar repair is nonzero. These are
expression-value tests; no coefficient maps are supplied.

| Formal source | Target | Parameter | Exact conclusion |
| --- | --- | --- | --- |
| `Q(8,4)` | `M(8,4,8)` | `15/8` | At least one scalar repair is necessary |
| `Q(20,4)` | `M(19,4,19)` | `8/5` | At least three scalar repairs are necessary |
| `Q(29,4)` | `M(27,4,27)` | `3/2` | At least two scalar repairs are necessary |
| `Q(6,4)` | `M(5,4,5)` | `7/4` | This parameter gives no exclusion |
| `Q(8,1)` | `M(8,1,8)` | `15/8` | Exact equality; the strict theorem requires `b>1` |

The first strict row has the compact independent witness
`2^774 > 53^8 * 67^120`. The third has
`2^8 * 27^6 * 4^3 > 11^2 * 61^6`.
A passing row is not evidence that the formal relation or an actual
degeneration exists. In particular, the open `Q(6,4)` target is not closed
by the displayed control.

The logarithmic coefficient uses a rational enclosure for `ln(x)` from
its atanh series, with a positive geometric tail bound, and an enclosure
for `e` from its factorial series. Powers of two reduce logarithm
arguments to `[1,2]`, so near-corner parameters also receive narrow
enclosures. No floating-point value decides an acceptance condition.
There are 1,395 finite positivity controls: widths
2 through 32 and the 45 reduced parameters in `(1,2)` with denominator
at most 12. Six exact generator comparisons cover both branches and a
width-one equality. Twenty-one entropy controls cover widths 2, 4 and 8
at seven simplex points, including coordinates of size `10^-12`.
The all-size convexity and limit arguments are written proofs, not
consequences of those checks.

For completeness, if `x>=1` and `z=(x-1)/(x+1)`, the logarithm enclosure
uses

\[
0\leq\ln x-2\sum_{k=0}^{N-1}\frac{z^{2k+1}}{2k+1}
\leq\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

Each tail denominator is at least `2N+1`, so the upper bound follows from
a geometric series. The other enclosure is

\[
0<e-\sum_{k=0}^{N}\frac1{k!}
\leq\frac{N+2}{(N+1)(N+1)!}.
\]

The ratios after the first omitted term are at most `1/(N+2)`. Dividing
the positive logarithm interval by the positive `e` interval gives the
reported rational bracket. The program uses `N=32` for width four.

From the repository root, using only the Python standard library:

```sh
python -m unittest discover -s tests -p 'test_operational_repair_barrier.py' -v
python research/ai/2026-10-23-operational-repair-barrier/barrier.py --output research/ai/2026-10-23-operational-repair-barrier/certificate.json
```

The eleven focused tests check the leg convention, direct substitution into
the external generator formula, the exact branch, strict finite witnesses,
nonzero scalar repairs, negative and equality controls, root enclosures,
the natural-logarithm constant, both uniform source branches, the entropy
inequalities near simplex corners, and the uniform finite envelope against
an asymmetric generator value. The saved certificate records completed
coverage. The external monotonicity theorem and the analytic proof are
not formally verified by this program.

## Attribution and limits

The external functions and their formal monotonicity belong to
Amanov--van den Berg--Zuiddam. The paired source, target conventions and
actual correction criteria are prior repository work. The evaluations,
subquadratic repair deduction, logarithmic coefficient, dimension-loss
refinement, all-parameter sharpness and exact replay were developed in
this owner-directed session.
A separate agent in the same session checked the formulas and supplied
the logarithmic-deficit formulation and uniform sharpness proof; two
other agents checked that proof in the same session. This is not independent external
mathematical review, and no historical priority is claimed.

Any successful actual family with the existing useful correction budget
must introduce a relation outside the specified formal calculus. The
calculus test identifies that requirement; it does not remove the open
construction problem or establish a lower bound on omega.
