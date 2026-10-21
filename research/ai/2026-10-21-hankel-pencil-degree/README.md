# Hankel pencils and the ordinary frontier

This package supplies a written, unreviewed Hankel Segre-image bound in the
range5r<2(a+b). The index sum theorem constrains annihilators of pencils;
a kernel-bundle calculation then controls arbitrary linear spaces and the
two Segre rulings. This recovers the earlier fixed-scheme and first-boundary
bounds and adds applications below that boundary.

The [proof](proof.md) states all field, rank and degree hypotheses. The
[application](application.md) excludes453 additional balanced single
rectangular formats through a12, including every remaining A8 and A9 format.
It also closes the old A8 ordinary square-sum candidate. All singular maps
remain outside this obstruction. The matrix multiplication exponent is9/4.

The exact controls include a three-dimensional moving Hankel family,
an eight-dimensional Segre image showing that an image cap of seven would
be false, and a quadratic-annihilator pencil outside the theorem's range.
The proof and controls were produced by the same owner-directed Codex
session. They are not independent mathematical review or formalization.
External results and prior local work retain their credits in sources.json.

From the repository root, with requirements.txt installed:

```sh
python research/ai/2026-10-21-hankel-pencil-degree/verify.py --output results/hankel-pencil-degree-2026-10-21/controls.json
python research/ai/2026-10-21-hankel-pencil-degree/application.py --rectangular-output results/hankel-pencil-degree-2026-10-21/rectangular.json --square-output results/hankel-pencil-degree-2026-10-21/squares.json
python -m unittest discover -s tests -p test_hankel_pencil_degree.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The manifest covers the package, reports and new test. The historical
frontier reports and both research archives are preserved unchanged.
