import json
import random
from typing import List, Dict

from hnclient.utils import Manager, post_ids_url, get_post
from hnclient.request import HTTPClient


class HackerNewsClient(Manager):

    def __init__(
        self, 
        disable_cache: bool = False,
    ):

        super().__init__()
        self.disable_cache = disable_cache
        
        
    def get_stories(self, story: str="top", descending: bool=False) -> List[Dict]:

        uids = HTTPClient(post_ids_url(story), self.disable_cache)()

        payload = []
        for uid in uids:
            data = HTTPClient(get_post(uid), self.disable_cache)()

            try:
                payload.append(
                    {
                        "id":       uid,
                        "title":    data["title"],
                        "text":     data["text"],
                        "url":      data["url"],
                        "comments": data["descendants"],
                        "score":    data["score"],
                        "time":     data["time"],
                        "author":   data["by"]
                    }
                )

            except KeyError:
                continue

        # sorts dict by "score"
        return sorted(payload, key=lambda d: d["score"], reverse=descending)

    def get_item(self, item: str, data: List[Dict]) -> List:

        return [obj[item] for obj in data]

    def get_random_story(self, data: List[Dict]) -> Dict:

        return random.choice(data)

