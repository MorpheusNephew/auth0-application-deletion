from dataclasses import dataclass, field
from typing import List


@dataclass
class UserIdentityDto:
    """Representation of user identity data within auth0
    """

    connection: str
    user_id: str
    provider: str
    isSocial: bool = False

    @staticmethod
    def create_from_dict(dictionary):
        """Creates `UserIdentityDto` from dictionary

        Arguments:
            dictionary {dict} -- user identity dictionary from auth0

        Returns:
            UserIdentityDto -- data representing user identity data from auth0
        """

        return UserIdentityDto(
            connection=dictionary.get('connection', ''),
            user_id=dictionary.get('user_id', ''),
            provider=dictionary.get('provider', ''),
            isSocial=dictionary.get('isSocial', False)
        )


@dataclass
class UserDto:
    """Representation of user data within auth0
    """

    user_id: str
    given_name: str
    family_name: str
    identities: List[UserIdentityDto] = field(default_factory=List)

    @staticmethod
    def create_from_dict(dictionary):
        """Creates `UserDto` from dictionary

        Arguments:
            dictionary {dict} -- user dictionary from auth0

        Returns:
            UserDto -- data representing user data from auth0
        """

        identities = dictionary.get('identities', [])

        return UserDto(
            user_id=dictionary.get('user_id', ''),
            given_name=dictionary.get('given_name', ''),
            family_name=dictionary.get('family_name', ''),
            identities=list(map(UserIdentityDto.create_from_dict, identities))
        )


@dataclass
class UsersDto:
    """Represents response from auth0 when getting all users
    """

    start: int = 0
    limit: int = 100
    users: List[UserDto] = field(default_factory=List)
    total: int = 0

    @staticmethod
    def create_from_dict(dictionary):
        """Creates `UsersDto` from dictionary

        Arguments:
            dictionary {dict} -- response from auth0 when getting all users

        Returns:
            UsersDto -- auth0 response converted into a class
        """

        users = dictionary.get('users', [])

        return UsersDto(
            start=dictionary.get('start', 0),
            limit=dictionary.get('limit', 100),
            users=list(map(UserDto.create_from_dict, users)),
            total=dictionary.get('total', 0)
        )
