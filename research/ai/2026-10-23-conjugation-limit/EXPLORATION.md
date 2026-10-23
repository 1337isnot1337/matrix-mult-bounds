# Two attempted escapes from the first conjugation obstruction

October 23, 2026. Finite exact exploratory computation. This note adds no
full-target construction, exponent improvement, or separate theorem claim.
The three registered claims retain their stated scope.

## Completed families

All source indices use the normalized basis and conventions in
[proof.md](proof.md). Put A=H_{0,0,0} and B=H_{6,3,3}. The following
experiments retain all 112 source slices and permit all polynomial
first-leg cancellations when forming the saturated limit.

| Family | Scalar-action subspace dimension | Principal coordinate pairs screened | Pairs needing full re-saturation | Surviving pairs |
| --- | ---: | ---: | ---: | ---: |
| g^-1 H g, g=(I+zA)(I+zB) | 29 | 6,216 | 0 | 0 |
| U^-1 H U, U=I+z(A+B) | 6 | 6,216 | 221 | 0 |

Both long maps have singular leading matrices in both families. The
first family uses two noncommuting square-zero factors. Its two leading
map ranks are at most 16. The second family uses a nonnilpotent sum;
its leading map ranks are at most 6 and 32. Thus these are two-sided
experiments, outside the one-regular-long-map hypothesis. The original
one-sided moving-unit probe was discarded because that known hypothesis
already applies to it, and is not counted as new research progress.

The first family has a scalar-action space on coordinates 0 through 27
and coordinate 87. Every principal compression has projected dimension
at least 108 modulo 1009, so the original loss-of-nine criterion already
excludes all of them. The general restriction bound below strengthens
the necessary loss for this family to 29.

For the second family, the six scalar coordinates are 19, 23, 27, 84,
88, and 92. Exactly 221 coordinate pairs have projected modular rank at
most 103, including three pairs of rank 85. These pairs therefore require
re-saturation; a raw leading-coefficient projection would be insufficient.
The full re-saturation was computed for all 221 pairs, with all polynomial
coefficients replayed exactly. Every resulting limiting space has an
explicit invariant coordinate subspace whose dimension is not divisible
by ten. None can contain a left/right equivalent copy of the full target.
Indeed, an invertible target slice would preserve that subspace and have
an inverse preserving it, after which the target would give a Mat10-module
on a vector space of dimension not divisible by ten.

The other 5,995 coordinate pairs in that family have modular dimension
at least 104 and are excluded by the loss-of-nine condition. Modular ranks
are lower bounds on complex dimensions, so this screening cannot omit
any complex projected space of dimension at most 103.

## Whole-subspace restriction bound

The scalar-action argument can use all of the surviving scalar subspace.
Suppose its original dimension is s, and the input compression has
codimension two. Its inverse image W under the input map has dimension
at least s-2. Every projected leading matrix restricts to W through a
single fixed map, so the restriction space has dimension at most one.
At most ell recovered leading directions can raise that dimension to
at most 1+ell.

For Mat10 tensor I11, identify each vector with a 10 by 11 matrix. If a
subspace W has dimension d, let a be the dimension of the span of all
columns of all its vectors. Then d <= 11a. The kernel of the restriction
map Mat10 -> Hom(W,C110) consists exactly of matrices annihilating that
column span, so the image dimension is 10a. Independent invertible changes
on the two long factors preserve this dimension bound. Consequently a
successful compression requires

\[
\ell\ge 10\left\lceil\frac{s-2}{11}\right\rceil-1.
\]

For the original s=12 this remains nine. For the two-factor s=29 family
it becomes 29. This is a refinement of the same elementary restriction
argument, not a claimed tensor construction.

## Exact computation and retained scope

[two_sided_escapes.py](two_sided_escapes.py) rebuilds the literal source,
computes each complete polynomial family, performs rational polynomial
row reduction, and independently replays the returned transformations.
Distinct leading pivots certify 112 independent limiting matrices.
All invariant-subspace equations are checked using integer zeroes, hence
over Q and C. Invariance is never inferred from a modular computation.

For the second family, an exact annihilating polynomial for N=A+B is

\[
x^{15}-12x^{13}+56x^{11}-127x^9+141x^7-65x^5+6x^3.
\]

It supplies a polynomial numerator for (I+zN)^-1 with common denominator
1-12z^2+56z^4-127z^6+141z^8-65z^10+6z^12. The script checks the inverse
identity over Q[z] before forming any slice limits. Multiplying every
slice by this common denominator does not change its Laurent-field span;
the first map can absorb that scalar. No inverse series is truncated.
No assertion of minimality of the annihilating polynomial is needed.

To reproduce both completed experiments from the repository root:

```sh
python research/ai/2026-10-23-conjugation-limit/two_sided_escapes.py --output results/local/conjugation-limit/escape-exploration.json
```

The retained report is
[escape-exploration.json](../../../results/conjugation-limit-2026-10-23/escape-exploration.json).
It records the two complete screening histograms and all 221 exact
invariant coordinate witnesses. A complete M(10,10,11) tensor identity
remains the acceptance condition for a positive result. No such maps
were obtained. Arbitrary noncoordinate compressions and other singular
families remain outside this finite search.
