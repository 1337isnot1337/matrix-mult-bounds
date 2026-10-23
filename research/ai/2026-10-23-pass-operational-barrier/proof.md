# Pass packings preserve the polynomial operational barrier

October 23, 2026. Owner-directed Codex research.
Status: written proof, without independent review or formalization.
No matrix multiplication exponent improvement is established.

## Question and attribution

Pass [PASS26, Lemmas 2.4–2.5] constructs primal and dual polynomial packings.
Amanov, van den Berg and Zuiddam [AVZ26, Theorem 5.4] prove an operational
barrier for a specified system of polynomial tensor operations.
This note proves that every Pass packing preserves their barrier functions.
The same conclusion holds for the full rectangular family of barrier functions.

The new argument uses their discrete concavity and eventual affine formulas.
It does not reconstruct either external proof or claim priority for this consequence.
The exact source versions and inspection scope appear in [sources.json](sources.json).
The repository already credits Pass in `PROVENANCE.md` and its
[`2026-10-21-pass-packing` note](../2026-10-21-pass-packing/).
This note adds the comparison with AVZ26's full rectangular potential family.

## 1. Conventions

Let \(a,b,c,t\) be positive integers and put \(s=a+b-1\).
The tensor \(\mathrm{Full}_{a,b}\) multiplies polynomials of lengths \(a,b\).
Its format is \((a,b,s)\).
The tensor \(\mathrm{Mid}_{a,b}\) takes coefficients \(a-1,\ldots,a+b-2\)
from a product of lengths \(a,s\).
Its format is \((a,s,b)\).

In AVZ26's symmetric notation these are \(P_{a,b,s}\) and \(P_{a,s,b}\).
The identification reverses the output coordinates in each block.
It leaves the common first coordinates unchanged.
Indeed, the zero-based Full relation \(i+j-k=0\) becomes
\(i+j+k=s-1\) after reversal.
The Mid relation \(i+j-k=a-1\) gives the same sum after its output reversal.

Write \(\oplus_1\) for a partial direct sum with a common first leg.
Each block has independent second and third coordinates.
Write \(c\odot_1 T\) for \(c\) identical blocks in this partial sum.
Pass's primal rule is

\[
c\odot_1\mathrm{Full}_{a,b+t}
\ \longrightarrow\
((c+1)\odot_1\mathrm{Full}_{a,b})
\oplus_1\mathrm{Mid}_{a,b},
\qquad ct\ge a+2b-1. \tag{1}
\]

The dual rule exchanges Full and Mid throughout.
The arrow denotes source-to-target degeneration.

## 2. External inputs and parameter domain

Fix

\[
\theta_i>0,\qquad \theta_1+\theta_2+\theta_3=1,\qquad
p_i=\frac{\theta_i}{(1-\theta_j)(1-\theta_k)}
=\frac{\theta_i}{\theta_i+\theta_j\theta_k},
\quad \{i,j,k\}=\{1,2,3\}.
\]

Thus \(0<p_i<1\).
The function \(F_\theta^\star\) is defined on formal expressions
[AVZ26, Definition 5.5].
It is additive on direct sums and multiplicative on tensor products.
Its partial-sum rule is

\[
F_\theta^\star(S\oplus_\ell T)
=\left(F_\theta^\star(S)^{1/p_\ell}
+F_\theta^\star(T)^{1/p_\ell}\right)^{p_\ell}. \tag{2}
\]

This function is not asserted to be a tensor character.
Monotonicity applies to AVZ26's specified formal preorder, not all tensor degenerations.

Set \(p=p_1\) and

\[
f(b)=F_\theta^\star(P_{a,b,a+b-1})^{1/p},\qquad
g(b)=F_\theta^\star(P_{a,a+b-1,b})^{1/p}.
\]

Both sequences are concave on the positive integers
[AVZ26, Proposition 5.8(ii)].
For \(g\), exchange \(\theta_2,\theta_3\) and the corresponding tensor legs.
This exchange does not change \(p_1\).
No value at zero is needed.

Put

\[
A=\frac{a-\theta_1}{1-\theta_1},\qquad L=A^{(1-p)/p}>0.
\]

