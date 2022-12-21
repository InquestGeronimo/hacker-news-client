from hnclient.utils import Manager
from hnclient.request import HTTPClient

from typing import List, Dict

class HackerNewsClient(Manager):
    def __init__(
        self, 
        descending: bool = False, 
        disable_cache: bool = False,
    ):

        super().__init__()
        self.descending = descending
        self.disable_cache = disable_cache
        
    def get_payload(self) -> List[Dict]:

        uids = HTTPClient(self.post_ids_url, self.disable_cache)()

        payload = []
        for uid in uids:
            data = HTTPClient(self.get_post(uid), self.disable_cache)()

            try:
                payload.append(
                    {
                        "id":        uid,
                        "title":     data["title"],
                        "text":      data["text"],
                        "url":       data["url"],
                        "comments":  data["descendants"],
                        "score":     data["score"],
                        "time":      data["time"],
                        "author":    data["by"]
                    }
                )

            except KeyError:
                continue

            # sorts dict by "score"
            return sorted(payload, key=lambda d: d["score"], reverse=self.descending)


    def get_item(self, item, data):

        return [obj[item] for obj in data]