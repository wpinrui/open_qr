# Core Rules

Universal behavioral rules that always apply.

## 1. Beep on Completion
After EVERY task completion or question:
```bash
powershell -c "[console]::beep(1000,1500)"
```

## 2. No Command Chaining
DO NOT chain terminal commands. Run each command separately.

## 3. Tech Debt Tracking
Create GitHub issues for discovered tech debt. Never ignore it.

## 4. No Assumptions
When uncertain, ask the user. Don't guess.

## 5. Debugging Protocol
Before making any code changes:
1. Add logging to see actual values at the failure point
2. Ask user to test and report what's logged
3. Only then identify root cause and fix

## 6. Path Formats
- Read/Write/Edit tools: Windows paths (`c:\Users\...`)
- Bash commands: Unix paths (`/c/Users/...`)

## 7. Proposal Updates
After completing any feature work, immediately update `agents/context/proposal.md` to check off completed items.
