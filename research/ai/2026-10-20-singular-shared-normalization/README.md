# A concrete singular shared-map family that survives the moving tests

October 20, 2026. AI-derived written proof and exact finite controls. This is
a construction of shared maps and moving linear tests, **not a convolution
degeneration to the fat-point target and not a smaller matrix multiplication
exponent**. The missing two tensor maps are stated explicitly below.

## 1. Question and outcome

The [fixed shared-map argument](../2026-10-20-koszul/arbitrary_shared_basis.md)
requires asymptotically 50 percent source overhead for the canonical target
`T_m`. One possible extension was to transport its catalecticant through a
singular shared map, normalize the two auxiliary spaces, and recover the
same rank obstruction from a concise limiting test.

That proposed extension does not follow from auxiliary conciseness. For every
even `m=2s>=4`, the explicit family here has the following properties:

- Its shared map is invertible away from zero and has a Laurent inverse with
  only a simple pole.
- The central limiting test is concise on both auxiliary spaces. It satisfies
  the stronger subspace-image inequality in Section 4.
- The same shared family passes **every** transported shared catalecticant
  test against the one-copy target at source length `B=N=m(m+1)/2`.
- The central test is sharp: its target rank equals the source allowance
  `N+s-1`.

This identifies explicit shared maps for a construction search. It also
preserves a rejected proof route: auxiliary conciseness, even strengthened
by the subspace-image inequality below, cannot restore the fixed-map bound.
No claim is made about all possible normalizations or other invariants.

## 2. The maps, with all conventions fixed

Work over the rational numbers, and hence over the complex numbers. Put

\[
m=2s,\qquad D=m-1,\qquad N=m(m+1)/2,
\qquad c(t)=(1,t,\ldots,t^D)^{\mathsf T}.
\]

Choose the distinct nonnegative rational nodes `t_j=j`, for `0<=j<=D`.
Let `V` be the square Vandermonde matrix whose column `j` is `c(t_j)`. Set

\[
P_\epsilon
=V\operatorname{diag}(\underbrace{1,\ldots,1}_{s+1},
                       \underbrace{\epsilon,\ldots,\epsilon}_{s-1})
 V^{\mathsf T},\qquad A_\epsilon=P_\epsilon^{-1}. \tag{1}
\]

Here `A_epsilon` is the proposed map on the shared **source** leg. In particular,

\[
\det P_\epsilon=(\det V)^2\epsilon^{s-1},\qquad
A_\epsilon=V^{-\mathsf T}
 \operatorname{diag}(1,\ldots,1,\epsilon^{-1},\ldots,\epsilon^{-1})
 V^{-1}. \tag{2}
\]

Thus `A_epsilon=A_regular+epsilon^(-1) A_pole`, with rational constant
matrices. The two coefficient matrices, and `P_0,P_1`, are exported for
`m=4` by the verifier. The notation in (1) avoids a dual-space ambiguity:
`P_epsilon` acts on the same coefficient-vector space as `A_epsilon`, and
their product is the identity.

For every `0<=q<=D`, put `h=D-q` and use the established structured map

\[
\Delta_q(X_i)=\sum_{r+t=i}U_r\otimes V_t,
\quad 0\le r\le q,\quad 0\le t\le h.
\]

In this formula the symbols `V_t` are auxiliary basis vectors; they do not
denote columns of the matrix `V` in (1). Define

\[
\Delta_{q,\epsilon}=\Delta_q\circ P_\epsilon.
\]

Since `P_epsilon` is a moment matrix, its coefficients give

\[
\Delta_{q,\epsilon}(X_i)
=\sum_{j=0}^{D}d_j(\epsilon)t_j^i
 (1,t_j,\ldots,t_j^q)^{\mathsf T}
 \otimes(1,t_j,\ldots,t_j^h)^{\mathsf T}, \tag{3}
\]

where `d_j=1` for `j<=s` and `d_j=epsilon` otherwise. In particular these
moving tests are regular at zero, and

\[
\Delta_{q,\epsilon}A_\epsilon=\Delta_q. \tag{4}
\]

If maps on the other two source legs completed an actual tensor degeneration,
(4) would bound the transported flattening rank by `B+q` at every nonzero
parameter. Taking its limit is legitimate because the moving test itself
is regular.

