# Complete subgroup-ideal cuts for three central-cover targets

October 21, 2026. The group tables and the subgroup-averaging implication
come from the existing repository work at base
`00d51337ddfe581a6e53ff9bc71bb1ece6ad8ee8`. The new contribution is a
complete finite subgroup catalog, exact ideal certificates and its
noncyclic split-cover applications. The written implication remains
unreviewed. No historical priority, independent mathematical review or
improved arithmetic exponent is claimed.

## 1. Credited implication and scope

Use the [subgroup-averaging proof](../2026-10-21-subgroup-ideal/proof.md),
claim `AI-SUBGROUP-IDEAL-027`. For a finite group G and a subgroup H over C,
write

    e_H = |H|^(-1) sum(h in H) h,
    D_H = dim_C C[G] e_H C[G].

For an injective-pair, strict-vertex-potential construction of M(s,t,u),
a full coset of H in the middle vertex set implies `s*u <= D_H`.
The cyclic permutations apply to the other two vertex sets. The credited
proof uses subgroup averaging of the potentials and a closed output-rank
condition. It does not apply to arbitrary complex input maps.

Thus a coset is forbidden in leg f of a specified target if its size is
at most that leg's size and D_H is strictly smaller than the product of
the other two sizes. Equality is permitted. We apply precisely this
condition, without adding a rank heuristic.

## 2. Completeness of the finite subgroup enumeration

`subgroup_catalog.py` begins with the identity subgroup. For every found
H, it generates `<H,g>` for one g in each left H-coset outside H. This
skips no extension: for h in H, `<H,h*g> = <H,g>`. Finite right-generator
closure gives the subgroup, since every generator's inverse is a
nonnegative power. Induction on the number of generators proves that
every subgroup is eventually found.

The verifier separately reconstructs each listed subgroup by left
multiplication. It checks that the trivial subgroup is present and the
list has no duplicate. It then checks extension-completeness for every
listed H and every right H-coset representative g. The identity
`<H,g*h> = <H,g>` justifies that different coset reduction. Every subgroup
of a finite group is finitely generated, so this certifies completeness
of the saved list without trusting the generator's traversal order.

Finally, the verifier checks that the exact conjugacy classes used in the
ideal calculation are disjoint and cover the entire subgroup list.

| Source | Subgroups | Subgroup conjugacy classes | Target |
| --- | ---: | ---: | --- |
| SL(2,5) | 76 | 12 | M(10,10,10) |
| PSL(2,5) x C2 | 164 | 22 | M(10,10,10) |
| SL(2,5) x C2 | 215 | 31 | M(13,13,15) |

These are exact finite statements about the existing, explicitly indexed
group tables. They do not classify subgroups of any other source.

## 3. Exact ideal dimensions

The existing `ideal.py` constructs a spanning matrix for C[G]e_HC[G]:
its rows are the indicator vectors of all left cosets of all conjugates
of H. Indeed the products g e_H k have supports gHk, and these are
exactly those cosets, up to the common nonzero factor |H|^(-1).

For every one of the 65 subgroup classes, the saved certificate includes
`|G|-D_H` integer annihilators and distinct free coordinates on which the
annihilators form a nonsingular diagonal matrix. Every annihilator is
checked against every coset row by integer summation. This proves rank
at most D_H over Q and C. Separate elimination modulo 1,000,003 proves
rank at least D_H over Q. Reduction modulo a prime may decrease rank;
it cannot create a nonzero integer minor from a zero one. The upper
bound does not rely on the modular computation or a good-prime guess.

The verifier reuses that existing integer/rank checker with credit.
It never accepts a floating rank or a character-table prediction.

## 4. Inclusion-minimal forbidden cosets

For each leg, collect every coset passing the condition in section 1.
Remove a coset if it contains a smaller forbidden coset. The verifier
checks three facts separately: each saved coset is actually forbidden,
no saved coset properly contains another, and every forbidden coset
contains a saved one. This proves the saved collection is exactly the
inclusion-minimal collection of all subgroup-ideal coset cuts.

All three legs have the same collection for each of the selected targets,
including the unequal target M(13,13,15).

| Source | Subgroup order | D_H | Minimal cosets per leg |
| --- | ---: | ---: | ---: |
| SL(2,5) | 2 | 60 | 60 |
| SL(2,5) | 5 | 80 | 144 |
| PSL(2,5) x C2 | 2 | 60 | 60 |
| PSL(2,5) x C2 | 4 | 84 | 150 |
| PSL(2,5) x C2 | 5 | 88 | 144 |
| PSL(2,5) x C2 | 6 | 76 | 200 |
| PSL(2,5) x C2 | 6 | 84 | 200 |
| SL(2,5) x C2 | 2 | 120 | 360 |
| SL(2,5) x C2 | 5 | 160 | 288 |

The order-two rows are central involution cosets. In each stated target,
they force every vertex set to meet each coset of the center in at most
one point. This also justifies that condition in projected searches for
these coordinate/potential targets.

The new split-cover order-four subgroups have every nonidentity element
of order two and are copies of C2 x C2. The two order-six classes are
noncyclic copies of S3, embedded with trivial or nontrivial central sign.
The exact subgroups, their conjugates and all cosets are retained in the
certificate; the conclusion does not depend on recognizing their names.
In contrast, a different order-four class has D_H=101 and is not forbidden
by this M10 threshold. The cut does not apply to every order-four subgroup.

Each new order-four or order-six coset contains no forbidden central pair
and no order-five coset. They give 150+200+200=550 additional minimal
cosets per leg, or 1,650 additional coset clauses across the three legs.
This is nonsubsumption by the earlier coset clauses. No independence
from the entire pair-capacity/parity encoding is asserted.

All other subgroup coset cuts in these sources are redundant for the
specified targets or fail the strict dimension comparison. In particular,
adding further cyclic subgroup classes cannot give a new minimal coset
cut here. This is completeness for this finite method, not an exclusion
of the targets or of more general necessary conditions.

## 5. Search adapter and limits

For the split-cover M10 search, each of the 754 minimal cosets has its
own ideal dimension at most 88. The existing runner can therefore use
88 as a common valid upper bound: the other-pair product is 100. The
adapter checks the complete split-cover certificate before using this
union. This common bound is specific to that target; it is not a new
exact ideal dimension for all its subgroups.

The runner adds 2,262 coset clauses, including 180 tautological central
pair clauses in its injective-projection representation. The remaining
2,082 contain the earlier 432 order-five clauses and the 1,650 new
noncyclic clauses. The known weighted M(3,3,3) control is preserved:
its other-pair product 9 activates none of the common-bound clauses,
and its full coefficient/potential witness is checked exactly.

SAT and floating LP are optional discovery tools. The saved parity and
Farkas contradictions must replay through the existing exact verifier.
A timeout or an untraced solver UNSAT does not exclude the source.
Neither a passing search filter nor a finite contradiction establishes
a smaller matrix multiplication exponent. General complex degenerations
and all surviving coordinate candidates remain construction questions.
