from dataclasses import dataclass
from typing import List


@dataclass
class ConnectionDto:
    """Representation of connection data from auth0
    """

    name: str
    id: str
    strategy: str
    enabled_clients: List[str]

    @staticmethod
    def create_from_dict(dictionary):
        """Creates `ConnectionDto` from dictionary

        Arguments:
            dictionary {dict} -- dictionary with connection data from auth0

        Returns:
            ConnectionDto -- data representing an connection within auth0
        """

        return ConnectionDto(
            name=dictionary.get('name', ''),
            id=dictionary.get('id', ''),
            strategy=dictionary.get('strategy', ''),
            enabled_clients=dictionary.get('enabled_clients', [])
        )
