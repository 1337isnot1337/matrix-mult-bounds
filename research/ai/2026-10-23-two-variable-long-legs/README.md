# Two variable long maps with bounded channel count

The [written theorem](proof.md) excludes subquadratic auxiliary repair
for ordinary Q(n,m) to M(n,m,n) maps when both long maps vary by column,
one has common window dimension r, and the other has s coefficient
profiles with r*s<m. The first map is arbitrary and exceptional columns
may be nonlocal. The asymptotic lower bound is n^2-o(n^2) at fixed width
and sublinear bandwidth and exception counts.

This extends the credited one-variable/Toeplitz common-symbol method.
Both maps may, for instance, have linear polynomial coefficients when
m>=5. The second map's profiles may be entirely arbitrary functions.
It does not exclude general variable maps or Laurent cancellations,
construct a matrix target, or establish a smaller exponent.
Claim `AI-TWO-VARIABLE-PAIRED-REPAIR-001` is written and unreviewed;
finite checks and CI do not supply independent mathematical review.

Reproduce from the repository root with Python 3.10 or later:

```sh
python -S research/ai/2026-10-23-two-variable-long-legs/verify.py --output results/local/two-variable-verification.json
python -m unittest discover -s tests -p test_two_variable_long_legs.py -v
```

The accepted maps in
[the exported controls](../../../results/two-variable-long-legs-2026-10-23/maps.json)
are integer coefficient data, interpreted over F2, F3 or F101.
`discover.py` generates them deterministically. The verifier imports no
discovery code: it expands the literal source, separately expands the
fixed-channel formula on all good slices, and builds the complete
residual flattening under a nonlocal first map. Source and method pins
are in [sources.json](sources.json). No external service receives the
private source or the computations.

The [finite receipt](../../../results/two-variable-long-legs-2026-10-23/verification.json)
records actual ranks and counts; it does not prove the universal theorem.
At width four, a separate exact equality control attains full symbol
rank with four channels, exhibiting the strict proof boundary.
The protected historical archives remain unchanged.
