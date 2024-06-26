import os
import pytest

from cd import cd
from exceptions import NotDirectoryError

"""
./tests/test_filesystem
├── dir_empty
├── dir_with_contents
│   ├── subdir_empty
│   ├── subdir_with_contents
│   │   └── test3.txt
│   └── test2.txt
└── test.txt
"""

@pytest.fixture
def valid_directory():
    return "./tests/test_filesystem"

@pytest.fixture
def invalid_path_name():
    return "unknown_path"

@pytest.fixture
def text_file():
    return "./tests/test_filesystem/test.txt"

def abs_path(path: str) -> str:
    return os.path.abspath(path)

def test_cd_for_valid_path(valid_directory: str, reset_cwd: str):
    intended_directory = abs_path(os.path.join(os.getcwd(), valid_directory))
    assert cd(valid_directory) == abs_path(os.getcwd())
    assert abs_path(os.getcwd()) == intended_directory

def test_cd_for_non_existed_filepath_raises_error(invalid_path_name, reset_cwd: str):
    with pytest.raises(FileNotFoundError) as exception_info:
        cd(invalid_path_name)
    error_message = str(exception_info.value)
    assert error_message == f"no such file or directory: {invalid_path_name}"

def test_cd_for_a_file_raises_error(text_file, reset_cwd: str):
    with pytest.raises(NotDirectoryError) as exception_info:
        cd(text_file)
    error_message = str(exception_info.value)
    assert error_message == f"not a directory: {text_file}"
