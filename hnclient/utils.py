class Manager:

    post_ids_url = "https://hacker-news.firebaseio.com/v0/showstories.json"

    # cache settings
    cache_name = "hacker-news-api"
    backend="filesystem"
    use_cache_dir=True

    def get_post(self, uid):

        return f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"