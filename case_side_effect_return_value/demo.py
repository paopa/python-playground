import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_func():
    return Mock()


def test_mock_function_pytest(mock_func):
    mock_func.return_value = 42
    print(mock_func())

    mock_func.side_effect = [1, 2, 3]
    print(mock_func())
    print(mock_func())
    print(mock_func())

    mock_func.side_effect = lambda x: x + 1
    print(mock_func(1))
    print(mock_func(2))
    print(mock_func(3))

    mock_func.side_effect = Exception("test")
    try:
        mock_func()
    except Exception as e:
        print(e)
