from unittest.mock import Mock, patch, call, ANY


def slack_post(user, message):
    # real implementation
    ...

def send_slack_message(user, message: str):
    if user.has_slack_disabled():
        return
    slack_post(user, message)


@patch(__name__ + '.slack_post')
def test_message_is_sent(mock_slack_post):
    user = Mock()
    user.has_slack_disabled.return_value = False
    send_slack_message(user, "Hi")
    mock_slack_post.assert_called_once_with(user, "Hi")

@patch(__name__ + '.slack_post')
def test_message_is_not_sent(mock_slack_post):
    user = Mock(**{"has_slack_disabled.return_value": True})
    send_slack_message(user, "Hi")
    mock_slack_post.assert_not_called()

@patch(__name__ + '.slack_post')
def test_message_sent_multiple_times(mock_slack_post):
    user = Mock(**{"has_slack_disabled.return_value": False})
    send_slack_message(user, "Hi")
    mock_slack_post.assert_called_once_with(user, "Hi")
    mock_slack_post.reset_mock()
    send_slack_message(user, "What's up?")
    mock_slack_post.assert_called_once_with(user, "What's up?")
    send_slack_message(user, "Write down to you shopping list:")
    send_slack_message(user, "- eggs")
    send_slack_message(user, "- milk")
    send_slack_message(user, "- apples")
    mock_slack_post.assert_has_calls([
        call(user, 'Write down to you shopping list:'),
        call(user, '- eggs'),
        call(user, '- milk'),
        call(user, '- apples'),
    ])
    mock_slack_post.assert_has_calls([
        call(user, '- apples'),
        call(user, '- eggs'),
        call(user, 'Write down to you shopping list:'),
        call(user, '- milk'),
    ], any_order = True)

@patch(__name__ + '.slack_post')
def test_message_sent_to_anyone(mock_slack_post):
    user = Mock(**{"has_slack_disabled.return_value": False})
    send_slack_message(user, "Hi")
    mock_slack_post.assert_called_with(ANY, "Hi")