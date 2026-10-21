# Complete common-profile screen for the A(8,8) target

## Result and scope

There is no ordinary complex restriction

\[
 A(8,8)\longrightarrow M_{27}\oplus M_7
\]

preserving the source grading `weight(F(i,k,s))=i+s-k` if each square
summand uses a common integer vertex-charge list on its three vertex
spaces. The two summands can use different lists. A target matrix unit
has its row charge minus its column charge. All three linear maps may
vary freely within their weight blocks.

The conclusion combines a complete finite enumeration with the written
[zero-grade minimum-rank lemma](parity_structure_zero_grade_rank.md),
the ordered-block rank inequalities, and the
[boundary-profile theorem](torus_boundary_profile.md). It concerns this
fixed source grading and ordinary restrictions. Different vertex lists
on the three sides, ungraded maps, and arbitrary singular degenerations
remain outside its scope. It establishes no smaller exponent.

The two endpoint arguments below close every profile left by the exact
enumeration. The enumeration is not a search over numerical map
coefficients, and a failed numerical fit is not used as an exclusion.
The local arguments and code have no external independent review or
formalization.

The later [support-peeling proof](torus_support_peeling.md) gives a
shorter, stronger exclusion covering unequal profiles as well. This
complete enumeration is retained as an independent record of the earlier
common-profile approach and of the zero-grade rank constraint.

## Why the charge-profile domain is finite and complete

The source dimensions at absolute weights 0 through 14 are

\[
 S=(64,63,61,58,54,49,43,36,28,21,15,10,6,3,1).
 \tag{1}
\]

An ordinary map from a concise target into the source is injective.
Thus no target matrix unit can have weight outside this interval. Each
common vertex list consequently has width at most 14. Translate the
two block lists independently so that both minimum charges are zero.
These translations leave all their matrix-unit weights unchanged.

Write `m_j` for the 27-block multiplicities and `n_j` for the seven-block
multiplicities, padding each list to fifteen bins. The zero-weight target
dimension is

\[
 T_0=\sum_jm_j^2+\sum_jn_j^2.
\]

Distributing 27 vertices over at most fifteen bins gives
`sum(m_j^2)>=51`, with equality for twelve twos and three ones. If the
seven-block list had no singleton bin, its squared multiplicities would
sum to at least `3^2+2^2+2^2=17`. That would give `T_0>=68>64`, violating
source capacity. Therefore every capacity-feasible profile has a scalar
slice in the seven-block zero-weight tensor.

The [zero-grade lemma](parity_structure_zero_grade_rank.md) says every
nonzero source zero-grade slice has matrix rank at least eight. Lifting
the target rank-one scalar slice and deleting `64-T_0` directions on
each of its two other legs gives

\[
 8\le1+2(64-T_0),\qquad T_0\le60.
 \tag{2}
\]

The squared multiplicity sum of an integer list has the parity of its
total size. The only remaining pairs of squared sums are therefore

\[
 (\sum m_j^2,\sum n_j^2)\in\{(51,7),(53,7),(51,9)\}.
 \tag{3}
\]

For the large list put `x_j=m_j-2`. Its total and squared sum obey

\[
 \sum x_j=-3,\qquad
 \sum m_j^2=48+\sum x_j^2\le53.
\]

Since `x_j>=-2` is integral, there are exactly three possibilities:

| Large-list pattern in fifteen bins | Squared multiplicity sum |
| --- | ---: |
| Three ones and twelve twos | 51 |
| One zero, one one, and thirteen twos | 53 |
| Four ones, one three, and ten twos | 53 |

The second pattern includes width-13 lists after trimming a trailing
zero. A leading zero represents the same list after translation and is
not a separate case. For the small block, squared sum seven means seven
distinct charges. Squared sum nine means one doubled charge and five
singleton charges. The program generates all their supports, including
holes: respectively `binomial(14,6)=3003` and
`6*binomial(14,5)=12012` normalized lists.

We remove simultaneous charge reflection, which is a symmetry of the
source and target. The large list is chosen lexicographically no larger
than its reversal. Both orientations of the small list remain when the
large list is asymmetric. Only when the large list is palindromic is the
small list also selected no larger than its reversal. Independent
reflection of the two summands is not assumed to be a source symmetry.

These reductions account for all integer lists in the stated scope;
neither positivity at intermediate charges nor consecutive small-block
charges is assumed.

## Exact ordered-block rank tests

For a common profile `m`, its leg dimension at absolute weight `w` is

\[
 T_m(w)=\sum_jm_jm_{j+w}.
 \tag{4}
\]

The direct-sum dimensions add. Capacity requires
`T_m(w)+T_n(w)<=S(w)` at every weight.

For ordered input weights `x,y`, the target block's third flattening has
rank

\[
 R_m(x,y)=\sum_{j:m_j>0}m_{j+x}m_{j-y},
 \tag{5}
\]

with out-of-range entries zero. The middle multiplicity is a positivity
condition, not an extra factor: it determines whether each third-leg
matrix coordinate occurs. Different third coordinates have disjoint
supports in the first-two-leg coordinate pairs. The direct-sum ranks
add in (5).

The source has a term at

\[
 X=(i,p+q,s),\quad Y=(j,p,r+s),\quad Z=(i+j,q,r),
 \qquad 0\le i,j,p,q,r,s<8.
\]

