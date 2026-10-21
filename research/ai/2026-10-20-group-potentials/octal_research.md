# F8 semidirect-product construction search

Checkpoint: October 20, 2026. No exponent below 9/4 is established. Source
certificates, partial feasibility, and pair-label injectivity are not target
degenerations. The local arguments are unreviewed; no priority is claimed.

## Sources and exact acceptance

For G=F8^d semidirect F8*, scalar multiplication acts freely on the nonzero
additive dual characters. The field trace pairing identifies that dual with
F8^d; nonidentity scalars have no fixed nonzero vector. The seven quotient
characters have degree one, and each free dual orbit induces one irreducible
of degree seven. Thus the remaining multiplicity is (8^d-1)/7. The sum of
the degree squares is 7*8^d. `octal_source_certificate.py` checks the free
orbits and exact integer-root gates.

The two sources considered have order 448 and 3584. A degeneration to,
respectively, M(19,19,19) or M(48,48,48) would pass the certified degree-sum
gate at 2249/1000. Both target degenerations remain unconstructed. The
source-to-exponent implication is the same group-algebra and asymptotic-rank
argument recorded in `research_note.md`; a conditional number is not a bound.

`stream_potentials.py` stores three injective pair maps and traverses all
supported group triples. A violated finite prefix suffices for rejection.
It never suffices for acceptance. The lazy LP adds exactly checked violations
and accepts only after a full traversal, followed by a second deterministic
integer verification. Round/time limits are unresolved outcomes.
`verify_stream_reports.py` independently replays the sparse circuits by
checking every group relation and positive integer zero dependence.

## Constant direction planes in F8^2

The restricted target has five three-point fibers and two two-point fibers,
at multipliers 6 and 7, in each family. Within a family every fiber has a
constant F2 direction plane; the two short fibers use the same nonzero
direction. All affine offsets are allowed.

A three-point set in characteristic two has difference set equal to its
two-dimensional direction plane. Consequently three such fibers can have
unique triple sums only if their six direction columns are independent.
After translating offsets, write the common three-point shapes as {0,u,v}.
The two-point shape is {0,u}; replacing v by u+v only translates the
three-point shape and preserves the two-point shape.

Under GL(2,F8), normalize u to (1,0). If u,v span one F8 line, v/u has
three representatives modulo r -> r+1: labels 2,4,6. If they span F8^2,
normalize the ordered basis to (1,0),(0,1), labels 1,8. These are the four
templates used in `octal_fixed_frontier.py`. There are 651 F2 planes, 560
disjoint from each fixed first plane, and three second short directions.
The exact frontier therefore has 4*560*3=6720 normalized pair cases.

`mask_packing.py` exhaustively tests the necessary translated pair-label
packings, using integer masks and complete backtracking. Its normalization
fixes the first translated mask; the program checks that each option list
really is a full XOR-translation orbit before applying this reduction.
The solver was separately checked against complete small brute force.

Exactly 126 cases pass the first quotient packing, all from the fourth
template. All 126 pass the six other local quotient checks. Joining the
pair frontiers and requiring six independent columns leaves 3942 local
direction triples. GL(2,F8), choices of the second basis direction and
permutation of the three vertex families reduce these to 342 classes.
For an odd family permutation the potentials change sign: inverting and
reversing the three edge labels preserves the group equation and negates
the vertex row. These are normalizations, not constructions.

Independent right translations set the three multiplier-one offsets to
zero. Common conjugation by a normal translation then sets S's multiplier-two
offset to zero: it adds (1-a)h to every multiplier-a fiber. A two-point
fiber is unchanged by adding its own nonzero direction to its offset, giving
one further redundant bit per short fiber. `octal_normalization.py` is
tested against actual group multiplication on 40 random complete offset
arrays. This does not imply that the other offsets are fixed.

One weak global encoding tested 990 pair-injective models without resolving
the base case. With the offset symmetries removed and exact point-membership
cuts, the same base returned solver UNSAT after one exact circuit. A second
base returned solver UNSAT without a pair model. These negative SAT outcomes
have no independently checked proof traces and are not all-class theorems.
The circuit in the one-model run uses variable fibers; it is not a proof
from the tiny subsystem consisting only of the explicitly fixed fibers.

