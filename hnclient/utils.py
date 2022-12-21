class Manager:

    # cache settings
    cache_name = "hacker-news-api"
    backend="filesystem"
    use_cache_dir=True

    def post_ids_url(self, story) -> str:
        
        return f"https://hacker-news.firebaseio.com/v0/{story}stories.json"

    def get_post(self, uid) -> str:

        return f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"