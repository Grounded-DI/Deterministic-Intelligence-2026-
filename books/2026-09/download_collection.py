"""Download and restore the byte-identical Grounded DI nine-book collection.
Run with Python 3: python3 download_collection.py
Uses the Python standard library. Writes the verified ZIP to the current folder.
"""
from pathlib import Path
import hashlib
import os
import tempfile
import urllib.request

NAME = "Grounded_DI_Book_Collection_2026-09_Revised.zip"
EXPECTED = "489b0060864b76ec47b18e75ecb6d1e5193845b053e4099630d0b2815a516903"
BASE = "https://raw.githubusercontent.com/Grounded-DI/Deterministic-Intelligence-2026-/main/books/2026-09/archive/"
def main():
    target = Path.cwd() / NAME
    if target.exists():
        raise SystemExit("Output already exists; move it before restoring another copy.")
    digest = hashlib.sha256()
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".gdi-download-", delete=False) as out:
            temporary = Path(out.name)
            for number in range(1, 10):
                name = NAME + ".part" + str(number).zfill(2)
                local = Path(__file__).resolve().parent / "archive" / name
                print("Reading part", number, "of 9")
                source = local.open("rb") if local.is_file() else urllib.request.urlopen(BASE + name, timeout=120)
                with source:
                    while True:
                        block = source.read(1024 * 1024)
                        if not block:
                            break
                        digest.update(block)
                        out.write(block)
        if digest.hexdigest() != EXPECTED:
            raise SystemExit("Checksum mismatch. No final archive written.")
        if target.exists():
            raise SystemExit("Output appeared during download; refusing replacement.")
        os.rename(temporary, target)
        temporary = None
        print("Verified SHA-256:", EXPECTED)
        print("Restored:", target)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
if __name__ == "__main__":
    main()
