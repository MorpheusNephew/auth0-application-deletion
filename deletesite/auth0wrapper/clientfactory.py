from .client import Auth0Client


class Auth0ClientFactory:
    """Factory that returns an Auth0Client
    """

    @staticmethod
    def get_auth0_client():
        """Return Auth0Client

        Returns:
            Auth0Client -- client to perform requests to delete all things
            associated with an application
        """

        return Auth0Client()
