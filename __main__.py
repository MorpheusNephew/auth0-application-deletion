"""Main file that will be run when the command `python .` is ran
"""

from deletesite.utilities import load_settings
from deletesite.manager import Auth0ManagerFactory


def main():
    load_settings()

    auth0_manager = Auth0ManagerFactory.get_auth0_manager()

    auth0_manager.run()


if __name__ == "__main__":
    main()
