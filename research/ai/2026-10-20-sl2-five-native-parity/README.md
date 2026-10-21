# Native central signs for the SL(2,5) target

Question: can a joint projected-point/central-sign encoding construct the
still-open strict-potential M(10,10,10) target in SL(2,5)? No witness or
smaller exponent is supplied at task selection.

This is a new formulation of the existing group worker's source, not a new
source theorem. It differs from the older full-element Borel SAT run and
the separated projection/lift search: the central signs are part of the
point-selection model. It uses the maintained exact central quotient
reduction and unchanged integer accepted-witness checker. Imported SAT/LP
discovery routines remain credited to their pinned package.

The target's other-pair sizes exceed 60, so the proved central-involution
argument forces all three sets to avoid antipodal pairs. Each selected
point is therefore one of sixty projected points with one sign bit. Above
the fifteen involution inverse classes the full inverse-class color is
independent of that bit; above the other twenty-two classes, its color is
the xor of the two endpoint signs and the exactly computed section offset.
Distinct vertex sets must have disjoint full quotient classes. These clauses
characterize the three injective pair maps in the center-free class.

The order-24 subgroup is extracted from the published direct-product
certificate and checked for closure. Index-five pigeonholing puts at least
two points of each ten-point set into that subgroup after independent right
translations. A finite conjugation/reversal certificate covers its eleven
nonidentity projected quotients by two anchors. A common subgroup
conjugation therefore allows the first-leg anchor disjunction while keeping
the other normalizations. Signs remain free except at identity.

The optional commuting-trade clauses are the unchanged necessary obstruction
from the credited group worker. Every negative LP cut has a positive integer
dependence; every positive candidate checks all group products and strict
integer weights. A timeout or untraced SAT negative is not an exclusion.

Optional discovery dependencies are NumPy, SciPy, python-sat and the
maintained SymPy dependency. Run the encoding controls before discovery:

```sh
python research/ai/2026-10-20-sl2-five-native-parity/native_search.py \
  --control --output results/local/native-five-controls.json
python research/ai/2026-10-20-sl2-five-native-parity/native_search.py \
  --seconds 600 --output results/local/native-five.json
```

The controls include both feasible and infeasible small lifts and the known
weighted (3,3,3) witness. They verify the finite implementation; the written
normalization argument has no independent mathematical review.

## Completed discovery and exact replay

The 600-second native run found no pair-injective model. A second encoding
keeps projected membership in the SAT master and learns induced central
parity rows with their exact membership guards. In 600 seconds it encountered
506 projected model events, learned 38,476 conditional rows and exported 506
contradictory parity circuits. Every circuit replays without the discovery
dependencies. These events are not claimed to be distinct projected triples.
Neither run proves nonexistence or produces a degeneration.

```sh
python research/ai/2026-10-20-sl2-five-native-parity/verify.py \
  results/sl2-five-native-2026-10-20/lazy-10.json
python -m unittest discover -s tests -p test_sl2_five_native.py -v
```

The native controls check 272 signed configurations, including 248 accepted
and 24 rejected pair-map cases. The maintained tests independently check all
7,080 projected endpoint/sign combinations against actual group products,
all eleven normalization anchors, the 506 circuits and a corrupted circuit.
The source certificate is reused with its hash and original attribution.
The target still passes the conditional exact comparison at 2.247, but its
construction is missing.

The next formulation also enforces the following necessary capacity: for
each two legs and each projected label q, there are at most two pairs with
s^-1*t=q. This is immediate from injectivity upstairs and the central cover
of degree two. `pair_capacity.py` exports minimal three-edge violations;
the verifier reconstructs every projected product. These cuts use the same
pair-map orientation as the accepted-witness checker. A draft using the
opposite orientation was interrupted before publication and contributes no
evidence; it is retained only under ignored `results/local/`.

The revised run reuses all 506 verified contradictions and their independent
right-translation orbits through the credited `parity_templates.py` helper:

```sh
python research/ai/2026-10-20-sl2-five-native-parity/lazy_parity.py \
  --capacity --reuse-report results/sl2-five-native-2026-10-20/lazy-10.json \
  --seconds 600 --output results/local/native-capacity-orbits.json
```
