import random
from typing import List, Dict
from .set_api import HTTPHandler

class HackerNewsClient(HTTPHandler):
    """
    A client for interacting with the Hacker News API.

    :param disable_cache: Set to True to disable caching.
    """

    def __init__(self, disable_cache: bool = False):
        """
        Initialize a new HackerNewsClient.

        :param disable_cache: Set to True to disable caching.
        """
        super().__init__()
        self.disable_cache = disable_cache

    def get_stories(self, story: str = "top", descending: bool = False) -> List[Dict]:
        """
        Get a list of Hacker News stories.

        :param story: The type of story to retrieve (e.g., "top").
        :param descending: Sort stories by score in descending order if True.
        :return: List of story dictionaries.
        """
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
        """
        Extract a specific item from a list of dictionaries.

        :param item: Key to extract from each dictionary.
        :param data: List of dictionaries.
        :return: List of extracted items.
        """
        return [obj[item] for obj in data]

    @staticmethod
    def get_random_story(data: List[Dict]) -> Dict:
        """
        Get a random story from a list of stories.

        :param data: List of story dictionaries.
        :return: Random story dictionary.
        """
        return random.choice(data)

