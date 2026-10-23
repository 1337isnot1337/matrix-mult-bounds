# Fixed components obstruct every finite standard-flip continuation

Claim `AI-EXTERNAL-FIXED-FLIP-GRID-004`: written unreviewed implication
with exact finite certificates. The separate trace continuation is claim
`AI-EXTERNAL-FIVE-SPLIT-TRACE-005`.

For each of the two explicit split seeds below, every finite sequence of
standard shared-factor flips retains 50 particular third-factor
directions. Those directions require at least ten rank-at-most-four
groups. Therefore none of these continuations admits a termwise
assignment to the Q(6,4) evaluation grid **with the third factor on a
long leg in the specified alignment**. The 25-dimensional target leg
is assigned to the first source leg; both 20-dimensional target legs
are then long legs.

This is a uniform obstruction to the proposed flip search from these
two seeds. It includes coefficients in characteristic-zero Laurent
fields and the common invertible physical transformations used by the
border constructions. It does not exclude other seeds, other target-leg
alignments, general source maps that are not termwise assignments, or
additional singular limits. It gives no exponent improvement.

The companion [trace proof](TRACE_PROOF.md) adds a separate conclusion
for the five-split seed: its isolated components have a positive scalar
trace pairing, which prevents a further nonempty subset deletion by the
physical matrix-multiplication stabilizer after these flips. This stronger
conclusion is not claimed for the four-split seed.

## Source data and the two constant seeds

We use the externally credited AlphaTensor rank-76 factorization of
M(4,5,5), with physical factor shapes 4-by-5, 5-by-5, and 5-by-4.
The original [source package](../2026-10-21-external-grid-seed/README.md)
records Fawzi et al., Nature (2022), the Lille catalogue, Perminov's
conversion, the source hashes, and the full coefficient convention.
The verifier reads its byte-pinned `factors.json`; no external
factorization is attributed to this investigation.

Let the original factors be U_i, V_i, W_i, for 0 <= i < 76. Retain V_i
and W_i, and replace the following first factors. Every right-hand side
refers to an original factor, and indices are zero based.

| Seed | First-factor replacements |
| --- | --- |
| Four-split | U_0 = -U_18; U_17 = U_8; U_48 = -U_2; U_56 = -U_22 |
| Five-split | U_16 = U_57; U_47 = -U_52; U_31 = -U_48; U_26 = U_32; U_54 = -U_60 |

Write S for the resulting constant 76-term tensor. **S is not asserted
to equal matrix multiplication.** The associated split constructions
give M = S + D, where D is the discarded error. They then apply a common
physical transformation G(epsilon) that fixes M and sends D to zero in
the limit. Their retained Laurent family is G(epsilon)S. The present
certificate reconstructs S directly and proves a statement about its
finite flip continuations. The transfer to G(epsilon)S is proved below;
it does not substitute an unrelated constant exact decomposition for
that border family.

## Component certificate

Join two term indices whenever their nonzero factors are proportional
on at least one of the three legs. Let C range over the connected
components. For a leg L, let E_(C,L) be the span of the initial factors
on that leg in component C. The exact replay establishes the following
facts for each seed.

