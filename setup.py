"""Setup script: generates open_qr.ahk with the correct project path and optionally compiles it."""

import os
import subprocess
import shutil
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.resolve()
TEMPLATE = PROJECT_DIR / "open_qr.ahk.template"
OUTPUT_AHK = PROJECT_DIR / "open_qr.ahk"
OUTPUT_EXE = PROJECT_DIR / "open_qr.exe"

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


def generate_ahk():
    template = TEMPLATE.read_text()
    result = template.replace("{{PROJECT_DIR}}", str(PROJECT_DIR))
    OUTPUT_AHK.write_text(result)
    print(f"Generated: {OUTPUT_AHK}")


def compile_ahk(compiler: Path, base: Path):
    cmd = [str(compiler), "/in", str(OUTPUT_AHK), "/out", str(OUTPUT_EXE), "/base", str(base)]
    subprocess.run(cmd, check=True)
    print(f"Compiled:  {OUTPUT_EXE}")


def main():
    generate_ahk()

    compiler = find_ahk_compiler()
    base = find_ahk_base()

    if compiler and base:
        print(f"Found AHK compiler: {compiler}")
        print(f"Found AHK v2 base:  {base}")
        compile_ahk(compiler, base)
    elif compiler:
        print(f"Found AHK compiler but no v2 base binary — skipping compilation.")
        print("Install AutoHotkey v2 to enable compilation.")
    else:
        print("AHK compiler (Ahk2Exe) not found — skipping compilation.")
        print("You can still run open_qr.ahk directly with AutoHotkey v2.")


if __name__ == "__main__":
    main()
