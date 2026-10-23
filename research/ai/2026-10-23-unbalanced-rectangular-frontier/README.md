# Three surviving single-rectangular formats through source dimension 1377

October 23, 2026. Finite application of the prior written, unreviewed
complex source-rank and Hankel theorems. Owner-directed OpenAI Codex work;
no independent mathematical review, construction or improved exponent.

For every cyclic source A(a,b) with 2<=a<=b and
N=ab(a+b-1)<=1377, enumerate every sorted single matrix target
M(l,h,n), l<=h<=n, with all three target legs fitting in N and

    216*l*h*n > [3(a+b)-2]^4.

The adopted minimum-rank, polynomial rank-locus and Hankel gates exclude
**2110 of2113 improving shapes in82 source formats**. Exactly three
necessary-test survivors remain, all from A(8,9), N=1152:

| Target | Three target leg dimensions | Volume |
| --- | --- | ---: |
| M(28,31,31) | (868,961,868) | 26908 |
| M(29,30,31) | (870,930,899) | 26970 |
| M30 | (900,900,900) | 27000 |

Thus the first surviving source dimension for this single-rectangular
screen is1152, and no other source through1377 survives. The balanced
single-rectangular frontier still first survives at A10, dimension1900;
this extends the earlier enumeration to unequal source lengths rather
than changing its balanced conclusion. The report exports every tested
shape and a complete exact witness for each exclusion. The three missing
target maps are not supplied, and survival is not evidence of existence.

## Adopted mathematical gates

Use the [prior polynomial rank-locus theorem](../2026-10-20-anisotropic-constructions/polynomial_rank_locus.md),
the [Hankel theorem](../2026-10-21-hankel-pencil-degree/proof.md), and its
[source-to-symbol injection](../2026-10-21-hankel-pencil-degree/application.md).
Their proofs, external dependencies, field assumptions and credit are
unchanged. The earlier balanced rectangular screen supplies the model
for this finite application. No new general rank inequality is proved.

For a cyclic ordering (x,y,z) of a target shape, the first matrix
parameter space has dimension xy. A rank-one parameter has target slice
rank z, and its ordinary source lift has rank at most

    R=z+(N-yz)+(N-zx).

The following sufficient exclusion witnesses are used:

1. R<ab, contrary to the minimum nonzero source slice rank.
2. R<2ab and xy>ab, contrary to the polynomial rank-locus bound.
3. For an integer r with 1<=r<min(a,b) and5r<2(a+b),
   R<(r+1)ab and xy>B*ab, where
   B=max(r,max(1,floor((3r-a-b+4)/2))^2).

The third condition includes the credited fixed-scheme and first-boundary
cases; r=1 is already included in the second gate. All strict inequalities
are retained. A source-to-symbol injection over the algebraic closure of
C(x,z) bounds the entire parameter-space dimension by B*ab under its
rank hypothesis. This is an ordinary-map argument; singular maps are
outside it.

Although A(a,b) need not have full permutation symmetry, the gate formulas
are symmetric in x,y and in a,b. Testing the three cyclic orderings
therefore tests all six permutations for these necessary conditions.
The finite exclusion does not assume arbitrary target permutations are
realized by source automorphisms.

## Complete finite enumeration and replay

For sorted l<=h<=n, all leg dimensions fit exactly when hn<=N.
Consequently 1<=l<=h<=floor(sqrt(N)) and h<=n<=floor(N/h).
At fixed l,h, strict improvement begins at

    n=max(h, floor([3(a+b)-2]^4/(216lh))+1).

These are finite exact integer intervals. The source loops enumerate
every allowed a,b; a>=10 already gives N>=1900 and b>=26 gives N>=1404.
All82 source formats are retained, including those with no improving
target. Every accepted exclusion records its orientation, rank lift,
rank threshold and, where needed, symbol-rank and dimension caps.

The tests independently scan the full unpruned target intervals and
filter by the exact score inequality. They compare every shape against
the exported inventory, reconstruct all2110 exclusion witnesses from
the theorem formulas, reject a corrupted lift bound for each witness,
and test all permutations of the three survivors. Pins and package
hashes authenticate the adopted sources and evidence. These checks do
not supply independent mathematical review of the imported proofs.

With root requirements.txt installed, from the repository root:

```sh
python research/ai/2026-10-23-unbalanced-rectangular-frontier/verify.py --output results/unbalanced-rectangular-frontier-2026-10-23/frontier.json
python -m unittest discover -s tests -p test_unbalanced_rectangular_frontier.py -v
python -m unittest discover -s tests -v
python tools/replay.py
```

The next questions are actual maps for the three A(8,9) formats or a
stronger obstruction valid there. In particular the rank-seven symbol
case is outside the adopted linear-annihilator hypothesis:35 is not
less than34. Increasing the rank parameter without a new theorem is
invalid. This screen leaves a=1, N>1377, rectangular direct sums, source
powers and general singular degenerations outside its scope. Every
historical report and both archived research directories are unchanged.
