import pytest
from io import StringIO
from main import main


@pytest.fixture
def input_file():
    return 'input.txt'


@pytest.fixture
def invalid_file():
    return 'non-existent-file.txt'


def test_command_line_arguments(monkeypatch, input_file):
    monkeypatch.setattr('sys.argv', ["", input_file])
    assert main() == None


def test_invalid_command_line_arguments(monkeypatch, invalid_file):
    monkeypatch.setattr('sys.argv', ["", invalid_file])
    assert "No such file or directory" in main()


def test_standard_input(monkeypatch, input_file):
    monkeypatch.setattr('sys.stdin', StringIO(input_file))
    assert main() == None
