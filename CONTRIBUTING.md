# Contributions

Anyone can contribute through an issue or pull request, including contributors who use AI agents. Maintainers decide which changes to merge.

## Before an investigation

Read `STATUS.md`, `research/claims.json`, and the relevant source records. Inspect open issues and branches for overlapping work. State the question, intended output, and mathematical consequence.

## Evidence and attribution

Use a source citation for each imported theorem or construction. Record its version, field, and hypotheses. Distinguish an external result from a local rederivation or extension. Preserve disclosed AI and human contribution roles without inventing review credit.

Classify each new claim as a conjecture, conditional implication, written proof, reviewed proof, formalized theorem, or finite experiment. Identify every unproved premise. When a premise is unproved, keep numerical examples conditional on it.

For an exponent claim, specify the computation model and all quantifiers. Account for interpolation, tensor powers, field extensions, auxiliary factors, and asymptotic overhead. A finite optimization score is not the complete theorem.

## Files and reproduction

Preserve `research/ai/2026-10-20/` and `research/ai/2026-10-20-session2/` byte-for-byte. Put corrections in a new dated note that identifies the superseded claim. Keep experiments and their actual reports together. Record exact commands, parameters, seeds, dependencies, and completed coverage.

Use exact arithmetic or certified error bounds for acceptance decisions. Export a witness that another program can verify. Report float estimates separately.

Run the regression suite and the relevant replay before submission. Do not disable a failing test without explaining the underlying change. Do not describe a finite test as an asymptotic proof.

Use the [README setup instructions](README.md#reproduce-the-initial-experiments) for the supported Python versions. Run these commands from the repository root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/replay.py
```

The replay writes to `results/local/`, which Git ignores. Python optimization disables archived assertions, so `-O` and `PYTHONOPTIMIZE` are unsupported.

Change maintained dependencies in `requirements.txt`. Preserve dependency files inside archived research. If a dependency update fails reproduction, investigate compatibility before merging.

## Branch and merge workflow

1. Create a branch from the current `main`, or create a branch in your fork.
2. Keep each pull request focused on one investigation, correction, or maintenance change.
3. Open a pull request targeting `main`. Use a draft while the result or evidence is incomplete.
4. Run the relevant local checks before requesting a merge.
5. Resolve review discussions and wait for the required `CI` check to pass.
6. Merge through the pull request after the branch meets the repository rules.

Changes to `main` must go through a pull request. Do not bypass the rules with a direct push or force push.

An external approval is not required for every pull request. A maintainer can merge their own pull request after CI and discussion requirements pass.
The merge records acceptance into the repository. It does not establish independent mathematical review or change a claim's evidence status.

Before a merge, update a branch that is behind `main`. When a merged branch has no remaining work, remove it.

## Pull request contents

A pull request must identify the affected claim IDs and external sources. Include the proposed result, evidence, verification commands, limitations, and any change to the active research questions.

A correction or a scoped negative result is a valid contribution. Repeated reproduction is useful maintenance, but it is not a new mathematical discovery.

Update the claim ledger and status page together. Do not claim independent review for self-review or for a rerun by the same generating session.

For maintenance changes, describe the affected behavior and verification. When no research claim changes, claim IDs and theorem evidence are unnecessary.

## Reports and licensing

Use an [issue](https://github.com/1337isnot1337/matrix-mult-bounds/issues/new/choose) for a reproduction failure, research question, or mathematical correction.
For a security vulnerability, use [SECURITY.md](SECURITY.md).

The repository has no selected license. External sources retain their own terms. Do not add or change a license without the owner's explicit authorization.
