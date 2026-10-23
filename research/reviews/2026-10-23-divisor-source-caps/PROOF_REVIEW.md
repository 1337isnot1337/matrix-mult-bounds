# Internal audit of the divisor source-space cap

Review target: PR [148](https://github.com/1337isnot1337/matrix-mult-bounds/pull/148),
commit `673710d3a4284d88e4d24350681b26912831bf7a`,
`research/ai/2026-10-23-divisor-source-caps/proof.md`.
The source is pinned even if that branch subsequently changes.

Reviewer: OpenAI Codex in a separate owner-directed session. This is an
internal consistency audit, not independent mathematical review or
formalization. The reviewed package is not incorporated by this audit.

## Conclusion and hypotheses

No gap was found in the two stated complex-field arguments. For every
integer `a>=2` and proper positive divisor `d` of `a`, the largest dimension
of a source subspace whose slices have rank at most `q` is `ad` when
`a(a+d-1)<=q<a(a+d)`. For the stated square parameter target with
`R=mn<=N=a^2(2a-1)` and `k=N-R`, a regular long map of limiting rank `R-c`
is excluded if all three strict conditions hold:

```
m > ad,       n+2k+c < a(a+d),       a^2 > 3k+c.
```

This conclusion retains the pinned biform block lemma and its external
bundle-splitting input. Claims `AI-DIVISOR-SOURCE-CAP-001` and
`AI-DIVISOR-LONG-EXCLUSION-002` remain written and unreviewed in the
repository's evidence terminology. No target construction, smaller
exponent, nondivisor cap, or new A4 cutoff follows from this audit.

## Arbitrary subspaces really reduce to coordinate subspaces

The weight `i+a*k+a*(2a-1)*s` uniquely encodes every coordinate in the
source's stated index ranges. Substitution in the full coefficient rule
`F_(H-j,b+c,L-r)` gives the displayed row weight plus column weight
exactly. Negative row or column weights cause no difficulty for nonzero
`t`, when all diagonal factors are invertible.

Order basis coordinates by increasing weight before taking reduced row
echelon form. Entries before each row's pivot are zero. After dividing
the transformed row by the pivot power, every remaining exponent is
nonnegative and its constant term is precisely that pivot vector. For
each fixed linear combination, every forbidden minor vanishes for all
nonzero complex `t`; it is a polynomial, so it vanishes also at zero.
The pivot vectors are distinct, preserving dimension. This argument
requires neither invariance of the original space nor a continuously
chosen basis for a rank stratum.

At a middle coefficient `k`, the disjoint `b+c=k` blocks give monomial
rank `a^2 min(k+1,a,2a-1-k)`. Because a proper divisor satisfies
`d<=a/2`, the ceiling is strictly below `2a^2`. Only the two middle
extremes survive. A sum of one coordinate from each has disjoint row
and column blocks and rank `2a^2`, so only one extreme occurs.

## Wrapped divisor pairs and the sharp strip

Translation by `(d,d)` on the square grid has orbit length `p=a/d`.
Thus there are `ad` orbits. Two distinct members differ by nonzero
multiples of `d` on both axes, even when the two axes wrap at different
steps. Removing the coordinatewise common monomial gives either
`1+x^(alpha*d) z^(beta*d)` or `x^(alpha*d)+z^(beta*d)` with both
`alpha,beta` between one and `p-1`.

Multiplication by the removed monomial only translates the nonzero
output row and column indices. No truncation occurs: the original
output ranges contain every convolution of a source exponent below
`a` with an input exponent below `a`. Residue classes of `j,H` and of
`L,r` give `d^2` blocks. Both input ranges have exactly `p` elements in
every residue; every required output index through `2p-2` is present.
An extra output index `2p-1`, when present, has zero entries. Each
nonzero block is therefore literally the smaller biform matrix.

Both reduced binomials have coefficient rank two, so the adopted
complex biform gap gives total rank at least
`d^2(p^2+p)=a(a+d)`. This forbids two coordinates from one orbit and
proves the upper dimension bound. The `d`-row strip has `ad` independent
coordinates and only `a(a+d-1)` possible nonzero columns, proving
attainment throughout the closed lower and open upper interval. No
assertion about the generic rank of that strip is needed.

## Polar maps do not invalidate the regular kernel correction

Write the complete degeneration as `B M(F(X)) C`, with target constant
term `Xi(X)=X tensor I_n`. A scalar Laurent balancing makes `F` regular
with nonzero `F_0`, while leaving regular `C` unchanged. Set
`Y_X=M(F(X))C`, `D=Y_I`, and `G=BD=I_R+O(t)`. The replacement
`B <- G^(-1)B` has the same target limit and makes `BD=I_R` exactly.
Both `Y_X` and `D` are regular; `Z_X=BY_X` is regular because the
complete degeneration has no negative coefficients.

The projection `P=I_N-DB` need not be regular. The required statement is
instead that `W_X=Y_X-D Z_X` is regular. Over the Laurent field,
`P` has image `ker B` and rank `k`. Thus every `(k+1)`-minor of `W_X`
vanishes generically and, by regularity, at zero. This avoids assuming
that a polar projection itself can be specialized.

At zero, `M(F_0(X))C_0=D_0 Xi(X)+W_X(0)`. For rank-one `X`, the right
side has rank at most `n+k`. Since `C_0` loses `k+c` source directions,
the full lifted slice has rank at most `n+2k+c`. If that lift is nonzero,
the source minimum `a^2` also forces
`rank(D_0 Xi(X))>=a^2-2k-c>k`.

Since rank-one matrices span the parameter space and `F_0` is nonzero,
some `u,v` have nonzero lift. Fix that `u`. For every nonzero `v`,
`D_0((uv^T) tensor I_n)` has the same image as
`D_0(u tensor I_n)`, because `v^T tensor I_n` is surjective. A nonzero
`v` in the kernel of the lift would force this rank to be at most `k`,
a contradiction. The entire `m`-dimensional ruling therefore injects
into the bounded-rank source locus, contradicting `m>ad`. The argument
uses no injectivity assumption on the full leading first map.

For `a=4,d=2,m=10,n=11,k=2`, the rank-ceiling inequality requires
`c<9`, while the active-ruling inequality requires `c<10`. Accordingly
`c<=8` is the established boundary; the argument does not exclude `c=9`.

## Dependency and evidence boundaries

The source minimum is the triangular-minor proof in
`research/ai/2026-10-20-koszul/cyclic_finite_target.md`, section 2.
The biform gap is section 1 of
`research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md`.
Its kernel-bundle argument uses a pointwise full-row-rank polynomial
matrix after removing the homogeneous common factor, including infinity.
The kernel embeds in a trivial bundle, has degree `-ad`, and splits as
`sum O(-mu_j)` with nonnegative `mu_j` and sum `ad`. Twisting and taking
sections yields the stated rank formula and its gap. The splitting
input is Grothendieck, *Sur la classification des fibres holomorphes sur
la sphere de Riemann*, Theorem 2.1, printed page 126, in the
[primary scan](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-25.pdf).
The theorem statement was checked against that scan; its full proof is
not independently reproved here.

PR129 retains credit for torus specialization and active rulings, and
PR113 for the regular kernel correction. The reviewed proof reconstructs
those methods, so their unmerged files are not extra proof premises.
PR171 separately proposes an elementary binomial rank formula. This
audit does not adopt it, remove the pinned splitting dependency, or
extend the field of the reviewed theorem.

## Independent finite controls

The adjacent `audit.py` imports no implementation from PR148. It builds
the literal padded biform matrices and uses SymPy's exact rational-domain
rank backend. It checks every pair within every divisor orbit for
`2<=a<=6`, using unequal nonzero coefficients `1,-2`: 237 pairs across
eight `(a,d)` cases. This includes different wraparound directions and
nonzero common monomial factors, rather than only normalized pairs.
All meet the required rank threshold. There are also 67,170 literal
row-plus-column weight identities for `2<=a<=6`.

Two explicit rational Laurent examples check regular corrections at a
regular and a polar kernel projection. These examples are linear-algebra
controls, not source degenerations. Boundary controls recover rank 34
for the stated nondivisor pair and exclude exactly `c=0,...,8` in the
inherited A4 inequalities. The frozen
[control record](../../../results/divisor-source-cap-review-2026-10-23/controls.json)
is replayed by `tests/test_divisor_cap_review.py`, which also verifies
the bytes of the two local proof dependencies.

From the repository root, with the maintained requirements installed:

```sh
python research/reviews/2026-10-23-divisor-source-caps/audit.py
python -m unittest discover -s tests -p 'test_divisor_cap_review.py' -v
```

These checks support the audit but do not prove its all-size statement.
The proof target, Git blob and SHA256, and inherited source hashes are
in `sources.json`. Repository-wide validation is recorded separately;
no full-suite pass is inferred from these focused controls.
