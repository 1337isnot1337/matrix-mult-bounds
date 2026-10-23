# Hankel Segre bounds in every characteristic

The [written proof](proof.md) extends the existing linear-annihilator
Hankel Segre bound to every characteristic, including characteristic two.
It retains the same cap `max(r,k^2)` for `r<min(a,b)` and
`5r<2(a+b)`, where `k=max(1,floor((3r-a-b+4)/2))`.

The change replaces the earlier symmetric-square assignment map with a
map on swap-invariant tensors (the divided square). Its diagonal
coefficient is one, so the diagonal assignment equations survive in
characteristic two. The inherited annihilator and dimension arguments
are restated with their field hypotheses; polynomial remainders or Hasse
coefficients handle nonreduced support.

Over a finite field, the theorem assumes polynomial minor identities,
or equivalently the rank bound on decomposable inputs over an algebraic
closure. A finite rational-point check is not substituted for that
hypothesis without a field-size condition: the supplied elementary
interpolation lemma shows that checking every rational decomposable input
does suffice over F_q when q>=r+1. Actual ordinary tensor restriction identities survive field
extension, giving the stated cyclic-source obstruction in every
characteristic.

The package supplies no improved characteristic-zero cap, construction,
singular-degeneration exclusion, or smaller exponent. The proof is
written and unreviewed, with same-session checking and no independent
review or formalization. [sources.json](sources.json) pins the inherited
proofs and identifies the two external arbitrary-field inputs. The
historical files remain unchanged.

From the repository root, reproduce the finite controls with:

```sh
python research/ai/2026-10-23-hankel-all-characteristics/verify.py
python -m unittest discover -s tests -p test_hankel_all_characteristics.py -v
```

The [saved controls](../../../results/hankel-all-characteristics-2026-10-23/controls.json)
check all 911 nonzero evaluation fibers of dimensions two through four
over F2, F3 and F5, and 882 monomial assignment systems for ranks two
through six in the stated degree range. In the smallest characteristic-two
negative control, doubling the diagonal changes the assignment dimension
from one to seven. These are exact finite checks supporting the written
proof, not an exhaustive census of arbitrary polynomial subspaces.
