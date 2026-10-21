# A bounded attempt to reuse an external rank-76 decomposition

This package checks a possible starting point for the Q(6,4) construction
search. The external AlphaTensor algorithm for M(4,5,5) uses 76 scalar
multiplications. All 10,000 coefficients of its retained integer
factorization check exactly. This is an external algorithm, not a new
matrix multiplication result from this repository.

The proposed direct reuse does not work. An exhaustive finite-field
calculation shows that any four-dimensional complex subspace contains at
most eight of this particular decomposition's first-leg vectors. The
nine groups in the Q(6,4) evaluation grid could consequently contain at
most 72 of its 76 distinct vectors. The scope is a term-by-term assignment
of this fixed decomposition to that grid. Different decompositions,
non-termwise maps, and singular constructions remain open.

## External data and coefficient convention

The source is the integer algorithm attributed to Fawzi et al.,
*Discovering faster matrix multiplication algorithms with reinforcement
learning*, Nature (2022), in the
[Lille algorithm catalogue](https://fmm.univ-lille.fr/4x5x5.html).
The numerical arrays are extracted from Andrew Perminov's conversion at
[commit b4f756b](https://github.com/dronperminov/FastMatrixMultiplication/blob/b4f756b4153e5ac2c2f37d0a9e4dc3e895fdcabe/schemes/known/alpha_tensor/4x5x5_m76_ZT.json).
The full commit, path and hashes are in `sources.json`. The upstream MIT
notice is retained for the conversion data; this adds no project-wide
license. Formula strings from that file are neither retained nor executed.

The three arrays have shapes 76-by-20, 76-by-25 and 76-by-20. In zero-based
indices their contraction equals one exactly when

\[
(a,b,c)=(5i+j,\;5j+k,\;4k+i),
\qquad i<4,\quad j,k<5,
\]

and equals zero at all other coefficient positions. In particular, the
third array uses the transposed output convention. Permuting the tensor
legs and transposing the physical matrix coordinates gives M(5,4,5).

## Why a Q(6,4) evaluation grid has small groups

Let L=n+m-1. Interpolation at L distinct nodes gives the usual L-term
decomposition of degree-(n-1) by degree-(m-1) polynomial multiplication.
Using it on both convolution factors of Q(n,m) gives an L-by-L grid of
rank-one tensor terms. Write e_d(s) for the degree-dimension evaluation
vector and ell_s for the interpolation coefficient vector. A grid term
at nodes s and t has the three factors

\[
e_n(s)\otimes e_n(t),\qquad
e_m(s)\otimes\ell_t,\qquad
\ell_s\otimes e_m(t).
\]

For fixed t, the middle factors span a space of dimension at most m.
For fixed s, the last factors have the same bound. Applying arbitrary
linear maps to the three tensor legs preserves these inequalities.
For Q(6,4), L=9 and m=4, so its terms are covered by nine rank-at-most-four
groups on either long leg.

The proposed assignment sends the 25-dimensional leg of the external
M(5,4,5) target to the source's first leg. Either orientation
of the two 20-dimensional target legs includes the external u vectors
on a long leg. Rescaling rank-one terms and applying invertible target
bases do not change their flat-incidence counts.

## Exact finite-field screen

The C99 program enumerates all 1,282,975 four-subsets of the 76 u vectors
over F_101. For each independent subset, it reduces the four rows and
counts every input vector in their span. The completed run gives:

| Number of vectors in the flat | Independent four-subsets producing it |
|---:|---:|
| 4 | 992,290 |
| 5 | 245,373 |
| 6 | 39,567 |
| 7 | 2,181 |
| 8 | 676 |

These are counts of bases, not distinct flats. There are 1,280,087
independent four-subsets in total; every remaining four-subset is
dependent. The full vector span has dimension 20 over F_101. Thus any
span of dimension below four extends to one of the enumerated
four-dimensional spans. No smaller-dimensional case is omitted.

If nine integer vectors had complex rank at most four, every five-minor
would vanish as an integer and would still vanish modulo 101. They would
then lie in an enumerated four-dimensional finite-field span. The computed
maximum of eight excludes that possibility. Reducing modulo a prime can
introduce additional dependencies, which cannot invalidate this direction
of the argument.

The maximum is attained by a rational rank-four span. In zero-based
numbering, vectors 0, 5, 7 and 14 span exactly the eight vectors
0, 5, 7, 14, 28, 36, 47 and 52. The Python verifier checks this witness
over both the rationals and F_101, and checks a ninth vector has rank five.
The pigeonhole bound is 9 times 8 equals 72, below the required 76.

## Deleting an unchanged subset cannot repair the assignment

A possible way to fit the grid would be to delete some of the 76 terms
after a transformation preserving the matrix multiplication target. The
linear invariant

\[
L\!\left(\sum_r U_r\otimes V_r\otimes W_r\right)
=\sum_r\operatorname{tr}(U_rV_rW_r)
\]

is unchanged by the usual three physical changes of matrix basis.
The integer replay finds 52 individual values equal to one and 24 equal
to two. Every nonempty unchanged subset therefore has positive L and
cannot converge to zero under that stabilizer. This excludes deleting
such a subset by the stabilizer-nullcone method described by
[Dumitriu et al., arXiv:2610.13905v1, Section 2.3](https://arxiv.org/html/2610.13905v1#S2.SS3).
It does not exclude first changing the decomposition by flips or replacing
the terms with a different decomposition.

## Reproduction and limitations

The quick standard-library verifier reconstructs every tensor coefficient,
checks the data hash, verifies the stored enumeration counters, and tests
the exact extremal flat and a negative control. It does not rerun the
exhaustive count. Reproduce that count separately with a C99 compiler:

```sh
python research/ai/2026-10-21-external-grid-seed/verify.py --write-u /tmp/alpha-u.txt
cc -O3 -std=c99 research/ai/2026-10-21-external-grid-seed/four_flats.c -o /tmp/four-flats
/tmp/four-flats /tmp/alpha-u.txt
```

Compare the final JSON with
`results/external-grid-seed-2026-10-21/four-flats.json`.
The C enumeration and the mathematical scope argument were produced and
checked in the same generating session. This is a finite reproducible
screen with a written implication, not independent mathematical review.
It does not exclude Q(6,4) from degenerating to M(5,4,5), and it does not
exclude an algorithm changed by flips before assigning its terms. Other
alignments of the 25-dimensional target leg are not covered by this screen.
