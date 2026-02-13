# PR Review Checklist

Use this checklist when running `-r` (PR review).

## Code Quality
- [ ] No unused variables or imports
- [ ] No hardcoded values that should be configurable
- [ ] No TODO comments without corresponding GitHub issues
- [ ] Error handling is present where needed
- [ ] No overly complex functions (break down if >30 lines)

## Security
- [ ] No secrets or credentials in code
- [ ] User input is validated/sanitized
- [ ] No unnecessary permissions requested

## Performance
- [ ] No obvious memory leaks (event listeners cleaned up, etc.)
- [ ] Screen capture/QR detection is efficient (no unnecessary re-scans)
- [ ] Resources are properly released after use

## Testing
- [ ] New functionality has tests where appropriate
- [ ] Edge cases are considered (no QR found, multiple QRs, partial QR)

## Documentation
- [ ] proposal.md is updated if a feature was completed
- [ ] Complex logic has inline comments
