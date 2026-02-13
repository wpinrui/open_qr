# -i: Fix Issues

## Steps
1. Run `gh issue list` to see open GitHub issues
2. Present issues to user, grouped by label/priority if available
3. Ask which issue to work on
4. Create a branch: `git checkout -b fix/[issue-description]`
5. Investigate the issue (read code, add logging, reproduce)
6. Follow debugging protocol: observe first, then fix
7. After fix, update proposal.md if relevant
8. Commit and create PR referencing the issue: `Fixes #N`
