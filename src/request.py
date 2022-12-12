import requests

class RequestClient:

    def __init__(self, url):
        self.url = url

    def __call__(self):
        
        response = requests.get(self.url)
        return response.json()
