from deletesite.utilities.request import perform_request
import pytest
from logging import Logger


class TestRequest:
    def test_perform_request_without_proccessing_successfully(self):
        """Testing that when a request is performed the data returns successfully
        """

        assert perform_request(lambda: True)

    def test_perform_request_with_processing_successfully(self):
        """Testing that when a request is performed if a processing method is
            sent as a variable some conversion should take place and data
            returned successfully
        """

        assert perform_request(lambda: False, lambda _: True)

    def test_perform_request_that_raises_error(self, mocker):
        """Testing that when a request returns an exception it gets logged and
            re-raised

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        mocked_request = mocker.Mock(side_effect=Exception("request error"))

        mocked_logger_error = mocker.patch.object(Logger, 'error')

        with pytest.raises(Exception):
            perform_request(mocked_request)

        mocked_logger_error.assert_called_once()
