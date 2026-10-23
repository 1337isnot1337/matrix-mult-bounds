# Repair support capacity and polynomial first maps

**Status: written proofs with exact finite controls and a separate agent's
same-session proof check; no independent mathematical review.**

This package gives two different necessary conditions for repairing an
actual tensor image to matrix multiplication. The first applies to
arbitrary maps, including formal Laurent maps whose poles cancel. The
second applies to ordinary paired-source maps with a specified polynomial
form on the first leg and arbitrary maps on the other two legs.

Neither theorem constructs a matrix target, excludes arbitrary paired
degenerations, or improves the matrix multiplication exponent. A first
flattening rank is used throughout; it is not the tensor's slice rank.

## 1. Results and scope

Write

\[
M(l,h,r)=\sum_{i<l,\alpha<h,j<r}
 a_{ij}\otimes b_{i\alpha}\otimes c_{\alpha j}.
\]

Its first space is identified with \(k^l\otimes k^r\). For a tensor
\(E\), let \(\operatorname{supp}_A(E)\) be its smallest first-leg
support and let \(r_A(E)=\dim\operatorname{supp}_A(E)\).

**Support-capacity theorem.** Suppose local maps give

\[
T(t)+E(t)=M(l,h,r)+tJ(t),\qquad
J(t)\in(A\otimes B\otimes C)[[t]],                 \tag{1}
\]

where \(T(t)\) and \(E(t)\) are images of fixed source tensors and
can individually have poles. Put \(e=r_A(E)\) for the auxiliary
source. If the two long maps on \(T\) have ranks \(a_B,a_C\) over
\(k((t))\), then

\[
\boxed{e\ge lr-\lfloor a_B/h\rfloor\lfloor a_C/h\rfloor.} \tag{2}
\]

A stronger version uses the coefficient-column and coefficient-row spans
of the limiting long-map annihilators. If those dimensions are
\(w_B,w_C\), then

\[
\boxed{e\ge rw_B+lw_C-w_Bw_C.}                    \tag{3}
\]

Both statements hold over every field, and ordinary identities are
included. In particular, \(e<\min(l,r)\) forces both long maps on
\(T\) to be surjective over \(k((t))\). This does not assert that
their coefficients are regular or their values at zero are surjective.

**Polynomial-first-map theorem.** Set \(r=n-c\), where \(c\ge0\)
and \(n>c\) are integers. Consider an ordinary identity

\[
Q(n,4)_{\rm image}=M(r,4,r)-E',\qquad e=r_A(E').   \tag{4}
\]

Assume the dual first map has the form

\[
L(u\otimes v)=H(x,y)F(u)(x)G(v)(y),               \tag{5}
\]

with a fixed nonzero bihomogeneous polynomial \(H\) and the
degree-compatible linear maps specified in Section 6. Source-variable
transposition is also allowed. The two long maps are arbitrary. Then

\[
e\ge\min\{n-c,\max(0,2n-10c-14)\}.              \tag{6}
\]

\[
e\ge\max(0,2n-10c-19).                           \tag{7}
\]

Use the larger of these two lower bounds. They hold over every field.
Equation (6) forces \(e\ge n-c\) when \(n\ge9c+14\). For
\(c=1\), this threshold is \(n=23\). At \(n=200,c=1\), (7)
requires \(e\ge371\). The special case \(H=1\) includes every
product first map. Nonseparable multipliers such as the homogeneous
version of \(1+xy\) are included as well.

Equations (6)-(7) require the ordinary identity (4) and the fixed form
(5). They do not apply to arbitrary first maps, sums of different
multiplier-product first maps, or Laurent degenerations. The linear
lower bound leaves repairs of linear border rank open.

## 2. Specializing a moving subspace without losing dimension

For a \(d\)-dimensional subspace \(V\subset k((t))^m\), its
regular vectors have a \(k[[t]]\)-basis with linearly independent
constant coefficients. Let \(V_0\) be the span of those coefficients.
Then \(\dim V_0=d\), and every regular vector in \(V\) specializes
into \(V_0\).

Choose an \(m\)-by-\(d\) basis matrix over \(k((t))\). Among
its nonzero maximal coordinate minors, choose one of least valuation,
with row set \(I\). Right multiplication by its inverse makes the
\(I\) rows the identity. Every other entry becomes a signed ratio of
a maximal minor to the chosen minor and is therefore regular. The
resulting columns have independent constant coefficients. The
coefficients of any regular vector in this basis are its \(I\)
coordinates, so they are regular too. This proves the assertion.

