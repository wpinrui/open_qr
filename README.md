# open_qr

Desktop tool that detects any QR code on your screen and copies the decoded text to your clipboard. Press a hotkey, get the text. That's it.

## Quick Start (prebuilt)

1. Download `open_qr.exe` from [Releases](https://github.com/wpinrui/open_qr/releases)
2. Run it — a tray icon appears
3. Press **Ctrl+Shift+Q** whenever a QR code is visible on screen
4. The decoded text is copied to your clipboard with a toast notification

Right-click the tray icon for **Scan Now** or **Quit**.

## Build from Source

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)

### Setup

```bash
git clone https://github.com/wpinrui/open_qr.git
cd open_qr
python -m venv venv
venv\Scripts\pip install -r requirements.txt
python setup.py
```

The setup script will:
1. Build a standalone `open_qr.exe` with PyInstaller
2. Ask if you want to add it to startup (runs on login)

### Run without building

```bash
venv\Scripts\pythonw -m src.main
```

## Stack

- **Python** — screen capture ([mss](https://github.com/BoboTiG/python-mss)), QR decoding ([pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)), clipboard ([pyperclip](https://github.com/asweigart/pyperclip)), system tray + notifications ([PyQt6](https://www.riverbankcomputing.com/software/pyqt/))
- **Win32 API** — global hotkey registration (Ctrl+Shift+Q)
- **PyInstaller** — standalone `.exe` packaging
