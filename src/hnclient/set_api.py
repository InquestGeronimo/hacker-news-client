from .utils import DataProcessor
from .session import FirebaseHTTPClient

class HTTPHandler(DataProcessor):
    """
    Handler for making API calls using the HTTPClient.

    This class inherits from DataProcessor and provides 
    a method for making API calls using an instance of 
    FirebaseHTTPClient.

    :param func: The API function to call.
    :param cache: Set to True to enable caching.
    :return: An instance of FirebaseHTTPClient.
    """

    def call_api(self, func: object, disable_cache: bool) -> FirebaseHTTPClient:
        """
        Make an API call using FirebaseHTTPClient.

        :param func: The API function to call.
        :param cache: Set to True to disagble caching.
        :return: An instance of FirebaseHTTPClient.
        """
        return FirebaseHTTPClient(func, disable_cache)()
