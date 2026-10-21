# Two rectangular summands with unequal leg dimensions

October 21, 2026. AI-derived, written and unreviewed. This is an extension of
existing necessary tests and an exact finite search, not a construction or a
smaller exponent. External results remain credited by the source notes.

**Update:** [low-rank saturation](saturation.md) excludes all 571 survivors of
this initial screen, including the earlier square A(8,8) target. The initial
frontier is preserved below as historical discovery data, not open ordinary-map
construction advice. Singular degenerations remain outside the obstruction.

## Score and the missing construction

Let A(a,b) be the cyclic convolution source of common leg dimension
N=ab(a+b-1). Consider an ordinary restriction to a full direct sum of blocks
M(m_j,n_j,p_j), with independent coordinates in all three legs. Write v_j=m_j n_j p_j.

The six-orientation source comparison in the anisotropic package gives the
following necessary inequality for an actual tensor character with total
parameter omega=3t:

    6^omega sum_j v_j^(omega/3) <= [3(a+b)-2]^3.

Here is the direct-sum step, which cannot be replaced by an unproved symmetry
assumption about the character. Apply the restriction in the three cyclic
orientations. The source is cyclically invariant, while the product of the
three character values of each rectangular block is v_j^(3t). Holder gives

    product_{cyclic c} (sum_j lambda(c M_j))
        >= (sum_j v_j^t)^3.

Consequently lambda(A)>=sum_j v_j^t. Repeat for the reflected source. The
product of the two source values is P(a,b)^(6t), so
P(a,b)^(3t)>=sum_j v_j^t. Combine with 6P(a,b)<=[3(a+b)-2]^(1/t).
These are the same external character hypotheses and detecting-character
implication as the [anisotropic source note](../2026-10-20-anisotropic-constructions/README.md).

At omega=9/4 the target score is sum_j(216 v_j)^(3/4). A strict score gain is
only a useful candidate gate: actual maps and the complete spectral implication
remain necessary. A passing target in the files is NOT an improved exponent.

## Asymmetric necessary conditions

Let total target leg dimensions be

    D_X=sum m_j n_j, D_Y=sum n_j p_j, D_Z=sum p_j m_j,

and k_i=N-D_i. Concision makes the three ordinary source-to-target maps
surjective. The source rank of a lifted X slice is at most its target rank
plus k_Y+k_Z; the other orientations follow cyclically.

For each block let d=(mn,np,pm), r=(p,m,n), and
L_i=r_i+sum_{h != i}k_h. The following conditions are necessary:

1. D_i<=N and L_i>=ab in every leg (minimum nonzero source slice rank).
2. If the block is not M(1,1,1), at least one L_i>=2ab. Otherwise the
   rank-one parameters in each leg have a fixed coherent long factor;
   the three-leg contraction has tensor rank at most one, contradiction.
3. For every integer s<min(a,b) with 3s<=a+b-1,
   d_i>sab implies L_i>=(s+1)ab.
4. At a+b-1=3s-1, with 2<=s<min(a,b), the boundary version replaces
   sab by max(s,4)ab in condition 3.
5. The existing square equality exclusion is used only when all total D_i
   agree and the selected block is square of size>=3, with a,b>=3 and
   a+b-1>=6. Its original hypotheses are not extended to rectangles.
6. Two scalar summands cannot have 2+k_h+k_l<2ab in all three legs.
   Their lifted two-dimensional spaces would again force a rank-one tensor.

Conditions 2 and 3 also allow rectangular parameters with one index equal to
one: the remaining rank-one ruling is a linear space, and the same fixed-factor
argument applies. A one-dimensional parameter space is immediate. In condition
3 the maintained symbol lemma is explicitly stated for arbitrary l-by-h matrices;
its proof injects the full lifted parameter space into s copies of the
ab-dimensional coefficient space. It therefore applies to d_i, not just n^2.

Dependencies and proof status:
- [Polynomial rank locus and three-leg factorization](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md).
- [General Hankel symbol dimension lemma](../2026-10-20-anisotropic-constructions/hankel_symbol_dimension.md).
- [Boundary symbol lemma](../2026-10-20-anisotropic-constructions/hankel_boundary_dimension.md).
- [Original square frontier and equality refinement](../2026-10-20-anisotropic-constructions/square_sum_frontier.md).

These supporting proofs are themselves written and unreviewed. This extension
is conditional on their correctness. None of the lifted-rank inequalities is
asserted for singular degenerations.

## Exhaustive finite two-block search

The code enumerates exactly TWO positive rectangular blocks. The first block
is sorted m<=n<=p; the second retains every distinct orientation. Blocks are
ordered by volume. This is exhaustive for the score and necessary conditions,
which are invariant under simultaneous permutations of matrix indices and
exchange of blocks. This symmetry reduction is not a claim that A(a,b) is
invariant under every reflection. The conditions hold in all three legs and
are numerically reflection-invariant.

