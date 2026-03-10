import json
import os
import shutil
import uuid
from datetime import datetime
from pathlib import Path

import config


def srm(file):

    trash_dir_files = config.trash_dir_files
    trash_dir_metadata = config.trash_dir_metadata

    file_type = None
    metadata = None
    delpath = os.getcwd()
    delfile = os.path.join(delpath, f"{file}")
    file_id = str(uuid.uuid4())
    del_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    destination = trash_dir_files / f"{file_id}{Path(file).suffix}"
    metadata_path = trash_dir_metadata / f"{file_id}.json"
    if os.path.isfile(delfile):
        file_type = "file"

    elif os.path.isdir(delfile):
        file_type = "folder"

    else:
        print(f"{delfile} doesn't exist")
        return

    metadata = {
        "UUID": file_id,
        "dest": str(destination),
        "og_path": str(delfile),
        "del_time": del_time,
        "type": file_type,
        "name": file,
        "size": os.path.getsize(file),
    }

    shutil.move(delfile, destination)
    print(f"File UUID: {file_id}")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f)
    print("Metadata created.")

    return metadata
