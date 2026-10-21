# Central signs for the two double covers of PSL(2,5)

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

That 600-second run produced 520 model events, 9,902 exact three-edge
capacity certificates and two parity circuits, with no lift. All certificates
replay. A further run compiled the complete capacity condition in advance:
all 34,220 triples of projected points form 577 right-translation classes,
567 of size60 and ten of size20. Each class receives one flag per leg;
every contained triple triggers its flag, and at most one leg may own it.
The 104,391 clauses characterize all degree-two projected pair capacities.
The 600-second compiled run produced nine exact parity circuits and no lift.
Timeouts retain their bounded scope.

To see why the compilation is exact, two triples have the same class if
and only if one is a right translate of the other. Matching corresponding
points then gives three pairs with constant s^-1*t. Three points above that
label cannot be distinct upstairs in a central cover of degree two.
Conversely, any three pairs above one projected label exhibit such a common
translation class. The maintained tests independently check every class
against its full translation orbit and check disjoint complete coverage.

## A constructive continuation on the split cover

`split_source.py` builds PSL(2,5) x C2 from the same explicitly computed
quotient group. The reused rational class-algebra routine derives quotient
degrees 1,3,3,4,5 from central idempotents; the direct C2 factor gives two
copies of that list. The exact source upper numerator at2.247 is
1,686,970,929,418, below the M10 target lower numerator1,766,037,820,686
at scale10^10. The existing rank-locus test leaves four dimensions of slack.
This is claim `AI-SPLIT-COVER-SOURCE-026`, conditional on a missing target.

Unlike SL(2,5), this split group has two inverse-class colors above every
one of the37 projected inverse classes. The fifteen involution classes no
longer force one owner. This changes the induced parity equations and is
a concrete new constructive lead. The same index-five normalization and
complete pair-capacity compilation apply. The new source certificate and
all7,080 sign colors are checked, and an actual weighted (3,3,3) positive
control survives both the group verifier and the full encoding.

```sh
python research/ai/2026-10-20-sl2-five-native-parity/split_source.py \
  --output results/local/split-source.json
python research/ai/2026-10-20-sl2-five-native-parity/lazy_parity.py \
  --split-cover --control --full-capacity \
  --output results/local/split-control.json
python research/ai/2026-10-20-sl2-five-native-parity/lazy_parity.py \
  --split-cover --full-capacity --seconds 600 \
  --output results/local/split-target10.json
```

No SL(2,5) cocycle circuit is reused on the split source: every such circuit
must be reconstructed in the actual source before it can be learned.
Neither the conditional numerical comparison nor the small control is an
exponent improvement.
