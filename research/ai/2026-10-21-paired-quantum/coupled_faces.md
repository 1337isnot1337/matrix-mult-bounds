# Two explicit coupled Laurent limits of the paired source

**Result.** There are explicit complex tensor degenerations

\[
P_3\rightsquigarrow F_0,\qquad P_3\rightsquigarrow F_1,
\]

where both intermediate tensors have format `(9,15,15)`, with 241 and
108 nonzero rational coefficients respectively. The complete sparse
tensors and all local-map exponents are in
[`coupled-faces.json`](../../../results/paired-quantum-2026-10-21/coupled-faces.json).
The verifier reconstructs them from the paired source over `Q(q)`.

This is a positive construction of two intermediate tensors. **It is not
a construction of a matrix multiplication direct sum and does not
improve the exponent.** The claims and interpretations below are written
and unreviewed, October 21, 2026, under `AI-PAIRED-QUANTUM-002`.

## 1. The local maps and polynomial parameter path

Use the maps `M_A(q), M_B(q), M_C(q)` from
[the exact paired quantum calibration](README.md), with `a=3`.
Their row labels are `(k,l)`, ordered by increasing `k` and then `l`.
Let `r_X` be the vector of minimum row valuations at `Phi(q)=q^2+1`.
These integers are recomputed from the rational local maps.

For either family, choose its positive integer `D` and concatenate the
three integer weight vectors `W_A,W_B,W_C` listed below. Set

\[
q(t)=i(1-t^D/2),\qquad
L_X(t)=\operatorname{diag}
 \left(i^{\eta_{X,j}}t^{W_{X,j}-D r_{X,j}}\right)M_X(q(t)).       \tag{1}
\]

The fixed local phases `eta` are obtained by an exact binary linear
system in the verifier and listed in the certificate. They only convert
the leading coefficients from `Q(i)` to `Q`. Omitting them gives an
isomorphic complex leading tensor.

For `F_0`, take `D=2` and

```text
W_A = [0,1,0,1,0,1,0,1,0]
W_B = [0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0]
W_C = [0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0]
```

For `F_1`, take `D=8` and

```text
W_A = [0,5,2,7,4,5,-6,7,-6]
W_B = [0,-3,2,-9,4,-7,6,-3,-6,-9,4,-7,-6,-1,4]
W_C = [0,5,2,7,4,1,6,5,2,7,12,1,2,-1,12]
```

Every map in (1) is invertible for generic `t`. The path is polynomial,
and its uniformizer satisfies the exact identity

\[
q(t)^2+1=t^D-t^{2D}/4.                                      \tag{2}
\]

In particular its leading uniformizer coefficient is one.

## 2. Complete Laurent cancellation proof

Let `R_abc(q)` be a coefficient of the paired source after applying the
three unnormalized maps `M_X(q)`. The exact contraction has 288 nonzero
rational functions; all other coefficients are identically zero.
The contraction is computed by summing every source contribution in
`Q(q)`, so canceled coefficients are removed only after exact summation.

Write

\[
v_{abc}=\nu(R_{abc})-r_{A,a}-r_{B,b}-r_{C,c}.
\]

There are 182 coefficients with `v=0`, 93 with `v=1`, and 13 with
`v=2`. By (1) and (2), the corresponding coefficient of the tensor
family has `t`-valuation

\[
E_{abc}=D v_{abc}+W_{A,a}+W_{B,b}+W_{C,c}.                    \tag{3}
\]

The verifier checks (3) for **every** one of the 288 nonzero coefficient
functions, with exact integer arithmetic. The results are:

| Family | Number at exponent 0 | Number at exponent 2 | Number at exponent 8 | Number at exponent 16 | Number at exponent 24 |
|---|---:|---:|---:|---:|---:|
| `F_0` | 241 | 47 | 0 | 0 | 0 |
| `F_1` | 108 | 0 | 97 | 77 | 6 |

Thus no tensor coefficient has a pole. The exponent-zero coefficients
are precisely the cyclotomic leading residues of `R_abc`, multiplied by
the local phases in (1); all positive-exponent coefficients vanish in
the limit. This proves both displayed tensor degenerations.

