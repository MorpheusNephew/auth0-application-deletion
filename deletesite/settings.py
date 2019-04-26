"""Settings file specifically to load the environment files
"""

from dotenv import load_dotenv


def load_settings():
    """Loads environment variables from .env file to running environment
    """

    load_dotenv()