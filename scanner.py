from __future__ import annotations

import os
from pathlib import Path
from typing import List


def scan_folder(root: Path) -> List[Path]:
    files: List[Path] = []

    for current_root, _, filenames in os.walk(root):
        for filename in filenames:
            file_path = Path(current_root) / filename
            if file_path.is_file() and file_path.stat().st_size > 0:
                files.append(file_path)

    return sorted(files)
