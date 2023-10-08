from unittest.mock import Mock, patch
import pytest
from typing import List
from logging import Logger

# ============
def fetch_one_page_of_slack_channels(cursor=None):
    channels = []
    next_page_cursor = None
    return channels, next_page_cursor


def fetch_all_slack_channels():
    all_channels: List[str] = []
    fetched_all_pages = False
    cursor = None
    while not fetched_all_pages:
        new_channels, cursor = fetch_one_page_of_slack_channels(cursor)
        all_channels.extend(new_channels)
        fetched_all_pages = bool(cursor is None)
    return all_channels


# ============
class SocialAlreadyClaimedException(Exception):
   pass


def connect_github_account(user, github_uid):
  try:
    user.social_accounts.add("github", github_uid)
  except SocialAlreadyClaimedException as exc:
    return False, "Sorry, we could not connect you"
  ...


# ============
def create_url(endpoint, org_slug=None, user_slug=None):
   # real implementation:
   ...

def menu_urls(user):
    org_settings_url = create_url(endpoint="org_settings", org_slug=user.org.slug)
    dashboard_url = create_url(endpoint="dashboard")
    user_settings_url = create_url(endpoint="user_settings", org_slug=user.org.slug, user_slug=user.slug)
    ...
    return [org_settings_url, dashboard_url, user_settings_url]

# ============
class Configuration:
    # real implementation:
    ...

def create_config(user) -> Configuration:
    config = Configuration()
    if user.can_read():
        config.set('literate', True)
    if user.can_jump():
        config.set('springy', True)
    ...
    return config


# side_effect as an iterator
@patch(__name__ + '.fetch_one_page_of_slack_channels') # use __name__ reference with '.<function>' for pathcing functions 
                                                       # sitting in the same module
def test_fetch_all_slack_channels(mock_fetch_one_page_of_slack_channels):
    mock_fetch_one_page_of_slack_channels.side_effect=[
        (["channel #1","channel #2"], "__NEXT__PAGE__"),
        (["channel #3"], None),]
    assert fetch_all_slack_channels() == ['channel #1', 'channel #2', 'channel #3']


# side_effect as exception
def test_connect_github_account_fails():
    user = Mock()
    user.social_accounts.add.side_effect = SocialAlreadyClaimedException
    result, message = connect_github_account(user, 'some_github_id')
    assert result == False
    assert message == "Sorry, we could not connect you"


# side_effect as a substitute function (not a mock object)
def substitute_create_url(endpoint, **kwargs):
   return f'{endpoint} WITH {kwargs}'

def test_menu_urls_with_substitution_function():
    user = Mock(**{
        'slug': '__USER_SLUG__',
        'org.slug': '__ORG_SLUG__',
    })
    with patch(__name__ + '.create_url', substitute_create_url) as p:
        assert menu_urls(user) == [
           "org_settings WITH {'org_slug': '__ORG_SLUG__'}",
           "dashboard WITH {}",
           "user_settings WITH {'org_slug': '__ORG_SLUG__', 'user_slug': '__USER_SLUG__'}"]

# side_effect as a substitute function (not a mock object)
class SubstituteConfiguration:
    def __init__(self):
        self._config = {}

    def set(self, key, value):
        self._config[key] = value
    
    def get(self, key):
        return self._config[key]


@patch(__name__ + '.Configuration')
def test_menu_urls_with_substitution_class(mock_config):
    mock_config.side_effect = SubstituteConfiguration
    user_1 = Mock()
    user_2 = Mock(**{'can_read.return_value': False})
    user_3 = Mock(**{'can_read.return_value': False, 'can_jump.return_value': False})

    config_1 = create_config(user_1)
    assert config_1._config == {'literate': True, 'springy': True}
    config_2 = create_config(user_2)
    assert config_2._config == {'springy': True}
    config_3 = create_config(user_3)
    assert config_3._config == {}
