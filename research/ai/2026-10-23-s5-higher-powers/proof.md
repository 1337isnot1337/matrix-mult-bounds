# A uniform high-power boundary for the S5 degree-cover method

October 23, 2026. Claim `AI-S5-MAJORANT-HIGH-POWER-001` is written,
AI-derived and unreviewed. It is not formalized and gives no exponent
improvement or lower bound on the actual source's slice rank.

## Statement

Retain the full separately bounded degree majorants and certified bases
of [PR111](../2026-10-23-s5-finite-covers/proof.md). For each r=1,2 and
every integer n>=36, **every coordinate cover of that majorant** on
`(S5 x C2^r)^n` costs strictly more than `V_r^(2n/3)`, where

    V_1 = 2548,       V_2 = 6498.

These are the largest volumes among the two and nine respective targets
left by the pinned PR111 certificate. Consequently such a cover cannot
exclude any of those eleven one-copy targets by a finite-power slice-rank
comparison, even with optimally balanced cyclic target orientations.

The conclusion allows arbitrary, nonmonotone covers and unequal leg
choices **within this majorant**. Its application requires covering every
degree-compatible triple, including triples that may actually vanish in
the source. Finer support, other bases and non-coordinate decompositions
are outside the conclusion. Powers below36 remain separate questions;
36 is a sufficient threshold, not an optimal-cover claim.

## The majorant and its large coordinate set

The source's two central blocks have dimension88 and32. Their certified
layer polynomials are

    P(x)=17+9x+9x^2+18x^3+9x^4+9x^5+17x^6,
    Q(y)=16+16y.

All algebra certificates and credits are retained from PR111 and its
source pins. No new modular representation theorem is imported here.

In an ordered block word of length n with j principal factors, put
`k=n(r+1)-j`. A leg coordinate is specified by principal layer choices,+k binary degrees, and one of `16^(n-j)` multiplicity labels. Define its
two total degrees as d and e. The full majorant includes every triple in
this word with

    d_1+d_2+d_3 <= 6j,       e_1+e_2+e_3 <= k.

There are no cross-word triples. Let U be the leg coordinates satisfying
`d<=2j` and `e<=floor(k/3)`. Its size is

    16^(n-j) A_j B_k,
    A_j = sum_(d=0..2j) [x^d] P(x)^j,
    B_k = sum_(e=0..floor(k/3)) binomial(k,e).

Every triple in `U x U x U` belongs to the majorant. Identify the three
copies of U by their coordinate labels. The triples `(u,u,u)` are then
pairwise coordinate-disjoint. Every cover must select at least one
coordinate from each of these triples, costing at least |U|. This is a
matching of a support **majorant**, not a claimed nonzero diagonal of the
actual group tensor. In particular it is not an actual tensor subrank or
slice-rank lower bound.

The words have disjoint leg coordinates. Summing their lower bounds gives

    L_r(n) = sum_(j=0..n) binomial(n,j) 16^(n-j) A_j B_(n(r+1)-j).    (1)

Every majorant cover costs at least L_r(n).

## Concatenation and all powers

We have `L_r(a+b)>=L_r(a)L_r(b)`. Indeed, concatenate a selected coordinate
in an a-word with one in a b-word. Their principal degrees add to at most
`2j_a+2j_b`. Their binary degrees add to at most
`floor(k_a/3)+floor(k_b/3)<=floor((k_a+k_b)/3)`. The concatenation thus
belongs to the selected coordinate set of the combined word. It is
injective, and its factors are recovered by cutting after a positions.
This proves supermultiplicativity by counting; it makes no assumption
about submultiplicativity of slice rank.

The certificate exports and separate acceptance recomputes all72 strict
integer inequalities

    L_r(s)^3 > V_r^(2s),       r=1,2,       36<=s<=71.              (2)

In particular (2) holds at s=36. For any n>=36, write `n=36q+s` with
`q>=0` and `36<=s<=71`. Repeated concatenation and (2) give

    L_r(n)^3 >= L_r(36)^(3q) L_r(s)^3 > V_r^(2n).                (3)

This proves the asserted uniform boundary. No extrapolation from a
sampled sequence or floating-point approximation is used. The n35
control fails this sufficient inequality for r1 and passes it for r2;
neither outcome is a statement of optimality of a cover.

## Why this prevents the target comparison

Let a remaining one-copy target have volume V=abc<=V_r. After n copies
and any choices of cyclic orientation, its tensor product is a matrix
tensor M(A,B,C) with `ABC=V^n`. Expanding along its smallest leg gives

    SR(M(A,B,C)) <= min(AB,BC,CA) <= V^(2n/3) <= V_r^(2n/3).

By (3), every majorant cover's cost is strictly larger than this upper
bound on the target's slice rank. Such a source upper bound cannot give
the strict opposite comparison required for an exclusion. For n
divisible by three, equal cyclic orientation counts recover the previous
balanced target exactly; its finite slice-rank value and external
Flanders/Meshulam/de Seguins Pazzis attribution remain those of PR111.
The proof here only needs the elementary target upper bound.

This does not construct any target or assert that the actual source
admits a target. It rules out this particular high-power method of
excluding the eleven targets.

## Acceptance

`bounds.py` uses sequential seven-term polynomial multiplication and
binomial coefficients. `verify.py` imports none of it: it uses truncated
binary polynomial powering, factorial word counts, and a separate
binomial recurrence. It verifies the complete seed inventory, all
integer gates, both boundary controls and the pinned prior algebra/cover
certificate. Tests also reconstruct literal small degree-coordinate sets
and concatenations, and reject incomplete or corrupted evidence.

The source bytes are pinned to PR111 head
38e3c12553a7c499994b9ccb87946d749d718ad2. The matching and concatenation
arguments are local written work. Exact replay and internal auditing do
not constitute independent mathematical review.
