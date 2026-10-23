# Border rank at least twelve for the fixed n6 residual

The [proof](proof.md) improves the complex border-rank interval for the
existing product-oblique residual from 11–18 to **12–18**. Its ordinary
rank remains exactly nineteen. The source maps and all earlier
certificates are unchanged.

More generally, for the one-dependency family `b>=2,n=b+2,r=b+1`, the
fixed residual has border rank at least `2r+2`. The upper bound remains
`4r-2`. Geometric border rank and formal degeneration obstructions are
covered in every characteristic.

The test compares actions on the two long legs. A tensor in
`A tensor k^m tensor k^m` of border rank at most `m` must have at least
`m` independent pairs of endomorphisms that act equally on it. This
residual has exactly two. A unit minor certifies that calculation for
the actual n6 tensor, and a coefficient proof handles the whole family.

## Reproduce

```sh
python -S research/ai/2026-10-23-oblique-border-equalizer/verify.py
python -m unittest discover -s tests -p 'test_oblique_border_equalizer.py' -v
```

The verifier checks the complete [certificate](certificate.json), eight
family controls, four [source hashes](sources.json), a unit minor of
order 240, both kernel generators, and all 10000 target coordinates of
the exported native source-map identity. It requires only the Python
standard library.

The local incremental check passed 35 tests: seven new equalizer tests,
seven unchanged full-residual tests, eighteen research and metadata
checks, and three archive-integrity checks. The standalone certificate
replay also passed. This was not a new complete-suite run.

Claim `AI-OBLIQUE-BORDER-EQUALIZER-001` is written and unreviewed.
The proof concerns this fixed residual; it does not optimize arbitrary
source maps, prove optimal border rank, or improve the matrix
multiplication exponent.
