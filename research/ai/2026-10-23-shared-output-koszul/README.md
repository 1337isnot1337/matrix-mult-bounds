# A second-leg Koszul obstruction for a shared-output candidate

The canonical candidate

\[
10\,\mathrm{Full}(5,4)
\;\dashrightarrow\;
10\,\mathrm{Full}(5,3)+\mathrm{Full}(5,2)+2\,P_{5,4,2}
\]

has no complex tensor degeneration. Its second-leg degree-one Koszul rank
would have to increase from **2595 to 2616**. This obstruction allows arbitrary
degeneration maps on every leg, including singular first-map limits and finite
Laurent poles. Here the two endpoints have the literal canonical coefficient
bases defined in [proof.md](proof.md).

The candidate came from a separate mixed-orientation packing search. It has
format `(5,40,80)` on both sides and a strict increase in the formal symmetric
operational score. Those facts motivated it; they do not supply a tensor map.
The exact radical comparison and original discovery record are retained.

This checkpoint does **not** exclude targets obtained by independent first-leg
basis changes in different target blocks. The source remains ten canonical
copies in one common first coefficient basis. A global basis change of either
endpoint does not affect the result. Extensions to independently changed block
bases require a separate proof.

## Evidence

- [Proof and scope](proof.md): the literal flattening, the block decomposition,
  rank totals, semicontinuity, and exact score comparison.
- [Standalone verifier](verify.py): standard-library Python; no dependency on a
  closed convolution rank formula.
- [Certificate](../../../results/shared-output-koszul-2026-10-23/certificate.json):
  ten integer minors of determinant `1` or `-1` and independent exact kernel
  vectors prove both rank inequalities.
- [Discovery input](discovery_input.json): unchanged record supplied by the
  research-frontier agent; discovery screens are distinguished from the new
  acceptance certificate.
- [Sources](sources.json), [proposed claims](claims.json), and
  [question](QUESTION.md).

Run from the repository root:

```sh
python research/ai/2026-10-23-shared-output-koszul/verify.py
python -m unittest discover -s tests -p test_shared_output_koszul.py -v
```

The proof is written and unreviewed. Same-session agent corroboration and exact
tests are not independent mathematical review or formalization. No smaller
matrix-multiplication exponent is established.
