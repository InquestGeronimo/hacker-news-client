import requests

class HTTPClient:

    def __init__(self, url):
        self.url = url

    def __call__(self):
        
        response = requests.get(self.url)
        return response.json()
