# Every output-leg Koszul rank of a zero-free bilinear tensor

2026-10-23. Written proof checked in the same generating session. The root agent
independently conjectured the padded-convolution formula and its maximality;
independent_theory derived the exterior quotient resolution below. The
first critical-degree elementary proof by pr_audit is retained separately.
No historical priority, external independent review, formalization, or
matrix-multiplication exponent improvement is claimed.

## 1. The result

Work over C. Let T belong to A tensor B tensor C, with dimensions
(a,N,M), where a>=2, N>=1, and M>=N+a-1. Suppose the bilinear contraction

\[
\mu_T:A^*\times B^*\longrightarrow C
\]

has no nonzero zero-product pair: mu_T(x,b) is nonzero whenever both
x and b are nonzero. Equivalently, for every nonzero x in A*, the linear
map b -> mu_T(x,b) is injective.

For 0<=p<M, define

\[
K_C^p(T):B^*\otimes\bigwedge^p C
\longrightarrow A\otimes\bigwedge^{p+1}C,
\qquad
b\otimes\xi\longmapsto\sum_i a_i\otimes\mu_T(a_i^*,b)\wedge\xi.
\]

Then, with binomial coefficients outside their range interpreted as zero,

\[
\kappa_p:=\dim\ker K_C^p(T)
=\sum_{j=a+1}^{p+1}(-1)^{j-a-1}
  \binom{N+j-1}{j}\binom{M}{p+1-j}\binom{j-2}{a-1},
\tag{1}
\]

\[
\operatorname{rank}K_C^p(T)=N\binom{M}{p}-\kappa_p.
\tag{2}
\]

In particular the map is injective for p<a, and it has full row rank for
p>=M-N. If a<M, its first nonzero kernel occurs at p=a, with dimension
binom(N+a,a+1), as in pr_audit's separate Vandermonde proof. When N=1
and M=a, every degree in the stated range is injective.

There is a cancellation-free equivalent formula. Put m0=N+a-1 and
d=M-m0. Then

\[
\boxed{\operatorname{rank}K_C^p(T)
=\sum_{j=0}^{m_0-1}
\min\left\{N\binom{m_0}{j},\ a\binom{m_0}{j+1}\right\}
\binom{d}{p-j}.}
\tag{3}
\]

These values are the maximum possible ranks among all tensors of format
(a,N,M), including tensors with zero-product pairs. Hence no C-leg
Koszul rank test can exclude a degeneration from such a zero-free source
to any target in the same format.

## 2. The quotient bundle

Use the convention that projective space X=P(A*) parametrizes lines in
A*. It has dimension a-1. The universal line O(-1) is a subbundle of
A* tensor O. Restricting mu_T to that line gives

\[
0\longrightarrow E:=B^*\otimes O(-1)
\overset{\iota}{\longrightarrow}F:=C\otimes O
\longrightarrow Q\longrightarrow0.
\tag{4}
\]

The zero-free hypothesis means iota has rank N at every point, so its
quotient Q is a vector bundle of rank M-N. No choice of a regular unit
slice, Laurent normalization, or compatibility between source block bases
is needed for this statement.

Fix n=p+1. The following complex resolves the exterior quotient:

\[
0\to\operatorname{Sym}^{n}E\to
\operatorname{Sym}^{n-1}E\otimes F\to\cdots\to
E\otimes\bigwedge^{n-1}F\to\bigwedge^nF\to\bigwedge^nQ\to0.
\tag{5}
\]

Here the differential removes one symmetric E factor, applies iota, and
wedges its image into F. Exactness can be checked locally, so it is enough
to split F=E direct_sum Q. Each summand with a fixed exterior Q degree
reduces to the standard symmetric/exterior complex on E, of some total
degree m. Its differential and contraction homotopy satisfy
dh+hd=m times the identity. Thus it is exact for m>0 over C. For m=0,
the surviving summand is exactly wedge^n Q. This proves (5) directly.

Twist (5) by O(1). Write its term in complex degree -j as

\[
L^{-j}=\operatorname{Sym}^{j}B^*\otimes
\bigwedge^{n-j}C\otimes O(1-j),\qquad0\le j\le n.
\tag{6}
\]

The complex has only one cohomology sheaf, in degree0, namely
G=wedge^n Q tensor O(1). In particular its hypercohomology vanishes in
every negative total degree.

## 3. The two nonzero cohomology rows

The elementary line-bundle calculation on P^(a-1) gives only the following
nonzero groups among H^q(O(1-j)), for j>=0:

\[
\begin{aligned}
H^0(O(1))&\cong A, &\dim&=a,\quad j=0,\\
H^0(O)&\cong\mathbb C, &\dim&=1,\quad j=1,\\
\dim H^{a-1}(O(1-j))&=\binom{j-2}{a-1},&&j\ge a+1.
\end{aligned}
\tag{7}
\]

All intermediate groups vanish. One direct verification uses the usual
coordinate affine cover of projective space. Its monomial Cech complex
splits by Laurent monomial. A monomial with all exponents nonnegative
contributes in degree0. A monomial with every exponent negative contributes
in top degree. The other monomial complexes are exact. Counting the two
surviving kinds gives the displayed dimensions.

Apply the cohomology-of-a-complex spectral sequence to (6), with
E1^(-j,q)=H^q(L^(-j)). Its degree-zero row has only the two terms j=1,0,
whose map is precisely K_C^p(T). Its other possible row has q=a-1 and
positions j>=a+1. In that upper row the term dimensions are

