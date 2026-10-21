# Near-capacity normal sums in C29 and a size-ten obstruction

Date: October 20, 2026. AI-derived work directed by the repository owner.
Claims AI-GROUP-C29-SUM-008 and AI-GROUP-C29-TARGET-009 are written and
unreviewed, with exact finite evidence. Neither improves the exponent.

## 1. Construction class and conclusion

Let G = F29 semidirect H, where H={1,12,28,17} is the order-four scalar
subgroup, and (a,v)(b,w)=(ab,v+aw). Consider three group subsets S,T,U
used through the injective pair maps s^-1 t, t^-1 u, u^-1 s and strict
vertex potentials. Every unintended supported group triple must have
positive potential difference. Then

```
min(|S|,|T|,|U|) <= 9.
```

It suffices to exclude (10,10,10), because restriction to ten vertices in
each family preserves pair injectivity and every required strict inequality.
The proof uses normal-fiber unique sums, an exact classification in C29,
finite pair-quotient packing, and a telescoping identity for the offsets.

The conclusion concerns this pair-map construction class. It excludes no
general complex tensor degeneration, arbitrary changes of basis or joint
extraction from tensor powers. Smaller unequal targets may still pass the
degree-sum gate. In particular (9,9,11) and (9,10,10) survive the earlier
rank-locus necessary test. Their construction remains open here.

## 2. Normal-fiber reduction

Write S_a={v:(a,v) in S}, and similarly for T,U. The
[abelian-coset lemma](../2026-10-20-group-potentials/research_note.md)
AI-GROUP-COSET-003 says that every triple of normal fibers has an injective
sum map. Its proof uses independent right translations to move any chosen
fibers into the abelian normal subgroup. A sum collision gives an extra
relation and its reverse with opposite potential differences, contradicting
strict positivity. The source coset of scalar a can be moved to scalar one
by right multiplication by (a^-1,0), leaving its normal coordinates unchanged.

Each family of size ten has a fiber of size at least three. The product of
the three largest fiber sizes is at most 29. Thus all fiber sizes are at
most three. No fiber can be empty, since the other three would then contain
at most nine points. Each family's size pattern is (3,3,2,2) or (3,3,3,1),
in any order. Every three-point fiber has an injective triple sum with a
largest fiber of each other family.

Independent right translations choose one largest fiber in each family
to lie over scalar one. Global multiplication of normal coordinates by a
nonzero field scalar is an automorphism of G. Normal-coordinate shifts do
not change any of the unique-sum or local packing tests below.

## 3. Complete three-point classification in C29

AI-GROUP-C29-SUM-008: if A,B,C each have three points and their sum map is
injective, then each is an arithmetic progression. After independent
translations and a common nonzero dilation, the ordered triples are exactly

```
012, 036, (0,9,18)
012, 036, (0,9,19)
012, (0,3,16), (0,9,19)
```

and their versions with the last two sets exchanged. Here 012 denotes
{0,1,2}, and 036 denotes {0,3,6}. These are six ordered normalized cases;
no family permutation is used in the reduction.

There are 126 translation classes of three-point subsets. Normalizing the
first set further under dilation leaves the five templates
{0,1,k}, k=2,3,4,5,9. The primary enumeration tests these templates against
all ordered pairs of translation classes. It first rejects repeated
two-set sums, then requires all 27 three-set sums to be different.
Exactly the six cases above survive.

The independent enumeration constructs its classes from all
binom(29,3)=3,654 actual subsets using all cyclic bit-mask rotations. It
covers all 126^3=2,000,376 translation-class triples, with pair failures
covering all their possible third sets. It finds 84 positive class triples.
All are arithmetic progressions, and normalization gives the same six cases.
This finite exhaustive argument is the proof of the classification here;
no all-prime classification or historical priority is claimed.

In centered progression coordinates the six direction triples are

```
(1,3,9), (1,3,10), (1,13,10),
(1,9,3), (1,10,3), (1,10,13).
```