AVZ26's formula (5.7) gives

\[
\begin{aligned}
f(b)&=L\bigl(b+\theta_2(A-1)\bigr)
&&\text{if }b\ge\theta_2+(1-\theta_2)A,\\
g(b)&=L\bigl(b+\theta_3(A-1)\bigr)
&&\text{if }b\ge\theta_3+(1-\theta_3)A.
\end{aligned} \tag{3}
\]

Each threshold is finite, so both sequences have an affine tail.
Their common slope is \(L\).
The two intercepts sum to \(L(a-1)\), because
\((\theta_2+\theta_3)(A-1)=a-1\).

## 3. Extension theorem

**Lemma.** Suppose a real sequence \(h(n)\), \(n\ge1\), is concave.
Suppose \(h(n)=Ln+\beta\) for every sufficiently large integer \(n\).
Then

\[
h(n+t)-h(n)\ge Lt,\qquad h(n)\le Ln+\beta
\quad(n,t\ge1). \tag{4}
\]

**Proof.** Concavity makes the consecutive differences nonincreasing.
Every sufficiently late difference equals \(L\).
Every earlier difference is therefore at least \(L\).
Summing \(t\) differences proves the first inequality.
Choose a sufficiently large integer \(N>n\).
Then \(h(N)-h(n)\ge L(N-n)\), which proves the second inequality. \(\square\)

**Theorem.** Every Pass primal and dual rule (1) preserves every
\(F_\theta^\star\) for \(\theta_i>0\) with sum one.

**Proof.** Apply (4) separately to \(f\) and \(g\), using (3).
This gives

\[
f(b+t)-f(b)\ge Lt,\qquad
g(b+t)-g(b)\ge Lt,\qquad
f(b)+g(b)\le L(a+2b-1).
\]

The condition \(ct\ge a+2b-1\) now gives

\[
c\bigl(f(b+t)-f(b)\bigr)
\ge cLt\ge L(a+2b-1)\ge f(b)+g(b).
\]

Hence

\[
\boxed{c f(b+t)\ge(c+1)f(b)+g(b).} \tag{5}
\]

The dual inequality follows by exchanging \(f,g\).
Rule (2) identifies these with the required potential comparisons.
All powers used here are positive. \(\square\)

**Operational consequence.** Extend AVZ26's preorder by every rule (1),
its dual and every simultaneous permutation of the legs.
Retain the original combination rules.
The new rules can also occur inside a compatible partial sum.
Their unchanged common first map permits this insertion.

Every \(F_\theta^\star\) remains monotone.
Equation (2) preserves inequalities when another fixed partial summand is added.
Direct sums, tensor products and transitivity also preserve inequalities.
Thus AVZ26's Proposition 5.7 gives the same full rectangular barrier.
In particular, the extended system cannot derive a square bound below \(9/4\).
Tensoring a rule with a fixed matrix multiplication tensor does not alter this conclusion.
Its potential is a common positive multiplicative factor.

The rectangular boundary case uses limits through positive \(\theta\).
No formula at \(\theta_i=0\) is required.
This proof does not assume that Pass's rules follow syntactically from AVZ26's earlier rules.
It also does not exclude new rules that violate these formal potentials.

## 4. Exact symmetric comparison and equality

At \(\theta=(1/3,1/3,1/3)\), put

\[
G(a,b)=F^\star(P_{a,b,a+b-1})^{4/3}
=\left(\frac{3m-1}{2}\right)^{1/3}
\left(M+\frac{m-1}{2}\right),
\quad m=\min(a,b),\quad M=\max(a,b).
\]

This formula comes from AVZ26's equation (5.3).
The following direct argument also proves the symmetric case.
For real \(1\le b<a\),

\[
\frac{d}{db}\log\frac{G(a,b)}{a+2b-1}
=\frac{1}{3b-1}+\frac{1}{2a+b-1}
-\frac{2}{a+2b-1}
=\frac{2(a-b)^2}
{(3b-1)(2a+b-1)(a+2b-1)}.
\tag{6}
\]

For \(b\ge a\), the ratio in (6) is constant.
It is continuous at \(b=a\).
Thus, for positive integer \(t\),

