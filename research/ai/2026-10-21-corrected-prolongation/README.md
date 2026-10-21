# A corrected172-parameter family of complete second jets

AI-assisted research, October 21, 2026. Written proof, unreviewed.
**No matrix-multiplication exponent improvement is established.**

With the outside first rows fixed to the canonical boundary frames,
the complete corrected second-order off-diagonal equations reduce the
532 coupled leading parameters to 172. Twenty-eight independent directions
still leave the fixed boundary spaces. All 36 remaining leading-block
quadratic obstructions vanish identically on the whole family.

The [proof](proof.md) gives rational constructions of the second
coefficients for every parameter choice. Two explicit witnesses include
all coefficients and both source-row corrections. Their first and second
identities are checked on the entire tensor, including every active output
coefficient. An independent fixed-index source formula replays them.

This is a compatible second jet, not an improving degeneration. Higher
conditions from order three remain open. The construction is consistent
with PR47's W2=W0 theorem. Its effective first ranks are12 on each side,
so PR46's maximal16-per-side hypothesis does not apply.

```sh
python research/ai/2026-10-21-corrected-prolongation/verify.py --output-dir /tmp/corrected-prolongation
python -m unittest discover -s tests -p test_corrected_prolongation.py -v
```

Use root requirements.txt. Acceptance uses rational linear algebra,
exact symbolic quadratic identities and integer tensor contractions.
The source family, canonical first extension spaces and prior traps retain
their original attribution in `sources.json`. All code and proof checks
were performed in the same Codex session; no independent review is claimed.