The sign of a step is immaterial. Every two-point fiber is a translate of
{0,e} for exactly one e in {1,...,14}; every three-point fiber is a translate
of {-d,0,d} for exactly one d in that set. Singleton fibers have no direction.

## 4. Complete finite direction filter

Fix one of the six base triples d_S,d_T,d_U. For each family generate every
fiber size pattern from Section 2 whose scalar-one fiber has size three.
At another size-three fiber allow every step giving a unique sum with the
other two base fibers. At a size-two fiber allow every difference with that
property. The normal unique-sum condition makes these necessary domains,
so this loses no potential construction. The direction domains determine
the point sets up to arbitrary offsets, which remain free.

For an ordered pair F,G and scalar quotient q, write b=aq. Its four normal
pair-label sets, before adding offsets, are

```
W_a = a^-1(P_G(aq)-P_F(a)),       a in (1,12,28,17).
```

Each set must have size |P_F(a)| |P_G(aq)|. Pair injectivity requires that
their four translations be disjoint in C29. The local filter permits the
translation of each W_a independently; this is a relaxation of globally
consistent offsets. `cyclic_packing.py` checks all cyclic translation
orbits and performs complete integer backtracking, normalizing one mask
by simultaneous translation. Permuting mask domains only reorders choices
and is used to cache repeated problems.

For each of the three family pairs, `fiber_frontier.py` checks every pair
of family domains against every scalar quotient. It also imposes all
normal triples involving the other family's base fiber. The three pair
frontiers are joined by their actual family-domain indices; all remaining
64 normal-fiber triples are checked. Across all six bases exactly twelve
configurations survive. There are 52,938 distinct cached quotient-packing
problems. These are local survivors, not constructed group subsets.

The committed report records all domain sizes, first-failure counts, pair
frontier sizes and twelve explicit configurations. Replaying the full
enumeration is required to check the asserted coverage; checking only the
twelve configurations would not establish completeness.

## 5. The identity-quotient offset contradiction

Let o_F(a) be the offset of family F's point set in scalar fiber a. At q=1
the normal pair-label center is

```
h_FG(a) = a^-1(o_G(a)-o_F(a)).
```

Normalize each pair's local packing by subtracting h_FG(1). Enumerating all
29^3 relative center triples gives a finite list L_FG for its three remaining
scalar fibers. For any genuine offsets, their three selected vectors obey

```
v_ST + v_TU + v_US = (0,0,0) in F29^3,                      (1)
```

because both the unnormalized centers and their scalar-one centers
telescope. This condition requires no choice of offset gauge.

For every one of the twelve local configurations, the three complete lists
have no triple satisfying (1). `identity_gluing.py` checks every combination
and records the actual lists. The separate modular-equation program
`offset_gluing.py` uses all twelve pair-quotient constraints and independently
finds no compatible affine system in each case. Its eight-variable gauge
fixes the three identity-fiber offsets and S's scalar-12 offset; this extra
calculation is not needed for the simpler identity-quotient contradiction.

Every prospective construction falls into a classified base case and a
generated family-domain triple. Section 4 leaves only the twelve recorded
cases, and (1) rejects each. This proves the size-ten exclusion in Section 1.

## Reproduction and limits

All maintained checkers here use the standard library. From the repository
root, with Python 3.10 or later:

```sh
python research/ai/2026-10-20-c29-near-capacity/normal_triples.py \
  --output results/local/c29-normal-triples.json
python research/ai/2026-10-20-c29-near-capacity/fiber_frontier.py \
  --output results/local/c29-fiber-frontier.json
python research/ai/2026-10-20-c29-near-capacity/identity_gluing.py \
  --source results/local/c29-fiber-frontier.json \
  --output results/local/c29-identity-gluing.json
python -m unittest discover -s tests -p test_c29_near_capacity.py -v
```

Committed reports are in `results/c29-near-capacity-2026-10-20/`. The earlier
restricted opposite-large-fiber pilot and the first-base frontier are
retained with their exact scope; the complete report supersedes their
coverage. No SAT answer or numerical optimizer is used for this exclusion.
The written reduction and programs have no independent review or Lean
formalization. The arithmetic exponent remains 9/4.
