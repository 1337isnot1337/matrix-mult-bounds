# Two restrictions on rectangular complete-grid aggregation

October 23, 2026. Owner-directed OpenAI Codex research. Written and unreviewed.

## 1. Fixed ordered shapes and arbitrary coordinate dimensions

Let F have d>=1 coordinates, and let a,b,c be nonnegative integers with
a+b+c=d. Take p ordered tripartitions `(U_t,V_t,W_t)` of F, all with
`(|U_t|,|V_t|,|W_t|)=(a,b,c)`. Assume conflict freedom: the three parts
`U_i,V_j,W_k` form a complete partition only when i=j=k.
Permuting the three cardinalities globally changes nothing. Permuting
them separately in different rows is outside this fixed-shape theorem.

For each coordinate r choose an integer q_r>=2. Product t may use any
integer `1<=n_{t,r}<=q_r-1`. Its three matrix dimensions, in the convention
where the factors are X_AB,Y_BC,Z_CA, are

\[
 A_t=\prod_{r\in V_t}n_{t,r},\quad
 B_t=\prod_{r\in W_t}n_{t,r},\quad
 C_t=\prod_{r\in U_t}n_{t,r}.
\]

In particular `A_t B_t C_t=product_r n_{t,r}`. Denote the critical
asymptotic-sum mass by

\[
 S=\sum_{t=1}^p(A_tB_tC_t)^{3/4}.
\]

**Theorem 1.** If d<=32, every nonnegative displayed budget B that charges
the complete leading grid, `B>=product_r q_r`, satisfies B>S. It therefore
cannot certify an exponent at most 9/4 by direct asymptotic-sum substitution.
This includes rectangular matrices, anisotropic coordinate grids, and
different coordinate dimensions for different products.

### The combinatorial bound

Write

\[
 C_U={d\choose a},\quad C_V={d\choose b},\quad C_W={d\choose c},\qquad
 E=\frac{d!}{a!b!c!},\qquad D_L=E/C_L.
\]

The full tripartite hypergraph has the indicated subsets as its vertices
and all complete ordered tripartitions as its E edges. A vertex in class
L has degree D_L. Each degree is a positive integer.

No two selected products repeat a part in any class: a repeated U part,
for example, would give an off-diagonal edge `(U_i,V_j,W_j)`. Thus each
class has p selected vertices. They induce exactly p edges, by conflict
freedom. Every other edge meets a deleted vertex. Counting such incidences
gives

\[
 E-p\le(C_U-p)D_U+(C_V-p)D_V+(C_W-p)D_W
      =3E-p(D_U+D_V+D_W).
\]

Since `D_U+D_V+D_W-1>=2`, it follows that

\[
 p\le P(a,b,c):=
 \min\left(C_U,C_V,C_W,
 \left\lfloor\frac{2E}{D_U+D_V+D_W-1}\right\rfloor\right).       \tag{1}
\]

Taking the minimum with the individual capacities is necessary for
unequal shapes. Setting a=b=c=N recovers the earlier balanced gate.

### Exact cost comparison

For every positive real x, weighted arithmetic-geometric mean gives
`x+1>=4*(x/3)^(3/4)`. Apply this separately at x=q_r-1. Then

\[
 \frac{B}{\prod_r(q_r-1)^{3/4}}
 \ge\frac{\prod_r q_r}{\prod_r(q_r-1)^{3/4}}
 \ge\frac{4^d}{3^{3d/4}},\qquad
 S\le p\prod_r(q_r-1)^{3/4}.                               \tag{2}
\]

For every unordered triple `0<=a<=b<=c`, `a+b+c=d`, and every d from
1 through 32, the exact integer check is

\[
             P(a,b,c)^4\,3^{3d}<4^{4d}.                   \tag{3}
\]

Permuting the three parts preserves (1), so this list covers every
ordered shape. Equations (1)-(3) prove the strict inequality B>S.
The complete table is in [certificate.json](certificate.json). The
verifier recomputes every shape and every integer, rather than testing
a selection of local dimensions.

At d=32 the largest cap is 64,512,240, attained at (10,11,11).
At d=33, shape (11,11,11) has cap 129,024,540 and fails (3).
That row marks the boundary of this argument, not an attained construction
or a sufficiency result. No claim is made that balanced shapes maximize
the bound in untested dimensions.

### Existence of the anisotropic corrected identity

The hypotheses above define actual restricted aggregation algorithms,
not only a hypothetical cost format. Here is the coordinate identity.
Over a characteristic-zero field set `E_r=[I;-1 ... -1]`, with q_r rows
and q_r-1 columns, and

\[
 D_r=E_r\left(I-\frac{J}{q_r}\right).
\]

Both column families are centered, and `E_r^T D_r=I`. For product t use
their first n_{t,r} columns. Assign E to X, D to Z, and assign E to Y
on U_t and D to Y on W_t, as in the parent proof. In each active pair
on a diagonal product the coordinate contraction is the identity.

