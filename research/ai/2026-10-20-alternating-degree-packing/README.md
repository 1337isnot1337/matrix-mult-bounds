# Exact packing at the fixed-shared threshold

October 20, 2026. AI-derived construction and proof. No smaller matrix
multiplication exponent is established. The finite `C(4,11)` existence
control was already certified in
[mixed restrictions](../2026-10-20-mixed-restrictions/README.md); this note
does not claim that case as new. The contribution here is an explicit
all-dimension, all-replication construction meeting the prior fixed-shared
lower bound exactly. No historical priority outside this repository is claimed.

## 1. Statement

Write `D=m-1`, `N=m(m+1)/2`, and let

\[
T_{m,k}=\sum_{r=0}^{k-1}\sum_{a+b+c+d=D}
 X_{a+c}Y_{r,a,b}Z_{r,c,d}.
\]

Only the nonshared spaces are copied: the same `m` shared coordinates occur
in all `k` copies. Put

\[
q=\lfloor D/2\rfloor,\qquad
L=N+\lfloor D^2/4\rfloor=\lceil3m^2/4\rceil,
\qquad B=kL-q.                                           \tag{1}
\]

**Theorem.** There is an explicit coordinate Laurent degeneration

\[
C(m,B)\ \unrhd\ T_{m,k}
\]

whose shared map is the identity. Consequently (1) is the exact minimum
source length among degenerations with a regular shared map having an
invertible limit, by the
[prior lower bound](../2026-10-20-koszul/arbitrary_shared_basis.md).
That lower bound allows arbitrary Laurent maps on the other legs and
independent invertible shared identifications in every target sector.

At `m=4,k=1`, the construction uses `B=11`. At fixed or growing `k`,
the asymptotic ratio `B/(kN)` tends to `3/2` as `m` tends to infinity.
This is far above the cost-one family sought by the
[fat-point growth criterion](../2026-10-20-concavity-equivalence/fatpoint_growth_route.md).
The theorem proves a sharp construction boundary; it does not improve
the exponent or supply a singular shared-map completion at lower cost.

## 2. Alternating degree blocks

Order the degrees as

\[
0,D,1,D-1,2,D-2,\ldots.
\]

For each `i` with `0<=i<D-i`, give low degree `p=i` the start

\[
s_i=im+i^2
\]

and high degree `p=D-i` the start

\[
s_{D-i}=im+(i+1)^2=s_i+2i+1.                 \tag{2}
\]

If `m` is odd, the unpaired middle degree `i=D/2` is low and has the
same low-start formula. Set `h_p=0` for low blocks and `h_p=1` for high
blocks. In copy `r`, select source indices

\[
J_{r,p,a}=rL+s_p+p-a,\quad 0\le a\le p,
\]

\[
K_{r,p,c}=rL+s_p+p+c,\quad 0\le c\le D-p.       \tag{3}
\]

The substitutions, with all unselected source coordinates sent to zero, are

\[
Y^{\rm source}_{J_{r,p,a}}
 \longmapsto \epsilon^{h_p-2r}Y_{r,a,p-a},
\]

\[
Z^{\rm source}_{K_{r,p,c}}
 \longmapsto \epsilon^{-h_p+2r}Z_{r,c,D-p-c}.
                                                               \tag{4}
\]

Each selected source coordinate occurs at most once on its leg. Negative
powers in the individual maps are allowed. The full transformed tensor has
no negative powers.

## 3. Proof of the coordinate and valuation assertions

Within one low/high pair, put `l=s_i`. The selected intervals are

| Block | Selected Y interval | Selected Z interval |
|---|---|---|
| Low degree `i` | `[l,l+i]` | `[l+i,l+m-1]` |
| High degree `D-i` | `[l+2i+1,l+m+i]` | `[l+m+i,l+m+2i]` |

The next low start is `s_(i+1)=l+m+2i+1`. Both legs' selected intervals
are therefore pairwise disjoint. This includes a final unpaired low block.

