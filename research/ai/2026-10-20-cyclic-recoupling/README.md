# Exact recoupling of the cyclic convolution source

October 20, 2026. AI-derived finite coefficient calculations and searches,
unreviewed. No new degeneration with a profile gain or smaller exponent is
established. This investigates actual coordinate mixing in the cyclic source
A_a from [the finite target](../2026-10-20-koszul/cyclic_finite_target.md).
It differs from the earlier two-factor, same-orientation product searches.

## Coefficients and block structure

Put D=a-1. An invertible diagonal scaling and reversal puts C(a,a) in the
SL2-invariant form with coefficient

    (-1)^(i+j) binom(D,i) binom(D,j)

at (i,j,2D-i-j). The raising operator on degree-d monomials sends e_i to
 i e_(i-1); the three contributions cancel since their index sum is 2D.
The lowering operator gives the analogous identity. These are standard
binary-form actions, not a new representation-theoretic construction.

Each cyclic-source leg is V_D tensor V_D tensor V_(2D), where V_d=Sym^d(C^2).
First couple the two short factors at order i, then couple their V_(2D-2i)
component to V_(2D) at order j. This gives V_(4D-2i-2j). The maintained
rational `equivariant_basis` in the earlier Clebsch--Gordan package supplies
both maps. Exact inverses are checked separately in every weight space.

`coefficients.py` applies the three inverse maps using sparse integer
arithmetic and exact rational denominators. It recomputes every coefficient;
no floating zero test or dimension-only block recognition is used. At a=4
there are 16 path labels on each leg, 2539 nonzero path triples and 91620
nonzero scalar coefficients. The full grouped leg has dimension 112.

Grouping equal representation degrees produces an actual factorization

    block_(L,M,N) = B_(L,M,N) tensor I_(L,M,N),

where B is the multiplicity tensor and I is the scalar invariant tensor.
The code checks this factorization coefficient by coefficient; it does not
infer it solely from the one-dimensional invariant space. For a=4 the
multiplicities at degrees 0,2,...,12 are 1,2,3,4,3,2,1. There are 175 nonzero
degree triples. Their exact B tensors and scalar factors are retained.

## Certified scoring rules

Every nonzero scalar invariant block has tight support: the three monomial
indices sum to a fixed integer, and the index maps on each leg are injective.
For dimensions (l,m,n), squared coefficient masses proportional to

    coefficient_(i,j,k)^2 /
      [binom(l-1,i) binom(m-1,j) binom(n-1,k)]

have exactly uniform marginals. This is checked over Q for every block.
Strassen's scalar tight-support theorem therefore gives asymptotic subrank
min(l,m,n). The primary statement used is Theorem 1.1.31, with tightness as
in Definition 1.1.27, in Christandl--Vrana--Zuiddam,
[arXiv:1609.07476v2](https://arxiv.org/abs/1609.07476v2), September 10, 2019,
printed pages 11-12. The theorem concerns scalar tensors; no weighted
block-extraction theorem is being assumed.

At t=3/4 this supplies the scalar profile lower bound min(l,m,n)^(4/3).
Saturated blocks may instead use a stronger convolution profile P_* after
an exact axis/reversal/diagonal-factor isomorphism check. For a grouped block,
we multiply by a certified profile lower bound for B: its largest coordinate
matrix-slice rank, or a verified full convolution isomorphism when stronger.
Unknown multiplicity tensors are not assigned a guessed value.

The outer support search uses integer input-label weights x,y and sets
z_k=-min_(i,j in support k)(x_i+y_j). Every retained coefficient has weight
zero and all other coefficients have nonnegative weight. An output-label
subset is then retained. These are actual coefficient degenerations, but a
retained support alone does not imply a profile gain.

The recursive scorer uses only independent direct sums and sectors disjoint
on two legs, exactly as in the earlier package. On profiles, a shared-sector
sum adds the child bounds; an independent direct sum uses
(sum child^(3/4))^(4/3). Integer square/fourth/cube-root intervals at scale
2^80 enclose every operation. The saved best support includes its weights
and recursive expression. Acceptance and negative score comparisons use
exact interval bounds; displayed decimals are descriptive.

## Completed coverage and active check

All full coefficient tensors and grouped factorizations at a=2,3,4 have
been generated and checked. The scalar-block counts are 36,429,2539, and the
corresponding nonzero coefficient counts are 239,7897,91620. The grouped
block counts are 15,65,175.

For each source the sampled run uses 36 ordered pairs of fixed linear path
weights, followed by 2964 seeded input pairs with entries in [-7,7]. Each
pair tests all output labels together and seven seeded nonempty output
subsets. Seeds are 202610204+a for path labels and 202610214+a for grouped
degrees. Reports give distinct supports, which can overlap between modes.

| a | Sampled path supports | Sampled grouped supports | Best grouped ratio to P_*(a,a)^3 |
|---|---:|---:|---:|
| 2 | 3108 | 483 | 0.660000 |
| 3 | 23110 | 8546 | 0.444578 |
| 4 | 23966 | 18771 | 0.359207 |

These completed runs have no profile violation or unresolved interval
comparison. A separate enumeration covers every binary input weight vector
with minimum zero and every nonempty output-label subset in the grouped
model. The a=2 and a=3 runs are complete, at 253 and 24156 distinct supports.
The a=4 run has enumerated 1797505 supports; scoring is still running at
this checkpoint. Its completed result must be recorded before claiming
negative coverage for that entire run.

These finite negatives do not exclude other weights, basis changes within
multiplicity spaces, different partitions, higher tensor powers or stronger
proved multiplicity values. Even a matching-profile violation would need
an implication for every relevant actual character before improving omega.
The concrete A_4 to M(10,10,11) degeneration remains unconstructed.

## Reproduction and attribution

Use root requirements.txt. This package adds no dependency. For example:

```sh
python research/ai/2026-10-20-cyclic-recoupling/coefficients.py --a 4 --output-directory results/local/cyclic-recoupling
python research/ai/2026-10-20-cyclic-recoupling/search.py --input results/local/cyclic-recoupling/grouped-a4.json.gz --mode grouped-binary --output results/local/cyclic-recoupling/binary-a4.json
python -m unittest discover -s tests -p test_cyclic_recoupling.py -v
```

Other modes are `scalar-sampled` on the coefficient file and
`grouped-sampled` on the grouped file. Sampled modes default to 3000 input
pairs. The exhaustive a=4 binary run takes several minutes. Regression tests
recompute the full exact coefficient and factorization data and replay every
saved best witness, while only the smallest full binary search is in the
regression suite.

The rational CG basis, convolution recognition, exact profile, component
partitioning and integer root enclosures are reused from the concurrent
product worker's maintained package, present at main `529b27d`. The cyclic
coefficient calculation, multiplicity factorization, adapted search and
reports are local work. No external source code was copied and no historical
priority, independent mathematical review or formalization is claimed.