The case \(d=0\) is immediate. This construction is the saturated
subspace limit; taking the constant coefficients of an arbitrary
Laurent basis would not give the same guarantee.

## 3. The union of the two forced first supports

Let \(S(t)=\operatorname{supp}_A(E(t))\), of dimension at most
\(e\), and let

\[
K_B(t)=\operatorname{ann}\operatorname{im}B_T(t),\qquad
K_C(t)=\operatorname{ann}\operatorname{im}C_T(t).
\]

Apply Section 2 to these three spaces, obtaining limits
\(S_0,K_{B,0},K_{C,0}\). For \(f\in K_{B,0}\), write its
coefficients in the \(b_{i\alpha}^*\) basis as an \(l\)-by-\(h\)
matrix \(F_f\). Define

\[
W_B=\sum_{f\in K_{B,0}}\operatorname{col}(F_f)\subset k^l.
\]

For \(g\in K_{C,0}\), use the \(h\)-by-\(r\) coefficient
matrix \(G_g\) and define

\[
W_C=\sum_{g\in K_{C,0}}\operatorname{row}(G_g)\subset k^r.
\]

Lift \(f\) to a regular \(f(t)\in K_B(t)\). Contracting (1) on
the second leg kills \(T(t)\) exactly and gives

\[
E(t)\mathbin{\lrcorner}f(t)
 =(M+tJ(t))\mathbin{\lrcorner}f(t).
\]

This contraction is regular, even if \(E(t)\) itself has a pole.
Each of its first-leg coefficient vectors lies in \(S(t)\); hence
its constant coefficients lie in \(S_0\). Direct contraction of
the displayed formula for \(M\) shows that its first support is
\(\operatorname{col}(F_f)\otimes k^r\). Varying \(f\), and
then performing the analogous third-leg contractions, gives

\[
W_B\otimes k^r+k^l\otimes W_C\subset S_0.        \tag{8}
\]

Choose complements to \(W_B,W_C\). Their tensor-product
decomposition shows that the intersection of the two summands in (8)
is \(W_B\otimes W_C\). Thus their sum has dimension
\(rw_B+lw_C-w_Bw_C\), proving (3).

This argument does not assume separate regularity of the two summands,
bounded coefficients of the local maps, or a fixed first support for
\(E(t)\). Only the total identity (1) is regular.

## 4. Consequences of the support-capacity theorem

Since \(K_{B,0}\subset W_B\otimes(k^h)^*\) and has dimension
\(lh-a_B\),

\[
w_B\ge l-\lfloor a_B/h\rfloor.
\]

Similarly \(w_C\ge r-\lfloor a_C/h\rfloor\). The expression in
(3) increases in each variable throughout \([0,l]\times[0,r]\),
so substitution proves (2). It also gives the individual bounds

\[
a_B\ge h(l-\lfloor e/r\rfloor),\qquad
a_C\ge h(r-\lfloor e/l\rfloor).                 \tag{9}
\]

In particular a first-support repair of size \(O(n)\) for a square
target with outer dimensions \(n-O(1)\) allows only \(O(1)\)
long-map deficiency. If both long maps are nonsurjective for a square
outer dimension \(r\), (3) implies \(e\ge2r-1\).

If the source long dimensions are only known to be \(m_B,m_C\), then

\[
e\ge lr-
 \min(l,\lfloor m_B/h\rfloor)
 \min(r,\lfloor m_C/h\rfloor).                  \tag{10}
\]

Each long dimension of \(Q(n,b)\) is \(b(n+b-1)\). For the target
\(M(n-c,4,n-c)\), (10) becomes

\[
e\ge(n-c)^2-
 \min\left(n-c,\left\lfloor\frac{b(n+b-1)}4\right\rfloor\right)^2.
                                                               \tag{11}
\]

For fixed \(b<4\) this is
\((1-b^2/16)n^2+O_{b,c}(n)\). Such source widths therefore cannot
provide a subquadratic first-support repair, even through (1). At
\(n=200,c=1\), the bounds for \(b=1,2,3,4\) are respectively
\(37101,29601,16800,0\).

### An attained structural bound

The product oblique maps from the separately pinned PR147 have bad
outer modes \(J\), of size \(d=r-b\). Their long annihilators are

\[
\langle b_{i0}^*,b_{i2}^*:i\in J\rangle,\qquad
\langle c_{0j}^*,c_{1j}^*:j\in J\rangle.
\]

