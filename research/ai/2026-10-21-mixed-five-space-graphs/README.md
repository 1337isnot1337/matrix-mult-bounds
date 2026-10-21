# Mixed five-space graph controls

Claim `AI-MIXED-FIVE-GRAPH-CONTROLS-090` is written and unreviewed.
At partner a=b=1, four specified nontrivial mixed rows are excluded with
arbitrary four-dimensional boundary parts. This extends beyond the
pure-row hypothesis, but does not classify all graph parameters.

The new exact certificate checks that selected quadratic minors span
all quadratic monomials. Modular full rank lifts to rational full rank;
the resulting vanishing conclusion holds over C. The final target-slice
conditions reduce the remaining normal dimensions10->2->0 in every case.
There is no exponent improvement.

From the repository root, using the root requirements:

```sh
python research/ai/2026-10-21-mixed-five-space-graphs/verify.py --output results/local/mixed-five-space-graphs.json
python -m unittest discover -s tests -p test_mixed_five_space_graphs.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

`quadratic-witnesses.json` contains only selected minor coordinates.
The maintained verifier reconstructs the full rational source data and
the relevant coefficient matrices; it does not import discovery caches.
The report in `results/mixed-five-space-graphs-2026-10-21/` records exact
normal complements, minor reductions, ranks and terminal source indices.
Finite certificate replay is separate from independent proof review.

See [proof.md](proof.md) for the complex argument and its scope,
[QUESTION.md](QUESTION.md) for the fifteen-chart continuation, and
[sources.json](sources.json) for adopted source identities and lemmas.
