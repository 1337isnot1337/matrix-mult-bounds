# A rank barrier for arbitrary common-input polynomial mixtures

October 23, 2026. Owner-directed Codex research.
Status: written proof, without independent mathematical review or formalization.
No new matrix multiplication exponent is established.

## Result and scope

Fix a common first dimension \(a\).
Consider partial sums of polynomial Full and Mid tensors with this first dimension.
The widths, multiplicities and Full/Mid orientations may differ between all blocks.
Every actual complex degeneration between two such sums preserves every AVZ26
operational potential \(F_\theta^\star\).
Independent invertible first-leg identifications for individual blocks are allowed.

The proof expresses the potential's partial-sum score as a finite nonnegative
linear combination of symmetric-power flattening ranks.
This representation applies to the stated block class.
It does not define \(F_\theta^\star\) on arbitrary tensors.
In particular, this is not a claim about the usual quantum functional.

Shared-output blocks, blocks with smaller first spaces, different source classes,
and different ambient first dimensions remain outside the main theorem.
Section 6 gives a stronger dimension-only statement for identical source blocks.

The construction and profile inputs retain their external attribution.
The boundary-format determinant theorem is due to Gelfand, Kapranov and
Zelevinsky; we use the primary proof of Dionisi and Ottaviani [DO01, Theorem 3.1].
The profile and its concavity are due to Amanov, van den Berg and Zuiddam
[AVZ26, Definition 5.5 and Proposition 5.8].
The rank decomposition and its application here are local deductions.
No historical priority is claimed.

## 1. Tensors, maps and exact conventions

Work over \(\mathbb C\).
Let \(A,B,C\) have dimensions \(a,b,a+b-1\), respectively.
With zero-based coefficient bases, define

\[
\mathrm{Full}_{a,b}
=\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
x_i\otimes y_j\otimes z_{i+j}.
\tag{1}
\]

Define \(\mathrm{Mid}_{a,b}\) by exchanging the last two tensor legs.
Reversing both long-leg coefficient bases gives the middle-product convention
used in the [Pass extension](../2026-10-23-pass-operational-barrier/proof.md).
That coordinate change leaves the common first space unchanged.
The formats are \((a,b,a+b-1)\) and \((a,a+b-1,b)\).

A partial sum shares \(A\), while the second and third spaces are direct sums.
Each block may use an independent invertible identification with \(A\).
Write a typical tensor as

\[
T=\bigoplus_{1,i}\mathrm{Full}_{a,b_i}
\ \oplus_1\ \bigoplus_{1,j}\mathrm{Mid}_{a,d_j}.
\tag{2}
\]

All widths are positive integers.
The index sets are finite and may be empty individually.
At least one block is present in each endpoint.

For \(T\in A\otimes B\otimes C\) and \(q\ge0\), define

\[
\begin{aligned}
\Phi_q(T)&:C^*\otimes\operatorname{Sym}^q A
\longrightarrow B\otimes\operatorname{Sym}^{q+1}A,\\
\Psi_q(T)&:B^*\otimes\operatorname{Sym}^q A
\longrightarrow C\otimes\operatorname{Sym}^{q+1}A.
\end{aligned}
\tag{3}
\]

The maps contract the indicated dual leg and multiply the first factor in
the symmetric algebra.
For example,
\(\Phi_q(T)(\gamma\otimes u)=\sum_r\gamma(c_r)b_r\otimes(a_ru)\)
when \(T=\sum_r a_r\otimes b_r\otimes c_r\).
Their matrix entries depend linearly on the coefficients of \(T\).

