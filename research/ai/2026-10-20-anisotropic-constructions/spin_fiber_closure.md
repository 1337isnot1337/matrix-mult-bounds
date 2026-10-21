# A linear identity also excludes Laurent limits of the weighted spin family

Written local proof, unreviewed, October 21, 2026.
Claim AI-SPIN-FIBER-CLOSURE-124 strengthens claim 118 for the same fixed
local map and radix fibers. It gives no matrix multiplication exponent gain.

## 1. A three-coefficient identity

Use exactly the raw-column weighted maps, numbering, and original source
of [claim 118](spin_fiber_compression.md). No weight is fixed or required
to be nonzero. Let C(x,y,z) denote an actual output coefficient.

For k=2, put A=w96*w239*w372 and B=w14*w157*w290.
Complete contraction from A(4,4) gives

    C(0,1,39)   = A,
    C(30,31,39) = A+B,
    C(30,31,69) = B.

The integral numerator has a common factor 64, canceled by the three
map denominators. Thus every weighted output obeys

    C(0,1,39)-C(30,31,39)+C(30,31,69)=0.                 (1)

The desired M9 coefficients are respectively 0, 1, 0, violating (1).
This linear identity holds identically in all 432 raw weights. It holds
over rational-function or Laurent-series extensions as well. If a
parameter-dependent output has a regular limit, that limit still obeys
(1). Consequently arbitrary pole weights and cancellation cannot give M9
inside this family.

## 2. A new base at three bits

Append high matrix-unit digits (E02,E20,E00) to those three output triples.
The new row triples at n=27 are

    (18,487,111), (102,571,111), (102,571,195).

The full A(8,8) contractions have integral numerators

    512 A', 512(A'+B'), 512 B',

where A'=w572*w3151*w3952 and B'=w90*w2669*w3470.
The common denominator is 512. Again the output relation has coefficients
(1,-1,1), while the M27 values are 0, 1, 0. This explicit three-bit
contraction is checked separately; it is not inferred by assuming that
arbitrary radix tensor powers preserve the original identity.

The two first-leg row images have minimum middle coordinates 11 and 9.
Both are at least 2^3-1=7.

## 3. All higher powers

The induction mechanism in claim 118 only requires that each lower
first-leg row have minimum middle at least d-1, where d=2^k.
Append high matrix units (E00,E02,E20). The E02 and E20 rows each have
one source column. The E00 row has columns (0,1,1) and (1,2,1).
The latter would require middle_X>=3d-1 while p+q<=3d-2, so it contributes
nothing. The surviving high columns reduce all source equalities to the
old ones and multiply every numerator by 8, with injective variable
renaming. The target numerator also scales by 8.

The new minimum first middle coordinate is at least (d-1)+d=2d-1.
The hypothesis therefore persists. Starting from Section 2 proves a
linear identity violated by M_(3^k) for every k>=3. Section 1 covers k=2.
At each power the hyperplane is fixed independently of the weights, so
it contains the image and all its regular limiting degenerations.

## 4. Replay, discovery, and exact scope

The maintained verifier uses only the standard library and the exact
coefficient engine of claim 118. Its certificate records the full selected
polynomials at powers 2, 3, 4, 5. Tests also enumerate all 4096 original
A(4,4) terms independently and reject a modified saved polynomial.

~~~sh
python -S research/ai/2026-10-20-anisotropic-constructions/spin_fiber_closure.py
python -S -m unittest discover -s tests -p 'test_spin_fiber_closure.py' -v
~~~

A bounded tropical solver suggested three relevant output coefficients.
The acceptance proof uses the exact linear identity (1), not the solver's
unsatisfiability report or a finite grid of weights. The higher-power
statement uses the written induction, not extrapolation from finite tests.

This excludes scalar weights on the prescribed columns of the fixed
spin map, including arbitrary Laurent weights and their limits. It does
not exclude changed local maps, arbitrary source linear compression,
or additional output maps outside that family. The prior ordinary
certificate remains correct; its formerly open Laurent question is
settled here only within this same specified family. No external
independent review or historical priority is claimed.
