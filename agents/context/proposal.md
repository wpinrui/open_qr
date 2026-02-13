# open_qr - Project Proposal

Personal desktop tool: press a hotkey, it captures the screen, detects any QR code, and copies the decoded text to clipboard.

## Stack
- **Language:** Python
- **GUI:** PyQt6 / PySide6 (for system tray + hotkey)
- **QR decoding:** pyzbar (or OpenCV fallback)
- **Screen capture:** mss (fast, cross-platform) or Pillow's ImageGrab
- **Clipboard:** pyperclip or Qt's built-in clipboard
- **Packaging:** PyInstaller (single .exe for Windows)

## Phase 1: MVP (hotkey → scan → clipboard)
- [x] Set up Python project (venv, requirements.txt, src/ structure)
- [x] Screen capture: grab full screen as image
- [x] QR detection: decode QR codes from screenshot using pyzbar
- [x] Clipboard: copy decoded text to system clipboard
- [x] Wire it together: single script that captures → detects → copies
- [x] Add basic console output confirming what was found/copied

## Phase 2: Desktop Integration
- [ ] System tray icon (PyQt6) — app lives in tray, no main window
- [ ] Global hotkey registration (e.g. Ctrl+Shift+Q)
- [ ] Toast notification on success ("Copied: <text preview>")
- [ ] Toast notification on failure ("No QR code found")
- [ ] Handle multiple QR codes: copy all, separated by newlines (or pick largest)

## Phase 3: Quality of Life
- [ ] Scan history (last N scans, viewable from tray menu)
- [ ] Multi-monitor support (capture all screens)
- [ ] Configurable hotkey
- [ ] Auto-start on Windows login (optional)
- [ ] Package as .exe with PyInstaller

## Future Ideas
- [ ] Region selection mode (drag to select area)
- [ ] URL preview before opening detected links
- [ ] Support other barcode formats (EAN, Code128, etc.)
- [ ] Continuous monitoring mode (always-on watcher)