## 3. Exact target ranks, for every catalecticant degree

Use the canonical target from
[the all-dimension construction criterion](../2026-10-20-koszul/all_dimension_targets.md):

\[
T_m=\sum_{a+b+c+d=D}X_{a+c}Y_{a,b}Z_{c,d}.
\]

Its block with `a+b=ell` is `C(ell+1,D-ell+1)` on its output-shared leg.
After applying `Delta_(q,0)` and flattening `(U,Y)` against `(V,Z)`, that
block has entries

\[
H_{q,\ell}[(r,a),(t,c)]
=\sum_{j=0}^{s}t_j^{r+a}t_j^{t+c}. \tag{5}
\]

The powers in the row factor range from zero to `q+ell`; the column powers
range from zero to `2D-q-ell`. Repeated powers merely duplicate rows or
columns. Consequently

\[
\operatorname{rank}H_{q,\ell}
=\min\{s+1,q+\ell+1,2D-q-\ell+1\}. \tag{6}
\]

For a direct verification of the lower bound, let the displayed minimum
be `r`. Select one row and column of each degree `0,...,r-1`. Their square
submatrix is the Gram matrix of these monomials evaluated at `s+1` distinct
real nodes, with positive weights. Its Vandermonde evaluation matrix has
row rank `r`, so the Gram determinant is positive. The upper bound follows
from (5) and the numbers of distinct powers. This is a proof over the real
numbers of a rational nonzero minor, so the same rank holds over `C`.

The blocks occupy disjoint nonshared spaces and their ranks add. If
`q'=min(q,D-q)`, then `0<=q'<=s-1`, and summing (6) gives

\[
R_q:=\operatorname{rank}L_{\Delta_{q,0}}(T_m)
=2s(s+1)-\frac{(s-q')(s-q'+1)}2. \tag{7}
\]

Indeed, for `q<=s-1` only the initial `s-q` block ranks lie below `s+1`;
their deficits are `s-q,...,1`. Transposing the block matrices handles
`q>=s`. Since `N=2s^2+s`, (7) yields

\[
R_q=N+q'-\binom{s-q'}2\le N+q. \tag{8}
\]

The source rank `rank L_(Delta_q)(C(m,B))=B+q` was proved in
[source_obstructions.md, Section 2](../2026-10-20-koszul/source_obstructions.md).
Its proof groups source rows by `r+j`; the distinct rows have disjoint
support. Therefore (8) proves the claimed survival of every moving test at
`B=N`. At `q=s-1` the rank is exactly `N+s-1`, while the fixed identity
test has target rank `N+(s-1)s`. For example:

| m | N | Central q | Fixed target rank | Moving limit rank | Source allowance |
|---:|---:|---:|---:|---:|---:|
| 4 | 10 | 1 | 12 | 11 | 11 |
| 6 | 21 | 2 | 27 | 23 | 23 |
| 8 | 36 | 3 | 48 | 39 | 39 |
| 10 | 55 | 4 | 75 | 59 | 59 |

The claim is for one copy of `T_m`. Taking `k` identical copies multiplies
the left side of (7) by `k`, whereas the source allowance is `kN+q`; thus
this argument does not establish the same survival for arbitrary `k>1`.
One copy at each unbounded `m` would already be sufficient for the existing
asymptotic construction criterion, if the missing degeneration were found.

## 4. Auxiliary conciseness and a stronger subspace inequality

Take `q=s-1`, so the auxiliary dimensions are `s` and `s+1`. The limit
in (3) uses `s+1` independent coefficient covectors `c(t_j)` on the shared
space. Its second auxiliary vectors are a Vandermonde basis; its first
auxiliary vectors have the property that every `s` of them are independent.
It follows at once that both auxiliary flattenings have full rank. Its
shared flattening has rank exactly `s+1`, below the original dimension `2s`.

There is also the following explicit stronger fact. For a nonzero subspace
`E` of the dual of the first auxiliary space, of dimension `r`, take the
span of all contractions by elements of `E` and arbitrary shared vectors.
This span, in the second auxiliary space, has dimension at least `r+1`.

