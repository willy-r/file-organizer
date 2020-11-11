import os
import sys
import shutil

from extensions import foldername


def organize_files(path: str) -> None:
    """Organize the files in the path location if exists."""
    if not os.path.isdir(path) or os.path.abspath(path) == os.getcwd():
        print(f'{sys.argv[0]}: {path}: Not a valid location')
        return

    files = [fname for fname in os.listdir(path)
             if os.path.isfile(os.path.join(path, fname))]
    extensions = {os.path.splitext(fname)[1].lstrip('.') for fname in files}

    # Create folders.
    for extension in extensions:
        folder = foldername(extension)
        new_folder = os.path.join(path, folder)
        os.makedirs(new_folder, exist_ok=True)

    # Move files to folders.
    for fname in files:
        extension = os.path.splitext(fname)[1].lstrip('.')
        folder = foldername(extension)

        src = os.path.join(path, fname)
        dest = os.path.join(path, folder, fname)
        if not os.path.exists(dest):
            shutil.move(src, dest)
            print(f'{sys.argv[0]}: {path}: Moved {fname} to {folder}')

    print(f'{sys.argv[0]}: {path}: SUCCESS! All files organized\n')


if __name__ == "__main__":
    USAGE = f'USAGE: python {sys.argv[0]} <locations>'

    locations = sys.argv[1:]
    if not locations:
        raise SystemExit(USAGE)
    try:
        for location in locations:
            organize_files(location)
    except Exception as err:
        print(err)
