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
Section 4 permits outer defects of order `n/ln n` as well. The coefficient
in (1) is sharp for the one-parameter functional family used here; no
optimality over all formal monotones or actual tensor constructions is
asserted.

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

## 5. Sharpness of this one-parameter bound for fixed defects

For fixed nonnegative `c_l,c_r`, let `G_n(p)` be the right side of (7)
with target `M(n-c_l,b,n-c_r)`. For large `n`, all `p` in `(1,2)` satisfy
(4), and

\[
G_n(p)\leq n^pD_b(p).
\]

Set `epsilon=2-p`. The function in (8) extends smoothly to
`epsilon in [0,1]`, and its Taylor expansion is

\[
D_b(2-\epsilon)=A\epsilon+O_b(\epsilon^2).
\]

A uniform upper remainder bound `C_b epsilon^2` therefore exists on this
compact interval. For `L=ln n`,

\[
\frac L{n^2}G_n(p)
\leq A L\epsilon e^{-L\epsilon}
     +C_b L\epsilon^2e^{-L\epsilon}
\leq\frac A e+\frac{4C_b}{e^2L}.
\]

The choice `epsilon=1/L` in Section 4 attains the limiting coefficient
`A/e`. Consequently

\[
\lim_{n\to\infty}\frac{\ln n}{n^2}
\sup_{1<p<2}G_n(p)=\frac A e.
\tag{12}
\]

Thus optimizing this family cannot add an unbounded logarithmic factor
to (1). This does not prove that `n^2/ln n` repair is sufficient, or that
other formal monotones have the same limitation.

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
for `e` from its factorial series. No floating-point value decides an
acceptance condition. There are 1,395 finite positivity controls: widths
2 through 32 and the 45 reduced parameters in `(1,2)` with denominator
at most 12.
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

The seven focused tests check the leg convention, direct substitution into
the external generator formula, the exact branch, strict finite witnesses,
nonzero scalar repairs, negative and equality controls, root enclosures,
and the natural-logarithm constant. The saved certificate records completed
coverage. The external monotonicity theorem and the analytic proof are
not formally verified by this program.

## Attribution and limits

The external functions and their formal monotonicity belong to
Amanov--van den Berg--Zuiddam. The paired source, target conventions and
actual correction criteria are prior repository work. The evaluations,
subquadratic repair deduction, logarithmic coefficient, dimension-loss
refinement and exact replay were developed in this owner-directed session.
A separate agent in the same session checked the formulas and supplied
the logarithmic-deficit formulation. This is not independent external
mathematical review, and no historical priority is claimed.

Any successful actual family with the existing useful correction budget
must introduce a relation outside the specified formal calculus. The
calculus test identifies that requirement; it does not remove the open
construction problem or establish a lower bound on omega.
