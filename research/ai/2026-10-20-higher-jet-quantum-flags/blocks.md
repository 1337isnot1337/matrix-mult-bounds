# A complete finite two-layer block family

Written proof with exact finite witnesses, unreviewed. This is a scoped
necessary-test calculation, not an improving tensor construction.

Use the sixteen blocks labelled (k,K) in the generic quantum local basis;
the third label indexes a weight basis within a block. At a primitive
sixth root let nu_c be the minimum Phi_6 valuation in block c. For each
choice of leading block b define the regular local curve

    P_b(q)=diag_on_block_c Phi_6(q)^(1[c!=b]-nu_c) M(q).

All sixteen choices are generically invertible. Exactly one block has
minimal order, and every other block enters one Phi order later. This
specifies a finite family of 256 ordered choices on the two regular legs.
The first-leg map may be arbitrary Laurent. The limit of the full tensor
in the 112-dimensional outputs is required to be regular.

For 131 pairs a leading-map minor of size 15+min(sB,sC) is nonzero, where
sB,sC are exact row-support upper bounds on the leading maps. The leading
saturation inequality gives slice ceiling

    112-(15+min(sB,sC))+min(sB,sC)=97.

For the other 125 pairs the left first-jet projected-source minor has size
15+sB+sC. Its core and outside-leading-row columns are disjoint. The
first-jet inequality gives the same ceiling

    112-(15+sB+sC)+sB+sC=97.

The saved minor sizes are conservative certificates; they do not purport
to determine the full complex ranks. At every nonzero approach rate the
jet minors are nonzero monomials, with exponents in the report. A common
nonconstant parameter arc, with any approach order and higher terms, is
therefore covered. The leading-only pairs allow arbitrary higher jets.
The jet pairs allow arbitrary opposite first jet once the specified left
jet occurs at the earliest nonconstant order.

All entries originate as exact rational functions over Q(q). Cyclotomic
valuations, residue units and derivatives are calculated before reducing
modulo p=786433. All residue denominators are checked. A nonzero minor in
this reduction proves nonvanishing over Q(zeta_6) and every complex
embedding. The report includes a primal minor for every pair.

These ceilings exclude the target's required slice rank 100 after a full
regular limit and any subsequent restriction or degeneration. Constant
or moving output projections before the limit are not included in this
256-pair conclusion; the distinct moving-surjection theorem only applies
to its specified globally normalized four-row leading flags. Multiple
leading blocks, larger gaps between blocks and changed block mixtures
remain open.
