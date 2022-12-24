import json
import random
from typing import List, Dict

from hnclient.set_api import HTTPHandler

class HackerNewsClient(HTTPHandler):

    def __init__(self, disable_cache: bool = False):

        self.disable_cache = disable_cache

    def get_stories(self, story: str="top", descending: bool=False) -> List[Dict]:

        payload = []
        for uid in self.call_api(self.story_ids(story), self.disable_cache):
            data = self.call_api(self.get_story(uid), self.disable_cache)
      
            try:
                payload.append(self.payload_dict(uid, data))
                
            except KeyError:
                continue

        # sorts dict by "score"
        return sorted(payload, key=lambda d: d["score"], reverse=descending)

    def get_item(self, item: str, data: List[Dict]) -> List:

        return [obj[item] for obj in data]

    def get_random_story(self, data: List[Dict]) -> Dict:

        return random.choice(data)

