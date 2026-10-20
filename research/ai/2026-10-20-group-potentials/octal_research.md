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
