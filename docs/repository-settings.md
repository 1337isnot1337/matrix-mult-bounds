# Repository settings

The checked-in settings files describe the merge policy. GitHub enforces the policy through repository settings, separately from committed files.
Committing the JSON files does not activate protection.

## Required policy for main

| Control | Setting |
| --- | --- |
| Target | `refs/heads/main` |
| Enforcement | Active |
| Bypass actors | None, including administrators and apps |
| Pull request | Required |
| Required approvals | Zero |
| Review discussions | Resolved before merge |
| Required check | `CI`, from the GitHub Actions app |
| Base branch | Pull request must be current with `main` |
| Merge method | Squash |
| History | Linear |
| Force push and deletion | Blocked |

Zero required approvals allows a maintainer to merge their own pull request after the other requirements pass.
Review requests and mathematical review status remain separate from that permission.
An administrator can edit repository rules, but the ruleset grants no bypass for routine pushes or merges.

The required check uses GitHub Actions app ID `15368`, verified from this repository's existing check runs.
The [workflow](../.github/workflows/verify.yml) runs all tests on Python 3.10 and 3.14 and the archive replay on Python 3.13.
Its final `CI` job fails unless both prerequisite jobs succeed.
The required workflow has no path filters, so documentation changes receive the check too.

## Apply the settings

Repository administration access is required. The repository owner can use GitHub's settings page or an authenticated GitHub CLI.

1. Merge the workflow and verify a successful `CI` check before activating its requirement.
2. Apply [.github/repository-settings.json](../.github/repository-settings.json) to the repository.
3. Import [.github/main-ruleset.json](../.github/main-ruleset.json) under **Settings → Rules → Rulesets → Import a ruleset**.
4. Verify that the ruleset is active and that it targets `main`.

These CLI commands use the same files. Run them from the repository root:

```sh
gh api --method PATCH repos/1337isnot1337/matrix-mult-bounds \
  --input .github/repository-settings.json
gh api repos/1337isnot1337/matrix-mult-bounds/rulesets
```

If the named ruleset does not exist, create it:

```sh
gh api --method POST repos/1337isnot1337/matrix-mult-bounds/rulesets \
  --input .github/main-ruleset.json
```

If the named ruleset exists, update its returned numeric ID with `PUT` instead of creating a duplicate.
Preserve unrelated rulesets.

```sh
gh api repos/1337isnot1337/matrix-mult-bounds/rules/branches/main
gh api repos/1337isnot1337/matrix-mult-bounds
```

The first response must contain the required pull request, status check, linear history, deletion, and force-push rules.
The repository response must show squash merging, automatic branch deletion, automatic merges, and branch updates enabled.
Automatic merge still waits for repository requirements. Enabling it does not enroll every pull request.

## Actions and security settings

Use read-only workflow token permissions. Keep permission to create or approve pull requests disabled for Actions.
Require approval for workflow runs from outside contributors. Do not expose repository secrets to fork workflows.
Keep private vulnerability reporting, Dependabot alerts, secret scanning, and push protection enabled where GitHub makes them available.

The [Dependabot file](../.github/dependabot.yml) checks Actions and maintained Python dependencies weekly.
Historical dependency records are excluded.
The [security policy](../SECURITY.md) gives the reporting procedure.

## Verification limits

Passing CI checks code and recorded artifacts. It does not prove an asymptotic theorem or provide independent mathematical review.
If hosted checks cannot start, resolve the runner or account error before merging. A local pass does not substitute for the required check.
An older research branch must incorporate the workflow before its pull request can provide `CI`.

## GitHub references

- [Create and import rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [Available rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [Rules REST API](https://docs.github.com/en/rest/repos/rules#create-a-repository-ruleset)
- [Repository REST API](https://docs.github.com/en/rest/repos/repos#update-a-repository)
