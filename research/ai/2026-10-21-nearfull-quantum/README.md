# All diagonal weights for two prescribed quantum families

This package proves a finite-family obstruction. It concerns the explicit
regular families from `Q(4,2)` to format `(9,6,6)` and from `Q(5,4)` to
format `(16,16,16)` constructed in `quantum.py`. No diagonal Laurent
weighting of either family, followed by any further tensor degeneration,
can give `M(3,2,3)` or `M(4,4,4)`, respectively.

The scope is the two prescribed families. The exact ordinary
`Q(5,4) -> M(4,4,4)` construction in the separate paired-construction
package uses different subspaces and is fully consistent with this result.
This package does not improve the matrix multiplication exponent.

## 1. Source, target, and prescribed maps

Over the complex numbers, use

\[
Q(n,m)=\sum_{p,q=0}^{n-1}\sum_{y,v=0}^{m-1}
A_{pq}B_{y,q+v}C_{p+y,v}.
\]

Its format is `(n²,m(n+m−1),m(n+m−1))`. Put `n=N+1` and
`h=N+m−1`. Reverse the convolution-output coordinates, so a summand
has local coordinates

\[
(p,q),\quad(y,h-q-v),\quad(h-p-y,v).
\]

The exact rational maps over `Q(q)` are obtained from the maintained
unequal-source Clebsch–Gordan maps in
`../2026-10-21-narrow-quantum/quantum.py`. A coordinate of a
Clebsch–Gordan component is labelled `(k,l)`: the component has highest
degree `u+v−2k`, and `0≤l≤u+v−2k`.

For the first leg retain every component with `k≥1`. For the two long
legs retain the following rows:

| Case | Root order | First-leg degrees | Long-leg retained rows |
|---|---:|---|---|
| `N=3,m=2` | 8 | `4,2,0` | Degree 5: `l=2,3`; degree 3: all rows |
| `N=4,m=4` | 12 | `6,4,2,0` | Degree 10: `l=5`; degree 8: `l=3,4,5`; degrees 6 and 4: all rows |

These selections specify rational subspaces. They do not presume that a
quantum component is a matrix multiplication tensor.

Within each weight `k+l`, `dvr_limit` chooses a pivot of minimum
cyclotomic valuation, normalizes it, and clears its column in every
other row. The retained rows are generically independent. At each step
the pivot has minimum valuation among the remaining entries, so the
normalized row is regular; the unprocessed rows remain subject to the
same next-pivot rule. Previously normalized rows remain regular when
cleared by a new regular row. The resulting matrix has an identity
pivot submatrix and all entries regular at the chosen root. Thus its
specialization has the required full row rank.

Each resulting local matrix acts on the original constant tensor
`Q(N+1,m)`. Direct contraction produces a regular tensor family
`T(q)`. The result files include every rational local row, pivot
column, tensor coefficient, cyclotomic valuation, and leading residue.
The files can be regenerated without numerical optimization.

Write `π=Φ_L(q)`, where `L` is the stated root order, and choose a
primitive root `ζ`. Since `Φ_L'(ζ)≠0`, the equation `π=t^D` defines a
formal local path for any positive integer `D`. A diagonal weighting
assigns an integer `w_{a,i}` to coordinate `i` of leg `a`. If tensor
coefficient `s=(i,j,k)` has valuation `v_s`, its weighted exponent is

\[
Dv_s+w_{1,i}+w_{2,j}+w_{3,k}.
\tag{1}
\]

We consider every choice for which (1) is nonnegative at every
nonzero generic coefficient. The initial tensor `F` consists exactly
of the terms where (1) vanishes, with their exact leading residues.

## 2. A general balanced-support lemma

Let `V=V₁⊗V₂⊗V₃`, with `dim(V_a)=d_a`, and let
`H=SL(V₁)×SL(V₂)×SL(V₃)`. Let `T(π)` be a fixed regular tensor family,
and assume the support of `T₀=T(0)` admits a probability distribution
whose marginal on each leg is uniform.

**Lemma.** Suppose `F` is an initial tensor obtained by any feasible
weighting (1). If `F` degenerates under the full product of general
linear groups to a nonzero `H`-polystable tensor `M`, then `T₀` also
degenerates to `M`.

Here polystable means that the affine `H` orbit is closed. The
conclusion allows arbitrary further changes of basis and singular
degenerations after taking the weighted initial tensor.

**Proof.** Write

\[
\mu_a=\frac1{d_a}\sum_iw_{a,i},\qquad
\tau=\mu_1+\mu_2+\mu_3.
\]

Average (1) over a distribution with uniform marginals supported on
the valuation-zero terms. This gives `τ≥0`. Define trace-zero weights
`\widetilde w_{a,i}=w_{a,i}−\mu_a`; a common positive multiple makes
them integral and hence defines an `H` one-parameter subgroup.

For every supported term of `F`, the total weight for the opposite
one-parameter subgroup is

\[
-\sum_a\widetilde w_{a,s_a}=Dv_s+\tau.
\tag{2}
\]

If `τ>0`, all these weights are positive. Thus this subgroup sends
`F` to zero. The nullcone is closed and stable under the full general
linear group, so `F` cannot degenerate to nonzero polystable `M`.

If `τ=0`, the opposite subgroup in (2) sends `F` to the tensor `F₀`
formed by its valuation-zero terms. On the other hand, applying the
subgroup with weights `\widetilde w` to `T₀` also gives `F₀`, because
the feasible exponents of its terms are their total original weights.
Consequently `F` and `T₀` have identical values for every polynomial
`H` invariant.

