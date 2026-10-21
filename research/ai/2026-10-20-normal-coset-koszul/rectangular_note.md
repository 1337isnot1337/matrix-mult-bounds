# Rectangular normal-coset slices exclude the full F8 size-nineteen target

October 20, 2026. AI-GROUP-F8-RECTANGULAR-013. Written proof, unreviewed.
No exponent improvement or general tensor-degeneration obstruction is claimed.

## Statement

Let G have an abelian normal subgroup H isomorphic to C2^6 and quotient C7.
No three subsets of G of sizes at least nineteen give a matrix target
through injective pair maps and strict vertex potentials. In particular,
the entire F8^2:C7 to M(19,19,19) construction class is excluded, including
four-point, one-point and empty fibers, variable directions and all offsets.

Restricting to nineteen vertices in each family suffices. The
[normal difference-space proof](research_note.md#5-a-size-only-upper-bound-of-four-on-f26-normal-fibers)
then caps every normal fiber at four. The remainder is a finite count
obstruction using a rectangular version of the same classical Koszul map.
General complex tensor degenerations, joint extraction and unequal targets
having a side below nineteen remain outside this theorem.

## 1. Rectangular three-slice rank

For a block M(a,b,c), use three a-by-b matrix slices, each acting on the
c independent columns. Put k=min(a,b).

If k>=2, embed the k-by-k identity, diagonal and cycle matrices used in
the earlier commutator proof. The resulting three-slice Koszul matrix has
rank 3kc: its embedded square part already has that rank, and 3kc is the
smaller row/column dimension after discarding the zero padding.

If k=1 and max(a,b)>=2, use two different elementary matrices and a zero
third slice. The corresponding 3-by-6 or 6-by-3 matrix has rank three,
repeated independently c times. If a=b=1, a single nonzero slice instead
gives rank 2c. A zero size gives a zero tensor. Thus the construction gives

```
R(a,b,c) = c * (3 min(a,b) - 1[a=b=1]).                       (2)
```

The three slices are chosen blockwise and then summed across cosets.
Their Koszul map is block diagonal after reordering, so the ranks add.
Since a rank-one tensor contributes at most two, the normal-subgroup
restriction of the group construction requires

```
sum_i R(a_i,b_i,c_i) <= 2|H| = 128.                          (3)
```

The analogous two bounds from the other choices of first tensor leg also
hold. Independent right translations give all cyclic shifts of the three
count arrays. This is still an application of the classical three-slice
Koszul/Strassen bound; it is not a new general rank inequality.
`certificate.py` explicitly builds these rectangular matrices, including
the size-one cases, and the tests check every nonzero size triple up to four.

## 2. An analytic exclusion when two families have no small fibers

Suppose a_i,b_i>=2 for all seven cosets. Each of these arrays sums to
nineteen and is bounded above by four. Therefore at least three entries
of each are at least three. Averaging over relative cyclic shifts puts
at least two such positions in their common set I.

Independently shifting the third array gives

```
sum_(i in I) c_i >= ceil(2*19/7) = 6.
```

Thus sum c_i min(a_i,b_i) >= 2*19+6=44, and the rank in (3) is at least
132, a contradiction. This excludes every candidate having all fibers at
least two in any two families, without a direction or offset assumption.
The finite square-only screen's 1,566 survivors are all subsumed by this
rectangular test.

## 3. Complete finite cover of the remaining count patterns

A seven-entry array in {0,1,2,3,4} summing to nineteen has 3,535 possible
values. None is fixed by a nontrivial cyclic shift, since 19 is not
divisible by seven. They form 505 cyclic classes. The verifier checks
coverage independently: it counts bounded compositions by a coefficient
recurrence and checks that the 505 disjoint rotation orbits contain exactly
that many arrays.

Call a pair of classes good if some relative cyclic shift gives

```
W(a,b) = sum_i (3 min(a_i,b_i) - 1[a_i=b_i=1]) >= 48.
```

For any third size-nineteen array c, averaging its cyclic shifts gives

```
average_s sum_i c_(i+s) (3 min(a_i,b_i)-1[a_i=b_i=1])
    = (19/7) W(a,b) >= 912/7 > 128.
```

Hence a good pair excludes every third class by (3). A repeated class is
always a good pair: align it with itself to get 57 minus its number of
one-point fibers, which is at least 54.

There are 33,735 bad distinct pairs. Of the 21,592,285 class triples modulo
family permutation and allowing repetition, 466,859 have all three pairs
bad. Every other triple is excluded by the averaging argument. All three
choices of first tensor leg are available, making the necessary score
symmetric in the three count families; sorting class indices loses no case.

For every bad triangle, a one-byte certificate specifies a first-leg choice
and two relative shifts for which the sum in (3) exceeds 128. The separate
Python checker rebuilds the graph and every triangle, decodes each byte and
computes the exact integer rank bound. It rejects missing, extra or invalid
bytes and any non-obstructing witness. Thus coverage of the exceptional
triangles is checked independently of the C++ discovery program.

## 4. Certificate format and provenance

`discovery/build_rectangular_cover.cpp` enumerated the classes and found
the alignment bytes. It is discovery code, and is not run by verification.
The binary stream has one byte for each bad triangle in lexicographic
order of its class indices i<j<k. Classes are ordered lexicographically by
their least cyclic rotation. Decode the byte as

```
byte = 49*leg + 7*shift_b + shift_c,
leg in {0,1,2}, shifts in {0,...,6}.
```

The leg scores are R(a,b,c), R(a,c,b) and R(b,c,a), respectively. Their
numerical values are the three cyclic first-leg bounds, since the first
two arguments of R are symmetric. The stream is 466,859 bytes. Its SHA256,
the full pair-score histogram and the checked rank histogram are in the
committed JSON replay report. A hash supplies integrity, while the Python
replay checks the mathematical inequalities and complete graph coverage.

Every size-nineteen fiber-count triple either has a good pair or belongs
to a verified bad triangle. Both cases violate (3). Together with the
four-point cap this proves the stated construction exclusion.

## 5. Balanced degree-sum consequence

For F8^2:C7 the existing source degrees are seven ones and nine sevens.
The ordinary 9/4 source gate costs 7+9*7^(9/4). Every balanced target
with side at most eighteen fails that gate, because

```
18^9 < 700^4,       78^4 < 7^9,       700 < 7+9*78 = 709.
```

Sides at least nineteen are excluded by the construction theorem. Thus no
balanced single target in this construction class passes the usual 9/4
source gate. Failure persists at smaller positive exponents by the same
ratio monotonicity used in the C29 note; sides at most seven already cost
no more than a single degree-seven source block. This is a negative result
for that source-cost route, not an improvement in omega.

## Reproduction

From the repository root with Python 3.10 or later:

```sh
python research/ai/2026-10-20-normal-coset-koszul/rectangular_certificate.py \
  --witness results/normal-coset-koszul-2026-10-20/rectangular-cover.bin \
  --output results/local/f8-rectangular-cover.json
python -m unittest discover -s tests -p test_normal_coset_koszul.py -v
```

Verification needs only the standard library. The discovery program can be
rebuilt with a C++17 compiler and passed a new output path; the resulting
stream must still pass Python replay. No independent review or formalization
is asserted. The exponent-improvement goal remains incomplete.
