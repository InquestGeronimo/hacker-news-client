from requests_cache import CachedSession
from hnclient.utils import Manager

from typing import List, Dict

session = CachedSession(
    cache_name=Manager.cache_name, 
    backend=Manager.backend, 
    use_cache_dir=Manager.use_cache_dir
)

class HTTPClient():

    """
    Client object for making requests to the Hacker News Firebase API.

    :param url: url used to make http request
    :param disable_cache: setting for turning cache on and off
    """

    def __init__(self, url: str, disable_cache: bool):
        self.url = url
        self.disable_cache = disable_cache

    def __call__(self):
        
        if self.disable_cache:
            with session.cache_disabled():
                return session.get(self.url).json()

        else:
            return session.get(self.url).json()
