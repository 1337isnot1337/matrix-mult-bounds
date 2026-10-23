# Sharp ruling caps and a closed-target dominance test

The [written proof](proof.md) gives the exact largest dimension of a
bilinear quotient with bilateral k-input ruling dimensions at most r:

    max(r, 2r-2k+1, q^2+2s if r>=k^2),  r=kq+s,0<=s<k.

It degenerates the kernel in a Grassmannian and uses the classical Borel
fixed-point theorem. The resulting Ferrers optimization is elementary.
The [second proof](dominance.md), in characteristic zero, adds a sharp
dichotomy: either the rank-k image fills its whole linear span densely,
or r>=k(k+1) and that span has dimension at most q^2+2s.

If the rank-k image lies in a closed cone whose contained linear spaces
have dimension at most r, this yields the cap r when r<k(k+1), and q^2+2s
otherwise. In the former case the whole span lies in the closed cone.
The uniform Hankel-space proof supplies precisely this hypothesis for
scalar Hankel cones; a ruling bound by itself does not supply it.

These are AI-assisted written proofs, unreviewed. No historical priority,
independent review, formalization, construction or smaller exponent is
claimed. The fixed-point input is explicitly credited to the inspected
Milne reference. The concurrent rectangular worker's earlier ruling
formulas and the source-lift tests retain their credit and exact pins.

The [finite application](application.md) adds67 exclusions to PR83's
balanced rectangular comparison and tightens three saved square-score
ceilings. It is not the full concurrent all-source frontier. The125
independent partition optima and51 rational Jacobians are controls for
the proofs; they are not substitutes for those all-size arguments.

From the repository root with requirements.txt installed:

```sh
python research/ai/2026-10-21-ferrers-ruling-cap/verify.py --output results/ferrers-ruling-cap-2026-10-21/controls.json
python research/ai/2026-10-21-ferrers-ruling-cap/application.py --rectangular-output results/ferrers-ruling-cap-2026-10-21/rectangular.json --square-output results/ferrers-ruling-cap-2026-10-21/squares.json
python -m unittest discover -s tests -p test_ferrers_ruling_cap.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The first focused test run found a test comparison trying to order None
scores for unattainable dimensions. The test now handles those dimensions
explicitly; the production frontier and all saved scores were unchanged.
The failure log is retained. Full regression remains required before merge.
