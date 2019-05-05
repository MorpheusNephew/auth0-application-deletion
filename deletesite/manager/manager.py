from deletesite.loggers import Auth0LoggerFactory


class Auth0Manager:
    """Manager for the site deletion process
    """

    def __init__(self):
        self.logger = Auth0LoggerFactory.get_logger()

    def run(self):

        self.logger.info("Hello, what would you like to run")
