# Active construction question

Goal active: prove an arithmetic exponent strictly below 9/4. No such bound
has been established. The user directed continued work beyond checkpoints.

Checkout `/home/cinna/matrix-mult-koszul-20261020`, branch
`research/finite-amplitude-20261020`. PR 1 was merged at `1c8b4f1` and PR 8
at `daeae6e`; both finished branches were removed locally and remotely.
Preserve the two historical archives.
Fetch the other branches before selecting a new substantial task.

Current mathematical gap: construct C(m,B_m) -> T_(m,k_m) along an unbounded
sequence of m with asymptotic overhead below 9/(7*cuberoot(2))-1. The precise
conditional exponent implication is in `all_dimension_targets.md`; its
stronger limiting-slope estimate is adopted from concurrent commit `cf79709`.

Completed exclusions in `source_obstructions.md`:

- Ordinary linear restrictions require asymptotically 100 percent overhead,
  after adopting the concurrent minimum-slice strengthening at `d2d505c`.
- Polynomial Y/Z changes preserving the shared binary-form coefficient
  structure require asymptotically 50 percent overhead.
- The later biform proof in `arbitrary_shared_basis.md` strengthens this to
  all constant shared GL(m) bases, and regular shared maps with invertible
  limit, with asymptotically 50 percent overhead. It also closes the other
  worker's constant-G graded ansatz at the desired cost.
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

Concrete construction experiment now selected: add nonzero shared weights
w(X_i)=i and target monomial weights w(Y_(a,b))=-a+gamma*(a+b),
w(Z_(c,d))=-c+gamma*(c+d)-gamma*(m-1), with gamma>m. Allow a constant dense
shared basis before those weights. This prescribes the negative-weight
coefficients to zero and the zero-weight coefficients to the target, while
positive-weight coefficients are free. It is distinct from the excluded
constant-G search, which has zero shared weights. Exact coefficient replay
is required for acceptance; small numerical residuals do not suffice.

Update: that concrete dominant-degree region is now excluded by Sections 5-6
of `arbitrary_shared_basis.md`. Its first-stage blocks have no zero divisors,
so the broadened catalecticant proof applies. Section 7 also excludes
0<alpha<=beta by an explicit support cover for the X_0 slice. Ten completed
floating fits are retained as diagnostics, with no exact certificate.
Do not rerun either excluded region. The subsequent exact covers in
`intermediate_weights.md` give asymptotic overhead at least 2-alpha/(2*beta)
for beta<=alpha<=2*beta. The balanced (2,1) direction requires
B>=k*(N+floor(m/2))-(m-1); it excludes the m=4,B=10k target for k>=2,
including the previously selected k>=53 target, but leaves k=1 open.
The scalar worker already owns mixed-direction numerical fitting; avoid
duplicating its completed runs. Our next question is an analytic condition
on the remaining larger slopes or on arbitrary singular shared maps.

The m=4,B=10,(alpha,beta)=(5,2) pilot completed 11 nonaffine shared
permutations with arbitrary dense P,Q and 600 function evaluations each.
No exact witness was found. All final arrays and full-tensor diagnostics are
retained; see `permutation_probe.md`. Do not rerun these unchanged fits.

Selected next question: can a finite tensor construction prove (H4) in
`finite_amplitude.md`, the universal near-endpoint inequality
P(4,4)>=(13/12)*P_*(4,4)=5005/486? The existing tripling and two-sector
constructions would then imply the exact rational bound omega<=2249/1000.
The premise is unproved. A dimension screen excludes using only independent
matrix products extracted from powers of the symmetrized C(2,2) or C(3,3)
to cross their corresponding endpoint ceilings. C(4,4) is the first
diagonal not eliminated by that screen; no extraction has been constructed.
The concrete selected target (H106) is a degeneration from the tensor product
of all six leg permutations of C(4,4) to M(106,106,106). It independently
implies omega<=2.249, by the exact certificate 3816^2249>22^6000. Source and
target leg dimensions are 12544 and 11236, respectively. Applying the group
worker's abelian opposite-relation argument now excludes coordinate
injections with diagonal weights: a single square target is at most M49.
Combining that argument with Holder also closes all-power coordinate
extractions into direct sums of matrix products at a=4. The remaining
H106 investigation must allow non-coordinate maps and cancellation. This
does not construct H106 or rule out its unrestricted form.

Other agents own full/off-leading Clebsch--Gordan and truncated-algebra source
searches (`f6f307c`) and the group-potential search (`f7aa680`). The scalar
agent's all-degree target/threshold work overlaps ours; retain attribution
and avoid counting the common formulas twice. See `docs/concurrent_research.md`.

The recoupling package merged through PR #16 at e41c77d after current CI;
its completed local and remote branch was removed. The exhaustive grouped
binary search covered 1,797,505 supports at a=4 without a scored gain.
The subsequent exact A_2 -> M(2,3,4) integer mixed-map certificate is in
`../2026-10-20-cyclic-mixed-map/README.md`. It does not improve P_*(2,2).
Current construction question: can its cancellations be extended to larger
cyclic targets or used to initialize a singular construction? Larger
ordinary small-source pilot fits are discovery only, not exclusions.

The exact M(2,3,4) construction merged through PR #18 at 9a4ee3d after
current CI; its completed local and remote branch was removed. The first
A_3 -> M(3,5,9) pilot found no certificate in eight real starts. Claim 047
now excludes full-capacity direct sums of square targets at all powers
using closed-orbit theory; it does not address the smaller H1100/H106
targets or provide an asymptotic loss. Continue on unrestricted singular
constructions, avoiding ordinary H1100 maps and full-capacity square aims.

Claim 048 also rules out a general complex degeneration of the central
4-by-4-by-4 multiplicity block to M2, using exact smooth-cubic identities
and polystability. This strengthens claim 045 but does not cancel the
scalar companion or rule out joint/higher-power extraction.
