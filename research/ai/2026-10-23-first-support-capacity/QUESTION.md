# Question and coordination

Starting main: `3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93`.
Topic branch: `research/repair-support-capacity-20261023`.

Can small first-support repair compensate for missing long-map images
in a near-full paired matrix target? If it forces the long maps to be
surjective, does the literal source-slice geometry constrain a specified
polynomial first-map class with arbitrary long maps?

The delivered statements are a Laurent support-capacity theorem and
two ordinary lower bounds for a fixed-polynomial first map. They remain
separate: the second proof requires exact ordinary rank-four slices.
There is no matrix construction or smaller exponent.

## Overlap checked on October 23

- Main's paired-source notes already give the raw source-slice lower
  bound and an unstratified finite-divisor incidence argument. These are
  adopted with byte pins; they are not new claims here.
- PR147 supplies the oblique maps used only as a comparison example.
  Its immutable commit and proof hash are recorded, and the new verifier
  does not require an unmerged path on disk.
- PR157, inspected by the coordinating parent at head `9e830aa`, studies
  ordinary finite-bandwidth Toeplitz long maps with exceptional columns
  and an arbitrary first map. This package restricts the first map and
  permits arbitrary long maps. The hypotheses differ, and neither is
  presented as an unrestricted result. No theorem from PR157 is imported.
- PR142 concerns first-gap source loci for the cyclic `A_a` source, not
  the paired `Q(n,4)` first-map class used here. No result is imported.
- The operational formal-repair barrier and conditional residual-cost
  criteria in PR130 are not used in either proof. No unmerged external
  source registry entry is required.

The next question is an actual construction outside the fixed-multiplier
class, or a justified ordinary classification of the shared-kernel
rank-at-most-thirty-six families in Section 5. The universal Laurent
support theorem gives necessary long-map ranks but does not turn the
ordinary slice analysis into a Laurent obstruction.
