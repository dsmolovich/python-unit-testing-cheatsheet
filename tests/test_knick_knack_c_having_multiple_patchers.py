from unittest.mock import Mock, patch


def connect(config):
    ...

def process(job, conection):
    ...

def disconnect(connection):
    ...

def perform_job(job, config):
    connection = connect(config)
    result = process(job, connection)
    disconnect(connection)
    return result

@patch(__name__ + '.connect')
@patch(__name__ + '.process')
@patch(__name__ + '.disconnect')
def test_perform_job(mock_disconnect, mock_process, mock_connect):
    job = {'cmd': 'pwd'}
    config = {'host': 'localhost'}
    mock_connection = Mock()
    mock_connect.return_value = mock_connection
    mock_process.return_value = '/home/user' 

    result = perform_job(job, config)

    assert result == '/home/user'
    mock_connect.assert_called_once_with(config)
    mock_process.assert_called_once_with(job, mock_connection)
    mock_disconnect.assert_called_once()
