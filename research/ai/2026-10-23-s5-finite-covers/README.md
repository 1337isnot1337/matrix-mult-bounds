# Finite weighted S5 cube covers

The [written, unreviewed proof](proof.md) bounds the characteristic-two
cube slice ranks for S5 x C2 and S5 x C2^2 by 6867542 and 42493572.
This closes the selected M19 coordinate/potential target in the second
source and excludes 38 additional shapes from the maintained frontier.
M(13,14,14) in the first source remains unresolved. General complex
degenerations and constructions from arbitrary higher powers are outside
this one-copy exclusion. No smaller exponent is established.

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-23-s5-finite-covers/covers.py --output results/s5-finite-covers-2026-10-23/certificate.json
python research/ai/2026-10-23-s5-finite-covers/verify.py --certificate results/s5-finite-covers-2026-10-23/certificate.json --output results/s5-finite-covers-2026-10-23/verification.json
python -m unittest discover -s tests -p test_s5_finite_covers.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The producer searches finite integer weights. The verifier imports none
of the producer, replays the pinned algebra certificates, enumerates
grouped coordinates with full multiplicity, checks the covers on every
allowed bidegree triple, and redoes the integer target comparisons.
The proof and verifier are owner-directed Codex work; source citations
and prior local credits are recorded in SOURCES.json.
