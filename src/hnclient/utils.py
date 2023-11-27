from typing import Dict

class CacheManager:
    """
    Manager for caching settings.

    :param cache_name: Name of the cache.
    :param backend: Backend for the cache (e.g., "filesystem").
    :param use_cache_dir: Use a cache directory if True.
    """

    # Default cache settings
    cache_name = "hacker-news-api"
    backend = "filesystem"
    use_cache_dir = True

class DataProcessor:
    """
    Helper class for processing Hacker News API data.

    This class provides methods for constructing API URLs, creating payload 
    dictionaries, and sorting data.

    :param story: The type of story to retrieve (e.g., "top").
    """

    def get_story_ids(self, story: str) -> str:
        """
        Construct the URL for retrieving story IDs.

        :param story: The type of story to retrieve (e.g., "top").
        :return: The constructed URL.
        """
        return f"https://hacker-news.firebaseio.com/v0/{story}stories.json"

    def get_story(self, uid: str) -> str:
        """
        Construct the URL for retrieving a story.

        :param uid: The unique identifier of the story.
        :return: The constructed URL.
        """
        return f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"

    def create_payload_dict(self, uid: str, data: Dict) -> Dict:
        """
        Create a payload dictionary from story data.

        :param uid: The unique identifier of the story.
        :param data: The data retrieved from the API.
        :return: A dictionary containing story information.
        """
        return {
            "id": uid,
            "title": data["title"],
            "text": data.get("text", ""),
            "url": data.get("url", ""),
            "comments": data["descendants"],
            "score": data["score"],
            "time": data["time"],
            "author": data["by"]
        }

    def sort_score(self, payload, descending):
        """
        Sort a list of story dictionaries by score.

        :param payload: List of story dictionaries.
        :param descending: Sort in descending order if True.
        :return: Sorted list of story dictionaries.
        """
        return sorted(payload, key=lambda d: d["score"], reverse=descending)
