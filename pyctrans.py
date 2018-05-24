#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import sys

__author__ = 'Meican Yg'
__version__ = '0.1-dev'
__license__ = 'MIT'

path = os.path.join(os.getcwd(), sys.argv[1])


def _complie_project():
    from compileall import compile_dir
    compile_dir(path)


def _proc_project():
    for root, subdir, files in os.walk(path):
        for _file in files:
            if _file.endswith(".py"):
                os.remove(os.path.join(root, _file))
            if _file.endswith(".pyc") and len(_file.split(".")) == 3:
                _file_tmp = _file.replace("." + _file.split(".")[1], "")
                shutil.move(
                    os.path.join(root, _file),
                    os.path.join(os.path.dirname(root), _file_tmp))
        if root.endswith("__pycache__"):
            os.rmdir(root)


if __name__ == "__main__":
    _complie_project()
    _proc_project()
