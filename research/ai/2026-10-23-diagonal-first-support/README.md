# First-support repair from the diagonal of the first map

For ordinary maps from the paired source to a near-full width-four
matrix target, a fixed polynomial product **on the diagonal alone**
forces a linear first-support repair cost. Off-diagonal values may have
arbitrary bilinear perturbations that vanish on the diagonal.

At \(n=200,c=1\), the bound is **188** when the two diagonal factor
maps are injective, and **176** without that assumption. These are
necessary first-flattening-rank costs. They do not exclude all linear
repairs or give a smaller matrix multiplication exponent.

## 1. Statement and scope

Let \(k\) be any field, \(n>c\ge0\) integers, and \(r=n-c\).
Use the source convention

\[
Q(n,4)=\sum_{p,q<n}\sum_{y,v<4}
 A_{pq}B_{y,q+v}C_{p+y,v}.
\]

Suppose ordinary linear maps give

\[
(A\otimes B\otimes C)Q(n,4)+E=M(r,4,r),\qquad
e=r_A(E).                                                   \tag{1}
\]

Identify the two outer target spaces by fixed bases. Write the dual
first map as \(L:\mathrm{Mat}_r(k)\to\mathrm{Mat}_n(k)\).
Let \(P_d\) denote binary homogeneous forms of degree \(d\), and
identify the source coefficient space with \(P_{n-1}\otimes P_{n-1}\).
The variables \(x,y\) below each stand for a separate binary pair.

Assume the **coefficient identity in the parameters \(u\)**

\[
L(uu^{\mathsf T})(x,y)=H(x,y)F(u)(x)G(u)(y),                 \tag{2}
\]

where \(H\ne0\) has fixed bidegree \((d_x,d_y)\),
\(0\le d_x,d_y\le n-1\), and

\[
F:k^r\to P_{n-1-d_x},\qquad G:k^r\to P_{n-1-d_y}
\]

are linear. The identity is polynomial, so it persists after scalar
extension. It is not a conclusion inferred from sampled finite-field
points. Apart from linearity and (2), no condition is imposed on
off-diagonal values. In particular, an arbitrary bilinear term
\(T(u,v)\) with \(T(u,u)=0\) is allowed. In characteristic two,
diagonal vanishing is the relevant condition; skew symmetry alone
does not state it.

Define

\[
\begin{split}
\kappa&=4(c+3),& a_0&=\max(0,n-5c-7),\\
\tau(e)&=\max\{d\in\mathbb Z_{\ge0}:d(d+1)/2\le e\},&
q(e)&=\max\{d\in\mathbb Z_{\ge0}:d(d+1)\le e\},\\
b(e)&=\max\{\tau(e)-6,q(e)\}.&&
\end{split}                                                \tag{3}
\]

**Theorem.** Every ordinary identity (1) satisfying (2) obeys

\[
e+b(e)\ge a_0.                                             \tag{4}
\]

If both \(F,G\) are injective, then

\[
e\ge a_0.                                                 \tag{5}
\]

Thus the general integer lower bound is
\(\min\{j\in\mathbb Z_{\ge0}:j+b(j)\ge a_0\}\). At \(a_0=188\),
\(175+b(175)=187\) while \(176+b(176)=188\), proving the
stated bound 176. Equation (5) gives 188.

This is a theorem about **ordinary exact maps with the specified
diagonal identity**. It does not cover arbitrary diagonal maps,
arbitrary first maps, or Laurent degenerations. Both conclusions leave
repairs of linear border rank open. Claim
`AI-DIAGONAL-FIRST-SUPPORT-001` remains written and unreviewed.

## 2. Imported source and incidence facts

The [preceding support-capacity package](../2026-10-23-first-support-capacity/README.md)
supplies the following inputs, pinned at commit
`7690348a792c5734d6f00d7fa7a9e6ce8dc37daa` in [sources.json](sources.json).
Its mathematical proof was already present at `66c4636`.

1. If \(e<r\), both ordinary source long maps are surjective. Their
   dimensions are \(4(n+3)\to4r\), so both kernels have dimension
   \(\kappa\).
