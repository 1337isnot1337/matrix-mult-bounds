# Smaller centered supports: exact counts and a remaining cost floor

October 23, 2026. Owner-directed OpenAI Codex research. Written and unreviewed.

This continuation deliberately removes both earlier hypotheses: the
leading grid may be pruned, and the products may have different ordered
part shapes. It still finds a cost obstruction for a broad class of
coordinate embeddings. The obstruction concerns **counting each nonzero
position after deleting zero forms**, before any further cancellation,
reweighting or replacement by new rank-one forms.

## 1. A cost floor from one diagonal target

Let p independent matrix multiplication tensors be indexed by complete
tripartitions of d coordinates. In target t, coordinate r has positive
integer dimension n_{t,r}. Its volume is

\[
 v_t=A_t B_t C_t=\prod_{r=1}^d n_{t,r}.
\]

Allow arbitrary ordered part sizes and product-dependent coordinate
embeddings in one common grid. On each diagonal coordinate, suppose the
two active factors have nonzero row vectors on a common set S_{t,r}
with at least n_{t,r}+1 positions. The positions and sets may differ
between products and coordinates. This condition holds when both active
maps are zero extensions of bases of the centered space on the same
n_{t,r}+1 coordinates, or when a truncated centered primal/dual pair
has that common support.

Assume that all main grid coefficients are nonzero and that the only
pruning performed before charging the budget is deletion of identically
zero rank-one forms. Correction costs, if any, are nonnegative. Scalar
gradings are allowed; they do not change which generic factor forms are
zero. The products' variable blocks must be independent.

**Theorem 1.** Every such pruned position budget satisfies

\[
 B_{\rm prune}\ \ge\
 \left(\frac4{3^{3/4}}\right)^d\max_t v_t^{3/4}.             \tag{1}
\]

Consequently, if

\[
                   p^4 3^{3d}<4^{4d},                     \tag{2}
\]

then `B_prune>sum_t v_t^(3/4)`. The direct 9/4 asymptotic-sum comparison
fails for every allowed choice of coordinate dimensions and supports.
This includes mixed graded shapes. It does not require conflict freedom
or an upper bound on the number of products from an induced-edge graph.

**Proof.** Fix target t. At each point of the Cartesian product
`product_r S_{t,r}`, its projected main grid form is a tensor product of
nonzero local row forms, so is nonzero. The full main form cannot be
zero because its projection to that independent target block is nonzero.
Thus at least `product_r |S_{t,r}|` main positions survive. Weighted
arithmetic-geometric mean gives

\[
 B_{\rm prune}\ge\prod_r(n_{t,r}+1)
 \ge\left(\frac4{3^{3/4}}\right)^d
           \prod_r n_{t,r}^{3/4}.
\]

Choose a target of largest volume. Since
`sum_t v_t^(3/4)<=p max_t v_t^(3/4)`, (2) proves the result. The argument
counts projected nonzero positions; it does not assert their linear
independence. Different positions could admit a cheaper representation
if the allowed operations were enlarged. This distinction is essential.

## 2. Scope for the investigated families

The exact [report](report.json) checks (2) for the external graded
general10, general13 and general22 families on six coordinates, and
the local 29- and 106-product families on nine and twelve coordinates.
All five satisfy the strict inequality. In fact, (2) excludes every
p<=29 on six coordinates under the stated common-support condition.
This statement concerns the number of independent blocks, not the
numerical size of any one block.

