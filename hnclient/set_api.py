from hnclient.utils import Manager
from hnclient.client import HTTPClient

class HTTPHandler(Manager):

        def call_api(self, func: object, cache: bool):

            return HTTPClient(func, cache)()