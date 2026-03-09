import argparse

from clean import clean
from list import list_files
from recover import recover
from remove import srm

"""
This is a simple script to remove files and directories SAFELY.
It will move the files and directories to a temporary directory before asking you for confirmation.

USAGE:
srm -clean -- delete ALL files in the "trash" directory
srm -clean (n) -- delete files older than 'n' days.
srm -clean xG -- delete files larger than 'x' GB.
srm -clean xM -- delete files larger than 'x' MB.
srm -recover (file) -- recover a file from the trash directory into current directory.
srm -recover (file) (directory) -- recover a file from the trash directory into specified directory.

ToDo:
-- ALL USAGE --
Recognition of sensible paths (e.g. /, /home/user, /home/user/Documents, /home/user/Documents/Projects, /home/user/Desktop, ...)
  - If user does "srm ." and is in /home/user/, srm WON'T delete anything.
Confirm deletion
Safe mode (keep files for 30 days)
"""


def main():
    parser = argparse.ArgumentParser(
        prog="srm", description="Smart Remove: a SAFE alternative to rm."
    )

    parser.add_argument("paths", nargs="*", help="Files or directories to be deleted.")
    parser.add_argument(
        "-c", "--clean", action="store_true", help="Clean the trash directory."
    )
    parser.add_argument(
        "-r",
        "--recover",
        metavar="FILE",
        help="Recover files from the trash directory.",
    )
    parser.add_argument(
        "-l", "--list", action="store_true", help="List files in the trash directory."
    )
    args = parser.parse_args()

    if args.clean:
        clean()
    elif args.recover:
        recover(args.recover)
    elif args.paths:
        for path in args.paths:
            srm(path)
    elif args.list:
        list_files()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