Both ranks are invariant under invertible changes of basis on all three legs.
For invertible \(g_A,g_B,g_C\), the transformed \(\Phi_q\) equals
\[
(g_B\otimes\operatorname{Sym}^{q+1}g_A)\,
\Phi_q(T)\,
(g_C^*\otimes\operatorname{Sym}^q(g_A^{-1})).
\]
The corresponding formula holds for \(\Psi_q\).
They cannot increase under a degeneration: the rank upper bounds are defined by minors.
Different long-leg dimensions are compared after adding zero coordinates.
Those coordinates do not change either rank.
These statements also cover restrictions, since singular linear maps are limits
of invertible maps in the padded complex ambient spaces.

For a partial sum (2), both maps are block diagonal on their long legs.
Thus their ranks add, despite the common first space.
An independent first-leg identification does not change a block's rank.

## 2. Exact ranks for one Full or Mid block

Put

\[
H_q=\binom{a+q-1}{q}=\dim\operatorname{Sym}^q A.
\]

**Lemma 1.** For all positive integers \(a,b\) and all \(q\ge0\),

\[
\begin{aligned}
\operatorname{rank}\Phi_q(\mathrm{Full}_{a,b})
&=\min\{(a+b-1)H_q,\ bH_{q+1}\},\\
\operatorname{rank}\Psi_q(\mathrm{Full}_{a,b})&=bH_q.
\end{aligned}
\tag{4}
\]

For Mid, exchange the two displayed ranks.

**Proof.** First suppose \(a,b\ge2\).
In DO01's notation, set

\[
V_0=C,\qquad V_1=B,\qquad V_2=A,\qquad
k_0=a+b-2,\quad k_1=b-1,\quad k_2=a-1.
\]

This is boundary format: \(k_0=k_1+k_2\).
The source tensor is nondegenerate in DO01's Definition 2.1.
Indeed, its map \(B^*\otimes A^*\to C\) is polynomial multiplication.
A product of two nonzero complex polynomials is nonzero.

DO01's Theorem 3.1 identifies the boundary determinant with the determinant of

\[
\partial_T:C^*\otimes\operatorname{Sym}^{b-1}A
\longrightarrow B\otimes\operatorname{Sym}^{b}A.
\]

Here \(m_1=0\) and \(m_2=k_1=b-1\), exactly as required by that theorem.
Nondegeneracy therefore makes \(\partial_T=\Phi_{b-1}(T)\) invertible.
Both dimensions equal
\((a+b-1)\binom{a+b-2}{b-1}=b\binom{a+b-1}{b}\).

View all \(\Phi_q\) as homogeneous components of one graded module map over
\(S=\operatorname{Sym}A\).
If \(q<b-1\), multiply any nonzero kernel element by a nonzero monomial of degree
\(b-1-q\).
The free source module over the polynomial domain \(S\) has no torsion.
This would give a nonzero element in the critical kernel, a contradiction.
Hence \(\Phi_q\) is injective for \(q\le b-1\).

Critical surjectivity gives every element of \(B\otimes S_b\) in the image.
Every homogeneous monomial of degree \(q+1\ge b\) is a product of a degree-\(b\)
monomial and a degree-\(q+1-b\) monomial.
Multiplication commutes with the module map.
Therefore \(\Phi_q\) is surjective for \(q\ge b-1\).
This proves its rank formula.

For \(\Psi_q\), write an input as \(\sum_j y_j^*\otimes u_j\), with \(u_j\in S_q\).
Its image lists the coefficients of

\[
\left(\sum_{i=0}^{a-1}x_i z^i\right)
\left(\sum_{j=0}^{b-1}u_j z^j\right)
\quad\text{in }S[z].
\]

The first factor is nonzero, and \(S[z]\) is an integral domain.
Thus the map is injective.

If \(b=1\), the critical map has \(q=0\) and is the identity between two
\(a\)-dimensional coefficient spaces.
The same propagation proves the first formula without invoking a theorem
on a zero-dimensional projective factor.
If \(a=1\), both maps are a scalar monomial times an identity of size \(b\).
Their ranks are \(b\), which also agrees with (4).
Mid exchanges the long legs. \(\square\)

For \(a\ge2\), an equivalent form of (4) is