Every block pair dimension is at most N, so n<=sqrt(N), p<=N/n in sorted
coordinates. For a fixed first block, let R_i=N-d_i be the residual capacities.
A second block satisfies v_2^2<=R_X R_Y R_Z. This integer-square-root bound
rejects impossible first blocks before enumeration. The second block is then
enumerated directly in its residual capacities, in all orientations. A binary
search for its minimum score-eligible integer volume skips irrelevant p values.
Scores are enclosed by integer fourth roots with denominator 10^6; all pruning
uses certified upper bounds, never floating-point estimates. A surviving
interval straddling the threshold remains undecided, not accepted.

Reports include normalization counts, score-eligible pairs, dimension-eligible
pairs, the first violated condition, and all survivors. They need not count
pairwise nonisomorphic tensors; volume ties can be represented more than once.
This is not a search over arbitrary numbers of blocks or over tensor powers.

Reproduce from repository root:

    python research/ai/2026-10-21-rectangular-direct-sums/screen.py 5 6 --output results/local/rectangular-a5b6.json
    python -m unittest discover -s tests -p test_rectangular_direct_sums.py -v

The controls include actual known restrictions, the existing unconstructed
A(8,8) square frontier, exact root inequalities, permutation invariance, and
comparison of score pruning against unpruned enumeration at three small formats.

## Completed frontier and first surviving format

The saved `frontier.json` covers all 62 formats 2<=a<=b with N<=960.
Across them, 5,113,297 dimension-compatible, score-eligible normalized pairs
were checked. All 60 formats other than A(7,9) and A(8,8) have no survivors.
The first surviving format by leg dimension is A(7,9), N=945, whereas the
existing square-partition frontier first survives at N=960. These are
frontiers of necessary conditions, not frontiers of actual constructions.
There are 19 normalized surviving pairs at A(7,9), and 552 at A(8,8).

A representative strongest-score survivor at A(7,9) is

    M(27,27,28) direct-sum M(6,6,2).

Its total target leg dimensions are (765,768,768). The exact score enclosure
at 9/4 is [97610234481,97610234483]/10^6, above 46^3=97336.
If actual maps were constructed, the source comparison would imply an
exponent below 4499/2000=2.2495. The conditional arithmetic has the integer
certificate

    4408992^4499 > 95972^6000,
    15552^4499 > 1390^6000,
    95972+1390=97362 > 97336.

This is NOT a proved exponent: the maps are missing. The numerical root
2.24944539263026 is only a descriptive solution of the conditional comparison.
The rational certificate is tested without logarithms. No preference between
surviving orientations is supported by a construction yet.

Validation checkpoint: five dedicated tests pass, including independent naive
small enumerations. A 400-test regression run passed on the initial screen;
the subsequent volume-pruning optimization was separately checked by the five
dedicated tests and the full recorded frontier. Further integration validation
will be recorded separately. Finite checks do not constitute independent review.

## Extended checkpoint

The strengthened projection lemma in `saturation.md` and the proof in
`second_boundary.md` extend the search through N<=1500. There are 24 extra
formats above 960. The only remaining necessary-test formats are A(8,9),
A(8,10), and A(9,9), with 62, 3687, and 1263 normalized retained pairs.
All 1143 initial A(7,10) candidates are now excluded. These counts include
possible symmetry duplicates; none is a constructed restriction.

Reproduce the compact extended report and all four support certificates:

    python research/ai/2026-10-21-rectangular-direct-sums/extended_search.py --maximum 1500 --directory results/local/rectangular-extension
    python -m unittest discover -s tests -p 'test_rectangular*.py' -v

The report hashes complete lists with SHA256 of sorted-key compact JSON,
and includes the first 20 survivors in deterministic enumeration order.
Those rows are not necessarily sorted by score. The large intermediate
lists are regenerated in memory rather than committed as a 19 MB artifact.
`equality_next.md` records the next obstruction question and an exact
counterexample to an overly broad full-row-rank equality conjecture.

The final counts above include `block_hankel_dimension.md`. This excludes
306 additional candidates, including M30 plus M3 across the three remaining formats.
The dimension proof requires the exact equality threshold; `equality_one_step.py`
certifies that a one-unit rank excess is genuinely possible. The first remaining
source format is still A(8,9), and no surviving target has been constructed.

`quantitative_crossed_rank.md` strengthens the equality statement to
rank(M_F)>=(ab-1)rank(B_F)+rank(T_F). The proof uses an elementary
polynomial-span growth lemma. It is written and unreviewed. Higher crossed
rank bounds do not enter the finite screen without corresponding proved
block-Hankel dimension bounds; no threshold is rounded upward.
