

from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0

import os

_domain = os.getenv('AUTH0_DOMAIN', '')


def _get_auth0_token():

    get_token = GetToken(_domain)

    token = get_token.client_credentials(
        os.getenv('AUTH0_CLIENT_ID', ''),
        os.getenv('AUTH0_CLIENT_SECRET', ''),
        f"https://{_domain}/api/v2/")

    return token['access_token']


def _get_auth0_client(management_auth_token):
    return Auth0(_domain, management_auth_token)


class Auth0Client:

    _instance = None

    def __new__(cls):
        if Auth0Client._instance is None:
            Auth0Client._instance = Auth0Client._Auth0Client()

        return Auth0Client._instance

    class _Auth0Client:

        def __init__(self):
            self._auth0 = _get_auth0_client(_get_auth0_token())

        def delete_application(self, application_id):
            return self._auth0.clients.delete(application_id)

        def get_application(self, application_id):
            return self._auth0.clients.get(application_id)

        def delete_connection(self, connection_id):
            return self._auth0.connections.delete(connection_id)

        def get_connection(self, connection_id):
            return self._auth0.connections.get(connection_id)

        def delete_user(self, user_id):
            return self._auth0.users.delete(user_id)
