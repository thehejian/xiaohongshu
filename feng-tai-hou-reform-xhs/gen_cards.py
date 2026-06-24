#!/usr/bin/env python3
"""Generate PNG cards from SVG using Inkscape."""
import subprocess
import sys

def run_inkscape(svg_path, png_path, size):
    """Render SVG to PNG via Inkscape."""
    cmd = [
        "inkscape",
        svg_path,
        "--export-filename=" + png_path,
        "--export-width=" + str(size[0]),
        "--export-height=" + str(size[1]),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Inkscape error for {svg_path}: {result.stderr}")
        return False
    return True

def main():
    # Cover
    run_inkscape("cover.svg", "cover.png", (1024, 1024))
    # Content cards
    for i in range(1, 5):
        svg = f"card-{i}.svg"
        png = f"card-{i}.png"
        run_inkscape(svg, png, (800, 800))

if __name__ == "__main__":
    main()
