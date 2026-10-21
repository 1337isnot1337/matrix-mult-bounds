# Projected pair counts and necessary binary lift equations

Written, unreviewed. These are necessary conditions for the coordinate group
construction in SL(2,5) times C2. No target degeneration or exponent
improvement is obtained.

The center Z has four elements and the selected target forces every selected
set to contain at most one point per Z orbit, as proved in source_proof.md.
Write the selected projections as S,T,U in Q=G/Z, which has sixty elements.

## Projected pair capacity

For every q in Q, at most four pairs (s,t) in S times T may have s^-1 t=q.
Their four possible full-group labels all lie in the same Z fiber. If more
than four pairs occur, two have equal labels and the required pair map is
not injective. The same statement holds for the other two cyclic pair maps.
Equivalently, |T intersect S q|<=4 for every q. This is a necessary counting
condition, not a sufficient lifting criterion. The optional projected SAT
encoding uses guarded pair-occurrence variables and exact cardinality bounds.

## Binary equations over the involutions

Of the projected nonidentity inverse classes, fifteen have two full inverse
classes above them and twenty-two have four. For each of the two-class
fibers, exact group enumeration checks that its two full classes are
distinguished by the direct C2 coordinate. Inversion preserves that bit.
For selected points p,q in one leg, their right quotient therefore has color

    bit(p)+bit(q) in F2.

If three selected legs use the same two-class fiber, the pigeonhole
principle already contradicts pair-map injectivity. A certificate needs only
one inducing point pair in each leg.

If exactly two legs f,h use that fiber c, all inducing pairs in each leg
must have one common color; otherwise that leg occupies both full classes
and leaves none for the other. Let those colors be owner(f,c),owner(h,c).
The necessary equations are

    owner(f,c)+owner(h,c)=1,
    bit(p)+bit(q)+owner(f,c)=0       for each inducing pair in leg f,
    bit(p)+bit(q)+owner(h,c)=0       for each inducing pair in leg h.

Each equation records the selected points needed to justify it, including
a witness pair in the other leg. Binary elimination tracks row provenance.
A dependency with zero left side and right side one rejects that point
support, even when additional points are subsequently added. The verifier
reconstructs every equation from the group configuration before checking the
contradiction. Consistency supplies no information about the twenty-two
four-class fibers or strict vertex potentials.

## Actual finite outcomes

The first projected fixed-thirteen-point run reached 2,684 candidates in
300 seconds; every inner lift solver reported UNSAT, without proof traces.
This is discovery output only. The separate run using the necessary binary
filter reached 9,034 candidates in 300 seconds. Its stream contains 2,765
exact capacity rejections and 2,474 exact parity rejections, all replayed.
It also used 3,794 untraced inner solver cores and skipped one projection
at the time limit. None reached a pair-injective full lift. These counts do
not constitute a complete exclusion or a distinctness claim across runs.

The two-bit inner SAT encoding accepts the existing weighted (3,3,3)
positive control when its full central choices are fixed, and the unchanged
integer verifier then accepts all 27 intended terms and its one killed
extra term. Independently, all 64 central lifts of a small shared-involution
configuration agree with the binary equations, including the impossible
cases. Deliberately damaged capacity and parity certificates are rejected.
The optional native binary CNF also agrees on those 64 lifts, and all
projected pruning options together preserve the known positive control.

The maintained all-power matrix-rank formula also gives no full-space Koszul
obstruction for the selected (13,13,15) target: all 240 powers pass in each
of the three leg orientations. The closest source-minus-target relative gap
is positive. This finite necessary screen is not a construction.

## Reproduction

Integer-only checks with root requirements.txt:

```sh
python research/ai/2026-10-20-sl2-five-c2/verify_projected_lifts.py \
  results/sl2-five-c2-2026-10-20/projected-binary.json
python research/ai/2026-10-20-sl2-five-c2/koszul_screen.py
python -m unittest discover -s tests -p test_sl2_five_projection.py -v
```

Optional discovery dependencies are NumPy, SciPy and python-sat, as in the
pinned group-search implementation. Reproduce the positive encoding control:

```sh
python research/ai/2026-10-20-sl2-five-c2/projected_lifts.py --control \
  --output results/local/lift-control.json
```

Use `--binary-filter --pair-capacity` for the strengthened projected search.
Add `--inverse-capacity --native-binary` to encode the necessary inverse-class
capacities and binary equations inside the outer solver before it chooses
projected sets. Untraced outer UNSAT remains discovery output.
The optional `--first-projection` file restricts the first leg and is not an
exhaustive normalization. The output reports all limits and skips. A default
shape is (13,13,15); other shapes require their own exact exponent comparison
and source screens before any exponent consequence is asserted.
