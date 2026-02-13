# Project Agent Configuration

## Project: open_qr

Desktop QR code tool that detects any QR code visible on screen and copies its text to clipboard.

## On Startup

Read these files before doing anything:
- `agents/memory/mistakes.md` - Avoid past errors
- `agents/memory/preferences.md` - User's workflow preferences
- `agents/rules/git-workflow.md` - Git and versioning conventions
- `agents/context/proposal.md` - Project roadmap (know what's next)

## CRITICAL RULES (ALWAYS APPLY)

After EVERY task completion or question, beep:
```bash
powershell -c "[console]::beep(1000,1500)"
```

DO NOT CHAIN terminal commands, even cd. RUN SEPARATELY.

Create GitHub issues for discovered tech debt - never ignore it.

NEVER assume - ask when uncertain.

**Debugging (BEFORE making any code changes):**
1. Add logging to see actual values at the failure point
2. Ask user to test and report what's logged
3. Only then identify root cause and fix
NEVER guess at fixes. Observe first, then fix.

**Path Formats:**
- Read/Write/Edit tools: Windows paths (`c:\Users\...`)
- Bash commands: Unix paths (`/c/Users/...`)

**Git Workflow (EVERY feature):**
1. Create branch FIRST: `git checkout -b feature/[name]`
2. Make code changes
3. **Update proposal.md** - check off completed items immediately
4. Commit: `git commit -m "Short description"` - SINGLE LINE, NO SUFFIX
5. Open PR

NEVER code on main. NEVER skip the PR. NEVER add co-author suffixes to commits.

## Commands

When user types a command, read the corresponding file in `agents/commands/`:

| Command | File | Purpose |
|---------|------|---------|
| -r | r.md | PR review (includes strict checks) |
| -f | f.md | Feature selection |
| -g | g.md | Git merged/continue |
| -p | p.md | Execute plan |
| -d | d.md | Documentation sync |
| -i | i.md | Fix issues |
| -c | c.md | Critique mode |
| -m | m.md | Metacognition / self-improvement |

**Command Chaining:** `-g -f -r` executes sequentially. Each command feeds into the next. Wait for user input when a command requires it before proceeding to the next.

## Compaction Recovery

After context compaction (detected by incomplete memory of recent conversation), re-read `agents/rules/core.md` and inform the user.

## Self-Improvement

- Learn something new → update relevant file in `agents/memory/`
- File exceeds 200 lines → note in `agents/meta/file-health.md`, propose split to user
- User repeats a correction → add to `agents/memory/mistakes.md`

## Continuous Improvement

When you notice things not going well (repeated corrections, misunderstandings, wasted effort):
- Pause and acknowledge
- Consider running `-m` to analyze and improve the agentic files
- Or note observations in `agents/memory/mistakes.md` for later

## Detailed Rules

For expanded rules on any topic, see `agents/rules/`:
- `core.md` - Universal behavioral rules (beep, tech debt, no assumptions)
- `pr-review-checklist.md` - Code smell checklist for PR reviews
- `git-workflow.md` - Branching, commit, and PR conventions
