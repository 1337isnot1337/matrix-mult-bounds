# A paired-source frontier with two matrix blocks

AI-assisted research, October 20, 2026. Written arguments are unreviewed.
**No tensor degeneration or smaller matrix multiplication exponent is
established.** This package finds a smaller source size for a sufficient
construction target that passes all first-leg Koszul tests.

The selected unconstructed premise is

\[
P_{10}\ \unrhd\ M(4,11,10)\oplus M(10,12,6).                 \tag{H}
\]

It would imply \(\omega<1121/500=2.242\). The premise remains open after
the tests recorded here. Arbitrary constant restrictions are excluded, so
a construction would require a singular degeneration.

## Source convention and finite question

Use the earlier [paired-source package](../2026-10-20-paired-sources/research_note.md).
For \(D=a-1\), its coefficients are

\[
P_a=\sum_{p,q,y,v=0}^{D}
 A_{p,q}B_{y,q+v}C_{p+y,v}.
\]

The format is \((a^2,a(2a-1),a(2a-1))\). Our target convention is

\[
M(l,b,r)=\sum_{i=0}^{l-1}\sum_{j=0}^{b-1}\sum_{k=0}^{r-1}
 A_{i,k}B_{i,j}C_{j,k},
\]

with format \((lr,lb,br)\). Every index range is finite. The source is
the product of two convolutions with their second and third legs exchanged.

The previous single-block frontier first had survivors at \(a=14\).
This investigation permits at most two positive matrix blocks from one
copy of \(P_a\). It asks for a target above the finite endpoint score,
subject to every first-leg Koszul rank inequality. It does not search
tensor powers, arbitrary numbers of blocks, or general tensors as targets.

## Additivity of the padded rank tests

Let the ambient first-leg dimension be \(v=a^2\). For a matrix block
\(M(l,b,r)\), let \(K_q(l,r)\) be the earlier exact Koszul rank for
middle dimension one and an intrinsic first space of dimension \(lr\).
The rank after padding the first space to dimension \(v\) is

\[
R_p(l,b,r;v)
 =b\sum_q\binom{v-lr}{p-q}K_q(l,r).                       \tag{1}
\]

Indeed, split the exterior power by its degree in the unused first-leg
coordinates. Each such summand is a copy of the intrinsic Koszul map.

For a direct sum of matrix blocks, the domain splits by its second-leg
block and the image splits by its third-leg block. The Koszul matrix is
block diagonal with respect to these splittings, even though the exterior
factor uses the complete ambient first space. Its rank is therefore

\[
\sum_j R_p(l_j,b_j,r_j;v).                               \tag{2}
\]

The earlier source formula gives

\[
\operatorname{rank}K_p(P_a)
 =a(2a-1)\binom{a^2-1}{p}
  +2(a-1)^2\binom{a^2-3}{p-1}.                          \tag{3}
\]

Equations (1) and (3) are adopted from the paired-source rank package.
Equation (2) is the elementary direct-sum accounting used by this search.
Ranks cannot increase in a tensor degeneration. Each block must first
pass its individual tests, and the sum must then pass (2) for every
\(p=0,\ldots,a^2-1\).

Checking only the blocks separately is insufficient. For example,
\(P_6\) passes the individual comparisons against \(M(2,6,3)\) and
\(M(6,9,5)\). Their direct sum has first Koszul rank 2,376, exceeding
the source rank 2,360. This target is excluded.

## Exact finite frontier

At \(t=3/4\), the score test is

\[
\sum_j(l_jb_jr_j)^{3/4}
  >\frac{(6a-2)^2}{6^{3/2}}.                            \tag{4}
\]

All comparisons in the maintained program use integers. Fourth-root
intervals enclose each summand in (4); squaring the sum and multiplying by
216 gives an integer comparison. The search refines an interval when it
does not decide a comparison. No displayed decimal selects or rejects a
target.

The program enumerates all positive shapes that fit the source format.
It removes individually impossible shapes, enumerates every unordered
pair of remaining shapes including repeated shapes, checks total leg
dimensions, checks (4), and then checks (2). Exchanging the complete B and
C legs identifies \((l,b,r)\) with \((r,b,l)\) in every block at once.
This is the only symmetry quotient beyond the order of the two blocks.

