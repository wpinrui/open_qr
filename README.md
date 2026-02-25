# open_qr

Desktop tool that detects any QR code on your screen and copies the decoded text to your clipboard. Press a hotkey, get the text. That's it.

## Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [AutoHotkey v2](https://www.autohotkey.com/) (for the hotkey and optional compilation)

## Setup

```bash
git clone https://github.com/wpinrui/open_qr.git
cd open_qr
python -m venv venv
venv\Scripts\pip install -r requirements.txt
python setup.py
```

The setup script will:
1. Generate the hotkey script with the correct project path
2. Compile it to an `.exe` (if AHK v2 compiler is found)
3. Ask if you want to add it to startup (runs on login)

## Usage

Start the hotkey listener by either:
- Running `open_qr.exe` (compiled) or `open_qr.ahk` (requires AHK v2 installed)
- Or let it start automatically on login if you chose that during setup

Then press **Ctrl+Shift+Q** whenever a QR code is visible on your screen. The decoded text is copied to your clipboard with a toast notification.

## Stack

- **Python** — screen capture ([mss](https://github.com/BoboTiG/python-mss)), QR decoding ([pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)), clipboard ([pyperclip](https://github.com/asweigart/pyperclip)), notifications ([PyQt6](https://www.riverbankcomputing.com/software/pyqt/))
- **AutoHotkey v2** — global hotkey listener
