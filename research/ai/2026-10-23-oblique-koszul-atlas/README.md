# Full-space Koszul ranks of the fixed oblique repair

October 23, 2026. Owner-directed OpenAI Codex continuation.
Claim `EXP-OBLIQUE-KOSZUL-ATLAS-001` is an exact finite experiment with
an elementary certificate argument. No independent mathematical review,
formalization, historical novelty, or exponent improvement is claimed.

The question is whether any full-space Koszul flattening improves the
existing border-rank lower bound for the fixed one-dependency residual
in [PR147](https://github.com/1337isnot1337/matrix-mult-bounds/pull/147).
The answer is negative for all four sizes checked here. This is useful
for selecting a stronger necessary condition; it does not determine the
residual's border rank or exclude other source maps.

| r | Source (n,b) | Residual format | Best full-space Koszul lower bound | Earlier equalizer lower bound | Earlier border upper bound |
|---|---|---|---:|---:|---:|
| 3 | (4,2) | 5 x 7 x 7 | 8 | 8 | 10 |
| 4 | (5,3) | 7 x 9 x 9 | 9 | 10 | 14 |
| 5 | (6,4) | 9 x 11 x 11 | 11 | 12 | 18 |
| 6 | (7,5) | 11 x 13 x 13 | 13 | 14 | 22 |

The equalizer and border upper bounds are credited comparisons from
PR147 at immutable commit `29a486ac622261c8b4854fc109fb8ab40dcf91a2`.
This package does not re-prove those bounds or import their code. The
112 new matrix ranks are computed here over the integers. All pivots
are units, so each reported rank is exact over **every field**, rather
than just a lower bound inferred from a modular rank.

## Tensor and source identification

Put q=r-2. Use first coordinates
`u,v,w,h_1,...,h_q,v_1,...,v_q`, second coordinates
`X,Z,a,eta,y,x_1,y_1,...,x_q,y_q`, and third coordinates
`P,Q,R,S,T,p_1,q_1,...,p_q,q_q`. All coordinates within a leg are
independent; the repeated letters with different subscripts denote
different vectors. The inherited adapted residual is

```
K = u(XP+ZQ) + v(aR+eta S)
    + w(XQ+ZT+eta R+yS+XR),
E_r = K + sum_j h_j(Xp_j+Zq_j) + sum_j v_j(x_j R+y_j S).
```

The adapted form and its unit support embeddings are inherited from
the prior ordinary-rank proof, with byte hashes and immutable links in
[sources.json](sources.json). The new verifier expands those embeddings
at r=5 and compares the complete tensor with the actual native source
contraction. Its sparse [native witness](native-witness.json) is an
exact extraction of the product-oblique case of PR147's credited JSON,
not a newly discovered map. It has 36,22,22 nonzero map entries.

The source convention is

```
Q(6,4) = sum_(p,q=0..5; y,v=0..3) A_(p,q) B_(y,q+v) C_(p+y,v).
M(5,4,5) = sum_(i,j=0..4; h=0..3) a_(i,j) b_(i,h) c_(h,j).
```

The independent contraction processes all 576 source terms, subtracts
from M, and compares sparse dictionaries representing every one of the
10,000 target coordinates, including all off-support coefficients.
It uses no floating-point arithmetic or parent-package imports.
The all-size adapted identification is inherited; native source maps
are re-contracted here only at (6,4).

## Why the rank certificates work

For a chosen wedge leg V of dimension d and the other two legs W,U,
the degree-p matrix is

```
Lambda^p(V) tensor W* -> Lambda^(p+1)(V) tensor U,
(xi,beta) -> sum_i (v_i wedge xi) tensor beta(w_i) u_i.
```

For a nonzero rank-one tensor, wedge multiplication by its V factor
has rank `binom(d-1,p)`. To see this, extend that factor to a basis:
exactly the p-wedges omitting the factor map to independent nonzero
(p+1)-wedges. Tensoring with the rank-one W-to-U map leaves this rank
unchanged. Matrix-rank subadditivity and closed minor equations therefore
give the usual border-rank lower bound

```
ceil(rank(K_p(E_r)) / binom(d-1,p)).
```

The same minor argument applies to formal degenerations and geometric
border rank over an algebraic closure in every characteristic.

For every matrix the verifier uses signed integer coefficients and
subtracts integer multiples of earlier pivot rows. It rejects a pivot
unless it equals +1 or -1. Consequently every row operation is invertible
over every field. The selected rows have distinct pivot columns and a
unit triangular minor, while every remaining row reduces to zero over Z.
This proves both the upper and lower matrix-rank bounds in every
characteristic. The saved rank and SHA-256 of the deterministic pivot
sequence are checked against a fresh complete reduction.

All degrees `0 <= p < d` and all three wedge legs are checked, including
the ordinary-flattening endpoints. There are
`19+25+31+37=112` matrices. Reversing the roles of the two other legs
transposes the complementary-degree matrix, up to signed wedge basis
changes. Its rank-one cost is the same because
`binom(d-1,p)=binom(d-1,d-1-p)`. Thus the three orientations and full
degree ranges also cover the three reversed external-leg conventions.

For r=5 the ranks in degree order are

```
first wedge leg: 11,74,226,414,503,414,226,74,11
second/third:    9,99,471,1284,2248,2675,2214,1266,479,108,11
```

The best resulting bound is eleven. The complete atlas, not an
extrapolation from these displayed rows, supports the table above.

## Replay and remaining question

Run from the repository root with Python 3.10 or later. The acceptance
program and its independent binary-rank controls use only the standard
library.

```sh
python research/ai/2026-10-23-oblique-koszul-atlas/verify.py
python -m unittest discover -s tests -p test_oblique_koszul_atlas.py -v
```

The focused tests replay all 112 integer certificates, cross-check all
112 ranks with a separate bit-packed binary elimination, check the
native contraction and a deliberately altered map, verify rank-one costs
and wedge signs, check transpose duality, and reject a nonunit pivot.

These results concern **unprojected full-space** Koszul flattenings of
four specified tensors. They do not exclude projected Koszul/Young
flattenings, stronger secant equations, other sizes, changes to the
source maps, or better repair constructions. The full r=5 residual
retains the inherited border-rank interval 12 through 18. A useful next
step is a stronger secant condition or a construction improving that
interval; repeating these exact full-space ranks cannot do so.
