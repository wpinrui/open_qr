# -g: Git Merged / Continue

## Steps
1. Switch to main: `git checkout main`
2. Pull latest: `git pull`
3. Delete merged local branches:
   ```bash
   git branch --merged main | grep -v "main" | xargs -r git branch -d
   ```
4. Report current state and what's ready for next work
5. If chained with `-f`, proceed to feature selection
