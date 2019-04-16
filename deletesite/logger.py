"""A singleton logger
"""

import logging
from deletesite.utilities import directory


class Auth0Logger:
    """Logger to log information to the console as well as a file if user chooses
    """

    instance = None

    def __new__(cls, output_file_path=None):

        if not Auth0Logger.instance:
            Auth0Logger.instance = Auth0Logger._Auth0LoggerInstance(
                output_file_path)

        return Auth0Logger.instance

    class _Auth0LoggerInstance:
        """Logger instance to be used for singleton
        """

        def __init__(self, output_file_path):

            self.logger = logging.getLogger('auth0_log')

            self.add_log_handlers(output_file_path)

        def info(self, msg):
            """logs info message

            Arguments:
                msg {str} -- info message to be logged
            """

            self.logger.info(msg)

        def error(self, msg):
            """logs error message

            Arguments:
                msg {str} -- error message to be logged
            """

            self.logger.error(msg)

        def debug(self, msg):
            """logs debug message

            Arguments:
                msg {str} -- debug message to be logged
            """

            self.logger.debug(msg)

        def add_log_handlers(self, output_file_path):
            """Adds log handlers to be used for logging

            Arguments:
                outputFilePath {str} -- file path to save logging to
            """

            self.logger.setLevel(logging.DEBUG)

            if output_file_path is not None:
                directory.ensure_exists(output_file_path)
                self.logger.addHandler(logging.FileHandler(output_file_path))

            self.logger.addHandler(logging.StreamHandler())
