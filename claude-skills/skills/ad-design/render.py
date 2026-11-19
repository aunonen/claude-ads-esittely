"""Render HTML ad designs to PNG with headless Chrome/Edge.

Usage:
    python render.py DESIGN.html [DESIGN2.html ...] [--sizes sq,vt,hz] [--out DIR] [--date DD-MM-YYYY]

Each design is one HTML file with all three sizes in it; the size is picked by
the URL hash (#sq, #vt, #hz), which base.css turns into the frame size.
Output: <out>/<DesignName>-SQ_<date>.png (and -VT, -HZ).
Defaults: all three sizes, out = the folder above the design file, date = today.

Copies base.css next to the design before rendering, so designs always use the
current shared version. Needs no Python packages, only Chrome, Chromium or Edge.
"""
import argparse
import datetime
import os
import shutil
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

SIZES = {"sq": (1080, 1080), "vt": (1080, 1920), "hz": (1920, 1080)}
HERE = Path(__file__).resolve().parent

BROWSER_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]


def find_browser():
    env = os.environ.get("CHROME_PATH")
    if env and Path(env).exists():
        return env
    for c in BROWSER_CANDIDATES:
        if Path(c).exists():
            return c
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No Chrome/Chromium/Edge found. Set CHROME_PATH to the browser executable.")


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def render(browser, design, size, out_png):
    w, h = SIZES[size]
    url = design.resolve().as_uri() + "#" + size
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--no-first-run",
            "--no-default-browser-check",
            "--force-device-scale-factor=1",
            "--allow-file-access-from-files",
            f"--user-data-dir={profile}",
            f"--window-size={w},{h}",
            "--virtual-time-budget=10000",  # lets web fonts and images finish loading
            f"--screenshot={out_png}",
            url,
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    got = png_size(out_png) if out_png.exists() else None
    if got != (w, h):
        return f"FAILED {out_png.name}: expected {w}x{h}, got {got}"
    return f"OK {out_png.name} ({w}x{h})"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("designs", nargs="+")
    p.add_argument("--sizes", default="sq,vt,hz")
    p.add_argument("--out")
    p.add_argument("--date", default=datetime.date.today().strftime("%d-%m-%Y"))
    a = p.parse_args()

    browser = find_browser()
    sizes = [s.strip().lower() for s in a.sizes.split(",") if s.strip()]
    for s in sizes:
        if s not in SIZES:
            sys.exit(f"Unknown size {s!r}; use sq, vt, hz")

    failed = False
    for d in a.designs:
        design = Path(d)
        if not design.exists():
            print(f"FAILED {d}: file not found")
            failed = True
            continue
        shutil.copyfile(HERE / "base.css", design.parent / "base.css")
        out_dir = Path(a.out) if a.out else design.parent.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        for s in sizes:
            out_png = (out_dir / f"{design.stem}-{s.upper()}_{a.date}.png").resolve()
            if out_png.exists():
                out_png.unlink()
            line = render(browser, design, s, out_png)
            failed |= line.startswith("FAILED")
            print(line)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
