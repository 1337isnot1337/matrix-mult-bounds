# Sharp odd-characteristic invertible quadratic four-space

The full quadratic R_(3,3) source has a four-dimensional geometric
rank-at-most14 family with coefficient determinant32t^3:

    M(t,b,c,f)=[[8t,b,c],[0,4t,f],[0,0,t]].

Its polynomial kernel and literal minor -2^18*t^14 give exact source
rank14 at every invertible coefficient point in every characteristic
other than two, including zero. Combined with the pinned upper bounds,
the maximum invertible-family dimension is four there. The separate
characteristic-two maximum is three.

Claim `AI-ODD-QUADRATIC-SHARP-FOUR-001` is **proof-written-unreviewed**.
See [proof.md](proof.md) and [sources.json](sources.json). No independent
review, complete attainer classification, or exponent improvement.

From the repository root:

```sh
python research/ai/2026-10-25-quadratic-odd-sharp-four/verify.py
python -m unittest discover -s tests -p 'test_quadratic_odd_sharp_four.py' -v
```

The report is saved in
`results/quadratic-odd-sharp-four-2026-10-25/controls.json`.
