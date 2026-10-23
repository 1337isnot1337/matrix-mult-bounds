# Cyclic torus packets in SL(2,F8)

October 21, 2026. AI-SL2-F8-TORUS-021. Written proof, unreviewed.
The local packet constructions do not improve the matrix exponent.

## 1. Classical incidence and the exact finite model

The cyclic order-nine subgroups give the standard smallest Ree-unital
incidence model. This incidence is classical. See Gabor P. Nagy,
[*Embeddings of Ree unitals in a projective plane over a field*](https://arxiv.org/abs/2007.10464),
v3, January25,2021, Sections1-2; published in Finite Fields and Their
Applications74 (2021),101875. That paper describes the fixed-involution
model, its28 points and63 blocks, and the exceptional PSL(2,8) action.
No discovery of the unital or its embedding is claimed here. The finite
rederivation below is used for the stated tensor-packet application.

Enumerating every element of the exact504-element group gives28 distinct
cyclic order-nine subgroups. They equal all conjugates of the selected
subgroup; every two intersect only at the identity. There are63 involutions.
Each inverts exactly four of these subgroups. These four-subgroup blocks
are distinct, and every pair of subgroups lies in exactly one block.

For subgroups A,B,C, the ordinary triple-product property is

```
a*b*c=1, a in A,b in B,c in C  =>  a=b=c=1.
```

The verifier checks all3276 unordered triples of distinct tori. Exactly252
have this property; they are exactly the triples inside the63 four-point
blocks. Each other triple has precisely one nonidentity solution(a,b,c).
The sorted translation-order triples have counts

```
(3,3,9):756,   (3,9,9):756,   (9,9,9):1512.
```

Thus every one of the3024 non-TPP parents has at least one order-nine
factor. The test is independent of the ordering of the three subgroups:
cyclic permutation and inversion/reversal preserve the product property.

The committed report records every subgroup, involution block and TPP
triple. The classification uses actual group multiplication, rather than
assuming a historical identification or importing a character table.

## 2. Full-coset direction rigidity

For a complete left coset aH define its direction to be aHa^-1. This is
its full left-difference set. Suppose a strict vertex-potential construction
contains at least one full order-nine coset in each family. Restrict to one
chosen coset in each family. Average the potentials over the independent
right actions of the three order-nine subgroups. These actions preserve
the group support equation and intended/nonintended distinction. Averaging
preserves strict positivity and makes the potential constant on each coset.
Every supported term now has weight zero. Consequently the three chosen
coset directions must be an ordinary TPP triple.

Directions in different families are distinct: a common nontrivial
left difference would violate the corresponding pair-map injection.
Choose directions A,B,C, one from each family. They lie in one four-point
block. Any further direction A' from the first family must complete the
pair B,C to a TPP triple, so it lies in the same block. The same argument
applies to the other families. Thus every full-coset direction lies in
this one block, and the three families' direction sets are disjoint.

In particular, two families cannot each have two distinct full-coset
directions when the third family has one. Three nonempty disjoint direction
sets inside a four-point block have sizes at most(2,1,1), up to permutation.

For the16 remaining improving formats, the
[normalizer-ideal bound](proof.md) forbids a full order-eighteen normalizer
coset on every leg. Two distinct left cosets aH,bH of one fixed order-nine
subgroup either have distinct directions, or b^-1*a normalizes H. In the
second case their union is a full left coset of its order-eighteen
normalizer, also forbidden. Therefore two families cannot each contain
two complete left cosets of a fixed cyclic order-nine subgroup if the
remaining family contains any complete order-nine coset. The fixed subgroup
may differ between families.

## 3. Doubled right cosets

There is a separate obstruction for two right cosets. Independently right
translate a family Ha union Hb to H union Hr. Right translation preserves
its left-difference set and the matrix construction. That difference set is

```
H union H*r*H union H*r^-1*H.                              (1)
```

For every cyclic order-nine H, the H,H double cosets have sizes
9,9,81,81,81,81,81,81. The second small coset lies in its order-eighteen
normalizer. That case is already forbidden for the improving formats.
Each large double coset is inverse closed, so(1) has90 elements.

Fix the first torus by common conjugation. All27 choices of a different
second torus and all6-by6 large-double-coset choices give972 cases. The
verifier recomputes both difference sets and their intersections. The
intersection sizes range from11 to30; the complete histogram is exported.
Thus the two families share a nonidentity left difference, so their pair
map cannot be injective. If their two tori coincide, that collision is
immediate without this enumeration.

Combining Sections2-3 excludes the following single-target ansatz for
all16 improving formats: each family contains two complete cosets of
one order-nine subgroup, and each family may independently choose left
or right cosets. At least two families choose the same orientation.
Two right-coset families fail pair injectivity; two left-coset families
fail direction rigidity. General vertex families, partial cosets and
arbitrary complex tensor maps remain open.

## 4. Exact punctured packets

Fix a non-TPP parent triple A,B,C of order-nine subgroups. Its unique
nonidentity relation is(a,b,c), with a*b*c=1. For subsets S,T,U of the
three parents, every unwanted source term is determined by edges

```
s -> a*s,       t' -> b*t',       u' -> c*u'
```

whose endpoints remain in the corresponding subsets. The potential row is
the sum of the three edge differences f(x)-f(g*x). Each edge graph is
a restriction of a permutation with cycles of length3 or9.

The subsets admit strict vertex potentials if and only if at least one
of these three restricted graphs has no directed cycle. If one is acyclic,
put decreasing integer heights on its directed paths and set the other
two potentials to zero. Every unwanted term then has positive weight.
If all three contain a directed cycle, take all products of one cycle's
edges from each graph. The sum of their potential rows is zero, while all
rows are strict constraints. This is a positive integer Farkas circuit.
It proves infeasibility without a floating LP argument.

Every parent has an order-nine relation factor. Delete one point from that
family's single nine-cycle, keep the other two families full, and give the
remaining path consecutive decreasing integer heights. This constructs
M(8,9,9), in the appropriate cyclic ordering. All extra supported terms
have weight1, so the selected tensor is exactly T0+epsilon*T1.

Conversely, an acyclic subset of an order-nine translation has size at
most8. An order-three translation has three cycles and allows at most6.
Any feasible non-TPP packet therefore has volume at most8*9*9=648, and
the construction attains that bound. The full TPP parents attain729.
These are complete statements about subsets of three fixed torus parents,
not about arbitrary group-algebra restrictions.

The exported example is checked over the entire group support:648 intended
terms,567 extra supported terms, and minimum extra weight1. Setting all
potentials to zero fails. The full nine-by-nine-by-nine parent also has an
exported positive cycle, checked independently by group multiplication and
integer cancellation. Separate ordinary M9 and M7 controls have729 and343
intended terms and no extras. None passes the exponent gate individually.

These local maps are not a simultaneous direct sum. Their joint assembly
would have to share one source tensor, keep the target legs independent
and eliminate every cross term. See [the assembly analysis](assembly_note.md)
for a conditional2.24 target and the additional coordinate obstruction.

## Reproduction

```sh
python research/ai/2026-10-21-sl2-f8-ideals/torus_packets.py --output results/local/sl2-f8-torus-packets.json
python -m unittest discover -s tests -p test_sl2_f8_torus_packets.py -v
```

Acceptance uses only exact finite-group operations, integer potentials and
positive integer cycles. No SAT solver or untraced refutation is involved.
