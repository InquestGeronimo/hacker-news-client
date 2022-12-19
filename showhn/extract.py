from showhn.utils import Manager
from showhn.request import HTTPClient

from typing import List, Dict
import pprint

class ShowHN(Manager):
    def __init__(
        self, 
        descending: bool = False, 
        disable_cache: bool = False, 
        pretty: bool = True
    ):

        super().__init__()
        self.descending = descending
        self.disable_cache = disable_cache
        self.pretty = pretty
        
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

        if self.pretty:
            return pprint.pformat(sorted(payload, key=lambda d: d["score"], reverse=self.descending))
        else:
            return sorted(payload, key=lambda d: d["score"], reverse=self.descending)

    def get_item(self, item, data):

        return [obj[item] for obj in data]