Both coefficient spans have dimension \(d\). Therefore (3) gives
\(e\ge2rd-d^2=r^2-b^2\), exactly their constructed residual's
first flattening rank. This observation concerns those annihilator
spaces. It does not classify arbitrary long maps. The verifier
reconstructs their explicit annihilator bases without needing that
unmerged package on disk.

### A pole-cancellation control

For \(M(2,1,2)\), abbreviate the long bases by \(b_0,b_1,c_0,c_1\).
The following two images sum exactly to the target:

\[
\begin{split}
T(t)&=t^{-1}a_{01}(b_0+tb_1)(c_0+tc_1),\\
E(t)&=(a_{00}-t^{-1}a_{01})b_0c_0
      +(a_{10}-a_{01})b_1c_0
      +(a_{11}-ta_{01})b_1c_1.                   \tag{12}
\end{split}
\]

The source of \(E(t)\) has first rank three. The saturated first
support specializes to \(\langle a_{01},a_{10},a_{11}\rangle\).
The long annihilators \(-tb_0^*+b_1^*\) and
\(-tc_0^*+c_1^*\) force the row-one and column-one supports, whose
union has dimension three. Both summands in (12) have poles; their
annihilator contractions are regular. This realizes equality in (3)
with the pole-cancellation feature used in the proof.

## 5. Ordinary exact slices and a necessary low-rank locus

Use the literal paired-source convention

\[
Q(n,b)=\sum_{p,q<n}\sum_{y,v<b}
 A_{pq}B_{y,q+v}C_{p+y,v}.                       \tag{13}
\]

For an \(n\)-by-\(n\) coefficient matrix \(X\), its slice is

\[
S_X[(y,z),(w,v)]=X_{w-y,z-v},                   \tag{14}
\]

where out-of-range entries are zero. The prior source-slice theorem,
credited and byte-pinned in `sources.json`, states

\[
\operatorname{rank}S_X\ge\operatorname{rank}X+b^2-1
\quad\text{for }X\ne0.                         \tag{15}
\]

For completeness, let \(g_p(t)=\sum_qX_{pq}t^q\), and let \(W\)
be their span, of dimension \(s=\operatorname{rank}X\). The last
\(B\) row block has rank
\(\dim(W+tW+\cdots+t^{b-1}W)\ge s+b-1\): each new translate
contains a polynomial of larger degree than those already present.
If \(p_0\) is the first nonzero row, adding the other row blocks in
descending order adds at least \(b\) ranks per block. Indeed the
columns \((p_0+y,v)\), \(0\le v<b\), vanish in all earlier
blocks and give the independent shifts of \(g_{p_0}\) in the new
block. The sum is \(s+b-1+(b-1)b=s+b^2-1\).
For a pure coefficient matrix the two polynomial-multiplication
families are each independent, so the slice has rank exactly \(b^2\).
This proof works over every field.