## Deletions from a pair-injective parent in F8^3

Use the following 56-point parent sets, with a nonzero and x arbitrary in F8:

    S: (a,(x,a^2,0))
    T: (a,(0,x,a^2))
    U: (a,(a^2,0,x)).

For S^-1 T at fixed quotient k=b/a, the third translation coordinate is
b^2/a=k^2*a. It determines a, then b, then both free coordinates. Thus this
pair map is injective; the other two follow by cyclic coordinate permutation.
Each parent pair map has 3136 labels. Deletion preserves pair injectivity.

The search deletes eight vertices per family, targeting 48. An initial
20,000-row feasible prefix was superseded by lazy full-constraint discovery.
The bounded run found 87 exact Farkas rejection circuits and no witness.
Every circuit replays without relying on the LP or SAT solver.

The parent has useful exact symmetries: independent right translations along
each family's free coordinate, common scalar relabeling combined with normal
scaling, and cyclic coordinate/family permutation. Their parent-position
formula is in `octal_parent_symmetry.py`. For the smallest eight-vertex
circuit, all 10752 transformed integer circuits were checked, including
43008 group support relations. They supply 10752 necessary hole-hitting
clauses. The 120-second hitting search timed out. It proves neither existence
nor nonexistence of a 48-point construction.

The written proofs and exact finite frontiers narrow these ansatzes. They do
not settle arbitrary group-algebra degeneration or improve the exponent.

## Fixed-parent deletion route closed by an orbit count

The earlier hitting-search timeout is superseded, within the fixed cubic
parent class, by the [orbit-hole proof](../2026-10-20-octal-parent-barrier/research_note.md).
It proves a volume bound of 92,928 for all rectangular vertex-subset targets
with strict coordinate potentials. These all fail the usual 9/4 degree-sum
gate. The proof is written and unreviewed. Independent-plane searches in the
two-dimensional source and general degenerations are outside this obstruction.

## Variable planes after the first main integration

The next question is whether M(19,19,19) can be obtained when each normal
fiber chooses its own affine direction. `octal_variable_planes.py` keeps the
five-three-point/two-two-point size pattern and one complementary base triple,
but permits all twelve other three-point planes and six short directions to
vary independently. This goes beyond the constant-direction frontier above.
It still does not cover all size-19 subsets or all choices of base triples.

Here is why its graph parameterization loses no plane choices over the fixed
base. In characteristic two the difference set of any three-point set is its
full two-dimensional F2 direction plane. The difference set of a two-point
set is its one-dimensional direction. Thus three fibers have unique sums if
and only if their three direction spaces have direct sum. A nonzero linear
dependence supplies a difference in each fiber and hence a collision; the
converse follows by subtracting a collision.

In particular, any three-point plane in the first family must be transverse
to the sum of the other two base planes. Projection onto its own base plane
is an isomorphism, so it is the graph of an arbitrary 2-by-4 binary matrix.
An arbitrary three-point subset of its affine coset is represented by an
offset and the two graph basis columns: its missing point determines the
offset. The short direction is an arbitrary six-bit vector, with the mixed
fiber conditions enforcing transversality. There are 240 initial Boolean
parameters: 96 graph entries, 108 offset bits and 36 short-direction bits.
Six offset bits are fixed by the earlier common-conjugation normalization.

All 343 mixed normal-fiber conditions are encoded as exact independence
constraints. Pair-label injectivity is encoded separately. The standard-library
`affine_fiber_certificate.py` independently compares full difference-space
sums with direct triple-sum enumeration, checks the gauges, and checks the
three group pair maps. It accepts no potential or exponent claim.

