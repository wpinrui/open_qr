# Git Workflow

## Branching
- NEVER code directly on `main`
- Create a feature branch first: `git checkout -b feature/[name]`
- Use descriptive branch names: `feature/screen-capture`, `fix/qr-decode-error`

## Commits
- Single-line commit messages: `git commit -m "Short description"`
- NO co-author suffixes
- NO multi-line commit messages unless absolutely necessary
- Write in imperative mood: "Add feature" not "Added feature"

## Pull Requests
- Every feature goes through a PR
- NEVER skip the PR step
- Use `-r` command to review before merging

## After Merge
- Use `-g` command to clean up and continue
- Delete merged branches locally and remotely
