from unittest.mock import Mock, patch
from slack.sending import send_slack_msg
from slack_lib.slack_api import SlackAPI

"""
The chain of calls:
slack.sending.send_slack_msg() 
    -> a_lib.aaa.A_slack_post()
        -> b_lib.bbb.B_slack_post()
            -> c_lib.ccc.C_slack_post()
                -> slack_lib.slack_api.slack_post()
                    -> slack_lib.slack_api.Slack_API.post()
"""

@patch('c_lib.ccc.slack_post')
def test_send_with_slack_post_patched(mock_slack_post):
    send_slack_msg(Mock())
    mock_slack_post.assert_called()

@patch('b_lib.bbb.C_slack_post')
def test_send_with_C_slack_post_patched(mock_slack_post):
    send_slack_msg(Mock())
    mock_slack_post.assert_called()

@patch('a_lib.aaa.B_slack_post')
def test_send_with_B_slack_post_patched(mock_slack_post):
    send_slack_msg(Mock())
    mock_slack_post.assert_called()

@patch('slack.sending.A_slack_post')
def test_send_with_A_slack_post_patched(mock_slack_post):
    send_slack_msg(Mock())
    mock_slack_post.assert_called()

@patch('slack_lib.slack_api.SlackAPI.post')
def test_send_with_SlackApi_post_patched(mock_slack_post):
    send_slack_msg(Mock())
    mock_slack_post.assert_called()

@patch.object(SlackAPI, 'post')
def test_send_with_SlackApi_object_patched(mock_slack_post):
    send_slack_msg(Mock())
    mock_slack_post.assert_called()
