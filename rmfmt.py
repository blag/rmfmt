#!python
import os
from pathlib import Path


VCS_DIRS = [
    ".git",
    ".hg",
    ".fossil",
    ".svn",
    ".cvs",
    ".rcs",
]


def main(*args):
    args = [Path(arg) for arg in args] if args else [Path(".").parent]
    files = []
    for entity in args:
        if os.path.isdir(str(entity)):
            for f in entity.rglob("*.py"):
                if any([str(f).replace(f'{entity}/', '').lower().startswith(vcs_dir) for vcs_dir in VCS_DIRS]):
                    continue
                files.append(f)
        else:
            files.append(entity)

    for f in files:
        f.write_text('')


if __name__ == "__main__":  # pragma: nocover
    import sys
    main(*sys.argv[1:])
