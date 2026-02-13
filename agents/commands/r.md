# -r: PR Review

## Steps
1. Run `git diff main...HEAD` to see all changes in the current branch
2. Read the changed files in full to understand context
3. Review against `agents/rules/pr-review-checklist.md`
4. Report findings grouped by severity:
   - **Blockers** - Must fix before merge
   - **Warnings** - Should fix, but not critical
   - **Nits** - Minor suggestions
5. If no issues found, confirm the PR is ready to merge
