# Matrix multiplication bounds

[![Verification](https://github.com/1337isnot1337/matrix-mult-bounds/actions/workflows/verify.yml/badge.svg?branch=main)](https://github.com/1337isnot1337/matrix-mult-bounds/actions/workflows/verify.yml)

A research workspace seeking a rigorously supported improvement below the matrix multiplication exponent $\omega\le9/4$.

**No smaller exponent is established here.** The repository contains exact tensor constructions, obstruction arguments, finite searches, numerical experiments, and analyses of possible routes to an improvement. General local proofs remain written and unreviewed unless their records explicitly state otherwise. Passing tests is not independent mathematical review or Lean formalization.

This overview covers the research available in this checkout as of **October 21, 2026**. Topic branches can contain work not yet merged into `main`. The badge above reports `main`, not every branch or local experiment.

## Start here

- **Understand the goal:** [problem and computation model](docs/problem.md), [external 9/4 route](docs/nine_fourths_route.md), and [literature](docs/literature.md).
- **Find results and their limits:** [research status](STATUS.md) and the [claim ledger](research/claims.json).
- **Choose work:** [research directions](docs/research_directions.md), [active investigations](research/ACTIVE.md), and [contribution rules](CONTRIBUTING.md).
- **Check evidence:** [verification limits](docs/verification.md), [attribution](PROVENANCE.md), and the dated reports under [`results/`](results/).

## Research map

### 1. Scalar profiles, filtrations, and asymptotic growth

The [initial analysis](research/ai/2026-10-20/research_note.md) constructs a pointwise-minimal two-variable profile for a stated scalar relaxation. The growth recurrence comes from the external proof; the repository analyzes the matching profile and its constraints.

The [product-filtration result](research/ai/2026-10-20-concavity-equivalence/research_note.md) identifies three fixed-label inequality families with separate concavity. The [scaling and rigidity argument](research/ai/2026-10-20-concavity-equivalence/homogeneous_rigidity.md) describes the limiting shape an endpoint character must have. The [whole-filtration entropy investigation](research/ai/2026-10-20-full-filtration/README.md) gives a separate analytic obstruction for its balanced-source formulation.

These results explain why several scalar searches cannot improve the endpoint. They do **not** prove a lower bound $\omega\ge9/4$ or construct an actual tensor character.

### 2. Exact constructions and extension problems

The [anisotropic construction program](research/ai/2026-10-20-anisotropic-constructions/README.md) contains explicit rational maps and source-level coefficient checks. Selected constructions include:

- [Spin-module maps](research/ai/2026-10-20-anisotropic-constructions/spin_module14.md): $A(4,8)\to M(3,3,14)$ and $A(8,8)\to M(3,3,28)$.
- [Crossed-module lifts](research/ai/2026-10-20-anisotropic-constructions/parity_balancing_cross_module_lifts.md): $A(4,8)\to M(4,4,11)$ and $A(8,8)\to M(4,4,22)$.
- [Changed-corner construction](research/ai/2026-10-20-anisotropic-constructions/parity_structure_cross_module_corner_shifted.md): an $M(4,4,12)$ core with checked response and flattening ranks.
- [Rectangular spin seed](research/ai/2026-10-21-asymmetric-sl2-seed/rectangular_exact.md): exact rational $A(3,3)\to M(5,5,3)$ maps.

Here $M(u,v,w)$ is a rectangular matrix multiplication tensor. The linked notes define each source. None of these constructions alone gives a smaller exponent. Compatible square-target extensions remain missing, and several fixed-map extension routes are already excluded.

### 3. Ordinary rectangular targets and direct sums

The [rectangular program](research/ai/2026-10-21-rectangular-direct-sums/README.md) combines source-slice bounds, crossed-Hankel ranks, saturation, bundle dimensions, and ruling arguments.

The [size-2,000 scan](research/ai/2026-10-21-rectangular-direct-sums/single_frontier.md) covers **110 source formats and 5,741 score-eligible single targets**, with **427,076 exact integer-minor checks**. Applying the recorded written arguments leaves **74 ordinary candidates**. A [fixed-diagonal SL2 capacity test](research/ai/2026-10-21-rectangular-direct-sums/equivariant_frontier.md) excludes that symmetry-restricted ansatz for all 74; arbitrary maps remain open.

The [critical finite-state argument](research/ai/2026-10-21-rectangular-direct-sums/critical_finite_states.md), with its unreviewed premises, excludes the last ordinary single target through source dimension 1,500. Successive [two-block filters](research/ai/2026-10-21-rectangular-direct-sums/ruling_two_sums.md) reduce an earlier 4,469-candidate list to 690 after the later critical-state filter.

An **ordinary restriction** uses fixed linear maps. A **degeneration** permits a parameter-dependent limiting construction. Ordinary exclusions do not automatically exclude degenerations.

### 4. Representation-theoretic and graded obstructions

The [cyclic-equivariant program](research/ai/2026-10-20-cyclic-equivariant/README.md) studies matrix-vertex representations and their compatibility with the source. The [invariant-slice argument](research/ai/2026-10-21-rectangular-direct-sums/invariant_slice_pairing.md) adds multiplicity-rank tests for ordinary equivariant maps.

A [bounded physical-subset search](research/ai/2026-10-21-rectangular-direct-sums/physical_subset_frontier.md) checks balanced source sizes 24–36. Its 4,070 capacity-compatible triples all fail the recorded ordinary tests. The search allows at most five distinct physical summands per vertex; it is not an unrestricted exclusion.

The [support-peeling argument](research/ai/2026-10-20-anisotropic-constructions/torus_support_peeling.md) separately excludes a specified $A(8,8)$ direct-sum target for maps homogeneous in the fixed grading. Ungraded maps and general singular degenerations remain outside that result.

### 5. Quantum root flags, jets, and mixed subspaces

The [higher-jet program](research/ai/2026-10-20-higher-jet-quantum-flags/README.md) and its continuations analyze parameter-dependent maps through exact coefficient equations, normal spaces, and projection minors.

Later work includes [moving boundary flags](research/ai/2026-10-21-moving-boundary-flags/README.md), [mixed hyperplanes](research/ai/2026-10-21-rankone-mixed-hyperplanes/README.md), [pure mixed five-spaces](research/ai/2026-10-21-pure-mixed-five-spaces/README.md), and a [uniform mixed-axis closure](research/ai/2026-10-21-mixed-axis-incidence/README.md). These close specified families with written proofs and exact witnesses. General mixed-row graph charts and other flags remain unresolved.

### 6. Finite-group and alternative sources

The repository also studies [group-potential constructions](research/ai/2026-10-20-group-potentials/README.md), [SL(2,7)](research/ai/2026-10-20-sl2-seven/README.md), [Heisenberg sources](research/ai/2026-10-20-heisenberg-five/README.md), and [other source constructions](research/ai/2026-10-20-new-source-constructions/README.md).

These packages separate exact group calculations, conditional target scores, rank obstructions, bounded search outcomes, and unresolved candidates. A target that passes necessary tests is not a construction. A timeout is not an impossibility proof.

### 7. Numerical discovery and exact acceptance

The [unrestricted small-target search](research/ai/2026-10-21-asymmetric-sl2-seed/unrestricted_search.md) explores extensions of the exact rectangular seed. It includes ordinary fits and Laurent-coefficient searches toward $M(5,5,4)$.

[Laurent scale normalization](research/ai/2026-10-21-asymmetric-sl2-seed/laurent_scale_balance.md) removes a rescaling freedom that can artificially reduce raw positive-power errors. Checkpoints retain their input hashes, residuals, validation results, and exact modular rejection tests.

A small numerical residual is not an exact identity, a probability of success, or an exponent improvement. Even an exact small-target result would still need a suitable extension and a complete asymptotic argument.

## What would count as a breakthrough?

An improved exponent requires both a valid construction or inequality and the full implication for the stated computational model. The [research directions](docs/research_directions.md) describe several open routes:

- Construct a target whose certified source cost yields a strict gain, including all auxiliary factors and interpolation costs.
- Realize a sufficiently efficient family of [all-dimension mixed targets](research/ai/2026-10-20-koszul/all_dimension_targets.md).
- Find an asymptotic tensor constraint that excludes every remaining endpoint-character profile.
- Construct compatible extensions of the exact cores without violating the existing scoped obstructions.

General proofs need review. Finite certificates need reproducible checks. Neither a longer experiment log nor a larger collection of excluded ansatzes establishes the desired bound.

## Reproduce the initial experiments

Use Python 3.10 or later in a virtual environment. The CI configuration tests Python 3.10 and 3.14 and replays the historical experiments on Python 3.13. Install maintained dependencies from the root requirements file.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest discover -s tests -v
python tools/replay.py
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` and set thread environment variables using PowerShell syntax. The full suite can take tens of minutes. Package notes provide focused replay commands.

The [703-test local regression receipt](results/rectangular-direct-sums-20261021/immutable-regression-a41c9ee.json) pins commit `a41c9ee` and its tree: all tests passed in 2,090.419 seconds. This is a checkpoint result, not a claim that later changes or other branches passed. It predates the subsequently integrated mixed-axis closure. The repository retains failed receipts and their corrections.

`tools/replay.py` reproduces the original archived experiments in temporary copies. It is not a replay of every later research package. The [historical report](results/bootstrap-2026-10-20/summary.json) records 73,856 scalar-profile assertions and 353,664 product-filtration inequalities, plus bounded weight searches. Do not use Python's `-O` option, which disables assertions.

The archives `research/ai/2026-10-20/` and `research/ai/2026-10-20-session2/` remain unchanged. See [verification limits](docs/verification.md) for the distinction between exact checks, floating-point displays, and general proofs.

## Attribution and contribution

The external $9/4$ baseline belongs to OpenAI's October 2026 work, as recorded in the [source guide](docs/nine_fourths_route.md). This repository does not claim that theorem or its growth recurrence. The [literature map](docs/literature.md) credits earlier tensor methods and related work. Local research records disclose AI involvement, imported hypotheses, proof status, and limitations. No historical priority is inferred from a local derivation.

Contributions from people and AI-assisted workflows are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), preserve existing evidence, and use a focused pull request. Changes to `main` follow the repository's review and CI workflow. The aggregate `CI` check covers the configured test jobs and archive replay; it does not certify mathematical novelty or general correctness.

No repository license was selected at initialization. External publications and code retain their own licenses. Consult [PROVENANCE.md](PROVENANCE.md) and [repository settings](docs/repository-settings.md).
