from .application import ApplicationDto
from .connection import ConnectionDto
from .user import UsersDto


class DtoCreationFactory:
    """Factory to create Dto objects from dictionaries representing resources
    from Auth0
    """

    @staticmethod
    def create_application_dto_from_dict(applicationDict):
        """Factory method to transform a dictionary to an ApplicationDto

        Arguments:
            applicationDict {dict} -- dictionary representing an application
            from Auth0

        Returns:
            ApplicationDto -- representing an application object from Auth0
        """

        return ApplicationDto.create_from_dict(applicationDict)

    @staticmethod
    def create_connection_dto_from_dict(connectionDict):
        """Factory method to transform a dictionary to a ConnectionDto

        Arguments:
            connectionDict {dict} -- dictionary representing a connection from
            Auth0

        Returns:
            ConnectionDto -- representing a connection object from Auth0
        """

        return ConnectionDto.create_from_dict(connectionDict)

    @staticmethod
    def create_users_dto_from_dict(userDict):
        """Factory method to transform a dictionary to a UsersDto

        Arguments:
            userDict {dict} -- dictionary representing a user response
            from Auth0

        Returns:
            UsersDto -- representing a users object from Auth0
        """

        return UsersDto.create_from_dict(userDict)
