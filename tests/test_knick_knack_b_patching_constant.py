from unittest.mock import patch
from messages.messages import get_latest_messages

@patch('messages.messages.MSG_LIMIT', new=3)
def test_get_latest_messages():
    assert get_latest_messages() == 'getting 3 latest messages'
