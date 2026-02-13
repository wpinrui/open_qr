from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol


def find_qr_codes(image: Image.Image) -> list[str]:
    """Detect all QR codes in the image and return their decoded text."""
    results = decode(image, symbols=[ZBarSymbol.QRCODE])
    return [r.data.decode("utf-8") for r in results]
