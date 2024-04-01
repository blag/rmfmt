#!python
import os
import sys
from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree

sys.path.append(str(Path(__file__).parent.parent))

from rmfmt import main as rmfmt, VCS_DIRS


def ignore_testdir(directory, *contents):
    if directory == "./tests/testdir" or directory.startswith("./tests/testdir/"):
        return contents[0]
    return []


def rlistdir(top):
    rtn = []
    for root, dirs, files in os.walk(top, topdown=False):
        rtn.extend([os.path.join(root, name) for name in files])
        for dir_ in dirs:
            rtn.extend(rlistdir(os.path.join(root, dir_)))
    return rtn


def test_rmfmt():
    if os.path.exists(os.path.join(os.getcwd(), 'tests', 'testdir')):
        rmtree("tests/testdir")
    copytree(".", "tests/testdir", ignore=ignore_testdir)
    Path("./tests/testdir/.git/something.py").write_text("import os")
    snapshot = {
        f: os.path.getsize(f)
        for f in rlistdir("./tests/testdir")
    }
    rmfmt("tests/testdir")
    for f in rlistdir("./tests/testdir"):
        if f.endswith(".py") and f != "./tests/testdir/.git/something.py":
            assert os.path.getsize(f) == 0
        else:
            assert os.path.getsize(f) == snapshot[f]


if __name__ == "__main__":
    test_rmfmt()
