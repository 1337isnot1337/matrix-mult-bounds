# Question and answer

Can the A4 source-space dimension caps be 64 below slice rank 92 and
68 below slice rank 96, continuing the supported-column staircase pattern?

No. Adding the full four-coordinate layer i=3,k=0 to two preceding
staircase spaces gives dimensions 68 and 72 with uniform ranks at most
91 and 95. A mixed row-and-column cover proves both bounds.

The corrected caps 68 and 72 are sharp. The credited order-ideal
reduction and eleven small coherent minors reduce their upper proofs
to short exhaustive layer-size case splits. Two additional odd integer
minors attain ranks 91 and 95 in the explicit spaces.

Claim IDs:

- AI-A4-RANK92-SHARP-LINEAR-SPACE-001.
- AI-A4-RANK96-SHARP-LINEAR-SPACE-001.

The status is written proof with exact finite certificates, without
independent external review or formalization. The package is restricted
to source-space theorems and does not alter any target-rank frontier.
