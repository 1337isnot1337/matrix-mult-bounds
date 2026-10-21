# Local audit of arXiv:2610.13971v1

October 21, 2026. Independent AI reconstruction, unreviewed.

The preprint [Tensor Degenerations for Matrix Multiplication](https://arxiv.org/html/2610.13971v1), attributed there to Zhi-Wei Sun, claims a border-rank-2048 construction of M32 and stronger bounds. This package checks several of its finite local maps. It **does not reconstruct the full M32 coefficient tensor**, accept its exponent claims, or provide a new exponent bound.

## A concrete error in the printed scalar maps

Section 5 and Appendix A.4 set the central X scalar to 1/128 while leaving the nonzero X satellite scalars equal to 1. For a fully retained satellite triple, Definition 2.4 then gives coefficients

    A_i: 1/128,  B_i: 1,  C_i: 1.

They are not all 1/128, contrary to the subsequent assertion. Reconstructing the chart sum from these literal coefficients fails 128 of its 256 comparisons. Two small witnesses are:

| Chart (rho,beta) | Literal coefficient | Claimed coefficient |
| --- | ---: | ---: |
| (0,0) | 3239/64 | 1 |
| (0,3) | 127/64 | 0 |

Scaling each nonzero X satellite entry by 1/128 repairs all 256 chart identities. This is a repairable local normalization omission, not a proof that every corrected global construction is impossible. The result file retains both the literal and repaired computations and every mismatch.

## Local identities that pass

The sparse Laurent expander builds the source monomials and substitutes the printed maps using exact rational coefficients. The checked constant tensors are generated separately from the formulas being expanded.

| Source map | Nonzero constant terms | Other nonzero degrees | Result |
| --- | ---: | --- | --- |
| Canonical four-term active family, (7.3) | 6 | 1 | Exact stated remainder |
| Source-resolved four-term lift, (9.4) | 5 | 1,2 | Correct leading tensor |
| Singular C3 compiler, Section 6.3 | 9 | 1,4 | Correct arrow plus endpoint |
| Five-empty C3 module, Section 6.5 | 54 | 3,6 | Correct 45 shared, 8 regular, and 1 cubic terms |

Every expansion has zero negative Laurent coefficients. The five-empty module has 62 nonzero degree-three coefficients and eight degree-six coefficients.

For each of the four generic exceptional blocks, the code reconstructs K from the declared direct sum of CW tensors and the printed barred covector. It verifies the endpoint identity and all three zero pairings over Q. The clean dimensions are (7,6), (8,7), (7,6), and (8,7), as stated in the source. The result file prints the reconstructed dense maps so their interpretation is reviewable. The separate characteristic-three endpoint matrices are not covered by this package.

The crossed five-empty matrices M_delta are reconstructed from B, D, and the five stated packet characters. All 256 representation identities M_a M_b=M_(a+b) hold over Q.

## Missing global certification

These identities establish only the audited local algebra. A complete finite bound still requires three actual side maps whose contraction has M32 as its first nonzero coefficient. The incidence count and several Fourier identities do not themselves supply those maps.

One point requiring an explicit realization is equation (8.3). Its term pairing the Y absolute character beta with q+r pairs beta with the Z relative coordinate s on the zero-displacement locus. That is a cross-side coupling. Its one-bit sign table in (beta,s) has rank two:

    [[1,1],[1,-1]].

Consequently that phase is not the product of a function of beta and a function of s. A source-provided coupling could realize it, but the displayed scalar phase identity alone does not establish that realization. This observation is a missing-certificate check; it is not an impossibility theorem for every source-resolved assembly.

### Why the fixed zero-fibre tensor cannot supply the global bridge

There is an elementary obstruction to first forming the literal fixed-row
zero-defect tensor of Section 4 and then applying a degeneration to its
sixteen-fold direct sum. This statement has narrower scope than the
preprint's proposed enriched construction.

In characteristic different from two, the fixed tensor factors as

    T_zero = group_tensor(H4) tensor M2 = D16 tensor M2.

The four-bit equation is the group relation q+r+s=0, independently of the
three central-bit equations defining M2. Walsh inversion identifies the H4
group tensor with D16. Hence

    D16 tensor T_zero = D256 tensor M2.

Both this tensor and M32 have format (1024,1024,1024), and both are concise
on every leg.

For a tensor T define its centroid as the vector space of triples of
endomorphisms (A,B,C) satisfying

    (A tensor I tensor I)T = (I tensor B tensor I)T
                          = (I tensor I tensor C)T.

It is the kernel of a linear map whose entries are linear in T. Its
dimension is invariant under invertible changes of basis and cannot
decrease under a same-format degeneration by such changes: at a limit,
matrix rank cannot increase, so kernel dimension cannot decrease.

The tensor D256 tensor M2 has at least 256 independent centroid elements,
obtained by multiplying the three factors of each direct-sum block by its
own common scalar. In contrast, the centroid of Mn is one-dimensional.
To see this using the trilinear form tr(XYZ), the equality of the X and Y
actions gives

    A(X)Y = X B(Y).

Setting X or Y to the identity shows A(X)=XH and B(Y)=HY for one matrix H.
Equality with the Z action gives both C(Z)=HZ and C(Z)=ZH. Thus H is
central in the full matrix algebra, hence scalar. This proves the claimed
centroid dimension in every characteristic.

It follows that M32 cannot be a same-format GL degeneration of
D16 tensor T_zero, since 1<256. The conclusion also covers arbitrary
square side maps in a Laurent degeneration with a concise M32 limit:
concision forces each side map to be invertible over the Laurent-series
field. A generically deficient side map could not have a full-rank
flattening in its leading coefficient.

This rules out the collapsed fixed-zero-fibre bridge only. It explains
why an enriched character-resolved coefficient tensor and its actual
three side maps are essential. It does **not** prove that every enriched
source-resolved construction in the preprint is impossible.

## Reproduction and attribution

```sh
python research/ai/2026-10-21-sun-local-audit/verify.py --output /tmp/sun-local-audit.json
python -m unittest discover -s tests -p test_sun_local_audit.py -v
```

Only the Python standard library is required. The external mathematical data and local constructions are from the cited preprint. The coefficient expansion, local normalization diagnosis, and independent exact replay are this repository's audit work. No historical priority, external peer review, or formal proof verification is claimed.

The inspected HTML snapshot has SHA256
`9c811f797344442cabe78f3b793ed74e0d986274567ec77e3ef1e23f8565171b`.

## Follow-up: a packetwise lifting obstruction

The [packet audit](packet_lift.md) reconstructs each printed generic
layer-one packet contribution on a 4-by-4-by-4 target subspace. It is
exactly one sixteenth of M2, including both representatives of every
chart. A directly assembled Koszul map has rank 32, greater than the
rank-30 ceiling for that packet's stated border cost five. Thus those
individual printed summands cannot each be supplied by the assigned C3
or D4 source packet.

This excludes a packet-by-packet lift preserving the printed contributions.
It does not exclude constructions that mix contributions or cancel
negative Laurent coefficients across different packets. The exact replay
covers 1,536 chart coefficients and also diagnoses the narrower additive
linear phase assignment. A straightforward Strassen replacement would
raise the recorded budget to 2512 before the other unresolved gluing
conditions are met; this bookkeeping is not a construction.
