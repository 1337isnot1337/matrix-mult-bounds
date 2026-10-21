# S5 x C2: a conditional rectangular target and two discovery methods

Question: can the split source S5 x C2 construct M(13,14,14) by injective
coordinate pair maps and strict integer vertex potentials? This source is
different from the earlier two covers of A5. No improving target has been
constructed and the exponent remains9/4.

## Exact complex source

The source is constructed directly from permutations of five points and a
central C2 bit. The maintained rational class-algebra routine, with its
original attribution, derives S5 degrees1,1,4,4,5,5,6 by exact central
idempotents. Tensoring with the two linear characters of C2 gives two
copies of this list and total dimension240. At tau=2247/1000 and scale10^10,
the source upper numerator is3,550,306,432,628 and the target lower numerator
is3,558,306,617,707. The margin8,000,185,079 is strictly positive.

This is a conditional comparison. The missing premise is the actual
M(13,14,14) degeneration. The existing rank-locus screen leaves22 dimensions
of slack; passing that necessary test does not construct a map.

The other-pair products182,182,196 exceed half the group order. The proved
central-involution argument therefore forces each vertex set to avoid two
points in the same central orbit. The quotient has120 points and72 inverse
classes, each with two full lift colors. Every one of the28,560 endpoint
sign combinations is checked against actual multiplication in the tests.

The index-five subgroup is S4 x C2. Independent right translations place
at least three selected points of each target set in it, including identity.
Conjugation inside that subgroup covers its23 nonidentity projected points
by four pair anchors. The generic projected builder now computes the actual
subgroup index. Its earlier SL(2,7) behavior remains index7; the S5 target
uses ceil(size/5)=3. The LP width is the actual sum of target sizes.

An inherited weighted (3,3,3) control is embedded through the faithful
five-coset action of PSL(2,5). All3,600 quotient products and parity of the
resulting permutations are checked. The new group verifier checks27
intended terms and one positive extra term. This small witness is not the
improving target.

## A finite characteristic-two certificate

`radical.py` constructs two four-dimensional binary representations. The
first is the even vertex subspace of the five-point permutation module.
For the second, take the edge space of K5, impose zero vertex boundary and
even edge parity, then quotient its five-dimensional subspace by the fixed
all-edges line. Direct checks verify28,800 representation products.

Together with augmentation, their algebra homomorphism has image dimension
33 in F2 plus two four-by-four matrix algebras. Its87-dimensional kernel J
has power dimensions

    dim J^0,...,dim J^7 = 120,87,62,53,35,26,17,0.

The image fills the33-dimensional semisimple product and the kernel is
nilpotent, so J is the Jacobson radical. The exported bit-vector bases
replay through a separate direct group-convolution implementation, checking
24,360 products and both inclusions needed for the successive power spans.
Corrupted representation and kernel vectors are rejected.

The resulting layers are33,25,9,18,9,9,17. Tensoring this filtration with
the augmentation filtration of F2[C2] gives layers
33,58,34,27,27,18,26,17. Products of total weight greater than7 vanish.
The standard slice-rank counting method therefore gives the cubed upper
bound F(t)^3/t^7, where F has this coefficient list. At t=9/10 it is

    225922289241301044816517631 / 17714700000000000000.

