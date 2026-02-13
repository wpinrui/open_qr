import sys

from src.capture import grab_screen
from src.decoder import find_qr_codes
from src.clipboard import copy_to_clipboard
from src.notify import show_notification


def scan() -> None:
    """Capture screen, detect QR codes, copy results to clipboard."""
    image = grab_screen()
    codes = find_qr_codes(image)

    if not codes:
        show_notification("No QR code found", is_error=True)
        return

    result = "\n".join(codes)
    copy_to_clipboard(result)

    if len(codes) == 1:
        show_notification(f"Copied: {codes[0]}")
    else:
        preview = f"{len(codes)} QR codes copied"
        show_notification(preview)


if __name__ == "__main__":
    scan()
