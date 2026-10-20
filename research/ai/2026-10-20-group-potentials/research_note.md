# Finite group degenerations: exact search and a determinant obstruction

October 20, 2026. AI-derived work by Codex at the repository owner's request.
Written arguments are unreviewed and not Lean formalized. **No smaller
matrix-multiplication exponent has been established.**

## 1. A finite certificate that would suffice

Let G be a finite group and use the tensor
\(T_G=\sum_{xyz=e}X_xY_yZ_z\) over C. For sets S,T,U, require each of

\[
(s,t)\mapsto s^{-1}t,\quad(t,u)\mapsto t^{-1}u,\quad
(u,s)\mapsto u^{-1}s
\]

to be injective. Restrict the tensor to these three label sets. Its intended
matrix-product terms come from the same triple \((s,t,u)\). There may be extra
terms. An integer weight assignment that is zero on intended terms and
strictly positive on every extra term gives a combinatorial degeneration to
\(M_{|S|,|T|,|U|}\).

Every zero assignment on the complete intended support has the form

\[
w_X(s,t)=a_s-b_t,\quad w_Y(t,u)=b_t-c_u,\quad
w_Z(u,s)=c_u-a_s. \tag{1}
\]

To verify this, fix one vertex in each of the three parts and subtract the
zero equations for triangles differing in one vertex. The differences on
any edge depend only on its endpoint; the remaining constants can be absorbed
in a,b,c. Conversely (1) plainly makes every intended triangle zero.

