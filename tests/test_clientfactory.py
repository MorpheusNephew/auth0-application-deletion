from deletesite.auth0wrapper import Auth0ClientFactory, Auth0Client


class TestClientFactory:
    """Testing client factory file
    """

    def test_get_auth0_client(self, mocker):
        """Testing to ensure that the Auth0ClientFactory returns an instance
            of _Auth0Client

        Arguments:
            mocker {pytest.mocker} -- mocking object
        """

        mocker.patch(f'deletesite.auth0wrapper.client.GetToken')

        returned_client = Auth0ClientFactory.get_auth0_client()

        assert isinstance(returned_client, Auth0Client._Auth0Client)