Now assume an ordinary identity (4) with \(c=1\), arbitrary first
map, and \(e<r=n-1\). Both long maps are surjective and have
sixteen-dimensional kernels. Set
\(Z=\operatorname{ann}\operatorname{supp}_A(E')\subset\mathrm{Mat}_r\).
For \(x\in Z\), the dual first map satisfies

\[
B S_{L(x)}C^{\mathsf T}=x\otimes I_4.            \tag{16}
\]

It is injective on \(Z\). Two-sided compression loses at most
thirty-two ranks, so a nonzero rank-one \(x\in Z\) obeys

\[
\operatorname{rank}S_{L(x)}\le36,\qquad
\operatorname{rank}L(x)\le21.                   \tag{17}
\]

For every nonzero \(u\), the vectors \(v\) with \(u\otimes v\in Z\)
form a space of dimension at least \(r-e\), and their nonzero
images satisfy (17). These are necessary conditions, not a
classification of the raw rank-at-most-thirty-six locus. In particular
they do not force pure source coefficients.

Only the generic long-map surjectivity statement extends automatically
to (1). The exact slice equality (16) does not: higher Laurent orders
can raise generic slice ranks and first-map lifts can have poles.

## 6. Fixed-polynomial first maps and divisor strata

Let \(P_d\) denote homogeneous binary forms of degree \(d\), of
dimension \(d+1\). In (5), \(x\) and \(y\) denote two separate
pairs of homogeneous variables. Let \(H\ne0\) have bidegree
\((d_x,d_y)\), where \(0\le d_x,d_y\le n-1\), and take

\[
F:k^r\longrightarrow P_{n-1-d_x},\qquad
G:k^r\longrightarrow P_{n-1-d_y}.                \tag{18}
\]

The output of (5) belongs to \(P_{n-1}\otimes P_{n-1}\), identified
with the source coefficient space in (13). Multiplication by a
nonzero \(H\) is injective, hence

\[
\operatorname{rank}L=\operatorname{rank}F\operatorname{rank}G.
                                                               \tag{19}
\]

For nonzero \(F(u),G(v)\), the raw slice has rank at least sixteen
by (15). Its two slice images are contained in

\[
V_{G(v)}=k^4\otimes G(v)P_{d_y+3},\qquad
V_{F(u)}=F(u)P_{d_x+3}\otimes k^4.               \tag{20}
\]

Each component on the appropriate side is divisible by \(G(v)\) or
\(F(u)\). For nonconstant \(H\), (20) gives containing spaces;
neither equality nor raw rank exactly sixteen is required.

### Divisor-stratum lemma

Work over an algebraic closure. Let \(K\) be a \(\kappa_K\)-dimensional
subspace of \(k^4\otimes P_N\). For fixed degree \(D\le N\),
put \(V_f=k^4\otimes fP_{N-D}\) for \(0\ne f\in P_D\). Then

\[
D_{K,j}=\{[f]:\dim(K\cap V_f)\ge j\}
\quad\text{satisfies}\quad
\dim D_{K,j}\le\kappa_K-j.                     \tag{21}
\]

An empty locus satisfies every displayed dimension upper bound. These
loci are closed: multiplication by a nonzero \(f\) has constant
rank, so its image forms a subbundle over \(\mathbf P(P_D)\);
intersection dimension at least \(j\) is a determinantal condition.

Consider the projective incidence of pairs \(([f],[z])\) with
\(0\ne z\in K\cap V_f\). Over a fixed \([z]\in\mathbf P(K)\),
the form \(f\) divides a fixed nonzero polynomial component of
\(z\). There are only finitely many projective divisors of a binary
form of any specified degree, including in positive characteristic.
The incidence therefore has dimension at most \(\kappa_K-1\).
Over \(D_{K,j}\), its other fibers have dimension at least
\(j-1\), proving (21). The fiber-dimension step is the standard
dimension formula, as in the Stacks Project
[Lemma 33.20.4, tag 0B2L](https://stacks.math.columbia.edu/tag/0B2L).

If this locus is pulled back along an injective linear parameter map
from a vector space of dimension \(f_0\), it still has projective
dimension at most \(\kappa_K-j\). A general vector subspace of
dimension \(f_0-\kappa_K+j-1\), when positive, avoids it.
One can check this last assertion by the Grassmannian incidence:
the set of \(d\)-planes containing any point of a projective
\(s\)-dimensional locus has dimension at most
\(s+(d-1)(f_0-d)\), less than \(d(f_0-d)\) when
\(s+d<f_0\). No assumption that the base field itself is infinite
is needed, because the argument is made after algebraic closure.

## 7. Segre intersection and the first ordinary bound

For every matrix \(S\) and two quotient maps,

\[
\operatorname{rank}(BSC^{\mathsf T})\ge\operatorname{rank}S
 -\dim(\operatorname{im}S\cap\ker B)
 -\dim(\operatorname{im}S^{\mathsf T}\cap\ker C). \tag{22}
\]

The first compression loses exactly the first intersection dimension.
The transpose image after that compression is contained in
\(\operatorname{im}S^{\mathsf T}\), so the second compression
loses no more than the other displayed dimension.

Put \(\kappa=4(c+3)\). If \(e<r\), the long maps are surjective
by (2), and both kernels have dimension \(\kappa\). Concision of
the target gives \(\operatorname{rank}L\ge r^2-e>r(r-1)\).
Equation (19) therefore forces \(F,G\) to be injective; in
particular \(d_x,d_y\le c\).

If \(r\ge\kappa-4\), apply (21) to choose subspaces

\[
\dim U_0=r-\kappa+5,\qquad
\dim V_0=r-\kappa+6,                            \tag{23}
\]

avoiding the \(j=6\) stratum for the \(C\) kernel and the
\(j=7\) stratum for the \(B\) kernel. Both dimensions are
positive and at most \(r\), since \(\kappa\ge12\).
Every nonzero pure slice on \(U_0\otimes V_0\) loses at most
\(5+6=11\) ranks in (22). Its compressed rank is at least five.
Thus no such pure tensor belongs to
\(Z=\operatorname{ann}\operatorname{supp}_A(E')\), because the
corresponding target slice in (16) would have rank four.

The Segre variety in \(\mathbf P(U_0\otimes V_0)\) has dimension
\(\dim U_0+\dim V_0-2\). A linear space of codimension at most
\(e\) meets it if \(e\) is no larger than that dimension. This
is the projective dimension theorem, in the form of the Stacks Project
[Lemma 33.34.3, tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R).
Consequently

\[
e\ge\dim U_0+\dim V_0-1=2r-2\kappa+10.          \tag{24}
\]

If \(r\le\kappa-5\), the right side is nonpositive. Combining
these cases with the initial possibility \(e\ge r\) proves (6).

## 8. Removing the small-support cap

Write \(f=\operatorname{rank}F\), \(g=\operatorname{rank}G\),
and let \(\kappa_B,\kappa_C\) be the actual two long-kernel
dimensions. On complements to \(\ker F,\ker G\), (21) allows
subspaces of dimensions

\[
d_U=f-\kappa_C+j-1,\qquad
d_V=g-\kappa_B+12-j,                            \tag{25}
\]

for \(1\le j\le12\), provided both are positive. They avoid
kernel intersections of dimensions \(j\) and \(13-j\). Thus
every pure slice again loses at most eleven ranks. The argument of
Section 7 gives

\[
e\ge f+g-\kappa_B-\kappa_C+10.                  \tag{26}
\]

It remains to ensure positive dimensions and bound the right side.
If \(e\ge2r-1\), (7) is immediate. Otherwise (19) and target
concision imply \(fg\ge r^2-e>(r-1)^2\). Integer ranks therefore
give

\[
f,g\ge r-1,\qquad f+g\ge2r-1.                  \tag{27}
\]

Both factors cannot lose one rank, and a loss of two in either factor
would make their product still smaller. Let \(a_B,a_C\) be the
long-map ranks and put
\(x=r-\lfloor a_B/4\rfloor\),
\(y=r-\lfloor a_C/4\rfloor\). Equation (2) gives
\(e\ge r(x+y)-xy\). If both \(x,y\) are positive, this is at
least \(2r-1\); if either is at least two, it is at least \(2r\).
Therefore \(x+y\le1\): one long map is surjective and the other
has deficiency at most four. In particular,

\[
\kappa_B,\kappa_C\le\kappa+4,\qquad
\kappa_B+\kappa_C\le2\kappa+4.                  \tag{28}
\]

If \(r\le\kappa-3\), (7) is trivial. Otherwise set
\(A_0=\kappa_C-f\), \(B_0=\kappa_B-g\). Equations (27)-(28)
give \(A_0,B_0\le7\) and \(A_0+B_0\le9\). Choose

\[
j=\max(1,A_0+2).
\]

Then \(1\le j\le9\) and \(j\le11-B_0\), so both dimensions
in (25) are positive. They do not exceed \(f,g\), because
\(\kappa_B,\kappa_C\ge\kappa\ge12\). Substitution into (26)
now yields

\[
e\ge2r-2\kappa+5=2n-10c-19,
\]

which proves (7). All ordinary arguments hold after algebraic closure.
An identity over the original field would extend with unchanged matrix
and flattening ranks, so the conclusions hold over that field too.

## 9. Verification, provenance, and remaining questions

`verify.py` uses only the Python standard library and exact arithmetic.
It reconstructs the finite pole-cancellation identity; actual target
contractions and support unions; the stated oblique annihilator patterns;
native paired-source slices; polynomial-multiplier containing spaces;
sharp rank-loss controls; and the integer threshold choices. The saved
`certificate.json` can be regenerated and checked in full. A changed
coefficient or saved certificate is rejected by the tests.

These controls do not prove the geometric dimension theorems, classify
all source slices, or replace the written proofs. No numerical optimizer
is used for acceptance. Same-session proof checks are disclosed in
`sources.json` and do not change the claims' unreviewed status.

```sh
python research/ai/2026-10-23-first-support-capacity/verify.py --check
python -m unittest discover -s tests -p test_first_support_capacity.py -v
```

The first-support union argument and its Laurent extension are local
deductions. The prior source convention, source-slice matrix-rank bound, and
divisor-incidence argument retain their repository attribution. The
higher-intersection strata and their Segre application are a local
continuation using the cited classical dimension facts. No historical
priority is claimed.

For arbitrary first maps, a remaining ordinary construction must satisfy
the shared-kernel conditions in Section 5. A genuinely mixed first map
can fall outside (5). Singular first maps remain open even when their
generic long maps are surjective. The separate finite-bandwidth Toeplitz
long-map work in PR157 concerns restrictions on the other two maps and
does not supply an unrestricted obstruction here; see `QUESTION.md`.
