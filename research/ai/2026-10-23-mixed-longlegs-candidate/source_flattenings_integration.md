# Source formulas and component screens: integration record

Date: 2026-10-23. Owner-directed work in one generating session. These
are written proofs and finite exact controls, with no external mathematical
review or formalization. They do not construct a degeneration or improve
the matrix-multiplication exponent.

## Included results and their scope

[source_b_koszul.md](source_b_koszul.md) proves all second-leg exterior
ranks and simultaneous tensor-power contraction ranks for Full sums with
one common canonical first coefficient basis. The proof explicitly computes
the evaluation kernel on the projective line. Its fiber argument permits
evaluation quotients of any rank. The B-leg exterior formula holds over
every field; the component screens below use characteristic zero.

[schur_screen.md](schur_screen.md) records the completed decomposition of
those tensor-power tests into every symmetric-group component. All ten
components in degrees two through four pass for the stated canonical
target. Degree one passes and degrees at least five are automatic. This
target calculation fixes the canonical first identifications. It is not an
all-identifications obstruction or a claim that all Young flattenings pass.

[source_c_koszul.md](source_c_koszul.md) has a different, broader hypothesis:
every nonzero first-leg slice is injective from the second leg to the third.
It gives every C-leg Koszul rank and shows that each is the maximum over
the entire tensor format. Full sums satisfy this hypothesis even with
independent invertible first identifications in their blocks. Consequently,
every target of format (5,100,140) passes this entire C-leg family against
the stated source. The note includes a local proof using the exterior
quotient resolution and a cohomology calculation. No historical priority
is asserted for the formula or its underlying constructions.

[first_critical_source_kernel.md](first_critical_source_kernel.md) is the
audit agent's byte-identical elementary proof for the canonical first
noninjective C degree. It is retained as a separate derivation. The broader
all-C note supplies the independent-first-identification scope; this does
not retroactively enlarge the elementary note's stated scope.

## Frozen originals and integration changes

[source_flattenings_manifest.json](source_flattenings_manifest.json)
records the original SHA256 of each of the fourteen input artifacts and
its integrated path. The original scratch checkpoint was not edited.
The maintained copies adapt output paths and reproduction commands, and
replace an obsolete statement that the Schur components were not screened.
The elementary first-critical proof and four computation reports remain
byte-identical. The all-C report is regenerated to pin its integrated
proof and program bytes.

The exterior source formula was proposed by the root agent and checked
by two agents in the same session. The tensor-power extension, Schur
character computation, and all-C bundle calculation were developed by
the independent-theory agent. The root agent independently proposed the
padded comparison formula. The audit agent supplied the elementary
critical-degree proof and checked the full bundle argument. These roles
record work within one session and do not constitute external review.

## Reproduction

Use Python 3.10 or later with the standard library. Run from the repository
root, without optimization:

```sh
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_full_source_exterior.py
python research/ai/2026-10-23-mixed-longlegs-candidate/full_source_c_leg_pilot.py
python research/ai/2026-10-23-mixed-longlegs-candidate/verify_full_source_all_c.py
python research/ai/2026-10-23-mixed-longlegs-candidate/shared_output_prolongation.py --max-degree 4 --rational
python research/ai/2026-10-23-mixed-longlegs-candidate/shared_output_schur.py
python -m unittest discover -s tests -p 'test_mixed_source_flattenings.py' -v
```

Reports are in `results/mixed-longlegs-candidate-2026-10-23/`:

| Report | Completed scope |
| --- | --- |
| `full_source_exterior_controls.json` | 120 literal F2 B-leg controls |
| `full_source_c_leg_pilot.json` | 97 literal F2 C-leg controls |
| `full_source_all_c_controls.json` | 2,640 integer formula checks in 240 formats; replay of the 97 C controls; nine additional literal degrees; all 140 candidate source degrees |
| `shared_output_prolongation_controls.json` | 125 target block-tuple systems with exact rational and F2 ranks; three separate source controls |
| `shared_output_schur_controls.json` | Thirty source kernel-character controls; all nonidentity cycle-type traces; ten exact component comparisons |

F2 ranks are finite convention checks and do not provide characteristic-zero
upper bounds. The Dq and Schur target ranks use rational arithmetic.
The proof of the universal source formulas is separate from the finite
checks. The elementary note's four additional critical-degree controls
were produced by the audit agent and are not counted in this module's
replay coverage.
