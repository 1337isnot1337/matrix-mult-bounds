# Mixed-target construction experiments

AI-assisted research, 2026-10-20. No smaller matrix exponent is established.
The target, its border-rank certificate, its conditional exponent criterion,
and the fixed-shared-basis catalecticant obstruction belong to the concurrent
Koszul branch, inspected at `6bdab15`. This package searches a different
finite ansatz and records overlaps explicitly.

## Exact collision ansatz

For `T_m`, put `D=m-1`, `N=m(m+1)/2`, with coordinates `(a,b)` of total
degree at most D. Its coefficients are one precisely at
`X_(a+c) Y_(a,b) Z_(c,d)` with `a+b+c+d=D`.

Select a permutation `xp` of the m source X coordinates and an injection
`yp` of the N target Y coordinates into the B source coordinates. Each
target Z coordinate may sum any set of source output coordinates. Thus
output collisions are allowed, extending the earlier no-collision coordinate
packing ansatz. The shared permutation need not preserve the polynomial
coefficient identification used by the concurrent catalecticant obstruction.

Search target-compatible weights

```
wX(p)   = alpha*p
wY(a,b) = -alpha*a + eta_(a+b+1)
wZ(c,d) = -alpha*c - eta_(m-c-d).
```

Every wanted term has weight zero. Its source output index forces that
index into the corresponding output sum. Whenever an unwanted source term
hits the same index, require strictly positive weight. These implications,
coordinate bounds and injectivity constraints form the saved exact SMT query.
Here alpha=1 and sector offsets are rational; clearing denominators produces
integer weights. Scalar rescaling of the positive slope loses no weight
directions in this class. Zero slope is not covered by these runs.

For SAT, a separate pure-Python loop evaluates every transformed coefficient:
negative-weight coefficients must vanish, weight-zero coefficients must equal
the target, and all desired terms must have weight zero. It does not use Z3.
The resulting integral powers give an explicit one-parameter degeneration.

| m | B | Solver result | Independent coefficient replay |
|---|---|---|---|
| 2 | 3 | SAT | 18 coefficients, 4 retained terms |
| 3 | 6 | SAT | 108 coefficients, 10 retained terms |
| 4 | 10 | UNSAT | Solver result only; no unrestricted exclusion |
| 4 | 11 | SAT | 400 coefficients, 20 retained terms |
| 5 | 15 | timeout | No positive or negative conclusion |

Allowing the shared source dimension A=m+1 still gives UNSAT at m=4,B=10
and a timeout at m=5,B=15. These are separate frozen queries. Such a source
change would have vanishing relative short-leg cost along unbounded m, but
no favorable family was found.

Queries, random seeds, solver versions and SHA-256 digests are saved in
`results/mixed-restrictions-2026-10-20/`. The m=2 and m=3 existence results
were already known on the concurrent branch; these are independent control
witnesses. The m=4,B=11 witness uses the identity shared permutation and no
output collision, so it meets rather than beats the prior bound. The m=4
UNSAT result covers the larger permutation/collision ansatz, but remains a
solver result. None of these finite cases establishes the unbounded-size
construction required by the exponent criterion.

## Floating discovery

`border_fit.py` allows a general constant shared matrix followed by target-
coordinate weights, together with general nonshared matrices. This can
represent a singular degeneration; a bounded ordinary restriction cannot
produce the proposed low-cost target. The completed m=4,B=10 run tested
24 sector orders with 150 alternating cycles each. Its best relative residual
was about 0.004275, with large coefficients and small singular values. This
is an exploratory fit, not an exact witness or nonexistence evidence.

## Reproduction and claim boundaries

```
python3 research/ai/2026-10-20-mixed-restrictions/check.py
python3 -m unittest discover -s tests -p 'test_mixed_restrictions.py' -v
# Optional search dependencies:
python3 -m pip install -r research/ai/2026-10-20-mixed-restrictions/requirements-search.txt
python3 research/ai/2026-10-20-mixed-restrictions/collision_search.py --m 4 --B 11 --seed 780897678 --timeout-ms 30000 --output /tmp/collision-m4-B11.json
```

The [written rank notes](research_note.md) and exact slice controls explain
why ordinary restrictions have asymptotic overhead at least two in the
canonical format. That result independently overlaps `d2d505c`. Their
shared-leg equivariant flattening argument is subsumed by `6bdab15`.
Neither excludes general Laurent-parameter degenerations. The actual
construction problem remains open; repeating this ansatz unchanged is not
the next step.
