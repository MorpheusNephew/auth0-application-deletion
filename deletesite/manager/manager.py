from deletesite.loggers import Auth0LoggerFactory
from deletesite.auth0wrapper import Auth0ClientFactory
import os


class Auth0Manager:
    """Manager for the site deletion process
    """

    def __init__(self):
        self.logger = Auth0LoggerFactory.get_logger()
        self.client = Auth0ClientFactory.get_auth0_client()

    def run(self):

        print('Welcome to the Auth0 Deletion App')

        while True:
            application_id = input(
                'Insert the id of the application you would like to delete: ')

            application_dto = self.client.get_application(application_id)

            connections_for_application = self._get_connections_to_delete(
                application_dto.client_id)

            answer = input(
                self._get_deletion_text(
                    application_dto,
                    connections_for_application
                )
            ).lower()

            if answer != 'y' and answer != 'yes':
                break
            else:
                print('Deletion process will now start\n\n\n')

                # TODO: Continue to flesh out deletion code

    def _get_connections_to_delete(self, application_id):
        """Gets connections associated with the application id

        Arguments:
            application_id {str} -- identifier of an auth0 application

        Returns:
            list(ConnectionDto) -- list of data that contains information
                about auth0 connections
        """

        all_connections = self.client.get_all_connections()

        excluded_connection_strategies = os.getenv(
            'AUTH0_EXCLUDE_CONNECTION_STRATEGIES', ''
        ).split(',')

        connections_for_application = list(
            filter(
                lambda connection: application_id in connection.enabled_clients
                and connection.strategy not in excluded_connection_strategies,
                all_connections
            )
        )

        return connections_for_application

    def _get_deletion_text(
        self,
        application_dto,
        connections_for_application
    ):
        """Get text to show for deleting an application

        Arguments:
            application_dto {ApplicationDto} -- data that contains information
                about an auth0 application
            connections_for_application {list(ConnectionDto)} -- list of data
                that contains information about auth0 connections

        Returns:
            str -- text to display
        """

        if not connections_for_application:
            return f'Is this the correct application ({application_dto}) you would like to delete? '
        else:
            return f'Is this the correct application ({application_dto}) and set of connections ({connections_for_application}) to delete? '