from mock import patch

from hello_world import MSGS


@patch('hello_world.print_msg')
def test_failing_test(mock_call_me):
    for msg in MSGS:
        mock_call_me(msg)
    assert mock_call_me.call_count == 2


@patch('hello_world.print_msg')
def test_print_all_msgs(mock_call_me):
    for msg in MSGS:
        mock_call_me(msg)
    assert mock_call_me.call_count == len(MSGS)