Its ordered grades are `x=i+s-p-q`, `y=j+p-r-s`, and `-x-y`.
Fixing the first two source coordinates uniquely determines the third.
Thus distinct appearing third coordinates again have disjoint supports.
The program enumerates all 262,144 source terms and counts those
coordinates in each of the 631 valid ordered grade pairs. These counts
are exact flattening ranks, not merely support upper bounds.

Two elementary rank inequalities are used. Every restriction satisfies

\[
 R_{\rm target}(x,y)\le R_{\rm source}(x,y).
 \tag{6}
\]

If both input weight blocks are saturated, their target-to-source maps
are isomorphisms. Restricting the third leg can then remove at most its
codimension from the source flattening rank, so

\[
 R_{\rm source}(x,y)-[S(-x-y)-T(-x-y)]
       \le R_{\rm target}(x,y).
 \tag{7}
\]

Every saturated ordered pair is checked in (7). For (6), only the two
ordered blocks `(13,-13,0)` and `(12,-12,0)` are needed by this complete
screen. Their source ranks are four and nine. The program does not
claim to check (6) at all 631 blocks for every candidate.

For an orientation-sensitive control, the width-13 profile
`(1,2,2,...,2)` with small charges zero through six has saturated blocks
at degrees -11 and 11. The source rank is sixteen; the target rank is
nine in that order and twelve in the opposite order. Third-leg loss
four would leave source rank at least twelve, contradicting the first
order. This is the same local example treated by the maintained
ordered-block screen.

## Complete enumeration and the last two proof classes

The exact replay gives the following counts. These are normalized
charge-list pairs, not counts of tensor isomorphism classes.

| Stage | Remaining count |
| --- | ---: |
| Large-list reflection representatives from the three complete patterns | 7,847 |
| Large lists passing their own weight capacities | 85 |
| Canonical large/small pairs to examine after (3) | 265,783 |
| Pairs passing combined weight capacity | 38,482 |
| Pairs passing every saturated-input lower-rank test | 14,220 |
| Pairs also passing the two selected upper-rank tests | 5,604 |
| Unclassified pairs after the written endpoint proofs below | 0 |

Of the 85 large lists, one has zero count 51 and 84 have zero count 53.
All 5,604 last-stage pairs have seven distinct small charges. Their large
lists have singleton multiplicities at 0, 1, 13 and 14, multiplicity two
at charges 2 through 12, and one extra vertex at an interior charge.
After reflection, only extra-vertex positions 7 through 11 remain.

| Position of the large list's multiplicity three | Small width at most 12 | Small width 13 | Total |
| ---: | ---: | ---: | ---: |
| 7 | 468 | 329 | 797 |
| 8 | 917 | 658 | 1,575 |
| 9 | 917 | 658 | 1,575 |
| 10 | 742 | 476 | 1,218 |
| 11 | 301 | 138 | 439 |
| Total | 3,345 | 2,259 | 5,604 |

**Small width at most twelve.** The auxiliary summand has no coordinates
at degrees ±13 or ±14. All large lists satisfy

\[
 m_0=m_1=m_{13}=m_{14}=1,\qquad m_2,m_{12}\ge2.
\]

These are exactly the hypotheses of the
[boundary-profile extension](torus_boundary_profile.md). The extension
uses a class of profiles preserved by reflection and leg reversal; it
does not require a symmetric position for the extra interior vertex.
It excludes all 3,345 cases.

**Small width thirteen.** The small list has one endpoint vertex at zero
and one at thirteen. Consequently each total target degree ±13 space
has dimension three: two coordinates from the large block and one from
the small block. Both source degree spaces also have dimension three,
so their maps are isomorphisms. The negative-positive source product
table from [the cube-determinant proof](torus_saturated_pencil.md) is

\[
 G=\begin{pmatrix}v&h&a\\a&0&0\\w&a&0\end{pmatrix},
 \qquad\det G=a^3,\qquad a=F(0,7,7).
 \tag{8}
\]

Evaluate the third target input at the large block's charge-zero
diagonal. The two extreme target units at degrees -14 and 14 force
`a` on its source lift to be nonzero. Thus the source matrix in (8)
has rank three. The corresponding target matrix has rank one: only
the large path through charge thirteen contributes. The other large
degree-13 path ends at charge one, and the whole small summand vanishes
at this large-block input. Independent invertible transformations of
the first two spaces preserve rank. This contradiction excludes all
2,259 cases. Auxiliary degree-13 coordinates are explicitly retained
in this argument; no absence hypothesis is being borrowed from the
earlier single-block formulation.

The two cases exhaust the enumeration, proving the stated common-profile
exclusion. The later support-peeling theorem also excludes unequal vertex
profiles in the same ordinary homogeneous-map model.

## Replay and certificate

The generator and verifier are
[parity_structure_common_profiles.py](parity_structure_common_profiles.py).
The compact [JSON certificate](parity_structure_common_profiles.json)
stores the exact counts, rejection categories, five terminal large
profiles, representatives of both final proof classes, and a SHA-256
of the deterministic stream of all 5,604 terminal pairs. Replay
regenerates the domain and the complete classification; it does not
accept stored Boolean conclusions.

```sh
python -S research/ai/2026-10-20-anisotropic-constructions/parity_structure_common_profiles.py
python -S -m unittest discover -s tests -p test_parity_structure_common_profiles.py -v
```

The maintained tests also check the ordered width-13 counterexample,
both terminal classes, the full zero-grade coordinate replay, and
rejection of a nonzero-to-nonzero change in a saved enumeration count.
All use only the Python standard library. The proof dependencies and
precise restriction model remain necessary even when every test passes.
