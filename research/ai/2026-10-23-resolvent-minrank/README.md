# Sharp rank six in the fixed-resolvent limit space

The 112-dimensional matrix space from PR103 has minimum nonzero matrix rank
exactly six. The proof uses a 31-dimensional outer block and 31 explicit
triangular six-by-six minors.

Every codimension-two compression on each side is injective on this space.
If both compression maps have rank 109, any lost nonzero direction must have
rank six and satisfy the alignment conditions in the proof.

Claim `AI-RESOLVENT-SHARP-MINRANK-001` is written and unreviewed.
The finite certificate uses integer identities and applies over every field.
The associated Laurent argument uses the complex field.
There is no smaller matrix multiplication exponent.

## Files

- `proof.md` gives the complete argument and its scope.
- `verify.py` reconstructs the literal source and replays the integer certificate.
- `sources.json` records immutable predecessor formulas and credits.
- `manifest.json` pins the certificate and recorded report.
- `../../../results/resolvent-minrank-2026-10-23/certificate.json` contains all 31 minor identities.
- `../../../results/resolvent-minrank-2026-10-23/validation.json` records the focused validation and package hashes.

## Reproduction

Run these commands from the repository root:

```sh
python research/ai/2026-10-23-resolvent-minrank/verify.py results/resolvent-minrank-2026-10-23/certificate.json
python -m unittest discover -s tests -p test_resolvent_minrank.py -v
```

The verifier and focused tests require only the Python standard library.
The full repository suite has separate maintained dependencies.

The acceptance program does not import a discovery script or an earlier tangent
solver. It reconstructs the source formula, verifies all 112 normalized source
slices, and verifies each minor entry and parameter substitution.

## Attribution and limits

PR103 supplies the fixed resolvent and its original limiting space.
The earlier cyclic-source work supplies the source convention and unit.
This package adds the sharp matrix-rank certificate and its compression consequences.
All new code and prose were prepared with OpenAI Codex under owner direction.
Another agent's replay is not independent mathematical review.

The concurrent regular-long-leg theorem supplies a broader target exclusion.
This package does not claim a complete classification of rank-six matrices,
arbitrary singular long maps, or higher resolvent corrections.