A source term connects a selected Y index `j` to a selected Z index `z`
only when `0<=z-j<=D`. A low Y block can connect only to its own low Z
block. Indeed, its own pair's high Z interval begins one step after
`max(Y_low)+D`; all later Z intervals are farther away. The preceding high
Z interval ends one step before `min(Y_low)`; all earlier intervals are
farther away. The same inequalities also separate distinct low blocks.

Distinct high blocks do not connect to one another. For the next high
block, its minimum Z index exceeds the present high Y maximum plus `D`
by `2i+3`; every preceding high Z interval ends before the present high
Y minimum. Thus every unwanted term within a copy goes from a high Y
block to a low Z block, and has weight `1` in (4).

Wanted terms within a block satisfy

\[
K_{r,p,c}-J_{r,p,a}=a+c.
\]

Their shared coordinate is exactly `X_(a+c)`, and their weight is zero.
They give precisely the target coefficients in that block.

For `m=2s`, the largest selected Y index in one copy is
`3s^2-s`, and the largest selected Z index is `3s^2-1`.
For `m=2s+1`, these indices are `3s^2+2s` and `3s^2+3s`.
Equivalently, they are `L-q-1` and `L-1`. The stated source length
`B=kL-q` therefore contains every selected Y index, and the source's
`B+D` output coordinates contain every selected Z index.

Translation by `L` keeps all selected intervals in different copies
disjoint. A later-copy Y index exceeds every earlier-copy selected Z
index, so no term can connect later Y to earlier Z. A term from Y in
copy `r` to Z in copy `v>r` has weight

\[
2(v-r)+h_p-h_{p'}\ge1.
\]

Thus no unwanted coefficient has zero or negative weight. Taking the
constant term in (4) gives `T_(m,k)` exactly, proving the theorem.

The matching lower bound is the cited prior theorem, not a new lower-bound
argument in this package. Combining it with the explicit maps proves the
claimed minimum within its stated shared-map scope.

## 4. The m=4 control

The four blocks in alternating order are as follows. Interval endpoints
are inclusive; the shared map remains the identity.

| Degree p | Start | Y indices | Z indices | Y weight |
|---|---:|---|---|---:|
| 0 | 0 | 0 | 0,1,2,3 | 0 |
| 3 | 1 | 1,2,3,4 | 4 | 1 |
| 1 | 5 | 5,6 | 6,7,8 | 0 |
| 2 | 8 | 8,9,10 | 10,11 | 1 |

Z weights are the negatives of the Y weights for their matched block.
Y indices are reversed within the block as in (3). The unwanted block
connections are `3 -> 0`, `3 -> 1`, and `2 -> 1`; they all have weight one.
Hence the full transformed tensor is exactly `T_4 + epsilon E_4` for an
explicit integral tensor `E_4`.

## 5. Exact reproduction and scope

```
python research/ai/2026-10-20-alternating-degree-packing/verify_packing.py --max-m 40 --max-k 3 --output results/alternating-degree-packing-2026-10-20/packing.json
python -m unittest discover -s tests -p test_alternating_degree_packing.py -v
```

The standard-library verifier constructs the source substitutions and
enumerates **every source term**. It accumulates the full Laurent tensor,
rejects negative coefficients, and compares its constant part against an
independently assembled target. Missing sparse entries are zero. Thus the
replay checks every target coefficient without materializing a dense
`m` by `kN` by `kN` array. It exports the full integer `m=4,k=1` witness.

The all-size proof is the interval argument above. The finite controls
validate the formulas and their implementation. The construction was
derived during this AI session; independent external review is not claimed.
The existing finite `C(4,11)` witness and the prior fixed-shared obstruction
are explicitly credited above. Higher-ramification singular shared maps,
growing shared source dimensions, and cost-one constructions remain outside
the theorem's optimality statement.