For completeness, the passage from full general linear degeneration
to the closed `H` orbit requires a scalar normalization. Take a
convergent orbit sequence `g_jF→M`. Over the complex numbers write
its action as `c_jh_j`, with `c_j∈C*` and `h_j∈H`, by extracting the
determinant roots in each leg. Choose a positive-degree homogeneous
`H` invariant `f` with `f(M)≠0`; such an invariant exists because
`M` is nonzero and polystable. Then

\[
c_j^{\deg f}f(F)\longrightarrow f(M)\ne0.
\]

It follows that `f(F)≠0`, and after a subsequence `c_j→c≠0`.
Therefore `c⁻¹M` belongs to the `H` orbit closure of `F`.
It is closed and is the unique closed `H` orbit in that invariant
fibre. Since `T₀` has the same invariants, its `H` orbit closure
contains `c⁻¹M` as well. This proves the claim. ∎

The invariant-fibre and closed-orbit facts used here are standard
affine geometric invariant theory over `C`; see Hoskins [H13],
the discussion of the affine quotient on page 2 and Theorem 4.2.
The averaging and common-face argument above are the new deduction
used in this package. Uniform marginals alone are not asserted to
imply polystability of `T₀`.

## 3. Exact finite certificates

The two files `N3-m2-balanced.json` and `N4-m4-balanced.json` give
rational probabilities on generic coefficient indices. Every
selected index has valuation zero. The verifier checks positivity,
total mass one, and every individual marginal using rational
arithmetic.

The obstruction is the first Koszul flattening, using the full target
dimensions in each case. The verifier constructs its signed
coefficient matrix directly over the cyclotomic number field and
splits it by exact additive weights. It independently builds the
ordinary matrix multiplication target over `Q`.

| Source family | Generic coefficients by valuation | Balanced positive support | `K₁` of `T₀`, legs A/B/C | `K₁` of target, legs A/B/C |
|---|---|---:|---|---|
| `Q(4,2)` to `(9,6,6)` | `v=0:40`, `v=1:7` | 18 | `54,52,52` | `54,54,54` |
| `Q(5,4)` to `16³` | `v=0:240`, `v=1:146`, `v=2:23` | 42 | `255,255,255` | `256,256,256` |

Koszul rank cannot increase under tensor degeneration. Thus neither
`T₀` can degenerate to its target. The lemma rules out all feasible
diagonal Laurent weights of each prescribed family, including
arbitrary further degeneration to that same target.

Matrix multiplication is polystable in these full intrinsic formats.
Indeed, for `M(N,m,N)` in its standard orthonormal basis, the three
flattening Gram matrices are

\[
mI_{N^2},\quad NI_{Nm},\quad NI_{Nm}.
\]

Dividing by its squared norm `N²m` gives the uniform density matrix
on every factor. The moment map for `H` therefore vanishes, and the
Kempf–Ness theorem gives a closed orbit [H13, Theorem 4.2]. The square
case is also stated explicitly in Bürgisser–Ikenmeyer [BI15,
Corollary 4.9]. No assertion of polystability in a larger padded
format is used.

## 4. A face that passes `K₁` but is unstable

One sampled `Q(5,4)` face has all three `K₁` ranks equal to 256, so a
Koszul-only search would retain it. It is still excluded by the
general lemma. It also admits a particularly small direct witness.

Take `D=27` and, on each of the three legs, the coordinate weights

\[
(0,5,-4,10,1,-8,15,6,-3,-12,11,2,-7,7,-2,3).
\]

The resulting face has 146 nonzero coefficients. Assign the following
trace-zero weights on each leg:

\[
(3,1,3,-1,1,3,-3,-1,1,3,-3,-1,1,-3,-1,-3).
\]

Every supported coefficient then has total weight 1 or 7, so the
corresponding `SL₁₆³` one-parameter subgroup sends this tensor to
zero. `verify.py` checks every coefficient and every trace. This
example is illustrative; the all-weight theorem does not depend on
the finite random search that first found it.

## 5. Reproduction and remaining scope

Run from the repository root:

```sh
python research/ai/2026-10-21-nearfull-quantum/verify.py \
  --output results/nearfull-quantum-2026-10-21/certificate.json
python -m unittest discover -s tests -p 'test_nearfull_quantum.py'
```

The first command rebuilds the rational local maps and complete tensor
contractions, then recomputes the exact certificates. `--stored`
checks the finite certificate against the stored contractions.

Changing the selected rational subspaces, making different regular
changes of basis before assigning weights, adding an auxiliary
tensor, or using a different singular family remains outside this
result. The scalable fixed-inner-dimension construction needed by the
correction-budget theorem remains open.

### External sources

- **[H13]** Victoria Hoskins, *Stratifications associated to reductive
  group actions on affine spaces*, 2013 publisher manuscript,
  DOI `10.1093/qmath/hat046`.
  <https://userpage.fu-berlin.de/hoskins/strat_affine.pdf>.
  Used for affine invariant fibres, closed orbits, and the
  Kempf–Ness theorem, with complex reductive groups and unitary
  maximal compact action.
- **[BI15]** Peter Bürgisser and Christian Ikenmeyer, *Fundamental
  invariants of orbit closures*, arXiv:1511.02927v2, 1 December 2015,
  Corollary 4.9. <https://arxiv.org/html/1511.02927v2>.
  Used only for the external polystability fact for square matrix
  multiplication.

The quantum coefficient conventions and generic source identities
are inherited from the separately documented maintained packages.
The all-weight deduction and the two exact applications are AI-derived
work in this repository. Computational replay does not establish an
independent mathematical review.
