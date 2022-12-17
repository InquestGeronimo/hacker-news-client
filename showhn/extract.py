from showhn.utils import Manager
from showhn.request import HTTPClient

from typing import List, Dict

class ShowHN(Manager):
    def __init__(self):

        super().__init__()
        
    def get_payload(
        self, 
        descending: bool=False, 
        disable_cache: bool=False
    ) -> List[Dict]:

        uids = HTTPClient(self.post_ids_url, disable_cache)()

        payload = []
        for uid in uids:
            data = HTTPClient(self.get_post(uid), disable_cache)()

            try:
                payload.append(
                    {
                        "id":        uid,
                        "title":     data["title"],
                        "text":      data["text"][:135] + "...",
                        "url":       data["url"],
                        "comments":  data["descendants"],
                        "score":     data["score"],
                        "time":      data["time"],
                        "hacker":    data["by"]
                    }
                )

            except KeyError:
                continue

        """ sorts dictionary by 'score' in descending order"""
        return sorted(payload, key=lambda d: d["score"], reverse=descending)

    
    def get_ids(self, data):

        return [obj["id"] for obj in data]    

    def get_titles(self, data):

        return [obj["title"] for obj in data]

    def get_text(self, data):

        return [obj["text"] for obj in data]

    def get_urls(self, data):

        return [obj["url"] for obj in data]

    def get_comments(self, data):

        return [obj["comments"] for obj in data]

    def get_scores(self, data):

        return [obj["score"] for obj in data]

    def get_hackers(self, data):

        return [obj["hacker"] for obj in data]    
