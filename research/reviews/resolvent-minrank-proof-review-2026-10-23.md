# Review of the fixed-resolvent minimum-rank certificate

**Claim:** `AI-RESOLVENT-SHARP-MINRANK-001`, Sections 1--4 of
[`proof.md`](../ai/2026-10-23-resolvent-minrank/proof.md).

**Source pin:** repository commit `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`;
the proof is Git blob `92eadeac412b1d83ce5ee306a1e4f5a5da8df5d1`, the verifier
is blob `11b15d6db6c8c35ed1ef23bd975ae1be2828fdfa`, and the 31-stage
certificate is blob `6b16a81eb4fa19ef394ecf98c4f6b264058ea75a`.

**Conclusion:** I found no gap in the stated all-field minimum-rank-six proof
for the specified 112-dimensional matrix space, nor in its constant
compression consequences. This is a first-party Codex audit, not independent
human review. The claim remains `proof-written-unreviewed`. Section 5's
fixed-resolvent Laurent transfer is outside this review. No general singular
degeneration or exponent improvement follows.

## Source normalization and the 31-dimensional block

The verifier rebuilds the 28-by-28 outer source matrices from
`S(f)[(j,L),(H,r)] = f[H-j,L-r]`, reconstructs the integer inverse of the
unit matrix `K`, and checks both inverse products. It then compares all 112
normalized source slices against the literal six-index source expansion.
The focused test also compares that expansion with a separate direct tensor
construction. These checks support the coordinate formulas and the identity
`N = E_(3,0) tensor G(e00)`, with `N^2 = 0` and rank 16.

The gauge relation is valid: `G(f_*) = I`, so `Q(f_*) = G(e00)`. Replacing
`f` by `f - f_03 f_*` and `g` by `g + f_03 e_00` preserves
`G(g) + Q(f)` and removes the single redundant coordinate. The resulting
31 generators are exactly the sixteen `S` matrices and the fifteen retained
`Q` matrices reconstructed by `mixed_basis()`.

At each stage, the selected six distinct rows and columns form a lower
triangular submatrix whose diagonal entries are the same linear form up to
units `+1` or `-1`. Its determinant is therefore a unit times the sixth
power of that form over every field. Rank at most five forces the form to be
zero. The pivot coefficient is a unit, so solving for that coordinate and
substituting it preserves the represented matrix over every characteristic.
The next certified stage applies to precisely the resulting basis. After all
31 eliminations the basis is empty, proving that no nonzero combination has
rank at most five and that the generators are independent. The verifier
checks the complete integer coefficient vectors, all entries above the
diagonal, each diagonal form, every pivot and substitution, and exhaustion.

The reported witness `S(e00)G(e00)` is nonzero with at most six nonzero rows.
The lower bound just proved makes its rank exactly six. Hence the mixed
block has dimension 31 and minimum nonzero rank six.

## The full space and compression bounds

The 16 leading-coefficient cases for the outer source are checked by
triangular 16-by-16 minors. For any nonzero outer coefficient array, choose
its last nonzero coefficient in the stated lexicographic order; the
corresponding minor has that coefficient on every diagonal entry and zeros
above the diagonal. This gives ordinary rank at least 16. The normalized
slice tests verify the block shifts used to place these outer maps in the
four-by-four block form.

In the full space, the scalar identity occupies block `(0,0)`, while the
two lower-middle coefficient families occupy distinct blocks `(1,0)` and
`(2,0)`. If either family is nonzero, the rank is at least 16 by the outer
bound. If both vanish and the scalar vanishes, only the last block row
remains. Its nonzero blocks have rank at least six by the mixed-block result.
The single-block witness at `(3,1)` attains six. The separated block
coordinates also show independence of all 112 listed generators, giving
`dim W = 112` and minimum rank six.

For linear maps `P` and `C`, the elementary rank-loss estimate is
`rank(PXC) >= rank(X) - (112-rank(P)) - (112-rank(C))`: restricting the
domain to `im(C)` loses at most its codimension, and applying `P` loses at
most `dim ker(P)`. For every nonzero `X` in `W`, rank is at least six.
Therefore total rank loss at most five leaves `PXC` nonzero, so the linear
map `X -> PXC` is injective. If both maps have rank 109 and `PXC=0` for a
nonzero `X`, the same estimate gives rank `X=6` and rank `X|im(C)=3`.
Since `ker(P)` has dimension three, `X(im(C))=ker(P)`. Comparing kernel
dimensions gives `ker(X) subset im(C)` and then `im(C)=X^-1(ker(P))`.
The block support argument places this three-dimensional kernel in the final
28-dimensional output layer, as stated.

## Reproduction and limits

From the repository root I ran:

```sh
python research/ai/2026-10-23-resolvent-minrank/verify.py \
  results/resolvent-minrank-2026-10-23/certificate.json
python -m unittest discover -s tests -p test_resolvent_minrank.py -v
```

The verifier reported all 112 normalized slices, all 31 elimination stages,
the outer rank-16 cases, the 31-dimensional mixed block, and the full
112-dimensional minimum-rank-six space. All five focused tests passed. The
certificate is an exact finite replay of its integer identities; it is not a
formalization of the accompanying linear-algebra proofs. The review does not
classify all rank-six matrices or extend the result to arbitrary singular
long-map trajectories. The associated narrow target application is also not
reviewed here.
