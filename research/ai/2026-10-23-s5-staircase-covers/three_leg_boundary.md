# Complete monotone three-leg cube boundary for S5 x C2

October 23, 2026. Claim `EXP-S5-THREE-LEG-COVERS-002` is a finite
experiment with a written completeness argument. It does not establish
optimal slice rank of the actual source or independent mathematical review.

The [preceding census](proof.md) fixes two equal threshold legs. This
continuation removes that equality for r=1, while keeping precisely the
same four cube block words, bidegree support majorants and monotone
threshold cover model. The result does not cover r=2 with three unequal
legs, nonmonotone covers, finer actual source support or other powers.

## Minimal third leg for two arbitrary first legs

For a block word put D=6j and k=6-j. Let f and h independently range over
all nonincreasing maps {0,...,k}->{-1,...,D}. The cheapest third threshold
is

    g(c)=max({-1} union
        {D-2-f(a)-h(b): a+b+c<=k, f(a)<D, h(b)<D}).

The proof is identical to the unequal version of the earlier uncovered
triple argument: when the first two legs do not already cover everything,
their least uncovered principal degrees are f(a)+1 and h(b)+1. All
principal degree triples of total at most D are covered exactly when the
displayed lower bound on g(c) holds. The maximum is at most D, and g is
nonincreasing. Positive coordinate multiplicities make this least g
optimal for the given f,h.

The implementations compute the same expression by first finding the
minimum f(a)+h(b) at each a+b and then taking its successive minima. Full
thresholds f(a)=D or h(b)=D are omitted from that minimum. An empty set
gives g(c)=-1. Thus computing this third leg does not search or truncate
any additional possibilities.

## Exhaustive pair census and justified pruning

Enumerate all N=binomial(D+k+2,k+1) monotone thresholds and sort them by
their exact one-leg costs, breaking ties lexicographically. Exchanging the
first two legs changes neither the support majorant nor the objective,
so enumerate only unordered pairs, including equality. There are
N(N+1)/2 pairs before pruning.

The initial incumbent is the full third leg with two empty legs. For
sorted indices a<=b, stop an inner loop when cost(f_a)+cost(f_b) is at
least the incumbent: third-leg costs are nonnegative and subsequent b
have no smaller cost. Stop the outer loop when 2cost(f_a) is at least
the incumbent. These tests discard only pairs that cannot improve a
known valid cover. Equality may be discarded because this is minimum
cost enumeration, not a census of all minimizing witnesses.

| j | N | Unordered pair universe | Evaluated after pruning | Minimum cost |
|---:|---:|---:|---:|---:|
| 0 | 8 | 36 | 13 | 147456 |
| 1 | 1716 | 1473186 | 78920 | 397568 |
| 2 | 8568 | 36709596 | 2346697 | 997536 |
| 3 | 8855 | 39209940 | 2782113 | 2534774 |

The universe has 77392758 pairs; 5207743 require the exact third-leg
calculation. The separate standard-library Python and C++ enumerations
agree on every count, cost and retained witness. All accepted arithmetic
uses integers. The C++ counters and costs fit signed 64-bit integers;
here one word's entire leg has at most 88^3*8 coordinates, and all pair
counts are below 2^31. There is no floating-point acceptance step.

Summing minima with word multiplicities (1,3,3,1) gives 6867542, exactly
the earlier weighted cube cover. The threshold for M(13,14,14) is
2548^2=6492304, strictly smaller. Thus no monotone threshold cover of
these block-word bidegree majorants can supply that target exclusion by
the previous cube comparison.

This is a limitation of the specified finite counting model. The support
majorants contain triples that need not be actual source coefficients.
No construction of the target, lower bound on the source's true slice
rank, arbitrary coordinate-cover optimality or exponent improvement follows.

## Verification and attribution

`three-leg-census.json` is the completed Python output, not an interrupted
partial report. The retained C++ output has the same four rows and witness
arrays. Literal small support enumeration checks the third-leg formula
for every pair of monotone thresholds at D,k<=2, including the empty and
full-leg boundaries. Every retained full-sized witness is tested on its
entire bidegree support majorant. An optional compiled cross-check reruns
the complete C++ enumeration in a temporary directory and compares the
output with the Python report; the primary producer uses only Python's
standard library. Absence of a compiler skips that extra cross-check.

Both implementations and the completeness argument are from the same
owner-directed Codex campaign. Agreement is separate code replay, not
independent mathematical review. The S5 group algebra certificates,
degree model and external finite matrix target theorem retain their
prior attribution through the pinned finite-cover package. No additional
external theorem is imported by this finite combinatorial reduction.
