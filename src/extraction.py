from src.settings import Manager
from src.request import RequestClient


import pprint as pp


class HackerNewsHandler(Manager):
    def __init__(self):

        super().__init__()

    def get_post_data(self, uids): 

        post_data = []
        for uid in uids:
            data = RequestClient(self.get_post(uid))()

            try:
                post_data.append(
                    {
                        "id":        uid,
                        "url":       data["url"],
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

        pp.pprint(post_data) # testing only

        # sorts dictionary by 'score' in descending order
        return sorted(post_data, key=lambda d: d["score"], reverse=True)


