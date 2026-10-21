# A partial matrix target and a fixed-seed first-cross obstruction

This package preserves twelve bounded construction probes for the source
`Q(6,4)` and the off-diagonal bulk of `M(5,4,5)`. None is an exact
construction. It also proves a narrower exact result: a specified
monomial `M2` seed cannot acquire the required first cross edges when
all new long rows have order one and the corresponding A rows have
poles of order at most one.

The obstruction does not use a tight saturation count. It does not
exclude other leading subspaces, different orders for the new long
rows, higher A poles, or general Laurent families. It does not improve
the matrix multiplication exponent.

## 1. The partial target and its correction cost

The full target is

\[
M(N,4,N)=\sum_{i,j<N}\sum_{k<4}a_{ij}b_{jk}c_{ki}.
\]

Omit the central A diagonal and the two outermost diagonals on each
side. For `N>=3`, these are `N+6` A entries. Restoring their standard
products costs at most `4N+24` rank-one terms. Therefore a construction
for every retained coefficient along an unbounded sequence of N would
fit the separate correction-budget criterion.

At `N=5` the retained coordinates satisfy `|i-j|=1` or `2`. The target
has format `(14,20,20)`, 56 nonzero products, and 5,600 coefficient
positions. The finite correction cost is 44. No all-N construction or
recurrence is proved by this package.

## 2. Exact leading seed

Use the original source

\[
Q(6,4)=\sum_{p,q<6}\sum_{y,v<4}A_{pq}B_{y,q+v}C_{p+y,v}.
\]

The stored matrices reverse each convolution output, so their source
indices are `(p,q)`, `(y,8-q-v)`, and `(8-p-y,v)`.

The monomial subspaces `U=span(1,t^2)` and `W=span(1,t)` give an exact
`M(2,4,2)` restriction. On two old outer vertices, identify

\[
A_{2h,2j}\mapsto a_{hj},\quad
B_{y,2j+v}\mapsto b_{j,2y+v},\quad
C_{2h+y,v}\mapsto c_{2y+v,h}
\tag{1}
\]

for `h,j,y,v` in `{0,1}`, and set the other indicated coordinates to
zero. Retain only the two off-diagonal A entries of this seed.

Before applying its A map, the two fixed long maps give an A-flattening
of rank 16. Its kernel is exactly

\[
K_0=\operatorname{span}\{A_{pq}:p\ge4\text{ or }q\ge4\}.
\tag{2}
\]

Every nonzero slice has `p,q<4`. The `y=v=0` coefficients supply an
explicit 16-by-16 identity minor. Both the old vertex choices `(0,1)`
and `(1,2)` are checked exactly.

The native old C identification is especially relevant below:

\[
z=2h+\alpha,\quad v=\beta,\quad
C^0_{z,v}=c_{2\alpha+\beta,h},
\qquad h,\alpha,\beta\in\{0,1\}.
\tag{3}
\]

Thus the first old outer vertex uses `z=0,1`, and the second uses
`z=2,3`, with both values of `v` present at each vertex.

## 3. Laurent chart under consideration

All old long rows have the leading maps in (1). All new B rows and
new C rows vanish to order at least one. A row intended for an
old/new cross edge has a pole of order at most one. Higher Taylor
coefficients are allowed; they do not contribute to the first cross
coefficient in this chart.

For a cross A row with leading coefficient `a`, cancellation of its
negative-power coefficient on old B and old C forces `a` into `K0`.
In a new-B/old-C coefficient, the terms with `p>=4` vanish because
the old C map is supported on `z<4`. Hence only

\[
0\le p<4,\qquad q=4,5
\tag{4}
\]

survive. The resulting tensor has format `(8,12,8)` and 40 nonzero
coefficients. The exact verifier compares all 768 coefficient
positions with the following polynomial-pencil form.

## 4. The unit-pencil obstruction

Let `J` be the four-by-four upper nilpotent shift, so
`(J^p)_{y,z}=1` exactly when `z=y+p`. A cross A row has two polynomial
coefficients

\[
(r,s)\in R^2,\qquad R=\mathbb C[u]/(u^4),
\]

where `r` is its coefficient at `q=4` and `s` at `q=5`.
At any one new B outer vertex, put

\[
X_j[:,y]=B^1_{y,4+j},\qquad j=0,1,2.
\]

The two old-C blocks, ordered first by `v` and then by `z`, are

\[
S(r,s)=
\left[X_0r(J)+X_1s(J)\ \middle|\
      X_1r(J)+X_2s(J)\right].
\tag{5}
\]

