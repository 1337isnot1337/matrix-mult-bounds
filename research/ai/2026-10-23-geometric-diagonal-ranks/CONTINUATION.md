# Continuation record: geometric diagonal source ranks

Recorded October 23, 2026. Topic branch: research/geometric-diagonal-ranks-20261023.
Base main commit: bd03b9dadba03b1089595f03ff7a091ee9e7ddbc.

## Selection and concurrency

At selection there were 97 open PRs in the available search snapshot. The closely related active PR #207, head 09041022f0bb8dd2233eee95eec0017ee6998b1e, supplied the prior all-degree Toeplitz-block reduction and a quadratic rank recurrence. Its description explicitly left simultaneous defects of central Toeplitz blocks for degree at least three open. PR #171 handles binomial biforms; PR #186 handles the arbitrary-biform rank gap. This continuation does not replace, copy without attribution, or claim the discovery of those results.

Selected question: for the all-degree coefficient model, classify simultaneous Toeplitz rank defects in the nontrivial geometric-progression coefficient family, uniformly in the field characteristic, and export explicit kernel vectors.

## Result and scope

For any field and nonzero c,lambda, a>=2, 1<=d<a, let q=a mod(d+1). The cyclic-source slice of c*sum_(k=0)^d(lambda*x*z)^k has rank

    a^2 + a*d - E,  E=0 if q=0, otherwise E=(q-1)*(d+1-q).

Every central Toeplitz block has nullity min(l,d-l,q-1,d+1-q) for nonzero q and zero for q=0. The proof constructs basis vectors supported on pairs of periodic residue classes and scales them by lambda^(-i). The maximum simultaneous defect at fixed d is floor(d^2/4). These are all-field theorems from written elementary proofs, not a finite extrapolation.

Claim: AI-GEOMETRIC-DIAGONAL-RANKS-001, status proof-written-unreviewed; no independent human review or Lean formalization. The proof includes a self-contained reconstruction of PR #207's block lemma with credit to that PR.

## Reproduction and completed verification

From repository root, after installing root requirements:

    python research/ai/2026-10-23-geometric-diagonal-ranks/verify.py --output results/local/geometric-diagonal-ranks.json
    python research/ai/2026-10-23-geometric-diagonal-ranks/verify_charzero.py
    python -m unittest discover -s tests -p 'test_geometric_diagonal_ranks.py' -v

Completed offline local exact finite-field verification: 3,276 Toeplitz rank checks, 3,276 individual nullity checks, 1,692 kernel vectors, 225 independently reconstructed conserved-index block sums, and 75 literal unpermuted source coefficient matrices, over F2,F3,F5,F7,F11 with permitted ratios 1 and 2. Result PASS.

Completed independent characteristic-zero SymPy ranks in four parallel processes: 50 rational coefficient cases, with a=3..12, d<=6 and geometric ratio 2/3. Result PASS. The implementation does not import the finite-field verifier.

Completed focused unittest controls: three tests passed, including a corrupted vector rejected as outside the kernel. The rational regression has a separate Fraction elimination backend. These are internal checks; neither supplies independent mathematical review.

Repository-wide regression and historical replay were not completed in this offline local workspace. They remain required CI/replay gates, and any later branch changes require checks on their *current* head.

## Unresolved bottleneck

The rank theorem concerns one input slice, not a linear space of jointly low-rank slices. It neither gives a three-leg tensor degeneration nor bridges the source-rank defect to a characteristic-zero matrix multiplication target. The next substantive direction is to determine whether several geometric coefficient slices admit compatible joint kernel/row-space control or whether mixing their parameters destroys the defect. An exact tensor construction would still have to verify *every* coefficient of all three source-to-target maps, auxiliary costs and asymptotic growth before it could establish an exponent below 9/4.

Do not continue by merely enumerating more residues or finite characteristics: equations (1)-(10) in proof.md already cover all sizes and every field in this family. Preserve the archived research paths and PR #207 attribution.