#Requires AutoHotkey v2.0

; open_qr — press Ctrl+Shift+Q to scan screen for QR codes
; The decoded text is copied to clipboard automatically.

PYTHON := A_ScriptDir "\venv\Scripts\pythonw.exe"
PROJECT := A_ScriptDir

^+q:: {
    Run(PYTHON ' -m src.main', PROJECT, "Hide")
}
