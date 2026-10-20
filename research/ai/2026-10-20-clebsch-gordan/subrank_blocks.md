# Scalar tight-support certificates for the recoupling blocks

2026-10-20. Application of a standard external theorem; AI-derived written
argument and exact rational certificates, unreviewed and not Lean formalized.
No smaller matrix multiplication exponent is established.

## The valid scalar theorem

Strassen's theorem for a scalar 3-tensor with tight support states that its
asymptotic subrank is the exponential of the largest possible minimum marginal
entropy on that support. The version inspected here is
Christandl--Vrana--Zuiddam, arXiv:1609.07476v2, Definition 1.1.27 and
Theorem 1.1.31, printed pages 11--12.

A character dominates asymptotic subrank: from T^N restricting to a diagonal
tensor of size Q(T^N), lambda(T)^N>=Q(T^N); take N-th roots and the limit.
Thus tight support with simultaneous uniform marginals on dimensions a,b,c
gives

    lambda(T)>=min(a,b,c),  P(T)>=min(a,b,c)^(1/t).        (1)

This applies inside an individual scalar coefficient block. It does not
assume a weighted tensor-valued block-extraction theorem. Outer assembly
still uses only the proved matched-sector and full-direct-sum rules.

## Why the recoupling blocks qualify

Every nonzero coefficient c_(alpha,beta,gamma) has alpha+beta-gamma=q for
one fixed integer q. Subtract q on the first leg to get injective integer
weights summing to zero, proving tightness.

Give monomials in Sym^M(C^2) the SU2-invariant squared norm
1/binom(M,alpha). The block is an equivariant map
Sym^(a-1) x Sym^(b-1) -> Sym^(c-1). Its coefficient tensor is in the duals
of the input representations and the output representation. Its squared
coefficient masses in orthonormal bases are proportional to

    c_(alpha,beta,gamma)^2
      * binom(a-1,alpha) binom(b-1,beta) / binom(c-1,gamma).   (2)

The normalized tensor is invariant under compact diagonal SU2. Each reduced
operator commutes with its irreducible representation and is scalar by
Schur's lemma. Its diagonal gives a uniform marginal. This is a standard
representation-theoretic argument, not a historical novelty claim.

The exact verifier also checks (2) independently for each actual block,
exporting every rational probability and marginal. It rejects a non-tight
support or a nonuniform marginal. The finite certificates therefore do not
depend on guessing subrank from dimensions or solely on the written argument.

For the interior (5,5,5) block, (1) gives P>=5^(4/3) at t=3/4, about 8.55.
This improves both the earlier dot score 5 and its C(3,3) score 56/9.

## Completed stronger runs

The six-source binary report certifies all 101 actual block distributions.
It scores 24,536 outer supports with these stronger leaves, without a P_*
violation or ambiguous interval. A further run permits recursive label
deletions on every outer leg for (3,3,3,3) and (4,4,4,4), evaluating 1,350
and 58,266 recursive supports respectively. It still finds no violation.
At (4,4,4,4) the best source-normalized score rises from about 0.768922 to
0.791054. Decimals are descriptive; integer enclosures decide comparisons.

```sh
python research/ai/2026-10-20-clebsch-gordan/cg_search.py --subrank --strengthen --output /tmp/cg-subrank.json
python research/ai/2026-10-20-clebsch-gordan/cg_search.py --sources '3,3,3,3;4,4,4,4' --subrank --strengthen --all-restrictions --output /tmp/cg-restrictions.json
```

A strict profile violation would still need a complete uniform consequence
for actual character profiles before supporting a smaller exponent.
