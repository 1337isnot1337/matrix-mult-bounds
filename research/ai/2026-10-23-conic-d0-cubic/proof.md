# An exact polynomial curve on the d=0 cubic-conic fiber

October 23, 2026. Written, unreviewed, owner-directed Codex work.

## Statement

Use the canonical integer source `T` of PR101, with its 4096
coefficient-one terms and coordinate convention `index(u,v,z)=28u+7v+z`.
Let `A0` be the twelve first-source coordinates
`index(i,j,z)` for `i,j in {1,2}` and `z in {0,3,6}`; let `K` be the
other one hundred first-source coordinates. The source and base maps are
credited to PR101 and are pinned in `sources.json`.

On `c=-d^3` at `d=0`, hence `c=0`, specialize PR101's exported polynomial
two-jet without changing its constant, first or second coefficient. Write
its maps as `B0,B1,B2` and `C0,C1,C2`. Here `C2=0`; the only nonzero
entries of `B2` are

| row | column | value |
| ---: | ---: | --- |
| 0 | 32 | `a^2*b` |
| 0 | 53 | `a*b` |
| 1 | 33 | `a^2*b` |
| 1 | 54 | `a*b` |
| 2 | 32 | `-a^2*b^2` |
| 2 | 53 | `-a*b^2` |
| 3 | 33 | `-a^2*b^2` |
| 3 | 54 | `-a*b^2` |

Define

```text
B(t) = B0 + t*B1 + t^2*B2,
C(t) = C0 + t*C1.
```

For every complex `a,b`, the contraction `T(B(t),C(t))` is identically
zero on the one hundred rows indexed by `K`. No source-row correction is
needed. The product has degree at most three, and the independent replay
checks all 100-by-196 coefficients at orders zero through three as
identities in `Q[a,b]`. Thus this is an exact polynomial curve, not only a
finite jet.

The chosen 14-column minors of `B0` and `C0` have determinants `1` and `1`.
The chosen 12-column minor of `T(B0,C0)[A0,:]` has determinant `-1`.
These constant units give the required leading ranks for every `a,b` and
ensure that the curve remains in the rank-twelve incidence chart near
`t=0`. The first coefficient retains PR101's normal class `[1:0]` and
has sixteen nonzero entries outside the boundary planes.

## Evidence

`discover.py` specializes the complete source operators and solves over
`Q(a,b)`, including all seventy second-coefficient tangent fields. It
finds zero weight for each field. This elimination is discovery evidence
only; the accepted claim is the explicit identity above.

`verify.py` uses a restricted polynomial parser, rebuilds the 4096 source
terms from the separate literal-source verifier, compares the constant,
first and second maps with PR101's pinned witness at `c=d=0`, and checks all
78,400 kernel coefficients directly. It independently computes the three
leading minors. It imports no tangent, curvature or discovery operator.
The receipt is `results/conic-d0-cubic-2026-10-23/verification.json`.

Reproduce from the repository root with the pinned root requirements:

```sh
python research/ai/2026-10-23-conic-d0-cubic/verify.py
python -m unittest discover -s tests -p 'test_conic_d0_exact_curve.py' -v
```

The curve concerns only local rank-twelve incidence. It does not construct
the full matrix target, resolve higher-order lifting for `d!=0`, prove an
asymptotic exponent improvement, or provide independent mathematical
review or Lean formalization.
