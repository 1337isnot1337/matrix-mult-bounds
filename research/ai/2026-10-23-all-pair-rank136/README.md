# Every balanced leading-rank pair has total at most136

The [proof](proof.md) gives necessary conditions for every complete
Laurent presentation of A4 to M(10,10,11):

    a+b<=136, a+c<=136, b+c<=136, and a+b+c<=204.

Here a is the balanced leading rank on the100-dimensional target leg.
If a=100, both long leading ranks are at most36. Claim
`AI-A4-ALL-PAIR-RANK136-001` is written and unreviewed externally,
with no formalization, target construction, or exponent improvement.

This application retains the prior every-pair144 theorem and applies
the sharp source caps56 below rank84 and60 below rank88 to the remaining
rank sums137 through144. Both prerequisites have exact byte pins in
[sources.json](sources.json). The source sharpness statements do not
assert sharpness of these target leading-rank bounds.

## Reproduce

From the repository root with Python3.10 or later:

```sh
python -I -S research/ai/2026-10-23-all-pair-rank136/verify.py
python -m unittest discover -s tests -p 'test_all_pair_rank136.py' -v
```

The standard-library checker uses integer arithmetic and checks all
20,706 rank pairs under the established individual bounds. It verifies
all992 new exclusions, both strict source thresholds, retained prior
coverage, and open arithmetic boundary controls. It does not rerun or
copy any large source matrix or minor census.
