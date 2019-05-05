from dotenv import load_dotenv
from deletesite.loggers import Auth0Logger


def load_settings(log_path=None):
    """Loads environment variables from .env file to running environment
    and initializes the logger
    """

    load_dotenv()
    Auth0Logger(log_path)
