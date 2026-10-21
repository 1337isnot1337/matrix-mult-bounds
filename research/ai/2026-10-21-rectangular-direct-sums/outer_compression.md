# Outer-compression obstruction and a finite-realization warning

October 21, 2026. Written proof, unreviewed. No exponent improvement.

## Imported theorem and scope

Mate Gyory, *Preserver problems and reflexivity problems on operator
algebras and on function algebras*, PhD thesis, Debrecen (2003), Theorem
2.1, printed page 10, PDF page 18, proves the following classification.
For a complex finite-dimensional Hilbert space, a linear endomorphism
of its full matrix algebra taking rank-k matrices to rank at most k
either has its entire image of rank at most k, or has the form AXB or
AX^t B. The continuity hypothesis in the general Hilbert-space statement
is automatic here. The proof on printed pages 12-13 reduces to Loewy's
rank-k theorem and the rank-one classification. This is external work.

Primary source, inspected October 21, 2026:
https://dea.lib.unideb.hu/bitstreams/29547839-340f-4f16-938a-f65b62dbf471/download
Original chapter publication: Gyory, Molnar and Semrl, *Linear rank and
corank preserving maps on B(H) and an application to *-semigroup
isomorphisms of operator ideals*, Linear Algebra Appl. 280 (1998),
253-266, https://doi.org/10.1016/S0024-3795(98)10045-9 .
The thesis, rather than the abstract alone, supplies the hypotheses used.

## Rectangular consequence

Let L: Mat_(p,q)(C) -> Mat_(m,n)(C) be linear, and assume L takes every
rank-at-most-k matrix to rank at most k. Its image dimension is at most

    max(k*(m+n-k), min(m,p)*min(n,q), min(m,q)*min(n,p)).       (1)

Here 1 <= k <= min(p,q,m,n). To prove this, choose N at least all four
sizes. Project Mat_N to its upper-left p-by-q block, apply L, and embed
its output into the upper-left m-by-n block. Projection cannot raise
rank, so the resulting endomorphism satisfies the imported theorem.

If its entire image has rank at most k, the dimension is bounded by the
rank-at-most-k determinantal variety, of dimension k(m+n-k). This last
formula follows directly on each maximal-rank chart by specifying a
k-by-k invertible block and the adjoining rows and columns; lower-rank
strata have smaller dimension. No bounded-rank linear-space theorem is
needed for this branch.

Otherwise restrict AXB (or AX^t B) back to the p-by-q input block and
project to the m-by-n output block. The resulting rectangular formula is
CXD (or CX^t D). Its linear-map rank is rank(C)*rank(D), giving the last
two terms of (1). This also justifies using the square theorem for a
rectangular map; no injectivity or surjectivity premise was inserted.

For p=32,q=33,k=2, the two outer flattenings of an A(8,10) source leg are
136-by-10 and 170-by-8. Their bounds in (1) are respectively 330 and 352,
both below 1056. Thus an injective target-leg map cannot take all rank-two
parameters into slices of outer-flattening rank at most two, in either
orientation. A generic rank-two condition suffices, since the minors
vanish on the irreducible rank-two variety and hence its closure.

This is a conditional obstruction to a compression stratum. It does NOT
show that all nonregular critical slices belong to such a stratum.

## Why crossed rank alone does not give a small finite realization

Consider A(8,10) and the single coefficient F_(0,8,0)=1, all others zero.
Its scalar 8-by-10 Hankel matrix has ones on p+q=8 and rank 8. Its crossed
coefficient matrix has the same eight independent entries (with i=s=0),
so has rank 8. Its original source matrix is a partial permutation with
8*8*10=640 nonzero entries: the remaining constraints are H=j and L=r.
Both outer coefficient flattenings have rank one.

But its scalar 9-by-9 moment Hankel matrix, using moments 0 through 16,
is the reverse identity and has rank 9. A representation f_k=u A^k v
with an eight-dimensional state space would factor that matrix through
the state space, which is impossible. Thus one finite crossed Hankel
rank does not justify assuming an eight-state realization. This example
also defeats a length-eight projective support representation: such a
representation factors the same catalecticant through a length-eight
algebra. The explicit finite control is in outer_compression.py.

## Remaining research question

A possible next classification would separate small finite-state strata
from low-outer-rank compression strata, including singular limits. This
is presently a question, not an established dichotomy. The regular-stratum
support-velocity argument also needs uniform local coefficient-fiber
bounds when arbitrary roots, amplitudes and Jordan partitions vary.
Neither missing step is counted as a target exclusion here.
