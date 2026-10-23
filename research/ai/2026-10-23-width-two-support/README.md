# Width-two monomial support scores cannot beat P*

For every b>=2, every coefficient-one support subset of either C(2,b)
or C(b,2) has historical matched-component score at most
`P*(2,b)=(4b+2)/3`. The statement allows arbitrary weights and additional
support deletions. It uses exactly the existing convolution-recognition
and single-slice fallback score.

The [proof](proof.md) gives an exact deficit identity in the path
orientation and a separate two-hub argument after exchanging inputs.
The latter orientation has equality only at full support. The path
orientation also has proper-support equality examples, including weights
`(0,0)` and `(0,1,1,0)` at b=4. Exchanging those inputs changes the score
from six to three, so the orientation distinction matters.

Claim `AI-WIDTH-TWO-SUPPORT-SCORE-001` is written and unreviewed. The proof
uses elementary graph counting and the prior explicit profile. No external
theorem, spectral realization of P*, or exponent improvement is claimed.
Stronger estimates for unrecognized sectors are outside its scope.

## Reproduction

From the repository root, using the Python standard library:

```sh
python -S research/ai/2026-10-23-width-two-support/verify.py --max-b 8 --output results/width-two-support-2026-10-23/exhaustive.json
python -m unittest discover -s tests -p test_width_two_support.py -v
```

The exhaustive command checks all 174752 support subsets, including empty
supports, at b=2 through 8 in both input roles. It checks both maximum
scores, the path deficit identity and the reversed equality assertion.
The test module separately compares every subset through b=5 with the
unchanged historical recognizer and tests longer sparse and dense cases.
Finite controls do not substitute for the all-size proof.

PR118 owns exact rational ordering and finite-weight certificate replay.
This package adds an all-size result, does not modify that branch and
preserves both historical archives. The next search question needs both
input dimensions at least three, or a stronger score for the sectors.

Concurrency update: PR189 appeared during this work with an overlapping
all-size width-two monomial proof, including equality analysis. That common
conclusion is overlapping evidence, not another frontier advance. This
package additionally covers every support subset, including deletions
outside the maximal diagonal-weight model. The proof is not independently
reviewed by the concurrent agreement.

Exact predecessor pins and attribution are in [sources.json](sources.json).
This is owner-directed OpenAI Codex research without a priority claim,
independent mathematical review or Lean formalization.
