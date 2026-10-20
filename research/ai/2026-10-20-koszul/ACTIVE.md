# Active construction question

Goal active: prove an arithmetic exponent strictly below 9/4. No such bound
has been established. The user directed continued work beyond checkpoints.

Checkout `/home/cinna/matrix-mult-koszul-20261020`, branch
`research/koszul-and-scaling-20261020`, draft PR 1. Preserve the two historical
archives. Fetch the other branches before selecting a new substantial task.

Current mathematical gap: construct C(m,B_m) -> T_(m,k_m) along an unbounded
sequence of m with asymptotic overhead below 9/(7*cuberoot(2))-1. The precise
conditional exponent implication is in `all_dimension_targets.md`; its
stronger limiting-slope estimate is adopted from concurrent commit `cf79709`.

Completed exclusions in `source_obstructions.md`:

- Ordinary linear restrictions require asymptotically 100 percent overhead,
  after adopting the concurrent minimum-slice strengthening at `d2d505c`.
- Polynomial Y/Z changes preserving the shared binary-form coefficient
  structure require the same asymptotic overhead.
- Projected shared Koszul and linear equivariant shared Young/Pieri maps
  cannot reject this border-rank-B target, by the polynomial-matrix lemma.

The exact m=2 all-k and m=3,k=1 constructions are positive controls, not growth
sequences. The 32 m=4 real/complex fits found no certificate. Do not interpret
stalled optimization as a no-go theorem or rerun it unchanged as new research.

Next source investigation: unrestricted shared-factor degenerations, or a
nonlinear invariant of the convolution's orbit closure. The classical source
identification is Definition 2.3 of Ancona--Ottaviani,
[*Unstable hyperplanes for Steiner bundles and multidimensional matrices*](https://arxiv.org/abs/math/9910046):
the coefficient tensor of binary polynomial multiplication is their
boundary-format identity tensor, associated with a Schwarzenberger bundle.
Sections 2 and 4 were inspected. Their Theorems 2.4--2.6 explicitly assume
nonzero hyperdeterminant; they do not classify our degenerate padded target.
No new obstruction is inferred from those theorems. Investigate the boundary
carefully before importing a classification result.

The Chebyshev experiment is complete at its stated scope. See
`orthogonal_bases.md`: the degree-ordered orthogonal class has an all-size
obstruction, and a necessary permutation/center enumeration is exhaustive for
m=4,...,38. The m=39 discovery timed out. Independent small enumeration and
exact coefficient-normalized m=2,3 controls pass. Do not rerun unchanged
searches as progress. General shared linear combinations remain outside it.

Selected next question: does a singular shared-factor transformation preserve
a nontrivial limiting rational-normal-curve incidence condition on the source?
Ordinary structured flattenings can become vacuous when their own coefficient
maps degenerate. Any proposed nonlinear test must control that loss explicitly,
or yield an actual source construction. Merely importing a nondegenerate
Schwarzenberger classification does not answer this boundary question.

Other agents own full/off-leading Clebsch--Gordan and truncated-algebra source
searches (`f6f307c`) and the group-potential search (`f7aa680`). The scalar
agent's all-degree target/threshold work overlaps ours; retain attribution
and avoid counting the common formulas twice. See `docs/concurrent_research.md`.
