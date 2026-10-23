# Singular-unit resolvent chart

The [written proof](proof.md) excludes A4 to M(10,10,11) for the fixed
singular-unit resolvent ansatz B(t)=P(tI+N)^(-1), with constant C, PC=I,
whenever the explicit candidate limiting matrix space has dimension 112.
The first map may have arbitrary finite Laurent poles. The rank condition
holds on a nonempty open dense set of constant compression pairs.

This is a construction-class obstruction. Exceptional compression pairs
where that rank drops, moving compressions and other singular unit
trajectories remain unresolved. No target map or improved exponent is
claimed. The argument is written and unreviewed.

Run from the repository root with the maintained dependencies:

```sh
python research/ai/2026-10-21-singular-unit-resolvent/certify.py --verify results/singular-unit-resolvent-2026-10-21/certificate.json
python -m unittest discover -s tests -p 'test_singular_unit_resolvent.py' -v
```

The acceptance verifier uses only the standard library. It checks the
source inverse over the integers, the square-zero coordinate slice and
source grading, and a saved rank-112 minor modulo 1009. It also checks an
integer invariant subspace at the explicit compression witness. The
universal limit and module-divisibility arguments are in the proof; the
finite verifier does not formalize them.

Earlier optional NumPy discovery and a rational flat-space pilot are
preserved outside the repository at
`/home/user/matrix-research/2026-10-21-singular-unit/`. Their output was
superseded for acceptance by the standard-library certificate.
