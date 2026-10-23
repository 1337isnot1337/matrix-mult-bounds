# Completeness of convolution recognition inside an addition support

**Status:** written proof, unreviewed. Claim
`AI-ADDITION-SUPPORT-RECOGNITION-001`. This is an elementary support statement,
not a tensor-character inequality or an exponent result.

## Statement

Let S be a nonempty finite subset of

`{(x,y,z) in Z^3 : x+y=z}`,

and let each axis contain exactly the coordinates occurring in S. Write
`C(r,s)={(i,j,i+j): 0<=i<r, 0<=j<s}` for positive integers r,s.
Then the following are equivalent:

1. S is C(r,s) after a permutation of the three axes and arbitrary bijections
   on their coordinate sets.
2. S is recognized by testing each choice of output axis, sorting the used
   coordinates on each axis, optionally reversing each sorted order, and
   checking equality with the complete convolution support.

Thus a rejected block in the archived search or PR118 cannot become an exact
single convolution solely by allowing more coordinate permutations. General
linear changes of basis, restrictions to smaller supports, multiple-block
recognition, and stronger lower bounds remain outside this statement.

## Proof

Condition 2 immediately implies condition 1: every order or reversal is a
bijection and the tested support is exactly C(r,s).

Conversely suppose condition 1. Call the actual integer labels on the chosen
two input axes f_i and g_j, and those on the chosen output axis h_k. Each list
is injective. The original equation x+y-z=0 gives fixed signs
epsilon_f, epsilon_g, epsilon_h in {1,-1}, with one negative sign, such that

`epsilon_f f_i + epsilon_g g_j + epsilon_h h_(i+j) = 0`       (1)

for every 0<=i<r and 0<=j<s. The signs depend only on which original axis
plays each role. The support is the *complete* convolution: all these pairs
are present, and no additional terms are present.

First suppose r,s>=2. Apply (1) to (i+1,j) and (i,j+1). Their output index is
the same, so subtraction gives

`epsilon_f (f_(i+1)-f_i) = epsilon_g (g_(j+1)-g_j)`           (2)

for every 0<=i<r-1 and 0<=j<s-1. Both index ranges are nonempty. Fixing j
shows that every signed f increment is equal; fixing i shows the same for
g. Denote their common value by d. It is nonzero by injectivity. Therefore

`epsilon_f f_i = epsilon_f f_0 + i d`,
`epsilon_g g_j = epsilon_g g_0 + j d`.

Every k in {0,...,r+s-2} is a sum i+j in these ranges. Substitution into (1)
therefore forces

`epsilon_h h_k = -epsilon_f f_0 - epsilon_g g_0 - k d`.

All three lists are strictly monotone arithmetic progressions. Sorting each
actual coordinate set recovers its convolution indexing, possibly reversed.
One of the tested reversal patterns consequently gives exactly C(r,s).

Now suppose r=1. Equation (1) says that h_j is an affine function of g_j with
slope +1 or -1. Their orders therefore agree or are reversed. After sorting
the two nonconstant coordinate sets and choosing the appropriate reversals,
the terms are exactly (0,j,j). The labels need not be arithmetic progressions
in this case. The case s=1 is identical with the inputs exchanged, and
r=s=1 is a single term. This proves condition 2 in every case.

## Connection to the implementations

The independent `check.py` compares literal sets. The reviewed producer
instead checks the dimension condition, the term count r*s, and the additive
equation for every relabeled term. These tests are equivalent here: coordinate
bijections keep all terms distinct, and the complete expected convolution
contains exactly r*s terms. Containment plus equal cardinality is equality.

The proof is self-contained. The source support and the existing recognizer
are credited to the historical search and PR118, pinned in `sources.json`.
The local addition is the argument that their reversal search already covers
arbitrary coordinate bijections in this stated class. No historical priority
or external proof review is claimed.

The regression test independently tries all input-coordinate permutations
for every nonempty subset of C(3,3), deriving the required output bijection
from each proposed convolution labeling. This finite comparison checks the
implementation on 511 supports; the all-size statement follows from the
argument above, not from that finite census.