For the first base, plain CNF has 265167 variables and 1105586 clauses.
The native parity encoding has 79393 variables, 65850 ordinary clauses and
74160 XOR equations. Both encodings were checked on a previously verified
pair-injective control by evaluating every Boolean variable and constraint.
The native API is from [CryptoMiniSat](https://github.com/msoos/cryptominisat),
with the installed Python binding pinned separately in
`requirements-discovery.txt`. Maintained verification still needs only root
`requirements.txt`; neither SAT engine is an acceptance authority.

Completed bounded runs on that base are:

| Discovery run | Requested seconds | Completed candidate checks | Result |
| --- | --- | --- | --- |
| Plain CNF, unseeded | 180 | 0 | timeout |
| Plain CNF, known-control phases | 120 | 1 | exact rejection, then timeout |
| Native XOR, explicit known control | 120 | 4 | four exact rejections, then timeout |

The first candidate in each control-seeded run is reused evidence, not a new
construction. In the native run the three-point planes all remain the base
planes; later candidates change one or two short directions. The independent
checker verifies all 343 normal triples and all three 361-label pair maps for
each candidate. Every rejection circuit is replayable using
`verify_stream_reports.py`. No positive potential is found.

The `--vary-plane` option imposes a nonzero graph entry after checking the
known control, forcing all subsequent candidates to change at least one
three-point plane. A control audit covers the initial encoding before this
additional search constraint. Actual run status and completed coverage belong
to each exported report; an unfinished or timed-out query is not an exclusion.

The first required-plane-change trials, based on normalized classes 000 and
007, each checked the reused control and then timed out without an additional
candidate. Their requested budgets were 120 seconds; actual elapsed times
were about 155 and 140 seconds, respectively. These are cooperative solver
limits. Neither run is evidence that a changed-plane solution does not exist.

## One-plane continuation and complete local filter

Starting from main d5911dd, `octal_single_plane.py` allows only one chosen
non-base three-point fiber to change its plane. All offsets vary; other
planes and all six short directions remain fixed. Two 90-second-budget
native-XOR runs, changing S's scalar-two or T's scalar-three fiber, each
returned the known control and an exact rejection circuit, followed by
untraced UNSAT after about 51-52 seconds. No changed-plane candidate emerged.
These solver negatives are not mathematical exclusions.

The independent `octal_single_plane_frontier.py` checks every graph plane
transverse to the fixed base complement: 255 genuine changes in each of the
twelve eligible fibers. For base [1,8,2,16,4,32], all 3,060 changes fail a
necessary pair-quotient mask packing, even when offsets in each quotient
are allowed to vary independently. Complete integer backtracking covers
293,390 search nodes in the recorded run. The report records first failures
for every fiber. This exact finite exclusion assumes the stated base and
fixed short directions; simultaneous changes and other bases remain open.

The separate `group-koszul-pilot.json` evaluates the paired-source worker's
exact matrix Koszul formula on group-algebra block sums, with target padding.
All 224 powers through transpose symmetry pass for source448 to M19; all
60 pass for SL2(5) to M10. These are necessary screens only. The calculation
uses the unreviewed matrix-rank derivation in
`../2026-10-20-paired-sources/matrix_euler.md`; no construction is inferred.

Coverage justification for the local filter: the other two base planes
span a four-dimensional complement. Normal-fiber triple injectivity forces
the changed two-dimensional plane to be transverse to it. Relative to the
fixed base it is the graph of one of 2^8=256 linear maps. The zero map is the
unchanged plane. Every three-point subset of a four-point affine plane is a
translate of the chosen three-point graph triangle, so no triangle choice
is lost. For each pair quotient q, the seven sets a^-1(P_f(a)+P_g(aq))
need disjoint translations in the 64-element normal group. Exact packing
allows each such translation independently. Failure in any quotient rejects
every global offset assignment.

Reproduction from the repository root:

```sh
python research/ai/2026-10-20-group-potentials/octal_single_plane_frontier.py \
  --base-report results/group-potentials-2026-10-20/octal-orbit-000.json \
  --output results/local/octal-single-plane-local-frontier0.json
python research/ai/2026-10-20-group-potentials/group_koszul_pilot.py
python -m unittest discover -s tests -p test_octal_single_plane.py -v
```

The two optional native-XOR experiments are reproduced with
`octal_single_plane.py --family 0 --scalar 2` or
`--family 1 --scalar 3`, adding `--seconds 90`, the same source report via
`--phase-report`, and a destination via `--output`.
