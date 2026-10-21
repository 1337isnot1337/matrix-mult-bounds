# Quantum recoupling with a varying parameter

Owner: product-filtration worker, research/quantum-recoupling-20261020.
Base: main ea72ec4, after the all-power paired-source package merged in PR17.
The exponent goal remains active; no exponent below 9/4 is established.

Investigate Laurent changes of basis obtained from quantum Clebsch--Gordan
matrices near q=0 and roots of unity. These vary with the degeneration
parameter and can coalesce. This differs from assigning scalar weights
to irreducibles in a fixed classical recoupling basis.

Required output: a complete coefficient degeneration, with a quantified
spectral implication if it improves the endpoint. A basis determinant
zero, finite-field fit, or necessary-test survivor is insufficient.

Exact controls verify the generic source equivalence and the singularity
of selected small bases. The straightforward rowwise-regular cyclic map
at q=i has ranks 8,32,64 at a=2,3,4, respectively, over Q(i). Its limit
is an ordinary restriction. It cannot provide the open size-four target
M(10,10,11). General singular tensor-level normalizations remain open.

Next: inspect tensor-level cancellations and coupled flags, rather than
repeating regular initial maps. Keep finite-field discovery separate from
complex coefficient acceptance. Do not reopen the 239 improving paired
single-matrix targets already excluded through a=13.
