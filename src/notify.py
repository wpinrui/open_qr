import sys

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer


def show_notification(message: str, is_error: bool = False) -> None:
    """Show a Windows toast notification via Qt system tray."""
    app = QApplication(sys.argv)

    # Invisible tray icon just to send the notification
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon())
    tray.setVisible(True)

    icon_type = (
        QSystemTrayIcon.MessageIcon.Warning
        if is_error
        else QSystemTrayIcon.MessageIcon.Information
    )
    tray.showMessage("open_qr", message, icon_type, 3000)

    # Give the notification time to display, then exit
    QTimer.singleShot(3500, app.quit)
    app.exec()