Suppose a row `f=(r,s)` gives a target edge from the first old outer
vertex to a new B outer vertex `a`. The target is an isomorphism on
the four C coordinates belonging to that old vertex. In particular,
it cannot annihilate both `z=0` columns. Thus `r(0)` or `s(0)` is
nonzero. Equivalently, one coefficient is a unit in R.

Now consider a different new B vertex `b`. The row f has zero target
coefficient there. Suppose first that r is a unit, and set `h=s/r`.
Writing the three matrices at b as `Y0,Y1,Y2`, the two zero blocks
in (5) imply

\[
Y_1=-Y_2h(J),\qquad Y_0=Y_2h(J)^2.
\tag{6}
\]

For any other row `g=(a,b)`, write its two blocks at this new vertex
as `Z0,Z1`. Since all polynomials in J commute, (6) gives

\[
Z_0=-Z_1h(J).
\tag{7}
\]

If g gives an edge from the second old outer vertex to this new B
vertex, each block vanishes on `z=0,1`. Therefore `rank Z1<=2`.
Equation (7) shows that the combined block matrix has rank at most
two. The target edge has rank four, a contradiction.

If s is a unit, the same calculation with `h=r/s` gives
`Z1=-Z0 h(J)` and the same contradiction.

Consequently this chart cannot contain two cross edges

\[
(\text{first old vertex},a),\qquad
(\text{second old vertex},b),\qquad a\ne b.
\]

Both tested partial targets require such edges. For old vertices
`(0,1)`, take new B vertices `2` and `3`. For old vertices `(1,2)`,
take new B vertices `0` and `3`.

This proof permits unused first-jet directions outside the target A
image. In particular, it does not require the earlier tight
saturation assumption. The other same-session worker independently
checked the polynomial reduction, the two unit cases, and the old-C
support identification. This is an AI-derived argument with
same-session review, not an external theorem or independent
mathematical validation.

## 5. Bounded numerical records

Twelve complete records are retained in
`results/bulk-partial-2026-10-21/`. The separate `experiments.json`
indexes their parameters, best sampled residuals, actual update
counts, and stops. Every record includes all numerical maps and the
full reported history. Ordinary-map records also preserve their
composition with the original 36-dimensional source factors.
The first two runs initially retained maps only through update 1,100.
They were replayed to preserve their final update-1,200 maps. Their
original checkpoints remain in `initial-checkpoints/`, and the replay
logs and provenance are retained beside the completed records.

The ten ordinary probes include the fixed root14 point, released
long subspaces, the full source with integer or finite cyclic
gradings, and two continuations balanced by the partial target's
stabilizer. All 5,600 coefficient positions were checked. The best
sampled unrestricted residual was approximately `0.1982693`; its
first sampled norm stop was approximately 123. This is not a
candidate identity.

The two output-flag probes used A weights `0,-1,-2` for old/old,
cross, and new/new entries. Old long rows had weight zero and new
long rows weight one. Every coefficient of exponent at most zero
was checked. Positive coefficients are allowed by this proposed
degeneration and were omitted from its objective.

Both flag runs stopped at their first 300-update norm check. For old
vertices `(0,1)`, the constrained relative residual was `0.1604250`,
the largest negative-power coefficient was `0.2308297`, and the map
norms were approximately 3,514. For old vertices `(1,2)`, these
numbers were `0.2439153`, `0.1976759`, and approximately 5,521.
Neither run cancels the negative Laurent coefficients. The much
smaller target-only residual in the first run cannot be used as
evidence of a degeneration.

Norm stopping was sampled at the stated reporting interval. A budget
of 100 was not an enforced bound between checkpoints. The flag
records retain this distinction and all ignored positive-coefficient
diagnostics. The exact obstruction above is independent of these
numerical outcomes.

## 6. Reproduction

Exact verification needs only the root verification dependencies:

```sh
python research/ai/2026-10-21-bulk-partial/verify.py
python -m unittest discover -s tests -p 'test_bulk_partial.py'
```

The two discovery scripts additionally require NumPy. They are not
part of the exact verifier. A representative stopped flag run is:

```sh
OPENBLAS_NUM_THREADS=1 python research/ai/2026-10-21-bulk-partial/q64_bulk_flag.py \
  --old-vertices 0,1 --seed 202610451 --iterations 1800 \
  --report-every 300 --balance-target --output /tmp/bulk-flag-replay.json
```

The ordinary discovery program reads the exact root14 family from
`results/quantum-correction-2026-10-21/N5-m4-family.json`. Its release
flags replace the relevant local maps by the original source basis;
`--weight-modulus 1` removes the grading restriction. Historical
scratch paths inside the stored numerical records identify their
original inputs. The complete inputs and continuation records are
also retained in the repository.
