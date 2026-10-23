# A uniform mixed-normal dichotomy

Written AI-assisted reduction, unreviewed. No target or exponent improvement.

For all six graph parameters at a=b=1, the [proof](proof.md) encloses
every necessary normal, modulo four common planes, in two fixed linear
spaces of dimensions54 and36. The rank-one projection alternative forces
projection zero uniformly, including exceptional graphs.

The certificate includes repeated square minors,68 quadratic minors,
eight exact identities expressing squares of linear forms in their span,
and four polynomial mixed-row identities of degree one. Replay uses
root requirements.txt, with no parameter denominators or radical routine.

```sh
python research/ai/2026-10-21-global-mixed-normal-dichotomy/verify.py --output /tmp/global-normal.json
python -m unittest discover -s tests -p test_global_mixed_normal_dichotomy.py -v
```

The remaining families require further source and rank conditions. Their
dimensions do not count constructed maps. See [QUESTION.md](QUESTION.md).

The subsequent [all-graph closure](../2026-10-21-all-mixed-graphs-a1/README.md)
excludes every graph at a=b=1, including this package's special fibers.
This package retains its original proof scope and evidence status.
