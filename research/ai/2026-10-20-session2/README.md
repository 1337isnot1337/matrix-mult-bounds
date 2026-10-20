# Second research pass: remote checkpoint

Date: 2026-10-20. No exponent below 9/4 is established.

The repository owner requested immediate remote preservation. This directory separates the second pass from the immutable first-pass archive.

## Contents

- [Research note](research_note.md): mixed-sector candidates, two specific obstructions, and conditional homogeneous-profile calculations.
- [Claim status](claims.json): completed calculations, unreviewed arguments, and unfinished work.
- [Dimension program](dimension_search.py): exact integer-budget relaxation across 189 cases.
- [Tensor program](tensor_checks.py): exact Koszul and symmetrizer calculations.
- [Incomplete scoring fragment](drafts/strong_scoring_fragment.py.txt): inert source text, not an executed search.
- [Regenerated reports](../../../results/session2-2026-10-20/verification.json) and [source comparison](../../../docs/external_followups.md).

The dimension report contains 85 candidate scores, not 85 certified degenerations. The tensor calculations reject two specific targets. The conditional criteria do not establish a positive gain.

## Recovery and reproduction

The current runtime retained the first-pass archive, but not the temporary second-pass files. These programs reconstruct the recorded code. The reports were regenerated for this checkpoint.

The reconstruction adds deterministic ordering, portable output paths, and packing verification. It adds a reproducible symmetrizer calculation and eight checkpoint tests. The reports are new runs, not recovered historical bytes.

From the repository root, run:

```sh
python research/ai/2026-10-20-session2/dimension_search.py --output /tmp/dimension_search.json.gz
python research/ai/2026-10-20-session2/tensor_checks.py --output /tmp/tensor_checks.json
python -m unittest discover -s tests -p test_session2_checkpoint.py -v
```

The compressed dimension report retains the complete JSON output. SymPy 1.14.0 is required for the tensor program. No network access is required.

All eight checkpoint tests passed. An initial tuple-versus-JSON-array comparison failed and was corrected. Both test logs are retained. The numerical outputs did not change.

## Attribution and limits

ChatGPT generated this work during a session directed by the repository owner. The owner did not independently review the proofs through this attribution.

The arguments have no independent review or local Lean formalization. The stronger scoring search is incomplete, with zero completed runs recorded.

The external 9/4 result belongs to OpenAI. The external field, ring, rectangular, and block-identity results remain attributed to their respective authors. This checkpoint did not rebuild those Lean projects.
