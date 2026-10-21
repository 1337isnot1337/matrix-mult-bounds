# Uniform-cap and proper-section applications

October21,2026. Exact finite applications of written, unreviewed proofs.
No matrix tensor construction, independent review or exponent gain is claimed.
The comparison below is against the preserved main-PR75 balanced report;
it is not a replacement for the concurrent PR76 all-source research frontier.

## Imported higher-input-rank arguments

The concurrent rectangular worker proves the following statements at commit
6db658954fe976e3d433991ebf606d1d5d31a9e9. Their source files and hashes are
in sources.json; those results are adopted with their original credit.

1. `saturation.md`: if a linear map sends rank-at-most-k matrices into a
   closed variety X of dimension less than k(k+2), its whole linear image
   lies in X. For scalar Hankel rank at most r<min(a,b), dim X<=2r.
2. `two_ruling_cap.md`: if every input subspace of dimension at most k on
   either side has image dimension at most r, generic ruling dimensions
   p,q satisfy p,q<=r, and the full image dimension is bounded by

       r, if p<=k or q<=k;
       min(pq, r+(q-k)floor((r-p)/(k-1)),
                  r+(p-k)floor((r-q)/(k-1))), otherwise.

   Maximizing over1<=p,q<=r gives an exact integer upper bound. The code
   uses this general formula and does not need the sharper special k=2
   refinement from the concurrent note.
3. `quantitative_crossed_rank.md`: a source slice of scalar symbol rank s
   and crossed coefficient rank R has source rank at least(ab-1)s+R.
4. `bundle_hankel_dimension.md`: the crossed rank-at-most-R locus in the
   source coefficient space has dimension at most

       min(N,(a+b)R+floor((a-b)^2/4)),  N=ab(a+b-1).

The last result uses its stated classical bundle-splitting input and
explicit extension-space parameter count. It is not attributed to this
package. All four imported statements remain written and unreviewed.

## Local refinements and the ordinary gate

The Wronskian proof supplies the scalar linear-space cap r uniformly, with
no new coordinate-subspace certificates. `boundary_saturation.md` extends
item1 to2r=k(k+2) for scalar Hankel targets. `proper_sections.md` subtracts
one from item4 when the injective target parameter image is a proper linear
subspace of the source coefficient space.

For a rectangular block with first parameter dimensions x,y and target slice
rank z on a rank-one parameter, a rank-k parameter has source rank at most

    L_k=k*z+(N-D_B)+(N-D_C).

If L_k<(r+1)ab, every k-input ruling maps into scalar Hankel rank at most r.
The uniform linear-space cap and items1--2 then bound the whole scalar
symbol image by the computed number B. Choosing B long coordinates that
inject this image over C(x,z) injects the original block into B copies of
the ab-dimensional biform space. Hence xy<=B*ab is necessary. Polynomial
identities on complex rank-k inputs justify extension to the algebraic
closure of C(x,z), as in the preceding maintained source-to-symbol proof.

For the crossed gate, put s=min(a,b). First exclude generic symbol rank
below s on the rank-k parameter variety by the same lower-rank image bound.
This prerequisite is compulsory: the crossed inequality alone does not make
the symbol full rank. On the generic full-rank stratum, item3 gives

    R<=L_k-(ab-1)s.

The crossed-rank condition is closed, so it extends to the entire irreducible
rank-k parameter variety. That variety has dimension k(x+y-k); the lift and
the crossed coefficient map are injective. It therefore must fit in the
item4 dimension bound, reduced by one exactly when xy<N. Each saved witness
records the prerequisite and every strict inequality. No rank threshold is
rounded down, and no ordinary rank-lift estimate is imposed on singular maps.

## Balanced rectangular comparison through a12

The preserved report contains5139 improving sorted formats for balanced
sources a2,...,12; its accumulated gates exclude4645. Combining the above
credited arguments and local uniform bounds excludes254 additional formats.
All additional witnesses are saved. The remaining counts are

    a10:9,  a11:62,  a12:169,  total240.

Every format through a9 was already excluded. These are necessary-test
survivors of this explicitly stated implementation, not constructed maps.
The comparison does not assert that these240 formats survive every theorem
in the concurrent all-source branch, and it covers neither unbalanced
sources nor general rectangular direct sums.

## Complete balanced square-partition screens

For square direct sums of common target leg dimension D, a block M_n has
L_k=k*n+2(N-D). The code adds the new gates to the earlier allowed-block
filter and reuses its exact integer dynamic program unchanged. Score
intervals use the maintained denominator10^6 and integer fourth roots.
All target dimensions and all square partitions are covered in each source.

| Source | Relaxed maximizing partition | Target D | Certified upper score numerator | Critical numerator |
| --- | --- | ---: | ---: | ---: |
| A8 | (27,3,2,1) | 743 | 94620376379 | 97336000000 |
| A9 | (32,5,3,1) | 1059 | 140053290292 | 140608000000 |
| A10 | (38,3,1,1,1) | 1456 | 202837340823 | 195112000000 |
| A11 | (44,5) | 1961 | 283043244655 | 262144000000 |
| A12 | (50,6,3) | 2545 | 378403133788 | 343000000000 |

Thus every improving ordinary square direct sum from A8 and A9 is excluded
by the accumulated written proofs. The larger relaxed maxima are not
constructions. Concurrent additional tests may further reduce them.

For the old A9 candidate(32,6,2), a rank-three M32 parameter lifts to rank
722<729=9*81. Rank-eight Hankel linear spaces have dimension at most8,
and the credited three-ruling bound is11. The full1024-dimensional block
would inject into11*81=891 dimensions, a contradiction. This higher-input-
rank argument supersedes the interpretation of the saved PR75 A9 survivors.

The new proper-section refinement matters at A12 total D=2546 with an M50
block. Its rank-four variety has dimension384. The prior crossed-locus
upper bound was also384; the proper target parameter image makes the bound
383 and excludes that block configuration. The new maximum instead has
D=2545. The proofs, not this finite numerical example, justify the gate.

## Evidence limits

The application reuses the prior candidate enumeration, score intervals and
dynamic program. Those source files and historical reports remain unchanged.
The new scalar cap is proved uniformly; coordinate certificates are preserved
for provenance and need not be newly generated for these formats. Finite
replays check implementation and witnesses, not the all-size theorems.
Nothing here constructs a matrix multiplication algorithm below9/4.
