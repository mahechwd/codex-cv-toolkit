#!/usr/bin/env python3
"""Create ignored private CV inputs from tracked public templates."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


FILE_TEMPLATES = {
    "main.example.tex": "main.tex",
    "job-description.example.txt": "job-description.txt",
}
DIRECTORY_TEMPLATES = {
    "cv-context.example": "cv-context",
}


def setup_workspace(root: Path) -> dict[str, str]:
    """Create missing private inputs without overwriting existing user files."""
    root = root.resolve()
    results: dict[str, str] = {}

    for source_name, destination_name in FILE_TEMPLATES.items():
        source = root / source_name
        destination = root / destination_name
        if not source.is_file():
            raise FileNotFoundError(f"missing tracked template: {source}")
        if destination.exists():
            results[destination_name] = "kept existing"
            continue
        shutil.copy2(source, destination)
        results[destination_name] = "created"

    for source_name, destination_name in DIRECTORY_TEMPLATES.items():
        source = root / source_name
        destination = root / destination_name
        if not source.is_dir():
            raise FileNotFoundError(f"missing tracked template directory: {source}")
        if destination.exists():
            results[f"{destination_name}/"] = "kept existing"
            continue
        shutil.copytree(source, destination)
        results[f"{destination_name}/"] = "created"

    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create ignored main.tex, job-description.txt, and cv-context/ inputs",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    try:
        results = setup_workspace(args.root)
    except OSError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    for path, status in results.items():
        print(f"{path}: {status}")
    print("Tracked *.example.* templates were not modified.")
    print("Next: paste your LaTeX CV into main.tex.")
    print("Next: paste one complete vacancy into job-description.txt.")
    print("Next: add evidence under cv-context/experience/ or cv-context/projects/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
