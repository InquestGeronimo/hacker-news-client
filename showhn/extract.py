from showhn.utils import Manager
from showhn.request import HTTPClient
import pprint as pp


class ShowHN(Manager):
    def __init__(self):

        super().__init__()

    def get_posts(self):

        uids = HTTPClient(self.post_ids_url)()

        post_data = []
        for uid in uids:
            data = HTTPClient(self.get_post(uid))()

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