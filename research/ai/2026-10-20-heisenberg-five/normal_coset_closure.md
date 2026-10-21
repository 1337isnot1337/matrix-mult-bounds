# The Heisenberg(5) single-target coordinate route is excluded

AI-derived written proof, unreviewed. This closes a source/construction
class; it does not improve omega or exclude a general complex degeneration
of this group algebra. No priority or independent-review claim is made.

The new ingredient is the finite-plane incidence argument below. The
rectangular normal-coset Koszul bound is the concurrent worker's existing
[result](../2026-10-20-normal-coset-koszul/rectangular_note.md), now merged
in main. That note credits Strassen's three-slice bound and proves the
specific rectangular rank used here. We apply its formula unchanged.

## 1. Necessary bounds on every parallel class

For a size-(s,t,u) coordinate construction in H_5, with s,t,u each at
least nine, the central-coset injection proved in source_proof.md forces
every selected set to have distinct images in H_5/Z=F5^2:
twice every other-pair size exceeds 125. Every projected parallel class
comes from an abelian normal subgroup H of order 25 and index five.
Let a,b,c be its five fiber-count arrays. They satisfy

    max(a)*max(b)*max(c)<=25,                                (1)

by the maintained abelian-coset theorem. For every pair of independent
cyclic shifts of b,c, they also satisfy all three rectangular inequalities

    sum_i R(a_i,b_i,c_i)<=50,
    R(x,y,z)=z*(3 min(x,y)-1[x=y=1]),                         (2)

and the two other first-leg choices R(a,c,b),R(b,c,a). These are the
merged rectangular Koszul inequalities. Initially every count is at most
five, because a projected affine line has five points.

## 2. The balanced size-ten target has no five-point fiber

If a fiber has size five, (1) forces the two other largest fibers to
equal two. Those two arrays, each summing to ten, are therefore constant
two. Taking them as the first two arguments in (2) gives rank score
6*10=60>50, a contradiction. Thus all counts are at most four.

Each maximum is at least two. Since 3^3>25, one family must have maximum
two in every parallel class, meaning its array is (2,2,2,2,2).

## 3. A small exact count classification

Five-entry arrays in {0,1,2,3,4} summing to ten have 381 values and
77 cyclic classes. Fix the constant-two family. For each of the 3003
unordered pairs of the remaining classes, the standard-library verifier
checks (1), then all five relative shifts and three choices in (2).
Only these four pairs survive:

```
(0,0,2,4,4)  with (0,3,3,1,3)
(0,0,4,4,2)  with (0,3,1,3,3)
(0,1,3,3,3)  with (0,4,0,4,2)
(0,2,4,0,4)  with (0,3,3,3,1)
```

Their maximum rank score is 48. Coverage is checked against an independent
coefficient recurrence for (1+x+...+x^4)^5, including the constant array's
one-element rotation orbit. No SAT refutation is used in this classification.

Consequently every family's line-count multiset, in every one of the six
directions of F5^2, must be one of

    (2,2,2,2,2),  (0,0,2,4,4),  (0,1,3,3,3).                (3)

The number of unordered point pairs on those five parallel lines is,
respectively, 5,13,9. All three numbers are one modulo four.

But each unordered pair of distinct projected points lies on exactly one
affine line and hence is counted in exactly one of the six directions.
A ten-point set would therefore have a total pair count congruent to
six, or two modulo four, while its actual count is binom(10,2)=45, or
one modulo four. This contradiction excludes M(10,10,10) in the entire
injective-pair-map, strict-vertex-potential construction class.

## 4. The unequal target (9,10,11)

Every fiber is again at most four. A five-point fiber in the size-nine
or size-ten family violates (1), because the other maxima are at least
two and three. If the size-eleven family has a five-point fiber, (1)
forces the other maxima to be two. Their arrays are, up to shifts,
(1,2,2,2,2) and (2,2,2,2,2). Shift the size-eleven array to put its
smallest entry at the deficient position. That minimum is at most two;
the score is at least 3*(2*11-2)=60>50. Thus this case is impossible too.

The size-nine, ten, eleven arrays have 365,381,365 possible values and
73,77,73 cyclic classes. Of the 410333 ordered class triples, 4757 pass
(1). Exhaustive integer checking of all 25 relative alignments and all
three choices in (2) leaves 58 triples. In every survivor the middle
array is constant two. Hence the ten-point projected family would have
two points on every line of every parallel class. Its pair count would
be 6*5=30, contradicting 45. This excludes the unequal target.

## 5. Complete single-target source-cost consequence

The exact 9/4 degree comparison has nine sorted positive matrix shapes
with largest input dimension at most 125. The maintained rank-locus
screen, which applies to arbitrary complex degenerations, excludes six.
Its only survivors are (10,10,10), (9,10,11), and (10,10,11). Sections
3-4 exclude the first two in the coordinate-potential construction;
the last contains a size-ten square subtarget and is excluded as well.

The finite frontier is generated with certified integer root intervals.
Targets with a size-one side cannot pass: their volume is at most 125.
If the effective side V^(1/3) is at most five, even one degree-five
source summand costs at least the target. Otherwise every ratio
d_i/V^(1/3) is below one, so failure of the strict degree-sum gate at
9/4 persists at smaller positive exponents. Thus no single matrix target
in this construction class gives an improving gate in [2,9/4].

This conclusion leaves arbitrary complex tensor degenerations, noncoordinate
linear maps, multiple-target or tensor-power extraction, and other groups
open. The 2.247 numbers in the earlier task selection remain conditional
comparisons whose coordinate construction premise is now excluded here.

## Verification and attribution

`normal_closure.py` imports the merged rectangular score rather than
reimplementing its rank theorem. It independently enumerates the small
count classes, checks composition coverage, lists every survivor, verifies
the incidence contradictions, and rebuilds the exact source-cost frontier.
The source-character and two-coset replay controls remain separate.

```sh
python research/ai/2026-10-20-heisenberg-five/normal_closure.py
python -m unittest discover -s tests -p test_heisenberg_five.py -v
```

All arithmetic in these finite checks is integral or certified rational.
The earlier untraced seven-class SAT reports are discovery history only;
they are not premises of this proof.
