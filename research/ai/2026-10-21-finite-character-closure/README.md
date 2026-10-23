# Finite constructions and the endpoint scalar closure

Date: 2026-10-21.

The accepted finite constructions do not exclude the endpoint through the
scalar profile rules considered here. The existing minimal profile is an
exact feasible assignment for every new inequality. It remains feasible
under hypothetical arbitrary-copy extensions at the same input cost per
copy. A larger explicit family of profiles also survives.

This is a closure result for a stated set of scalar inequalities. It does
not construct an endpoint tensor character, prove a lower bound for the
matrix-multiplication exponent, or exclude new tensor identities obtained
by using the actual maps.

## 1. The finite inequalities being audited

Write P for the symmetrized powered convolution character profile. At the
hypothetical endpoint t=3/4, put d=4/3. The shared-leg entropy inequality,
combined over the six orientations by weighted Holder, gives

    P(a,B) >= sum_(r=1)^m P(r,m+1-r)                 (F_m)

from a degeneration C(a,B) -> matched T_m. Each sector may have its own
invertible shared identification; a simultaneous shared basis is not
needed. This is the already proved
[independent-sector criterion](../2026-10-20-construction-sprint/independent_sector_bases.md).

The accepted finite sources in this audit are:

| Target | Source | Certificate type |
| --- | --- | --- |
| T_4 | C(5,10) | Exact finite characteristic-zero construction |
| T_5 | C(6,16) | Integer canonical construction |
| T_6 | C(7,24) | Integer canonical construction |
| T_7 | C(8,34) | Integer canonical construction |
| Independently based T_5 | C(7,15) | Exact characteristic-zero existence from the 45-equation chart |

The earlier C(9,46) -> T_8 data were not recovered as an accepted
certificate at this checkpoint. Its scalar consequence is evaluated below
only as a hypothetical extra constraint.

## 2. Exact finite compatibility

Use the established minimal profile

    h_1=1,  h_(n+1)=(1+1/(3n))h_n,
    P_*(a,b)=h_min(a,b) [max(a,b)+(min(a,b)-1)/2].

Its all-size normalization, separate concavity, tripling, rank, and
replication proofs are in the
[first scalar note](../2026-10-20/research_note.md). The
[two-sector proof](../2026-10-20-truncated-algebras/two_sector_bound.md)
shows that it also satisfies both two-sector upper bounds.

Let S_m=sum_r P_*(r,m+1-r). The exact comparisons are:

| m | a | B | S_m | P_*(a,B) | S_m/P_*(a,B) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 5 | 10 | 52/3 | 1820/81 | 27/35 |
| 5 | 6 | 16 | 254/9 | 26936/729 | 10287/13468 |
| 6 | 7 | 24 | 380/9 | 13832/243 | 135/182 |
| 7 | 8 | 34 | 4820/81 | 543400/6561 | 19521/27170 |
| 5 | 7 | 15 | 254/9 | 27664/729 | 10287/13832 |
| 8, hypothetical | 9 | 46 | 6500/81 | 6792500/59049 | 729/1045 |

Every ratio is strictly below one. The largest is 27/35.
Thus no accepted inequality forces a point above P_*.

### Closed formulas for the target sums

These sums have useful exact forms:

    S_(2n)   = [(6n+1)(3n+1)/7] h_n,
    S_(2n-1) = [(18n^2-12n+1)/7] h_n.

One proof uses

    sum_(r=1)^n h_r = (3n+1)h_n/4,
    sum_(r=1)^n r h_r = (4n+3)(3n+1)h_n/28,

which follow directly by telescoping the recurrence.

## 3. Arbitrary copies would still pass this model

No arbitrary-copy extension is claimed for the finite maps. Suppose,
as a stronger hypothetical premise, that one could obtain

    P(a,kB) >= k sum_(r=1)^m P(r,m+1-r)             (R_m,k)

for every positive k. This would follow from actual shared-target copies
with no extra source-input cost per copy.

Every audited row satisfies the stronger exact comparison

    S_m < B h_a.

The respective ratios S_m/(B h_a) are

    162/175, 10287/11648, 1215/1456,
    292815/369512, 30861/34580,

with 3645/4807 for the hypothetical m=8 row. Since

    P_*(a,kB)=h_a[kB+(a-1)/2] >= k B h_a,

P_* satisfies (R_m,k) for every k. Thus simply obtaining more copies at
these same finite formats cannot refute this scalar model.

The endpoint homogeneous upper envelope is

    F(a,B)=K a^(1/3)(B+a/2)       (B>=a).

Combining it with (F_m) and the old lower bounds gives only

    K >= S_m/[a^(1/3)(B+a/2)].

Each of these lower bounds is weaker than the already available
K>=h_a/a^(1/3), because S_m<P_*(a,B)<h_a(B+a/2).
The same conclusion holds for the hypothetical copy limit using
S_m/(B a^(1/3)), by S_m<Bh_a.

## 4. A whole feasible family

Compatibility is not confined to a single point. Define

    L(a,b)=max(a,b)+(min(a,b)-1)/2,
    P_c(a,b)=c P_*(a,b)-(c-1)L(a,b),  1<=c<=21/20.

