# Pure mixed rows close a nonzero partner chart

At the canonical leading flags, take a full B seven-frame and any C
five-space **containing its pure mixed partner row**. For every rank-one
partner `u=(ab,-a,-b,1)`, `v=(ab,b,a,1)` with `b != 0`, the necessary
normal directions are exactly the four common-plane motions. The
[written proof](proof.md), unreviewed, then excludes the matrix target
by the adopted shifted moving-boundary induction.

The certificate is polynomial in every complex `a` after normalizing
`b=1`. It includes the coalescing-mode values `a^3=-1`. The source torus
transports the result to arbitrary nonzero b. There is no division by
`a` or `a^3+1` in the elimination.

The main step replaces a large determinantal case search by two linear
families. A stable14-row part of the obstruction and a uniform
minimum-rank-two projection force a32-dimensional quotient normal into
families of dimensions6 and14. Their remaining third-tensor equations
eliminate both families exactly.

The pure-row hypothesis matters: a general mixed five-space can have a
nontrivial boundary graph and need not contain the pure mixed row. Those
graphs, the remaining partner strata, and an exponent below9/4 are open.
The global first-rank frontier is unchanged.

```sh
python research/ai/2026-10-21-pure-mixed-five-spaces/verify.py \
  --output results/local/pure-mixed-five-spaces.json
python -m unittest discover -s tests -p 'test_pure_mixed_five_spaces.py' -v
```

The report reconstructs all source equations and exports the polynomial
kernels, minor witnesses, source changes, rowspace certificates and both
terminal eliminations. Exact replay is not independent proof review.