Rational local maps suffice to define these limits. If finite Laurent
polynomial maps are desired, expand each rational entry and truncate
above an order larger than the sum of the other two pole orders. Such a
truncation preserves every coefficient through order zero. This does
not require an unverified numerical fit or an assumption that a small
residual is zero.

## 3. Exact flattening and Koszul ranks

Exact rational row reduction gives first, second, and third flattening
ranks `(9,15,15)` for both tensors. For the first-leg Koszul maps

\[
\bigwedge^p A\otimes B^*\longrightarrow
\bigwedge^{p+1}A\otimes C,
\]

the complete ranks are:

| Power `p` | `F_0` | `F_1` | `M(1,3,3) direct_sum M(3,3,2)` |
|---:|---:|---:|---:|
| 0 | 15 | 15 | 12 |
| 1 | 128 | 124 | 108 |
| 2 | 468 | 438 | 402 |
| 3 | 960 | 874 | 825 |
| 4 | 1210 | 1085 | 1035 |
| 5 | 960 | 861 | 822 |
| 6 | 468 | 427 | 408 |
| 7 | 128 | 121 | 117 |
| 8 | 15 | 15 | 15 |

The ranks of the intermediate tensors are computed directly, using
their exact coefficients. Cartan weights split the matrices into smaller
blocks without changing their rank. The target ranks are independently
reproduced with the maintained
[matrix Koszul formula](../2026-10-20-paired-sources/matrix_euler.md).
Both tensors pass these necessary tests. Passing them does not imply
the existence of a target degeneration.

## 4. Why an ordinary second restriction cannot reach the target

The proposed small direct sum has format `(9,12,15)`. Its maximum
first-slice rank is

\[
3\min(1,3)+3\min(3,2)=9.                                   \tag{4}
\]

For both `F_0` and `F_1`, slice index 6 is an invertible `15`-by-`15`
matrix, with exact determinant

\[
1/31701690482688.
\]

Suppose an ordinary restriction produced the proposed concise target.
Its first and third maps would be invertible, since those leg dimensions
are retained in full. Its second map would have rank 12. Applying these
maps to the invertible slice produces a target slice of rank 12, contrary
to (4). Hence neither intermediate tensor admits that ordinary
restriction. A further singular degeneration of `F_0` remains possible.

## 5. A stronger exclusion for `F_1`

The exact rank of first slice index 2 of `F_1` is two. This excludes
**every further degeneration** of `F_1` to the proposed small direct sum
while keeping a concise first space of dimension nine.

Here is the required closedness argument. For fixed spaces `A,B,C`, let

\[
Z_r=\{(T,[x])\in(A\otimes B\otimes C)\times\mathbb P(A^*) :
       \operatorname{rank}T(x)\le r\}.
\]

The `(r+1)`-minors make `Z_r` closed. Projection along the projective
factor is a closed map; this is the standard properness of projective
space, for example
[Stacks Project, Section 29.44, Lemma 29.44.5](https://stacks.math.columbia.edu/tag/01W7).
Therefore tensors admitting some projective first slice of rank at most
`r` form a closed set. That property is invariant under invertible first
changes of basis and is preserved by arbitrary maps on the other legs.
It consequently persists under their limits.

Every nonzero first slice of the proposed direct sum has rank at least
three: each nonzero matrix block contributes three times a positive
matrix rank. Its first flattening is injective, so a projective first
slice cannot become the zero matrix either. Taking `r=2` gives the
contradiction. This exclusion includes independent Laurent flags and
arbitrary first-space mixing; it is not limited to monomial maps.

It leaves other targets with different first-space dimensions or smaller
minimum slice ranks outside the claim. For the present small direct-sum
target, the useful continuation is `F_0`.

## 6. Reproduction

```sh
python research/ai/2026-10-21-paired-quantum/coupled_faces.py \
  --output results/paired-quantum-2026-10-21/coupled-faces.json
python -m unittest discover -s tests -p test_paired_quantum_faces.py -v
```

The maintained verifier has no SciPy, LP, or finite-field dependency.
Discovery used numerical linear programming to propose the two weight
vectors, followed by modular rank probes. The accepted results use only
the fixed vectors, formal rational-function contractions, exact
cyclotomic residues, and rational matrix ranks.
