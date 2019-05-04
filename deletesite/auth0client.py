from auth0.v3 import Auth0Error
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
import os


def _get_auth0_domain():
    """Gets 'AUTH0_DOMAIN' from environment variables

    Returns:
        str -- The domain for Auth0 in environment variables
        or and empty string
    """

    return os.getenv('AUTH0_DOMAIN', '')


def _get_auth0_token():
    """Helper method to get an access token to be used to authenticate with
    the auth0 management API

    Returns:
        str -- access token for the Auth0 management API
    """

    get_token = GetToken(_get_auth0_domain())

    token = get_token.client_credentials(
        os.getenv('AUTH0_CLIENT_ID', ''),
        os.getenv('AUTH0_CLIENT_SECRET', ''),
        f"https://{_get_auth0_domain()}/api/v2/")

    return token['access_token']


def _get_auth0_client(management_auth_token):
    """Helper method that takes an access token and creates an instance of
    the Auth0 class

    Arguments:
        management_auth_token {str} -- access token for management API

    Returns:
        Auth0 -- instance of the Auth0 class
    """

    return Auth0(_get_auth0_domain(), management_auth_token)


def _perform_request(request):
    """Wrapper for requests to either return data or
    returning an error if an exception is raised

    Arguments:
        request {lambda} -- an anonymous function to be called

    Returns:
        data -- the data will either be a response from the request
        or an exception
    """

    # TODO: Determine strategy for DTO usage, logging, and handling errors
    try:
        response = request()

        if response is Auth0Error:
            print(response)
            return None
        else:
            return response
    except Exception as err:
        print(err)
        return None


class Auth0Client:
    """Singleton class representing an Auth0 wrapper

    Returns:
        _Auth0Client -- the internal auth0 client wrapper class
    """

    _instance = None

    def __new__(cls):
        if Auth0Client._instance is None:
            Auth0Client._instance = Auth0Client._Auth0Client()

        return Auth0Client._instance

    class _Auth0Client:

        def __init__(self):
            self._auth0 = _get_auth0_client(_get_auth0_token())

        def delete_application(self, application_id):
            """Deletes an auth0 application/client

            Arguments:
                application_id {str} -- id associated with the application

            Returns:
                object -- a response from auth0
            """

            return _perform_request(
                lambda: self._auth0.clients.delete(application_id)
            )

        def get_application(self, application_id):
            """Gets an auth0 application/client

            Arguments:
                application_id {str} -- id associated with the application

            Returns:
                object -- a response from auth0
            """

            return _perform_request(
                lambda: self._auth0.clients.get(application_id)
            )

        def delete_connection(self, connection_id):
            """Deletes an auth0 connection

            Arguments:
                connection_id {str} -- id associated with the connection

            Returns:
                object -- a respnose from auth0
            """

            return _perform_request(
                lambda: self._auth0.connections.delete(connection_id)
            )

        def get_all_connections(self):
            """Get all auth0 connections

            Returns:
                list(object) -- a list of auth0 connections
            """

            return _perform_request(
                lambda: self._auth0.connections.all()
            )

        def get_connection(self, connection_id):
            """Gets an auth0 connection

            Arguments:
                connection_id {str} -- id associated with the connection

            Returns:
                object -- a response from auth0
            """

            return _perform_request(
                lambda: self._auth0.connections.get(connection_id)
            )

        def delete_user(self, user_id):
            """Deletes an auth0 user

            Arguments:
                user_id {str} -- id associated with the user

            Returns:
                object -- a response from auth0
            """

            return _perform_request(
                lambda: self._auth0.users.delete(user_id)
            )
