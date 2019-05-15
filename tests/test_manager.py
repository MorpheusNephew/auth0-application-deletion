from deletesite.manager import Auth0Manager
from deletesite.auth0wrapper import Auth0Client
from deletesite.dtos import ConnectionDto


def _mock_auth0_client_get_token(mocker):
    """Helper method to mock GetToken which is used to instantiate Auth0

    Arguments:
        mocker {pytest.mocker} -- mocking object
    """

    mocker.patch(f'deletesite.auth0wrapper.client.GetToken')


def create_connection_dtos(array_of_connection_dictionaries):
    """Helper method to create a list of connection_dto from an array of
        dictionaries

    Arguments:
        array_of_connection_dictionaries {list} -- list of dictionaries

    Returns:
        list -- list of ConnectionDto
    """

    return list(
        map(
            lambda dictionary: ConnectionDto.create_from_dict(
                dictionary),
            array_of_connection_dictionaries
        )
    )


class TestManager:
    """Test class for testing Auth0Manager
    """

    def test__delete_connections_without_connections(self, mocker):
        """Testing _Auth0Client._delete_connections is not called if the
            manager does not have any connections to delete

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_auth0_client_get_token(mocker)

        mocked_delete_connection = mocker.patch.object(
            Auth0Client._Auth0Client, 'delete_connection')

        auth0_manager = Auth0Manager()

        auth0_manager._delete_connections([])

        mocked_delete_connection.assert_not_called()

    def test__delete_connections_with_connections(self, mocker):
        """Testing _Auth0Client._delete_connections is called if the manager
            has connections to delete

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_auth0_client_get_token(mocker)

        mocked_delete_connection = mocker.patch.object(
            Auth0Client._Auth0Client, 'delete_connection')

        auth0_manager = Auth0Manager()

        connections = [{'id': 'a'}, {'id': 'b'}, {'id': 'c'}]

        connection_dtos = create_connection_dtos(connections)

        auth0_manager._delete_connections(connection_dtos)

        assert mocked_delete_connection.call_count == len(connections)
