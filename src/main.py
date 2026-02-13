from src.capture import grab_screen
from src.decoder import find_qr_codes
from src.clipboard import copy_to_clipboard


def scan() -> None:
    """Capture screen, detect QR codes, copy results to clipboard."""
    print("Capturing screen...")
    image = grab_screen()

    print("Scanning for QR codes...")
    codes = find_qr_codes(image)

    if not codes:
        print("No QR codes found.")
        return

    result = "\n".join(codes)
    copy_to_clipboard(result)

    count = len(codes)
    if count == 1:
        print(f"Found QR code. Copied to clipboard: {codes[0]}")
    else:
        print(f"Found {count} QR codes. Copied all to clipboard:")
        for i, code in enumerate(codes, 1):
            print(f"  {i}. {code}")


if __name__ == "__main__":
    scan()
