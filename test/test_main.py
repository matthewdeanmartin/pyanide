from unittest.mock import Mock, patch

import pytest

from pyanide import kill_process_by_name


@pytest.fixture()
def mock_process_list():
    mock_process_list = [Mock(info={"pid": 1, "name": "vim"}), Mock(info={"pid": 2, "name": "notepad"})]
    return mock_process_list


@patch("psutil.process_iter")
def test_kill_process(mock_process_iter, mock_process_list):
    # Mock the process list
    mock_process_iter.return_value = mock_process_list

    # Call the function
    kill_process_by_name("vim", 0, max_cycles=1)

    # Assert that the process was killed
    mock_process_list[0].kill.assert_called_once()


@patch("psutil.process_iter")
def test_not_kill_process(mock_process_iter, mock_process_list):
    # Mock the process list
    mock_process_iter.return_value = mock_process_list

    # Call the function
    kill_process_by_name("fake_process", 0, max_cycles=1)

    # Assert that the process was not killed
    mock_process_list[0].kill.assert_not_called()
    mock_process_list[1].kill.assert_not_called()