To prove it, independence of the shared covectors allows each node's
coefficient to be selected separately. A node contributes unless its first
auxiliary vector lies in `E`'s annihilator, which has dimension `s-r`.
General position puts at most `s-r` of the `s+1` node vectors there.
At least `r+1` remain, and their second auxiliary vectors are independent.
In particular the image dimension is at least `(s+1)r/s`, strictly greater
when `r<s`. No stability theorem is needed for this elementary statement.

Thus any attempt to recover the old target rank from only these auxiliary
rank or subspace-image conditions has this exact counterexample. It does
not exclude a stronger argument that uses additional compatibility with
the two still-missing source maps.

## 5. The concrete construction problem left open

For `m=4`, (1) uses the nodes `0,1,2,3` and diagonal weights `(1,1,1,epsilon)`.
The construction question initially posed was to find Laurent maps

\[
Y_\epsilon:\mathbb C^{10}\longrightarrow\mathbb C^{10},\qquad
Z_\epsilon:\mathbb C^{13}\longrightarrow\mathbb C^{10}
\]

such that

\[
(A_\epsilon\otimes Y_\epsilon\otimes Z_\epsilon)C(4,10)
\longrightarrow T_4. \tag{9}
\]

For general `m=2s`, replace these two maps by dimensions `N->N` and
`N+D->N`. The maps may have poles and cancellation; restricting both to
regular leading matrices is an additional assumption, not a normal form.
No such pair has been constructed here, at `m=4` or asymptotically.
Even an exact `m=4` solution alone would not establish the unbounded
construction premise needed for an exponent improvement.

The subsequent [first and second order proof](../2026-10-20-shared-tangent-lift/README.md)
now excludes integer-power Laurent completions at `B=N` for this exact
parameterization and for its quadratic ramification. Its proof uses the
sharp central rank, not a failure of the limiting rank tests above.
Higher ramification is outside that claim. The construction search now
also allows `B=N+O(m)`, whose asymptotic cost remains one and whose extra
rank allowance avoids this particular obstruction.

There is no numerical acceptance criterion in this note. A proposed pair
must be checked on every tensor coefficient, including all required zeros
and every negative Laurent coefficient. Small residuals on selected
coefficients would not verify (9).

## 6. Reproduction, history, and review status

Run from the repository root:

```sh
python research/ai/2026-10-20-singular-shared-normalization/verify_family.py --max-s 5 --output results/singular-shared-normalization-2026-10-20/family.json
```

The standard-library verifier uses rational Gaussian elimination. It builds
the actual transformed block matrices independently of (6), checks their
ranks for every `q,ell`, checks the fixed identity and nonsingular moment
controls, verifies the source support count, and exports the exact `m=4`
shared Laurent matrices. It also checks the auxiliary ranks. The all-size
claims rest on the proof above, not on the finite run.

The investigation first tried to preserve the fixed catalecticant obstruction
by normalizing a singular shared map. Sparse concise counterexamples showed
that conciseness alone was insufficient. The positive Vandermonde family
above strengthens that diagnosis and gives exact shared maps for the next
construction attempt. A rederivation of the already-existing intermediate
weight bound was recognized as overlap and is not counted as a new result.

The sibling higher-Hankel/Segre argument was checked separately by this agent
within the same AI session. The support-divisor and bilinear propagation
steps passed that check, with one suggested field-extension clarification.
That is same-session AI review, not external independent certification.

All new statements here remain externally unreviewed and unformalized. The
matrix multiplication exponent remains at the externally established `9/4`.

## Explicit algebra smoothing and a broader next model

The [curvilinear smoothing note](curvilinear_krylov.md) gives an all-size
rational degeneration of the truncated univariate algebra to the plane
fat-point algebra, using exponential jets. It identifies the extra
consecutive-moment condition needed for the corresponding convolution
construction. That condition is not supplied by algebra smoothability;
at size three a square-dimension obstruction excludes the stated
algebra-compatible realization even though general tensor maps exist.
Exact controls through size six are preserved with the note.

The next model permits two independent nonshared maps and
[extra shared source coordinates](../2026-10-20-construction-sprint/shared_dimension_slack.md).
These extensions remain construction questions. The algebra smoothing
alone does not establish a convolution degeneration or a smaller exponent.
