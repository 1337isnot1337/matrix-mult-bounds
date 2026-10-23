# Total compression loss seven

For the fixed-resolvent space W and the stated 110-by-112/112-by-110
factors, total rank loss at most seven leaves compression-kernel dimension
at most max(0,p+q-5). This holds over every field by scalar extension and
descent. At total loss seven, integer factors of ranks 109 and 108 attain
a two-dimensional kernel and compressed dimension 110.

The [proof](proof.md) depends on PR188's complete low-rank locus and the
classical projective-intersection theorem in Stacks tag 0B2R. The latter
is explicitly imported, with its hypotheses and retrieved-page hash in
`sources.json`. No theorem priority, independent review, formalization,
target construction or exponent improvement is claimed.

```sh
python -S research/ai/2026-10-23-resolvent-loss-seven/verify.py
python -m unittest discover -s tests -p test_resolvent_loss_seven.py -v
```

Exact replay checks the predecessor certificate and integer sharpness
support. The full 112-dimensional source compresses to dimension 110 in
F2 and F3. An independent packed-bit implementation repeats the F2 rank
calculation, and corrupted factor choices are rejected. Finite controls
support the written proof; they do not replace its universal implication.
