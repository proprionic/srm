from pathlib import Path

trash_dir = Path.home() / ".trash"
trash_dir_files = trash_dir / "files"
trash_dir_metadata = trash_dir / "metadata"


def init():
    trash_dir.mkdir(exist_ok=True)
    trash_dir_files.mkdir(exist_ok=True)
    trash_dir_metadata.mkdir(exist_ok=True)
