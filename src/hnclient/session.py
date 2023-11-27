from requests_cache import CachedSession
from .utils import CacheManager

class FirebaseHTTPClient:
    """
    Client object for making requests to the Hacker News Firebase API.

    :param url: URL used to make an HTTP request
    :param disable_cache: Setting for turning cache on and off
    """

    # Class-level attribute for the CachedSession instance
    session = CachedSession(
        cache_name=CacheManager.cache_name,
        backend=CacheManager.backend,
        use_cache_dir=CacheManager.use_cache_dir
    )

    def __init__(self, url: str, disable_cache: bool):
        """
        Initialize a new FirebaseHTTPClient.

        :param url: The URL for the HTTP request.
        :param disable_cache: Set to True to disable caching.
        """
        self.url = url
        self.disable_cache = disable_cache

    def __call__(self):
        """
        Make an HTTP request to the specified URL.

        :return: JSON response from the HTTP request.
        """
        with self.session.cache_disabled() if self.disable_cache else self.session:
            return self.session.get(self.url).json()


