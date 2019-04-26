"""Test file for directory utilities
"""

from deletesite.utilities.directory import ensure_exists

from os import path

directory_module = 'deletesite.utilities.directory'


def test_creating_directory_if_none_present(mocker):
    """Test asserts directory does not exist then tests that the
    `ensure_exists` method creates the directory and removes the
    directory in cleanup
    """

    mocked_makedirs = mocker.patch(f'{directory_module}.makedirs')
    mocked_path = mocker.patch(f'{directory_module}.path')

    dir_path = 'test'
    file_path = path.join(dir_path, 'test.log')

    mocked_path.dirname.return_value = dir_path
    mocked_path.exists.return_value = False

    ensure_exists(file_path)

    mocked_makedirs.assert_called_once_with(dir_path)


def test_should_not_error_when_attempting_to_create_an_existing_directory(mocker):
    """Test asserts that directory `ensure_exists` method does not error if
    directory already exists
    """

    mocked_makedirs = mocker.patch(f'{directory_module}.makedirs')
    mocked_exists = mocker.patch(f'{directory_module}.path.exists')

    mocked_exists.return_value = True

    ensure_exists('file path')

    mocked_makedirs.assert_not_called()
