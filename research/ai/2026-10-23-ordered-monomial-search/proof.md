# An all-size asymmetry of the shared-input score

This statement concerns the historical monomial score defined in
`research/ai/2026-10-20/search_degenerations.py`, pinned in `sources.json`.
It is a written, unreviewed proof about that score, not a tensor-exponent
improvement. PR118 already identifies the distinguished shared first input
and preserves it in exact candidate ordering. The family below explains why
restricting the exhaustive dimension inventory to `a <= b` is not justified
by input exchange or by pointwise score dominance.

## Definition and claim

For normalized integer weights `x_i,y_j`, retain precisely the convolution
terms `(i,j,i+j)` minimizing `x_i+y_j` on their output diagonal. Partition
these terms by connected components of the bipartite graph on the second
input and output coordinates. The first input is shared. A component that
is a convolution after ordered reindexing and axis reversals receives its
profile value `P_*(r,s)`; any other component receives the largest number of
terms in a single coordinate slice. Sum these component scores.

For every integer `m >= 2`, take

    x = (0,0,0),     y = (0,1,0,1,...,0,1) of length 2m.

Then the score with `x` shared is `max(3,m)+1`, whereas the score with `y`
shared is `2m+1`. Their common source profile is

    P_*(3,2m) = (14/9)(2m+1).

Thus the swapped score has ratio `9/14` to the source. The ratio of swapped
to original target scores tends to two. In particular, an exhaustive search
of `a <= b` cannot represent all ordered candidates by swapping inputs while
preserving the score, nor can it discard the reverse by pointwise dominance.
This does not say that either orientation has a better *global* maximum.

## Exact support

On each output diagonal except the last, an available even second-input
index gives weight zero. The final diagonal contains only `(2,2m-1,2m+1)`
and has weight one. Therefore the retained support is exactly

    {(i,2r,i+2r) : 0 <= i <= 2, 0 <= r < m}
      union {(2,2m-1,2m+1)}.

All coefficients are one. The support calculation uses only integer
weights and works over every field.

## First input shared

The output intervals `[2r,2r+2]` of consecutive even second-input
coordinates meet. Consequently the `3m` terms with even second input form
one connected component. Its coordinate dimensions are `(3,m,2m+1)`.
For `m >= 2` no coordinate dimension is the sum of the other two minus
one, so the maintained recognition rule cannot identify a convolution.
Its largest coordinate slice has size `max(3,m)`: fixed first coordinates
have `m` terms, fixed second coordinates have three, and fixed output
coordinates have at most two. The final term is a separate component and
has score one. The total is `max(3,m)+1`.

## Second input shared

After swapping inputs, the first `3m` terms are `(2r,i,i+2r)`. In the
nonshared-coordinate graph, output parity equals `i` parity. There are
two components. The component with `i=1` has `m` terms and is a `C(m,1)`
convolution, so its score is `m`.

The even component has `i=0,2`; their consecutive output sets overlap.
The final term attaches to `i=2` and adds its new output `2m+1`. This
component has dimensions `(m+1,2,m+2)` and `2m+1` terms. Only its third
axis could serve as the convolution output, but a convolution of those
dimensions would have `2(m+1)` terms. Thus it is not recognized.
The largest slice is the `i=2` slice, of size `m+1`; the other slice
sizes are at most `m`, two, or one. The total score is `m+(m+1)=2m+1`.

Finally, `h_3=(4/3)(7/6)=14/9` gives the displayed source profile.
This proves the claim for all `m >= 2`. Exact replay for `m=2,...,12`
checks the stated formulas through a separate support verifier; the finite
checks support the argument and do not replace it.

## Attribution and limits

The profile, support degeneration, component score and slice fallback are
prior repository work; no priority is claimed for those ingredients.
The ordered family and its component calculation are owner-directed Codex
continuations. The independently implemented verifier is software
independence, not independent mathematical review. The proof does not
classify arbitrary bases, arbitrary integer-weight scores or actual tensor
characters, and supplies no smaller matrix-multiplication exponent.
