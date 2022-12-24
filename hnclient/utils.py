from typing import Dict

class Manager:

    # cache settings
    cache_name = "hacker-news-api"
    backend="filesystem"
    use_cache_dir=True

    def story_ids(self, story: str) -> str:
        
        return f"https://hacker-news.firebaseio.com/v0/{story}stories.json"

    def get_story(self, uid: str) -> str:

        return f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"

    def payload_dict(self, uid: str, data: Dict) -> Dict:

        return {
            "id":       uid,
            "title":    data["title"],
            "text":     data["text"],
            "url":      data["url"],
            "comments": data["descendants"],
            "score":    data["score"],
            "time":     data["time"],
            "author":   data["by"]
        }