Equivalently P_c(a,b)=h_c(min(a,b))L(a,b), where
h_c(n)=c h_n-(c-1). These are formal scalar profiles; no tensor character
with these values is asserted.

They satisfy all of the following all-size rules.

1. **Positivity, symmetry and edges.** h_n>=1 gives P_c>=P_*>0, and
   P_c(1,b)=b.

2. **Separate concavity through zero.** On each positive axis L is convex:
   its slope is 1/2 before the diagonal and 1 afterwards. Thus
   cP_*-(c-1)L is concave. At the zero boundary, for b>=2,
   P_c(2,b)=(1+c/3)(b+1/2)<=2b because c<=9/5. The b=1 axis is linear.

3. **Shifted tripling.** For all a,b,
   L(a,3b+a-1)-3L(a,b) is zero if b>=a and is
   3(b-a)/2 if b<a. It is nonpositive. Subtracting this expression from
   c times the valid P_* tripling inequality proves the P_c inequality.

4. **Replication.** h_n/n^(1/3) is nondecreasing, as follows from
   (1+1/(3n))^3-(1+1/n)=(9n+1)/(27n^3)>0.
   Therefore h_c(n)/n^(1/3)=c h_n/n^(1/3)-(c-1)n^(-1/3)
   is also nondecreasing. Together with
   L(qa,qb)>=q L(a,b), this proves
   P_c(qa,qb)>=q^(4/3)P_c(a,b).

5. **Both two-sector bounds.** The established uniform estimate is
   (2P_*(a,b))^3/(a+2b-1)^4<=27/32.
   Since P_c<=cP_*, the corresponding ratio for P_c is at most
   (21/20)^3(27/32)=250047/256000<1.
   Input interchange gives the other orientation.

6. **The ordinary rank bound.** If both arguments are at least two, put
   R=min(a+2b-1,2a+b-1) and S=a+b-1. Then R<=5S/3, so the two-sector
   bound gives P_c(a,b)^3<=625 S^4/648<S^4.
   An argument equal to one is covered by the exact edge value.

7. **The three fixed-label product-filtration families.** These follow
   from separate concavity through zero by the established
   [equivalence theorem](../2026-10-20-concavity-equivalence/research_note.md).
   Consequently they also hold for P_c at every size.

8. **The finite diagonal ceilings.** Combining tripling and the
   two-sector bounds gives 6P_c(a,a)<=(6a-2)^(4/3), exactly as in the
   existing [finite amplitude note](../2026-10-20-koszul/finite_amplitude.md).

The new finite inequalities also hold for every c in this interval.
Indeed their gap is

    c[P_*(a,B)-S_m]-(c-1)[L(a,B)-sum_r L(r,m+1-r)].

The first bracket is positive and the second is negative in every row of
the table. For the stronger arbitrary-copy inequalities replace the two
source terms by B h_a and B; the same signs hold.

The homogeneous limits of this feasible family have amplitudes

    K_c=c/Gamma(4/3),   1<=c<=21/20.

This is an explicit nonempty interval of scalar endpoint models surviving
the new finite constraints and the listed old rules.

## 5. Precise closure conclusion

Any scalar deduction using only the rules above and the audited finite
inequalities must remain valid on P_*. This includes substitutions at
arbitrary positive integer sizes, nonnegative combinations, products,
and limit passages justified for the displayed explicit profiles.
The same holds for the hypothetical arbitrary-copy inequalities.

Hence this set of scalar rules cannot force a value strictly above P_*,
exclude t=3/4, or close the endpoint amplitude interval. This is stronger
than observing that a finite numerical optimizer did not find a violation:
an exact all-size feasible assignment is supplied.

The conclusion does not apply to a new tensor construction using more
information about the maps, an oriented inequality not represented by
these scalar rules, or a larger family of source formats.

## 6. Finite size guides, not exponent claims

For a=m+e and B=N=m(m+1)/2, exact rational comparisons give:

| Shared excess e | First m with S_m>N h_(m+e) | First m with S_m>P_*(m+e,N) |
| ---: | ---: | ---: |
| 0 | 4 | 53 |
| 1 | 22 | 71 |
| 2 | 38 | 88 |
| 3 | 54 | 104 |

The first column concerns a hypothetical arbitrary-copy limit; the second
concerns a single finite inequality. The verifier checks every smaller
positive m as well as each crossing, so these are exact first crossings.
No degeneration at these formats is claimed. Refuting P_* alone would
still be short of excluding every endpoint profile.

The conditional unbounded construction criterion remains unchanged.
The current finite maps are useful construction seeds, while their direct
scalar consequences leave the endpoint feasible.

## Verification and attribution

Run:

    python research/ai/2026-10-21-finite-character-closure/verify.py

All acceptance comparisons use rational arithmetic. The verifier checks
the table, copy-limit margins, sum formulas, first crossings, and finite
controls for the explicit P_c family. Universal claims rely on the
written proofs above.

The external character/entropy and replication inputs are OpenAI's
October 2 paper at revision fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb and
Uznanski, arXiv:2610.10494v2, as attributed in the linked repository notes.
The minimal profile and two-sector theorem predate this audit. The new
contribution here is the exact finite-format comparison and its explicit
scalar closure certificate. Review within the generating AI session is
not external independent certification.