The external unequal-shape constructions are Solomonik and Blaeser,
[arXiv:2610.26563v2](https://arxiv.org/html/2610.26563v2), Appendix D,
revised October 22, 2026. Their source files, signed scalar gradings,
correction sets and SHA256 pins are retained here. They are credited
external constructions, not newly discovered families.

For mixed ordered shapes, centering and conflict freedom alone do not
justify the exact ungraded identity. A mixed triple can have coordinates
omitted by no factor and have no replicated coordinate to cancel. The
verifier therefore checks the actual signed grades, including all such
triples. Every non-diagonal term either has a coordinate omitted by
exactly two factors, is canceled by the supplied corrections, or has
strictly positive total grade. Only the last class vanishes by the
border-rank limit. No approximate floating-point residual is used.

## 3. A concrete family of pruned rectangular algorithms

Here is the constructive model used for the exact counts. Let n>=2 and
q=n+1. A profile H_t subset F gives target t dimension n on coordinates
in H_t and dimension one on all other coordinates. No target in the
saved witnesses has H_t=F.

For a coordinate of dimension m in {1,n}, form

\[
 E_m=\begin{bmatrix}I_m\\-\mathbf1^T\end{bmatrix},\qquad
 D_m=E_m\left(I_m-\frac{J_m}{m+1}\right).
\]

Embed both maps into the q-row grid on positions
`{0,...,m-1,q-1}`, with zero rows elsewhere. Both are centered,
`E_m^T D_m=I_m`, and both have exactly the same m+1 nonzero rows.
Assign one E and one D on each active diagonal pair, using the parent
proof's orientation. The source centering/correction identities continue
to hold because the columns remain centered and the diagonal pairings
remain identities. The scalar grades are unchanged. Thus these are
uniform border-rank upper bounds over characteristic zero for every
integer n>=2, not merely sampled dimension evaluations.

### Exact count for every n

Let P be a supplied correction subset, including the empty set for the
main aggregate. A product is eligible in its X, Y or Z factor exactly
when P is contained in its respective omitted part U, V or W.
Coordinates outside P have two low grid positions `{0,q-1}`, and n-1
high grid positions. Let L subset F minus P be the coordinates assigned
high positions. At a factor with omitted part O_t, target block t is
nonzero exactly when

\[
                  L\subseteq H_t\cup O_t.
\]

Different products use independent variable blocks, so an aggregate
factor is nonzero exactly when at least one of its eligible blocks is
nonzero. The whole rank-one position survives if that condition holds
in all three factors. Its position type L has multiplicity

\[
              2^{d-|P|-|L|}(n-1)^{|L|}.                    \tag{3}
\]

The verifier enumerates every P,L pair and sums (3). This gives a
polynomial with nonnegative integer coefficients in n-1, separately
for the main and each correction aggregate. It counts actual nonzero
forms, not the complete ambient grid. An independent direct grid
enumeration at n=2 and n=3 checks the counter.

The critical target mass is exactly

\[
                       \sum_t n^{3|H_t|/4}.                \tag{4}
\]

The saved finite samples compare their integer budgets with rational
intervals for (4), obtained by an integer fourth-root calculation.
Their exploratory scores used floats only to choose candidates.
Acceptance and the all-dimension cost limitation use exact arithmetic.

These restrictions can reduce the original displayed budget. They also
reduce the target volumes. The comparison with (4), and Theorem 1 above,
show why the budget reduction is insufficient for the exponent target.

### One explicit restricted construction

The [featured witness](witness.json) uses the 22 external tripartitions
and grades with one coordinate of dimension one in each product. The
coordinate selected varies between products. The exact count gives

\[
 \underline R\left(\bigoplus_{t=1}^{22}M(A_t,B_t,C_t)\right)
 \le 4n^5+32n^4+102n^3+158n^2+118n+34.                     \tag{5}
\]

Every target has volume n^5. The ordered exponent triples, with dimensions
`(A_t,B_t,C_t)=(n^a,n^b,n^c)`, are:

| (a,b,c) | Products |
| --- | ---: |
| (0,1,4) | 1 |
| (0,3,2) | 1 |
| (1,2,2) | 7 |
| (1,3,1) | 2 |
| (1,4,0) | 1 |
| (2,1,2) | 1 |
| (2,2,1) | 4 |
| (2,3,0) | 1 |
| (3,1,1) | 4 |

The main aggregate contributes `4n(n+1)^4` positions; all correction
positions are included in (5). Compared with the classical rank upper
bound `22n^5`, the difference becomes

\[
18u^5+328u^4+2266u^3+7066u^2+8570u+678>0,
\qquad n=4+u,\ u\ge0.
\]

Thus (5) is a smaller border-rank budget for every integer n>=4.
It does not assert that a numerically stable finite-precision algorithm
has the same cost. Its 9/4 critical mass is only `22n^(15/4)`, and (1)-(2)
prove that this budget cannot reach it at any allowed n.

## 4. A tested escape from the common-support premise

The premise `|S_{t,r}|>=n_{t,r}+1` is substantive. On a grid of q=n+2
positions the centered pair

\[
 E=\begin{bmatrix}I_n\\-\mathbf1^T\\0\end{bmatrix},\qquad
 D=\begin{bmatrix}I_n\\0\\-\mathbf1^T\end{bmatrix}
\]

satisfies `E^T D=I_n`, but its common nonzero row support has only n
positions. It falls outside (1), and also outside the earlier full-target
fixed-grid theorem. This is a concrete alternative embedding, not an
assumption that a smaller target automatically makes the budget useful.

A bounded discovery experiment on general22 allows separate weights for
every ordinary/first-extra/second-extra coordinate pattern. It constrains
all nonpositive mixed grades by their complete coefficient patterns.
The no-correction systems are inconsistent over the recorded prime field
at n=2,3,4. Including the external correction subsets gives modular
solutions, but their cost exceeds the original cited budget at all three
bases. These finite modular results are retained in the discovery log.
They are **not** characteristic-zero impossibility proofs, all-n rank
constructions, or optimization certificates. The search is stopped here;
the common-support theorem does not close this alternative embedding
class.

## Mathematical status

The cost-floor argument and the restricted coordinate identity are
written and unreviewed. The external graded aggregation framework keeps
its source attribution. New embedding choices, explicit finite profiles,
and exact counts are local deductions and experiments. No historical
priority, independent mathematical review, formalization, tensor-rank
lower bound, or smaller matrix multiplication exponent is asserted.