\[
\frac{\operatorname{rank}\Phi_{k-1}(\mathrm{Full}_{a,b})}{H_{k-1}}
=b+\frac{a-1}{k}\min(b,k),\qquad
\frac{\operatorname{rank}\Psi_{k-1}(\mathrm{Full}_{a,b})}{H_{k-1}}=b,
\quad k\ge1.
\tag{5}
\]

## 3. The operational score and its finite curvature expansion

Fix positive real parameters

\[
\theta_1+\theta_2+\theta_3=1,\qquad
p_i=\frac{\theta_i}{(1-\theta_j)(1-\theta_k)},
\quad\{i,j,k\}=\{1,2,3\}.
\]

Each \(p_i\) lies strictly between zero and one.
Let \(p=p_1\), and use AVZ26's formal operational potential:

\[
f(b)=F_\theta^\star(P_{a,b,a+b-1})^{1/p},\qquad
g(b)=F_\theta^\star(P_{a,a+b-1,b})^{1/p}.
\tag{6}
\]

The symmetric polynomial conventions agree with (1) after reversing outputs.
AVZ26's partial-sum rule gives

\[
F_\theta^\star(T)^{1/p}=\sum_i f(b_i)+\sum_j g(d_j)=:\mathcal S_\theta(T)
\tag{7}
\]

for the formal expression (2).

AVZ26's Proposition 5.8(ii) makes both sequences concave on positive integers.
For \(g\), exchange \(\theta_2,\theta_3\); this leaves \(p_1\) unchanged.
Set

\[
A=\frac{a-\theta_1}{1-\theta_1},\qquad
L=A^{(1-p)/p},\qquad
\beta_f=L\theta_2(A-1),\qquad
\beta_g=L\theta_3(A-1).
\]

The exact piecewise formula (5.7) in AVZ26 gives affine tails:

\[
\begin{aligned}
f(b)&=Lb+\beta_f
&&\text{if }b\ge\theta_2+(1-\theta_2)A,\\
g(b)&=Lb+\beta_g
&&\text{if }b\ge\theta_3+(1-\theta_3)A.
\end{aligned}
\tag{8}
\]

These are eventual equalities, not asymptotic estimates.
Their intercepts satisfy

\[
\beta_f+\beta_g=L(a-1).
\tag{9}
\]

The endpoint at zero requires a separate check.
Formula (5.7) gives \(f(1)=a^{p_2/p_1}\).
Proposition 5.8(iv) gives \(f(b)\le b\,a^{p_2/p_1}=b f(1)\).
In particular, \(f(2)\le2f(1)\).
The corresponding statements hold for \(g\), with \(p_2\) replaced by \(p_3\).
Consequently, defining \(f(0)=g(0)=0\) preserves discrete concavity.
No external formula at a zero tensor dimension is used.

Define the discrete curvatures

\[
w_k^f=2f(k)-f(k-1)-f(k+1),\qquad
w_k^g=2g(k)-g(k-1)-g(k+1),\quad k\ge1.
\tag{10}
\]

They are nonnegative.
They have finite support by (8).
More precisely, take the ceiling of the larger threshold in (8).
All curvatures beyond that integer vanish.

**Lemma 2.** The following identities hold for every positive integer \(b\):

\[
\begin{aligned}
f(b)&=Lb+\sum_{k\ge1}w_k^f\min(b,k),&
\sum_{k\ge1}k w_k^f&=\beta_f,\\
g(b)&=Lb+\sum_{k\ge1}w_k^g\min(b,k),&
\sum_{k\ge1}k w_k^g&=\beta_g.
\end{aligned}
\tag{11}
\]

