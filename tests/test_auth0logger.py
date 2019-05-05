# from deletesite.loggers import Auth0Logger

auth0_logger_module = 'deletesite.loggers.logger'


class TestLogger:
    """Test class testing logger code
    """

    def test_add_log_handlers_without_output_file_path(self, mocker):
        """Ensuring that file handler is not added to the list of handlers
        for the logger if no output file path is provided

        Arguments:
            mocker {pytest_mocker} -- wrapper for python mock
        """

        # TODO: Figure out mocking strategy for instance property of a nested class

        # mocked_logger = mocker.patch(f'{auth0_logger_module}.logging.Logger')

        # Auth0Logger._Auth0LoggerInstance(output_file_path=None)

        # mocked_logger.addHandler.assert_called_once()

        pass
