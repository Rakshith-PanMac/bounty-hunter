---
description: Branch, commit, push to the fork, and open a PR for the current changes
argument-hint: "[short branch-name or PR title]"
---

Ship the current working-tree changes as a pull request. Optional argument: `$ARGUMENTS`
(use it as the branch name slug / PR title if given, otherwise derive both from the diff).

Repos: the fork is `Rakshith-PanMac/bounty-hunter` (`origin`); upstream is
`iconicwolf/bounty-hunter` (base branch `master`).

## Steps

1. **Inspect.** Run `git status` and `git diff`. If there are no changes, say so and stop.
2. **Branch.** Never commit to `master`. If on `master`, create a new branch
   (`fix/...`, `feat/...`, `docs/...`, or `chore/...`) from the latest `origin/master`.
3. **Stage deliberately.** `git add` specific files only. Never stage `.env`, `*.pyc`,
   `__pycache__/`, `*.db`, or anything that looks like a secret. If one shows up, stop and warn.
4. **Check.** Run what applies (e.g. `pytest`, and for frontend changes a browser check). Report
   failures honestly; do not skip or weaken tests to get green.
5. **Commit.** Write a detailed message: a short imperative subject, then a body explaining what
   changed and why. End with the attribution lines the session specifies.
6. **Push.** `git push -u origin <branch>`. Never force-push. Retry network failures up to 4 times
   with 2s/4s/8s/16s backoff.
7. **Open the PR.** Check for a PR template (`.github/pull_request_template.md`, root, or
   `docs/`) and mirror its headings; otherwise use Summary / Problem / Changes / Testing /
   Not included. Include what was and was not tested. End with the PR attribution lines the
   session specifies.
   - First try upstream: `create_pull_request` with owner `iconicwolf`, repo `bounty-hunter`,
     head `Rakshith-PanMac:<branch>`, base `master`.
   - If that is denied (the session is only granted the fork), open the PR in the fork
     (`Rakshith-PanMac/bounty-hunter`, base `master`) and print this link for the user to open
     the upstream PR with the same title and description:
     `https://github.com/iconicwolf/bounty-hunter/compare/master...Rakshith-PanMac:bounty-hunter:<branch>`
8. **Report.** Give the PR URL (and the compare link if upstream was denied), then ask whether to
   watch the PR with `subscribe_pr_activity`.

## Rules
- Do not merge, approve, or close PRs.
- Do not rewrite history or push to `master`.
- If a real secret may have been committed earlier, remind the user to rotate it.
