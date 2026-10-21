# Subgroup-ideal cuts for the central-cover targets

Question: can the two failed pair-injective split-cover M10 lifts be avoided
by a necessary condition stronger than pair injectivity, leaving a productive
construction search? Both contain a full coset of a cyclic order-five
subgroup. The [written proof](proof.md) shows that such a coset in one leg
forces the product of the other two sizes below the dimension of a specific
two-sided subgroup-averaging ideal.

The exact dimensions are80,88,160 for SL(2,5), PSL(2,5) x C2 and
SL(2,5) x C2. The first two M10 targets have other-pair product100; all
three other-pair products for M(13,13,15) in the third source exceed160.
Thus every complete five-cycle coset is forbidden in every target leg.
Arbitrary complex degenerations and the remaining coordinate candidates
are not excluded. No smaller exponent has been established.

The rank upper bounds use independent integer annihilators of every coset
vector; matching modular ranks provide separate lower bounds. No imported
complex character table or floating arithmetic enters these checks.
The controls include a real equality-case witness in C3^2 and rejection of
a corrupted annihilator. The underlying averaging and idempotent facts are
standard; the local proof application has no independent review.

```sh
python research/ai/2026-10-21-subgroup-ideal/ideal.py \
  --output results/local/subgroup-ideal.json
python -m unittest discover -s tests -p test_subgroup_ideal.py -v
```

The earlier split-cover run ended after600 seconds with59 model events,
53 exact parity circuits and two pair-injective lifts, both rejected by
positive integer Farkas circuits. Its55 saved certificates replay through
the maintained verifier. These are bounded discovery results, not a finite
exclusion. The inline517-parent transfer pilot was untraced discovery and
is not used as evidence here.

The revised search adds432 full-coset clauses, after verifying the ideal
certificate. It also retains the complete projected pair-capacity encoding
and learns only actual-source parity circuits. SAT and floating LP are
optional discovery dependencies; all accepted witnesses and exported
contradictions are checked exactly.

```sh
python research/ai/2026-10-21-subgroup-ideal/search.py --control \
  --output results/local/subgroup-control.json
python research/ai/2026-10-21-subgroup-ideal/search.py \
  --reuse-report results/sl2-five-native-2026-10-20/split-full-capacity-10.json \
  --seconds 600 --output results/local/subgroup-target10.json
```

The package builds on the central-cover implementation from PR #73.
Its new optional search argument is source-checked by the wrapper; it does
not alter the earlier default searches. Claim `AI-SUBGROUP-IDEAL-027` is
written and unreviewed.
