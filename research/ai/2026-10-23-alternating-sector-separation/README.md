# Alternating matched-sector separation

Date: October 23, 2026. Written, unreviewed local construction; no exponent
improvement is claimed.

## Statement

Let `a,k,b_1,...,b_k` be positive integers, put `d=a-1`, and set

\[
B=\sum_{i=1}^k b_i+\left\lfloor\frac{k}{2}\right\rfloor d.
\]

The convolution tensor

\[
C(a,B)=\sum_{s=0}^{a-1}\sum_{j=0}^{B-1}X_s Y_j Z_{s+j}
\]
has a weight degeneration to a matched sum of `k` sectors. Sector `i` is
`C(a,b_i)` when `i` is odd. When `i` is even, it is `C(a,b_i)` with the
second and third legs exchanged and the first-leg basis reversed. The sectors
have disjoint coordinates on their second and third legs and share the
first leg.

Consequently every actual complex tensor character profile satisfies

\[
P\!\left(a,\sum_i b_i+\left\lfloor\frac{k}{2}\right\rfloor(a-1)\right)
\geq\sum_{i=1}^kP(a,b_i).
\tag{1}
\]

This extends the three-sector construction to every sector count. It is one
matched partition at a time, not the joint multi-fiber constraint proposed in
the separate formulation comparison.

## Exact support and weights

Write `Y_i` and `Z_i` for the coordinate intervals of sector `i`, concatenated
in increasing order. For odd `i`, give them lengths `b_i` and `b_i+d`; for
even `i`, give them lengths `b_i+d` and `b_i`. The total second-leg length is
`B`. The total selected third-leg length is
`sum_i b_i+ceil(k/2)d`: it equals `B+d`, the full third-leg length of `C(a,B)`,
when `k` is odd, and leaves a trailing interval of length `d` when `k` is even.

Let `J_i` and `K_i` be the initial coordinates of `Y_i` and `Z_i`. Alternation
gives `K_i=J_i` for odd `i` and `K_i=J_i+d` for even `i`. Set the second-leg
weight to zero on odd blocks and `+1` on even blocks. Set the third-leg weight
to zero on odd blocks, `-1` on even blocks, and zero on the possible trailing
coordinates. The first-leg weight is zero.

Every source term has the form `z=x+y`. An odd `Y_i` block can meet only its
own odd `Z_i` block: its largest output coordinate is
`J_i+b_i+d-1`, one less than the next even output block's start, while every
preceding even output block ends before `J_i`. In particular, an odd input
block cannot meet a negative-weight output block or the trailing output
interval. An even `Y_i` block can meet its own even output block and adjacent
odd output blocks, but not any other even output block: its largest possible
output is `J_i+b_i+2d-1`, before the next even output block, and previous even
output blocks end before `J_i`. Thus every supported term has nonnegative
weight, and the weight-zero terms are exactly the `k` intended sectors.

For odd `i`, the zero-weight block has local relation `z=x+y`, giving
`C(a,b_i)`. For even `i`, write the local second coordinate as `u` and the
third as `v`. The zero-weight relation is `u=(a-1-x)+v`, which is `C(a,b_i)`
after reversing the first-leg basis and exchanging the other two legs. Taking
the constant term in this nonnegative weight degeneration proves the stated
matched-sector extraction. The interval argument also covers `a=1`, when
`d=0` and all weights are zero.

## Character inequality

For an actual tensor character with `t=(p_X+p_Y+p_Z)/3>0`, the shared-leg
entropy inequality applies to every matched sum `A=sum_i A_i` and every
probability vector `q`:

\[
\mathcal P(A)\geq e^{H(q)}\prod_i\mathcal P(A_i)^{q_i},
\qquad H(q)=-\sum_i q_i\log q_i.
\]

It follows by applying the oriented shared-leg inequality to all six leg
permutations and taking their geometric mean. The mean exponent on the common
leg is `t=(p_X+p_Y+p_Z)/3`. Maximizing over `q` gives
`max_q(H(q)+sum_i q_i log P(a,b_i))=log(sum_i P(a,b_i))`, proving (1).

The entropy inequality and character framework are external: OpenAI, *An
Upper Bound of 9/4 for the Matrix Multiplication Exponent*, pinned at
[`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb),
Sections 2–3 (character degeneration and shared-leg entropy). The local
contribution is the alternating interval construction; it does not claim a
new entropy theorem.

## The matching scalar profile survives

The exact pointwise-minimal scalar profile from `AI-SCALAR-001` satisfies
every instance of (1). For fixed `a`, its row is concave and has a linear tail
of slope `h_a`:

\[
P_*(a,b)=h_a\left(b+\frac{a-1}{2}\right)\quad(b\geq a).
\]

Concavity implies the tail line lies above the earlier row as well, so for
every positive `b`,

\[
P_*(a,b)\leq h_a\left(b+\frac d2\right).
\]

For `k=1`, (1) is equality. For `k>=2`, `B>=a`, and therefore

\[
P_*(a,B)=h_a\left(\sum_i b_i+
  \left(\left\lfloor\frac{k}{2}\right\rfloor+\frac12\right)d\right)
\geq h_a\left(\sum_i b_i+\frac{k}{2}d\right)
\geq\sum_iP_*(a,b_i).
\]

The first inequality is equality for odd `k`; for even `k` it has slack when
`a>1`. This family therefore does not exclude `P_*`, prove a character
realization, or improve the exponent.

## Reproduction and limits

Run the exact finite support verifier with:

```sh
python research/ai/2026-10-23-alternating-sector-separation/verify.py \
  --output results/alternating-sector-separation-2026-10-23/coverage.json
python -m unittest discover -s tests -p test_alternating_sector_separation.py -v
```

The verifier checks exact integer support for its recorded finite grid. The
interval and tangent-line arguments, not the finite grid, establish the
all-size statement. No full character construction, joint multi-fiber
constraint, independent mathematical review, Lean formalization, or result
below `9/4` is claimed.
