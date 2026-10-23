# Long-leg exterior and tensor-power ranks for canonical Full sums

2026-10-23. Written proof and same-session audit. The exterior formula was
proposed by the root agent and checked by independent_theory and pr_audit.
The tensor-power extension and its finite candidate screen were developed
by independent_theory. Neither is externally reviewed or formally verified.

## 1. Precise source and maps

Let a>=1 and let b1,...,bc be positive integers. All blocks use the same
coefficient basis on the first leg. Put N=sum b_i and
L=N+c(a-1), and take the canonical partial sum

\[
S=\bigoplus_{1,i=1}^{c}\operatorname{Full}_{a,b_i},
\qquad
\operatorname{Full}_{a,b}
=\sum_{u=0}^{a-1}\sum_{v=0}^{b-1}x_u\otimes y_v\otimes z_{u+v}.
\]

Thus S belongs to A tensor B tensor C of dimensions(a,N,L).
For p>=0, its second-leg Koszul map is

\[
K_B^p(S):C^*\otimes\bigwedge^pB
\longrightarrow A\otimes\bigwedge^{p+1}B.
\]

For q>=1, define a second natural map

\[
D_q(T):A^*\otimes(B^*)^{\otimes q}
\longrightarrow\bigoplus_{k=1}^{q}
C\otimes(B^*)^{\otimes(q-1)}.
\]

The kth component applies the tensor contraction
mu_T:A* tensor B* -> C to the first factor and kth B* factor, leaving the
other B* factors in their original order. The q output components are
separate direct summands. No sum over positions is taken inside one output.

Both maps have matrix entries linear in T, are covariant under all three
general linear groups, and have rank that cannot increase in a degeneration.
The displayed source formulas require the common canonical first basis.
They are not asserted for independently reidentified source blocks.

## 2. Explicit evaluation kernel

On the projective line, put

\[
V=\bigoplus_i O(b_i-1),\qquad E=H^0(V),\qquad\dim E=N.
\]

Polynomial multiplication identifies A* with H0(O(a-1)), B* with E,
and C with H0(V(a-1)). The contraction mu_S is the multiplication map
on these global sections. Let

\[
0\longrightarrow M\longrightarrow E\otimes O
\overset{\mathrm{ev}}{\longrightarrow}V\longrightarrow0
\]

be the evaluation sequence. It has the explicit splitting

\[
M\cong O(-1)^{N-c}.
\]

Here no general vector-bundle splitting theorem is needed. For a single
summand O(d), evaluation sends e_j to u^(d-j)v^j, for j=0,...,d.
Its d syzygies are

\[
u e_{j+1}-v e_j,\qquad 0\le j<d.
\]

They define O(-1)^d -> O^(d+1). At every point with u nonzero, the last
d coordinates give a nonzero triangular minor u^d. At every point with
v nonzero, the first d coordinates give the minor(-v)^d. The map therefore
has rank d at every point, and its image is the rank-d evaluation kernel.
Taking direct sums proves the claim, including d=0.

## 3. Exterior formula, including higher-rank evaluation quotients

Put q=p+1. The transpose of K_B^p(S) is the global-section map of the
twisted bundle morphism

\[
\delta_q:\bigwedge^q(E\otimes O)\otimes O(a-1)
\longrightarrow\bigwedge^{q-1}(E\otimes O)\otimes V(a-1),
\]

where delta is alternating comultiplication followed by evaluation of the
removed factor. Its bundle kernel is exactly wedge^q M, tensored with
O(a-1). This remains true when V has rank c greater than one.

For completeness, split one fiber as E=M_point direct_sum Q. Decompose
the exterior power according to the number r of Q factors. The r=0
summand is killed. For r>0, a basis wedge maps to the sum of its r terms
obtained by removing one Q basis vector and recording that vector in the
last tensor factor. The supports of these sums are disjoint for different
basis wedges: an output records both the retained wedge and the removed
vector, and hence determines the input wedge. All coefficients are1 or-1.
The map is therefore injective on every positive-r summand. Different r
also have different output grading. This proves the fiberwise kernel
claim without dividing by r.

Taking global sections is left exact. Since

\[
\bigwedge^qM\otimes O(a-1)
\cong O(a-1-q)^{\binom{N-c}{q}},
\]

the kernel dimension is max(a-q,0)*binom(N-c,q). It follows that

\[
\boxed{\operatorname{rank}K_B^p(S)
=a\binom{N}{p+1}
-\max(a-p-1,0)\binom{N-c}{p+1}.}
\]

Binomial coefficients outside their range are zero. The proof uses only
the explicit evaluation syzygies, the elementary exterior fiber calculation,
and h0(O(d))=max(d+1,0). In fact these arguments are valid over every field;
the application below is over C. At p>=a-1 the map has full row rank,
so no target in the same ambient format can violate it in those degrees.

