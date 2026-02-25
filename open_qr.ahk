#Requires AutoHotkey v2.0

; open_qr — press Ctrl+Shift+Q to scan screen for QR codes
; The decoded text is copied to clipboard automatically.

PROJECT := "C:\Users\Ivan\Documents\projects\open_qr"
PYTHON := PROJECT "\venv\Scripts\pythonw.exe"

^+q:: {
    Run(PYTHON ' -m src.main', PROJECT, "Hide")
}
