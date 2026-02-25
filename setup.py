"""Setup script: builds open_qr into a standalone .exe and optionally adds to startup."""

import os
import subprocess
import shutil
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()
DIST_EXE = PROJECT_DIR / "dist" / "open_qr.exe"
STARTUP_DIR = Path(os.environ.get("APPDATA", "")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"


def find_pyzbar_dlls() -> list[Path]:
    """Find pyzbar bundled DLLs that PyInstaller misses."""
    try:
        import pyzbar
        pyzbar_dir = Path(pyzbar.__file__).parent
        return list(pyzbar_dir.glob("*.dll"))
    except ImportError:
        return []


def build_exe() -> bool:
    add_data = []
    for dll in find_pyzbar_dlls():
        add_data.extend(["--add-binary", f"{dll};pyzbar"])

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name", "open_qr",
        "--clean",
        *add_data,
        str(PROJECT_DIR / "src" / "main.py"),
    ]

    try:
        subprocess.run(cmd, check=True, cwd=str(PROJECT_DIR))
        print(f"Built: {DIST_EXE}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: PyInstaller build failed (exit code {e.returncode})")
        return False
    except FileNotFoundError:
        print("Error: PyInstaller not found. Run: pip install pyinstaller")
        return False


def add_to_startup() -> bool:
    dest = STARTUP_DIR / DIST_EXE.name
    try:
        shutil.copy2(DIST_EXE, dest)
        print(f"Copied to startup: {dest}")
        return True
    except FileNotFoundError:
        print(f"Error: startup directory not found at {STARTUP_DIR}")
        return False
    except OSError as e:
        print(f"Error copying to startup: {e}")
        return False


def prompt_yes_no(question: str) -> bool:
    while True:
        answer = input(f"{question} [y/n]: ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def main():
    print("Building open_qr.exe with PyInstaller...")
    if not build_exe():
        return

    if prompt_yes_no("Add open_qr.exe to shell:startup (run on login)?"):
        add_to_startup()


if __name__ == "__main__":
    main()
