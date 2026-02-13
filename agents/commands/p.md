# -p: Execute Plan

## Steps
1. Read `agents/context/proposal.md` to understand current state
2. Check current git branch (should be on a feature branch, not main)
3. If no feature branch exists, ask user what to work on
4. Execute the planned implementation for the current feature
5. After completion, update `agents/context/proposal.md` to check off completed items
6. Commit changes: `git commit -m "Short description"`
7. Push and create PR