It exceeds the squared target volume6,492,304, so this reported rational
parameter does not exclude the coordinate target. No best bound over all
parameters or filtrations, or target construction, is asserted. The general
modular filtration method is external:
[Petrov v4](https://arxiv.org/abs/1606.03256v4) and
[Sawin2018](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i4p23/pdf/).
The finite S5 module and ideal certificates here are local work, with no
independent review or claim of historical priority for the standard facts.

## Search and exact acceptance

Two600-second SAT runs, before and after canonicalization, found no
projected model. These are timeouts. The complete projected pair capacity
uses2347 right-translation classes covering280,840 triples. It does not
prove a source exclusion.

The canonicalization compares the first projected set with all24 common
subgroup conjugates, with subgroup points ordered first and membership
preferred. Its maximum has a minimum-orbit first-pair anchor. It also orders
the equal-size last two sets. Swapping those two sets and negating vertex
potentials preserves the construction: the three group labels are inverted
and their order reversed. A joint maximum under the finite conjugation and
swap action satisfies both constraints. The lexicographic CNF is checked
against every pair of Boolean vectors through length4. A genuinely weighted
control survives the complete canonicalized encoding.

The complementary local search updates the exact projected pair-capacity
and inverse-class-capacity energies after each point change. Its first
120-second run performed1,140,949 steps and reached two zero-capacity
configurations. Both have exact induced parity contradictions, independently
replayed. The score is a discovery aid; it is not a matrix degeneration.
The600-second continuation reuses those verified circuits and warm-starts
from their actual points. It produced30 further exact parity contradictions
in7,078,373 steps and no pair-injective lift. All32 circuits replay.
Neither a solver timeout nor failure of sampled lifts is a proof of
nonexistence. Positive candidates always use the unchanged exact group and
strict-potential verifier.

```sh
python research/ai/2026-10-21-s5-split/s5_source.py \
  --output results/local/s5-source.json
python research/ai/2026-10-21-s5-split/verify_radical.py \
  results/s5-split-2026-10-21/radical-pilot.json
python research/ai/2026-10-21-s5-split/verify_search.py \
  results/s5-split-2026-10-21/local-target13-14-14.json
python -m unittest discover -s tests -p test_s5_split.py -v
```

SAT/LP discovery additionally requires the optional python-sat, NumPy and
SciPy packages. Maintained verification uses the root dependencies only.
Claims `AI-S5-SPLIT-028`, `EXP-S5-RADICAL-029` and `EXP-S5-PARITY-030` retain conditional/finite
status. No smaller matrix multiplication exponent is supplied.


## Four central colors

The verified S5 factor also gives the source S5 x C2 squared, of order480,
with four copies of the degree list1,1,4,4,5,5,6. Its M19 comparison at
2247/1000 has source upper numerator7100612865256 and target lower
numerator7470666361594, both at scale10^10. This is conditional on a
missing degeneration. The native one-hot color encoding checks all114240
endpoint combinations,64 small configurations (24 accepted,40 rejected),
and the genuine weighted3-by3 control. A600-second native target search
returned no pair model; this is a timeout, not an exclusion.

The [central matching proof](central_slice_proof.md) gives an additional
necessary cut. Four aligned projected vertices would restrict to D4 inside
the central group algebra. Its characteristic-two slice rank is at most3,
contradicting the coefficient-one integer-potential degeneration. An actual
four-point control passes pair injectivity and every earlier commuting
trade test, but has an exact five-row Farkas circuit. Its finite control
checks all27 zero-cube products and64 transformed tensor coefficients.
This local application is written and unreviewed; the underlying zero-cube
slice method retains its explicit external credit.

```sh
python research/ai/2026-10-21-s5-split/verify_four.py \
  results/s5-split-2026-10-21/four-target19.json
python -m unittest discover -s tests -p test_s5_split.py -v
```

Claims AI-S5-FOUR-SOURCE-031 and AI-CENTRAL-FOUR-MATCHING-032 remain
conditional and written-unreviewed respectively. No exponent is improved.

The smaller target M(18,18,20) also passes at2247/1000: its target lower
numerator7159285462356 exceeds7100612865256 at scale10^10. Its600-second
projected run made7,883,122 steps and102 model events: one exact central
matching cut,93 untraced inner SAT negatives and eight budget hits, with
no pair-injective lift. The direct colored-point heat-bath sampler instead
resamples all480 possibilities for each moved vertex, using exact pair
histograms to check every saved incremental score. The first600-second
run performed1,142,316 steps and reached collision energy2, with no pair
model. A low score is not a degeneration or an exclusion.

The alternative S5 x C4 basis has the same complex degree cost, with263
full inverse classes rather than288. Its order-two subgroup transfers the
actual weighted3-by3 control. Every114240 endpoint color case is checked
in the cyclic group. The C2-squared slice-rank-three proof does not apply
to C4. Its four-matching prohibition follows already from the elementary
color-sum argument in the proof; all36 normalized matched permutations
are checked, alongside the12 surviving matched patterns for C2 squared.
The same direct sampler now explores both bases with source-specific
receipts and recomputed warm-start histograms.
