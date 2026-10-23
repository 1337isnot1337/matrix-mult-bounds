# Complete extension criterion for the prescribed third jet

Claim `AI-CONIC-FIXED-THIRD-OBSTRUCTION-001` is written and unreviewed.
For every complex a,b,d with d nonzero and c=-d^3, the complete PR107
third jet extends to order four exactly when

```text
(a+d^3)*(b-d^3)=0.
```

The same condition characterizes its formal or polynomial all-order
extension. On either surviving component, every prescribed second and
third map coefficient and every kernel correction vanish; the prescribed
constant and first maps give an exact linear curve. Away from those
components, a 28-entry functional annihilates all 3,136 fourth map
variables and all 1,200 fourth kernel variables but evaluates to
`-d*(a+d^3)^4*(b-d^3)^3/3` on the known fourth coefficient.

The result fixes every entry through order three, including Y3. The
preceding all-order fixed-two construction changes the third coefficient
and remains valid on the full d-nonzero chart. No complete matrix target
or exponent improvement is claimed. See the [proof](proof.md).

From the repository root:

```sh
python research/ai/2026-10-23-conic-fixed-third-obstruction/construct.py results/local/conic-fixed-third-obstruction.json
python -I -S research/ai/2026-10-23-conic-fixed-third-obstruction/verify.py results/conic-fixed-third-obstruction-2026-10-23/dual-and-linear-branches.json
python -m unittest discover -s tests -p 'test_conic_fixed_third_obstruction.py' -v
```

Construction uses the maintained SymPy dependency. Acceptance uses only
the Python standard library, reconstructs all 4,096 source terms, replays
the supplied third jet, checks every adjoint variable and both complete
linear branches, and runs a separate Fraction-only source control at
(a,b,d)=(1,2,1). It imports no constructor or tangent solver.

Full regression, archive replay and current-head hosted CI remain
separate integration gates. Computational checks do not change the
written proof's unreviewed status.
