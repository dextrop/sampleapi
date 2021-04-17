import logging
class LoggingMixin(object):
    """
    Provides full logging of requests and responses
    """
    def __init__(self):
        self.logger = logging.getLogger('django')
        self.log_data = None

    def initial(self, request, *args, **kwargs):
        try:
            self.logger.debug({"request": request.data, "method": request.method, "endpoint": request.path})
        except:
            self.logger.debug({"request": dict(), "method": request.method, "endpoint": request.path})

        super(LoggingMixin, self).initial(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        self.logger = logging.getLogger('django')
        self.logger.debug(response.data)
        return super(LoggingMixin, self).finalize_response(request, response, *args, **kwargs)