\[
\boxed{\frac{G(a,b+t)}{G(a,b)}
\ge\frac{a+2b+2t-1}{a+2b-1}.} \tag{7}
\]

Equality holds exactly when \(b\ge a\).
If \(b<a\), the interval of integration contains a positive-length interval with strictly positive derivative.

Combining (7) with \(ct\ge a+2b-1\) proves

\[
(c+2)G(a,b)\le cG(a,b+t).
\]

Equality holds exactly when \(b\ge a\) and \(ct=a+2b-1\).
The case \(a=1\) is included.

The comparison requires no numerical radicals:

\[
G(a,b)^3=\frac{(3m-1)(2M+m-1)^3}{16}. \tag{8}
\]

Cubing positive quantities preserves their order.
The verifier uses integer numerators in (8).

## 5. Homogeneous target mixtures and the two flattenings

Consider any proposed degeneration

\[
c\odot_1\mathrm{Full}_{a,b+t}
\longrightarrow
(u\odot_1\mathrm{Full}_{a,b})
\oplus_1(v\odot_1\mathrm{Mid}_{a,b}),
\tag{9}
\]

where \(u,v\ge0\) are integers and \(u+v>0\).
The target has independent long-leg coordinates between blocks.
It is concise on those legs.
Consequently, its two flattening dimensions give necessary conditions

\[
c(b+t)\ge ub+v(a+b-1),\qquad
c(a+b+t-1)\ge u(a+b-1)+vb. \tag{10}
\]

These conditions hold for arbitrary local maps and arbitrary degeneration order.
They do not require a fixed first map.

Adding (10) gives

\[
\frac{u+v}{c}
\le\frac{a+2b+2t-1}{a+2b-1}
\le\frac{G(a,b+t)}{G(a,b)}, \tag{11}
\]

where the last step is (7).
Thus every dimension-compatible format (9) preserves the symmetric potential.
This statement covers all positive \(a,b\), including \(b<a\).
The dual-source statement follows by exchanging the long legs.

For Pass's \(u=c+1,v=1\), both inequalities (10) reduce to
\(ct\ge a+2b-1\).
Its minimum source cost therefore saturates both flattenings.
Shorter sources fail conciseness, irrespective of the chosen decoder.

This is a square operational barrier for the stated homogeneous formats.
It does not assert rectangular-potential monotonicity for every choice of \(u,v\).
It does not exclude heterogeneous target sizes or a different source.
A new same-shaped construction can exist without violating this barrier.

## 6. Verification and limits

The standard-library verifier expands the numerator identity (6) exactly.
It also evaluates 13,824 ratio comparisons and 27,648 admissible Pass boundary cases.
The homogeneous census covers 21,875 specified formats.
Every acceptance decision uses integer arithmetic.
The saved report gives the exact ranges, counts and named controls.

Six focused tests verify normalization, equality, strictness, both flattenings,
invalid inputs and the complete recorded finite controls.
The shortened \((a,b,c,t)=(2,2,4,1)\) control fails both flattenings.
The exact \((2,2,5,1)\) control saturates both.

Run from the repository root:

~~~sh
python research/ai/2026-10-23-pass-operational-barrier/verify.py
python -m unittest discover -s tests -p test_pass_operational_barrier.py -v
~~~

The all-parameter result rests on Sections 2–5.
The finite checks do not establish that result or the external concavity theorem.
This package constructs no new tensor maps and proves no smaller exponent.

## Sources

- **AVZ26.** Alimzhan Amanov, Maxim van den Berg and Jeroen Zuiddam.
  [arXiv:2610.30054v1](https://arxiv.org/html/2610.30054v1),
  October 21, 2026. Definitions 5.1–5.5, Proposition 5.7,
  Proposition 5.8(ii), equations (5.3), (5.7), and Theorem 5.4.
- **PASS26.** Rafael Pass.
  [arXiv:2610.28627v1](https://arxiv.org/html/2610.28627v1),
  October 20, 2026. Lemmas 2.4–2.5.

Both external proofs retain their authors' credit.
The discrete-tail extension and homogeneous dimension argument are local written derivations.
No external mathematical review or historical-priority claim is made.
