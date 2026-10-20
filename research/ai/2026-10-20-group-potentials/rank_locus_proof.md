# Rank-locus dimensions remove two SL(2,5) construction targets

October 20, 2026. AI-derived written proof by Codex, unreviewed and not Lean
formalized. No smaller matrix-multiplication exponent is established.

The argument below concerns arbitrary complex tensor degenerations. It does
not assume a coordinate-weight construction, a potential LP, or that a SAT
search is exhaustive. No historical priority claim is made for this application
of standard rank-locus and projective-dimension arguments.

## 1. Source slice geometry

Let the source be the multiplication tensor of a finite-dimensional semisimple
complex algebra

\[
A=\bigoplus_{i=1}^s M_{d_i}(\mathbb C),\qquad N=\dim A=\sum_i d_i^2.
\]

Use a nondegenerate trace pairing to identify the output with its dual. Slicing
on one tensor leg at \(x=(X_i)_i\) gives the regular multiplication operator,
whose matrix rank is

\[
\operatorname{rank} L_x=\sum_i d_i\operatorname{rank}X_i. \tag{1}
\]

Each group algebra C[G] has this form by its Fourier decomposition. The
nonzero scalar factors in its trace pairing do not change (1). Cyclic changes
of legs and matrix transposes make the same calculation available on every leg.

Fix integers \(0\le k_i\le d_i\). The affine cone

\[
V_k=\{(X_i):\operatorname{rank}X_i\le k_i\text{ for every }i\}
\]

has dimension

\[
D(k)=\sum_i k_i(2d_i-k_i), \tag{2}
\]

and every one of its slices has rank at most
\(R(k)=\sum_i d_i k_i\). For (2), rank-exactly-k matrices form a dense open
part of the rank-at-most-k determinantal variety. Factoring as a full-column
matrix times a full-row matrix has 2dk parameters and the free GL(k) change
of the middle basis has dimension k squared, giving 2dk-k squared. Products
of these varieties add dimensions. These are statements over C.

## 2. A necessary degeneration inequality

Sort the target dimensions as \(a\le b\le c\). Contracting its largest leg,
of dimension bc, means choosing a b by c matrix Y. The resulting slice of
\(M_{a,b,c}\) has rank \(a\operatorname{rank}Y\). Consequently every nonzero
slice on that leg has rank at least a.

**Theorem.** A degeneration from the multiplication tensor of A to
\(M_{a,b,c}\) requires, for every rank choice with \(R(k)<a\),

\[
\boxed{N\ge bc+D(k).} \tag{3}
\]

Equivalently, put

\[
D(r)=\max\left\{\sum_i k_i(2d_i-k_i):
             \sum_i d_i k_i\le r,\quad0\le k_i\le d_i\right\}.
\]

Then a necessary condition is \(N\ge bc+D(a-1)\).

**Proof.** First take arbitrary linear restriction maps to the target spaces.
Dualizing the largest-leg map gives a linear map
\(F:\mathbb C^{bc}\to A\). If F has a kernel, a nonzero target parameter
in that kernel gives a zero slice. Otherwise its image E has dimension bc.

Suppose \(bc+D(k)>N\). The projectivizations of E and \(V_k\) have dimensions
bc-1 and D(k)-1 in projective space of dimension N-1. Their dimension sum is
at least N-1, so the projective dimension theorem forces an intersection.
Equivalently, successively intersecting a nonempty projective variety with
at most its dimension many hyperplanes cannot empty it. Thus some nonzero
parameter maps into \(V_k\), giving slice rank at most \(R(k)\). Linear maps
on the other two tensor legs cannot increase that rank.

The property "some nonzero parameter has slice rank at most R(k)" is closed
in the target tensor space. Indeed, the incidence set consisting of a tensor
and a projective parameter where all (R(k)+1)-minors vanish is closed, and
projection from the projective parameter factor is proper, hence closed.
It therefore persists under degeneration, including arbitrary basis changes.
But the target has no such nonzero parameter when \(R(k)<a\), a contradiction.
This proves (3). QED.

The closedness step matters: a condition requiring an *invertible* parameter
matrix would be open and cannot be substituted into this argument.

## 3. Explicit SL(2,5) exclusion witnesses

The source degrees 1,2,2,3,3,4,4,5,6 are independently replayed from the exact
central-idempotent certificate in this investigation; its dimension is 120.
Take rank at most one in one degree-six block and one degree-two block,
and zero in all other blocks. Then

\[
R=6+2=8,\qquad D=(2\cdot6-1)+(2\cdot2-1)=11+3=14.
\]

Thus:

| Target | Largest input bc | Minimum nonzero target slice | Required source dimension | Actual |
| --- | ---: | ---: | ---: | ---: |
| M(9,9,12) | 108 | 9 | 108+14=122 | 120 |
| M(9,10,11) | 110 | 9 | 110+14=124 | 120 |

Both targets are impossible from this group-algebra tensor, even under general
complex tensor degeneration. This sharpens the unverified agent-board report
that listed the coordinate-potential constructions as open. It does not rely
on that report's negative experiments or counting claims.

For M(10,10,10), the maximum D at rank budget nine is 16, for example from
rank one in a degree-six and a degree-three block. Its required dimension is
100+16=116, so this screen does **not** exclude it from dimension 120.

The exact program enumerates every sorted shape with a>=2 and bc<=120 and
certifies the strict source degree-sum gate at exponent 9/4 using rational
root intervals. Seven shapes pass that numerical gate. Six violate (3).
Only **(10,10,10)** survives this particular screen. A surviving screen is not
a construction.

## 4. Other consequences and limits

The same screen removes the tested affine-group shapes
C13:C3 -> M(6,6,6), C17:C4 -> M(8,8,8), M(7,7,9), M(7,8,8),
and C19:C3 -> M(6,6,9), M(6,7,8), independently of the untraced SAT outcomes.
It also removes C31:C5 -> M(12,12,12) and C31:C6 -> M(13,13,13).

C29:C4 -> M(10,10,10) and C31:C6 -> M(12,13,13) survive the screen.
Their coordinate-potential and arbitrary-degeneration status is not decided
by this note. Nor does the screen exclude tensor-power constructions whose
dimensions differ from the finite instances tested here.

## 5. Exact verification

`rank_locus_obstruction.py` maximizes (2) with an integer knapsack dynamic
program. It exports the individual block ranks, actual regular rank, variety
dimension and dimension deficit for every accepted exclusion. The written
projective argument is the all-size proof; the program checks its finite data.

```sh
python3 research/ai/2026-10-20-group-potentials/rank_locus_obstruction.py \
  --output results/group-potentials-2026-10-20/rank_locus_obstruction.json
```

The source certificate, conditional numerical gate and actual degeneration
remain separate objects. This result eliminates finite construction targets;
it proves no new upper bound on omega.
