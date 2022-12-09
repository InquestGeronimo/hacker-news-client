import requests


class RequestClient:

    def __init__(self, url):
        self.url = url

    def __call__(self):
        
        response = requests.get(self.url)
        return response.json()

class HackerNewsHandler:

    def get_post_data(self, uids):  
    
        post_data = []
        for uid in uids:
            data = RequestClient(f"https://hacker-news.firebaseio.com/v0/item/{uid}.json")()

            try:
                post_data.append(
                    {
                        "id":        uid,
                        "title":     data["title"],
                        "text":      data["text"][:135] + "...",
                        "comments":  data["descendants"],
                        "score":     data["score"],
                        "time":      data["time"],
                        "hacker":    data["by"]
                    }
                )

            except KeyError:
                continue

        #Sorts dictionary by 'score' in descending order
        return sorted(post_data, key=lambda d: d["score"], reverse=True)

# posts = RequestClient(post_ids_url)
# HN = HackerNewsHandler()
# post_ids = HN.get_post_data(posts())
# search = HN.sort_data(post_ids)