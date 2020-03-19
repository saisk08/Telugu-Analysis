import sys
import os


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)


this_dir = os.path.dirname(__file__)
utils_path = os.path.join(this_dir, 'utils')
add_path(utils_path)
