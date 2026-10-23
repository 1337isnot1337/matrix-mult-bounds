# Primitive supporting degrees and exact inner ranks

The [written unreviewed proof](proof.md) counts the bounded-degree
polynomial kernels of the two full-output coefficient maps. If r is
strictly below both scalar Hankel format sizes, their ranks are

    rho=ar+(b-r)min(epsilon_z,a),
    sigma=br+(a-r)min(epsilon_x,b).

Here epsilon_x and epsilon_z are the primitive degrees of the homogeneous
supporting form in each coefficient variable. This forces a constant
length-r scheme whenever

    rank M_F < ab*r+min(a(a-r),b(b-r)).

The boundary is sharp for every balanced a=b=n and every 2<=r<n. This
extends the preceding [kernel-descent strip](../2026-10-23-hankel-equality/README.md),
whose coefficient-map helpers and source credits remain pinned. The new
proof uses its field-intersection step and the prior elementary Hankel
kernel description; no pencil index or bundle-splitting theorem is added.
If all f_k have one fixed nonzero short polynomial factor in z, the full
slice rank is exactly a*sigma; the symmetric x-factor chart has rank b*rho.
The proof gives the literal Kronecker factors, with no converse factorization
assumed for arbitrary one-variable supporting forms.

Twenty-four exact controls cover fifteen balanced sharpness cases, seven
unbalanced or higher-degree cases, and two cases varying in both variables.
The verifier reconstructs the supporting form from the literal recurrence
matrix and computes its primitive degrees after clearing denominators and
removing common factors. Both inner ranks and full source ranks are computed
independently of their predicted formulas. The tests separately count kernel
dimensions at input lengths below, equal to, and above the primitive degree.

```sh
python research/ai/2026-10-23-hankel-annihilator-degree/verify.py --output results/hankel-annihilator-degree-2026-10-23/controls.json
python -m unittest discover -s tests -p test_hankel_annihilator_degree.py -v
```

This remains a pointwise source-slice constraint, with no proved constancy
over matrix parameters. At A9 and r=8 the strip is still nine units wide.
No target construction or exclusion, independent review, formalization,
historical novelty, or smaller exponent is claimed.

The [additive question](additive_question.md) separates an unproved
two-variable inequality from a written boundary-family rank calculation
at r=n-1. A forty-case recurrence pilot found no violation; its declared
scope and compact records are separate from the theorem. Replay it with
`python research/ai/2026-10-23-hankel-annihilator-degree/additive_pilot.py`.
