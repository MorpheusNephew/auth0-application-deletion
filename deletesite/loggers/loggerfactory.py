from .logger import Auth0Logger
import os


class Auth0LoggerFactory:
    """Factory to get logger
    """

    @staticmethod
    def get_logger():
        """Returns logger

        Returns:
            Auth0Logger -- logger to be used for logging
        """

        return Auth0Logger(os.getenv('AUTH0_LOG_PATH', None))
