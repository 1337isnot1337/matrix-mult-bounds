# Characteristic-two invertible quadratic cap four

Claim `AI-CHAR2-QUADRATIC-INVERTIBLE-CAP-001` is **proof-written-unreviewed**.

For the literal complete 15-by-15 quadratic source, a geometric
rank-at-most-fourteen linear coefficient family with coefficient determinant
not identically zero has dimension at most four in characteristic two.
Together with the pinned odd-characteristic cap and universal three-plane,
the maximum lies in **[3,4] over every field**. Singular six-spaces remain
possible. Dimension-four sharpness and compatible tensor maps remain open.

[proof.md](proof.md) includes the previously unpublished integral-linear-form
reduction and singular-four-space classification, followed by all three
common-kernel orbits and compression exclusions. [sources.json](sources.json)
pins every imported local proof and the discovery records. Those scratch
records are attribution only; reproduction uses tracked repository files.

From the repository root, with the maintained requirements installed:

```sh
python research/ai/2026-10-25-quadratic-char2-cap-four/verify.py
python -m unittest discover -s tests -p 'test_quadratic_char2_cap_four.py' -v
```

The saved report is
[controls.json](../../../results/quadratic-char2-cap-four-2026-10-25/controls.json).
It checks exact polynomial identities modulo two and an integer block
identity. It does not certify the geometric classification by computation.
Tests include the actual discarded cubic coefficient, omission of the
quartic mixed term, and corruption of a pinned dependency hash.

The separate same-session algebra audit is not independent mathematical
review. No historical-priority claim, formalization, or exponent improvement
is made. Do not repeat the closed characteristic-two five-space question
or the already excluded extensions of the universal three-plane.
