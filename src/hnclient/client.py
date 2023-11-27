import random
from typing import List, Dict
from .set_api import HTTPHandler

class HackerNewsClient(HTTPHandler):
    def __init__(self, disable_cache: bool = False):
        super().__init__()
        self.disable_cache = disable_cache

    def get_stories(self, story: str = "top", descending: bool = False) -> List[Dict]:
        payload = []
        story_ids = self.call_api(self.get_story_ids(story), self.disable_cache)

        for uid in story_ids:
            data = self.call_api(self.get_story(uid), self.disable_cache)
            try:
                payload.append(self.create_payload_dict(uid, data))
            except KeyError:
                continue

        return self.sort_score(payload, descending)

    @staticmethod
    def get_item(item: str, data: List[Dict]) -> List:
        return [obj[item] for obj in data]

    @staticmethod
    def get_random_story(data: List[Dict]) -> Dict:
        return random.choice(data)
