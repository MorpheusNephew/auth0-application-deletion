from deletesite.manager import Auth0Manager, Auth0ManagerFactory


class TestManagerFactory:
    """Testing ManagerFactory
    """

    def test_get_auth0_manager(self, mocker):
        """Testing getting an Auth0Manager

        Arguments:
            mocker {pytest.mocker} -- wrapper for mock
        """

        mocker.patch(f'deletesite.auth0wrapper.client.GetToken')

        returned_manager = Auth0ManagerFactory.get_auth0_manager()

        assert isinstance(returned_manager, Auth0Manager)
