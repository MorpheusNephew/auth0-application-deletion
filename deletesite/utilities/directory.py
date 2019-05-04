"""Directory utilities
"""

from os import path, makedirs


def ensure_directory_exists(file_path):
    """Creates directory if it does not exist

    Arguments:
        file_path {str} -- file path to check to see if the directory exists
    """

    dir_path = path.dirname(path.abspath(file_path))
    exists = path.exists(dir_path)

    if not exists:
        makedirs(dir_path)
