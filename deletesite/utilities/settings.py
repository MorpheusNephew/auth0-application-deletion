from dotenv import load_dotenv
from deletesite.loggers import Auth0Logger
import os


def load_settings():
    """Loads environment variables from .env file to running environment
    and initializes the logger
    """

    load_dotenv()
    Auth0Logger(os.getenv('AUTH0_LOG_PATH', None))
