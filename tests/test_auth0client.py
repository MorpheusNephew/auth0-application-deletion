from auth0.v3.management import Clients, Connections, Users
from deletesite.auth0wrapper import Auth0Client
from uuid import uuid4

_auth0_module = 'deletesite.auth0wrapper.client'


def _mock_internal_auth0_client_setup(mocker):
    """helper function that will be turned into method_setup

    Arguments:
        mocker {pytest.mocker} -- mocking object
    """

    mocker.patch(f'{_auth0_module}.GetToken')


class TestAuth0Client:
    """Auth0Client test class
    """

    def test_delete_application_called_with_application_id(self, mocker):
        """Testing deleting an application with an application id

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_client_delete = mocker.patch.object(Clients, 'delete')

        application_id = uuid4()

        auth0Client = Auth0Client()

        auth0Client.delete_application(application_id)

        mocked_auth0_client_delete.assert_called_once_with(application_id)

    def test_get_application_called_with_application_id(self, mocker):
        """Testing getting an application with an application id

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_client_get = mocker.patch.object(Clients, 'get')

        application_id = uuid4()

        auth0Client = Auth0Client()

        auth0Client.get_application(application_id)

        mocked_auth0_client_get.assert_called_once_with(application_id)

    def test_delete_connection_called_with_connection_id(self, mocker):
        """Testing deleting a connection with a connection id

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_connection_delete = mocker.patch.object(
            Connections, 'delete'
        )

        connection_id = uuid4()

        auth0Client = Auth0Client()

        auth0Client.delete_connection(connection_id)

        mocked_auth0_connection_delete.assert_called_once_with(connection_id)

    def test_get_all_connections_called(self, mocker):
        """Testing getting all connections

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_connections_get = mocker.patch.object(
            Connections, 'all'
        )

        auth0Client = Auth0Client()

        auth0Client.get_all_connections()

        mocked_auth0_connections_get.assert_called_once()

    def test_get_connection_called_with_connection_id(self, mocker):
        """Testing getting a connection with a connection id

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_connection_get = mocker.patch.object(Connections, 'get')

        connection_id = uuid4()

        auth0Client = Auth0Client()

        auth0Client.get_connection(connection_id)

        mocked_auth0_connection_get.assert_called_once_with(connection_id)

    def test_delete_user_called_with_user_id(self, mocker):
        """Testing deleting a user with a user id

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_user_delete = mocker.patch.object(Users, 'delete')

        user_id = uuid4()

        auth0Client = Auth0Client()

        auth0Client.delete_user(user_id)

        mocked_auth0_user_delete.assert_called_once_with(user_id)

    def test_get_all_users_called_with_connection_name(self, mocker):
        """Testing getting all users based on a connection name

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        _mock_internal_auth0_client_setup(mocker)

        mocked_auth0_user_get_all_with_connection = mocker.patch.object(
            Users, 'list')

        connection_name = str(uuid4())
        default_users_per_page = 100

        auth0Client = Auth0Client()

        auth0Client.get_all_users_with_connection(connection_name)

        mocked_auth0_user_get_all_with_connection.assert_called_once_with(
            connection=connection_name,
            per_page=default_users_per_page
        )
