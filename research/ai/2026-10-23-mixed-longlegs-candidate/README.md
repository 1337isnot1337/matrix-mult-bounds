# Mixed-orientation candidate excluded by a geometric obstruction

## Current result: no degeneration from the stated source

The [global RNC proof](global_rnc_obstruction.md) excludes the source-target
degeneration below, even with independent target first identifications
and arbitrary poles, singular leading maps and mixing on all tensor legs.
It forces the source's moving rational normal quartic to have a smooth
limit, uses binary substitution symmetry to normalize the first map,
and applies the catalecticant contradiction120<130. All ordinary Koszul
screens below remain passing tests. This proof does not determine target
border rank or improve the matrix multiplication exponent.

The following geometric checkpoint and original rank census record the
steps leading to this exclusion. The new controls and source records are
separate files; the discovery tensor and earlier proofs retain their bytes.

## Geometric checkpoint

The [cactus-rank proof](cactus_rank.md) gives ordinary, smoothable and
cactus rank exactly 178 for the canonical target. It does not determine
border rank. The [catalecticant proof](catalecticant_chart.md) compares
source rank120 with target rank at least130 after every independent
invertible first identification. It excludes any degeneration whose
scalar-normalized first map has an invertible leading limit, allowing
arbitrary poles and mixing on the long maps. Singular leading first maps
were the remaining construction question at that checkpoint and are
now covered by the global proof above.

The exact controls are additive; the discovery input and prior rank
reports retain their bytes. The original validation manifest refers to
public checkpoint `79b23815c68cef6c013d4ba54ae37d4d068ae712`.

This package records the now-excluded proposed complex degeneration

\[
10\,\mathrm{Full}_{5,10}\ \dashrightarrow\
7\,\mathrm{Full}_{5,2}+10\,\mathrm{Full}_{5,3}
+4\,O_{3,3}+2\,O_{4,2}+6\,\mathrm{Mid}_{5,2}.
\]

Every sum shares the same canonical coefficient basis of the first
five-dimensional space. Both endpoints have format (5,100,140).
The target's symmetric formal operational score is strictly larger.

The candidate passes every ordinary Koszul degree on all three tensor
factors. The shared-first-leg profiles agree exactly. Higher-degree
literal controls and an all-degree source formula settle the B leg.
The output-leg source theorem proves the maximum possible C-leg rank
in every degree, so any target of this format passes that family.
The source also has maximal ranks for both symmetric-power families
and simultaneous uniform marginals. These are necessary tests. They
do not construct a degeneration.

The original discovery input is byte-frozen in discovery_input.json.
Later results belong in separate notes and result files. See proof.md for
the literal endpoints, score certificate, the scope of each screen, and
the current construction frontier and the excluded frozen question. The source proofs are
source_b_koszul.md and source_c_koszul.md. The earlier interpolation
windows and exterior-kernel controls are retained in
source_koszul_tails.md and shadow_note.md as independent evidence.
The whole-block allocation argument in copywise_dimensions.md proves
that a construction must go beyond assigning target blocks separately
to the ten source copies.

From the repository root:

    python research/ai/2026-10-23-mixed-longlegs-candidate/verify.py
    python research/ai/2026-10-23-mixed-longlegs-candidate/verify_higher.py
    python research/ai/2026-10-23-mixed-longlegs-candidate/verify_shadow.py
    python -m unittest discover -s tests -p 'test_mixed_longlegs_*.py' -v

The verifier needs only the Python standard library. It exports
results/mixed-longlegs-candidate-2026-10-23/verification.json and
degree_one_certificates.json. The latter gives independent incidence
forest rows and component kernel vectors for every degree-one block map.
The higher and shadow verifiers save separate reports in the same
results directory. The initial report's stated remaining-degree window
records that earlier checkpoint; the current all-degree conclusion is
the one above and in proof.md.

Evidence status: exact finite necessary-condition experiments and
written source-rank proofs, audited by other agents in the same session.
No external independent review, tensor construction, or improved matrix
multiplication exponent is claimed. The all-degree B comparisons use
the canonical target first bases; the C theorem permits arbitrary
target coefficients. Projected Koszul maps and other invariants are
outside the completed ordinary Koszul census.

