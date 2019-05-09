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
        # mocked_logger_streamHandler = mocker.patch(
        #     f'{_logging_module}.StreamHandler')
        mocked_logger_fileHandler = mocker.patch(
            f'{_logging_module}.FileHandler')

        file_path = f'{str(uuid4())}.log'

        Auth0Logger._Auth0LoggerInstance(output_file_path=file_path)

        assert mocked_logger_addHandler.call_count == 2
        # Figure out: AttributeError: 'LogCaptureHandler' object has no attribute 'stream'
        # mocked_logger_streamHandler.assert_called_once()
        mocked_logger_fileHandler.assert_called_once()
