---
description: Branch, commit, push to the fork, and open a PR automatically
argument-hint: "[short branch-name or PR title]"
---

Ship the current working-tree changes as a pull request, end to end, without stopping to ask
for the link or for confirmation. Optional argument: `$ARGUMENTS` (use it as the branch name
slug / PR title if given, otherwise derive both from the diff).

Repos: the fork is `Rakshith-PanMac/bounty-hunter_work` (`origin`); upstream is
`iconicwolf/bounty-hunter` (base branch `master`).

## Steps

1. **Inspect.** Run `git status` and `git diff`. If there are no changes, say so and stop.
2. **Branch.** Never commit to `master`. If on `master`, create a new branch
   (`fix/...`, `feat/...`, `docs/...`, or `chore/...`) from the latest `origin/master`.
3. **Stage only the intended files.** `git add` specific paths; never `git add -A` or `.`.
   **Always omit** (leave untracked, and delete generated ones you created):
   - secrets and config: `.env` (only `.env.example` may be committed), keys, tokens
   - Python/build artifacts: `__pycache__/`, `*.pyc`, `*.pyo`, `.pytest_cache/`, `venv/`, `.venv/`
   - local data and editor files: `*.db`, `*.sqlite*`, `.idea/`, `.vscode/`, `.DS_Store`
   - scratch and test output: temp scripts, logs, screenshots or recordings not part of the change
   - known leftovers: `Test.txt`, `audit_zinc.json`
   If any of these are already tracked or show up as modified, do not commit them; mention it
   in the PR description. Screenshots under `static/evidence/` are committed only when the
   change is meant to add evidence.
4. **Check.** Run what applies (e.g. `pytest`, and a browser check for frontend changes).
   Report failures honestly; do not skip or weaken tests to get green.
5. **Commit.** Detailed message: short imperative subject, then a body explaining what changed and
   why. End with the attribution lines the session specifies.
6. **Push.** `git push -u origin <branch>`. Never force-push. Retry network failures up to 4
   times with 2s/4s/8s/16s backoff.
7. **Open the PR automatically.** Mirror a PR template if one exists
   (`.github/pull_request_template.md`, root, or `docs/`); otherwise use Summary / Problem /
   Changes / Testing / Not included, stating what was and was not tested. End with the PR
   attribution lines the session specifies.
   - Try upstream first: `create_pull_request` with owner `iconicwolf`, repo `bounty-hunter`,
     head `Rakshith-PanMac:<branch>`, base `master`.
   - If that is denied because the session is only granted the fork, open the PR in the fork
     (`Rakshith-PanMac/bounty-hunter_work`, base `master`) instead.
8. **Report** the PR URL in one line, then ask whether to watch it with `subscribe_pr_activity`.

## Rules
- Do not merge, approve, or close PRs.
- Do not rewrite history or push to `master`.
- If a real secret may have been committed earlier, remind the user to rotate it.
