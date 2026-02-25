"""Setup script: generates open_qr.ahk with the correct project path, compiles it, and optionally adds to startup."""

import os
import subprocess
import shutil
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()
TEMPLATE = PROJECT_DIR / "open_qr.ahk.template"
OUTPUT_AHK = PROJECT_DIR / "open_qr.ahk"
OUTPUT_EXE = PROJECT_DIR / "open_qr.exe"

STARTUP_DIR = Path(os.environ.get("APPDATA", "")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

AHK_SEARCH_ROOTS = [
    Path(os.environ.get("ProgramFiles", "")),
    Path(os.environ.get("ProgramFiles(x86)", "")),
    Path(os.environ.get("LocalAppData", "")) / "Programs",
]


def find_ahk_compiler() -> Path | None:
    found = shutil.which("Ahk2Exe")
    if found:
        return Path(found)
    for root in AHK_SEARCH_ROOTS:
        path = root / "AutoHotkey" / "Compiler" / "Ahk2Exe.exe"
        if path.exists():
            return path
    return None


def find_ahk_base() -> Path | None:
    for root in AHK_SEARCH_ROOTS:
        path = root / "AutoHotkey" / "v2" / "AutoHotkey64.exe"
        if path.exists():
            return path
        path = root / "AutoHotkey" / "v2" / "AutoHotkey.exe"
        if path.exists():
            return path
    return None


def generate_ahk() -> bool:
    try:
        template = TEMPLATE.read_text()
        result = template.replace("{{PROJECT_DIR}}", str(PROJECT_DIR))
        OUTPUT_AHK.write_text(result)
        print(f"Generated: {OUTPUT_AHK}")
        return True
    except FileNotFoundError:
        print(f"Error: template not found at {TEMPLATE}")
        return False
    except OSError as e:
        print(f"Error generating AHK file: {e}")
        return False


def compile_ahk(compiler: Path, base: Path) -> bool:
    try:
        cmd = [str(compiler), "/in", str(OUTPUT_AHK), "/out", str(OUTPUT_EXE), "/base", str(base)]
        subprocess.run(cmd, check=True)
        print(f"Compiled:  {OUTPUT_EXE}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: AHK compilation failed (exit code {e.returncode})")
        return False
    except OSError as e:
        print(f"Error running AHK compiler: {e}")
        return False


def add_to_startup() -> bool:
    dest = STARTUP_DIR / OUTPUT_EXE.name
    try:
        shutil.copy2(OUTPUT_EXE, dest)
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
    if not generate_ahk():
        return

    compiler = find_ahk_compiler()
    base = find_ahk_base()

    if not compiler:
        print("AHK compiler (Ahk2Exe) not found — skipping compilation.")
        print("You can still run open_qr.ahk directly with AutoHotkey v2.")
        return

    if not base:
        print("Found AHK compiler but no v2 base binary — skipping compilation.")
        print("Install AutoHotkey v2 to enable compilation.")
        return

    print(f"Found AHK compiler: {compiler}")
    print(f"Found AHK v2 base:  {base}")

    if not compile_ahk(compiler, base):
        return

    if prompt_yes_no("Add open_qr.exe to shell:startup (run on login)?"):
        add_to_startup()


if __name__ == "__main__":
    main()
