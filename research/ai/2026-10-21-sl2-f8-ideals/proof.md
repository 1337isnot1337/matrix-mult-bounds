# Subgroup-ideal cuts for SL(2,F8)

October 21, 2026. AI-SL2-F8-IDEALS-020. Written proof, unreviewed.
No improving degeneration or smaller arithmetic exponent is constructed.

## Imported lemma and attribution

This applies the concurrent worker's subgroup-averaging lemma,
AI-SUBGROUP-IDEAL-027, from commit
`b6f01fb781d64589e8681f5bfbff8750291daaf6`. Its exact source text is pinned
by hash in `import.json` and preserved in
[the imported proof](imported/subgroup_ideal_proof.md). The
[original source](https://github.com/1337isnot1337/matrix-mult-bounds/blob/b6f01fb781d64589e8681f5bfbff8750291daaf6/research/ai/2026-10-21-subgroup-ideal/proof.md)
retains its attribution and written, unreviewed status. This session does
not claim its discovery or independent review.

For a finite group G and subgroup H, put

```
e_H = (1/|H|)*sum_(h in H) h,      I_H = C[G]*e_H*C[G].
```

If one vertex family contains a full left coset gH in the injective-pair-map
and strict-vertex-potential construction, the product of the other two
family sizes is at most dim I_H. The imported proof averages the potentials
on that coset, then restricts its middle index to the trivial H-component.
The resulting output lies in I_H; flattening rank cannot increase in the
limit. It applies to every conjugate and coset of H. The coordinate and
potential hypotheses are essential; it is not a general tensor-degeneration
obstruction.

## New exact projection certificates

Use the exactly enumerated504-element SL(2,F8) group from the
[semisimple source package](../2026-10-21-semisimple-koszul/proof.md).
For each selected H, export a central rational group-algebra element z
satisfying

```
z*z = z,                  z*sum_(h in H) h = sum_(h in H) h. (1)
```

Then I_H lies in C[G]z. Left multiplication by z is idempotent, so its
rank equals its trace. On the regular representation the trace is504
times the identity coefficient z_1. Therefore

```
dim I_H <= 504*z_1.                                        (2)
```

Only this upper bound is needed. No equality or minimality of the chosen
central projection is claimed.

The three projections give:

| Subgroup | Order | Identity coefficient z_1 | Certified upper bound |
| --- | ---: | ---: | ---: |
| additive upper-unipotent subgroup | 8 | 77/126 | 308 |
| selected cyclic subgroup | 9 | 55/63 | 440 |
| its selected dihedral normalizer | 18 | 61/126 | 244 |

The full nine-entry class coefficient vectors are in
`results/sl2-f8-ideals-2026-10-21/projections.json`.
Discovery sums suitable rational central projectors from the existing exact
source certificate. Acceptance does not trust a character-table assertion
or a modular rank upper bound. It enumerates the nine conjugacy classes,
computes their integer class-product constants, clears the coefficient
denominators and directly verifies both identities in(1). It checks the
idempotent identity in the class algebra and the subgroup-containment
identity at all504 group elements. Subgroup closure is also checked.
The integer trace then proves(2) over C.

## Consequences for the selected target and the full frontier

For M(18,18,25), the other-pair products are450,450,324.
Every complete coset of either the order-eight or order-eighteen subgroup
is therefore forbidden in every vertex family. A full order-nine coset is
forbidden in either size-eighteen family; this particular bound does not
forbid it in the size-twenty-five family, whose other-pair product is324.

Every one of the16 remaining general SL(2,F8) target formats from the
full-space frontier has other-pair products at least324. Thus complete
unipotent-eight and dihedral-eighteen cosets are forbidden on every leg
of all those coordinate/potential targets. General tensor degenerations
and coordinate candidates without these full cosets remain open.

In particular, the first fixed-full-D18 subgroup pilot is now excluded
by a written proof. Its historical180-second timeout remains an experiment
outcome; it is not used as a nonexistence certificate. The new proof uses
the imported lemma and the exact244-dimensional projection upper bound.
Do not rerun that full-subgroup frame.

The independent tests reproduce the projections and reject corrupted
coefficients, a false rank, a non-subgroup and an overclaimed nine-cycle
cut. The zero central projection is idempotent but fails containment,
which the verifier rejects. The identity projection gives the safe
trivial upper bound504 and no forbidden-coset assertion for the selected
format. The imported proof's byte hash is checked separately.

## Reproduction

From the repository root with its maintained requirements:

```sh
python research/ai/2026-10-21-sl2-f8-ideals/sl2_f8_ideal_certificate.py --output results/local/sl2-f8-ideal-projections.json
python -m unittest discover -s tests -p test_sl2_f8_ideals.py -v
```

The projection verifier uses exact rational and integer arithmetic and the
finite multiplication table. Source-projector discovery reuses the existing
rational center derivation. No SAT, LP or floating acceptance step is needed.
