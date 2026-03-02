#!/usr/bin/env python3
"""Convert .mobi files to .epub format using calibre's ebook-convert tool."""

import argparse
import glob
import os
import subprocess
import sys


def find_mobi_files(paths):
    """Return a list of .mobi file paths from files and/or directories."""
    mobi_files = []
    for path in paths:
        if os.path.isdir(path):
            mobi_files.extend(
                glob.glob(os.path.join(path, "**", "*.mobi"), recursive=True)
            )
        elif os.path.isfile(path):
            if path.lower().endswith(".mobi"):
                mobi_files.append(path)
            else:
                print(f"Warning: skipping '{path}' — not a .mobi file", file=sys.stderr)
        else:
            print(f"Warning: '{path}' not found", file=sys.stderr)
    return mobi_files


def convert_file(mobi_path, output_dir=None):
    """Convert a single .mobi file to .epub. Returns True on success."""
    base = os.path.splitext(mobi_path)[0]
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        epub_path = os.path.join(output_dir, os.path.basename(base) + ".epub")
    else:
        epub_path = base + ".epub"

    try:
        result = subprocess.run(
            ["ebook-convert", mobi_path, epub_path],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"[OK]   {mobi_path} -> {epub_path}")
            return True
        else:
            print(
                f"[FAIL] {mobi_path}: {result.stderr.strip() or 'ebook-convert error'}",
                file=sys.stderr,
            )
            return False
    except FileNotFoundError:
        print(
            "Error: 'ebook-convert' not found. Please install calibre: https://calibre-ebook.com/",
            file=sys.stderr,
        )
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert .mobi files to .epub using calibre's ebook-convert."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        metavar="PATH",
        help="One or more .mobi files or directories containing .mobi files.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        metavar="DIR",
        default=None,
        help="Directory to write .epub files into (default: same directory as source).",
    )
    args = parser.parse_args()

    mobi_files = find_mobi_files(args.paths)

    if not mobi_files:
        print("No .mobi files found.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(mobi_files)} .mobi file(s) to convert.\n")

    succeeded = 0
    failed = 0
    for mobi_path in mobi_files:
        if convert_file(mobi_path, args.output_dir):
            succeeded += 1
        else:
            failed += 1

    print(f"\nDone: {succeeded} succeeded, {failed} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
