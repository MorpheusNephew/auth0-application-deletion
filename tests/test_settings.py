from deletesite.utilities import load_settings


class TestSettings:
    """Test class for settings file
    """

    def test_load_dotenv_called_when_load_settings_is_called(self, mocker):
        """Testing that load_dotenv is called when the load_settings function is called

        Arguments:
            mocker {pytest.mocker} -- wrapper for python mock
        """

        mocked_load_dotenv = mocker.patch(
            'deletesite.utilities.settings.load_dotenv')

        load_settings()

        mocked_load_dotenv.assert_called_once()
