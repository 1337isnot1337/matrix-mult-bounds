# Exceptional affine mixed graphs

Written AI-assisted result, unreviewed. No exponent improvement.

The [proof](proof.md) identifies the affine graph family
h=(x-y,1-x-z,1-x,x,y,z), at a=b=1, whose complete necessary normal
dimension is at least38 everywhere and exactly38 generically. Two
degree-two polynomial left-relation certificates establish the family;
their independence minors are4 at the base point.

At h=(0,1,1,0,0,0), the complete38-dimensional normal kernel is recomputed.
Saved square minors and the remaining source equations eliminate all34
non-plane directions. The adopted shifted induction excludes M(10,10,11)
there for an arbitrary C boundary four-space and arbitrary later maps.
The entire affine family is not classified.

```sh
python research/ai/2026-10-21-mixed-exceptional-affine/verify.py --output /tmp/affine-graphs.json
python -m unittest discover -s tests -p test_mixed_exceptional_affine.py -v
```

Use root requirements.txt. Acceptance uses exact rational linear algebra
and polynomial coefficient identities. The finite modular grid that led
to the family is discovery evidence only; it is not an all-parameter
rank classification. See [QUESTION.md](QUESTION.md) for remaining work.

The subsequent [all-graph closure](../2026-10-21-all-mixed-graphs-a1/README.md)
excludes every graph at a=b=1, including this package's special fibers.
This package retains its original proof scope and evidence status.
