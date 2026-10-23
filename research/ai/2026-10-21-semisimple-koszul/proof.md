# Full-space semisimple Koszul screens and an exact SL(2,F8) source

October 21, 2026. AI-SEMISIMPLE-KOSZUL-017 and AI-SL2-F8-SOURCE-018.
Written proofs and conditional implication, unreviewed. No smaller exponent.

## 1. General source and rank formula

Work over C with source S=direct_sum_i M(d_i,d_i,d_i), where d_i are
positive integers. Put D=sum_i d_i^2. For an a-by-b matrix pencil with
its entire ab-dimensional first leg, let f_(a,b)(q) be its Koszul rank
without the independent repeated-column factor. In code this is
`matrix_basic_rank(b,a,q)`: the first argument is the input dimension.
The exact formula is imported unchanged from the earlier
[Casimir proof](../2026-10-20-paired-sources/matrix_koszul.md) and
[Euler proof](../2026-10-20-paired-sources/matrix_euler.md).
These are written, unreviewed derivations. Standard Koszul flattenings
and the prior kernel-module inclusion are attributed there to Landsberg
and Ottaviani, [Theory of Computing 11 (2015)](https://theoryofcomputing.org/articles/v011a011/).
No new general matrix-rank formula or historical priority is claimed here.

Padding the first leg from ab to D gives

```
F_(a,b,D)(p) = sum_q binomial(D-ab,p-q)*f_(a,b)(q).          (1)
```

Indeed, split the exterior algebra into used and unused first-leg
directions. For each q, every choice of p-q unused directions gives an
independent copy of the qth intrinsic map. Thus the exact full-space ranks
of the source and of a padded matrix target are

```
rank K_p(S)          = sum_i d_i*F_(d_i,d_i,D)(p),           (2)
rank K_p(M(a,b,c))   = c*F_(a,b,D)(p).                     (3)
```

For(2), the other two tensor legs split into independent source blocks,
so ordinary matrix ranks add. This is not an additivity assertion about
tensor rank or border rank. Every number in(1)-(3) is an exact integer.

If(3) exceeds(2), the proposed degeneration is impossible. The Koszul map
is polynomial in tensor entries, and bounded matrix rank is closed under
degeneration. Arbitrary local linear maps can be obtained as limits of
invertible maps in fixed padded leg dimensions, so the argument applies
to all complex tensor degenerations, not only coordinate constructions.

It suffices to check 0<=p<=floor(D/2) and all tensor-leg orderings.
Exterior duality identifies power D-p-1 with the transpose map after
exchanging the remaining legs. The square-block source has the same
rank under that exchange. The code checks all distinct permutations of
the target sides and uses this duality for the other half of the powers.

Tests construct every first-leg slice of small direct-sum sources and
compare their full integer Koszul matrices with(2). A seven-scalar to
M2 control passes, while four scalars to M2 fail at power1 with ranks12
and16. These controls check the padding and orientation conventions.

## 2. General F8 exclusions

For C[F8^2:C7], the degrees are seven copies of1 and nine copies of7.
The earlier exact source-degree/rank-locus frontier left26 formats.
The new full-space tests exclude these five under arbitrary complex
tensor degeneration:

| Matrix format | Koszul power |
| --- | --- |
| (16,16,26) | 189 |
| (17,17,24) | 210 |
| (18,18,23) | 188 |
| (18,19,22) | 187 |
| (19,19,22) | 178 |

The report stores both exact integer ranks for each witness. Twenty-one
formats still pass these general tests, including(19,19,19). Thus these
are broader exclusions for specific formats, not a general exclusion of
the source's improving matrix targets. The separate normal-coset
construction barriers have narrower hypotheses and retain their status.

## 3. Exact SL(2,F8) source

Represent F8 as F2[t]/(t^3+t+1), using the existing exact multiplication
function. Enumerate all2-by2 matrices with determinant one. Matrix
multiplication gives a504-element group; every product and inverse is
checked by table construction. Tests independently verify the field
associative and distributive laws on all8^3 triples. The matrix group
laws then follow from matrix algebra over this field. Its computed center
has order one; no external character table is imported.

The central-algebra derivation reuses the unchanged procedure from the
[SL(2,7) source package](../2026-10-20-sl2-seven/source_proof.md), with an
isolated group-table callback. Prime-field arithmetic from that package's
group constructor is not used. Exact rational class multiplication,
a cyclic center generator, its squarefree minimal polynomial and rational
central idempotents derive the complex matrix block degrees

```
1, 7,7,7,7, 8, 9,9,9.
```

The nine class sizes are1,63,56,56,72,56,72,56,72. The regular ranks of the
central projectors sum to504, and the complex degree squares sum to504.
The exported polynomial, idempotents and perfect-square block checks are
recomputed in the tests. This uses the standard characteristic-zero
group-algebra interpretation already stated in the source package.

All5834 sorted dimension-compatible shapes with a>=2 are screened.
The exact9/4 degree comparison holds for56; the general rank-locus theorem
leaves18. Full-space Koszul ranks further exclude(18,18,26) at power232
and(21,21,22) at power237. Sixteen shapes remain, with eight componentwise
minimal elements recorded in `frontiers.json`.

In particular(18,18,25) survives every stated necessary test. If a genuine
complex degeneration from this group algebra to M(18,18,25) were supplied,
the existing group-algebra/asymptotic-sum bridge would give an arithmetic
exponent at most449/200=2.245. This is a conditional implication only.
No such degeneration is supplied.

The numerical comparison is certified by integer root intervals at
scale10^10. At tau=449/200 the source upper numerator is8395333387305,
and the target lower numerator is8411038530536. Their difference is
15705143231>0. Tests check the defining integer power inequalities
for every interval, not floating approximations. The source blocks are
smaller than the target's geometric mean, so the same monotone source-cost
argument used in the existing bridge applies. Border conversion and
the usual exponent slack retain that bridge's existing hypotheses.

## 4. First restricted construction experiment

The first pilot fixes S to one full order-eighteen dihedral subgroup H.
It obtains a cyclic order-nine subgroup and an involution inverting its
generator, then checks all324 products of H. The other sets have sizes
18 and25, contain the identity after independent right translation, and
meet each right coset H*g in at most one point. This exactly enforces
their pair-map injectivity with S. Membership clauses also require the
two remaining right-difference sets to be disjoint away from the identity,
which enforces the T,U pair map.

This fixes a particular full-subgroup frame. It does not cover arbitrary
vertex families or general tensor maps. The actual180-second pilot used
42994 variables and336676 clauses, returned no pair model and timed out
after180.02 seconds. It proves no nonexistence. The independent replay
checks actual cuts and witnesses only; there are none in this report.

The separate positive control fixes the same S and uses T=U={identity}.
SAT and LP discovery return a zero-potential M(18,1,1) witness; the exact
streaming verifier checks all18 intended terms and no extra terms. This
control does not pass the exponent gate. No construction approaching the
improving target has been found.

The optional discovery code uses python-sat and the existing NumPy/SciPy
LP discovery. Maintained source, rank and report verification do not import
these optional packages. Every accepted target must pass the independent
full-support integer verifier. Timeouts and untraced UNSAT remain finite
experiment outcomes.

## 5. Reproduction

From the repository root with its maintained requirements:

```sh
python research/ai/2026-10-21-semisimple-koszul/semisimple_koszul.py --output results/local/semisimple-koszul.json
python research/ai/2026-10-21-semisimple-koszul/sl2_f8_source.py --output results/local/sl2-f8-source.json
python -m unittest discover -s tests -p test_semisimple_koszul.py -v
```

The default full-D18 command now replays the subsequent exact subgroup-ideal
exclusion244<450 before importing optional discovery dependencies. Its
report has status `excluded-by-subgroup-ideal`; it does not repeat the
historical180-second pilot. The positive control still requires the
optional discovery dependencies:

```sh
python research/ai/2026-10-21-semisimple-koszul/subgroup_search.py --seconds 180 --output results/local/sl2-f8-subgroup.json
python research/ai/2026-10-21-semisimple-koszul/subgroup_search.py --control --seconds 30 --output results/local/sl2-f8-subgroup-control.json
```

The timing and solver outcome need not repeat. Exact acceptance conditions
and the source/rank certificates are independent of solver timing.
