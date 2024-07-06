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


class Klass:
    def __init__(self, a: int):
        self._a = a

    def sum(self, b: int) -> int:
        return self._a + b

class AnotherClass:
    def some_method(self):
        obj = Klass(a=2)
        return obj.sum(b=3)

def test_another_class():
    sut = AnotherClass()
    assert sut.some_method() == 5

@patch("tests.test_level_5_mocking_imports_with_patch.Klass")
def test_another_class_with_patched_Klass(some_class):
    some_class.return_value.sum.return_value = 10

    sut = AnotherClass()
    assert sut.some_method() == 10

    some_class.assert_called_once_with(a=2)
    some_class.return_value.sum.assert_called_once_with(b=3)



"""
How to mock a module that imports the package that is not installed:

The import below will fail with the:
E   ModuleNotFoundError: No module named 'gravity'
Instead patch the 'sys.modules' dictionary with the non-existing module then import
"""
# from etc.module_importing_not_installed_package import GravityController

def test_gravity_controller_adjust():
    mock_gravity_module = Mock()
    mock_gravity_module.GravityField.return_value.set_curvature_radius.return_value = True
    with patch.dict('sys.modules', {'gravity': mock_gravity_module}):               # <--- patch
        from etc.module_importing_not_installed_package import GravityController    # <--- then import
        sut = GravityController()
    sut.adjust(curvature_radius=2.5)
    mock_gravity_module.GravityField.return_value.set_curvature_radius(value=2.5)
    