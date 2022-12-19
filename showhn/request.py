from requests_cache import CachedSession
from showhn.utils import Manager

session = CachedSession(
    cache_name=Manager.cache_name, 
    backend=Manager.backend, 
    use_cache_dir=Manager.use_cache_dir
)

class HTTPClient:

    def __init__(self, url, disable_cache=False):
        self.url = url
        self.disable_cache = disable_cache

    def __call__(self):
        
        if self.disable_cache:
            with session.cache_disabled():
                return session.get(self.url).json()

        else:
            return session.get(self.url).json()
