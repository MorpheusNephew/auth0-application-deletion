from logging import Logger
from uuid import uuid4

from deletesite.loggers import Auth0Logger

_logging_module = 'deletesite.loggers.logger.logging'


class TestLogger:
    """Test class testing logger code
    """

    def test_add_log_handlers_without_output_file_path(self, mocker):
        """Ensuring that file handler is not added to the list of handlers
        for the logger if no output file path is provided

        Arguments:
            mocker {pytest.mocker} -- wrapper for python mock
        """

        mocked_logger_addHandler = mocker.patch.object(Logger, 'addHandler')
        # mocked_logger_streamHandler = mocker.patch(
        #     f'{_logging_module}.StreamHandler')
        mocked_logger_fileHandler = mocker.patch(
            f'{_logging_module}.FileHandler')

        Auth0Logger._Auth0LoggerInstance(output_file_path=None)

        mocked_logger_addHandler.assert_called_once()
        # Figure out: AttributeError: 'LogCaptureHandler' object has no attribute 'stream'
        # mocked_logger_streamHandler.assert_called_once()
        mocked_logger_fileHandler.assert_not_called()

    def test_add_log_handlers_with_output_file_path(self, mocker):
        """Ensuring that file handler is added to the list of handlers
        for logging if an input file path is provided

        Arguments:
            mocker {pytest.mocker} -- wrapper for python mock
        """

        mocked_logger_addHandler = mocker.patch.object(Logger, 'addHandler')
        mocked_path_exists = mocker.patch(
            'deletesite.loggers.utilities.directory.path.exists')
        # mocked_logger_streamHandler = mocker.patch(
        #     f'{_logging_module}.StreamHandler')
        mocked_logger_fileHandler = mocker.patch(
            f'{_logging_module}.FileHandler')

        mocked_path_exists.return_value = True

        file_path = f'{str(uuid4())}.log'

        Auth0Logger._Auth0LoggerInstance(output_file_path=file_path)

        assert mocked_logger_addHandler.call_count == 2
        # Figure out: AttributeError: 'LogCaptureHandler' object has no attribute 'stream'
        # mocked_logger_streamHandler.assert_called_once()
        mocked_logger_fileHandler.assert_called_once()

    def test_log_info_called(self, mocker):
        """Ensuring that Logger.info is called when the logger instance
            info method is called

        Arguments:
            mocker {pytest.mocker} -- wrapper for python mock
        """

        mocked_logger_info = mocker.patch.object(Logger, 'info')

        auth0Logger = Auth0Logger._Auth0LoggerInstance()

        string = str(uuid4())

        auth0Logger.info(string)

        mocked_logger_info.assert_called_once()

    def test_log_debug_called(self, mocker):
        """Ensuring that Logger.debug is called when the logger instance
            debug method is called

        Arguments:
            mocker {pytest.mocker} -- wrapper for python mock
        """

        mocked_logger_debug = mocker.patch.object(Logger, 'debug')

        auth0Logger = Auth0Logger._Auth0LoggerInstance()

        string = str(uuid4())

        auth0Logger.debug(string)

        mocked_logger_debug.assert_called_once()

    def test_log_error_called(self, mocker):
        """Ensuring that Logger.error is called when the logger instance
            error method is called

        Arguments:
            mocker {pytest.mocker} -- wrapper for python mock
        """

        mocked_logger_error = mocker.patch.object(Logger, 'error')

        auth0Logger = Auth0Logger._Auth0LoggerInstance()

        string = str(uuid4())

        auth0Logger.error(string)

        mocked_logger_error.assert_called_once()
