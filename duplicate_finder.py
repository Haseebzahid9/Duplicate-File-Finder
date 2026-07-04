from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple

from config import DEFAULT_REPORT_PATH
from hash_utils import calculate_sha256
from report import build_report, write_report
from scanner import scan_folder


def find_duplicates(root: Path) -> Tuple[int, List[Dict[str, object]]]:
    file_paths = scan_folder(root)
    grouped_files: Dict[str, List[Path]] = {}

    for file_path in file_paths:
        try:
            file_hash = calculate_sha256(file_path)
        except (PermissionError, OSError):
            continue

        grouped_files.setdefault(file_hash, []).append(file_path)

    duplicate_groups: List[Dict[str, object]] = []
    for file_hash, files in grouped_files.items():
        if len(files) > 1:
            size_bytes = files[0].stat().st_size
            duplicate_groups.append(
                {
                    "hash": file_hash,
                    "files": files,
                    "size_bytes": size_bytes,
                    "copies": len(files),
                }
            )

    duplicate_groups.sort(key=lambda item: len(item["files"]), reverse=True)
    return len(file_paths), duplicate_groups


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Find duplicate files in a folder")
    parser.add_argument("--path", type=Path, default=Path.cwd(), help="Folder to scan")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional report output path (defaults to reports/duplicate_report.txt)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.path.expanduser().resolve()

    if not target.exists():
        print(f"The path '{target}' does not exist.")
        return 1

    if not target.is_dir():
        print(f"'{target}' is not a folder.")
        return 1

    scanned_files, duplicates = find_duplicates(target)
    report_text = build_report(target, scanned_files, duplicates)
    print(report_text)

    output_path = args.output.expanduser() if args.output else DEFAULT_REPORT_PATH
    if not output_path.is_absolute():
        output_path = (Path.cwd() / output_path).resolve()

    write_report(output_path, report_text)
    print(f"\nReport saved to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
