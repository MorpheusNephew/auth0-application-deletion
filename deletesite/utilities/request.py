from auth0.v3 import Auth0Error
# from deletesite.dtos.factories import DtoCreationFactory


def perform_request(request, process=None):
    """Wrapper for requests to either return data or
    returning an error if an exception is raised

    Arguments:
        request {lambda} -- an anonymous function to be called

    Returns:
        data -- the data will either be a response from the request
        or an exception
    """

    # TODO: Determine strategy for DTO usage, logging, and handling errors
    try:
        response = request()

        if response is Auth0Error:
            print(response)
            return None

        if process is None:
            return response
        else:
            return process(response)
    except Exception as err:
        print(err)
        return None