| a | Pairs that fit after the individual tests | Pairs passing (4) | Pairs rejected by the summed ranks | Surviving pairs modulo B/C exchange |
| --- | ---: | ---: | ---: | ---: |
| 2 | 35 | 0 | 0 | 0 |
| 3 | 1,123 | 0 | 0 | 0 |
| 4 | 10,954 | 0 | 0 | 0 |
| 5 | 56,476 | 0 | 0 | 0 |
| 6 | 211,337 | 10 | 10 | 0 |
| 7 | 614,296 | 49 | 49 | 0 |
| 8 | 1,552,390 | 432 | 432 | 0 |
| 9 | 3,433,151 | 2,180 | 2,180 | 0 |
| 10 | 6,979,330 | 7,213 | 7,175 | 19 |

No improving single-block target survives for these sizes. The complete
[report](../../../results/paired-direct-sums-2026-10-20/frontier-through-10.json)
lists all 19 size-ten pair orbits. There are 38 survivors before the B/C
quotient. These are necessary-test survivors, with no construction
inferred from the enumeration.

## Selected target and conditional exponent

In (H), the source format is \((100,190,190)\); the target format is
\((100,164,182)\). Its matrix volumes are 440 and 720. All 100 first-leg
rank comparisons pass, with the complete integers retained in the
[selected-target certificate](../../../results/paired-direct-sums-2026-10-20/selected-target.json).
The Koszul maps on the other two source legs have not been completely
computed by this package.

The spectral implication uses the existing convolution profile \(P\) and
parameter \(t\). For any matrix direct sum extracted from \(P_a\), apply
character monotonicity to the three cyclic orientations and use Hölder's
inequality on their block sums. The character parameters have sum \(3t\),
so

\[
P(a,a)^{2t}\ge\sum_j(l_jb_jr_j)^t.                     \tag{5}
\]

The earlier [finite profile ceiling](../2026-10-20-koszul/finite_amplitude.md)
is \(6P(a,a)\le(6a-2)^{1/t}\). Combining it with (5) gives

\[
\sum_j(36l_jb_jr_j)^t\le(6a-2)^2.                      \tag{6}
\]

For (H), this is

\[
15840^t+25920^t\le3364.                                \tag{7}
\]

At \(t_0=1121/1500\), the exact root intervals certify

\[
\left(\frac{27519}{20}\right)^{1500}<15840^{1121},
\qquad
\left(\frac{39763}{20}\right)^{1500}<25920^{1121}.
\]

The two lower endpoints sum to \(3364.1>3364\). The left side of (7)
is strictly increasing in \(t\). Its unique equality point is therefore
strictly smaller than \(t_0\), giving a common strict upper bound for
every relevant character. The external detecting-character argument would
then imply \(\omega<3t_0=1121/500\).

The descriptive equality value is approximately 2.2419839324 after
multiplication by three. This decimal and the rational comparison are
conditional on (H). Neither is an established exponent bound.

## Ordinary restrictions fail

The prior paired-source triangular-minor proof gives minimum nonzero
first-slice rank \(a^2\). Under a constant restriction producing a concise
target, the dual first-leg map is injective. The other two maps can reduce
matrix rank by at most their kernel dimensions.

For (H), the kernel dimensions are \(190-164=26\) and \(190-182=8\).
Every nonzero target first slice would consequently have rank at least
\(100-26-8=66\). The first target block has rank-11 first slices.
This contradiction excludes every constant linear restriction, including
dense maps. The argument does not prevent rank from dropping in a
singular parameter limit.

## Reproduction and attribution

From the repository root, with the standard library:

```sh
python research/ai/2026-10-20-paired-direct-sums/frontier.py --output /tmp/paired-direct-sum-frontier.json
python research/ai/2026-10-20-paired-direct-sums/frontier.py --selected --output /tmp/paired-direct-sum-target.json
python -m unittest discover -s tests -p test_paired_direct_sums.py -v
```

The optional LP/MILP discovery used SciPy. Those solver outcomes are not
acceptance certificates. The maintained finite enumeration and selected
target certificate require neither SciPy nor numerical optimization.

The 9/4 theorem, tensor-character framework, shifted tripling construction,
and detecting-character theorem remain external OpenAI work. The profile
ceiling, paired-source minimum-rank proof, and exact source/matrix Koszul
formulas are adopted from the cited local packages and their external
dependencies. The new work is the two-block search, its complete finite
frontier, and the selection and exact comparison for (H). No historical
priority, independent mathematical review, or formalization is claimed.

The immediate construction question is whether a singular family realizes
any of the 19 surviving targets, or whether an additional invariant
excludes them. No claim about arbitrary numbers of blocks or tensor
powers follows from this finite frontier.