2. The native slice of a nonzero coefficient matrix \(Y\) satisfies
   \(\operatorname{rank}S_Y\ge\operatorname{rank}Y+15\ge16\).
   The field-independent proof and source convention are prior work.
3. For \(Y=Hfg\ne0\), its two source slice images lie in

   \[
   k^4\otimes gP_{d_y+3},\qquad fP_{d_x+3}\otimes k^4.
                                                               \tag{6}
   \]

   These are containing spaces; no equality or exact raw rank sixteen
   is asserted for nonconstant \(H\).
4. Over an algebraic closure, for a fixed \(\kappa\)-dimensional
   kernel \(K\), the projective divisor stratum

   \[
   D_{K,j}=\{[f]:\dim(K\cap(fP_m\otimes k^4))\ge j\}
   \]

   is closed and has dimension at most \(\kappa-j\). The factors
   are reversed for the other source leg. Multiplication has constant
   rank, making the intersection condition determinantal. The incidence
   with \(\mathbf P(K)\) has finite divisor fibers, including in
   positive characteristic. The classical fiber-dimension step retains
   its attribution to the Stacks Project,
   [tag 0B2L](https://stacks.math.columbia.edu/tag/0B2L).
5. Two-sided matrix compression satisfies

   \[
   \operatorname{rank}(BSC^{\mathsf T})\ge\operatorname{rank}S
   -\dim(\operatorname{im}S\cap\ker B)
   -\dim(\operatorname{im}S^{\mathsf T}\cap\ker C).             \tag{7}
   \]

The earlier package also proves a Laurent support theorem. Only its
ordinary surjectivity consequence is used here. The subsequent exact
slice and diagonal arguments do not acquire a Laurent interpretation
from that input.

## 3. Residual-free points on the Veronese

It suffices to prove the bounds when \(e<r\). If \(e\ge r\),
then \(a_0\le r\) and \(b(e)\ge0\), so both conclusions are
automatic. Under \(e<r\), the long kernels have dimension \(\kappa\).

Extend scalars to an algebraic closure. Matrix ranks and the dimensions
of linear kernels are unchanged, while (1) and (2) continue to hold.
Let \(W=\ker E_A\subset\mathrm{Mat}_r\), the annihilator of the
first support of \(E\). It has codimension \(e\). The projective
set

\[
Z=\{[u]\in\mathbf P^{r-1}:uu^{\mathsf T}\in W\}              \tag{8}
\]

is cut out by \(e\) homogeneous quadrics. Equivalently, it is the
intersection of the quadratic Veronese with \(\mathbf P(W)\).
The Veronese is a closed embedding over every field: the coordinates
include all \(u_i u_j\), not just the squares. The projective
dimension theorem, in the Stacks Project
[tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R), gives

\[
Z\ne\varnothing,\qquad \dim Z\ge r-1-e.                    \tag{9}
\]

No regular-sequence or smoothness hypothesis is imposed. Some of the
quadrics can be dependent or zero, including in characteristic two;
this only increases the lower dimension bound. Over finite fields,
the argument concerns geometric points after scalar extension.

For \([u]\in Z\), the residual contraction vanishes, and the target
contraction has rank four. Thus

\[
BS_{L(uu^{\mathsf T})}C^{\mathsf T}=M_{uu^{\mathsf T}},
\qquad L(uu^{\mathsf T})\ne0.                               \tag{10}
\]

In particular, \(Z\) avoids \(\mathbf P(\ker F)\) and
\(\mathbf P(\ker G)\). More generally, \(L\) is injective on
\(W\): zero source contraction and zero residual contraction force
zero target contraction. Therefore

\[
\dim\ker L\le e.                                          \tag{11}
\]

## 4. Diagonal factor deficiencies use first-support capacity

Put \(d_F=\dim\ker F\) and \(d_G=\dim\ker G\). If a nonzero
\(u\) belonged to both kernels, (2) and polarization by subtraction
would make \(L\) vanish on

\[
uu^{\mathsf T},\qquad uv^{\mathsf T}+vu^{\mathsf T}
\quad(v\text{ in a fixed complement of }ku).
\]

These span an \(r\)-dimensional space. Choosing a basis with first
vector \(u\) makes independence immediate. No division by two is
used. This contradicts (11) and \(e<r\). Hence

\[
\ker F\cap\ker G=0.                                       \tag{12}
\]

For any subspace \(K\), let \(\mathcal S(K)\) be the actual span
of the tensors \(vv^{\mathsf T}\), \(v\in K\). If \(\dim K=d\),
its independent basis consists of

\[
e_i e_i^{\mathsf T},\qquad
e_i e_j^{\mathsf T}+e_j e_i^{\mathsf T}\quad(i<j).
\]

The second kind is obtained by expanding \((e_i+e_j)(e_i+e_j)^{\mathsf T}\)
and subtracting the diagonal terms. Thus \(\dim\mathcal S(K)=d(d+1)/2\)
over every field, including characteristic two. This is a subspace of
\(K\otimes K\), not an appeal to a characteristic-dependent
identification of symmetric quotients.

Equation (2) kills both \(\mathcal S(\ker F)\) and
\(\mathcal S(\ker G)\). They intersect trivially by (12), as can
also be seen in a basis extending the direct sum of the two kernels.
Together with (11), this gives the joint budget

\[
\frac{d_F(d_F+1)}2+\frac{d_G(d_G+1)}2\le e.                 \tag{13}
\]

This is stronger than two separate deficiency bounds and is the
reason the general numerical consequence is 176.

## 5. A closed bad union for every threshold split

Choose an integer \(1\le j\le12\). Use threshold \(j\) for the
\(F\)-side divisor stratum associated with \(\ker C\), and
threshold \(13-j\) for the \(G\)-side stratum associated with
\(\ker B\). Their dimensions are bounded by
\(\kappa-j\) and \(\kappa-13+j\).

Pull these loci back along the linear maps \(F,G\), including their
kernel loci by taking inverse images of affine cones and then
projectivizing. This makes the inverse images closed even where the
projective linear map is undefined. Away from its kernel, the
projective map induced by \(F\) has fibers of dimension \(d_F\).
Its inverse image therefore has dimension at most

\[
\max(d_F-1,d_F+\kappa-j)=d_F+\kappa-j.                      \tag{14}
\]

The other bound is \(d_G+\kappa-13+j\). These estimates also hold
if the stratum misses the image of the parameter map: only the kernel
locus remains. Since \(\kappa\ge12\), all thresholds are at most
\(\kappa\), so (14) has no negative-dimension endpoint problem.

If a point of \(Z\) avoided both inverse images, its raw slice in
(10) would have rank at least sixteen. The two kernel intersections
would have dimensions at most \(j-1\) and \(12-j\), whose sum
is eleven. By (7), the compressed rank would be at least five. This
contradicts (10). Thus \(Z\) is contained in the closed bad union,
and (9) implies, for every such \(j\),

\[
r-1-e\le\kappa+\max(d_F-j,d_G-13+j).                        \tag{15}
\]

In the injective case, choose \(j=6\). Equation (15) becomes
\(r-1-e\le\kappa-6\), proving (5).

## 6. Exact optimization of the joint deficiency budget

For nonnegative integers \(a,b\), set

\[
h(a,b)=\max\left\{a-6,b-6,\left\lfloor\frac{a+b}{2}\right\rfloor\right\}.
\]

The elementary identity

\[
\min_{1\le j\le12}\max(a+6-j,b-7+j)=h(a,b)                 \tag{16}
\]

has no parity exception. Each maximum is at least \(a-6\),
\(b-6\), and the ceiling of \((a+b-1)/2\), which is
\(\lfloor(a+b)/2\rfloor\). Conversely, an integer \(j\) can
be chosen in

\[
[1,12]\cap[a+6-h,h+7-b].                                   \tag{17}
\]

This interval is nonempty because \(h\ge a-6\), \(h\ge b-6\),
and \(2h\ge a+b-1\). Equations (15) and (16) give

\[
e+h(d_F,d_G)\ge r-\kappa+5.                                \tag{18}
\]

Under (13), each deficiency is at most \(\tau(e)\). Also, putting
\(s=\lfloor(d_F+d_G)/2\rfloor\), convexity of the triangular
numbers gives

\[
s(s+1)\le
\frac{d_F(d_F+1)}2+\frac{d_G(d_G+1)}2\le e.
\]

Hence \(s\le q(e)\), and \(h(d_F,d_G)\le b(e)\).
Substitution in (18), together with nonnegativity, proves (4).

The scalar budget maximum is exact. If \(q(e)\) dominates, the
feasible pair \((q(e),q(e))\) attains \(b(e)\). If \(\tau(e)-6\)
dominates, the pair \((\tau(e),0)\) attains it: the budget bound
already gives \(\lfloor\tau(e)/2\rfloor\le q(e)\le\tau(e)-6\).
This is only sharpness of the integer optimization in (13); it does
not assert that tensor maps attain the resulting repair bound.

## 7. An injective shift-transpose example and its diagonal

Let \(r=n-1\ge2\). Define \(J_0,J_1:k^r\to k^{r+1}\) by
\(J_0e_i=e_i\), \(J_1e_i=e_{i+1}\), and set

\[
L_*(X)=J_0XJ_0^{\mathsf T}+J_1X^{\mathsf T}J_1^{\mathsf T}.  \tag{19}
\]

Its top-left entries are

\[
[L_*(X)]_{ij}=X_{ij}+X_{j-1,i-1},                           \tag{20}
\]

with negative indices interpreted as zero. The transpose in the
second summand is essential to this indexing. Ordering coordinates
by \(i+j\) makes the top-left projection unit triangular. Equivalently,
it is \(I+N\) with \(N^r=0\). Thus \(L_*\) is injective over
every field, with a determinant-one \(r^2\)-square minor.

For a pure input,

\[
L_*(uv^{\mathsf T})=(J_0u)(J_0v)^{\mathsf T}
                    +(J_1v)(J_1u)^{\mathsf T},
\]

so its rank is at most two everywhere on the Segre. Yet
\(L_*(E_{ii})=E_{ii}+E_{i+1,i+1}\), which has rank two. These
matrices also show that the whole image space has zero common left
and right kernels, and spans every row and column direction. Over
characteristic zero, \(L_*(I_r)=\operatorname{diag}(1,2,\ldots,2,1)\)
has rank \(n\). Low rank on the Segre therefore does not imply low
rank on its linear span or force a single product map.

For the binary form \(f_u\) of degree \(n-2\) with coefficients
\(u\), the diagonal is

\[
L_*(uu^{\mathsf T})=(x_0y_0+x_1y_1)f_u(x)f_u(y).             \tag{21}
\]

After dehomogenization, this is \((1+xy)f_u(x)f_u(y)\).
Thus the injective case of the theorem applies to any actual ordinary
realization with this diagonal, giving \(e\ge\max(0,n-12)\).
At \(n=200\) it rules out first residual below 188.

For a concrete allowed off-diagonal change, add

\[
(u_0v_1-u_1v_0)I_n.
\]

This term vanishes on the diagonal in every characteristic, including
two. At \(u=e_0,v=e_1\), the new output is
\(I_n+E_{01}+E_{21}\), which is invertible since the added matrix
squares to zero. The diagonal theorem therefore permits behavior
far beyond the full product-first-map class.

No long maps implementing a matrix target are supplied by these
examples. They are controls for the first-map hypotheses and a
counterexample to a naive rank-only structural inference. The theorem
uses the two shared source long kernels to obtain its obstruction.

## 8. Verification and remaining question

[verify.py](verify.py) reconstructs the unit triangular minors,
diagonal polynomial identities, a genuine diagonal-vanishing change,
characteristic-two square and cross spaces, native source controls,
and the exact threshold optimization. It checks local source hashes
before accepting [certificate.json](certificate.json). Altered
coefficients, altered source pins and altered or incomplete certificates
are rejected. [VERIFICATION.md](VERIFICATION.md) records the completed
finite scope and its limits.

These controls do not prove the universal projective dimension theorem
or divisor-incidence bounds. The written proof above uses those
explicitly credited inputs. Same-session review is not independent
mathematical review or formalization.

The next ordinary construction must change the diagonal form (2),
accept the stated repair cost, or supply another justified structure.
Singular Laurent families remain outside this theorem. No exponent
improvement is claimed.
