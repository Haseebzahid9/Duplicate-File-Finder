from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Sequence


def format_size(size_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}" if unit != "B" else f"{int(size)} {unit}"
        size /= 1024
    return f"{size:.2f} {units[-1]}"


def build_report(root: Path, scanned_files: int, duplicates: Sequence[Dict[str, object]]) -> str:
    duplicate_files = sum(int(group["copies"]) for group in duplicates)
    duplicate_groups = len(duplicates)
    wasted_space = sum(
        (int(group["copies"]) - 1) * int(group["size_bytes"])
        for group in duplicates
    )

    lines = [
        "=" * 36,
        "Duplicate File Finder",
        "=" * 36,
        f"Scanned path: {root}",
        f"Files scanned: {scanned_files}",
        f"Duplicate groups: {duplicate_groups}",
        f"Duplicate files: {duplicate_files}",
        f"Space wasted: {format_size(wasted_space)}",
        "",
    ]

    if not duplicates:
        lines.append("No duplicate files found.")
        return "\n".join(lines)

    for group in duplicates:
        file_hash = str(group["hash"])
        files = list(group["files"])
        lines.append(f"Hash: {file_hash}")
        lines.append("Files:")
        for file_path in files:
            try:
                display_path = file_path.relative_to(root).as_posix()
            except ValueError:
                display_path = file_path.as_posix()
            lines.append(f"  - {display_path}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_report(output_path: Path, report_text: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_text, encoding="utf-8")
