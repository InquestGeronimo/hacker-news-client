class Manager:

    post_ids_url = "https://hacker-news.firebaseio.com/v0/showstories.json"

    def get_post(self, uid):

        return f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"