**Proof.** Put \(\Delta_n=f(n+1)-f(n)\) for \(n\ge0\).
Then \(w_k^f=\Delta_{k-1}-\Delta_k\), and \(\Delta_n=L\) eventually.
Telescoping gives \(\Delta_n=L+\sum_{k>n}w_k^f\).
Sum this identity for \(0\le n<b\).
The coefficient of \(w_k^f\) is \(\min(b,k)\), proving the first identity.
At a sufficiently large \(b\), compare this identity with the exact affine tail.
This proves the intercept identity.
The proof for \(g\) is identical. \(\square\)

## 4. Arbitrary mixtures preserve the full rectangular family

**Theorem.** Let \(S,T\) be tensors of the form (2), with the same first dimension \(a\).
If \(S\) degenerates to \(T\) over \(\mathbb C\), then

\[
\boxed{F_\theta^\star(S)\ge F_\theta^\star(T)}
\tag{12}
\]

for every positive \(\theta\) of sum one.
Here the potentials are evaluated on the stated block expressions.

**Proof.** Suppose \(a\ge2\).
Write \(W=\sum_i b_i+\sum_j d_j\).
Additivity of the ranks and (5) give

\[
\begin{aligned}
\frac{\operatorname{rank}\Phi_{k-1}(T)}{H_{k-1}}
&=W+\frac{a-1}{k}\sum_i\min(b_i,k),\\
\frac{\operatorname{rank}\Psi_{k-1}(T)}{H_{k-1}}
&=W+\frac{a-1}{k}\sum_j\min(d_j,k).
\end{aligned}
\]

Substitute these formulas in (11).
Equations (9) and (11) cancel the remaining coefficient of \(W\).
The resulting identity is

\[
\boxed{
\mathcal S_\theta(T)
=\sum_{k\ge1}\frac{k w_k^f}{(a-1)H_{k-1}}
\operatorname{rank}\Phi_{k-1}(T)
+\sum_{k\ge1}\frac{k w_k^g}{(a-1)H_{k-1}}
\operatorname{rank}\Psi_{k-1}(T).
}
\tag{13}
\]

Both sums are finite.
Every coefficient is nonnegative and depends only on \(a,\theta,k\).
It does not depend on the block widths or multiplicities.
Each rank is nonincreasing under the actual degeneration.
Thus \(\mathcal S_\theta(S)\ge\mathcal S_\theta(T)\).
Raising positive quantities to \(p>0\) proves (12).

If \(a=1\), both block types have format \((1,b,b)\), and \(f(b)=g(b)=b\).
Their partial sum is a matrix of rank \(\sum b\).
Ordinary rank monotonicity proves the claim. \(\square\)

Adjoining these actual rules to AVZ26's formal system preserves its rectangular barrier.
The potential comparison also persists under the original formal combination rules.
This does not show that the new rules follow from the earlier formal rules.
The theorem rules out a potential improvement from changing only Full/Mid widths,
multiplicities, or independent first-leg bases at fixed common first dimension.

## 5. A misleading balancing candidate and its exact rejection

For every \(a\ge2\), consider

\[
\mathrm{Full}_{a,a-1}\oplus_1\mathrm{Full}_{a,a+1}
\quad\dashrightarrow\quad
2\odot_1\mathrm{Full}_{a,a}.
\tag{14}
\]

Both long dimensions agree: \((2a,4a-2)\).
Every nonzero first slice has rank \(2a\) on both sides.
The [existing shared-input Koszul formula, equation (2)](../2026-10-20-koszul/research_note.md)
also gives equal ranks in every exterior degree.
Its exact source hash appears in [sources.json](sources.json).
Indeed, its breakpoints are at most \(a-1\), and all widths in (14) exceed or equal that value.

Nevertheless, the symmetric operational score strictly increases.
At \(\theta=(1/3,1/3,1/3)\), write

\[
G(a,b)=\left(\frac{3m-1}{2}\right)^{1/3}
\left(M+\frac{m-1}{2}\right),\qquad
m=\min(a,b),\quad M=\max(a,b).
\]

The target-minus-source score is positive because

