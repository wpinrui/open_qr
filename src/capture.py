import mss
from PIL import Image


def grab_screen() -> Image.Image:
    """Capture the entire primary monitor and return as a PIL Image."""
    with mss.mss() as sct:
        # monitor[0] is all monitors combined, monitor[1] is the primary
        shot = sct.grab(sct.monitors[1])
        return Image.frombytes("RGB", shot.size, shot.bgra, "raw", "BGRX")
