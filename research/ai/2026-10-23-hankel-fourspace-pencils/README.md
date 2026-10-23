# Quadratic lines in the A10 moment four-space

The [proof](proof.md) treats arbitrary lines in the moment four-space
`h_3=A,h_7=B,h_11=C,h_15=D`, under an explicit nonzero determinant guard.
An exact coefficient identity `det N=-4*Delta*chi^3` separates common
tangent dimension four from dimension seven. For the former, the
four-space is the unique maximal linear Hankel extension.

For one exceptional seed, `A=v,B=0,C=u,D=v`, quadratic Schur equations
and a higher determinant still prove that its unique maximal extension
has dimension four. An explicit rank-eight tangent direction becomes
rank ten after adding a seed endpoint. First-order dimension alone
therefore cannot solve the exceptional extension problem.

These are written unreviewed local results. Other exceptional lines and
quadratic pencils outside this four-space remain open. No matrix target,
independent mathematical review, formalization or exponent improvement
is supplied. The prior prescribed-pencil result keeps its credit.

From the repository root with requirements.txt installed:

```sh
python research/ai/2026-10-23-hankel-fourspace-pencils/verify.py --output results/hankel-fourspace-pencils-2026-10-23/controls.json
python -m unittest discover -s tests -p test_hankel_fourspace_pencils.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The [question](QUESTION.md), exact report, source records and package
manifest preserve the scope. The full parameter identity is checked
symbolically; finite rational controls are supplementary evidence.