\[
(3a-1)(3a-3)^3-(3a-4)(3a-2)^3=6a-5>0.
\tag{15}
\]

This compares the cubes of the two positive terms after collecting the common tail factor.
It is not a construction.
At symmetric degree \(q=a-1\), the target's \(\Phi_q\) rank exceeds the source's by

\[
\boxed{\frac{a-1}{a}\binom{2a-2}{a-1}>0.}
\tag{16}
\]

Thus the proposed degeneration is impossible.
For \(a=2\), the ranks are \(11\) and \(12\).
This example explains why dimensions, ordinary slice ranks and shared-leg Koszul
screens alone can suggest an invalid escape.

## 6. A dimension-only theorem for heterogeneous targets

The following statement does not need DO01 or any symmetric-power rank test.
Suppose the source consists of \(c\) identical \(\mathrm{Full}_{a,B}\) blocks.
Let the target contain arbitrary Full widths \(b_i\) and Mid widths \(d_j\).
Assume only the two necessary dimension inequalities:

\[
\begin{aligned}
\sum_i b_i+\sum_j(d_j+a-1)&\le cB,\\
\sum_i(b_i+a-1)+\sum_jd_j&\le c(B+a-1).
\end{aligned}
\tag{17}
\]

Then \(\mathcal S_\theta(T)\le c f(B)\) for every positive \(\theta\).
This excludes an improving profile before any tensor-map search.

For \(a>1\), take the right supporting slope
\(r=f(B+1)-f(B)\), and put \(h=f(B)-Br\).
Equation (11) gives

\[
r=L+\sum_{k>B}w_k^f\ge L,\qquad
h=\sum_{k\le B}k w_k^f\in[0,\beta_f].
\]

Concavity gives \(f(b)\le rb+h\) for every positive integer \(b\).
Define

\[
\mu=\frac{h}{a-1},\qquad \lambda=r-\mu.
\]

Both are nonnegative: \(\beta_f<L(a-1)\le r(a-1)\).
The affine-tail upper bound \(g(b)\le Lb+\beta_g\) follows from (11).
Using (9), it gives

\[
\begin{aligned}
f(b)&\le\lambda b+\mu(b+a-1),\\
g(b)&\le\lambda(b+a-1)+\mu b.
\end{aligned}
\tag{18}
\]

For the second inequality, its right side minus \(Lb+\beta_g\) equals
\((r-L)(b+a-1)+\beta_f-h\), which is nonnegative.
The first bound is an equality at the source width \(B\).
Multiply (17) by \(\lambda,\mu\) and add.
This proves the assertion.
For \(a=1\), both scores equal their widths and the result is immediate.
Exchanging the long legs proves the identical-Mid-source version.

## Verification and remaining construction question

The accompanying standard-library verifier checks integer coefficient matrices,
critical determinants, exact curvature identities and the balancing rejection.
Modular full rank is used only to certify full rank over \(\mathbb Q\), hence \(\mathbb C\).
Exact radical intervals certify finite signs; floating-point comparisons do not decide acceptance.
The finite controls do not replace the imported determinant theorem or the all-size proof.

The saved report records 160 literal coefficient matrices and 12 critical integer determinants.
It also checks 240 exact profile expansions and 1400 mixed-orientation rank decompositions.
Of 6225 heterogeneous formats, 2291 satisfy both dimensions; all preserve the symmetric score.
These last finite controls specialize to the symmetric parameter.
The written argument supplies the general positive-parameter statement.

~~~sh
python -m unittest discover -s tests -p test_common_input_rank_barrier.py -v
python research/ai/2026-10-23-common-input-rank-barrier/verify.py \
  --output results/common-input-rank-barrier-2026-10-23/verification.json
~~~

The constructive search must now leave the fixed-dimension Full/Mid class.
Shared-output blocks are one concrete possibility.
Survival of dimension or rank screens would remain a necessary-condition result,
with an explicit tensor degeneration still required.

