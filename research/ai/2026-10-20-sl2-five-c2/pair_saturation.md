# Cocycle parity forced by saturated central fibers

Written, unreviewed. No smaller exponent or target degeneration is obtained.
This continues the necessary conditions in projected_note.md.

Let Z=C2 times C2 be the center of the selected group G=SL(2,5) times C2.
Identify Z with F2^2 in the recorded, exactly checked order. Fix a section
r of G/Z. A selected full point over p has the form z_(b_p) r(p), where
b_p is an unknown two-bit vector. For each ordered projected pair define
the exactly computed cocycle offset k(p,q) by

    r(p)^-1 r(q) = z_(k(p,q)) r(p^-1 q).

Since the center has exponent two, the full pair label has central color

    b_p+b_q+k(p,q).

Suppose four selected pairs have the same projected label. Injectivity of
the full pair map forces their four colors to be all of F2^2. The sum of
those four colors is zero. Consequently

    sum_over_four_pairs (b_p+b_q) = sum_over_four_pairs k(p,q).       (1)

Equation (1) gives one necessary F2 equation for each central bit. For
the direct C2 bit its offset is zero. For the other bit it detects the
SL(2,5) central extension. More than four pairs gives an immediate counting
contradiction. Each row retains its inducing point support, so it stays
necessary whenever those points are present; additional points in the same
fiber would already violate the capacity bound.

The generator combines (1) with the previously derived inverse-class
equations and eliminates over F2 with exact row provenance. The independent
verifier reconstructs all cocycle offsets by group multiplication, checks
that each saved row is induced by the selected pairs, and verifies an XOR
dependency with right side one. No floating point or solver refutation is
accepted for these certificates.

The first 300-second run with fixed thirteen-point projection rejects 169
candidates, all by these exact augmented parity circuits, without reaching
an inner lift solver. A separate 600-second run learns individual necessary
rows inside the outer SAT solver: it reaches 245 candidates, rejects 244 by
exact circuits and inserts 1,075 conditional rows. One candidate passes the
augmented parity test but gets an untraced inner solver refutation. All 244
saved circuits replay exactly. Neither run has a witness. The first run has
no untraced inner core; the learning run's one core is not certified evidence.
No distinctness claim is made
between runs, and no complete projected or group-degeneration exclusion is
claimed. The first saved circuit uses 24 twisted-bit rows and all 41 selected
points; their XOR is zero on the left and one on the right.

Controls enumerate all 4^6=4096 normalized lifts of a fixed four-by-four
projected pair. Exactly 128 have an injective full pair map; every one
satisfies all induced saturation equations. Other assignments violate the
equations, confirming that the test is nonvacuous. A five-pair capacity
certificate and a parity circuit are deliberately damaged and rejected.
These finite controls do not replace the derivation of (1).

The optional learning adapter introduces auxiliary XOR variables and guards
the final parity equality by the inducing point selections. Such learning
changes discovery, while the saved exact circuits remain the accepted
evidence. The unchanged integer witness verifier still checks every group
product and strict potential before any positive result is accepted.

Reproduce acceptance with the maintained verification environment:

```sh
python research/ai/2026-10-20-sl2-five-c2/pair_saturation.py \
  results/sl2-five-c2-2026-10-20/projected-saturated-first13.json
python research/ai/2026-10-20-sl2-five-c2/pair_saturation.py \
  results/sl2-five-c2-2026-10-20/projected-saturated-learning-first13.json
python -m unittest discover -s tests -p test_sl2_five_saturation.py -v
```

Discovery additionally needs the pinned optional SAT/LP dependencies. The
command uses projected_saturated.py with --pair-capacity --inverse-capacity
--native-binary and the saved --first-projection list. Add --learn-saturated
for conditional-row learning. The exact reports retain the limits and scope.
