# When the balanced quadratic rank defect occurs

October 23, 2026. Owner-directed Codex research. Written and unreviewed;
same-session checks are not independent mathematical review. This package
does not improve the matrix-multiplication exponent.

The [prior kernel-index package](../2026-10-23-quadratic-kernel-indices/README.md)
proves four-value containment for a balanced quadratic-in-z source block.
The present [proof](proof.md) identifies its one-unit rank defect with the
order of a line bundle on a bidegree-(2,2) curve, and settles its
attainment over F2 for every size a>=3:

    rank a^2+2a-1 occurs  iff  gcd(a+1,30)>1.

The complete nonzero rank set for quadratic-in-z slices over F2 is

    {a^2, a^2+a, a^2+2a}
       union {a^2+2a-1 : gcd(a+1,30)>1}.

Thus a=6,10,12 exclude the one-unit defect, while a=3,4,5,7,8,9
admit it. This concerns the quadratic-in-z family; for a>3 it does not
classify arbitrary biforms or the full cyclic source.

## Geometric statement

Over any field, divide the coefficient triple of u+zv+z^2w by its
common gcd. If its primitive degree is two and there is no fixed
K-rational homogeneous z-root, homogenize to a curve C of bidegree
(2,2) and put L=O_C(1,-1). The proof shows that L is nontrivial and

    rank R_(a,a)=a^2+2a-1  iff  L^(a+1) is trivial.

An explicit Laurent-monomial calculation identifies the recurrence
coefficient kernel with H0(C,L^(a+1)), without binomial factors or
division by two. The section criterion covers integral singular curves,
two (1,1) components, and a doubled (1,1) curve as well as smooth
genus-one curves. The doubled case has order p in characteristic p and
infinite order in characteristic zero.

For F2, normalization controls the singular cases, while an elementary
rational-point argument and Riemann--Roch bound the smooth case. Three
explicit polynomial recurrence vectors certify exact orders 2, 3, and
5. The all-size proof does not infer periodicity from the finite profiles.

## Exact finite controls

[verify.py](verify.py) reconstructs all 264 primitive binary triples of
coefficient degree two without a fixed F2 root. Their exact action under
PGL2(F2) on each coordinate gives 16 orbits, with all 576 representative
transforms checked. The saved
[report](../../../results/quadratic-torsion-2026-10-23/controls.json)
records every orbit member, the exact small-power kernel polynomials,
and 176 comparisons against the literal crossed source matrix at
a=3,...,15 excluding the previously tested a=6,10.

There are 64 recorded cohomology controls for n=2,3,4,5; 32 are
additional small matrices at a=1,2, used only for cohomology and never
as source ranks outside the allowed range. The first nonzero powers in
these controls have orbit counts 9,4,2,1 for n=2,3,4,5, respectively,
and triple counts 96,96,36,36. These are finite results, separate from
the all-size proof.

From the repository root, reproduce the report and focused tests with:

```sh
python research/ai/2026-10-23-quadratic-torsion/verify.py --output /tmp/quadratic-torsion-controls.json
python -m unittest discover -s tests -p 'test_quadratic_torsion.py'
```

The focused tests replay the saved report, check the coordinate action
on every bidegree-(2,2) basis element, validate the three prime-order
witnesses, reject a corrupted witness, and verify local source hashes.
The previous a=6,10 negatives are preserved outside this package and
are not rerun or recounted as new checks.

## Provenance and limits

[sources.json](sources.json) pins the merged kernel-index prerequisites,
the literal source, the reused exact matrix constructors, and dated
primary-source snapshots for the external geometry. The original
source construction and general bundle formula retain their prior
credit. The new results are a torsion interpretation and the binary
attainment classification, with no historical-priority claim.

The line bundle is fixed by the particular biform. Attainment over
other fields requires an argument for that field; the binary conclusion
is not an all-field order bound. Review status remains written and
unreviewed regardless of successful finite checks or CI.
