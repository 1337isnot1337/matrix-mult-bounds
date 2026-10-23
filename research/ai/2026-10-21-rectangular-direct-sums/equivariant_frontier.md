# Fixed-diagonal SL2 capacity screen of all74 remaining ordinary targets

October 21, 2026. Exact finite calculation, written and unreviewed.
No general symmetry reduction, target maps, or smaller exponent.

The representation-capacity argument in equivariant_large_targets.md
extends to every entry of the maintained size2000 ordinary survivor list.
The source is V_(a-1) tensor V_(a+b-2) tensor V_(b-1), and its irreducible
highest weights are all even. Therefore all three nonzero matrix-vertex
representations must have one common pure parity.

The previous two examples had an odd vertex dimension, forcing even
highest weights and partitions into odd dimensions. Some of the74 targets
have all three dimensions even. The complete screen includes both sectors:
partitions into odd irreducible dimensions (even highest weights), and
partitions into even irreducible dimensions (odd highest weights). A mixed
parity vertex would create odd-weight Hom summands absent from the source.

For each source, pair of vertex dimensions and parity, the script computes
the full compatibility graph by integer Clebsch-Gordan multiplicities.
For each target triple it intersects the three adjacency lists. Every
one of the74 candidates has no compatible representation triple in either
allowed sector. The report records the hash of the exact frontier input,
all vertex-list sizes, pair counts, parity exclusions, and the empty
witness results. Cached graphs accelerate the enumeration without pruning
any representation or edge.

This excludes only maps intertwining the specified diagonal action with
matrix-vertex target actions, including degenerations through those fixed
actions. It does not assert that arbitrary constructions can be made
equivariant. The74 ordinary candidates remain open without that symmetry.
Nor does this screen exclude equivariant singular degenerations to all
other shapes: many shapes were removed from the input by ordinary-only
slice arguments, which do not apply to general singular degenerations.

The first two examples retain their standalone explicit pair lists.
The larger screen uses actual highest-weight labels, independently of
the half-degree implementation used there, and agrees on both examples.
