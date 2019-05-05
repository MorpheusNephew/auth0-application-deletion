from deletesite.dtos import ApplicationDto, ConnectionDto, UserDto


class DtoCreationFactory:
    """Factory to create Dto objects from dictionaries representing resources
    from Auth0
    """

    @staticmethod
    def createApplicationDtoFromDict(applicationDict):
        """Factory method to transform a dictionary to an ApplicationDto

        Arguments:
            applicationDict {dict} -- dictionary representing an application
            from Auth0

        Returns:
            ApplicationDto -- representing an application object from Auth0
        """

        return ApplicationDto.create_from_dict(applicationDict)

    @staticmethod
    def createConnectionDtoFromDict(connectionDict):
        """Factory method to transform a dictionary to a ConnectionDto

        Arguments:
            connectionDict {dict} -- dictionary representing a connection from
            Auth0

        Returns:
            ConnectionDto -- representing a connection object from Auth0
        """

        return ConnectionDto.create_from_dict(connectionDict)

    @staticmethod
    def createUserDtoFromDict(userDict):
        """Factory method to transform a dictionary to a UserDto

        Arguments:
            userDict {dict} -- dictionary representing a user from Auth0

        Returns:
            UserDto -- representing a user object from Auth0
        """

        return UserDto.create_from_dict(userDict)
