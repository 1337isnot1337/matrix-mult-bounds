# Complete affine conic tangents and second jets

The full row-gauged tangent module at the affine conic flags has dimension
70 over every a,b,c in C. It consists of a smooth 68-dimensional boundary
family with three independent polynomial planes and two non-plane
normal classes. Allowing every boundary tangent, arbitrary second row
coefficients and a moving source kernel, a nonzero normal class
[lambda:mu] extends through order two exactly when

```
(a-c)*(b+c)*(c*lambda^3+mu^3)=0.
```

The package includes exact linear incidence curves on a=c or b=-c and an
explicit polynomial two-jet on c=-d^3 with normal class [1:d], including
d=0. Its uncorrected third coefficient is nonzero. These are statements
about rank-twelve contractions of two fourteen-row maps of a fixed
112-cubed source. No full matrix target or exponent improvement follows.
The proofs are written and unreviewed.

Read [the question](QUESTION.md), [proof](proof.md) and [source pins](sources.json).
PR94 supplies the predecessor projective conic classification. This
continuation was prepared with OpenAI Codex under owner direction;
self-replay is not independent review.

From the repository root, with root requirements installed:

```sh
python research/ai/2026-10-21-conic-second-jets/verify.py
python -m unittest discover -s tests -p test_conic_second_jets.py -v
```

`verify.py` rebuilds all row-gauged source operators and polynomial kernel
identifications. It compares its deterministic output to the compressed
certificate. `--write` regenerates that certificate; it is a discovery
operation and must be followed by replay without the flag. Tests also
replay the mixed unit operations independently, check both exact ideal
containments, include the pure fibers, and reject corrupted pivots and
a corrupted moving-source correction. `witness_checks` directly
contracts the original source without relying on the curvature system.

`results/conic-second-jets-2026-10-21/witnesses.json.gz` contains the two
normal-map representatives and every polynomial row coefficient of the
cubic-component two-jet, the moving-source correction, and its nonzero
third residual. `certificates.json.gz` contains three complete tangent
kernels, their invertible geometric basis identifications, two full
curvature quotients, and mixed/pure residual ideal certificates. Both
use deterministic gzip with zero modification time. No ignored local
script or discovery report is a maintained dependency.

Claims: `AI-CONIC-TANGENT-001`, `AI-CONIC-SECOND-JET-002`, and
`AI-CONIC-POLYNOMIAL-JET-003`. Validation at `db312b03197d36096808c3b3806b5ac8efbdb88a` completed840
tests:837 passed and3 optional controls skipped. All five archive replays
passed. Integration of main `d833eb0` preserves this package and both
archives unchanged; its five incoming tests and18 metadata tests pass.
Exact commits, tree, commands and logs are in the dated results directory.
Hosted CI separately verifies the final combined head.