An extra term with labels from \((s,t),(t',u),(u',s')\) thus has weight

\[
a_s-a_{s'}+b_{t'}-b_t+c_{u'}-c_u. \tag{2}
\]

The verifier enumerates every product of an X label and a Y label, looks up
the unique inverse product on Z, and checks (2) with integers. It also checks
all intended terms and all three pair-map injectivity conditions. No floating
LP or SAT result is trusted for witness acceptance.

For an infeasible system, positive integers \(w_l\) and extra-relation rows
\(R_l\) satisfying \(\sum_lw_lR_l=0\) are an exact Farkas certificate:
strict positivity of every \(R_l\cdot v\) would be contradictory. The source
vertices of such a certificate give a learned clause forbidding that same
configuration in a larger candidate. Floating linear programs discover these
circuits; integer arithmetic checks them before they become SAT cuts.

There is also an orbit-wide cut. If quotient elements qT,qU commute and
\(qS=qTqU\), the forward and reversed extra terms have opposite rows in (2).
They cannot both be positive. The SAT encoding adds this necessary condition
using inverse-pair quotient indicators. This derivation is local; no claim of
priority is made for the condition or the SAT approach.

## 2. A certified source and a conditional numerical endpoint

For SL(2,5), the source degrees are certified as

\[
1,2,2,3,3,4,4,5,6.
\]

The program generates the 120 matrices modulo five and their nine conjugacy
classes, constructs the class-sum multiplication algebra, and verifies nine
nonzero pairwise orthogonal central idempotents over Q(sqrt(5)). Their sum is
one. Since the center has dimension nine, these idempotents are primitive.
The trace of left multiplication by e on C[G] is \(|G|e(1)\), so their
regular-representation ranks are exact squares \(d_i^2\). Maschke's theorem
and Artin--Wedderburn identify the corresponding simple blocks as M(di).
All 81 idempotent products are checked; no character table was imported.

If a matrix tensor of volume V degenerates from this group algebra, the
asymptotic sum inequality and the usual border-to-asymptotic conversion imply

\[
V^{\omega/3}\le\sum_i d_i^\omega. \tag{3}
\]

For \(V=972,990,1000\), respectively shapes (9,9,12), (9,10,11), (10,10,10),
integer-root interval certificates establish the strict comparison

\[
\sum_i d_i^{2249/1000}<V^{2249/3000}. \tag{4}
\]

Every \(d_i<V^{1/3}\), so \(\sum_i(d_i/V^{1/3})^x\) decreases strictly in x.
If the degeneration existed, (3)-(4) would force \(\omega<2249/1000\), in
particular the weaker displayed bound \(\omega\le2249/1000<9/4\).
**The degeneration is unconstructed. This number is conditional.**

The shapes came from matmul-swarm's October 17 agent-board post
`3a4edfaa-d6a8-44ec-9131-6ff0a66781d3`. That post is an unverified external
research report; its private scripts were not available here.

## 3. A general determinant-divisor obstruction

**Proposition.** Let G be a finite group of order N, with complex irreducible
degrees d. Suppose its group-algebra multiplication tensor degenerates to
\(M_{n,n,p}\), where \(np\le N\). Put \(c=N-np\). Then every degree d with
\(d>c\) must be divisible by n.

This is a necessary condition for arbitrary tensor degenerations, including
general basis changes. It is not restricted to the coordinate/potential ansatz.

**Proof.** Slice the source along its first leg. Up to a fixed invertible
change identifying the dual regular space, the resulting N by N matrix is
left multiplication by a group-algebra element x. In Fourier coordinates it is

\[
L_x\cong\bigoplus_\rho I_{d_\rho}\otimes\rho(x). \tag{5}
\]

Fix a block of degree d>c, and write \(D(x)=\det\rho(x)\), a homogeneous
polynomial of degree d. Every \((N-c)\)-minor of (5) is divisible by
\(D(x)^{d-c}\). Indeed, there are d identical d by d blocks for this rho.
Deleting c rows and c columns can touch at most c of these blocks on the row
side. For a nonzero minor, each independent diagonal block must retain the
same number of rows and columns, so at least d-c copies are untouched and
contribute their full determinant.

Cauchy--Binet preserves the common divisor under arbitrary linear maps on
the other two legs. Substitution by any linear first-leg map preserves it as
well. If the substituted D is identically zero then the resulting square
matrix has identically zero determinant, and cannot limit to the target below
with a nonzero determinant.

For any source transformation with nonzero resulting determinant, that
determinant therefore has a homogeneous divisor of degree d. The locus of
nonzero homogeneous polynomials having a factor of degree d is closed in
projective coefficient space: it is the image of the multiplication map from
the product of projective spaces of degree-d and degree-(np-d) forms. This
image is closed because its domain is projective. Hence the property persists
under degeneration whenever the limiting determinant is nonzero.

For the target, its first-leg variables form a generic n by n matrix X and
the slice is, up to fixed changes and transposes, \(X\otimes I_p\). Its
determinant is \(\det(X)^p\). The generic determinant is irreducible over C,
so each of its nonconstant homogeneous divisors has degree divisible by n.
The forced divisor of degree d therefore requires n to divide d. QED.

The proof also works if first-leg variable spaces are padded before the
transformation. If dimensions already fail, an ordinary flattening is the
earlier obstruction. The case n=1 supplies no divisibility restriction.

**Corollaries.** Since every finite group has a degree-one trivial
representation, a target with n>=2 and np=N is impossible. If n is greater
than every source degree, a necessary condition is
\(N-np\ge\max_\rho d_\rho\).

## 4. Affine groups and examples removed before further search

For \(G=C_q\rtimes C_r\), with q prime and the faithful order-r subgroup of
\(\mathbb F_q^\times\) acting by multiplication, the degrees are r copies of
one and (q-1)/r copies of r. One can verify this without a table: the r linear
characters factor through C(r); the nontrivial characters of C(q) form free
orbits of size r. Induction gives r-dimensional representations with distinct
diagonal eigencharacters on C(q) and a transitive cyclic action on them, hence
irreducibility. Distinct orbits give inequivalent representations. The sum of
degree squares is \(r+(q-1)r=qr\), proving completeness.

The proposition removes these tempting candidates:

| Source | Target | N-np | Obstructing degree |
| --- | --- | ---: | ---: |
| C5 semidirect C4 | M(4,4,5) | 0 | 1 |
| C7 semidirect C3 | M(4,4,5) | 1 | 3 |
| C13 semidirect C4 | M(7,7,7) | 3 | 4 |

It does not remove C13:C3 -> M(6,6,6), C17:C4 -> M(8,8,8),
C19:C3 -> M(7,7,7), or the three SL(2,5) shapes above. Passing this screen
does not establish a construction.

### 4.1 The abelian-coset ceiling constraint

This next lemma concerns the coordinate-potential construction of Section 1,
not every arbitrary tensor degeneration excluded by Section 3.

Let H be **any abelian subgroup** of G, of order h and index r. If S,T,U
give the coordinate-potential degeneration, write mS,mT,mU for their largest
intersections with right cosets of H. Then

\[
\boxed{m_Sm_Tm_U\le h,\qquad
\left\lceil\frac{|S|}{r}\right\rceil
\left\lceil\frac{|T|}{r}\right\rceil
\left\lceil\frac{|U|}{r}\right\rceil\le h.} \tag{6}
\]

To prove this, first restrict to a largest coset intersection in each set,
then translate each set independently on the right into H. Independent right
translations preserve the construction: pair labels transform as
\(x\mapsto a^{-1}xb\), \(y\mapsto b^{-1}yc\),
\(z\mapsto c^{-1}za\), preserving the identity-product condition and all
vertex-potential sums. In an abelian group every extra relation has the reversed
extra relation with the opposite weight. Thus no extra relation is possible.
The ordinary triple product property in an abelian group makes the product map
from the three sets injective, so their size product is at most h.
Pigeonhole gives the ceilings in (6). Normality of H is not needed.

This is a local derivation of a coset-counting screen, with no novelty claim.
Keeping the ceilings strengthens its coarser consequence
\(|S||T||U|\le r^3h=r^2|G|\).

For C19:C3 at shape (7,7,7), the lower sizes are (3,3,3), with product 27>19.
That coordinate-potential construction is therefore excluded by the written
lemma, independently of the untraced SAT result. At shape (6,7,8), lower sizes
are (2,3,3), and (6) forces largest coset sizes to be exactly (2,3,3).
For C17:C4 at (8,8,8), lower sizes are (2,2,2); at least two of the largest
coset sizes must equal two, because 2*3*3>17. These integer constraints justify
stronger search normalization. They do not settle the remaining shapes.

## 5. Search evidence and its limits

The machine reports preserve seeds, parameters, actual model counts and exact
Farkas circuits. The small SL(2,5) control (3,3,3) has 27 intended terms and
one extra term, killed by a strictly positive integer potential. It is a genuine
control degeneration, with no record exponent consequence.

The first unrestricted pair-injective SL(2,5) run at (9,9,12), and runs with
commuting cuts at all three target shapes, timed out after 180 seconds each
without a pair-injective model. These are unresolved searches, not exclusions.

For C5:C4 at (4,4,5), the solver encountered 459 pair-injective models and
each received an exact Farkas cut, then reported UNSAT. No proof trace was
exported, so the solver outcome is not an independent nonexistence certificate.
The all-size determinant argument above independently excludes this target.
The smaller C7:C3 and C13:C3 runs also reported UNSAT without a proof trace;
only C7:C3 is independently covered by the determinant proposition.

Additional completed runs: C19:C3 at (6,7,8) and C17:C4 at (8,8,8)
timed out after 180 seconds without a model. C19:C3 at (7,7,7) returned
solver-reported UNSAT without a proof trace. None of these outcomes is an
independently checked nonexistence theorem. The campaign continues; the
construction question remains separate from source and infrastructure checks.

## 6. Reproduction and sources

Exact verification and source/gate programs use the standard library. The
discovery search additionally uses NumPy, SciPy, python-sat and SymPy.

```sh
python3 research/ai/2026-10-20-group-potentials/fourier_certificate.py \
  --output results/group-potentials-2026-10-20/fourier_and_conditional_gates.json
python3 research/ai/2026-10-20-group-potentials/determinant_obstruction.py \
  --output results/group-potentials-2026-10-20/determinant_obstruction.json
python3 research/ai/2026-10-20-group-potentials/search.py \
  --shape 9 9 12 --seconds 180 --seed 20261021 \
  --output /tmp/sl2-5-new-run.json
```

External sources:

- Cohn and Umans, [*A group-theoretic approach to fast matrix multiplication*](https://arxiv.org/abs/math/0307321),
  Theorems 2.3 and 4.1: group-algebra embedding and the character-degree
  inequality. Their rank argument is extended to a degeneration using the
  standard interpolation/asymptotic-rank passage; no finite target is supplied
  by the numerical gate.
- Bini, [*Relations between exact and approximate bilinear algorithms*](https://doi.org/10.1007/BF02575865):
  border-to-asymptotic conversion, as already attributed in the repository's
  source registry. No new independent audit of that paper is claimed.
- [Matrix agent board](https://board.bigospeedrun.com/matrix-multiplication),
  post `3a4edfaa-d6a8-44ec-9131-6ff0a66781d3`, read October 20: the three
  SL(2,5) target shapes and prior search reports. These remain attributed leads.

The determinant proof and concrete certificates were derived in this session.
No historical priority claim or independent review is asserted.