1. For distinct components C and C', the intersection
   E_(C,L) intersect E_(C',L) is zero, separately on every leg L.
2. Within a component C, the vectors V_i are linearly independent.
   The vectors Z_i = U_i tensor W_i are also linearly independent.
3. Exactly 50 components have third-leg span of dimension one. Their
   50 distinct projective directions span dimension 20.

| Seed | Component sizes and counts | Pair-and-leg disjointness checks | Fixed third directions |
| --- | --- | ---: | ---: |
| Four-split | 36 of size 1; 15 of size 2; 2 of size 3; 1 of size 4 | 4,293 | 50 |
| Five-split | 36 of size 1; 15 of size 2; 2 of size 5 | 4,134 | 50 |

The larger four-split components are {0,18,25}, {2,47,48}, and
{22,29,56,75}; {8,17} is its additional shared-first-factor pair.
The five-split components of size five are {16,54,57,60,63} and
{31,47,48,51,52}; {26,32} is its additional shared-first-factor pair.
The full partitions, leg dimensions, fixed-direction representatives,
and weights are retained in `certificate.json` and reconstructed by the
verifier.

The program first selects each component span basis by exact rational
elimination. For each pair it checks that the concatenated basis has
rank equal to the sum of the two dimensions modulo 101. A nonzero
minor modulo 101 is a nonzero integer minor, so this proves the required
rational independence. The independence checks for V_i and Z_i use the
same implication. Every rational rank remains unchanged over any
characteristic-zero extension K of Q, including C((epsilon)).

### Why the components remain isolated

A standard flip is an exact two-term transformation on a shared
projective factor. After absorbing a nonzero scalar so that the shared
factors are equal, the two remaining factor matrices B and C can be
replaced by B H and C H^(-transpose), for H in GL_2(K). This preserves
their tensor sum. The other two choices of shared leg are allowed.
Factor gauges whose three nonzero scalars have product one, and
permutations of the terms, are also allowed. These gauges preserve each
complete rank-one tensor term.

Suppose every current factor remains in its initial component leg span.
Two terms in different components cannot share a nonzero factor: their
corresponding spans have zero intersection. Every admissible flip
therefore acts within one component, preserves that component tensor,
and keeps its factors in the same three leg spans.

There is no exception from a zero term. If a component has r terms,
its flattening across the middle leg is

\[
\left[U_i\otimes W_i\right]_{i\in C}
\left[V_i\right]_{i\in C}^{\mathsf T}.
\]

Both matrices have column rank r, so this flattening has rank r. A
representation of the same tensor with r displayed terms cannot have
a zero term, because its flattening would then have rank at most r-1.
This reasoning holds over K. Starting from the initial partition,
induction now proves the claimed isolation for every finite sequence of
standard flips. In particular, whenever dim E_(C,W) = 1, every current
W factor in that component lies on the same nonzero line. All 50 such
directions must remain represented.

The argument concerns finite exact flips of the displayed terms. It
does not equate the entire space of rank-76 decompositions with this
flip orbit. Nor does it allow a separate limiting operation to change
the component tensor while invoking the same rank argument.

## Exact weights on the 50 permanent directions

Order components by their least term index, and keep those with a
one-dimensional third-leg span. Normalize the W vector of the first
term of each component to a primitive integer vector with positive
first nonzero coordinate. This gives the 50-vector ordering used by
the displayed integer weights in `verify.py` and `certificate.json`.

| Seed | Total weight | Maximum weight in a rank-at-most-four set | Nine-group capacity | Minimum number of groups |
| --- | ---: | ---: | ---: | ---: |
| Four-split | 148 | 16 | 144 | 10 |
| Five-split | 74 | 8 | 72 | 10 |

For each seed the replay checks all C(50,4) = 230,300 four-subsets over
F_101. There are 229,716 independent subsets for the four-split seed and
229,803 for the five-split seed. For each independent subset, the C99
enumerator tests all 50 vectors for membership in its span and sums
their nonnegative integer weights. The complete outputs are
`four_enumeration.json` and `five_enumeration.json`. Each reported cap
is also attained by a rational rank-four equality witness, checked by
Python independently of the exhaustive run.

The full finite-field span has dimension 20. Every smaller span of a
subset of these vectors therefore extends to one of the enumerated
rank-four spans. Nonnegative weights make the cap valid for the
smaller set as well. If a set of the integer vectors has rank at most
four over K, all its five-minors are zero integers, and reduction modulo
101 still has rank at most four. Thus the same weight cap applies over
K. Modular reduction may add dependencies; that cannot invalidate this
direction of the argument.

The weights were found by numerical optimization during discovery.
Acceptance uses only the retained integers and the exhaustive exact
enumeration. No optimizer output or floating-point objective is a
premise, and replay needs neither SciPy nor SymPy.

### Transfer to the physical Laurent families and the grid

For invertible physical matrices R, S, and T over K, the changes

\[
U\longmapsto R^{-1}US,\qquad
V\longmapsto S^{-1}VT,\qquad
W\longmapsto T^{-1}WR
\]

are common invertible linear maps on the three factor spaces. They
preserve every component intersection, flattening rank, and projective
incidence. Conjugating a shared-factor flip by these maps gives another
shared-factor flip with the same scalar coefficients. The constant
certificate therefore applies to the actual retained Laurent families,
and to every finite flip continuation of those families over K.

The [evaluation-grid argument](../2026-10-21-external-grid-seed/README.md#why-a-q64-evaluation-grid-has-small-groups)
gives nine groups of dimension at most four on each long leg of Q(6,4).
Arbitrary linear source maps preserve these dimensions. In the specified
alignment, any termwise assignment of the full generic retained family
must cover its W directions by those nine groups. Common invertible
target transformations and factor gauges do not change
their ranks. For nonnegative weights, a union of nine groups has weight
at most nine times the cap, even if groups overlap. The inequalities
148 > 144 and 74 > 72 prove the obstruction for both seeds.

This transfer is a statement over the generic Laurent field. Merely
taking leading coefficients or specializing a singular limit can change
incidences and is not covered by this argument.

## Replay, coverage, and next constructions

From the repository root:

```sh
python research/ai/2026-10-23-fixed-flip-components/verify.py
python research/ai/2026-10-23-fixed-flip-components/verify.py --enumerate
python research/ai/2026-10-23-fixed-flip-components/trace_invariant.py
python -m unittest discover -s tests -p 'test_fixed_flip_components.py' -v
```

The quick component verifier checks the source hash, reconstructs both
seeds and component partitions, checks every disjointness and flattening
rank, and validates the stored enumeration counters and exact equality
witnesses. Its output explicitly says that enumeration was not rerun.
The `--enumerate` command compiles the prior package's
`weighted_flats.c` in a temporary directory, repeats all 460,600
four-subsets, and compares the complete outputs with both retained runs.
`certificate.json` records that completed full replay. The tests also
run it when a C99 compiler is available, and otherwise skip only that
compiler-dependent check. They include corruption controls and an exact
nontrivial shared-factor flip that preserves the component certificate.

The construction consequence is specific: further random standard
flips of these two seeds cannot repair this termwise grid assignment.
A new construction must change the seed or use operations outside the
proved invariant. Other split choices, a new decomposition, or a
singular construction remain possible; passing a weighted screen alone
would still not construct the required source maps.

The written implication and exact finite certificates are AI-derived
work from the same research session. Their evidence status remains
unreviewed; reproducibility and code checks do not establish independent
mathematical review.
