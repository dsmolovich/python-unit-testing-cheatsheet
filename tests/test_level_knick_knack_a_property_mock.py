from unittest.mock import PropertyMock, patch
from models.user import User
from service.user import create_user

@patch.object(User, 'name', new_callable=PropertyMock)
def test_user_service(mock_user):
    mock_user.return_value = 'Jane Doe'
    assert create_user('Janette') == 'Jane Doe'
    mock_user.assert_any_call('Janette')
