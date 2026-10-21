# All projective rank-one partners, seven versus five

Claim `AI-ALL-RANKONE-SEVEN-FIVE-101`, written and unreviewed.

The [proof](proof.md) closes the exceptional endpoint with one complete
source reduction,84->0 modulo the four planes. A physical source reversal
and the adopted affine-chart theorem then cover all projective rank-one
partners. All mixed graphs and boundary four-spaces are included, at the
canonical leading flags and first dimensions seven and five. Smaller first
spaces, other flags and an improving target remain open. The exponent is9/4.

Run from the repository root:

```sh
python research/ai/2026-10-21-all-rankone-seven-five/verify.py --output results/all-rankone-seven-five-2026-10-21/report.json
python -m unittest discover -s tests -p 'test_all_rankone_seven_five.py' -v
```

The verifier reconstructs the endpoint's complete normal kernel, virtual
corrections,42-row source obstruction,28 added coordinate slices and all
actual repeated cubic minors. It checks source reversal on all4096 terms,
the leading lines and both mixed quotient bases. It adopts100 without
rerunning that affine verifier. CI does not supply independent review.

Concurrent work, read at pinned heads in sources.json: [PR86](https://github.com/1337isnot1337/matrix-mult-bounds/pull/86)
sharpens ordinary ruling caps through a Borel-fixed quotient and dominance
argument; [PR84](https://github.com/1337isnot1337/matrix-mult-bounds/pull/84)
adds ordinary semisimple slice-span/reflexivity tests and a square-target
border determinant-factor obstruction. These written unreviewed findings
are separate from this proof. Neither supplies the missing improving
singular construction. Their tests were not replayed by this package.
