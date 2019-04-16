"""Test file for directory utilities
"""


from unittest import TestCase
from os import makedirs, removedirs, path
import deletesite.utilities.directory as dr


class DirectoryTests(TestCase):
    """DirectoryTests class that will test use cases for directory utilities

    Arguments:
        TestCase {TestCase} -- class to be inherited to run unit tests
    """

    def test_creating_directory_if_none_present(self):
        """Test asserts directory does not exist then tests that the `ensure_exists` method creates
        the directory and removes the directory in cleanup
        """

        dir_path = path.join(path.dirname(__file__), "a", "b")
        file_path = path.join(dir_path, "c.txt")

        self.assertFalse(path.exists(dir_path))

        dr.ensure_exists(file_path)

        self.assertTrue(path.exists(dir_path))

        removedirs(dir_path)

    def test_should_not_error_when_attempting_to_create_an_existing_directory(self):
        """Test asserts that directory `ensure_exists` method does not error if
        directory already exists
        """

        dir_path = path.join(path.dirname(__file__), "x", "y")
        file_path = path.join(dir_path, "z.txt")

        makedirs(dir_path)

        self.assertIsNot(OSError, dr.ensure_exists(file_path))

        removedirs(dir_path)
