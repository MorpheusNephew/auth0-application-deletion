from auth0.v3.management import Clients, Connections, Users

from deletesite.auth0client import Auth0Client, _perform_request

from uuid import uuid4

_auth0_module = 'deletesite.auth0client'


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
            Connections, 'delete')

        connection_id = uuid4()

        auth0Client = Auth0Client()

        auth0Client.delete_connection(connection_id)

        mocked_auth0_connection_delete.assert_called_once_with(connection_id)

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

    def test__perform_request_with_successful_request(self):
        """Testing the helper method for performing requests to ensure that
        the DTO's data property is filled
        """

        pass

    def test__perform_request_with_unsuccessful_request(self):
        """Testing the helper method for performing requests to ensure that
        the DTO's error property is filled
        """

        pass

    def test__perform_request_with_exception_in_request(self):
        """Testing the helper method for performing requests to ensure that
        an exception is caught if one were to occur
        """

        pass
