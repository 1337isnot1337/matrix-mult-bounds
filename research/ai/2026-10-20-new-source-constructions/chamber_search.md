# A compatible chamber with fewer coefficient equations

October 21, 2026. This is an exact construction formulation and a recorded
discovery search. No exact degeneration or smaller exponent is established.

## 1. Change the weights and retain every required coefficient

Use the same source `C(4,10)`, target `T4`, and point order as the main
note. Set

\[
 \beta=100,\qquad \eta=(0,301,628,844).
\]

The three weight families remain

\[
 w_X(p)=\beta p,\qquad
 w_Y(a,b)=\eta_{a+b}-\beta a,\qquad
 w_Z(c,d)=-\eta_{3-c-d}-\beta c.
\]

Every desired term has total weight zero. All Y weights are distinct, and
all Z weights are distinct. Assign a monic input polynomial P_y of degree
9-rankY(y), and a monic output functional Q_z whose first nonzero source
coordinate is rankZ(z). The shared polynomial G_p has degree 3-p. As in
the main note, source translation fixes G_2=t and normalization fixes G_3=1.

In the stated point order, the new flags are

```
degree(P_y): 9, 7, 8, 3, 5, 6, 0, 1, 2, 4
pivot(Q_z): 0, 2, 1, 5, 4, 3, 9, 8, 7, 6
```

The source still has 125 free monic coefficients. Exactly 115 transformed
tensor entries have nonpositive weight. None of those entries is forced
to vanish just by the degree flags. Twenty entries are desired target
terms, and the other 95 must vanish. The twenty target coefficients must
be nonzero and satisfy the same two target-orbit binomials from the main
note. Thus this chamber needs **97 polynomial equations in 125 variables**,
with twenty nonvanishing conditions.

The predecessor chamber needed 103 equations: 101 zero conditions and two
target-orbit conditions. The new count is six smaller. This is a different
weight degeneration, not permission to discard six constraints from the
old one. Its nonpositive mask removes eight old entries and adds two:

```
removed: (0,1,9), (0,2,8), (0,4,5), (0,5,4),
         (0,5,9), (0,9,5), (1,2,9), (1,5,5)
added:   (3,0,3), (3,1,1)
```

Triples in this display mean `(p,y,z)`. The indices y and z refer to the
ten-point order in the main note. The Q pivots also change, so the two
polynomial systems cannot be compared by their entry masks alone.

`chamber_system.py` derives all degrees, polynomial coefficients, and
constraints from the specified weights. It rejects tied flag weights,
absent desired pivots, and unwanted coefficients forced to be nonzero by
their leading terms. Its exact sparse evaluator checks the new chamber's
full nonpositive mask. Two added tests reproduce the complete predecessor
system and compare every new nonpositive entry against direct source
polynomial multiplication over F3 and F4.

If an exact residue-field point satisfies the 97 equations, has nonzero
target coefficients, and its 97-by-125 Jacobian has row rank 97, the same
Hensel and target-normalization argument from the main note applies. The
remaining 28 coefficients can be fixed while lifting the selected square
system. No such point has been found. A smaller equation count does not
establish existence.

## 2. Reproducible discovery of the weights

`chamber_search.py` samples 20,000 integer offset triples using Python's
`random.Random` with seed 829191. Each offset lies in [-900,900], eta_0 is
zero, and beta is 100. It rejects the leading-term obstructions described
above. The saved run retained 6,928 samples and 1,745 distinct coefficient
patterns. Patterns distinguish both polynomial flags and all retained
coefficient constraints.

The displayed chamber was the unique sampled pattern with 115 coefficient
equations. The next count in this sample was 117. The compact saved report
contains the count histogram and twenty best sampled representatives. This
is not an enumeration of all real chambers and does not prove optimality.

## 3. Actual construction searches

The complete finite queries over F3 and F4 each ran for 120 seconds and
returned `unknown` with reason `timeout`. They imposed no additional
restriction on the five shared-polynomial residue coefficients. A second
F4 run used the `qfbv-sls` tactic on the exact same query. It also timed
out after 120 seconds. It is a different solver attempt on the same
finite mathematical question.

The Boolean F2 formulation requires each target coefficient to equal one;
these are the only nonzero field values. Its candidates, if returned, are
checked by the same exact evaluator over the containing field F4. Matrix
rank of an F2 matrix is unchanged by this field extension. The two toric
relations hold automatically when every target equals one. Its actual
outcome is recorded in `chamber-f2.json`: the solver reported UNSAT after
7.293 seconds. The saved query has no independently checked UNSAT proof.
This finite-field outcome is not a characteristic-zero exclusion.

The bounded complex optimizer started from the preceding numerical point,
transferred coefficients by their actual source coordinates, and added a
seeded complex perturbation. It checked all 115 normalized nonpositive
coefficients with a separate convolution implementation. After 2,000
function evaluations, its residual norm was 2.4937721e-7, and its largest
individual residual was 1.3747897e-7. The smallest row-scalar magnitude
was 0.0623067, and the largest coefficient of the complete transformed
tensor was about 227.007.

The first five shared coefficients were again small: their magnitudes
were at most 6.27e-6. The smallest numerical Jacobian singular value was
about 2.27e-9. This is another near-singular numerical point near the
excluded pure-power shared stratum. It supplies no exact construction and
does not justify further optimization toward that same limiting stratum.

The suite now has thirteen exact tests, all passing. The chamber comparison
and direct source checks establish the implemented coefficient systems;
they do not certify a solution. A size-four construction would still need
an all-size growth argument before it could yield a smaller value of omega.

## 4. Exact elimination within the new chamber

The integer coefficient-by-degree matrices have 65 unit elimination pivots.
Their nonzero ranks are 6, 8, 13, 11, 9, 7, 5, 3, 2, and 1. Every selected
square minor has determinant +1 or -1. Thus the formulation can retain 60
free monic coefficients and 18 nonzero target row scalars, with 50 residual
coefficient equations. The previous chamber retained 57 monic coefficients
and 18 target scalars with 53 residual equations. This changes the system;
it does not establish a computational speedup or a solution.

`chamber_elimination.py` reconstructs this elimination from the actual
chamber after an interrupted execution session. Its exact test checks every
original coefficient over F3 and F4, including all eliminated rows. An early
working message incorrectly summed the pivot ranks to 75; both the direct
coefficient reconstruction and the saved report give 65. The incorrect
count is not used in any result.
