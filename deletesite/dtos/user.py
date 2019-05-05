from dataclasses import dataclass
from typing import List


@dataclass
class UserIdentityDto:
    """Representation of user identity data within auth0
    """

    connection: str
    user_id: str
    provider: str
    isSocial: bool

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
    identities: List[UserIdentityDto]

    @staticmethod
    def create_from_dict(dictionary):
        """Creates `UserDto` from dictionary

        Arguments:
            dictionary {dict} -- user dictionary from auth0

        Returns:
            UserDto -- data representing user data from auth0
        """

        identities = dictionary.get('identities', [])

        user_identity_dtos = map(UserIdentityDto.create_from_dict, identities)

        return UserDto(
            user_id=dictionary.get('user_id', ''),
            given_name=dictionary.get('given_name', ''),
            family_name=dictionary.get('family_name', ''),
            identities=user_identity_dtos
        )
