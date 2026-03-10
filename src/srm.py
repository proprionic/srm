import argparse

import config
from clean import clean
from list import list_files
from recover import recover
from remove import srm

config.init()


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
