from deletesite.loggers import Auth0LoggerFactory


def perform_request(request, process=None):
    """Wrapper for requests to either return data or
    returning an error if an exception is raised

    Arguments:
        request {lambda} -- an anonymous function to be called

    Returns:
        data -- the data will either be a response from the request
        or an exception
    """

    logger = Auth0LoggerFactory.get_logger()

    try:
        response = request()

        data = None
        if process is None:
            data = response
        else:
            data = process(response)

        logger.info(f'Retrieved data: {data}')
        return data
    except Exception as err:
        logger.error(err)
        raise