## 4. Simultaneous tensor-power contraction formula

The map Dq is the global-section map of the q separate fiber evaluations

\[
(E\otimes O)^{\otimes q}\otimes O(a-1)
\longrightarrow\bigoplus_{k=1}^{q}
(E\otimes O)^{\otimes(k-1)}\otimes V
\otimes(E\otimes O)^{\otimes(q-k)}\otimes O(a-1).
\]

Its kernel is M^tensor(q) tensor O(a-1). Indeed, after splitting E=M+Q
in a fiber, any summand with a Q factor survives the component evaluating
that factor. All summands using only M factors vanish in every component.
Equivalently, the intersection of the kernels of the q individual
evaluations is M in every tensor position.

Since M^tensor(q) is O(-q)^(N-c)^q, left exactness again gives

\[
\boxed{\operatorname{rank}D_q(S)
=aN^q-\max(a-q,0)(N-c)^q.}
\]

For q>=a this is full column rank. Therefore only q=1,...,a-1 can give
a nontrivial necessary condition in the fixed format. The symmetric group
on q letters acts on the tensor positions and the kernel. The exterior
component reproduces the preceding formula. Other symmetry types can give
stronger individual tests than the total Dq rank. The complete component
screen is recorded in [schur_screen.md](schur_screen.md).

## 5. The new shared-output candidate

The precise canonical candidate, supplied by research_frontier, is

\[
10\operatorname{Full}_{5,10}\ \rightsquigarrow\
7\operatorname{Full}_{5,2}
\oplus_1 10\operatorname{Full}_{5,3}
\oplus_1 4\operatorname{SharedOutput}_{3,3}
\oplus_1 2\operatorname{SharedOutput}_{4,2}
\oplus_1 6\operatorname{Mid}_{5,2}.
\]

Here Mid5,2 has coefficients x_i y_(i+k) z_k, and SharedOutput(d,e)
has coefficients x_(j+k)y_j z_k. Every block has first dimension5;
its second and third legs occupy disjoint concatenated intervals.
Both total formats are(5,100,140). The input record is
`discovery_input.json`, SHA256
`c53abefde0cb5d5e2e816f96ae6c257ee843f59e6c28d13a6ae1994de9ab88f3`.

The source exterior formula gives ranks12735,573540,17050935 at
p=1,2,3. Its higher degrees are automatically maximal as above.

The Dq target calculation splits over ordered tuples of target B blocks.
Each tuple has a separate input summand and separate output summands:
the C block in an output determines the removed B block, while the other
positions retain their B block labels. Thus ranks add over block tuples.
Tuples of the same five block types have identical matrices. Permuting
positions preserves rank, so only5,15,35,70 sorted type tuples are needed
at q=1,2,3,4. Copy multiplicities and ordering are restored exactly.

| q | Source rank | Canonical target rank | Target minus source |
| --- | ---: | ---: | ---: |
| 1 | 140 | 140 | 0 |
| 2 | 25700 | 25317 | -383 |
| 3 | 3542000 | 3432270 | -109730 |
| 4 | 434390000 | 412195367 | -22194633 |

The verifier `shared_output_prolongation.py` rebuilds every
small matrix from the literal coefficients. Primitive-integer Gaussian
elimination gives its rational rank; a separate bit-vector elimination
gives its rank over F2. Every recorded pair agrees. The report contains
all125 type-tuple systems and their exact multiplicities, plus independent
Full-only formula controls.

Thus this specific canonical target passes every Dq necessary rank test:
the four nontrivial degrees pass exactly, and q>=5 is automatic from the
source's full column rank. This is no construction, no exclusion under
other tests, and no exponent improvement. Independently changing target
first identifications may change these target ranks; the displayed target
calculation uses the stated canonical identifications.

## Attribution and reproducibility

The polynomial Full/Mid conventions and shared-leg partial-sum setting
are adopted from the maintained research program. PR143 at
`079dbdc4a72fc8bf4bcccaf4f4487c2717882062` concerns a different paired
source and should not be confused with this Full-only formula. The
candidate and its earlier dimension, shared-leg, and degree-one screens
belong to research_frontier and pr_audit. The current note adds a direct
evaluation-kernel proof and the stated finite tensor-power screen; it
does not assert historical priority for these natural flattenings.

Run from the repository root:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_full_source_exterior.py
python research/ai/2026-10-23-mixed-longlegs-candidate/shared_output_prolongation.py --max-degree 4 --rational
```

Reports are stored in `results/mixed-longlegs-candidate-2026-10-23/`.
The frozen source files and integration changes are recorded in
[source_flattenings_integration.md](source_flattenings_integration.md).