In a mixed product let eta_r count membership of r in U_i,V_j,W_k.
If eta_r=2, exactly one factor uses that coordinate and its centered
column sum kills the term. The fixed ordered cardinalities give
`sum_r eta_r=a+b+c=d`. Therefore, if there is no eta=2 and the term is
not diagonal, conflict freedom implies a nonempty replicated set
`R=U_i intersect V_j intersect W_k` of eta=3 coordinates.

Let Q contain every nonempty subset of each such R. For P in Q use the
correction aggregate A(P), with products eligible in its three factors
only when `P subset U`, `P subset V`, `P subset W`, respectively. Then

\[
 A(\varnothing)+
 \sum_{P\in Q}\left(\prod_{r\in P}(-q_r)\right)A(P)
       =\bigoplus_{t=1}^p M(A_t,B_t,C_t).                    \tag{4}
\]

A replicated mixed term contributes the same remaining coordinate
form for each P subset R. The q_r factors cancel by
`sum_{P subset R}(-1)^|P|=0`. Different target dimensions do not affect
this factorization. The displayed budget is

\[
 B=\sum_{P\in Q\cup\{\varnothing\}}\prod_{r\notin P}q_r,
\]

so Theorem 1 applies when all these positions are charged. It does not
exclude a smaller cost obtained by deleting identically zero forms.

For mixed ordered cardinality shapes, conflict freedom alone is
insufficient for this proof: a centered survivor can have eta=0
coordinates and no eta=3 coordinate. The scalar-graded constructions
in the external paper impose additional conditions on those terms.
They are not included in Theorem 1.

## 2. Rigidity when one target fills every centered space

Keep the same fixed main grid forms and correction eligibility rule.
The following result does not require all products to have one shape,
or require every off-diagonal term to vanish.

**Theorem 2.** Suppose one retained diagonal target t uses
`n_{t,r}=q_r-1>=2` at every coordinate. Work over a characteristic-zero
field. In a linear combination of the fixed main grid forms and any
forms whose projection to `X_t tensor Y_t tensor Z_t` is zero, equality
with the desired diagonal product forces every main grid coefficient
to be one. For a Laurent-parameter degeneration to that product, every
main coefficient must be `1+O(lambda)`.

Consequently no main position can be removed by reweighting these same
forms, including in a degeneration. The theorem does not allow replacing
them by new linear forms or recombining them into new rank-one tensors.
It is not an actual tensor-rank lower bound.

### Local independence

Let `H_q={v in K^q:sum_i v_i=0}`, q>=3. The span of the coordinatewise
products of two vectors in H_q is all of K^q. Indeed, for any i choose
distinct j,k other than i. Then

\[
             (e_i-e_j)\mathbin{\odot}(e_i-e_k)=e_i.
\]

The columns of E and D above are two bases of H_q. Hence their pairwise
coordinate products also span K^q. Equivalently, the q row tensors
`E(i,:) tensor D(i,:)` are linearly independent in
`K^(q-1) tensor K^(q-1)`.

Project a main grid form to the independent variables of target t.
After regrouping coefficient factors by coordinate, the projected form
at position `(i_r)_r` is the tensor product of those local row tensors.
Tensor products of independent families are independent. There are
exactly `product_r q_r` such projected forms, and their unit-weight sum
is the diagonal matrix product.

For each nonempty correction subset P, the three t-blocks could all
appear only if `P subset U_t intersect V_t intersect W_t`, which is
impossible for a tripartition. Every correction form therefore projects
to zero on the diagonal block. Independence now forces unit weights.

For the Laurent statement, choose a constant left inverse of the matrix
whose columns are the independent projected forms. Applying it to an
error tensor in `lambda*K[[lambda]]` shows that each coefficient minus
one lies in that same ideal. This also covers arbitrary finite poles in
the original scalar coefficients; the conclusion eliminates their poles.

### Necessary hypotheses and finite controls

For q=2, H_q has dimension one and its products span a one-dimensional
space. The two projected positions are equal up to scalar and can be
merged. Thus the requirement `q_r-1>=2` cannot be dropped.

For q=4 and a target restricted to the first two columns of the displayed
E,D, the third ordinary row of E is zero. The local product matrix has
rank three, not four, so that position can be omitted. This demonstrates
the concrete escape when no target fills the ambient centered space.

The verifier checks exact rational local matrices for q=2 through 8,
the q=4 restricted control, and the dual and centering identities. The
proof above, rather than those finite tests, establishes the general
dimension statement.

## Attribution and limits

The centering and correction framework and the asymptotic sum theorem
are external prior work, as credited in [README.md](README.md). The
fixed-shape counting extension, anisotropic cost argument and fixed-grid
independence proof are local written deductions. No historical priority
is asserted. Same-session reasoning checks and exact test results do
not supply independent mathematical review or formalization.

Theorem 1 limits a complete-grid upper-bound certificate. Theorem 2
limits reweighting fixed forms under a full-target hypothesis. Neither
excludes better rank decompositions, smaller or mixed targets with a
pruned grid, arbitrary source constructions, or a smaller matrix
multiplication exponent.
