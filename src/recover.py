import json
import shutil
from pathlib import Path

import config

"""
1. Get metadata
2. Scan metadata ---> Name, Size, Type, Original path (if needed)
3. Move files that match to their designated paths.
"""


def recover(file):
    found = False
    metadata_path = config.trash_dir_metadata
    files_path = config.trash_dir_files

    for meta_file in Path(metadata_path).iterdir():
        if not meta_file.exists():
            continue

        with open(meta_file, "r") as f:
            data = json.load(f)
        if data.get("name") == file:  # Compare names in data with the file
            found = True

            file_uuid = meta_file.stem  # get file UUID
            file_name = data.get("name")
            file_og_path = data.get("og_path")

            file_path = data.get("dest")

            shutil.move(file_path, file_og_path)
            print(f"{file} moved to {file_og_path}")
            break
    if not found:
        print(f"File {file} not found.")
