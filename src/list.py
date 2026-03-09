import json
from pathlib import Path

import config


def list_files():
    files_path = config.trash_dir_files
    metadata_path = config.trash_dir_metadata

    rows = []

    # load all metadata
    for file in Path(files_path).iterdir():
        if not file.is_file():  # skip directories
            continue

        file_id = file.stem  # just the UUID, no extension
        file_metadata = metadata_path / f"{file_id}.json"

        if not file_metadata.exists():
            continue  # skip files without metadata

        with open(file_metadata, "r") as f:
            metadata = json.load(f)
            rows.append(
                {
                    "name": metadata["name"],
                    "size": str(metadata["size"]),
                    "og_path": metadata["og_path"],
                    "type": metadata["type"],
                }
            )

    if not rows:
        print("Trash is empty!")
        return

    # calc max width of each column
    name_width = max(len(r["name"]) for r in rows + [{"name": "Name"}])
    size_width = max(len(r["size"]) for r in rows + [{"size": "Size"}])
    path_width = max(len(r["og_path"]) for r in rows + [{"og_path": "Original Path"}])
    type_width = max(len(r["type"]) for r in rows + [{"type": "Type"}])

    # print header
    print("-" * (5 + name_width + size_width + path_width + type_width + 9))
    print(
        f"{'ID':<3} {'Name':<{name_width}} | {'Size':<{size_width}} | {'Original Path':<{path_width}} | {'Type':<{type_width}}"
    )
    print("-" * (5 + name_width + size_width + path_width + type_width + 9))

    # print rows
    for i, r in enumerate(rows, start=1):
        # optional: truncate long names
        name_display = (r["name"][:50] + "...") if len(r["name"]) > 50 else r["name"]
        og_path_display = (
            (r["og_path"][:70] + "...") if len(r["og_path"]) > 70 else r["og_path"]
        )

        print(
            f"{i:<3}. {name_display:<{name_width}} | {r['size']:<{size_width}} | {og_path_display:<{path_width}} | {r['type']:<{type_width}}"
        )

    print("-" * (5 + name_width + size_width + path_width + type_width + 9))
