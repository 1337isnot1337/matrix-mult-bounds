# Abelian normal fibers and a three-slice Koszul obstruction

October 20, 2026. AI-GROUP-NORMAL-KOSZUL-011; written proof, unreviewed.
EXP-GROUP-NORMAL-COUNTS-012 is an exact finite count screen. No improvement
of the arithmetic exponent is established.

## 1. The normal-coset bound

Work over C. Let H be a finite abelian normal subgroup of G, of order h.
Suppose S,T,U give a group-algebra matrix target through injective pair
maps s^-1 t, t^-1 u, u^-1 s and strict vertex potentials. For each coset
a in G/H put k_a=min(|S_a|,|T_a|,|U_a|), discard zero values, and define

```
D = sum_a k_a^2,                  z = number of a with k_a=1.
```

Then

```
3D-z <= 2h.                                                     (1)
```

The same bound holds after every independent right translation of the
three families. This gives a stronger normal-fiber necessary test than
product-of-largest-fiber cardinality alone.

This is an application of the classical three-slice commutator bound,
not a new general tensor-rank inequality. Strassen's 1983 work is
[Rank and optimal computation of generic tensors](https://www.sciencedirect.com/science/article/pii/002437958380041X).
For the Koszul-map formulation and attribution, see Landsberg and Ottaviani,
[New Lower Bounds for the Border Rank of Matrix Multiplication](https://theoryofcomputing.org/articles/v011a011/v011a011.pdf),
Theory of Computing 11 (2015), Sections 1-2. The needed special case is
proved directly below. No historical priority is claimed for this application.

## 2. Restriction to the abelian subgroup

Restrict every group-tensor leg to the basis H. A pair label s^-1 t lies
in H precisely when s and t lie in the same coset of H. An intended term
whose three pair labels lie in H therefore uses vertices from a single
common coset. The restricted coordinate degeneration gives

```
C[H] multiplication >= direct_sum_a M(|S_a|,|T_a|,|U_a|).
```

Unintended terms remaining in this restriction still have strictly positive
weight. Restricting vertex sets to k_a points in each family gives the
square subtarget A = direct_sum_a M(k_a,k_a,k_a), the multiplication tensor
of the algebra direct_sum_a Mat_(k_a). Its algebra dimension is D.

The complex Fourier transform identifies C[H] with C^h. Its multiplication
has tensor rank h, so the border rank of A is at most h if the proposed
degeneration exists. This uses that H is finite abelian and the field is C.
It is not a claim about the rank of a nonabelian group algebra.

Independent right translations preserve the group construction: on a pair
leg they act by x -> g_S^-1 x g_T, and the three such transformations
cancel in the trace product. Since H is normal, they permute the quotient
cosets independently. This justifies the additional count-pattern alignments.

## 3. Explicit three-slice rank

Choose three first-leg slices of A: its unit I, blockwise left multiplication
by X=diag(0,...,k-1), and blockwise left multiplication by the k-cycle Y.
On a block Mat_k, the commutator is left multiplication by [X,Y]. For k>=2,
the latter is a weighted cycle with k-1 edge weights 1 and one weight -(k-1),
and is invertible. For k=1 its commutator is zero. Thus, on the D-dimensional
algebra, rank([L_X,L_Y])=D-z.

The first Koszul map on these three slices is the 3D-by-3D matrix

```
K(v0,v1,v2) = (-L_X v0+v1, -L_Y v0+v2,
               -L_Y v1+L_X v2).
```

Its kernel identifies with ker([L_X,L_Y]): the first two equations give
v1=L_X v0 and v2=L_Y v0. Therefore rank K=2D+(D-z)=3D-z.
A rank-one tensor contributes rank at most two to this Koszul map, because
wedging a vector on a three-dimensional space has rank two. Matrix rank
cannot increase in a degeneration, since bounded rank is defined by minors.
Border rank at most h would imply rank K<=2h, proving (1).

If D=1 and all slices are dependent, the same matrix construction remains
valid and has rank two. No independence assumption on I,X,Y is used in the
rank-one bound. `certificate.py` builds the integer matrices and checks their
ranks modulo 101; the displayed commutator proof supplies their exact
characteristic-zero ranks. The selected block sizes are all below 101.

## 4. The entire size-nineteen, maximum-three F8 fiber class is excluded

Take |H|=64 and quotient C7, as in F8^2:C7. Suppose all three families have
size nineteen and every normal fiber has size at most three. A family must
have five fibers of size three and two of size two (type B), or six fibers
of size three and one of size one (type A).

Independently translate each family so a deficient fiber lies at the
identity quotient. If all are type B, at most four quotient positions are
deficient in the pointwise minimum: the common position and at most one
additional position from each family. Every fiber still has at least two
points, so the square subtarget has dimension at least

```
4*2^2 + 3*3^2 = 43.
```

It has no scalar blocks. Its three-slice rank is at least 129, exceeding
2h=128. If exactly j>=1 families are type A, only 3-j extra deficient
positions remain, and the shared position has size one. The lower bounds
on D are 40+5j, giving ranks at least 134,149,164 for j=1,2,3. Thus every
case fails (1).

This argument makes no assumption about affine fiber directions, offsets,
or which scalar labels held the short fibers. In particular it excludes
the entire earlier variable-plane search ansatz. It does not exclude
other size patterns or a general complex degeneration to M(19,19,19).
The checker also covers all 28^3=21,952 ordered size-pattern triples under
the stated maximum-three assumption and agrees with the four analytic bounds.

## 5. A size-only upper bound of four on F2^6 normal fibers

For completeness, every size-nineteen construction in this group must have
all normal fibers of size at most four. Each other family has a three-point
fiber, since ceil(19/7)=3. Choose three-point subsets A,B of two such fibers.
Normal-fiber unique sums are necessary by the earlier abelian-coset lemma.

Over F2, the difference set of any three-point set is a two-dimensional
linear plane. Injectivity of A+B makes these two planes disjoint, so
their sum W has dimension four and

```
(A+B)-(A+B)=W.
```

A third fiber C can meet each coset of W in at most one point; otherwise
its difference produces a collision in A+B+C. There are four such cosets
in F2^6, hence |C|<=4. This applies to every fiber of every family.
Combined with Section 4, at least one family must have a four-point fiber.

## 6. Other scoped consequences

- If H has order 64 and index three and all three target sizes are twelve,
  the largest-fiber product bound forces every fiber size to equal four.
  The square subtarget is three copies of M4: D=48, rank K=144>128.
  This excludes the whole stated coordinate-potential size-twelve class in
  F4^3:C3, including all affine bases and offsets considered earlier.
- If H has order 31 and index six and every fiber in each family has at
  least two points, there are six M2 subtargets: D=24 and rank K=72>62.
  Thus any proposed C31:C6 target (12,13,13) must have a fiber of size at
  most one. The constant two-point/three-point pilot violates this necessary
  condition regardless of directions or offsets.

These statements are construction obstructions; they do not improve omega.

## 7. Count patterns that remain open

If all F8 normal fibers have at least two points, Section 5 leaves entries
in {2,3,4} summing to nineteen. There are 266 patterns, or 38 classes under
cyclic rotation. `count_frontier.py` checks all 9,880 unordered triples of
these classes and all 49 relative cyclic alignments. For pointwise minimum
k>=2 the rank score is

```
84 + 15*|{k>=3}| + 21*|{k>=4}|.
```

Exactly 1,566 class triples are not excluded by this count test: 558 have
four-point fibers in two families, and 1,008 in all three. Directions,
offsets and positive potentials for them are unconstructed. These counts
do not concern patterns with zero- or one-point fibers. Passing the test
is only a necessary condition, not evidence of a degeneration.

## Reproduction

```sh
python research/ai/2026-10-20-normal-coset-koszul/certificate.py \
  --output results/local/normal-coset-koszul.json
python research/ai/2026-10-20-normal-coset-koszul/count_frontier.py \
  --output results/local/normal-coset-counts.json
python -m unittest discover -s tests -p test_normal_coset_koszul.py -v
```

Committed reports are in `results/normal-coset-koszul-2026-10-20/`. The code
uses only the standard library. The written reductions have no independent
review or formalization; a passing test does not change that status.
