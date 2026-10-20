# Projected search, exact lift equations, and abelian fibers

Written AI-derived argument, unreviewed and not Lean formalized. This is a
search reduction for three-set group-potential constructions, not an exponent
improvement or an obstruction to arbitrary tensor degenerations.

## 1. Exact lifting conditions

The central-involution lemma excludes antipodal pairs in each selected set
for shape (16,16,17). Every point in PSL(2,7) therefore has at most one lift
in a given set. Choose a canonical representative for each of the 168 points
and a sign bit for every selected point. Fix the three identity sign bits to
zero. This is harmless: independently multiplying a whole set by -I preserves
its right quotient set and all witness conditions.

Pair-map injectivity for S^-1*T is equivalent to disjointness of the nonidentity
right quotient sets SS^-1 and TT^-1. Apply this cyclically. A projected
inverse class has either one or two full inverse classes above it. Direct
enumeration finds 21 fibers of size one and 73 fibers of size two. At most
that many of the three sets may use a projected inverse class.

For a size-two fiber used by two sets, each set must use just one full lift
class and the choices must differ. Introduce one owner bit for each user.
If points u,v occur in that set, their full inverse class is

    sign(u) + sign(v) + offset(u,v)   modulo 2.

The offset is computed by an exact product of the canonical representatives
in SL(2,7), followed by inverse-class recognition. Thus the lift constraints
are linear equations over F2. When a projected class has one user there is
no cross-set condition; when its fiber has size one there can be only one
user. These observations prove necessity and sufficiency for lifting the
projected sets with three injective cyclic pair maps.

This is only pair-map feasibility. Strictly positive vertex potentials are
an additional requirement, checked by the existing integer/Farkas verifier.

`central_lift.py` eliminates the parity equations exactly, retaining a row
circuit for a contradiction. Every row records the projected points needed
to induce it. A row about one user's owner bit includes a witness pair from
the other user. A circuit therefore excludes every candidate containing the
union of those points. This support condition is essential: an owner parity
constraint cannot be used after its second user disappears.

`verify_projected_reports.py` reconstructs the equations from the actual
group products, checks every saved row, checks their XOR is 0=1, and checks
the point support. It requires no SAT solver or floating arithmetic. The
test suite also compares parity feasibility with exhaustive sign enumeration
on thirteen small projected configurations, including an inconsistent case.

## 2. An order-48 normalization

Four explicit determinant-one generators produce a subgroup of order 48 and
index seven. Its closure and all 47 nonidentity conjugation/inversion cases
are checked exactly. Each of the selected sets has at least three members in
some right coset. Independent right translations move these cosets to the
subgroup and a selected point to identity; subgroup conjugation and pair
reversal then give the finite anchor disjunction. This is an alternative to
the earlier Borel normalization, not an additional simultaneous assumption.

## 3. Abelian fibers and a stronger cyclic-eight rule

The concurrent group worker already uses the abelian-coset bound in its
affine-group search (pinned implementation at `75f453b`). We apply that bound
to preimages of cyclic subgroups of PSL(2,7), with a further C8 equality test.

Here is a direct explanation of the bound. In any accepted construction,
if a subset S0 lies in a coset of the center of the group, the map

    S0 x T x U -> G,  (s,t,u) |-> s*t^-1*u

is injective. After a translation put S0 in the center. A collision with
different S vertices gives exactly the two opposite-weight unwanted terms
in `central_involution_proof.md`; the proof uses c and c inverse and does not
require c to have order two. A collision with the same S vertex contradicts
ordinary pair-map injectivity. Therefore |S0|*|T|*|U|<=|G|.

In an abelian subgroup H, independently translate three chosen coset fibers
into H and restrict the witness to them. The argument applies with S0 equal
to the whole first fiber, giving the product bound |S_H|*|T_H|*|U_H|<=|H|.
The pair bound follows already from pair-map injectivity. Consequently the
three maximum coset occupancies satisfy the same product bound.

There are 28 cyclic subgroups of order three, 21 of order four and eight of
order seven in the quotient. Exact group arithmetic checks that their
preimages are cyclic of orders 6,8,14. The encoding imposes the resulting
fiber product constraints. For order-three quotient subgroups it is enough
to forbid full three-point fibers in two different sets. For order-seven
subgroups, thresholds 2,3,4,5 give valid pair and triple clauses; omitted
thresholds only weaken pruning and do not change acceptance.

For a C8 preimage, none of the three fibers may contain an antipodal pair.
If all three fibers had two points, injectivity would require their eight
triple sums to cover C8. Translate each two-point set to {0,q_i}. In the
group ring its product would satisfy

    product_i (1+x^q_i) = 1+x+...+x^7   modulo x^8-1.

At a primitive eighth root of unity the right side is zero. Hence a factor
vanishes and some q_i=4 modulo eight, contradicting the absence of antipodal
pairs. Thus at least one fiber has size at most one. This gives clauses
forbidding all three projected sets from having any nontrivial difference
inside the same cyclic order-four subgroup. Exhaustive enumeration of all
216 allowed difference triples independently checks this finite C8 fact.

## 4. Completed and ongoing discovery

The original 600-second direct run, the center-pruned direct run and its
order-48 variant ended without a pair-injective model. They give no
nonexistence conclusion. The first projected 600-second run found 1,394
projected candidates; all 1,394 fail the exact lift equations. All stored
parity circuits replay. None gives a tensor witness.

The fiber-strengthened run is recorded separately. A running checkpoint, a
time limit, or an untraced solver refutation is not a complete exclusion.
Only an exact full-support integer potential witness can supply the missing
construction for the conditional 2.247 exponent comparison.

## 5. Reusing a parity contradiction across its translations

A verified parity circuit excludes a triple of point patterns, given by its
conditional support. This is stronger than rejecting just the particular
full sets that led to it. Independently right translating each pattern
preserves impossibility: if translated patterns had pair-injective lifts,
right translating those lifts back would give lifts of the original patterns.
Central sign gauges can always be reset. Permuting the three patterns also
preserves impossibility, because pair-map injectivity is equivalent to
pairwise disjointness of the three nonidentity right quotient sets.

For a nonempty pattern P, choose the lexicographically least translate
`P*p^-1` over p in P. It represents the entire right-translation orbit:
the least tuple contains identity, so some member must be moved to identity.
For each leg and canonical pattern introduce an occurrence flag. Every
translate gives a clause that forces the flag when all its points occur.
Forbid the three flags of every verified impossible pattern triple and its
permutations. Empty or singleton patterns require no flag because all target
sets are nonempty. These one-way flag implications preserve every valid lift;
unused flags may be set to their actual occurrence values.

The maintained discovery implementation first reconstructs and verifies every
reused parity circuit from exact group products. It adds all original point
cuts and applies the orbit construction only to cores with at most 18 points.
Source report and cut hashes are recorded. For the initial 1,394 cuts this
produces 963 pattern triples, 783 occurrence flags and 125,496 translation
trigger clauses. This is finite certified input to discovery, not a complete
SAT refutation. Small controls check canonicalization on all 168 translations
and verify that the template clauses preserve independently checked lifts.

The separate fiber-strengthened 600-second run ended with 149 projected
candidates, all rejected by replayed parity circuits. Its candidates are not
asserted distinct from those of the first run. The run reusing translation
templates is retained separately, with no outcome inferred before completion.

That 600-second template run has now completed: it found 619 projected
candidates, and all 619 fail the exact lift equations. All saved circuits
replay. It produced no pair-injective lift or potential witness. These are
bounded rejections, without a distinctness claim across runs or a complete
exclusion of the target.
