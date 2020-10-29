import os
import shutil
import sys

from ext import foldername

FILE_NAME = "organize.py"
EXT_NAME = "ext.py"


def organize_files(path: str) -> None:
    if not os.path.exists(path):
        print(f"{sys.argv[0]}: {path}: Invalid location")
        return

    files = os.listdir(path)
    extns = {os.path.splitext(f)[1].strip(".") for f in files}

    # Create Folders
    for ext in extns:
        folder = foldername(ext) or ''
        new = os.path.join(path, folder)
        if folder and not os.path.exists(new):
            os.makedirs(new)

    # Move Files To Folders
    for f in files:
        if f in [FILE_NAME, EXT_NAME]:
            continue

        ext = os.path.splitext(f)[1].strip(".")
        folder = foldername(ext)
        if not folder:
            continue

        src = os.path.join(path, f)
        dest = os.path.join(path, folder, f)

        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f"{sys.argv[0]}: {path}: Moved {f} to {folder}")

    print(f"{sys.argv[0]}: {path}: SUCCESS! All files organized\n")


if __name__ == "__main__":
    USAGE = f"USAGE: python {sys.argv[0]} <location>"

    locations = sys.argv[1:]
    if not locations:
        raise SystemExit(USAGE)
    try:
        for location in locations:
            organize_files(location)
    except Exception as err:
        print(err)
