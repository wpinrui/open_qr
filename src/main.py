import sys
import ctypes
import ctypes.wintypes

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QStyle
from PyQt6.QtCore import QAbstractNativeEventFilter
from PyQt6.QtGui import QAction

try:
    from src.capture import grab_screen
    from src.decoder import find_qr_codes
    from src.clipboard import copy_to_clipboard
except ImportError:
    from capture import grab_screen
    from decoder import find_qr_codes
    from clipboard import copy_to_clipboard

HOTKEY_ID = 1
MOD_CTRL = 0x0002
MOD_SHIFT = 0x0004
MOD_NOREPEAT = 0x4000
VK_Q = 0x51
WM_HOTKEY = 0x0312


class HotkeyFilter(QAbstractNativeEventFilter):
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def nativeEventFilter(self, eventType, message):
        if eventType == b"windows_generic_MSG":
            msg = ctypes.wintypes.MSG.from_address(int(message))
            if msg.message == WM_HOTKEY and msg.wParam == HOTKEY_ID:
                self.callback()
                return True, 0
        return False, 0


class TrayApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)

        self.tray = QSystemTrayIcon()
        icon = self.app.style().standardIcon(QStyle.StandardPixmap.SP_ComputerIcon)
        self.tray.setIcon(icon)
        self.tray.setToolTip("open_qr — Ctrl+Shift+Q to scan")

        menu = QMenu()
        scan_action = QAction("Scan Now", menu)
        scan_action.triggered.connect(self.scan)
        quit_action = QAction("Quit", menu)
        quit_action.triggered.connect(self.quit)
        menu.addAction(scan_action)
        menu.addSeparator()
        menu.addAction(quit_action)

        self.tray.setContextMenu(menu)
        self.tray.show()

        self._register_hotkey()

        # Intercept WM_HOTKEY inside Qt's event loop
        self.hotkey_filter = HotkeyFilter(self.scan)
        self.app.installNativeEventFilter(self.hotkey_filter)

    def _register_hotkey(self):
        result = ctypes.windll.user32.RegisterHotKey(
            None, HOTKEY_ID, MOD_CTRL | MOD_SHIFT | MOD_NOREPEAT, VK_Q
        )
        if not result:
            self.tray.showMessage(
                "open_qr",
                "Failed to register Ctrl+Shift+Q — hotkey may be in use",
                QSystemTrayIcon.MessageIcon.Warning,
                3000,
            )

    def scan(self):
        image = grab_screen()
        codes = find_qr_codes(image)

        if not codes:
            self.tray.showMessage(
                "open_qr",
                "No QR code found",
                QSystemTrayIcon.MessageIcon.Warning,
                3000,
            )
            return

        result = "\n".join(codes)
        copy_to_clipboard(result)

        if len(codes) == 1:
            msg = f"Copied: {codes[0]}"
        else:
            msg = f"{len(codes)} QR codes copied"

        self.tray.showMessage(
            "open_qr", msg, QSystemTrayIcon.MessageIcon.Information, 3000
        )

    def quit(self):
        ctypes.windll.user32.UnregisterHotKey(None, HOTKEY_ID)
        self.tray.hide()
        self.app.quit()

    def run(self):
        sys.exit(self.app.exec())


def main():
    app = TrayApp()
    app.run()


if __name__ == "__main__":
    main()
