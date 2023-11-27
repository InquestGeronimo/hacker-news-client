from .utils import DataProcessor
from .session import FirebaseHTTPClient

class HTTPHandler(DataProcessor):

        def call_api(self, func: object, cache: bool) -> FirebaseHTTPClient:

            return FirebaseHTTPClient(func, cache)()