from dataclasses import dataclass


@dataclass
class ApplicationDto:
    """Representation of application data from auth0
    """

    name: str
    client_id: str

    @staticmethod
    def create_from_dict(dictionary):
        """Creates `ApplicationDto` from dictionary

        Arguments:
            dictionary {dict} -- dictionary with application data from auth0

        Returns:
            ApplicationDto -- data representing an application within auth0
        """

        return ApplicationDto(
            name=dictionary.get('name', ''),
            client_id=dictionary.get('client_id', '')
        )
