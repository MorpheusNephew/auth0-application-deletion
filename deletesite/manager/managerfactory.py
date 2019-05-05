from .manager import Auth0Manager


class Auth0ManagerFactory:

    @staticmethod
    def get_auth0_manager():
        """Gets an auth0 manager

        Returns:
            Auth0Manager -- manages the auth0 process for deleting a site
        """

        return Auth0Manager()
