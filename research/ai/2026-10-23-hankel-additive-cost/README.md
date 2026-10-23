# Exact minimum rank in the binomial supporting chart

The [written unreviewed proof](proof.md) determines the exact minimum
full source-slice rank among all nonzero polynomial moments satisfying

    f_(k+r)=xz*f_k,     2<=r<min(a,b).

This proves the additive degree-cost bound throughout this fixed
binomial chart, over every field. Arbitrary polynomial initial moments
are included. The general primitive-degree-(1,1) supporting-form
conjecture remains open.

For a feasible initial seed j, let u_s and v_s count the residues s in
the a and b moment windows. Its basis-slice rank is

    ab*r+a(a-r)+b(b-r)+sum_s (u_s-1)(v_((j-s) mod r)-1).

The chart minimum is the minimum of these ranks over feasible seeds.
The proof gives a literal key factorization and identity minor for each
basis slice, then a source row/column scaling limit for arbitrary initial
moments. If no seed fits both source degree bounds, the chart is zero.

For a=b=n, write n=qr+t, 0<=t<r. The closed minimum is

    r*n^2+2n(n-r)+r(q-1)^2+2(q-1)t+max(0,2t-r).

The r=n-1 case recovers the preceding two-variable boundary family,
with its credit retained. No matrix-target maps or new general target
exclusions are supplied, and no smaller exponent follows.

The exact controls cover 140 ordered source formats through a,b=9,
426 feasible seed cases, and 1711 balanced formula checks through n=60.
Nineteen certificates check all 910075 literal source coefficients and
export identity minors. The tests additionally reconstruct four selected
matrices from the original six-index tensor sum and reject a corrupted
minor. A finite torus control checks the coefficientwise limit and actual
row/column scaling. The earlier 161-case initial-moment grid is retained
as discovery evidence, separately from the general proof.

```sh
python research/ai/2026-10-23-hankel-additive-cost/verify.py --output results/hankel-additive-cost-2026-10-23/chart-minima.json
python research/ai/2026-10-23-hankel-additive-cost/pilot.py --output results/hankel-additive-cost-2026-10-23/initial-moments.json
python -m unittest discover -s tests -p test_hankel_binomial_chart.py -v
```

The [question and attempt ledger](QUESTION.md) retains the general
additive problem and the distinction between this chart and arbitrary
supporting forms. No historical priority, independent mathematical
review or formalization is claimed.
