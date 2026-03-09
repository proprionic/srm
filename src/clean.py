import os
import shutil

import config

config.init()


def clean():
    trash_files = os.listdir(config.trash_dir_files)
    metadata_files = os.listdir(config.trash_dir_metadata)
    try:
        if len(trash_files) == 0:
            print("Trash is empty! good job.")
        elif len(trash_files) > 0:
            print("deleting files..")
            for file in trash_files:
                if not os.path.isdir(os.path.join(config.trash_dir_files, file)):
                    os.remove(os.path.join(config.trash_dir_files, file))
                else:
                    shutil.rmtree(os.path.join(config.trash_dir_files, file))
            for file in metadata_files:
                os.remove(os.path.join(config.trash_dir_metadata, file))
    except Exception as e:
        print(f"An error occurred: {e}")
