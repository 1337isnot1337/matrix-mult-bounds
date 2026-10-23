# Independent aggregation families: research question

## Question and acceptance criterion

Can a balanced family of tripartitions of nine coordinates contain more
than 14 products while every off-diagonal mixed triple has a coordinate
omitted from exactly two factors? An exact list of 15 such tripartitions
would give 15 independent products of n^3 by n^3 matrices with at most
(n+1)^9 scalar multiplications, over characteristic-zero fields.

A secondary question is whether a conflict-free balanced family contains
more than 28 products on nine coordinates, or 105 on twelve coordinates.
The centered, padded, weighted construction would then give the corresponding
number of independent products with cost (n+2)^(3N). Corrections must be
counted explicitly if the cheaper centered construction is used instead.

These are finite positive-construction questions. A search that fails to
find a larger family proves no upper bound. A family improving these
small aggregation counts does not establish omega < 9/4. A contribution
to the present exponent target would require a further cost inequality or
a new restriction that remains to be supplied.

## Mathematical criterion

Write t=(U_t,V_t,W_t), with the three sets a partition of {0,...,3N-1}
into N-element sets. Let eta_r(i,j,k) count membership of coordinate r in
U_i,V_j,W_k. For correction-free centering, require that each (i,j,k)
other than i=j=k has some r with eta_r=2. For ordinary conflict freedom,
require that eta_r=1 for every r implies i=j=k. These are different tests.
Acceptance uses integer masks and complete enumeration of all ordered
mixed triples. A separate verifier must check the serialized witness.

## Sources and relation to prior repository work

Edgar Solomonik and Markus Blaeser, *Simultaneous Matrix Multiplication by
Tensor Contraction Aggregation*, arXiv:2610.26563v2, revised 2026-10-22:
https://arxiv.org/html/2610.26563v2 . Definition 7 gives conflict freedom;
Sections 5 and 8 give centering, correction costs, and the attained
14-, 28-, and 105-product comparison constructions. These attained
counts are not claimed optimal. Source pins and ancillary checksums are
in sources.json. The aggregation mechanism is external prior work.

The local note ../2026-10-21-centered-orientations/README.md already uses
version 1 of this paper to build products sharing an input and studies
partial-transpose obstructions. This investigation instead varies the
independent-product tripartition family. It does not repeat or supersede
the shared-input obstruction.

## Work plan and evidence status

Implement an independent exact family verifier, then a reproducible
local search seeded by the cited ancillary witnesses. Commit a successful
new witness, proof of its uniform rank consequence, and exact checks. If
search finds no improvement, report only the actual finite coverage and
retain the external baseline attribution. No new mathematical claim is
established by this initial question record.

## Recorded outcome

The secondary nine-coordinate question has a positive answer: the
exported 29-product family and proof.md establish its exact uniform rank
identity and strict cost-per-output improvement over the external 28
comparison. The first correction-free 15 question remains open. No
smaller matrix multiplication exponent follows.

The twelve-coordinate secondary question also has a positive answer:
`witness_106.json` gives 106 products. Its corrected cost per output
beats the credited 105-product comparison for every integer n>=7.
The unsuccessful 30-product and correction-free 39 searches are recorded
separately as bounded experiments, not impossibility proofs.