\[
u_j=\binom{N+j-1}{j}\binom{M}{n-j}\binom{j-2}{a-1}.
\tag{8}
\]

After taking the horizontal cohomology, the only possible differential
between the two rows is d_a. It changes(-j,a-1) to(-j+a,0).
For a nonzero lower-row target, j must be a or a+1. The upper row has
no term at j=a. Therefore the only possible nonzero such differential
goes from j=a+1 to j=1.

Every upper-row position has negative total degree a-1-j<=-2.
Positions j>a+1 have no possible later differential to or from a nonzero
entry, so their horizontal cohomology must vanish. The upper-row cokernel
at j=a+1 maps isomorphically by d_a onto ker K_C^p(T): injectivity and
surjectivity follow because both source and target have negative total
degree and the total hypercohomology has none there.

It follows that the upper row is exact except at its rightmost cokernel,
and that this cokernel has dimension dim ker K_C^p(T). Its Euler sum is
u_(a+1)-u_(a+2)+..., proving (1) and (2).

The same argument shows that the lower-row cokernel is H0(G). If n>M-N,
then wedge^n Q=0, so that cokernel vanishes. This proves full row rank
for p>=M-N. For p<a the upper row is empty, proving injectivity.

This calculation is the point where the zero-free hypothesis matters:
without it, Q need not be a vector bundle and (5) is not justified by the
displayed local splitting.

## 4. Padding a single convolution gives the positive formula

The canonical multiplication tensor Full(a,N) has third dimension
m0=N+a-1 and is zero-free: a product of two nonzero polynomials is
nonzero. Apply the preceding proof to it. Its Q has rank a-1, so the
Koszul map is injective for p<a and surjective for p>=a-1. At p=a-1,
the two dimensions agree. Thus every degree has rank

\[
\min\{N\binom{m_0}{p},a\binom{m_0}{p+1}\}.
\]

Now add d unused third-leg coordinates. The tensor remains zero-free.
Decompose exterior powers according to their number of unused coordinates.
Each fixed unused-coordinate wedge carries a copy of the smaller Koszul
map, giving the sum in (3). Since (1)--(2) depend only on(a,N,M), this
padded tensor has the same ranks as every zero-free tensor of that format.

## 5. Why these ranks are universal maxima

Inside the affine space of all tensors of format(a,N,M), let U be the
zero-free locus. Its complement is closed: impose mu_T(x,b)=0 in the
product with P(A*) times P(B*), then project this closed incidence along
the projective factors. U is nonempty because the padded Full tensor
belongs to it. Hence U is dense and open.

For every fixed p, (1) gives one constant rank on U. If any tensor had a
strictly larger rank, nonvanishing of an appropriate minor would give a
nonempty open set of larger ranks. That set would meet U, since the
ambient affine space is irreducible, a contradiction. Thus the common
rank on U is the maximum over all tensors in the format.

This conclusion includes targets with singular maps, arbitrary independent
first-leg identifications of their blocks, and target tensors outside the
polynomial block class. It concerns only this C-leg Koszul family.

## 6. Application to canonical and independently identified Full sources

For any partial sum of Full(a,b_r), let N=sum b_r and
M=N+c(a-1). Even if each block has its own invertible first-leg
identification, every nonzero x in the common first dual space becomes a
nonzero polynomial in each block. Multiplication by that polynomial is
injective. Since the other two legs are direct sums of blocks, the whole
A-slice B* -> C is injective.

Therefore every such Full source satisfies (1)--(3), with arbitrary
independent invertible first identifications. This is stronger scope than
the canonical-first B-leg exterior and tensor-power formulas, whose
evaluation sequence lives on a common projective line.

In particular S=10 Full(5,10) has(a,N,M)=(5,100,140), and is compared
with padded Full(5,100), whose104-dimensional output has36 unused
coordinates added. Every(5,100,140) target automatically passes every
C-leg Koszul rank inequality against S. No target C6,...,C39 matrix needs
to be built to decide those inequalities.

For reference, the first critical degree has kernel1609344100 and
rank40087208700. The next degree has kernel103457835000 and
rank834714603000. These large values follow from exact integer formulas,
not floating-point rank estimates.

## 7. Finite controls and remaining scope

The program `verify_full_source_all_c.py` checks the equality of
(1)--(3), rank bounds, and the injective and surjective ranges on a finite
grid. It also reruns `full_source_c_leg_pilot.py`'s literal canonical
coefficient matrices over F2 for 97 small cases, including unequal widths
and repeated blocks. All ranks agree with (1). The companion report is
`results/mixed-longlegs-candidate-2026-10-23/full_source_all_c_controls.json`
and includes every source degree for the
(5,100,140) candidate. These are independent finite convention checks;
the theorem above is over C and does not use modular rank as a
characteristic-zero upper bound.

The complementary elementary critical-degree proof is
[first_critical_source_kernel.md](first_critical_source_kernel.md). The root agent's
independent all-degree literal control for3 Full(3,1) gives ranks
(3,27,108,237,306,237,108,27,3), also agreeing with (3).

The result computes and maximizes one family of necessary rank tests.
It neither constructs the shared-output candidate nor proves a barrier
for all tensor invariants, all projected Koszul maps, all Young flattenings,
or the exponent problem.

Reproduce from the repository root:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_full_source_all_c.py
```

Original byte hashes and integration changes are recorded in
[source_flattenings_integration.md](source_flattenings_integration.md).
